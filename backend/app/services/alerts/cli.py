import argparse

from sqlalchemy import desc, select

from app.core.config import settings
from app.core.database import SessionLocal, init_db
from app.models.entities import Opportunity
from app.services.alerts.service import evaluate_opportunity


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluate-existing", nargs="?")
    args = parser.parse_args()
    init_db(); db = SessionLocal(); count = 0
    try:
        for opportunity in db.scalars(select(Opportunity).order_by(desc(Opportunity.created_at)).limit(settings.alert_backfill_batch_size)):
            evaluate_opportunity(db, opportunity.id); count += 1
        print(f"opportunities_evaluated={count}")
    finally:
        db.close()


if __name__ == "__main__": main()
