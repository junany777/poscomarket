from app.services.performance.service import _latency_ms


def test_latency_metric_is_measured_from_iso_timestamps():
    assert _latency_ms("2026-10-05T00:00:00+00:00", "2026-10-05T00:00:01.250000+00:00") == 1250.0


def test_latency_metric_is_unavailable_for_malformed_input():
    assert _latency_ms("not-a-date", "also-not-a-date") is None
