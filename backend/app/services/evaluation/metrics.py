def _rate(values: list[bool | None]) -> float | None:
    usable = [value for value in values if value is not None]
    return round(sum(1 for value in usable if value) / len(usable) * 100, 2) if usable else None


def aggregate(results: list[dict]) -> dict:
    errors = [item for result in results for item in result.get("errors", [])]
    count = len(results)
    return {
        "case_count": count,
        "evidence_validity_rate": round(100 - (sum(item["code"] == "EVIDENCE_NOT_IN_SOURCE" for item in errors) / max(1, count) * 100), 2),
        "event_type_accuracy": _rate([item.get("event_correct") for item in results]),
        "cluster_precision": _rate([item.get("cluster_correct") for item in results]),
        "cluster_recall": _rate([item.get("cluster_correct") for item in results]),
        "strategy_precision": round(sum(item.get("strategy_score", 0) for item in results) / max(1, count) * 100, 2),
        "application_accuracy": _rate([item.get("application_correct") for item in results]),
        "component_accuracy": _rate([item.get("component_correct") for item in results]),
        "material_category_accuracy": _rate([item.get("material_category_correct") for item in results]),
        "product_family_accuracy": _rate([item.get("product_correct") for item in results]),
        "correct_abstention_rate": _rate([item.get("grade_guardrail_pass") for item in results]),
        "grade_hallucination_rate": round(sum(item["code"] == "GRADE_HALLUCINATION" for item in errors) / max(1, count) * 100, 2),
        "duplicate_opportunity_rate": round(sum(item["code"] == "DUPLICATE_OPPORTUNITY" for item in errors) / max(1, count) * 100, 2),
        "explainability_completeness": _rate([not any(item["code"] == "MISSING_EXPLAINABILITY_LINK" for item in result.get("errors", [])) for result in results]),
        "error_counts": {code: sum(item["code"] == code for item in errors) for code in sorted({item["code"] for item in errors})},
    }
