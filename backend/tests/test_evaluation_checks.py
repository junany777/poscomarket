from app.services.evaluation.automatic_checks import evaluate_case


def test_evaluation_rejects_forbidden_product_and_invalid_evidence():
    case = {"expected_product": {"forbidden_product_families": ["HYPER_NO"]}}
    actual = {"event": {}, "steel_demand": {}, "product_match": {"product_family": "HYPER_NO"}, "opportunity": {}}
    evidence = [type("Evidence", (), {"quote_text": "not in source"})()]
    result = evaluate_case(case, actual, "source text", evidence)
    codes = {item["code"] for item in result["errors"]}
    assert "FORBIDDEN_PRODUCT_ROUTE" in codes
    assert "EVIDENCE_NOT_IN_SOURCE" in codes


def test_grade_unknown_is_a_guardrail():
    case = {"expected_product": {"grade_behavior": "UNKNOWN"}}
    result = evaluate_case(case, {"event": {}, "steel_demand": {}, "product_match": {"candidate_grades": []}, "opportunity": {}}, "source", [])
    assert result["grade_guardrail_pass"] is True
