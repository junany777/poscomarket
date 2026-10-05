from datetime import datetime, timezone
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
from uuid import uuid4
import logging
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.core.database import get_db, init_db
from app.core.exceptions import ApplicationError
from app.models.entities import Alert, AlertDelivery, AlertDeliverySubscription, CollectionRun, Company, DeliveryChannel, DigestDelivery, DigestSubscription, EvaluationCaseResult, EvaluationRun, Evidence, Event, EventCluster, EventClusterDecisionLog, HumanEvaluation, IntelligenceDigest, Opportunity, PerformanceBenchmark, ProductMatch, PromptChange, RecommendedAction, SourceDocument, SteelDemandHypothesis, StrategyInference, TuningCandidate, ValidationRun, ValidationRunSource, ValidationStage, WatchRule, Watchlist
from app.schemas import Envelope, OpportunityRead, PipelineResult, SourceCreate, SourceRead
from app.services.ingestion import collect_sources, create_source, list_registry_sources
from app.services.pipeline import run_intelligence_pipeline
from app.services.intelligence.event_clustering import merge_clusters
from app.services.evaluation.runner import run_evaluation
from app.services.evaluation.comparison import compare_summaries
from app.services.ask_steel import ask_steel
from app.services.alerts.matcher import match_watchlist
from app.services.alerts.service import evaluate_event_cluster, evaluate_opportunity, validate_rule
from app.services.ask_steel.retrieval import get_opportunity_context
from app.services.delivery import enqueue_alert, process_digest_pending, process_pending
from app.services.delivery.service import enqueue_digest
from app.services.delivery.channels.telegram import TelegramAdapter
from app.services.delivery.base import DeliveryMessage
from app.services.digest import generate_digest
from app.services.operations.metrics import ai_runs as operations_ai_runs, collection as operations_collection, delivery as operations_delivery, digest as operations_digest, knowledge_gaps as operations_knowledge_gaps, pipeline as operations_pipeline, quality as operations_quality
from app.services.operations.overview import admin_overview
from app.services.operations.health import component_health, overall_status
from app.services.operations.recovery import reprocess_source
from app.services.validation.runner import run_validation
from app.services.performance.service import benchmark_validation
from app.core.config import settings
from app.core.deployment import check_required_knowledge_files, validate_runtime_config
from app.services.dart import DartClient

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO), format="%(asctime)s %(levelname)s %(message)s")
app = FastAPI(title="Steel Market Intelligence API", version=settings.app_version)
if settings.app_env.lower() in {"staging", "production"}:
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=[item.strip() for item in settings.allowed_hosts.split(",") if item.strip()])
app.add_middleware(CORSMiddleware, allow_origins=[item.strip() for item in settings.cors_allowed_origins.split(",") if item.strip()], allow_credentials=False, allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"], allow_headers=["*"])


@app.middleware("http")
async def request_context(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or str(uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "same-origin"
    return response


def _period(value: str | None) -> str:
    value = (value or "24h").lower()
    if value not in {"24h", "7d", "30d"}: raise HTTPException(422, "period must be 24h, 7d or 30d")
    return value


@app.get("/api/v1/dart/health", response_model=Envelope)
async def dart_health_route() -> Envelope:
    return Envelope(data=await DartClient().health())


@app.get("/api/v1/dart/disclosures", response_model=Envelope)
async def dart_disclosures_route(bgn_de: str | None = None, end_de: str | None = None, corp_code: str | None = None, industry: str | None = None, page: int = Query(1, ge=1), page_count: int = Query(100, ge=1, le=100)) -> Envelope:
    return Envelope(data=await DartClient().disclosures(bgn_de, end_de, corp_code, industry, page, page_count))


@app.get("/api/v1/dart/analysis", response_model=Envelope)
async def dart_analysis_route(bgn_de: str | None = None, end_de: str | None = None) -> Envelope:
    return Envelope(data=await DartClient().analysis(bgn_de, end_de))


@app.get("/api/v1/admin/overview", response_model=Envelope)
def admin_overview_route(period: str = "24h", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=admin_overview(db, _period(period)))


@app.get("/api/v1/admin/health", response_model=Envelope)
def admin_health_route(db: Session = Depends(get_db)) -> Envelope:
    components = component_health(db)
    return Envelope(data={"system_status": overall_status(components), "components": components})


@app.get("/api/v1/admin/collection", response_model=Envelope)
def admin_collection_route(period: str = "24h", source: str | None = None, status: str | None = None, db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_collection(db, _period(period), source, status))


@app.get("/api/v1/admin/pipeline", response_model=Envelope)
def admin_pipeline_route(period: str = "24h", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_pipeline(db, _period(period)))


@app.get("/api/v1/admin/ai-runs", response_model=Envelope)
def admin_ai_route(period: str = "24h", run_type: str | None = None, model: str | None = None, status: str | None = None, db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_ai_runs(db, _period(period), run_type, model, status))


@app.get("/api/v1/admin/knowledge-gaps", response_model=Envelope)
def admin_knowledge_gaps_route(period: str = "30d", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_knowledge_gaps(db, _period(period)))


@app.get("/api/v1/admin/delivery", response_model=Envelope)
def admin_delivery_route(period: str = "24h", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_delivery(db, _period(period)))


@app.get("/api/v1/admin/digest", response_model=Envelope)
def admin_digest_route(period: str = "30d", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_digest(db, _period(period)))


@app.get("/api/v1/admin/quality", response_model=Envelope)
def admin_quality_route(period: str = "30d", db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data=operations_quality(db, _period(period)))


@app.post("/api/v1/admin/sources/{source_id}/reprocess", response_model=Envelope)
def admin_reprocess_source_route(source_id: str, db: Session = Depends(get_db)) -> Envelope:
    try:
        return Envelope(data=reprocess_source(db, source_id))
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc


@app.post("/api/v1/validation-runs", response_model=Envelope)
def create_validation_run(payload: dict | None = None, db: Session = Depends(get_db)) -> Envelope:
    payload = payload or {}
    result = run_validation(db, source_limit=min(int(payload.get("source_limit", 100)), 100), source_ids=payload.get("source_ids"), real_collection=bool(payload.get("real_collection", False)), source_codes=payload.get("source_codes"), delivery_dry_run=bool(payload.get("delivery_dry_run", True)), name=payload.get("name", "Controlled E2E Validation"))
    return Envelope(data={"id": result["id"], "status": result["status"], "summary": result["summary"]})


@app.get("/api/v1/validation-runs", response_model=Envelope)
def list_validation_runs(limit: int = Query(20, ge=1, le=100), db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(ValidationRun).order_by(desc(ValidationRun.created_at)).limit(limit)))
    return Envelope(data=[{"id": row.id, "name": row.name, "status": row.status, "started_at": row.started_at, "completed_at": row.completed_at, "source_document_count": row.source_document_count, "opportunity_count": row.opportunity_count, "summary": row.summary_json} for row in rows])


@app.get("/api/v1/validation-runs/{run_id}", response_model=Envelope)
def validation_run_detail(run_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(ValidationRun, run_id)
    if not row: raise HTTPException(404, "validation run not found")
    sources = list(db.scalars(select(ValidationRunSource).where(ValidationRunSource.validation_run_id == run_id)))
    stages = list(db.scalars(select(ValidationStage).where(ValidationStage.validation_run_id == run_id).order_by(ValidationStage.created_at)))
    return Envelope(data={"id": row.id, "name": row.name, "status": row.status, "started_at": row.started_at, "completed_at": row.completed_at, "counts": {"sources": row.source_document_count, "events": row.event_count, "clusters": row.cluster_count, "opportunities": row.opportunity_count, "alerts": row.alert_count, "deliveries": row.delivery_count, "digests": row.digest_count}, "summary": row.summary_json, "sources": [{"source_document_id": item.source_document_id, "review_status": item.review_status, "review": item.review_json} for item in sources], "stages": [{"stage": item.stage, "input_count": item.input_count, "success_count": item.success_count, "failure_count": item.failure_count, "skipped_count": item.skipped_count, "duration_ms": item.duration_ms, "errors": item.errors_json} for item in stages]})


@app.post("/api/v1/performance/benchmarks", response_model=Envelope)
def create_performance_benchmark(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    try: return Envelope(data=benchmark_validation(db, payload.get("validation_run_id"), payload.get("name")))
    except ValueError as exc: raise HTTPException(422, str(exc)) from exc


@app.get("/api/v1/performance/benchmarks", response_model=Envelope)
def list_performance_benchmarks(limit: int = Query(20, ge=1, le=100), db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(PerformanceBenchmark).order_by(desc(PerformanceBenchmark.created_at)).limit(limit)))
    return Envelope(data=[{"id": row.id, "name": row.name, "validation_run_id": row.validation_run_id, "started_at": row.started_at, "completed_at": row.completed_at, "metrics": row.metrics_json} for row in rows])


@app.post("/api/v1/ask", response_model=Envelope)
def ask_steel_route(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    question, mode = payload.get("question"), payload.get("mode", "STANDARD")
    if not question: raise HTTPException(422, "question is required")
    if mode not in {"BRIEF", "STANDARD", "DETAILED"}: raise HTTPException(422, "mode must be BRIEF, STANDARD or DETAILED")
    try:
        result = ask_steel(db, question, mode)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    return Envelope(data=result, meta=result.pop("meta", {}))


@app.post("/api/v1/digests/generate", response_model=Envelope)
def generate_digest_route(payload: dict | None = None, db: Session = Depends(get_db)) -> Envelope:
    payload = payload or {}
    try:
        parse = lambda value: datetime.fromisoformat(value.replace("Z", "+00:00")) if isinstance(value, str) else value
        result = generate_digest(db, payload.get("digest_type", "DAILY"), parse(payload.get("period_start")), parse(payload.get("period_end")))
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    if result.get("id") and not result.get("deduplicated"):
        try: enqueue_digest(db, result["id"])
        except Exception: pass
    return Envelope(data=result)


@app.get("/api/v1/digests", response_model=Envelope)
def list_digests(digest_type: str | None = None, status: str | None = None, limit: int = Query(50, ge=1, le=100), db: Session = Depends(get_db)) -> Envelope:
    query = select(IntelligenceDigest).order_by(desc(IntelligenceDigest.period_end)).limit(limit)
    if digest_type: query = query.where(IntelligenceDigest.digest_type == digest_type.upper())
    if status: query = query.where(IntelligenceDigest.status == status.upper())
    rows = list(db.scalars(query))
    return Envelope(data=[{"id": row.id, "digest_type": row.digest_type, "period_start": row.period_start, "period_end": row.period_end, "title": row.title, "status": row.status, "event_count": row.event_count, "opportunity_count": row.opportunity_count, "high_priority_count": row.high_priority_count, "generated_at": row.generated_at} for row in rows])


@app.get("/api/v1/digests/{digest_id}", response_model=Envelope)
def digest_detail(digest_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(IntelligenceDigest, digest_id)
    if not row: raise HTTPException(404, "digest not found")
    return Envelope(data={"id": row.id, "digest_type": row.digest_type, "period_start": row.period_start, "period_end": row.period_end, "title": row.title, "executive_summary": row.executive_summary, "status": row.status, "event_count": row.event_count, "opportunity_count": row.opportunity_count, "high_priority_count": row.high_priority_count, "content": row.content_json, "generated_at": row.generated_at, "deliveries": [{"id": item.id, "delivery_channel_id": item.delivery_channel_id, "status": item.status, "attempt_count": item.attempt_count, "delivered_at": item.delivered_at} for item in db.scalars(select(DigestDelivery).where(DigestDelivery.digest_id == row.id))]})


@app.post("/api/v1/digests/{digest_id}/regenerate", response_model=Envelope)
def regenerate_digest(digest_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(IntelligenceDigest, digest_id)
    if not row: raise HTTPException(404, "digest not found")
    result = generate_digest(db, row.digest_type, row.period_start, row.period_end)
    return Envelope(data=result)


@app.post("/api/v1/digest-subscriptions", response_model=Envelope)
def create_digest_subscription(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    digest_type = str(payload.get("digest_type", "DAILY")).upper()
    channel_id = payload.get("delivery_channel_id")
    if digest_type not in {"DAILY", "WEEKLY"}: raise HTTPException(422, "digest_type must be DAILY or WEEKLY")
    channel = db.get(DeliveryChannel, channel_id)
    if not channel: raise HTTPException(422, "delivery channel not found")
    row = DigestSubscription(delivery_channel_id=channel.id, digest_type=digest_type, enabled=payload.get("enabled", True), minimum_opportunity_score=payload.get("minimum_opportunity_score"), industries_json=payload.get("industries", []), product_families_json=payload.get("product_families", []))
    db.add(row); db.commit(); db.refresh(row)
    return Envelope(data={"id": row.id, "delivery_channel_id": row.delivery_channel_id, "digest_type": row.digest_type, "enabled": row.enabled, "minimum_opportunity_score": row.minimum_opportunity_score, "industries": row.industries_json, "product_families": row.product_families_json})


@app.get("/api/v1/digest-subscriptions", response_model=Envelope)
def list_digest_subscriptions(db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(DigestSubscription).order_by(desc(DigestSubscription.created_at))))
    return Envelope(data=[{"id": row.id, "delivery_channel_id": row.delivery_channel_id, "digest_type": row.digest_type, "enabled": row.enabled, "minimum_opportunity_score": row.minimum_opportunity_score, "industries": row.industries_json, "product_families": row.product_families_json} for row in rows])


@app.patch("/api/v1/digest-subscriptions/{subscription_id}", response_model=Envelope)
def update_digest_subscription(subscription_id: str, payload: dict, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DigestSubscription, subscription_id)
    if not row: raise HTTPException(404, "digest subscription not found")
    if "enabled" in payload: row.enabled = bool(payload["enabled"])
    if "minimum_opportunity_score" in payload: row.minimum_opportunity_score = payload["minimum_opportunity_score"]
    if "industries" in payload: row.industries_json = payload["industries"]
    if "product_families" in payload: row.product_families_json = payload["product_families"]
    db.commit(); return Envelope(data={"id": row.id, "enabled": row.enabled})


@app.delete("/api/v1/digest-subscriptions/{subscription_id}", response_model=Envelope)
def delete_digest_subscription(subscription_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DigestSubscription, subscription_id)
    if not row: raise HTTPException(404, "digest subscription not found")
    row.enabled = False; db.commit(); return Envelope(data={"id": row.id, "enabled": False})


@app.post("/api/v1/watchlists", response_model=Envelope)
def create_watchlist(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    if not payload.get("name"): raise HTTPException(422, "name is required")
    watchlist = Watchlist(name=payload["name"], description=payload.get("description"), enabled=payload.get("enabled", True), user_id=payload.get("user_id"))
    db.add(watchlist); db.flush()
    try:
        rules = []
        for item in payload.get("rules", []):
            rule = validate_rule(item, db); rules.append(WatchRule(watchlist_id=watchlist.id, rule_type=rule["dimension"], operator=rule["operator"], value_json=rule["value"], enabled=True))
        db.add_all(rules); db.commit(); db.refresh(watchlist)
    except ValueError as exc:
        db.rollback(); raise HTTPException(422, str(exc)) from exc
    return Envelope(data={"id": watchlist.id, "name": watchlist.name, "enabled": watchlist.enabled, "rules": [{"dimension": rule.rule_type, "operator": rule.operator, "value": rule.value_json} for rule in rules]})


@app.get("/api/v1/watchlists", response_model=Envelope)
def list_watchlists(db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(Watchlist).order_by(desc(Watchlist.created_at))))
    data = []
    for row in rows:
        rules = list(db.scalars(select(WatchRule).where(WatchRule.watchlist_id == row.id)))
        latest = db.scalar(select(Alert).where(Alert.watchlist_id == row.id).order_by(desc(Alert.created_at)))
        data.append({"id": row.id, "name": row.name, "description": row.description, "enabled": row.enabled, "rules": [{"dimension": item.rule_type, "operator": item.operator, "value": item.value_json} for item in rules], "latest_alert": latest.created_at if latest else None})
    return Envelope(data=data)


@app.get("/api/v1/watchlists/{watchlist_id}", response_model=Envelope)
def watchlist_detail(watchlist_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Watchlist, watchlist_id)
    if not row: raise HTTPException(404, "Watchlist not found")
    rules = list(db.scalars(select(WatchRule).where(WatchRule.watchlist_id == row.id)))
    alerts = list(db.scalars(select(Alert).where(Alert.watchlist_id == row.id).order_by(desc(Alert.created_at)).limit(20)))
    return Envelope(data={"id": row.id, "name": row.name, "description": row.description, "enabled": row.enabled, "rules": [{"id": item.id, "dimension": item.rule_type, "operator": item.operator, "value": item.value_json, "enabled": item.enabled} for item in rules], "match_count": len(alerts), "recent_alerts": [{"id": item.id, "title": item.title, "priority": item.priority, "status": item.status, "created_at": item.created_at} for item in alerts]})


@app.patch("/api/v1/watchlists/{watchlist_id}", response_model=Envelope)
def update_watchlist(watchlist_id: str, payload: dict, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Watchlist, watchlist_id)
    if not row: raise HTTPException(404, "Watchlist not found")
    if "name" in payload: row.name = payload["name"]
    if "description" in payload: row.description = payload["description"]
    if "enabled" in payload: row.enabled = bool(payload["enabled"])
    if "rules" in payload:
        new_rules = []
        try:
            for item in payload["rules"]:
                rule = validate_rule(item, db); new_rules.append(WatchRule(watchlist_id=row.id, rule_type=rule["dimension"], operator=rule["operator"], value_json=rule["value"], enabled=True))
        except ValueError as exc:
            db.rollback(); raise HTTPException(422, str(exc)) from exc
        for old in db.scalars(select(WatchRule).where(WatchRule.watchlist_id == row.id)): db.delete(old)
        db.add_all(new_rules)
    db.commit()
    return Envelope(data={"id": row.id, "name": row.name, "enabled": row.enabled})


@app.delete("/api/v1/watchlists/{watchlist_id}", response_model=Envelope)
def delete_watchlist(watchlist_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Watchlist, watchlist_id)
    if not row: raise HTTPException(404, "Watchlist not found")
    row.enabled = False; db.commit()
    return Envelope(data={"id": row.id, "enabled": False})


@app.post("/api/v1/watchlists/{watchlist_id}/test", response_model=Envelope)
def test_watchlist(watchlist_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Watchlist, watchlist_id)
    if not row: raise HTTPException(404, "Watchlist not found")
    rules = list(db.scalars(select(WatchRule).where(WatchRule.watchlist_id == row.id, WatchRule.enabled)))
    examples = []
    for opportunity in db.scalars(select(Opportunity).order_by(desc(Opportunity.created_at)).limit(100)):
        from app.services.alerts.service import _context
        values, cluster = _context(db, opportunity=opportunity)
        result = match_watchlist(row, rules, values)
        if result["matched"]: examples.append({"opportunity_id": opportunity.id, "title": opportunity.title, "score": opportunity.score, "match_reason": {"matched_rules": result["matched_rules"]}})
        if len(examples) >= 20: break
    return Envelope(data={"matches": len(examples), "examples": examples})


@app.get("/api/v1/alerts", response_model=Envelope)
def list_alerts(status: str | None = None, priority: str | None = None, watchlist_id: str | None = None, product_family: str | None = None, company: str | None = None, limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), db: Session = Depends(get_db)) -> Envelope:
    query = select(Alert).order_by(desc(Alert.created_at)).offset(offset).limit(limit)
    if status: query = query.where(Alert.status == status.upper())
    if priority: query = query.where(Alert.priority == priority.upper())
    if watchlist_id: query = query.where(Alert.watchlist_id == watchlist_id)
    rows = list(db.scalars(query))
    data = []
    for row in rows:
        opportunity = db.get(Opportunity, row.opportunity_id) if row.opportunity_id else None
        product = db.get(ProductMatch, opportunity.product_match_id) if opportunity and opportunity.product_match_id else None
        event = db.get(Event, opportunity.event_id) if opportunity else None
        company_obj = db.get(Company, event.company_id) if event and event.company_id else None
        if product_family and (not product or product.product_family != product_family.upper()): continue
        if company and (not company_obj or company_obj.normalized_name != company.lower()): continue
        data.append({"id": row.id, "watchlist_id": row.watchlist_id, "title": row.title, "summary": row.summary, "priority": row.priority, "status": row.status, "alert_type": row.alert_type, "opportunity_id": row.opportunity_id, "event_cluster_id": row.event_cluster_id, "product_family": product.product_family if product else None, "company": company_obj.name if company_obj else None, "score": opportunity.score if opportunity else None, "created_at": row.created_at, "match_reason": row.match_reason_json})
    return Envelope(data=data, meta={"count": len(data), "limit": limit, "offset": offset})


@app.get("/api/v1/alerts/unread-count", response_model=Envelope)
def unread_alert_count(db: Session = Depends(get_db)) -> Envelope:
    return Envelope(data={"count": len(list(db.scalars(select(Alert).where(Alert.status == "NEW"))))})


@app.get("/api/v1/alerts/{alert_id}", response_model=Envelope)
def alert_detail(alert_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Alert, alert_id)
    if not row: raise HTTPException(404, "Alert not found")
    watchlist = db.get(Watchlist, row.watchlist_id)
    context = get_opportunity_context(db, row.opportunity_id) if row.opportunity_id else None
    return Envelope(data={"id": row.id, "title": row.title, "summary": row.summary, "priority": row.priority, "status": row.status, "alert_type": row.alert_type, "watchlist": {"id": watchlist.id, "name": watchlist.name} if watchlist else None, "matched_rules": row.match_reason_json, "rule_snapshot": row.watch_rule_snapshot_json, "opportunity_id": row.opportunity_id, "event_cluster_id": row.event_cluster_id, "evidence": context["evidence"] if context else []})


@app.post("/api/v1/alerts/{alert_id}/read", response_model=Envelope)
def mark_alert_read(alert_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Alert, alert_id)
    if not row: raise HTTPException(404, "Alert not found")
    row.status = "READ"; row.read_at = datetime.now(timezone.utc); db.commit()
    return Envelope(data={"id": row.id, "status": row.status})


@app.post("/api/v1/alerts/{alert_id}/dismiss", response_model=Envelope)
def dismiss_alert(alert_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(Alert, alert_id)
    if not row: raise HTTPException(404, "Alert not found")
    row.status = "DISMISSED"; row.dismissed_at = datetime.now(timezone.utc); db.commit()
    return Envelope(data={"id": row.id, "status": row.status})


@app.post("/api/v1/delivery-channels", response_model=Envelope)
def create_delivery_channel(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    channel_type = str(payload.get("channel_type", "")).upper()
    if channel_type != "TELEGRAM" or not payload.get("name") or not payload.get("config", {}).get("chat_id"):
        raise HTTPException(422, "TELEGRAM channel requires name and config.chat_id")
    row = DeliveryChannel(channel_type=channel_type, name=payload["name"], enabled=payload.get("enabled", True), config_json={"chat_id": str(payload["config"]["chat_id"])})
    db.add(row); db.commit(); db.refresh(row)
    return Envelope(data={"id": row.id, "channel_type": row.channel_type, "name": row.name, "enabled": row.enabled, "config": {"chat_id": row.config_json.get("chat_id")}})


@app.get("/api/v1/delivery-channels", response_model=Envelope)
def list_delivery_channels(db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(DeliveryChannel).order_by(desc(DeliveryChannel.created_at))))
    return Envelope(data=[{"id": row.id, "channel_type": row.channel_type, "name": row.name, "enabled": row.enabled, "config": {"chat_id": row.config_json.get("chat_id")}} for row in rows])


@app.get("/api/v1/delivery-channels/{channel_id}", response_model=Envelope)
def delivery_channel_detail(channel_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DeliveryChannel, channel_id)
    if not row: raise HTTPException(404, "Delivery channel not found")
    return Envelope(data={"id": row.id, "channel_type": row.channel_type, "name": row.name, "enabled": row.enabled, "config": {"chat_id": row.config_json.get("chat_id")}})


@app.patch("/api/v1/delivery-channels/{channel_id}", response_model=Envelope)
def update_delivery_channel(channel_id: str, payload: dict, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DeliveryChannel, channel_id)
    if not row: raise HTTPException(404, "Delivery channel not found")
    if "name" in payload: row.name = payload["name"]
    if "enabled" in payload: row.enabled = bool(payload["enabled"])
    if payload.get("config", {}).get("chat_id"): row.config_json = {"chat_id": str(payload["config"]["chat_id"])}
    db.commit(); return Envelope(data={"id": row.id, "name": row.name, "enabled": row.enabled})


@app.delete("/api/v1/delivery-channels/{channel_id}", response_model=Envelope)
def delete_delivery_channel(channel_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DeliveryChannel, channel_id)
    if not row: raise HTTPException(404, "Delivery channel not found")
    row.enabled = False; db.commit(); return Envelope(data={"id": row.id, "enabled": False})


@app.post("/api/v1/delivery-channels/{channel_id}/test", response_model=Envelope)
async def test_delivery_channel(channel_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(DeliveryChannel, channel_id)
    if not row: raise HTTPException(404, "Delivery channel not found")
    if row.channel_type != "TELEGRAM": raise HTTPException(422, "channel adapter is not implemented")
    outcome = await TelegramAdapter().send(DeliveryMessage("Steel Intelligence test", "Alert delivery connection test.", "LOW"), row)
    return Envelope(data={"success": outcome.success, "external_message_id": outcome.external_message_id, "error_code": outcome.error_code, "error_message": outcome.error_message})


@app.post("/api/v1/delivery-subscriptions", response_model=Envelope)
def create_delivery_subscription(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    if not db.get(DeliveryChannel, payload.get("delivery_channel_id")): raise HTTPException(422, "delivery channel not found")
    if payload.get("watchlist_id") and not db.get(Watchlist, payload["watchlist_id"]): raise HTTPException(422, "watchlist not found")
    minimum = payload.get("minimum_priority")
    if minimum and minimum not in {"LOW", "MEDIUM", "HIGH"}: raise HTTPException(422, "invalid minimum_priority")
    row = AlertDeliverySubscription(watchlist_id=payload.get("watchlist_id"), delivery_channel_id=payload["delivery_channel_id"], enabled=payload.get("enabled", True), minimum_priority=minimum)
    db.add(row); db.commit(); db.refresh(row)
    return Envelope(data={"id": row.id, "watchlist_id": row.watchlist_id, "delivery_channel_id": row.delivery_channel_id, "enabled": row.enabled, "minimum_priority": row.minimum_priority})


@app.get("/api/v1/delivery-subscriptions", response_model=Envelope)
def list_delivery_subscriptions(db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(AlertDeliverySubscription).order_by(desc(AlertDeliverySubscription.created_at))))
    return Envelope(data=[{"id": row.id, "watchlist_id": row.watchlist_id, "delivery_channel_id": row.delivery_channel_id, "enabled": row.enabled, "minimum_priority": row.minimum_priority} for row in rows])


@app.patch("/api/v1/delivery-subscriptions/{subscription_id}", response_model=Envelope)
def update_delivery_subscription(subscription_id: str, payload: dict, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(AlertDeliverySubscription, subscription_id)
    if not row: raise HTTPException(404, "delivery subscription not found")
    if "enabled" in payload: row.enabled = bool(payload["enabled"])
    if "minimum_priority" in payload: row.minimum_priority = payload["minimum_priority"]
    db.commit(); return Envelope(data={"id": row.id, "enabled": row.enabled, "minimum_priority": row.minimum_priority})


@app.delete("/api/v1/delivery-subscriptions/{subscription_id}", response_model=Envelope)
def delete_delivery_subscription(subscription_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(AlertDeliverySubscription, subscription_id)
    if not row: raise HTTPException(404, "delivery subscription not found")
    row.enabled = False; db.commit(); return Envelope(data={"id": row.id, "enabled": False})


@app.post("/api/v1/deliveries/process", response_model=Envelope)
async def process_deliveries(payload: dict | None = None, db: Session = Depends(get_db)) -> Envelope:
    payload = payload or {}
    return Envelope(data={"alerts": await process_pending(db, payload.get("limit"), bool(payload.get("dry_run", False))), "digests": await process_digest_pending(db, payload.get("limit"), bool(payload.get("dry_run", False)))})


@app.get("/api/v1/deliveries", response_model=Envelope)
def list_deliveries(status: str | None = None, alert_id: str | None = None, delivery_channel_id: str | None = None, limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), db: Session = Depends(get_db)) -> Envelope:
    query = select(AlertDelivery).order_by(desc(AlertDelivery.created_at)).offset(offset).limit(limit)
    if status: query = query.where(AlertDelivery.status == status.upper())
    if alert_id: query = query.where(AlertDelivery.alert_id == alert_id)
    if delivery_channel_id: query = query.where(AlertDelivery.delivery_channel_id == delivery_channel_id)
    rows = list(db.scalars(query))
    return Envelope(data=[{"id": row.id, "alert_id": row.alert_id, "delivery_channel_id": row.delivery_channel_id, "status": row.status, "attempt_count": row.attempt_count, "last_attempt_at": row.last_attempt_at, "delivered_at": row.delivered_at, "external_message_id": row.external_message_id, "error_code": row.error_code, "error_message": row.error_message} for row in rows], meta={"count": len(rows)})


@app.get("/api/v1/deliveries/{delivery_id}", response_model=Envelope)
def delivery_detail(delivery_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(AlertDelivery, delivery_id)
    if not row: raise HTTPException(404, "delivery not found")
    return Envelope(data={"id": row.id, "alert_id": row.alert_id, "delivery_channel_id": row.delivery_channel_id, "status": row.status, "attempt_count": row.attempt_count, "last_attempt_at": row.last_attempt_at, "delivered_at": row.delivered_at, "external_message_id": row.external_message_id, "error_code": row.error_code, "error_message": row.error_message, "message_snapshot": row.message_snapshot})


@app.post("/api/v1/deliveries/{delivery_id}/retry", response_model=Envelope)
def retry_delivery(delivery_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(AlertDelivery, delivery_id)
    if not row: raise HTTPException(404, "delivery not found")
    if row.status != "FAILED": raise HTTPException(409, "only FAILED deliveries can be retried")
    row.status = "RETRY_PENDING"; row.error_code = None; row.error_message = None; db.commit()
    return Envelope(data={"id": row.id, "status": row.status})


@app.on_event("startup")
def startup() -> None:
    validate_runtime_config()
    init_db()


@app.get("/health", response_model=Envelope)
def health() -> Envelope:
    return Envelope(data={"status": "ok"})


@app.get("/api/v1/admin/version", response_model=Envelope)
def version() -> Envelope:
    return Envelope(data={"version": settings.app_version, "build_sha": settings.build_sha, "environment": settings.app_env, "deployed_at": settings.deployed_at, "knowledge": check_required_knowledge_files()})


@app.post("/api/v1/sources", response_model=Envelope)
def create_source_route(payload: SourceCreate, db: Session = Depends(get_db)) -> Envelope:
    source, duplicate = create_source(db, payload)
    return Envelope(data=SourceRead.model_validate(source).model_dump(), meta={"duplicate": duplicate})


@app.get("/api/v1/sources/{source_id}", response_model=Envelope)
def get_source(source_id: str, db: Session = Depends(get_db)) -> Envelope:
    source = db.get(SourceDocument, source_id)
    if not source: raise HTTPException(404, "Source not found")
    return Envelope(data=SourceRead.model_validate(source).model_dump())


@app.get("/api/v1/collectors/sources", response_model=Envelope)
def collector_sources() -> Envelope:
    return Envelope(data=list_registry_sources())


@app.post("/api/v1/collectors/run", response_model=Envelope)
async def collector_run(payload: dict | None = None, db: Session = Depends(get_db)) -> Envelope:
    payload = payload or {}
    source_codes = payload.get("source_codes")
    if source_codes is not None and not isinstance(source_codes, list):
        raise HTTPException(422, "source_codes must be an array")
    results = await collect_sources(db, source_codes=source_codes, dry_run=bool(payload.get("dry_run", False)))
    return Envelope(data=results, meta={"count": len(results)})


@app.get("/api/v1/collectors/runs", response_model=Envelope)
def collector_runs(limit: int = Query(20, ge=1, le=100), db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(CollectionRun).order_by(desc(CollectionRun.started_at)).limit(limit)))
    return Envelope(data=[{
        "id": row.id, "source_code": row.source_code, "started_at": row.started_at, "completed_at": row.completed_at,
        "status": row.status, "items_seen": row.items_seen, "items_new": row.items_new,
        "items_duplicate": row.items_duplicate, "items_failed": row.items_failed, "error_summary": row.error_summary,
    } for row in rows], meta={"count": len(rows)})


@app.get("/api/v1/event-clusters", response_model=Envelope)
def list_event_clusters(company: str | None = None, event_type: str | None = None, status: str | None = None, date_from: str | None = None, date_to: str | None = None, minimum_confidence: float = Query(0, ge=0, le=1), limit: int = Query(50, ge=1, le=100), offset: int = Query(0, ge=0), db: Session = Depends(get_db)) -> Envelope:
    query = select(EventCluster).where(EventCluster.confidence >= minimum_confidence).order_by(desc(EventCluster.last_seen_at)).offset(offset).limit(limit)
    if event_type: query = query.where(EventCluster.primary_event_type == event_type.upper())
    if status: query = query.where(EventCluster.status == status.upper())
    if date_from: query = query.where(EventCluster.event_date >= date_from)
    if date_to: query = query.where(EventCluster.event_date <= date_to)
    if company: query = query.join(Company, EventCluster.primary_company_id == Company.id).where(Company.normalized_name.contains(company.lower()))
    rows = list(db.scalars(query))
    return Envelope(data=[{"id": row.id, "cluster_key": row.cluster_key, "canonical_event_id": row.canonical_event_id, "primary_company_id": row.primary_company_id, "primary_event_type": row.primary_event_type, "title": row.title, "summary": row.summary, "event_date": row.event_date, "location": row.location, "status": row.status, "confidence": row.confidence, "source_count": row.source_count, "first_seen_at": row.first_seen_at, "last_seen_at": row.last_seen_at, "conflicts": (row.cluster_metadata_json or {}).get("conflicts", [])} for row in rows], meta={"limit": limit, "offset": offset, "count": len(rows)})


@app.get("/api/v1/event-clusters/{cluster_id}", response_model=Envelope)
def event_cluster_detail(cluster_id: str, db: Session = Depends(get_db)) -> Envelope:
    cluster = db.get(EventCluster, cluster_id)
    if not cluster: raise HTTPException(404, "Event cluster not found")
    events = list(db.scalars(select(Event).where(Event.event_cluster_id == cluster.id).order_by(Event.created_at)))
    source_ids = [event.source_document_id for event in events]
    sources = list(db.scalars(select(SourceDocument).where(SourceDocument.id.in_(source_ids)))) if source_ids else []
    evidence = list(db.scalars(select(Evidence).where(Evidence.source_document_id.in_(source_ids)))) if source_ids else []
    opportunities = list(db.scalars(select(Opportunity).where(Opportunity.event_id.in_([event.id for event in events])))) if events else []
    canonical = db.get(Event, cluster.canonical_event_id) if cluster.canonical_event_id else None
    decisions = list(db.scalars(select(EventClusterDecisionLog).where(EventClusterDecisionLog.candidate_cluster_id == cluster.id).order_by(EventClusterDecisionLog.created_at)))
    return Envelope(data={"cluster": {"id": cluster.id, "status": cluster.status, "title": cluster.title, "summary": cluster.summary, "confidence": cluster.confidence, "source_count": cluster.source_count, "first_seen_at": cluster.first_seen_at, "last_seen_at": cluster.last_seen_at, "conflicts": (cluster.cluster_metadata_json or {}).get("conflicts", [])}, "canonical_event": {"id": canonical.id, "type": canonical.primary_event_type, "title": canonical.title, "summary": canonical.summary, "metadata": canonical.metadata_json} if canonical else None, "member_events": [{"id": event.id, "source_document_id": event.source_document_id, "type": event.primary_event_type, "title": event.title, "is_canonical": event.is_canonical, "confidence": event.confidence} for event in events], "source_documents": [{"id": source.id, "title": source.title, "source_name": source.source_name, "source_url": source.source_url, "published_at": source.published_at, "status": source.status} for source in sources], "evidence": [{"id": item.id, "source_document_id": item.source_document_id, "quote_text": item.quote_text, "confidence": item.confidence} for item in evidence], "opportunities": [{"id": item.id, "event_id": item.event_id, "score": item.score, "status": item.status, "title": item.title} for item in opportunities], "decisions": [{"id": item.id, "event_id": item.event_id, "score": item.score, "decision": item.decision, "reasons": item.reasons_json} for item in decisions]})


@app.post("/api/v1/event-clusters/merge", response_model=Envelope)
def merge_event_clusters(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    source_id, target_id = payload.get("source_cluster_id"), payload.get("target_cluster_id")
    if not source_id or not target_id or source_id == target_id:
        raise HTTPException(422, "source_cluster_id and target_cluster_id must be different")
    try:
        cluster = merge_clusters(db, source_id, target_id)
    except ValueError as exc:
        db.rollback()
        raise HTTPException(404, str(exc)) from exc
    return Envelope(data={"id": cluster.id, "status": cluster.status, "canonical_event_id": cluster.canonical_event_id, "source_count": cluster.source_count})


@app.post("/api/v1/evaluations/run", response_model=Envelope)
def run_evaluation_route(payload: dict | None = None, db: Session = Depends(get_db)) -> Envelope:
    payload = payload or {}
    mode = payload.get("mode", "live")
    if mode not in {"live", "replay"}: raise HTTPException(422, "mode must be live or replay")
    return Envelope(data=run_evaluation(db, payload.get("dataset_path"), mode, payload.get("limit")))


@app.get("/api/v1/evaluations/runs", response_model=Envelope)
def evaluation_runs(limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(EvaluationRun).order_by(desc(EvaluationRun.created_at)).limit(limit)))
    return Envelope(data=[{"id": row.id, "name": row.name, "dataset_version": row.dataset_version, "status": row.status, "started_at": row.started_at, "completed_at": row.completed_at, "summary": row.summary_json} for row in rows], meta={"count": len(rows)})


@app.get("/api/v1/evaluations/runs/{run_id}", response_model=Envelope)
def evaluation_run_detail(run_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(EvaluationRun, run_id)
    if not row: raise HTTPException(404, "Evaluation run not found")
    return Envelope(data={"id": row.id, "name": row.name, "dataset_version": row.dataset_version, "pipeline_version": row.pipeline_version, "prompt_version": row.prompt_version, "model": row.model, "status": row.status, "started_at": row.started_at, "completed_at": row.completed_at, "summary": row.summary_json})


@app.get("/api/v1/evaluations/runs/{run_id}/cases", response_model=Envelope)
def evaluation_cases(run_id: str, error_code: str | None = None, severity: str | None = None, failed_only: bool = False, limit: int = Query(100, ge=1, le=500), db: Session = Depends(get_db)) -> Envelope:
    rows = list(db.scalars(select(EvaluationCaseResult).where(EvaluationCaseResult.evaluation_run_id == run_id).order_by(EvaluationCaseResult.created_at).limit(limit)))
    data = []
    for row in rows:
        errors = row.errors_json or []
        if failed_only and not errors: continue
        if error_code and not any(item.get("code") == error_code for item in errors): continue
        if severity and not any(item.get("severity") == severity for item in errors): continue
        data.append({"id": row.id, "case_id": row.case_id, "source_document_id": row.source_document_id, "event_correct": row.event_correct, "cluster_correct": row.cluster_correct, "strategy_score": row.strategy_score, "application_correct": row.application_correct, "component_correct": row.component_correct, "material_category_correct": row.material_category_correct, "product_correct": row.product_correct, "grade_guardrail_pass": row.grade_guardrail_pass, "opportunity_quality": row.opportunity_quality, "action_quality": row.action_quality, "errors": errors, "review_notes": row.review_notes})
    return Envelope(data=data, meta={"count": len(data)})


@app.post("/api/v1/evaluations/cases/{case_result_id}/review", response_model=Envelope)
def review_evaluation_case(case_result_id: str, payload: dict, db: Session = Depends(get_db)) -> Envelope:
    if not payload.get("dimension") or not payload.get("reviewer", "anonymous"):
        raise HTTPException(422, "dimension is required")
    case = db.get(EvaluationCaseResult, case_result_id)
    if not case: raise HTTPException(404, "Evaluation case result not found")
    review = HumanEvaluation(evaluation_case_result_id=case.id, reviewer=payload.get("reviewer", "anonymous"), dimension=payload["dimension"], score=payload.get("score"), label=payload.get("label"), comment=payload.get("comment"))
    db.add(review); db.commit(); db.refresh(review)
    return Envelope(data={"id": review.id, "case_result_id": case.id, "dimension": review.dimension, "score": review.score, "label": review.label, "comment": review.comment})


@app.get("/api/v1/evaluations/compare", response_model=Envelope)
def compare_evaluations(baseline: str, candidate: str, target_metric: str | None = None, db: Session = Depends(get_db)) -> Envelope:
    before, after = db.get(EvaluationRun, baseline), db.get(EvaluationRun, candidate)
    if not before or not after: raise HTTPException(404, "Both evaluation runs are required")
    return Envelope(data=compare_summaries(before.summary_json, after.summary_json, target_metric))


@app.get("/api/v1/tuning/candidates", response_model=Envelope)
def tuning_candidates(status: str | None = None, error_code: str | None = None, db: Session = Depends(get_db)) -> Envelope:
    query = select(TuningCandidate).order_by(desc(TuningCandidate.created_at))
    if status: query = query.where(TuningCandidate.status == status.upper())
    if error_code: query = query.where(TuningCandidate.error_code == error_code)
    rows = list(db.scalars(query.limit(100)))
    return Envelope(data=[{"id": row.id, "error_code": row.error_code, "root_cause": row.root_cause, "affected_stage": row.affected_stage, "proposed_fix_type": row.proposed_fix_type, "proposed_change": row.proposed_change, "expected_metric": row.expected_metric, "status": row.status, "baseline_run_id": row.baseline_run_id, "candidate_run_id": row.candidate_run_id, "decision": row.decision_json} for row in rows])


@app.get("/api/v1/tuning/candidates/{candidate_id}", response_model=Envelope)
def tuning_candidate_detail(candidate_id: str, db: Session = Depends(get_db)) -> Envelope:
    row = db.get(TuningCandidate, candidate_id)
    if not row: raise HTTPException(404, "Tuning candidate not found")
    return Envelope(data={"id": row.id, "error_code": row.error_code, "root_cause": row.root_cause, "affected_stage": row.affected_stage, "proposed_fix_type": row.proposed_fix_type, "proposed_change": row.proposed_change, "expected_metric": row.expected_metric, "status": row.status, "decision": row.decision_json})


@app.post("/api/v1/tuning/candidates", response_model=Envelope)
def create_tuning_candidate(payload: dict, db: Session = Depends(get_db)) -> Envelope:
    required = ["error_code", "root_cause", "affected_stage", "proposed_fix_type", "proposed_change", "expected_metric"]
    if any(not payload.get(key) for key in required): raise HTTPException(422, "error_code, root_cause, affected_stage, proposed_fix_type, proposed_change and expected_metric are required")
    row = TuningCandidate(**{key: payload[key] for key in required}, source_evaluation_run_id=payload.get("source_evaluation_run_id"), baseline_run_id=payload.get("baseline_run_id"))
    db.add(row); db.commit(); db.refresh(row)
    return Envelope(data={"id": row.id, "status": row.status})


@app.post("/api/v1/intelligence/run/{source_id}", response_model=Envelope)
def run_intelligence(source_id: str, db: Session = Depends(get_db)) -> Envelope:
    try:
        return Envelope(data=run_intelligence_pipeline(db, source_id))
    except ApplicationError as exc:
        db.rollback()
        raise HTTPException(422, {"code": exc.code, "message": exc.message}) from exc
    except Exception as exc:
        db.rollback()
        raise HTTPException(500, {"code": "INTELLIGENCE_PIPELINE_ERROR", "message": "Pipeline failed without exposing internal details."}) from exc


@app.get("/api/v1/opportunities", response_model=Envelope)
def list_opportunities(industry: str | None = None, company: str | None = None, minimum_score: float = Query(0, ge=0, le=100), status: str | None = None, product_family: str | None = None, limit: int = Query(50, ge=1, le=100), offset: int = Query(0, ge=0), db: Session = Depends(get_db)) -> Envelope:
    query = select(Opportunity, Company, Event, ProductMatch).join(Company, Opportunity.company_id == Company.id, isouter=True).join(Event, Opportunity.event_id == Event.id, isouter=True).join(ProductMatch, Opportunity.product_match_id == ProductMatch.id, isouter=True).where(Opportunity.score >= minimum_score).order_by(desc(Opportunity.score)).offset(offset).limit(limit)
    if status: query = query.where(Opportunity.status == status)
    if industry:
        query = query.where(Company.industry_code == industry.upper())
    if company:
        query = query.where(Company.normalized_name.contains(company.lower()))
    if product_family:
        query = query.where(ProductMatch.product_family == product_family.upper())
    rows = list(db.execute(query))
    data = []
    for opportunity, company_obj, event, product in rows:
        data.append({
            **OpportunityRead.model_validate(opportunity).model_dump(),
            "company": {"id": company_obj.id, "name": company_obj.name} if company_obj else None,
            "industry": company_obj.industry_code if company_obj else None,
            "event_type": event.primary_event_type if event else None,
            "product_family": product.product_family if product else None,
            "created_at": opportunity.created_at,
        })
    return Envelope(data=data, meta={"limit": limit, "offset": offset, "count": len(data)})


@app.get("/api/v1/opportunities/{opportunity_id}", response_model=Envelope)
def opportunity_detail(opportunity_id: str, db: Session = Depends(get_db)) -> Envelope:
    item = db.get(Opportunity, opportunity_id)
    if not item: raise HTTPException(404, "Opportunity not found")
    event = db.get(Event, item.event_id)
    source = db.get(SourceDocument, event.source_document_id) if event else None
    evidence = list(db.scalars(select(Evidence).where(Evidence.source_document_id == source.id))) if source else []
    strategies = list(db.scalars(select(StrategyInference).where(StrategyInference.event_id == event.id))) if event else []
    demand = db.scalar(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id == event.id)) if event else None
    product = db.get(ProductMatch, item.product_match_id) if item.product_match_id else None
    company_obj = db.get(Company, item.company_id) if item.company_id else None
    actions = list(db.scalars(select(RecommendedAction).where(RecommendedAction.opportunity_id == item.id)))
    return Envelope(data={
        "opportunity": {**OpportunityRead.model_validate(item).model_dump(), "created_at": item.created_at},
        "company": {"id": company_obj.id, "name": company_obj.name, "industry_code": company_obj.industry_code} if company_obj else None,
        "source": {"id": source.id, "title": source.title, "source_name": source.source_name, "source_url": source.source_url, "published_at": source.published_at, "content": source.content} if source else None,
        "evidence": [{"id": row.id, "quote_text": row.quote_text, "confidence": row.confidence} for row in evidence],
        "event": {"id": event.id, "type": event.primary_event_type, "title": event.title, "summary": event.summary, "confidence": event.confidence} if event else None,
        "strategies": [{"id": row.id, "code": row.strategy_code, "reasoning_summary": row.reasoning_summary, "confidence": row.confidence, "evidence_ids": row.evidence_ids_json} for row in strategies],
        "steel_demand": {"id": demand.id, "industry_code": demand.industry_code, "application_code": demand.application_code, "component_code": demand.component_code, "material_requirements": demand.material_requirements_json, "material_category": demand.material_category, "demand_direction": demand.demand_direction, "confidence": demand.confidence} if demand else None,
        "product_match": {"id": product.id, "product_family": product.product_family, "product_file": product.product_file, "candidate_series": product.candidate_series_json, "candidate_grades": product.candidate_grades_json, "match_score": product.match_score, "confidence": product.confidence, "status": product.status, "reasoning_summary": product.reasoning_summary} if product else None,
        "score_breakdown": item.score_breakdown_json or {},
        "recommended_actions": [{"id": row.id, "action_type": row.action_type, "description": row.description, "priority": row.priority} for row in actions],
    })


# Local MVP convenience: serve the dashboard from the same process as the API.
FRONTEND_DIR = Path(__file__).resolve().parents[2]
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
