import hashlib
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import SourceDocument
from app.schemas import SourceCreate


def create_source(db: Session, payload: SourceCreate) -> tuple[SourceDocument, bool]:
    digest = hashlib.sha256(payload.content.strip().encode("utf-8")).hexdigest()
    existing = db.scalar(select(SourceDocument).where(SourceDocument.content_hash == digest))
    if existing:
        return existing, True
    item = SourceDocument(
        source_type=payload.source_type.upper(), source_name=payload.source_name, source_url=payload.source_url,
        title=payload.title, published_at=payload.published_at.isoformat() if payload.published_at else None,
        collected_at=datetime.now(timezone.utc).isoformat(), content=payload.content.strip(), content_hash=digest,
        language=payload.language, status="READY_FOR_ANALYSIS", metadata_json=payload.metadata_json,
    )
    db.add(item); db.commit(); db.refresh(item)
    return item, False

