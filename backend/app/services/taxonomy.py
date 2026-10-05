from pathlib import Path
import re
import os


ROOT = Path(os.getenv("KNOWLEDGE_ROOT", str(Path(__file__).resolve().parents[3])))

FALLBACK = {
    "industry": {"AUTOMOTIVE", "SHIPBUILDING", "CONSTRUCTION", "ENERGY", "HOME_APPLIANCE", "MACHINERY", "SEMICONDUCTOR"},
    "event": {"CAPEX", "NEW_FACTORY", "CAPACITY_EXPANSION", "NEW_BUSINESS", "R_AND_D", "CONTRACT", "ESG", "SUPPLY_CHAIN", "PROCUREMENT", "OTHER"},
    "strategy": {"GROWTH", "LOCALIZATION", "ELECTRIFICATION", "DECARBONIZATION", "AUTOMATION", "NEW_MARKET_ENTRY", "OTHER"},
    "application": {"EV_MOTOR", "MOTOR_CORE", "COMMERCIAL_VEHICLE", "TRUCK_FRAME", "VEHICLE_BODY", "BODY_IN_WHITE", "CHASSIS"},
    "material": {"NON_ORIENTED_ELECTRICAL_STEEL", "AUTOMOTIVE_STEEL", "COATED_STEEL", "ZINC_COATED_STEEL"},
}


def _codes(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"\b[A-Z][A-Z0-9_]{2,}\b", text))


def taxonomy_codes(kind: str) -> set[str]:
    files = {
        "industry": ROOT / "knowledge/taxonomy/industries.md",
        "event": ROOT / "knowledge/taxonomy/events.md",
        "strategy": ROOT / "knowledge/taxonomy/strategies.md",
        "application": ROOT / "knowledge/taxonomy/applications.md",
        "material": ROOT / "knowledge/taxonomy/materials.md",
    }
    values = _codes(files.get(kind, Path("")))
    # Keep the documented MVP fallback vocabulary available when a taxonomy
    # document does not yet enumerate a required cross-domain code.
    return values | FALLBACK[kind]


def validate_code(kind: str, value: str) -> str:
    normalized = value.strip().upper()
    return normalized if normalized in taxonomy_codes(kind) else "UNKNOWN"
