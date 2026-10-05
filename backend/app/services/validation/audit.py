from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.entities import Alert, Company, Event, Evidence, Opportunity, ProductMatch, SourceDocument, SteelDemandHypothesis, StrategyInference
from app.services.taxonomy import validate_code


def integrity_audit(db: Session) -> dict:
    evidence_orphans = db.scalar(select(func.count()).select_from(Evidence).outerjoin(SourceDocument, Evidence.source_document_id == SourceDocument.id).where(SourceDocument.id.is_(None))) or 0
    event_orphans = db.scalar(select(func.count()).select_from(Event).outerjoin(SourceDocument, Event.source_document_id == SourceDocument.id).where(SourceDocument.id.is_(None))) or 0
    demand_orphans = db.scalar(select(func.count()).select_from(SteelDemandHypothesis).outerjoin(Event, SteelDemandHypothesis.event_id == Event.id).where(Event.id.is_(None))) or 0
    product_orphans = db.scalar(select(func.count()).select_from(ProductMatch).outerjoin(SteelDemandHypothesis, ProductMatch.steel_demand_hypothesis_id == SteelDemandHypothesis.id).where(SteelDemandHypothesis.id.is_(None))) or 0
    opportunity_orphans = db.scalar(select(func.count()).select_from(Opportunity).outerjoin(Event, Opportunity.event_id == Event.id).where(Event.id.is_(None))) or 0
    alert_orphans = db.scalar(select(func.count()).select_from(Alert).outerjoin(__import__("app.models.entities", fromlist=["Watchlist"]).Watchlist, Alert.watchlist_id == __import__("app.models.entities", fromlist=["Watchlist"]).Watchlist.id).where(__import__("app.models.entities", fromlist=["Watchlist"]).Watchlist.id.is_(None))) or 0
    counts = {"evidence_without_source": evidence_orphans, "event_without_source": event_orphans, "demand_without_event": demand_orphans, "product_without_demand": product_orphans, "opportunity_without_event": opportunity_orphans, "alert_without_watchlist": alert_orphans}
    return {"counts": counts, "orphan_count": sum(counts.values()), "passed": sum(counts.values()) == 0}


def evidence_audit(db: Session, source_ids: list[str]) -> dict:
    rows = list(db.execute(select(Evidence, SourceDocument).join(SourceDocument, Evidence.source_document_id == SourceDocument.id).where(Evidence.source_document_id.in_(source_ids)))) if source_ids else []
    invalid = [{"evidence_id": evidence.id, "source_document_id": source.id} for evidence, source in rows if not evidence.quote_text or evidence.quote_text not in source.content]
    return {"checked": len(rows), "invalid": invalid, "validity_rate": round((len(rows) - len(invalid)) / len(rows) * 100, 2) if rows else 100.0, "critical": bool(invalid)}


def duplicate_audit(db: Session, run_source_ids: list[str]) -> dict:
    if not run_source_ids: return {"source_count": 0, "duplicate_content_hashes": 0, "duplicate_urls": 0}
    docs = list(db.scalars(select(SourceDocument).where(SourceDocument.id.in_(run_source_ids))))
    hashes = len(docs) - len({doc.content_hash for doc in docs})
    urls = len([url for url in [doc.source_url for doc in docs] if url]) - len({doc.source_url for doc in docs if doc.source_url})
    return {"source_count": len(docs), "duplicate_content_hashes": max(0, hashes), "duplicate_urls": max(0, urls)}


def taxonomy_audit(db: Session, source_ids: list[str]) -> dict:
    events = list(db.scalars(select(Event).where(Event.source_document_id.in_(source_ids)))) if source_ids else []
    event_ids = [item.id for item in events]
    demands = list(db.scalars(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id.in_(event_ids)))) if event_ids else []
    strategies = list(db.scalars(select(StrategyInference).where(StrategyInference.event_id.in_(event_ids)))) if event_ids else []
    invalid = []
    for item in events:
        if validate_code("event", item.primary_event_type) == "UNKNOWN": invalid.append({"kind": "event", "value": item.primary_event_type, "id": item.id})
    for item in demands:
        for kind, value in (("industry", item.industry_code), ("application", item.application_code), ("material", item.material_category)):
            if value and validate_code(kind, value) == "UNKNOWN": invalid.append({"kind": kind, "value": value, "id": item.id})
    for item in strategies:
        if validate_code("strategy", item.strategy_code) == "UNKNOWN": invalid.append({"kind": "strategy", "value": item.strategy_code, "id": item.id})
    return {"checked": len(events) + len(demands) + len(strategies), "invalid": invalid, "passed": not invalid}
