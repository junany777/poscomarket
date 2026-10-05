from datetime import datetime, timezone
from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import SourceNotFound, InvalidEvidence
from app.models.entities import AIRun, Company, Event, EventCluster, Evidence, Opportunity, ProductMatch, RecommendedAction, SourceDocument, SteelDemandHypothesis, StrategyInference
from app.services.opportunity import opportunity_level, score_opportunity
from app.services.product_brain.router import route_product_knowledge
from app.services.product_brain.loader import load_routed_products
from app.services.taxonomy import validate_code
from app.services.evidence import require_evidence_quote
from app.services.intelligence.event_clustering import assign_event_to_cluster
import re


def _company(db: Session, content: str) -> Company | None:
    lowered = content.lower()
    names = [("Hyundai Motor", "현대자동차", "AUTOMOTIVE"), ("Samsung Electronics", "삼성전자", "SEMICONDUCTOR"), ("HD Hyundai", "HD현대", "SHIPBUILDING")]
    for english, korean, industry in names:
        if english.lower() in lowered or korean in content:
            existing = db.scalar(select(Company).where(Company.normalized_name == english.lower()))
            if existing: return existing
            item = Company(name=english, normalized_name=english.lower(), industry_code=industry, country="KR")
            db.add(item); db.flush(); return item
    return None


