from app.core.config import settings

CRITICAL_METRICS = {"evidence_validity_rate": 100, "grade_hallucination_rate": 0, "forbidden_product_violation_rate": 0, "false_event_merge_rate": 5}


def compare_summaries(baseline: dict, candidate: dict, target_metric: str | None = None) -> dict:
    improvements, regressions, critical_failures = {}, {}, []
    for key in set(baseline) | set(candidate):
        before, after = baseline.get(key), candidate.get(key)
        if not isinstance(before, (int, float)) or not isinstance(after, (int, float)):
            continue
        delta = round(after - before, 2)
        if delta > 0: improvements[key] = delta
        if delta < -settings.evaluation_max_non_target_regression_pct: regressions[key] = delta
        if key in {"evidence_validity_rate", "material_category_accuracy", "product_family_accuracy", "explainability_completeness"} and after < 90:
            critical_failures.append({"metric": key, "value": after})
        if key in {"grade_hallucination_rate", "forbidden_product_violation_rate", "false_event_merge_rate"} and after > CRITICAL_METRICS[key]:
            critical_failures.append({"metric": key, "value": after})
    target_improved = not target_metric or (candidate.get(target_metric, 0) > baseline.get(target_metric, 0))
    if target_metric and "rate" in target_metric and any(word in target_metric for word in ("hallucination", "over_inference", "duplicate", "false_merge")):
        target_improved = candidate.get(target_metric, 0) < baseline.get(target_metric, 0)
    return {"decision": "ACCEPT" if target_improved and not critical_failures and not regressions else "REJECT", "target_improvements": improvements, "regressions": regressions, "critical_failures": critical_failures}
