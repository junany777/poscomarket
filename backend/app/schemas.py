from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class Envelope(BaseModel):
    data: object | None = None
    meta: dict = Field(default_factory=dict)
    error: dict | None = None


class SourceCreate(BaseModel):
    source_type: str = "NEWS"
    source_name: str
    source_url: str | None = None
    title: str
    published_at: datetime | None = None
    content: str = Field(min_length=1, max_length=500_000)
    language: str = "en"
    metadata_json: dict = Field(default_factory=dict)


class SourceRead(SourceCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str
    collected_at: str
    content_hash: str
    status: str


class OpportunityRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    company_id: str | None
    event_id: str
    product_match_id: str | None
    title: str
    opportunity_type: str
    summary: str
    score: float
    score_breakdown_json: dict
    confidence: float
    status: str


class PipelineResult(BaseModel):
    source_id: str
    event: dict
    strategy: dict
    steel_demand: dict
    product_match: dict
    opportunity: dict
    actions: list[dict]
