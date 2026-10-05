from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import AIRun, EvaluationCaseResult, EvaluationRun, Evidence, SourceDocument
from app.schemas import SourceCreate
from app.services.evaluation.automatic_checks import evaluate_case
from app.services.evaluation.dataset_loader import load_dataset
from app.services.evaluation.metrics import aggregate
from app.services.ingestion_service import create_source
from app.services.pipeline import run_intelligence_pipeline


def run_evaluation(db: Session, dataset_path: str | None = None, mode: str = "live", limit: int | None = None, subset: str | None = None) -> dict:
    dataset = load_dataset(dataset_path or settings.evaluation_dataset_path)
    cases = dataset.get("cases", [])
    if subset:
        cases = [case for case in cases if subset.upper() in {str(case.get("category", "")).upper(), str(case.get("subset", "")).upper()}]
    cases = cases[:limit] if limit else cases
    started = datetime.now(timezone.utc)
    evaluation = EvaluationRun(name=dataset.get("name", "MVP Evaluation"), dataset_version=dataset.get("version", "unknown"), pipeline_version=settings.evaluation_pipeline_version, prompt_version=settings.evaluation_prompt_version, model="deterministic", rule_version=settings.evaluation_rule_version, product_knowledge_revision="workspace", started_at=started, status="RUNNING", summary_json={})
    db.add(evaluation); db.commit()
    results = []
    for case in cases:
        source = None; actual = case.get("actual", {})
        if mode == "live":
            source_payload = SourceCreate.model_validate(case["source"])
            source, _ = create_source(db, source_payload)
            actual = run_intelligence_pipeline(db, source.id)
        elif case.get("source_document_id"):
            source = db.get(SourceDocument, case["source_document_id"])
            run = db.scalar(select(AIRun).where(AIRun.input_reference == source.id, AIRun.status == "SUCCESS").order_by(AIRun.created_at.desc())) if source else None
            actual = (run.output_json or {}).get("result", {}) if run else actual
        evidence_rows = list(db.scalars(select(Evidence).where(Evidence.source_document_id == source.id))) if source else []
        checked = evaluate_case(case, actual, source.content if source else case.get("source", {}).get("content", ""), evidence_rows)
        results.append(checked)
        db.add(EvaluationCaseResult(evaluation_run_id=evaluation.id, case_id=case["id"], source_document_id=source.id if source else None, event_correct=checked["event_correct"], cluster_correct=checked["cluster_correct"], strategy_score=checked["strategy_score"], application_correct=checked["application_correct"], component_correct=checked["component_correct"], material_category_correct=checked["material_category_correct"], product_correct=checked["product_correct"], grade_guardrail_pass=checked["grade_guardrail_pass"], opportunity_quality=checked["opportunity_quality"], action_quality=checked["action_quality"], errors_json=checked["errors"]))
        db.commit()
    summary = aggregate(results)
    evaluation.status = "COMPLETED"
    evaluation.completed_at = datetime.now(timezone.utc)
    evaluation.summary_json = summary
    db.commit()
    return {"id": evaluation.id, "name": evaluation.name, "dataset_version": evaluation.dataset_version, "status": evaluation.status, "summary": summary}