def run_intelligence_pipeline(db: Session, source_document_id: str) -> dict:
    source = db.get(SourceDocument, source_document_id)
    if not source: raise SourceNotFound(f"Source {source_document_id} was not found")
    cache_key = sha256(f"DETERMINISTIC_MVP_PIPELINE|{source.content_hash}|pipeline-v1|rules-v1".encode()).hexdigest()
    prior = db.scalar(select(AIRun).where(AIRun.cache_key == cache_key, AIRun.status.in_(["SUCCESS", "CACHE_HIT"])).order_by(AIRun.created_at.desc()))
    if not prior:
        prior = db.scalar(select(AIRun).where(AIRun.input_reference == source_document_id, AIRun.status == "SUCCESS").order_by(AIRun.created_at.desc()))
    if prior and isinstance(prior.output_json, dict) and prior.output_json.get("result"):
        now = datetime.now(timezone.utc).isoformat()
        db.add(AIRun(run_type="DETERMINISTIC_MVP_PIPELINE", model="deterministic", prompt_version="deterministic-mvp", input_reference=source_document_id, output_json={"result": prior.output_json["result"], "cache": {"hit": True, "reused_from_id": prior.id}}, status="CACHE_HIT", started_at=now, completed_at=now, cache_key=cache_key, cache_hit=True, reused_from_id=prior.id))
        db.commit()
        return prior.output_json["result"]
    started = datetime.now(timezone.utc).isoformat()
    content = source.content
    company = _company(db, content)
    quote = content[: min(len(content), 240)].strip()
    require_evidence_quote(content, quote)
    evidence = Evidence(source_document_id=source.id, evidence_type="DIRECT_QUOTE", quote_text=quote, start_offset=0, end_offset=len(quote), confidence=.86)
    db.add(evidence); db.flush()
    lowered = content.lower()
    event_type = "CAPACITY_EXPANSION" if any(k in lowered for k in ("expand", "expansion", "증설", "확대", "capacity")) else "CAPEX"
    event_type = validate_code("event", event_type)
    is_ev = any(k in content.lower() for k in ("ev", "electric vehicle", "traction motor", "전기차", "모터"))
    application = "EV_MOTOR" if is_ev else "VEHICLE_BODY"
    component = "MOTOR_CORE" if is_ev else "STRUCTURAL_MEMBER"
    numeric_facts = {}
    investment = re.search(r"(?:\$|USD\s*)([0-9]+(?:\.[0-9]+)?)\s*(billion|million|bn|m)?", content, re.I)
    if investment:
        numeric_facts["investment_amount"] = investment.group(0)
    capacity = re.search(r"([0-9][0-9,]*)\s*(?:units|vehicles|tons|tonnes|대|톤)", content, re.I)
    if capacity:
        numeric_facts["capacity"] = capacity.group(0)
    event = Event(company_id=company.id if company else None, source_document_id=source.id, primary_event_type=event_type, secondary_event_types_json=[], status="VALIDATED", title=source.title, summary=f"Structured event extracted from {source.source_name}.", confidence=.86, metadata_json={"application": application, "component": component, "numeric_facts": numeric_facts, "source_authority": (source.metadata_json or {}).get("source_authority", "SECONDARY")})
    db.add(event); db.flush()
    cluster_decision = assign_event_to_cluster(db, event, source)
    if cluster_decision.decision == "AUTO_CLUSTER" and cluster_decision.cluster_id:
        cluster_event_id = db.get(EventCluster, cluster_decision.cluster_id).canonical_event_id
        existing_opportunity = db.scalar(select(Opportunity).where(Opportunity.event_id == cluster_event_id)) if cluster_event_id else None
        if existing_opportunity:
            source.status = "PROCESSED"
            db.commit()
            return {"source_id": source.id, "event": {"id": event.id, "cluster_id": cluster_decision.cluster_id, "decision": cluster_decision.decision}, "deduplicated": True, "opportunity": {"id": existing_opportunity.id, "score": existing_opportunity.score}}
    strategy_code = "ELECTRIFICATION" if any(k in lowered for k in ("ev", "electric", "전기차", "traction motor")) else "GROWTH"
    strategy_code = validate_code("strategy", strategy_code)
    strategy = StrategyInference(event_id=event.id, strategy_code=strategy_code, reasoning_summary="The source indicates a business-capability change consistent with this strategy.", confidence=.78, evidence_ids_json=[evidence.id])
    db.add(strategy); db.flush()
    material_category = validate_code("material", "NON_ORIENTED_ELECTRICAL_STEEL" if is_ev else "AUTOMOTIVE_STEEL")
    demand = SteelDemandHypothesis(event_id=event.id, industry_code="AUTOMOTIVE" if is_ev else (company.industry_code if company else "AUTOMOTIVE"), application_code=application, component_code=component, material_requirements_json=["LOW_CORE_LOSS", "HIGH_MECHANICAL_STRENGTH"] if is_ev else ["HIGH_STRENGTH", "FORMABILITY"], material_category=material_category, demand_direction="INCREASE", reasoning_summary="Industry change maps to application, component and material requirements before product routing.", confidence=.74)
    db.add(demand); db.flush()
    route = route_product_knowledge(demand.industry_code, application, component, demand.material_requirements_json)
    loaded_products = load_routed_products(route, max_files=1)
    if route.knowledge_files and not loaded_products:
        route.product_family = None
        route.knowledge_files = []
        route.confidence = 0.0
        route.reason = "PRODUCT_KNOWLEDGE_PENDING"
    product = ProductMatch(steel_demand_hypothesis_id=demand.id, product_family=route.product_family, product_file=route.knowledge_files[0] if route.knowledge_files else None, candidate_series_json=[], candidate_grades_json=[], match_score=88 if route.confidence > .8 else 60, confidence=route.confidence, reasoning_summary=route.reason, status="MATCHED" if route.product_family else "UNKNOWN")
    db.add(product); db.flush()
    score = score_opportunity(92, 88, 80, 90, 92 if route.product_family else 45, 85)
    opportunity = Opportunity(company_id=company.id if company else None, event_id=event.id, product_match_id=product.id, title=f"{source.title} · steel opportunity", opportunity_type="DEMAND_GROWTH", summary=f"{route.product_family or 'Product knowledge pending'} candidate connected to the extracted demand hypothesis.", score=score["total"], score_breakdown_json=score, confidence=round(min(.95, (evidence.confidence + event.confidence + route.confidence) / 3), 2) * 100, status="NEW")
    db.add(opportunity); db.flush()
    actions = [RecommendedAction(opportunity_id=opportunity.id, action_type="CUSTOMER_ENGAGEMENT", description="Confirm target component, production start date and current material.", priority="HIGH"), RecommendedAction(opportunity_id=opportunity.id, action_type="TECHNICAL", description="Confirm thickness, required strength and qualification status.", priority="MEDIUM")]
    for action in actions: db.add(action)
    now = datetime.now(timezone.utc).isoformat()
    result = {"source_id": source.id, "event": {"id": event.id, "type": event.primary_event_type, "confidence": event.confidence, "cluster_id": event.event_cluster_id}, "strategy": {"id": strategy.id, "code": strategy.strategy_code, "confidence": strategy.confidence}, "steel_demand": {"id": demand.id, "application": demand.application_code, "component": demand.component_code, "material_category": demand.material_category, "material_requirements": demand.material_requirements_json, "industry": demand.industry_code}, "product_match": {"id": product.id, "product_family": product.product_family, "product_file": product.product_file, "candidate_series": product.candidate_series_json, "candidate_grades": product.candidate_grades_json, "status": product.status, "confidence": product.confidence}, "opportunity": {"id": opportunity.id, "score": opportunity.score, "score_breakdown": score, "level": opportunity_level(opportunity.score), "confidence": opportunity.confidence}, "actions": [{"id": a.id, "description": a.description, "priority": a.priority} for a in actions]}
    db.add(AIRun(run_type="DETERMINISTIC_MVP_PIPELINE", model="deterministic", prompt_version="deterministic-mvp", input_reference=source.id, output_json={"event": event.id, "opportunity": opportunity.id, "result": result}, status="SUCCESS", started_at=started, completed_at=now, cache_key=cache_key, cache_hit=False))
    db.commit()
    try:
        from app.services.alerts.service import evaluate_event_cluster, evaluate_opportunity
        evaluate_opportunity(db, opportunity.id)
        if event.event_cluster_id:
            evaluate_event_cluster(db, event.event_cluster_id)
    except Exception:
        # Alert evaluation must never roll back a committed intelligence result.
        pass
    return result
