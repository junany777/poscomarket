from pathlib import Path

import yaml


def load_dataset(path: str) -> dict:
    file_path = Path(path)
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path
    if not file_path.exists():
        file_path = Path(__file__).resolve().parents[3] / "evaluation" / "datasets" / file_path.name
    return yaml.safe_load(file_path.read_text(encoding="utf-8"))
