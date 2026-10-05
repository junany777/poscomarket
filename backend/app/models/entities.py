from sqlalchemy import Boolean, ForeignKey, Index, Integer, JSON, Float, Text, UniqueConstraint, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, uuid_column


class Company(TimestampMixin, Base):
    __tablename__ = "companies"
    id = uuid_column()
    name: Mapped[str] = mapped_column(index=True)
    normalized_name: Mapped[str] = mapped_column(index=True)
    industry_code: Mapped[str | None] = mapped_column(String(80), nullable=True, index=True)
    country: Mapped[str | None] = mapped_column(String(10), nullable=True)
    website: Mapped[str | None] = mapped_column(nullable=True)


class SourceDocument(TimestampMixin, Base):
    __tablename__ = "source_documents"
    id = uuid_column()
    source_type: Mapped[str] = mapped_column(String(40), default="NEWS")
    source_name: Mapped[str] = mapped_column(String(200))
    source_url: Mapped[str | None] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(String(500))
    published_at: Mapped[str | None] = mapped_column(nullable=True)
    collected_at: Mapped[str] = mapped_column(String(40))
    content: Mapped[str] = mapped_column(Text)
    content_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    language: Mapped[str] = mapped_column(String(10), default="en")
    status: Mapped[str] = mapped_column(String(40), default="READY_FOR_ANALYSIS", index=True)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)


class CollectionRun(TimestampMixin, Base):
    __tablename__ = "collection_runs"
    id = uuid_column()
    source_code: Mapped[str] = mapped_column(String(100), index=True)
    started_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="RUNNING", index=True)
    items_seen: Mapped[int] = mapped_column(Integer, default=0)
    items_new: Mapped[int] = mapped_column(Integer, default=0)
    items_duplicate: Mapped[int] = mapped_column(Integer, default=0)
    items_failed: Mapped[int] = mapped_column(Integer, default=0)
    error_summary: Mapped[str | None] = mapped_column(Text, nullable=True)


class Evidence(TimestampMixin, Base):
    __tablename__ = "evidence"
    id = uuid_column()
    source_document_id: Mapped[str] = mapped_column(ForeignKey("source_documents.id"), index=True)
    evidence_type: Mapped[str] = mapped_column(String(40), default="DIRECT_QUOTE")
    quote_text: Mapped[str] = mapped_column(Text)
    start_offset: Mapped[int | None] = mapped_column(Integer, nullable=True)
    end_offset: Mapped[int | None] = mapped_column(Integer, nullable=True)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)


class Event(TimestampMixin, Base):
    __tablename__ = "events"
    id = uuid_column()
    company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"), nullable=True, index=True)
    source_document_id: Mapped[str] = mapped_column(ForeignKey("source_documents.id"), index=True)
    primary_event_type: Mapped[str] = mapped_column(String(80), index=True)
    secondary_event_types_json: Mapped[list] = mapped_column(JSON, default=list)
    status: Mapped[str] = mapped_column(String(40), default="EXTRACTED")
    title: Mapped[str] = mapped_column(String(500))
    summary: Mapped[str] = mapped_column(Text)
    event_date: Mapped[str | None] = mapped_column(nullable=True)
    location: Mapped[str | None] = mapped_column(nullable=True)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    event_cluster_id: Mapped[str | None] = mapped_column(ForeignKey("event_clusters.id"), nullable=True, index=True)
    is_canonical: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)


class EventCluster(TimestampMixin, Base):
    __tablename__ = "event_clusters"
    id = uuid_column()
    cluster_key: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    canonical_event_id: Mapped[str | None] = mapped_column(ForeignKey("events.id"), nullable=True, index=True)
    primary_company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"), nullable=True, index=True)
    primary_event_type: Mapped[str] = mapped_column(String(80), index=True)
    title: Mapped[str] = mapped_column(String(500))
    summary: Mapped[str] = mapped_column(Text)
    event_date: Mapped[str | None] = mapped_column(String(40), nullable=True, index=True)
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", index=True)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    source_count: Mapped[int] = mapped_column(Integer, default=0)
    first_seen_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    last_seen_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    cluster_metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)


