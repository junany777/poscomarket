import os
import sys
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
sys.path.insert(0, str(Path(__file__).parents[1]))

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


def test_api_vertical_slice():
    with TestClient(app) as client:
        response = client.post("/api/v1/sources", json={
            "source_type": "NEWS",
            "source_name": "TEST_SOURCE",
            "title": "Automaker expands EV traction motor production capacity",
            "content": "Example Motors announced that it will expand production capacity for electric-vehicle traction motors at its local plant.",
        })
        assert response.status_code == 200
        source_id = response.json()["data"]["id"]
        duplicate = client.post("/api/v1/sources", json={
            "source_type": "NEWS", "source_name": "TEST_SOURCE",
            "title": "duplicate", "content": "Example Motors announced that it will expand production capacity for electric-vehicle traction motors at its local plant.",
        })
        assert duplicate.json()["meta"]["duplicate"] is True
        result = client.post(f"/api/v1/intelligence/run/{source_id}")
        assert result.status_code == 200
        assert result.json()["data"]["product_match"]["product_family"] == "HYPER_NO"
        opportunity_id = result.json()["data"]["opportunity"]["id"]
        detail = client.get(f"/api/v1/opportunities/{opportunity_id}")
        assert detail.status_code == 200
        payload = detail.json()["data"]
        assert payload["evidence"]
        assert payload["event"]["type"] == "CAPACITY_EXPANSION"
        assert payload["product_match"]["product_family"] == "HYPER_NO"
        assert payload["recommended_actions"]

