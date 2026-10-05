from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from statistics import mean

from sqlalchemy import desc, func, or_, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import AIRun, Alert, AlertDelivery, CollectionRun, DigestDelivery, EvaluationRun, Event, EventCluster, IntelligenceDigest, Opportunity, ProductMatch, SourceDocument, SteelDemandHypothesis
from app.services.ingestion.collection_service import list_registry_sources


def window(period: str = "24h") -> tuple[datetime, datetime]:
    now = datetime.now(timezone.utc)
    hours = {"24h": 24, "7d": 24 * 7, "30d": 24 * 30}.get(period, 24)
    return now - timedelta(hours=hours), now


def _age(value, now: datetime) -> int | None:
    if not value: return None
    if isinstance(value, str):
        try: value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError: return None
    if value.tzinfo is None: value = value.replace(tzinfo=timezone.utc)
    return max(0, int((now - value).total_seconds()))


def _latency_ms(started: str | None, completed: str | None) -> float | None:
    if not started or not completed: return None
    try:
        start = datetime.fromisoformat(started.replace("Z", "+00:00")); end = datetime.fromisoformat(completed.replace("Z", "+00:00"))
        if start.tzinfo is None: start = start.replace(tzinfo=timezone.utc)
        if end.tzinfo is None: end = end.replace(tzinfo=timezone.utc)
        return max(0.0, (end - start).total_seconds() * 1000)
    except ValueError:
        return None


def _count(db, model, since, until, field=None) -> int:
    column = field or model.created_at
    return int(db.scalar(select(func.count()).select_from(model).where(column >= since, column <= until)) or 0)


def collection(db: Session, period: str = "24h", source: str | None = None, status: str | None = None) -> dict:
    since, until = window(period); query = select(CollectionRun).where(CollectionRun.created_at >= since, CollectionRun.created_at <= until).order_by(desc(CollectionRun.created_at)).limit(500)
    if source: query = query.where(CollectionRun.source_code == source)
    if status: query = query.where(CollectionRun.status == status.upper())
    runs = list(db.scalars(query)); now = datetime.now(timezone.utc)
    registry = list_registry_sources(); by_source = defaultdict(list)
    for run in runs: by_source[run.source_code].append(run)
    sources = []
    for item in registry:
        rows = by_source.get(item.get("source_code"), []); last = rows[0] if rows else None; success = next((row for row in rows if row.status in {"COMPLETED", "PARTIAL"}), None)
        sources.append({"source_code": item.get("source_code"), "source_name": item.get("source_name"), "collector_type": item.get("collector_type"), "enabled": bool(item.get("enabled")), "last_run": last.created_at if last else None, "last_success": success.completed_at if success else None, "status": "UNKNOWN" if not last else "FAILED" if last.status == "FAILED" else "DEGRADED" if last.status == "PARTIAL" else "HEALTHY", "items_new": last.items_new if last else 0, "failures": last.items_failed if last else 0})
    backlog = list(db.execute(select(SourceDocument.status, func.count()).group_by(SourceDocument.status)))
    return {"period": period, "runs": {"total": len(runs), "successful": sum(run.status in {"COMPLETED", "PARTIAL"} for run in runs), "failed": sum(run.status == "FAILED" for run in runs), "items_seen": sum(run.items_seen or 0 for run in runs), "items_new": sum(run.items_new or 0 for run in runs), "duplicates": sum(run.items_duplicate or 0 for run in runs), "parse_failures": sum(run.items_failed or 0 for run in runs)}, "enabled_sources": sum(item["enabled"] for item in sources), "healthy_sources": sum(item["status"] == "HEALTHY" for item in sources), "degraded_sources": sum(item["status"] == "DEGRADED" for item in sources), "failed_sources": sum(item["status"] == "FAILED" for item in sources), "sources": sources, "backlog": {status: count for status, count in backlog}}


