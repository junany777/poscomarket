"""performance benchmark and AI cache provenance"""
from alembic import op
import sqlalchemy as sa

revision = "0012_performance"
down_revision = "0011_validation"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind(); inspector = sa.inspect(bind); tables = set(inspector.get_table_names())
    if "ai_runs" in tables:
        columns = {item["name"] for item in inspector.get_columns("ai_runs")}
        if "cache_key" not in columns: op.add_column("ai_runs", sa.Column("cache_key", sa.String(128), nullable=True))
        if "cache_hit" not in columns: op.add_column("ai_runs", sa.Column("cache_hit", sa.Boolean(), nullable=False, server_default=sa.false()))
        if "reused_from_id" not in columns: op.add_column("ai_runs", sa.Column("reused_from_id", sa.String(36), nullable=True))
        indexes = {item["name"] for item in inspector.get_indexes("ai_runs")}
        if "ix_ai_runs_cache_key" not in indexes: op.create_index("ix_ai_runs_cache_key", "ai_runs", ["cache_key"], unique=False)
        if "ix_ai_runs_cache_hit" not in indexes: op.create_index("ix_ai_runs_cache_hit", "ai_runs", ["cache_hit"], unique=False)
    if "performance_benchmarks" not in tables:
        op.create_table("performance_benchmarks", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("name", sa.String(160), nullable=False), sa.Column("validation_run_id", sa.String(36), sa.ForeignKey("validation_runs.id"), nullable=True), sa.Column("pipeline_version", sa.String(80), nullable=False), sa.Column("model", sa.String(100), nullable=False), sa.Column("prompt_versions_json", sa.JSON(), nullable=False), sa.Column("rule_version", sa.String(80), nullable=False), sa.Column("started_at", sa.DateTime(timezone=True), nullable=False), sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True), sa.Column("metrics_json", sa.JSON(), nullable=False))
    if "ix_performance_benchmarks_validation_run_id" not in {item["name"] for item in sa.inspect(bind).get_indexes("performance_benchmarks")}: op.create_index("ix_performance_benchmarks_validation_run_id", "performance_benchmarks", ["validation_run_id"], unique=False)
    for table, name, column in [("source_documents", "ix_source_documents_published_at", "published_at"), ("event_clusters", "ix_event_clusters_last_seen_at", "last_seen_at"), ("ai_runs", "ix_ai_runs_run_type", "run_type"), ("ai_runs", "ix_ai_runs_status", "status"), ("ai_runs", "ix_ai_runs_started_at", "started_at"), ("opportunities", "ix_opportunities_created_at", "created_at"), ("alerts", "ix_alerts_created_at", "created_at")]:
        if table in tables and name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}: op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("performance_benchmarks")
    op.drop_index("ix_ai_runs_cache_hit", table_name="ai_runs"); op.drop_index("ix_ai_runs_cache_key", table_name="ai_runs")
    op.drop_column("ai_runs", "reused_from_id"); op.drop_column("ai_runs", "cache_hit"); op.drop_column("ai_runs", "cache_key")
