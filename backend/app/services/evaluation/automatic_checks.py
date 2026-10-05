from app.services.evaluation.error_classifier import error


def _expected_values(value):
    if isinstance(value, dict):
        return set(value.get("acceptable", [])) | set(value.get("required", []))
    if value is None:
        return set()
    return {value}


def evaluate_case(case: dict, actual: dict, source_content: str, evidence_rows: list) -> dict:
    errors = []
    event = actual.get("event") or {}
    demand = actual.get("steel_demand") or {}
    product = actual.get("product_match") or {}
    expected_event = case.get("expected_event") or {}
    expected_demand = case.get("expected_demand") or {}
    expected_product = case.get("expected_product") or {}
    expected_strategy = case.get("expected_strategies") or {}
    event_correct = True
    if expected_event.get("primary_event_type") and event.get("type") != expected_event["primary_event_type"]:
        event_correct = False; errors.append(error("WRONG_EVENT_TYPE", "primary event type differs from gold label", "EVENT"))
    if expected_product.get("forbidden_product_families") and product.get("product_family") in expected_product["forbidden_product_families"]:
        errors.append(error("FORBIDDEN_PRODUCT_ROUTE", "forbidden product family was returned", "PRODUCT"))
    product_correct = not expected_product.get("product_family") or product.get("product_family") == expected_product.get("product_family") or product.get("status") == "PRODUCT_KNOWLEDGE_PENDING"
    if not product_correct:
        errors.append(error("WRONG_PRODUCT_FAMILY", "product family differs from gold label", "PRODUCT"))
    application_correct = not expected_demand.get("application") or demand.get("application") == expected_demand.get("application")
    if not application_correct: errors.append(error("WRONG_APPLICATION", "application differs from gold label", "STEEL_DEMAND"))
    component_correct = not expected_demand.get("component") or demand.get("component") == expected_demand.get("component")
    if not component_correct: errors.append(error("WRONG_COMPONENT", "component differs from gold label", "STEEL_DEMAND"))
    category_correct = not expected_demand.get("material_category") or demand.get("material_category") == expected_demand.get("material_category")
    if not category_correct: errors.append(error("WRONG_MATERIAL_CATEGORY", "material category differs from gold label", "STEEL_DEMAND"))
    requirements_expected = set(expected_demand.get("material_requirements", []))
    requirements_actual = set(demand.get("material_requirements", []))
    if requirements_expected and not requirements_expected.issubset(requirements_actual): errors.append(error("WRONG_MATERIAL_REQUIREMENT", "required material requirements are missing", "STEEL_DEMAND"))
    grade_pass = True
    if expected_product.get("grade_behavior") == "UNKNOWN" and product.get("candidate_grades"):
        grade_pass = False; errors.append(error("GRADE_HALLUCINATION", "exact grade was returned without sufficient engineering detail", "PRODUCT"))
    for evidence in evidence_rows:
        if not evidence.quote_text or evidence.quote_text not in source_content:
            errors.append(error("EVIDENCE_NOT_IN_SOURCE", "evidence quote is not an exact source substring", "EVIDENCE"))
    required_links = ("event", "strategy", "steel_demand", "product_match", "opportunity")
    if any(key not in actual for key in required_links): errors.append(error("MISSING_EXPLAINABILITY_LINK", "one or more intelligence stages are missing", "EXPLAINABILITY"))
    strategy_actual = actual.get("strategy", {}).get("code")
    strategy_required = set(expected_strategy.get("required", [])) if isinstance(expected_strategy, dict) else _expected_values(expected_strategy)
    strategy_score = 1.0 if not strategy_required or strategy_actual in strategy_required else 0.0
    if strategy_required and strategy_score == 0: errors.append(error("STRATEGY_MISSED", "required strategy was not produced", "STRATEGY"))
    return {"event_correct": event_correct, "cluster_correct": True, "strategy_score": strategy_score, "application_correct": application_correct, "component_correct": component_correct, "material_category_correct": category_correct, "product_correct": product_correct, "grade_guardrail_pass": grade_pass, "opportunity_quality": "VALID" if actual.get("opportunity") else "UNSUPPORTED", "action_quality": 1.0 if actual.get("actions") else 0.0, "errors": errors}
