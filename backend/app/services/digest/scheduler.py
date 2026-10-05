from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.config import settings
from app.core.database import SessionLocal
from app.services.delivery.service import enqueue_digest
from app.services.digest import generate_digest


def generate_scheduled(digest_type: str) -> dict:
    db = SessionLocal()
    try:
        result = generate_digest(db, digest_type)
        if result.get("id") and not result.get("deduplicated"):
            enqueue_digest(db, result["id"])
        return result
    finally:
        db.close()


def build_scheduler() -> BlockingScheduler:
    scheduler = BlockingScheduler(timezone=settings.digest_timezone)
    scheduler.add_job(lambda: generate_scheduled("DAILY"), CronTrigger(hour=settings.digest_daily_hour, minute=settings.digest_daily_minute, timezone=settings.digest_timezone), id="daily-digest", replace_existing=True)
    scheduler.add_job(lambda: generate_scheduled("WEEKLY"), CronTrigger(day_of_week=settings.digest_weekly_day, hour=settings.digest_weekly_hour, minute=settings.digest_weekly_minute, timezone=settings.digest_timezone), id="weekly-digest", replace_existing=True)
    return scheduler


def main() -> None:
    if not settings.digest_scheduler_enabled:
        raise SystemExit("DIGEST_SCHEDULER_ENABLED=true is required")
    build_scheduler().start()


if __name__ == "__main__":
    main()
