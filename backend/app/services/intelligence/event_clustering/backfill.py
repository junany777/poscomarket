from app.core.config import settings
from app.core.database import SessionLocal, init_db
from app.models.entities import Event, SourceDocument
from app.services.intelligence.event_clustering import assign_event_to_cluster
from sqlalchemy import select


def run_backfill() -> int:
    init_db()
    total = 0
    while True:
        db = SessionLocal()
        try:
            events = list(db.scalars(select(Event).where(Event.event_cluster_id.is_(None)).order_by(Event.created_at).limit(settings.event_cluster_backfill_batch_size)))
            if not events:
                return total
            for event in events:
                assign_event_to_cluster(db, event, db.get(SourceDocument, event.source_document_id))
                total += 1
            db.commit()
        finally:
            db.close()


if __name__ == "__main__":
    print(f"backfilled_events={run_backfill()}")
