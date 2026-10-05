def evaluate_quality_gate(summary: dict) -> dict:
    evidence = summary.get("evidence_audit", {})
    integrity = summary.get("integrity_audit", {})
    taxonomy = summary.get("taxonomy_audit", {})
    overview = summary.get("operations_snapshot", {})
    delivery_rate = ((overview.get("delivery") or {}).get("success_rate")) if isinstance(overview, dict) else None
    failures = list(summary.get("critical_errors", []))
    for error_code in (overview.get("quality") or {}).get("critical_errors", []) if isinstance(overview, dict) else []:
        failures.append(error_code)
    if evidence.get("validity_rate", 100) < 100: failures.append("FABRICATED_EVIDENCE")
    if integrity.get("orphan_count", 0): failures.append("ORPHAN_RECORD")
    if not taxonomy.get("passed", True): failures.append("INVALID_TAXONOMY")
    if delivery_rate is not None and delivery_rate < 95: failures.append("DELIVERY_SUCCESS_BELOW_95")
    failures = sorted(set(failures))
    return {"passed": not failures, "critical_errors": failures, "thresholds": {"evidence_validity": "100%", "grade_hallucination": "0%", "forbidden_product_violation": "0", "delivery_success": ">=95%"}, "observed": {"evidence_validity": evidence.get("validity_rate"), "delivery_success": delivery_rate}}
