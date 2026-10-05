from datetime import datetime, timezone

from app.services.digest.service import period_for


def test_daily_period_is_one_day_and_utc_aware():
    start, end = period_for("DAILY", datetime(2026, 10, 5, 0, 0, tzinfo=timezone.utc))
    assert end - start == __import__("datetime").timedelta(days=1)
    assert start.tzinfo is not None and end.tzinfo is not None


def test_weekly_period_is_seven_days():
    start, end = period_for("WEEKLY", datetime(2026, 10, 5, 0, 0, tzinfo=timezone.utc))
    assert end - start == __import__("datetime").timedelta(days=7)
