from dataclasses import dataclass
from pathlib import Path
import os


ROOT = Path(os.getenv("KNOWLEDGE_ROOT", str(Path(__file__).resolve().parents[4])))


@dataclass
class ProductRouteResult:
    product_family: str | None
    knowledge_files: list[str]
    confidence: float
    reason: str


def route_product_knowledge(industry_code: str, application_code: str | None, component_code: str | None, material_requirements: list[str], environment: list[str] | None = None) -> ProductRouteResult:
    app = (application_code or "").upper()
    component = (component_code or "").upper()
    requirements = {x.upper() for x in material_requirements}
    if app == "EV_MOTOR" or component == "MOTOR_CORE" or "LOW_CORE_LOSS" in requirements:
        path = "knowledge/posco/automotive/hyper-no.md"
        return ProductRouteResult("HYPER_NO", [path], 0.91, "EV traction motor core requiring electrical steel performance")
    if app in {"COMMERCIAL_VEHICLE", "CHASSIS"} or component == "TRUCK_FRAME":
        return ProductRouteResult("ATOS", ["knowledge/posco/automotive/atos.md"], 0.86, "Structural automotive application requiring high strength")
    env = {x.upper() for x in (environment or [])}
    if {"HIGH_SALINITY", "COASTAL", "HIGH_HUMIDITY"} & env:
        return ProductRouteResult("POSMAC_SUPER", ["knowledge/posco/coated/posmac-super.md"], 0.82, "Corrosion-resistant coated steel environment")
    return ProductRouteResult("AUTOMOTIVE_STEEL", ["knowledge/posco/automotive/automotive-steel.md"], 0.55, "Base automotive steel route; detailed product review required")
