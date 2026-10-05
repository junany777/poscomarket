import argparse
import json

from app.core.database import SessionLocal
from app.models.entities import PerformanceBenchmark
from app.services.performance.service import benchmark_validation, compare_benchmarks


def main() -> None:
    parser = argparse.ArgumentParser(description="Steel Market performance benchmark")
    sub = parser.add_subparsers(dest="command", required=True)
    benchmark = sub.add_parser("benchmark"); benchmark.add_argument("--validation-run", required=True); benchmark.add_argument("--name")
    compare = sub.add_parser("compare"); compare.add_argument("--baseline", required=True); compare.add_argument("--candidate", required=True)
    args = parser.parse_args(); db = SessionLocal()
    try:
        if args.command == "benchmark": result = benchmark_validation(db, args.validation_run, args.name)
        else: result = compare_benchmarks(db, args.baseline, args.candidate)
        print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
    finally: db.close()


if __name__ == "__main__": main()
