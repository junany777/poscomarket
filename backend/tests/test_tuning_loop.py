from app.services.evaluation.comparison import compare_summaries
from app.services.prompt_registry import get_active_prompt, prompt_text


def test_active_prompt_resolution_and_versioned_text():
    prompt = get_active_prompt("strategy_inference")
    assert prompt["version"] == "v1"
    assert "localization" in prompt_text("strategy_inference").lower()


def test_quality_gate_rejects_critical_regression():
    result = compare_summaries(
        {"strategy_precision": 78, "evidence_validity_rate": 100, "grade_hallucination_rate": 0},
        {"strategy_precision": 88, "evidence_validity_rate": 99, "grade_hallucination_rate": 0},
        "strategy_precision",
    )
    assert result["decision"] == "REJECT"
    assert result["critical_failures"]
