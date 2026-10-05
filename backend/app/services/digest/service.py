from collections import Counter
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import Alert, Company, DigestSubscription, Event, Evidence, EventCluster, IntelligenceDigest, Opportunity, ProductMatch, RecommendedAction, SourceDocument, SteelDemandHypothesis


def period_for(digest_type: str, now: datetime | None = None) -> tuple[datetime, datetime]:
    local_now = (now or datetime.now(timezone.utc)).astimezone(ZoneInfo(settings.digest_timezone))
    end = local_now
    start = end - timedelta(days=1 if digest_type == "DAILY" else 7)
    return start.astimezone(timezone.utc), end.astimezone(timezone.utc)


def _context(db: Session, digest_type: str, start: datetime, end: datetime) -> dict:
    max_opps = settings.digest_daily_max_opportunities if digest_type == "DAILY" else settings.digest_weekly_max_opportunities
    clusters = list(db.scalars(select(EventCluster).where(EventCluster.updated_at >= start, EventCluster.updated_at <= end).order_by(desc(EventCluster.confidence)).limit(settings.digest_max_events)))
    cluster_ids = {item.id for item in clusters}
    rows = list(db.execute(select(Opportunity, Event, ProductMatch, Company).join(Event, Opportunity.event_id == Event.id).join(ProductMatch, Opportunity.product_match_id == ProductMatch.id, isouter=True).join(Company, Opportunity.company_id == Company.id, isouter=True).where(Opportunity.updated_at >= start, Opportunity.updated_at <= end).order_by(desc(Opportunity.score)).limit(max_opps * 4)))
    opportunities = []
    seen_routes = set()
    for opportunity, event, product, company in rows:
        cluster_id = event.event_cluster_id
        key = (cluster_id or event.id, product.product_family if product else None)
        if key in seen_routes: continue
        seen_routes.add(key)
        opportunities.append({"id": opportunity.id, "title": opportunity.title, "score": opportunity.score, "confidence": opportunity.confidence, "status": opportunity.status, "product_family": product.product_family if product else None, "company": company.name if company else None, "event_type": event.primary_event_type, "event_cluster_id": cluster_id})
        if cluster_id: cluster_ids.add(cluster_id)
        if len(opportunities) >= max_opps: break
    alerts = list(db.scalars(select(Alert).where(Alert.created_at >= start, Alert.created_at <= end, Alert.priority == "HIGH").order_by(desc(Alert.created_at)).limit(settings.digest_max_alerts)))
    industry = Counter(); products = Counter()
    for item in opportunities:
        products[item["product_family"] or "UNKNOWN"] += 1
        event = db.get(Event, db.get(Opportunity, item["id"]).event_id)
        demand = db.scalar(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id == event.id)) if event else None
        if demand: industry[demand.industry_code] += 1
    citations = []
    source_ids = [event.source_document_id for event in db.scalars(select(Event).where(Event.event_cluster_id.in_(list(cluster_ids))))] if cluster_ids else []
    evidence_rows = list(db.scalars(select(Evidence).where(Evidence.source_document_id.in_(source_ids)).limit(settings.digest_max_evidence))) if source_ids else []
    sources = {source.id: source for source in db.scalars(select(SourceDocument).where(SourceDocument.id.in_(source_ids)))} if source_ids else {}
    for evidence in evidence_rows:
        source = sources.get(evidence.source_document_id)
        citations.append({"source_document_id": evidence.source_document_id, "evidence_id": evidence.id, "title": source.title if source else None, "source_name": source.source_name if source else None, "source_url": source.source_url if source else None, "quote_text": evidence.quote_text})
    actions = []
    for item in opportunities:
        for action in db.scalars(select(RecommendedAction).where(RecommendedAction.opportunity_id == item["id"])):
            if action.description not in actions: actions.append(action.description)
    return {"period_start": start, "period_end": end, "opportunities": opportunities, "event_clusters": [{"id": item.id, "title": item.title, "summary": item.summary, "event_type": item.primary_event_type, "source_count": item.source_count, "confidence": item.confidence} for item in clusters], "alerts": [{"id": item.id, "title": item.title, "priority": item.priority, "opportunity_id": item.opportunity_id} for item in alerts], "industry_summary": [{"code": key, "count": value} for key, value in industry.items()], "product_summary": [{"product_family": key, "opportunity_count": value} for key, value in products.items()], "recommended_actions": actions[:10], "citations": citations}


def generate_digest(db: Session, digest_type: str = "DAILY", period_start: datetime | None = None, period_end: datetime | None = None) -> dict:
    digest_type = digest_type.upper()
    if digest_type not in {"DAILY", "WEEKLY"}: raise ValueError("digest_type must be DAILY or WEEKLY")
    start, end = (period_start, period_end) if period_start and period_end else period_for(digest_type)
    existing = db.scalar(select(IntelligenceDigest).where(IntelligenceDigest.digest_type == digest_type, IntelligenceDigest.period_start == start, IntelligenceDigest.period_end == end))
    if existing: return {"id": existing.id, "status": existing.status, "content": existing.content_json, "deduplicated": True}
    context = _context(db, digest_type, start, end)
    opportunities, events = context["opportunities"], context["event_clusters"]
    bullets = [f"{len(opportunities)}개 Opportunity와 {len(events)}개 EventCluster를 확인했습니다."]
    high = sum(1 for item in opportunities if item["score"] >= 80)
    if high: bullets.append(f"고우선순위 Opportunity {high}건이 포함되었습니다.")
    if events and len(events) < settings.digest_min_events_for_trend: bullets.append("현재 신호는 업계 전체 추세가 아닌 단일·초기 신호로 해석해야 합니다.")
    elif events: bullets.append(f"{len(events)}개 독립 EventCluster에서 반복 신호가 관찰되었습니다.")
    if context["product_summary"]: bullets.append("제품 신호: " + ", ".join(f"{item['product_family']} {item['opportunity_count']}건" for item in context["product_summary"]))
    content = {"executive_summary": bullets, "top_opportunities": opportunities, "major_events": events, "industry_trends": [{"label": "EARLY_SIGNAL" if len(events) < settings.digest_min_events_for_trend else "TREND", "items": context["industry_summary"]}], "product_signals": context["product_summary"], "watchlist_highlights": context["alerts"], "recommended_actions": context["recommended_actions"], "sources": context["citations"]}
    digest = IntelligenceDigest(digest_type=digest_type, period_start=start, period_end=end, title=f"{'Daily' if digest_type == 'DAILY' else 'Weekly'} Steel Intelligence", executive_summary="\n".join(f"• {bullet}" for bullet in bullets), status="READY", event_count=len(events), opportunity_count=len(opportunities), high_priority_count=high, content_json=content, generated_at=datetime.now(timezone.utc), model="deterministic", prompt_version="digest-v1")
    db.add(digest); db.commit(); db.refresh(digest)
    return {"id": digest.id, "status": digest.status, "content": digest.content_json, "event_count": digest.event_count, "opportunity_count": digest.opportunity_count, "high_priority_count": digest.high_priority_count}
