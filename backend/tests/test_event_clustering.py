from datetime import datetime, timezone

from app.services.intelligence.event_clustering.service import EVENT_TYPE_COMPATIBILITY, _title_similarity, score_candidate


def test_event_type_compatibility_is_explicit():
    assert "CAPACITY_EXPANSION" in EVENT_TYPE_COMPATIBILITY["NEW_FACTORY"]
    assert "CAPEX" not in EVENT_TYPE_COMPATIBILITY["NEW_FACTORY"]


def test_title_similarity_is_explainable():
    assert _title_similarity("EV motor plant expansion", "EV motor plant capacity expansion") > 0.5
    assert _title_similarity("EV motor plant", "battery supply contract") < 0.5
