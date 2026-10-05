from dataclasses import dataclass


RULE_TYPES = {"COMPANY", "INDUSTRY", "EVENT_TYPE", "STRATEGY", "APPLICATION", "COMPONENT", "MATERIAL_CATEGORY", "PRODUCT_FAMILY", "OPPORTUNITY_SCORE", "OPPORTUNITY_STATUS", "OPPORTUNITY_CONFIDENCE", "PRODUCT_MATCH_CONFIDENCE", "EVENT_CONFIDENCE"}
OPERATORS = {"EQUALS", "IN", "NOT_IN", "GTE", "LTE"}


@dataclass(frozen=True)
class RuleMatch:
    dimension: str
    operator: str
    expected: object
    actual: object
    matched: bool


def _equals(actual, expected) -> bool:
    return str(actual).upper() == str(expected).upper()


def match_rule(rule, values: dict) -> RuleMatch:
    dimension, operator, expected = rule.rule_type, rule.operator, rule.value_json
    actual = values.get(dimension)
    if operator == "EQUALS": matched = _equals(actual, expected)
    elif operator == "IN": matched = any(_equals(actual, item) for item in (expected if isinstance(expected, list) else [expected]))
    elif operator == "NOT_IN": matched = not any(_equals(actual, item) for item in (expected if isinstance(expected, list) else [expected]))
    elif operator == "GTE": matched = actual is not None and float(actual) >= float(expected)
    elif operator == "LTE": matched = actual is not None and float(actual) <= float(expected)
    else: matched = False
    return RuleMatch(dimension, operator, expected, actual, matched)


def match_watchlist(watchlist, rules, values: dict) -> dict:
    checks = [match_rule(rule, values) for rule in rules if rule.enabled]
    return {"matched": bool(watchlist.enabled and checks and all(item.matched for item in checks)), "matched_rules": [item.__dict__ for item in checks if item.matched], "failed_rules": [item.__dict__ for item in checks if not item.matched]}
