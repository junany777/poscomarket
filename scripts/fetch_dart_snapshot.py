"""Fetch public OpenDART snapshots for the static GitHub Pages frontend."""

import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))

from app.services.dart.client import DartClient  # noqa: E402
from knowledge_router import enrich_signals  # noqa: E402


async def main() -> None:
    if not os.getenv("DART_API_KEY"):
        raise RuntimeError("DART_API_KEY GitHub Actions secret is required")

    client = DartClient()
    health = await client.health()
    if not health.get("connected"):
        raise RuntimeError(f"OpenDART connection failed: {health.get('status')}")
    disclosures = await client.disclosures(page_count=100)
    analysis = await client.analysis()
    analysis = enrich_signals(analysis, ROOT)

    output_dir = ROOT / "data" / "dart"
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in {"health": health, "disclosures": disclosures, "analysis": analysis}.items():
        (output_dir / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(main())
