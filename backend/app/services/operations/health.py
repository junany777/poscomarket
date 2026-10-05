from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select, text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import AIRun, AlertDelivery, CollectionRun, EvaluationRun, IntelligenceDigest, SourceDocument


ORDER = {"HEALTHY": 0, "UNKNOWN": 1, "DEGRADED": 2, "FAILED": 3}


def _component(name: str, state: str, reason: str, checked_at: datetime | None = None) -> dict:
    return {"name": name, "status": state, "reason": reason, "checked_at": checked_at or datetime.now(timezone.utc)}


def component_health(db: Session) -> dict:
    now = datetime.now(timezone.utc)
    result = {}
    try:
        db.execute(text("SELECT 1"))
        result["DATABASE"] = _component("DATABASE", "HEALTHY", "basic query succeeded", now)
    except Exception as exc:
        result["DATABASE"] = _component("DATABASE", "FAILED", "database query failed", now)
        return result

    runs = list(db.scalars(select(CollectionRun).order_by(CollectionRun.created_at.desc()).limit(3)))
    if not runs:
        result["NEWS_COLLECTOR"] = _component("NEWS_COLLECTOR", "UNKNOWN", "no collection history")
    else:
        last_success = next((run for run in runs if run.status in {"COMPLETED", "PARTIAL"}), None)
        stale = not last_success or (now - (last_success.completed_at or last_success.created_at).replace(tzinfo=timezone.utc) > timedelta(minutes=settings.ops_collection_stale_minutes))
        failed = sum(run.status == "FAILED" for run in runs)
        state = "FAILED" if stale and not last_success else "DEGRADED" if failed >= 2 or stale else "HEALTHY"
        result["NEWS_COLLECTOR"] = _component("NEWS_COLLECTOR", state, f"last_success={last_success.id if last_success else 'none'}; failures_last_3={failed}", last_success.completed_at if last_success else runs[0].created_at)

    backlog_statuses = ["READY_FOR_INTELLIGENCE", "PROCESSING", "REVIEW_REQUIRED"]
    source_backlog = db.scalar(select(func.count()).select_from(SourceDocument).where(SourceDocument.status.in_(backlog_statuses))) or 0
    oldest_backlog = db.scalar(select(SourceDocument.created_at).where(SourceDocument.status.in_(backlog_statuses)).order_by(SourceDocument.created_at).limit(1))
    backlog_stale = oldest_backlog and now - oldest_backlog.replace(tzinfo=timezone.utc) > timedelta(minutes=settings.ops_pipeline_stale_minutes)
    result["INTELLIGENCE_PIPELINE"] = _component("INTELLIGENCE_PIPELINE", "DEGRADED" if source_backlog >= settings.ops_backlog_warning_threshold or backlog_stale else "HEALTHY", f"source_backlog={source_backlog}; backlog_stale={bool(backlog_stale)}")

    ai_runs = list(db.scalars(select(AIRun).order_by(AIRun.created_at.desc()).limit(100)))
    failed_ai = sum(item.status == "FAILED" for item in ai_runs)
    ai_state = "UNKNOWN" if not ai_runs else "DEGRADED" if failed_ai / len(ai_runs) >= settings.ops_ai_failure_rate_threshold else "HEALTHY"
    result["OPENAI"] = _component("OPENAI", ai_state, f"recent_runs={len(ai_runs)}; failure_rate={round(failed_ai / len(ai_runs), 3) if ai_runs else None}")

    delivery_failures = db.scalar(select(func.count()).select_from(AlertDelivery).where(AlertDelivery.status == "FAILED")) or 0
    result["ALERT_DELIVERY"] = _component("ALERT_DELIVERY", "DEGRADED" if delivery_failures >= settings.ops_delivery_failure_threshold else "HEALTHY", f"failed_deliveries={delivery_failures}")

    latest_digest = db.scalar(select(IntelligenceDigest).order_by(IntelligenceDigest.period_end.desc()))
    result["DIGEST"] = _component("DIGEST", "UNKNOWN" if not latest_digest else "HEALTHY" if latest_digest.status == "READY" else "DEGRADED", f"latest_status={latest_digest.status if latest_digest else 'none'}")
    latest_eval = db.scalar(select(EvaluationRun).order_by(EvaluationRun.completed_at.desc()))
    result["EVALUATION"] = _component("EVALUATION", "UNKNOWN" if not latest_eval else "HEALTHY" if latest_eval.status == "COMPLETED" else "DEGRADED", f"latest_status={latest_eval.status if latest_eval else 'none'}")
    return result


def overall_status(components: dict) -> str:
    statuses = [item["status"] for item in components.values()]
    if "FAILED" in statuses: return "FAILED"
    if any(status in {"DEGRADED", "UNKNOWN"} for status in statuses): return "DEGRADED"
    return "HEALTHY" if statuses else "DEGRADED"
