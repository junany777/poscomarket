from pathlib import Path

import yaml


def load_sources(path: str) -> list[dict]:
    registry_path = Path(path)
    if not registry_path.is_absolute():
        registry_path = Path.cwd() / registry_path
    if not registry_path.exists():
        candidate = Path(__file__).resolve().parents[3] / "config" / registry_path.name
        registry_path = candidate if candidate.exists() else registry_path
    if not registry_path.exists():
        return []
    payload = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    return payload.get("sources", [])


def enabled_sources(path: str, source_codes: list[str] | None = None) -> list[dict]:
    selected = {code.upper() for code in source_codes or []}
    return [source for source in load_sources(path) if source.get("enabled") and (not selected or source.get("source_code", "").upper() in selected)]