class EventClusterDecisionLog(TimestampMixin, Base):
    __tablename__ = "event_cluster_decision_logs"
    id = uuid_column()
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id"), index=True)
    candidate_cluster_id: Mapped[str | None] = mapped_column(ForeignKey("event_clusters.id"), nullable=True, index=True)
    score: Mapped[float] = mapped_column(Float, default=0.0)
    decision: Mapped[str] = mapped_column(String(40))
    reasons_json: Mapped[list] = mapped_column(JSON, default=list)
    ai_run_id: Mapped[str | None] = mapped_column(ForeignKey("ai_runs.id"), nullable=True)


class StrategyInference(TimestampMixin, Base):
    __tablename__ = "strategy_inferences"
    id = uuid_column()
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id"), index=True)
    strategy_code: Mapped[str] = mapped_column(String(80), index=True)
    reasoning_summary: Mapped[str] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    evidence_ids_json: Mapped[list] = mapped_column(JSON, default=list)


class SteelDemandHypothesis(TimestampMixin, Base):
    __tablename__ = "steel_demand_hypotheses"
    id = uuid_column()
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id"), index=True)
    industry_code: Mapped[str] = mapped_column(String(80), index=True)
    application_code: Mapped[str | None] = mapped_column(nullable=True)
    component_code: Mapped[str | None] = mapped_column(nullable=True)
    material_requirements_json: Mapped[list] = mapped_column(JSON, default=list)
    material_category: Mapped[str | None] = mapped_column(nullable=True)
    demand_direction: Mapped[str] = mapped_column(String(30))
    reasoning_summary: Mapped[str] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)


class ProductMatch(TimestampMixin, Base):
    __tablename__ = "product_matches"
    id = uuid_column()
    steel_demand_hypothesis_id: Mapped[str] = mapped_column(ForeignKey("steel_demand_hypotheses.id"), index=True)
    product_family: Mapped[str | None] = mapped_column(nullable=True, index=True)
    product_file: Mapped[str | None] = mapped_column(nullable=True)
    candidate_series_json: Mapped[list] = mapped_column(JSON, default=list)
    candidate_grades_json: Mapped[list] = mapped_column(JSON, default=list)
    match_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    reasoning_summary: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30), default="UNKNOWN")


