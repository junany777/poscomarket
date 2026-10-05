import os
import sys
from pathlib import Path
from sqlalchemy import select

sys.path.insert(0, str(Path(__file__).parents[1]))
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app.core.database import SessionLocal, init_db  # noqa: E402
from app.schemas import SourceCreate  # noqa: E402
from app.services.ingestion import create_source  # noqa: E402
from app.services.pipeline import run_intelligence_pipeline  # noqa: E402
from app.services.product_brain.router import route_product_knowledge  # noqa: E402
from app.services.evidence import validate_evidence_quote  # noqa: E402
from app.models.entities import AIRun, Opportunity  # noqa: E402


def test_ev_motor_routes_to_hyper_no():
    route = route_product_knowledge("AUTOMOTIVE", "EV_MOTOR", "MOTOR_CORE", ["LOW_CORE_LOSS"])
    assert route.product_family == "HYPER_NO"
    assert route.knowledge_files == ["knowledge/posco/automotive/hyper-no.md"]


def test_vertical_slice():
    init_db()
    db = SessionLocal()
    source, duplicate = create_source(db, SourceCreate(source_name="TEST", title="EV capacity expansion", content="The automaker announced an expansion of EV traction motor production capacity in North America."))
    assert not duplicate
    result = run_intelligence_pipeline(db, source.id)
    assert result["event"]["type"] == "CAPACITY_EXPANSION"
    assert result["strategy"]["code"] == "ELECTRIFICATION"
    assert result["product_match"]["product_family"] == "HYPER_NO"
    assert result["opportunity"]["score"] == 88.5
    assert result["opportunity"]["score_breakdown"]["product_fit"] == 92


def test_evidence_must_be_exact_substring():
    assert validate_evidence_quote("EV production expands in North America.", "production expands")
    assert not validate_evidence_quote("EV production expands in North America.", "EV production is growing")


def test_negative_product_routes():
    assert route_product_knowledge("AUTOMOTIVE", "EV", "UNKNOWN", []).product_family != "HYPER_NO"
    assert route_product_knowledge("AUTOMOTIVE", "BATTERY_CELL", "BATTERY_CELL", []).product_family != "HYPER_NO"
    assert route_product_knowledge("AUTOMOTIVE", "COMMERCIAL_VEHICLE", "TRUCK_FRAME", []).product_family == "ATOS"
    assert route_product_knowledge("AUTOMOTIVE", "VEHICLE_BODY", "BODY_IN_WHITE", []).product_family == "AUTOMOTIVE_STEEL"
    assert route_product_knowledge("ENERGY", "SOLAR_STRUCTURE", "STRUCTURE", [], ["HIGH_SALINITY", "HIGH_HUMIDITY", "COASTAL"]).product_family == "POSMAC_SUPER"


def test_pipeline_is_idempotent():
    db = SessionLocal()
    before_opportunities = len(list(db.scalars(select(Opportunity))))
    before_runs = len(list(db.scalars(select(AIRun))))
    source, _ = create_source(db, SourceCreate(source_name="IDEMPOTENCY", title="EV expansion", content="The automaker announced an expansion of EV traction motor production capacity."))
    first = run_intelligence_pipeline(db, source.id)
    second = run_intelligence_pipeline(db, source.id)
    assert first["opportunity"]["id"] == second["opportunity"]["id"]
    assert len(list(db.scalars(select(Opportunity)))) == before_opportunities + 1
    assert len(list(db.scalars(select(AIRun)))) == before_runs + 1
