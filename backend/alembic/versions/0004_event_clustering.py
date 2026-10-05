"""add event clustering tables and event membership"""

from alembic import op
import sqlalchemy as sa

revision = "0004_event_clustering"
down_revision = "0003_collection_runs"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    tables = inspector.get_table_names()
    if "event_clusters" not in tables:
        op.create_table(
            "event_clusters",
            sa.Column("id", sa.String(36), primary_key=True),
            sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("cluster_key", sa.String(120), nullable=True),
            sa.Column("canonical_event_id", sa.String(36), sa.ForeignKey("events.id"), nullable=True),
            sa.Column("primary_company_id", sa.String(36), sa.ForeignKey("companies.id"), nullable=True),
            sa.Column("primary_event_type", sa.String(80), nullable=False),
            sa.Column("title", sa.String(500), nullable=False),
            sa.Column("summary", sa.Text(), nullable=False),
            sa.Column("event_date", sa.String(40), nullable=True),
            sa.Column("location", sa.String(200), nullable=True),
            sa.Column("status", sa.String(30), nullable=False),
            sa.Column("confidence", sa.Float(), nullable=False),
            sa.Column("source_count", sa.Integer(), nullable=False),
            sa.Column("first_seen_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("last_seen_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("cluster_metadata_json", sa.JSON(), nullable=False),
        )
    event_columns = {column["name"] for column in inspector.get_columns("events")}
    if "event_cluster_id" not in event_columns:
        op.add_column("events", sa.Column("event_cluster_id", sa.String(36), sa.ForeignKey("event_clusters.id"), nullable=True))
    if "is_canonical" not in event_columns:
        op.add_column("events", sa.Column("is_canonical", sa.Boolean(), nullable=False, server_default=sa.false()))
    if "metadata_json" not in event_columns:
        op.add_column("events", sa.Column("metadata_json", sa.JSON(), nullable=False, server_default=sa.text("'{}'")))
    if "event_cluster_decision_logs" not in tables:
        op.create_table(
            "event_cluster_decision_logs",
            sa.Column("id", sa.String(36), primary_key=True),
            sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("event_id", sa.String(36), sa.ForeignKey("events.id"), nullable=False),
            sa.Column("candidate_cluster_id", sa.String(36), sa.ForeignKey("event_clusters.id"), nullable=True),
            sa.Column("score", sa.Float(), nullable=False),
            sa.Column("decision", sa.String(40), nullable=False),
            sa.Column("reasons_json", sa.JSON(), nullable=False),
            sa.Column("ai_run_id", sa.String(36), sa.ForeignKey("ai_runs.id"), nullable=True),
        )
    index_specs = [
        ("event_clusters", "ix_event_clusters_primary_company_id", ["primary_company_id"]),
        ("event_clusters", "ix_event_clusters_primary_event_type", ["primary_event_type"]),
        ("event_clusters", "ix_event_clusters_event_date", ["event_date"]),
        ("event_clusters", "ix_event_clusters_last_seen_at", ["last_seen_at"]),
        ("events", "ix_events_event_cluster_id", ["event_cluster_id"]),
        ("event_cluster_decision_logs", "ix_event_cluster_decision_logs_event_id", ["event_id"]),
    ]
    for table, name, columns in index_specs:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}:
            op.create_index(name, table, columns, unique=False)


def downgrade() -> None:
    op.drop_index("ix_event_cluster_decision_logs_event_id", table_name="event_cluster_decision_logs")
    op.drop_table("event_cluster_decision_logs")
    op.drop_index("ix_events_event_cluster_id", table_name="events")
    op.drop_column("events", "metadata_json")
    op.drop_column("events", "is_canonical")
    op.drop_column("events", "event_cluster_id")
    op.drop_index("ix_event_clusters_last_seen_at", table_name="event_clusters")
    op.drop_index("ix_event_clusters_event_date", table_name="event_clusters")
    op.drop_index("ix_event_clusters_primary_event_type", table_name="event_clusters")
    op.drop_index("ix_event_clusters_primary_company_id", table_name="event_clusters")
    op.drop_table("event_clusters")
