from app.services.operations.health import overall_status


def test_overall_status_is_healthy_when_all_components_are_healthy():
    assert overall_status({"DATABASE": {"status": "HEALTHY"}, "DIGEST": {"status": "HEALTHY"}}) == "HEALTHY"


def test_overall_status_degrades_for_backlog_or_unknown_component():
    assert overall_status({"DATABASE": {"status": "HEALTHY"}, "PIPELINE": {"status": "DEGRADED"}}) == "DEGRADED"
    assert overall_status({"DATABASE": {"status": "HEALTHY"}, "AI": {"status": "UNKNOWN"}}) == "DEGRADED"


def test_overall_status_fails_when_database_fails():
    assert overall_status({"DATABASE": {"status": "FAILED"}, "AI": {"status": "HEALTHY"}}) == "FAILED"