def pipeline(db: Session, period: str = "24h") -> dict:
    since, until = window(period)
    counts = {"source_documents": _count(db, SourceDocument, since, until), "events": _count(db, Event, since, until), "event_clusters": _count(db, EventCluster, since, until), "steel_demand_hypotheses": _count(db, SteelDemandHypothesis, since, until), "product_matches": _count(db, ProductMatch, since, until), "opportunities": _count(db, Opportunity, since, until)}
    relevant = int(db.scalar(select(func.count()).select_from(SourceDocument).where(SourceDocument.created_at >= since, SourceDocument.created_at <= until, SourceDocument.status != "REJECTED")) or 0)
    backlog_query = select(SourceDocument.status, func.count()).where(SourceDocument.status.in_(["READY_FOR_INTELLIGENCE", "PROCESSING", "REVIEW_REQUIRED"])).group_by(SourceDocument.status)
    backlog = {status: count for status, count in db.execute(backlog_query)}; backlog_total = sum(backlog.values()); oldest = db.scalar(select(SourceDocument.created_at).where(SourceDocument.status.in_(["READY_FOR_INTELLIGENCE", "PROCESSING", "REVIEW_REQUIRED"])).order_by(SourceDocument.created_at).limit(1)); backlog_state = "CRITICAL" if backlog_total >= settings.ops_backlog_critical_threshold else "WARNING" if backlog_total >= settings.ops_backlog_warning_threshold else "NORMAL"
    failures = [{"time": row.created_at, "stage": "COLLECTION", "reference": row.source_code, "error_type": row.status, "error_message": row.error_summary, "retryable": row.status != "FAILED"} for row in db.scalars(select(CollectionRun).where(CollectionRun.status.in_(["FAILED", "PARTIAL"])).order_by(desc(CollectionRun.created_at)).limit(20))]
    rates = {"event_extraction_rate": round(counts["events"] / relevant * 100, 2) if relevant else None, "cluster_creation_rate": round(counts["event_clusters"] / counts["events"] * 100, 2) if counts["events"] else None, "product_match_rate": round(counts["product_matches"] / counts["steel_demand_hypotheses"] * 100, 2) if counts["steel_demand_hypotheses"] else None, "opportunity_creation_rate": round(counts["opportunities"] / counts["product_matches"] * 100, 2) if counts["product_matches"] else None}
    return {"period": period, "funnel": counts, "conversion_rates": rates, "backlog": {"counts": backlog, "total": backlog_total, "state": backlog_state, "oldest_at": oldest, "oldest_age_seconds": _age(oldest, datetime.now(timezone.utc))}, "failures": failures}


def ai_runs(db: Session, period: str = "24h", run_type: str | None = None, model: str | None = None, status: str | None = None) -> dict:
    since, until = window(period); query = select(AIRun).where(AIRun.created_at >= since, AIRun.created_at <= until).order_by(desc(AIRun.created_at)).limit(1000)
    if run_type: query = query.where(AIRun.run_type == run_type)
    if model: query = query.where(AIRun.model == model)
    if status: query = query.where(AIRun.status == status.upper())
    rows = list(db.scalars(query)); grouped = defaultdict(lambda: {"total": 0, "success": 0, "failed": 0, "latencies_ms": [], "tokens": 0})
    for row in rows:
        key = f"{row.run_type}:{row.model}"; item = grouped[key]; item["total"] += 1; item["success"] += row.status == "SUCCESS"; item["failed"] += row.status == "FAILED"; latency = _latency_ms(row.started_at, row.completed_at)
        if latency is not None and latency >= 0: item["latencies_ms"].append(latency)
        usage = (row.output_json or {}).get("usage", {}) if isinstance(row.output_json, dict) else {}; item["tokens"] += int(usage.get("total_tokens", 0) or 0)
    for item in grouped.values(): item["average_latency_ms"] = round(mean(item.pop("latencies_ms")), 2) if item.get("latencies_ms") else None
    total = len(rows); failed = sum(row.status == "FAILED" for row in rows)
    return {"period": period, "total_runs": total, "success": total - failed, "failed": failed, "failure_rate": round(failed / total, 4) if total else None, "groups": dict(grouped), "token_usage_available": any(item["tokens"] for item in grouped.values()), "total_tokens": sum(item["tokens"] for item in grouped.values())}


