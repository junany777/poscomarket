from datetime import datetime

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import Company, Evidence, Event, EventCluster, Opportunity, ProductMatch, SourceDocument, SteelDemandHypothesis, StrategyInference, RecommendedAction


def search_opportunities(db: Session, intent, limit: int | None = None) -> list[dict]:
    limit = min(limit or settings.ask_max_opportunities, 20)
    query = select(Opportunity, Company, Event, ProductMatch).join(Company, Opportunity.company_id == Company.id, isouter=True).join(Event, Opportunity.event_id == Event.id, isouter=True).join(ProductMatch, Opportunity.product_match_id == ProductMatch.id, isouter=True).order_by(desc(Opportunity.score)).limit(limit)
    if intent.minimum_score is not None: query = query.where(Opportunity.score >= intent.minimum_score)
    if intent.product_families: query = query.where(ProductMatch.product_family.in_(intent.product_families))
    if intent.company_names: query = query.where(Company.name.in_(intent.company_names))
    if intent.date_from: query = query.where(Opportunity.created_at >= intent.date_from)
    rows = list(db.execute(query))
    return [{"id": opp.id, "title": opp.title, "summary": opp.summary, "score": opp.score, "confidence": opp.confidence, "status": opp.status, "company": company.name if company else None, "event_id": event.id if event else None, "event_type": event.primary_event_type if event else None, "product_family": product.product_family if product else None, "product_match_id": product.id if product else None} for opp, company, event, product in rows]


def search_event_clusters(db: Session, intent, limit: int | None = None) -> list[dict]:
    query = select(EventCluster).order_by(desc(EventCluster.last_seen_at)).limit(min(limit or settings.ask_max_events, 20))
    if intent.event_types: query = query.where(EventCluster.primary_event_type.in_(intent.event_types))
    rows = list(db.scalars(query))
    return [{"id": row.id, "title": row.title, "summary": row.summary, "event_type": row.primary_event_type, "company_id": row.primary_company_id, "event_date": row.event_date, "status": row.status, "confidence": row.confidence, "source_count": row.source_count, "canonical_event_id": row.canonical_event_id} for row in rows]


def get_evidence_for_opportunities(db: Session, opportunities: list[dict]) -> list[dict]:
    event_ids = [item["event_id"] for item in opportunities if item.get("event_id")]
    events = list(db.scalars(select(Event).where(Event.id.in_(event_ids)))) if event_ids else []
    source_ids = [event.source_document_id for event in events]
    evidence = list(db.scalars(select(Evidence).where(Evidence.source_document_id.in_(source_ids)).limit(settings.ask_max_evidence))) if source_ids else []
    sources = {source.id: source for source in db.scalars(select(SourceDocument).where(SourceDocument.id.in_(source_ids)))} if source_ids else {}
    return [{"id": item.id, "source_document_id": item.source_document_id, "quote_text": item.quote_text, "title": sources[item.source_document_id].title if item.source_document_id in sources else None, "source_name": sources[item.source_document_id].source_name if item.source_document_id in sources else None, "source_url": sources[item.source_document_id].source_url if item.source_document_id in sources else None, "published_at": sources[item.source_document_id].published_at if item.source_document_id in sources else None} for item in evidence]


def get_opportunity_context(db: Session, opportunity_id: str) -> dict | None:
    opportunity = db.get(Opportunity, opportunity_id)
    if not opportunity: return None
    event = db.get(Event, opportunity.event_id)
    demand = db.scalar(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id == event.id)) if event else None
    strategy = db.scalar(select(StrategyInference).where(StrategyInference.event_id == event.id)) if event else None
    product = db.get(ProductMatch, opportunity.product_match_id) if opportunity.product_match_id else None
    actions = list(db.scalars(select(RecommendedAction).where(RecommendedAction.opportunity_id == opportunity.id)))
    evidence = get_evidence_for_opportunities(db, [{"event_id": event.id}]) if event else []
    cluster = db.get(EventCluster, event.event_cluster_id) if event and event.event_cluster_id else None
    return {"opportunity": opportunity, "event": event, "cluster": cluster, "demand": demand, "strategy": strategy, "product": product, "actions": actions, "evidence": evidence}
