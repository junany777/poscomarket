import argparse
import asyncio
from sqlalchemy import select
from app.core.database import SessionLocal, init_db
from app.models.entities import Alert
from app.services.delivery import enqueue_alert, process_pending


async def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("command", choices=["enqueue-existing", "process"]); parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(); init_db(); db = SessionLocal()
    try:
        if args.command == "enqueue-existing":
            count = 0
            for alert in db.scalars(select(Alert).order_by(Alert.created_at)):
                enqueue_alert(db, alert.id); count += 1
            print(f"alerts_enqueued={count}")
        else:
            print(await process_pending(db, dry_run=args.dry_run))
    finally: db.close()


if __name__ == "__main__": asyncio.run(main())