def opportunities(db: Session, period: str = "24h") -> dict:
    since, until = window(period); rows = list(db.scalars(select(Opportunity).where(Opportunity.created_at >= since, Opportunity.created_at <= until).order_by(desc(Opportunity.score)).limit(1000))); product_counts = Counter(); industry_counts = Counter(); company_counts = Counter()
    for row in rows:
        product = db.get(ProductMatch, row.product_match_id) if row.product_match_id else None; event = db.get(Event, row.event_id); demand = db.scalar(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id == row.event_id)); product_counts[product.product_family or "UNKNOWN"] += 1 if product else 0; industry_counts[demand.industry_code if demand else "UNKNOWN"] += 1; company_counts[event.company_id or "UNKNOWN"] += 1 if event else 0
    return {"period": period, "new": len(rows), "high_priority": sum(row.score >= 80 for row in rows), "qualified": sum(row.status in {"QUALIFIED", "NEW"} for row in rows), "dismissed": sum(row.status == "DISMISSED" for row in rows), "average_score": round(mean([row.score for row in rows]), 2) if rows else None, "top_product_families": product_counts.most_common(10), "top_industries": industry_counts.most_common(10), "top_companies": company_counts.most_common(10)}


def knowledge_gaps(db: Session, period: str = "30d") -> dict:
    since, until = window(period); rows = list(db.execute(select(ProductMatch, SteelDemandHypothesis, Opportunity).join(SteelDemandHypothesis, ProductMatch.steel_demand_hypothesis_id == SteelDemandHypothesis.id).join(Event, SteelDemandHypothesis.event_id == Event.id).join(Opportunity, Opportunity.event_id == Event.id, isouter=True).where(ProductMatch.created_at >= since, ProductMatch.created_at <= until, or_(ProductMatch.status.in_(["UNKNOWN", "PRODUCT_KNOWLEDGE_PENDING", "REVIEW_REQUIRED"]), ProductMatch.product_family.is_(None), ProductMatch.reasoning_summary.ilike("%PRODUCT_KNOWLEDGE_PENDING%"))).limit(1000)))
    grouped = defaultdict(lambda: {"occurrences": 0, "high_score_blocked": 0, "last_seen": None})
    for product, demand, opportunity in rows:
        key = (demand.industry_code or "UNKNOWN", demand.application_code or "UNKNOWN", demand.material_category or "UNKNOWN", product.product_family or "UNKNOWN"); item = grouped[key]; item["occurrences"] += 1; item["high_score_blocked"] += bool(opportunity and opportunity.score >= 80); item["last_seen"] = max(item["last_seen"] or product.created_at, product.created_at); item["status"] = product.status
    result = []
    for key, item in grouped.items():
        recency = min(20, int((_age(item["last_seen"], datetime.now(timezone.utc)) or 0) / 86400))
        item["priority"] = min(100, item["occurrences"] * 10 + item["high_score_blocked"] * 10 + max(0, 20 - recency)); result.append({"industry": key[0], "application": key[1], "material_category": key[2], "requested_product_family": key[3], **item})
    return {"period": period, "count": len(rows), "gaps": sorted(result, key=lambda item: item["priority"], reverse=True)}


def delivery(db: Session, period: str = "24h") -> dict:
    since, until = window(period); alerts = list(db.scalars(select(AlertDelivery).where(AlertDelivery.created_at >= since, AlertDelivery.created_at <= until).order_by(desc(AlertDelivery.created_at)).limit(1000))); digests = list(db.scalars(select(DigestDelivery).where(DigestDelivery.created_at >= since, DigestDelivery.created_at <= until).limit(1000))); rows = alerts + digests; counts = Counter(row.status for row in rows); pending = [row for row in rows if row.status in {"PENDING", "RETRY_PENDING"}]; failed = [row for row in rows if row.status == "FAILED"]; return {"period": period, "status_counts": dict(counts), "alert_deliveries": len(alerts), "digest_deliveries": len(digests), "success_rate": round(counts["DELIVERED"] / len(rows) * 100, 2) if rows else None, "failure_rate": round(counts["FAILED"] / len(rows) * 100, 2) if rows else None, "average_attempts": round(mean([row.attempt_count for row in rows]), 2) if rows else None, "pending_backlog": len(pending), "oldest_pending_age_seconds": min((_age(row.created_at, datetime.now(timezone.utc)) for row in pending), default=None), "failures": [{"time": row.created_at, "delivery_id": row.id, "attempts": row.attempt_count, "error_code": row.error_code, "error_message": row.error_message} for row in failed[:20]]}


