import logging
import time
from datetime import datetime, timedelta, timezone

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.entities import Alert, AlertDelivery, Event, EventCluster, Opportunity, ProductMatch, SourceDocument, SteelDemandHypothesis, ValidationRun, ValidationRunSource, ValidationStage
from app.services.digest import generate_digest
from app.services.delivery.service import enqueue_digest
from app.services.ingestion.collection_service import collect_sources
from app.services.operations.overview import admin_overview
from app.services.pipeline import run_intelligence_pipeline
from app.services.validation.audit import duplicate_audit, evidence_audit, integrity_audit, taxonomy_audit
from app.services.validation.gate import evaluate_quality_gate
from app.services.product_brain.loader import product_load_stats

logger = logging.getLogger(__name__)


def _stage(db, run_id, name, input_count, success_count, failure_count=0, skipped_count=0, duration_ms=None, errors=None):
    db.add(ValidationStage(validation_run_id=run_id, stage=name, input_count=input_count, success_count=success_count, failure_count=failure_count, skipped_count=skipped_count, duration_ms=duration_ms, errors_json=errors or []))


def _selected_ids(db: Session, source_ids: list[str] | None, source_limit: int) -> list[str]:
    if source_ids: return source_ids[:source_limit]
    return list(db.scalars(select(SourceDocument.id).where(SourceDocument.status.in_(["READY_FOR_INTELLIGENCE", "PROCESSED", "REVIEW_REQUIRED", "FAILED"])).order_by(desc(SourceDocument.created_at)).limit(source_limit)))


