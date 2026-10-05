import argparse
import asyncio
import json
import sys

from app.core.database import SessionLocal, init_db
from app.core.config import settings
from app.services.evaluation.runner import run_evaluation
from app.models.entities import EvaluationRun
from app.services.evaluation.comparison import compare_summaries


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Steel Intelligence quality evaluation")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--dataset", default=settings.evaluation_dataset_path)
    run.add_argument("--mode", choices=["live", "replay"], default="live")
    run.add_argument("--limit", type=int)
    run.add_argument("--subset")
    gate = sub.add_parser("quality-gate")
    gate.add_argument("--dataset", default=settings.evaluation_dataset_path)
    gate.add_argument("--mode", choices=["live", "replay"], default="live")
    gate.add_argument("--limit", type=int)
    gate.add_argument("--run")
    gate.add_argument("--subset")
    compare = sub.add_parser("compare")
    compare.add_argument("--baseline", required=True)
    compare.add_argument("--candidate", required=True)
    compare.add_argument("--target-metric")
    args = parser.parse_args()
    init_db()
    db = SessionLocal()
    try:
        if args.command == "compare":
            baseline, candidate = db.get(EvaluationRun, args.baseline), db.get(EvaluationRun, args.candidate)
            if not baseline or not candidate: raise SystemExit("baseline and candidate runs must exist")
            result = compare_summaries(baseline.summary_json, candidate.summary_json, args.target_metric)
        elif args.command == "quality-gate" and args.run:
            run_row = db.get(EvaluationRun, args.run)
            if not run_row: raise SystemExit("evaluation run not found")
            result = {"id": run_row.id, "summary": run_row.summary_json, "status": run_row.status}
        else:
            result = run_evaluation(db, args.dataset, args.mode, args.limit, args.subset)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
        if args.command == "quality-gate":
            summary = result["summary"]
            failed = summary.get("evidence_validity_rate", 0) < 100 or summary.get("grade_hallucination_rate", 0) > 0 or summary.get("product_family_accuracy", 0) < 90 or summary.get("explainability_completeness", 0) < 95
            if failed:
                raise SystemExit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
