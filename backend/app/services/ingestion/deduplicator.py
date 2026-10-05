from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import SourceDocument
from app.services.ingestion.collectors.base import CollectedItem


def find_duplicate(db: Session, item: CollectedItem) -> SourceDocument | None:
    content_hash = item.metadata.get("content_hash")
    if content_hash:
        existing = db.scalar(select(SourceDocument).where(SourceDocument.content_hash == content_hash))
        if existing:
            return existing
    canonical_url = item.metadata.get("canonical_url")
    if canonical_url:
        return db.scalar(select(SourceDocument).where(SourceDocument.metadata_json["canonical_url"].as_string() == canonical_url))
    return None