def run_validation(db: Session, source_limit: int = 100, source_ids: list[str] | None = None, real_collection: bool = False, source_codes: list[str] | None = None, delivery_dry_run: bool = True, name: str = "Controlled E2E Validation") -> dict:
    started = datetime.now(timezone.utc); product_load_stats(reset=True); validation = ValidationRun(name=name, started_at=started, status="RUNNING", summary_json={}); db.add(validation); db.commit()
    all_source_ids: list[str] = []; errors: list[dict] = []
    try:
        collection_results = []
        if real_collection:
            collection_results = __import__("asyncio").run(collect_sources(db, source_codes=source_codes, dry_run=False))
            all_source_ids = [source_id for item in collection_results for source_id in item.get("source_document_ids", [])]
            all_source_ids = all_source_ids[:source_limit]
        else:
            all_source_ids = _selected_ids(db, source_ids, source_limit)
        for source_id in all_source_ids: db.add(ValidationRunSource(validation_run_id=validation.id, source_document_id=source_id))
        db.commit()
        collection_input = sum(item.get("items_seen", 0) for item in collection_results) if collection_results else len(all_source_ids)
        _stage(db, validation.id, "COLLECTION", collection_input, sum(item.get("status") in {"COMPLETED", "PARTIAL"} for item in collection_results) if collection_results else len(all_source_ids), sum(item.get("status") == "FAILED" for item in collection_results), duration_ms=None)
        _stage(db, validation.id, "DOCUMENT_DEDUPLICATION", collection_input, sum(item.get("items_new", 0) for item in collection_results) if collection_results else len(all_source_ids), errors=[{"type": "DUPLICATE", "count": sum(item.get("items_duplicate", 0) for item in collection_results)}] if collection_results else [])
        _stage(db, validation.id, "RELEVANCE_FILTER", collection_input, len(all_source_ids), max(0, collection_input - len(all_source_ids)))

        pipeline_start = time.perf_counter(); processed = 0
        for source_id in all_source_ids:
            source = db.get(SourceDocument, source_id)
            if not source or source.status == "PROCESSED":
                if source and source.status == "PROCESSED": processed += 1
                continue
            try:
                run_intelligence_pipeline(db, source_id); processed += 1
            except Exception as exc:
                errors.append({"source_document_id": source_id, "stage": "INTELLIGENCE", "error": str(exc)[:240]})
        _stage(db, validation.id, "EVENT_EXTRACTION", len(all_source_ids), processed, len(all_source_ids) - processed, duration_ms=round((time.perf_counter() - pipeline_start) * 1000, 2), errors=errors)
        event_ids = list(db.scalars(select(Event.id).where(Event.source_document_id.in_(all_source_ids)))) if all_source_ids else []
        cluster_ids = list(db.scalars(select(Event.event_cluster_id).where(Event.id.in_(event_ids), Event.event_cluster_id.is_not(None)))) if event_ids else []
        demand_count = int(db.scalar(select(__import__("sqlalchemy", fromlist=["func"]).func.count()).select_from(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id.in_(event_ids))) or 0) if event_ids else 0
        product_count = int(db.scalar(select(__import__("sqlalchemy", fromlist=["func"]).func.count()).select_from(ProductMatch).join(SteelDemandHypothesis, ProductMatch.steel_demand_hypothesis_id == SteelDemandHypothesis.id).where(SteelDemandHypothesis.event_id.in_(event_ids))) or 0) if event_ids else 0
        opportunities = list(db.scalars(select(Opportunity).where(Opportunity.event_id.in_(event_ids)))) if event_ids else []
        _stage(db, validation.id, "EVENT_CLUSTERING", len(event_ids), len(set(cluster_ids)), 0, len(event_ids) - len(set(cluster_ids)))
        _stage(db, validation.id, "STRATEGY_INFERENCE", len(event_ids), processed)
        _stage(db, validation.id, "STEEL_DEMAND_INFERENCE", len(event_ids), demand_count)
        _stage(db, validation.id, "PRODUCT_MATCH", demand_count, product_count)
        _stage(db, validation.id, "OPPORTUNITY", product_count, len(opportunities))
        alert_ids = list(db.scalars(select(Alert.id).where(Alert.opportunity_id.in_([item.id for item in opportunities])))) if opportunities else []
        delivery_ids = list(db.scalars(select(AlertDelivery.id).where(AlertDelivery.alert_id.in_(alert_ids)))) if alert_ids else []
        _stage(db, validation.id, "WATCHLIST_ALERT", len(opportunities), len(alert_ids))
        _stage(db, validation.id, "DELIVERY", len(alert_ids), len(delivery_ids), skipped_count=len(alert_ids) - len(delivery_ids))
        digest_result = generate_digest(db, "DAILY", started, datetime.now(timezone.utc)); digest_id = digest_result.get("id")
        if digest_id and not digest_result.get("deduplicated"): enqueue_digest(db, digest_id)
        _stage(db, validation.id, "DIGEST", 1, 1 if digest_id else 0)
        evidence = evidence_audit(db, all_source_ids); integrity = integrity_audit(db); duplicates = duplicate_audit(db, all_source_ids); taxonomy = taxonomy_audit(db, all_source_ids); overview = admin_overview(db, "24h")
        critical = []
        if evidence["critical"]: critical.append("FABRICATED_EVIDENCE")
        if integrity["orphan_count"]: critical.append("ORPHAN_RECORD")
        summary = {"source_document_ids": all_source_ids, "collection": collection_results, "stages": [{"stage": row.stage, "input_count": row.input_count, "success_count": row.success_count, "failure_count": row.failure_count, "duration_ms": row.duration_ms, "errors": row.errors_json} for row in db.scalars(select(ValidationStage).where(ValidationStage.validation_run_id == validation.id))], "evidence_audit": evidence, "integrity_audit": integrity, "duplicate_audit": duplicates, "taxonomy_audit": taxonomy, "product_brain": product_load_stats(), "critical_errors": critical, "operations_status": overview["system_status"], "operations_snapshot": overview, "delivery_dry_run": delivery_dry_run}
        summary["quality_gate"] = evaluate_quality_gate(summary)
        validation.source_document_count = len(all_source_ids); validation.event_count = len(event_ids); validation.cluster_count = len(set(cluster_ids)); validation.opportunity_count = len(opportunities); validation.alert_count = len(alert_ids); validation.delivery_count = len(delivery_ids); validation.digest_count = 1 if digest_id else 0; validation.summary_json = summary; validation.status = "PARTIAL" if errors else "COMPLETED"; validation.completed_at = datetime.now(timezone.utc); db.commit()
        return {"id": validation.id, "status": validation.status, "summary": summary}
    except Exception as exc:
        db.rollback(); validation = db.get(ValidationRun, validation.id); validation.status = "FAILED"; validation.completed_at = datetime.now(timezone.utc); validation.summary_json = {"error": str(exc)[:500], "source_document_ids": all_source_ids}; db.commit(); raise