class Opportunity(TimestampMixin, Base):
    __tablename__ = "opportunities"
    id = uuid_column()
    company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"), nullable=True, index=True)
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id"), index=True)
    product_match_id: Mapped[str | None] = mapped_column(ForeignKey("product_matches.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(500))
    opportunity_type: Mapped[str] = mapped_column(String(60))
    summary: Mapped[str] = mapped_column(Text)
    score: Mapped[float] = mapped_column(Float, index=True)
    score_breakdown_json: Mapped[dict] = mapped_column(JSON, default=dict)
    confidence: Mapped[float] = mapped_column(Float, index=True)
    status: Mapped[str] = mapped_column(String(30), default="NEW", index=True)


class RecommendedAction(TimestampMixin, Base):
    __tablename__ = "recommended_actions"
    id = uuid_column()
    opportunity_id: Mapped[str] = mapped_column(ForeignKey("opportunities.id"), index=True)
    action_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    priority: Mapped[str] = mapped_column(String(20), default="MEDIUM")


class AIRun(TimestampMixin, Base):
    __tablename__ = "ai_runs"
    id = uuid_column()
    run_type: Mapped[str] = mapped_column(String(80))
    model: Mapped[str] = mapped_column(String(100))
    prompt_version: Mapped[str] = mapped_column(String(50), default="deterministic-mvp")
    input_reference: Mapped[str] = mapped_column(String(200))
    output_json: Mapped[dict] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(String(30))
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[str] = mapped_column(String(40))
    completed_at: Mapped[str | None] = mapped_column(String(40), nullable=True)
    cache_key: Mapped[str | None] = mapped_column(String(128), nullable=True, index=True)
    cache_hit: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    reused_from_id: Mapped[str | None] = mapped_column(String(36), nullable=True)


class PerformanceBenchmark(TimestampMixin, Base):
    __tablename__ = "performance_benchmarks"
    id = uuid_column()
    name: Mapped[str] = mapped_column(String(160))
    validation_run_id: Mapped[str | None] = mapped_column(ForeignKey("validation_runs.id"), nullable=True, index=True)
    pipeline_version: Mapped[str] = mapped_column(String(80), default="mvp-1")
    model: Mapped[str] = mapped_column(String(100), default="deterministic")
    prompt_versions_json: Mapped[dict] = mapped_column(JSON, default=dict)
    rule_version: Mapped[str] = mapped_column(String(80), default="rules-v1")
    started_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    metrics_json: Mapped[dict] = mapped_column(JSON, default=dict)


class EvaluationRun(TimestampMixin, Base):
    __tablename__ = "evaluation_runs"
    id = uuid_column()
    name: Mapped[str] = mapped_column(String(160))
    dataset_version: Mapped[str] = mapped_column(String(80), index=True)
    pipeline_version: Mapped[str] = mapped_column(String(80))
    prompt_version: Mapped[str] = mapped_column(String(80))
    model: Mapped[str] = mapped_column(String(100))
    started_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(30), index=True)
    summary_json: Mapped[dict] = mapped_column(JSON, default=dict)
    rule_version: Mapped[str] = mapped_column(String(80), default="rules-v1")
    product_knowledge_revision: Mapped[str] = mapped_column(String(120), default="unknown")
    change_set_id: Mapped[str | None] = mapped_column(nullable=True, index=True)


class EvaluationCaseResult(TimestampMixin, Base):
    __tablename__ = "evaluation_case_results"
    id = uuid_column()
    evaluation_run_id: Mapped[str] = mapped_column(ForeignKey("evaluation_runs.id"), index=True)
    case_id: Mapped[str] = mapped_column(String(120), index=True)
    source_document_id: Mapped[str | None] = mapped_column(ForeignKey("source_documents.id"), nullable=True, index=True)
    event_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    cluster_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    strategy_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    application_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    component_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    material_category_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    product_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    grade_guardrail_pass: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    opportunity_quality: Mapped[str | None] = mapped_column(String(30), nullable=True)
    action_quality: Mapped[float | None] = mapped_column(Float, nullable=True)
    errors_json: Mapped[list] = mapped_column(JSON, default=list)
    review_notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class HumanEvaluation(TimestampMixin, Base):
    __tablename__ = "human_evaluations"
    id = uuid_column()
    evaluation_case_result_id: Mapped[str] = mapped_column(ForeignKey("evaluation_case_results.id"), index=True)
    reviewer: Mapped[str] = mapped_column(String(120))
    dimension: Mapped[str] = mapped_column(String(60))
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    label: Mapped[str | None] = mapped_column(String(60), nullable=True)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)


class PromptChange(TimestampMixin, Base):
    __tablename__ = "prompt_changes"
    id = uuid_column()
    prompt_name: Mapped[str] = mapped_column(String(100), index=True)
    from_version: Mapped[str | None] = mapped_column(String(40), nullable=True)
    to_version: Mapped[str] = mapped_column(String(40))
    change_reason: Mapped[str] = mapped_column(Text)
    target_error_codes_json: Mapped[list] = mapped_column(JSON, default=list)
    evaluation_run_before: Mapped[str | None] = mapped_column(String(36), nullable=True)
    evaluation_run_after: Mapped[str | None] = mapped_column(String(36), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="CANDIDATE", index=True)


class TuningCandidate(TimestampMixin, Base):
    __tablename__ = "tuning_candidates"
    id = uuid_column()
    source_evaluation_run_id: Mapped[str | None] = mapped_column(ForeignKey("evaluation_runs.id"), nullable=True, index=True)
    error_code: Mapped[str] = mapped_column(String(80), index=True)
    root_cause: Mapped[str] = mapped_column(String(80))
    affected_stage: Mapped[str] = mapped_column(String(80))
    proposed_fix_type: Mapped[str] = mapped_column(String(30))
    proposed_change: Mapped[str] = mapped_column(Text)
    expected_metric: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(30), default="PROPOSED", index=True)
    baseline_run_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    candidate_run_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    decision_json: Mapped[dict] = mapped_column(JSON, default=dict)


