from pathlib import Path
import yaml


def _root() -> Path:
    return Path(__file__).resolve().parents[1] / "prompts"


def load_registry() -> list[dict]:
    path = _root() / "registry.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")).get("prompts", [])


def get_active_prompt(prompt_name: str) -> dict:
    matches = [item for item in load_registry() if item.get("name") == prompt_name and item.get("status") == "ACTIVE"]
    if len(matches) != 1:
        raise RuntimeError(f"active prompt resolution failed: {prompt_name}")
    return matches[0]


def prompt_text(prompt_name: str, version: str | None = None) -> str:
    metadata = next((item for item in load_registry() if item.get("name") == prompt_name and (version is None or item.get("version") == version)), None)
    if not metadata:
        raise RuntimeError(f"prompt not found: {prompt_name}/{version or 'active'}")
    path = _root() / prompt_name / f"{metadata['version']}.md"
    if not path.exists():
        raise RuntimeError(f"prompt content not found: {path}")
    return path.read_text(encoding="utf-8")
