import argparse

from app.core.database import SessionLocal
from app.services.delivery.service import enqueue_digest
from app.services.digest import generate_digest


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Steel Intelligence digests")
    parser.add_argument("--type", choices=["daily", "weekly"], default="daily")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    db = SessionLocal()
    try:
        result = generate_digest(db, args.type.upper())
        if not args.dry_run and result.get("id") and not result.get("deduplicated"):
            result["deliveries_enqueued"] = enqueue_digest(db, result["id"])
        print(result)
    finally:
        db.close()


if __name__ == "__main__":
    main()