class AskQuery(TimestampMixin, Base):
    __tablename__ = "ask_queries"
    id = uuid_column()
    question: Mapped[str] = mapped_column(Text)
    resolved_question: Mapped[str] = mapped_column(Text)
    intent: Mapped[str] = mapped_column(String(50), index=True)
    answer_text: Mapped[str] = mapped_column(Text)
    airun_id: Mapped[str | None] = mapped_column(ForeignKey("ai_runs.id"), nullable=True)


class Watchlist(TimestampMixin, Base):
    __tablename__ = "watchlists"
    id = uuid_column()
    user_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String(160))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, index=True)


class WatchRule(TimestampMixin, Base):
    __tablename__ = "watch_rules"
    id = uuid_column()
    watchlist_id: Mapped[str] = mapped_column(ForeignKey("watchlists.id"), index=True)
    rule_type: Mapped[str] = mapped_column(String(50), index=True)
    operator: Mapped[str] = mapped_column(String(20))
    value_json: Mapped[object] = mapped_column(JSON)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)


class Alert(TimestampMixin, Base):
    __tablename__ = "alerts"
    id = uuid_column()
    watchlist_id: Mapped[str] = mapped_column(ForeignKey("watchlists.id"), index=True)
    watch_rule_snapshot_json: Mapped[list] = mapped_column(JSON, default=list)
    event_cluster_id: Mapped[str | None] = mapped_column(ForeignKey("event_clusters.id"), nullable=True, index=True)
    opportunity_id: Mapped[str | None] = mapped_column(ForeignKey("opportunities.id"), nullable=True, index=True)
    alert_type: Mapped[str] = mapped_column(String(40))
    title: Mapped[str] = mapped_column(String(500))
    summary: Mapped[str] = mapped_column(Text)
    priority: Mapped[str] = mapped_column(String(20), index=True)
    status: Mapped[str] = mapped_column(String(20), default="NEW", index=True)
    match_reason_json: Mapped[dict] = mapped_column(JSON, default=dict)
    read_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    dismissed_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)


class DeliveryChannel(TimestampMixin, Base):
    __tablename__ = "delivery_channels"
    id = uuid_column()
    user_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    channel_type: Mapped[str] = mapped_column(String(30), index=True)
    name: Mapped[str] = mapped_column(String(160))
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    config_json: Mapped[dict] = mapped_column(JSON, default=dict)


class AlertDeliverySubscription(TimestampMixin, Base):
    __tablename__ = "alert_delivery_subscriptions"
    id = uuid_column()
    watchlist_id: Mapped[str | None] = mapped_column(ForeignKey("watchlists.id"), nullable=True, index=True)
    user_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    delivery_channel_id: Mapped[str] = mapped_column(ForeignKey("delivery_channels.id"), index=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    minimum_priority: Mapped[str | None] = mapped_column(String(20), nullable=True)


class AlertDelivery(TimestampMixin, Base):
    __tablename__ = "alert_deliveries"
    __table_args__ = (UniqueConstraint("alert_id", "delivery_channel_id", name="uq_alert_delivery_alert_channel"),)
    id = uuid_column()
    alert_id: Mapped[str] = mapped_column(ForeignKey("alerts.id"), index=True)
    delivery_channel_id: Mapped[str] = mapped_column(ForeignKey("delivery_channels.id"), index=True)
    status: Mapped[str] = mapped_column(String(30), default="PENDING", index=True)
    attempt_count: Mapped[int] = mapped_column(Integer, default=0)
    last_attempt_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    delivered_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    external_message_id: Mapped[str | None] = mapped_column(String(160), nullable=True)
    error_code: Mapped[str | None] = mapped_column(String(60), nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    message_snapshot: Mapped[dict] = mapped_column(JSON, default=dict)


class IntelligenceDigest(TimestampMixin, Base):
    __tablename__ = "intelligence_digests"
    id = uuid_column()
    digest_type: Mapped[str] = mapped_column(String(20), index=True)
    period_start: Mapped[object] = mapped_column(DateTime(timezone=True), index=True)
    period_end: Mapped[object] = mapped_column(DateTime(timezone=True), index=True)
    title: Mapped[str] = mapped_column(String(200))
    executive_summary: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30), default="READY", index=True)
    event_count: Mapped[int] = mapped_column(Integer, default=0)
    opportunity_count: Mapped[int] = mapped_column(Integer, default=0)
    high_priority_count: Mapped[int] = mapped_column(Integer, default=0)
    content_json: Mapped[dict] = mapped_column(JSON, default=dict)
    generated_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    prompt_version: Mapped[str | None] = mapped_column(String(80), nullable=True)
    airun_id: Mapped[str | None] = mapped_column(ForeignKey("ai_runs.id"), nullable=True)


