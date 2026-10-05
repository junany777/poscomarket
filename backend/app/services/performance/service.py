from datetime import datetime, timezone
from statistics import mean

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.entities import AIRun, PerformanceBenchmark, ValidationRun
from app.services.product_brain.loader import product_load_stats


def _latency_ms(started: str | None, completed: str | None) -> float | None:
    if not started or not completed: return None
    try: return max(0.0, (datetime.fromisoformat(completed.replace("Z", "+00:00")) - datetime.fromisoformat(started.replace("Z", "+00:00"))).total_seconds() * 1000)
    except ValueError: return None


def benchmark_validation(db: Session, validation_run_id: str, name: str | None = None) -> dict:
    validation = db.get(ValidationRun, validation_run_id)
    if not validation: raise ValueError("validation run not found")
    end = validation.completed_at or datetime.now(timezone.utc); rows = list(db.scalars(select(AIRun).where(AIRun.created_at >= validation.started_at, AIRun.created_at <= end)))
    actual_calls = [row for row in rows if not row.cache_hit and row.status != "CACHE_HIT"]; latencies = [value for row in rows if (value := _latency_ms(row.started_at, row.completed_at)) is not None]; input_tokens = 0; output_tokens = 0; inventory = {}
    for row in rows:
        usage = (row.output_json or {}).get("usage", {}) if isinstance(row.output_json, dict) else {}; input_value = int(usage.get("prompt_tokens", usage.get("input_tokens", 0)) or 0); output_value = int(usage.get("completion_tokens", usage.get("output_tokens", 0)) or 0); input_tokens += input_value; output_tokens += output_value; bucket = inventory.setdefault(row.run_type, {"calls": 0, "cache_hits": 0, "input_tokens": 0, "output_tokens": 0, "latencies_ms": []}); bucket["calls"] += not row.cache_hit and row.status != "CACHE_HIT"; bucket["cache_hits"] += bool(row.cache_hit or row.status == "CACHE_HIT"); bucket["input_tokens"] += input_value; bucket["output_tokens"] += output_value; value = _latency_ms(row.started_at, row.completed_at)
        if value is not None: bucket["latencies_ms"].append(value)
    for bucket in inventory.values(): bucket["average_latency_ms"] = round(mean(bucket.pop("latencies_ms")), 2) if bucket.get("latencies_ms") else None
    product_stats = (validation.summary_json or {}).get("product_brain") or product_load_stats()
    started = validation.started_at; benchmark = PerformanceBenchmark(name=name or f"Benchmark {validation.name}", validation_run_id=validation.id, started_at=started, completed_at=end, metrics_json={})
    metrics = {"total_runtime_seconds": max(0.0, (end - started).total_seconds()), "documents_processed": validation.source_document_count, "events_processed": validation.event_count, "clusters_processed": validation.cluster_count, "opportunities_created": validation.opportunity_count, "ai_call_count": len(actual_calls), "ai_cache_hits": sum(row.cache_hit or row.status == "CACHE_HIT" for row in rows), "ai_cache_misses": len(actual_calls), "ai_input_tokens": input_tokens, "ai_output_tokens": output_tokens, "average_ai_latency_ms": round(mean(latencies), 2) if latencies else None, "p95_ai_latency_ms": sorted(latencies)[max(0, int(len(latencies) * .95) - 1)] if latencies else None, "ai_inventory": inventory, "product_files_loaded": product_stats.get("files_loaded", 0), "product_cache_hit_rate": product_stats.get("cache_hit_rate"), "ask_latency_ms": None, "digest_latency_ms": None, "token_usage_available": bool(input_tokens or output_tokens), "ai_calls_per_source": round(len(actual_calls) / validation.source_document_count, 4) if validation.source_document_count else None, "input_tokens_per_source": round(input_tokens / validation.source_document_count, 2) if validation.source_document_count else None, "runtime_per_source_seconds": round(max(0.0, (end - started).total_seconds()) / validation.source_document_count, 4) if validation.source_document_count else None, "quality_gate": (validation.summary_json or {}).get("quality_gate", {})}
    benchmark.metrics_json = metrics; db.add(benchmark); db.commit(); db.refresh(benchmark)
    return {"id": benchmark.id, "name": benchmark.name, "validation_run_id": validation.id, "metrics": metrics}


def compare_benchmarks(db: Session, baseline_id: str, candidate_id: str) -> dict:
    baseline = db.get(PerformanceBenchmark, baseline_id); candidate = db.get(PerformanceBenchmark, candidate_id)
    if not baseline or not candidate: raise ValueError("benchmark not found")
    keys = sorted(set((baseline.metrics_json or {}).keys()) & set((candidate.metrics_json or {}).keys())); rows = []
    for key in keys:
        old, new = baseline.metrics_json.get(key), candidate.metrics_json.get(key)
        if isinstance(old, (int, float)) and isinstance(new, (int, float)): rows.append({"metric": key, "baseline": old, "candidate": new, "delta": round(new - old, 4), "delta_pct": round((new - old) / old * 100, 2) if old else None})
    quality = {"baseline": baseline.metrics_json.get("quality_gate"), "candidate": candidate.metrics_json.get("quality_gate"), "non_regressive": bool((candidate.metrics_json.get("quality_gate") or {}).get("passed", False))}
    return {"baseline_id": baseline.id, "candidate_id": candidate.id, "metrics": rows, "quality": quality}
