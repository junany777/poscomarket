from app.services.validation.gate import evaluate_quality_gate


def test_quality_gate_passes_clean_validation():
    result = evaluate_quality_gate({"evidence_audit": {"validity_rate": 100}, "integrity_audit": {"orphan_count": 0}, "taxonomy_audit": {"passed": True}, "operations_snapshot": {"delivery": {"success_rate": 100}}})
    assert result["passed"] is True


def test_quality_gate_fails_fabricated_evidence_and_orphans():
    result = evaluate_quality_gate({"evidence_audit": {"validity_rate": 95}, "integrity_audit": {"orphan_count": 1}, "taxonomy_audit": {"passed": True}})
    assert result["passed"] is False
    assert "FABRICATED_EVIDENCE" in result["critical_errors"]
    assert "ORPHAN_RECORD" in result["critical_errors"]


def test_quality_gate_fails_low_delivery_success():
    result = evaluate_quality_gate({"evidence_audit": {"validity_rate": 100}, "integrity_audit": {"orphan_count": 0}, "taxonomy_audit": {"passed": True}, "operations_snapshot": {"delivery": {"success_rate": 90}}})
    assert result["passed"] is False
    assert "DELIVERY_SUCCESS_BELOW_95" in result["critical_errors"]
