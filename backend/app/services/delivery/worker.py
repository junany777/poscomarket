import asyncio
from app.core.config import settings
from app.core.database import SessionLocal, init_db
from app.services.delivery.service import process_pending


async def run() -> None:
    init_db()
    while True:
        db = SessionLocal()
        try:
            await process_pending(db)
        finally:
            db.close()
        await asyncio.sleep(settings.delivery_worker_poll_seconds)


if __name__ == "__main__": asyncio.run(run())