def digest(db: Session, period: str = "30d") -> dict:
    since, until = window(period); rows = list(db.scalars(select(IntelligenceDigest).where(IntelligenceDigest.created_at >= since, IntelligenceDigest.created_at <= until).order_by(desc(IntelligenceDigest.created_at)).limit(200))); delivery_rows = list(db.scalars(select(DigestDelivery).where(DigestDelivery.created_at >= since, DigestDelivery.created_at <= until))); return {"period": period, "daily_generated": sum(row.digest_type == "DAILY" for row in rows), "weekly_generated": sum(row.digest_type == "WEEKLY" for row in rows), "status_counts": dict(Counter(row.status for row in rows)), "delivery_status_counts": dict(Counter(row.status for row in delivery_rows)), "last_success_daily": next((row.generated_at for row in rows if row.digest_type == "DAILY" and row.status == "READY"), None), "last_success_weekly": next((row.generated_at for row in rows if row.digest_type == "WEEKLY" and row.status == "READY"), None), "failures": [{"id": row.id, "digest_type": row.digest_type, "period_start": row.period_start, "period_end": row.period_end, "status": row.status} for row in rows if row.status == "FAILED"]}


def quality(db: Session, period: str = "30d") -> dict:
    rows = list(db.scalars(select(EvaluationRun).order_by(desc(EvaluationRun.completed_at)).limit(2))); latest = rows[0] if rows else None; baseline = rows[1] if len(rows) > 1 else None; current = (latest.summary_json or {}) if latest else {}; previous = (baseline.summary_json or {}) if baseline else {}; critical = {key: value for key, value in (current.get("error_counts") or {}).items() if key in {"EVIDENCE_NOT_IN_SOURCE", "FALSE_EVENT_MERGE", "FORBIDDEN_PRODUCT_ROUTE", "GRADE_HALLUCINATION"} and value}; deltas = {key: round(value - previous[key], 2) for key, value in current.items() if isinstance(value, (int, float)) and isinstance(previous.get(key), (int, float))}; regressions = [key for key, delta in deltas.items() if ("rate" in key or "hallucination" in key or "duplicate" in key) and delta > 0 or key not in {"grade_hallucination_rate", "duplicate_opportunity_rate", "evidence_validity_rate"} and delta < 0]; return {"latest": {"id": latest.id, "status": latest.status, "completed_at": latest.completed_at, "summary": current} if latest else None, "baseline": {"id": baseline.id, "summary": previous} if baseline else None, "deltas": deltas, "quality_regression": bool(critical or regressions), "critical_errors": critical, "regressions": regressions}


def stale_jobs(db: Session) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=settings.ops_stale_job_minutes)
    jobs = []
    for row in db.scalars(select(CollectionRun).where(CollectionRun.status == "RUNNING", CollectionRun.started_at < cutoff).limit(50)):
        jobs.append({"category": "COLLECTION", "reference": row.id, "started_at": row.started_at, "status": row.status})
    for row in db.scalars(select(AIRun).where(AIRun.status == "RUNNING", AIRun.created_at < cutoff).limit(50)):
        jobs.append({"category": "AI", "reference": row.id, "started_at": row.started_at, "status": row.status})
    for row in db.scalars(select(AlertDelivery).where(AlertDelivery.status == "SENDING", AlertDelivery.created_at < cutoff).limit(50)):
        jobs.append({"category": "DELIVERY", "reference": row.id, "started_at": row.created_at, "status": row.status})
    for row in db.scalars(select(IntelligenceDigest).where(IntelligenceDigest.status.in_(["GENERATING", "PROCESSING"]), IntelligenceDigest.created_at < cutoff).limit(50)):
        jobs.append({"category": "DIGEST", "reference": row.id, "started_at": row.created_at, "status": row.status})
    return jobs
