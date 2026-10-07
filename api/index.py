"""Minimal Vercel function used by the static dashboard for OpenDART only."""

import sys
from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

BACKEND_DIR = Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.dart import DartClient  # noqa: E402
from app.core.config import settings  # noqa: E402

app = FastAPI(title="POSCO Market OpenDART Proxy")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[item.strip() for item in settings.cors_allowed_origins.split(",") if item.strip()],
    allow_credentials=False,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/v1/dart/health")
@app.get("/api/v1/dart/health")
async def dart_health() -> dict:
    return await DartClient().health()


@app.get("/v1/dart/disclosures")
@app.get("/api/v1/dart/disclosures")
async def dart_disclosures(
    bgn_de: str | None = None,
    end_de: str | None = None,
    corp_code: str | None = None,
    industry: str | None = None,
    page: int = Query(1, ge=1),
    page_count: int = Query(100, ge=1, le=100),
) -> dict:
    return await DartClient().disclosures(bgn_de, end_de, corp_code, industry, page, page_count)


@app.get("/v1/dart/analysis")
@app.get("/api/v1/dart/analysis")
async def dart_analysis(bgn_de: str | None = None, end_de: str | None = None) -> dict:
    return await DartClient().analysis(bgn_de, end_de)

