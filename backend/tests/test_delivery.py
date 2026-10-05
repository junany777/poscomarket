from types import SimpleNamespace

from app.services.delivery.formatter import format_alert_message
from app.services.delivery.service import priority_for_score


def test_priority_mapping_is_deterministic():
    assert priority_for_score(87) == "HIGH"
    assert priority_for_score(72) == "MEDIUM"
    assert priority_for_score(40) == "LOW"


def test_formatter_does_not_require_product_for_event_alert():
    alert = SimpleNamespace(priority="HIGH", title="New factory", match_reason_json={})
    message = format_alert_message(alert, SimpleNamespace(name="Energy watchlist"), None, SimpleNamespace(name="Example Energy"), SimpleNamespace(primary_event_type="NEW_FACTORY"), None)
    assert "Example Energy" in message.body
    assert "Product:" not in message.body
    assert len(message.body) <= 3900
