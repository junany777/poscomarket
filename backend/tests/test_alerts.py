from types import SimpleNamespace

from app.services.alerts.matcher import match_rule, match_watchlist


def test_watch_rules_use_and_semantics():
    rules = [SimpleNamespace(rule_type="PRODUCT_FAMILY", operator="EQUALS", value_json="HYPER_NO", enabled=True), SimpleNamespace(rule_type="OPPORTUNITY_SCORE", operator="GTE", value_json=80, enabled=True)]
    watchlist = SimpleNamespace(enabled=True)
    assert match_watchlist(watchlist, rules, {"PRODUCT_FAMILY": "HYPER_NO", "OPPORTUNITY_SCORE": 87})["matched"]
    assert not match_watchlist(watchlist, rules, {"PRODUCT_FAMILY": "ATOS", "OPPORTUNITY_SCORE": 90})["matched"]


def test_rule_operator_gte():
    rule = SimpleNamespace(rule_type="OPPORTUNITY_SCORE", operator="GTE", value_json=80)
    assert match_rule(rule, {"OPPORTUNITY_SCORE": 80}).matched