class DigestSubscription(TimestampMixin, Base):
    __tablename__ = "digest_subscriptions"
    id = uuid_column()
    delivery_channel_id: Mapped[str] = mapped_column(ForeignKey("delivery_channels.id"), index=True)
    digest_type: Mapped[str] = mapped_column(String(20), index=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    minimum_opportunity_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    industries_json: Mapped[list] = mapped_column(JSON, default=list)
    product_families_json: Mapped[list] = mapped_column(JSON, default=list)


class DigestDelivery(TimestampMixin, Base):
    __tablename__ = "digest_deliveries"
    __table_args__ = (UniqueConstraint("digest_id", "delivery_channel_id", name="uq_digest_delivery_digest_channel"),)
    id = uuid_column()
    digest_id: Mapped[str] = mapped_column(ForeignKey("intelligence_digests.id"), index=True)
    delivery_channel_id: Mapped[str] = mapped_column(ForeignKey("delivery_channels.id"), index=True)
    status: Mapped[str] = mapped_column(String(30), default="PENDING", index=True)
    attempt_count: Mapped[int] = mapped_column(Integer, default=0)
    delivered_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    external_message_id: Mapped[str | None] = mapped_column(String(160), nullable=True)
    error_code: Mapped[str | None] = mapped_column(String(60), nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    message_snapshot: Mapped[dict] = mapped_column(JSON, default=dict)


class ValidationRun(TimestampMixin, Base):
    __tablename__ = "validation_runs"
    id = uuid_column()
    name: Mapped[str] = mapped_column(String(160))
    started_at: Mapped[object] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[object | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="RUNNING", index=True)
    source_document_count: Mapped[int] = mapped_column(Integer, default=0)
    event_count: Mapped[int] = mapped_column(Integer, default=0)
    cluster_count: Mapped[int] = mapped_column(Integer, default=0)
    opportunity_count: Mapped[int] = mapped_column(Integer, default=0)
    alert_count: Mapped[int] = mapped_column(Integer, default=0)
    delivery_count: Mapped[int] = mapped_column(Integer, default=0)
    digest_count: Mapped[int] = mapped_column(Integer, default=0)
    summary_json: Mapped[dict] = mapped_column(JSON, default=dict)


class ValidationRunSource(TimestampMixin, Base):
    __tablename__ = "validation_run_sources"
    id = uuid_column()
    validation_run_id: Mapped[str] = mapped_column(ForeignKey("validation_runs.id"), index=True)
    source_document_id: Mapped[str] = mapped_column(ForeignKey("source_documents.id"), index=True)
    review_status: Mapped[str] = mapped_column(String(30), default="UNREVIEWED")
    review_json: Mapped[dict] = mapped_column(JSON, default=dict)
    __table_args__ = (UniqueConstraint("validation_run_id", "source_document_id", name="uq_validation_run_source"),)


class ValidationStage(TimestampMixin, Base):
    __tablename__ = "validation_stages"
    id = uuid_column()
    validation_run_id: Mapped[str] = mapped_column(ForeignKey("validation_runs.id"), index=True)
    stage: Mapped[str] = mapped_column(String(60), index=True)
    input_count: Mapped[int] = mapped_column(Integer, default=0)
    success_count: Mapped[int] = mapped_column(Integer, default=0)
    failure_count: Mapped[int] = mapped_column(Integer, default=0)
    skipped_count: Mapped[int] = mapped_column(Integer, default=0)
    duration_ms: Mapped[float | None] = mapped_column(Float, nullable=True)
    errors_json: Mapped[list] = mapped_column(JSON, default=list)
