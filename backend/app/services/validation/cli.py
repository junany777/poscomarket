import argparse
import csv
import json
import sys

from app.core.database import SessionLocal, init_db
from app.models.entities import ValidationRun, ValidationRunSource, ValidationStage
from app.services.validation.runner import run_validation


def _run(args):
    init_db(); db = SessionLocal()
    try:
        result = run_validation(db, source_limit=args.source_limit, source_ids=args.source_id, real_collection=args.real, source_codes=args.source_code, delivery_dry_run=args.delivery_dry_run, name=args.name)
        print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
        return 0
    finally:
        db.close()


def _quality_gate(args):
    db = SessionLocal()
    try:
        row = db.get(ValidationRun, args.run)
        if not row: print(f"validation run not found: {args.run}", file=sys.stderr); return 2
        gate = (row.summary_json or {}).get("quality_gate", {})
        print(json.dumps(gate, ensure_ascii=False, indent=2))
        return 0 if gate.get("passed") else 1
    finally:
        db.close()


def _report(args):
    db = SessionLocal()
    try:
        row = db.get(ValidationRun, args.run)
        if not row: print(f"validation run not found: {args.run}", file=sys.stderr); return 2
        payload = {"id": row.id, "name": row.name, "status": row.status, "started_at": row.started_at, "completed_at": row.completed_at, "counts": {"sources": row.source_document_count, "events": row.event_count, "clusters": row.cluster_count, "opportunities": row.opportunity_count, "alerts": row.alert_count, "deliveries": row.delivery_count, "digests": row.digest_count}, "summary": row.summary_json}
        if args.format == "csv":
            writer = csv.writer(sys.stdout); writer.writerow(["source_document_id", "review_status"])
            for item in db.scalars(__import__("sqlalchemy", fromlist=["select"]).select(ValidationRunSource).where(ValidationRunSource.validation_run_id == row.id)): writer.writerow([item.source_document_id, item.review_status])
        else: print(json.dumps(payload, ensure_ascii=False, default=str, indent=2))
        return 0
    finally:
        db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Steel Market real-world validation")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, real in (("run", False), ("run-real", True)):
        command = sub.add_parser(name); command.set_defaults(real=real, handler=_run); command.add_argument("--source-limit", type=int, default=100); command.add_argument("--source-id", action="append"); command.add_argument("--source-code", action="append"); command.add_argument("--delivery-dry-run", action="store_true", default=real); command.add_argument("--name", default="Real-World E2E Validation" if real else "Controlled E2E Validation")
    gate = sub.add_parser("quality-gate"); gate.set_defaults(handler=_quality_gate); gate.add_argument("--run", required=True)
    report = sub.add_parser("report"); report.set_defaults(handler=_report); report.add_argument("--run", required=True); report.add_argument("--format", choices=["json", "csv"], default="json")
    args = parser.parse_args(); raise SystemExit(args.handler(args))


if __name__ == "__main__":
    main()
