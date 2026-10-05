import logging

from sqlalchemy.orm import Session
from sqlalchemy import desc, select
from app.models.entities import PerformanceBenchmark

from app.services.operations.health import component_health, overall_status
from app.services.operations.metrics import ai_runs, collection, delivery, digest, knowledge_gaps, opportunities, pipeline, quality, stale_jobs

logger = logging.getLogger(__name__)


def admin_overview(db: Session, period: str = "24h") -> dict:
    components = component_health(db)
    stuck_jobs = stale_jobs(db)
    if stuck_jobs:
        components["INTELLIGENCE_PIPELINE"]["status"] = "DEGRADED"
        components["INTELLIGENCE_PIPELINE"]["reason"] += f"; stuck_jobs={len(stuck_jobs)}"
    latest_benchmark = db.scalar(select(PerformanceBenchmark).order_by(desc(PerformanceBenchmark.created_at)))
    result = {"system_status": overall_status(components), "components": components, "collection": collection(db, period), "pipeline": pipeline(db, period), "ai": ai_runs(db, period), "opportunities": opportunities(db, period), "product_knowledge": knowledge_gaps(db, "30d"), "delivery": delivery(db, period), "digest": digest(db, "30d"), "quality": quality(db, "30d"), "performance": latest_benchmark.metrics_json if latest_benchmark else None, "stale_jobs": stuck_jobs, "period": period}
    logger.info("ops_overview_requested", extra={"period": period, "system_status": result["system_status"]})
    return result
