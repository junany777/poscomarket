import logging

from sqlalchemy.orm import Session

from app.models.entities import SourceDocument
from app.services.pipeline import run_intelligence_pipeline

logger = logging.getLogger(__name__)


def reprocess_source(db: Session, source_id: str) -> dict:
    source = db.get(SourceDocument, source_id)
    if not source: raise ValueError("source document not found")
    if source.status not in {"FAILED", "REVIEW_REQUIRED"}: raise ValueError("only FAILED or REVIEW_REQUIRED sources can be reprocessed")
    logger.info("ops_reprocess_started", extra={"source_id": source_id})
    result = run_intelligence_pipeline(db, source_id)
    source.status = "PROCESSED"
    db.commit()
    return {"source_id": source_id, "status": source.status, "result": result}
