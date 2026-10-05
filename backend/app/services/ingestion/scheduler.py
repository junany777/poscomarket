from apscheduler.schedulers.blocking import BlockingScheduler

from app.core.config import settings
from app.core.database import SessionLocal, init_db
from app.services.ingestion.collection_service import collect_sources
import asyncio


def build_scheduler(job):
    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(job, "interval", minutes=30, id="news-collector", max_instances=1, coalesce=True)
    return scheduler


def scheduler_enabled() -> bool:
    return settings.news_scheduler_enabled


def run_once() -> None:
    init_db()
    db = SessionLocal()
    try:
        asyncio.run(collect_sources(db))
    finally:
        db.close()


def main() -> None:
    if not scheduler_enabled():
        raise SystemExit("NEWS_SCHEDULER_ENABLED is false; set it to true to start the collector process")
    scheduler = build_scheduler(run_once)
    scheduler.start()


if __name__ == "__main__":
    main()
