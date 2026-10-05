"""validation run tracking"""
from alembic import op
import sqlalchemy as sa

revision = "0011_validation"
down_revision = "0010_digest"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind(); tables = set(sa.inspect(bind).get_table_names())
    if "validation_runs" not in tables:
        op.create_table("validation_runs", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("name", sa.String(160), nullable=False), sa.Column("started_at", sa.DateTime(timezone=True), nullable=False), sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True), sa.Column("status", sa.String(30), nullable=False), sa.Column("source_document_count", sa.Integer(), nullable=False), sa.Column("event_count", sa.Integer(), nullable=False), sa.Column("cluster_count", sa.Integer(), nullable=False), sa.Column("opportunity_count", sa.Integer(), nullable=False), sa.Column("alert_count", sa.Integer(), nullable=False), sa.Column("delivery_count", sa.Integer(), nullable=False), sa.Column("digest_count", sa.Integer(), nullable=False), sa.Column("summary_json", sa.JSON(), nullable=False))
    if "validation_run_sources" not in tables:
        op.create_table("validation_run_sources", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("validation_run_id", sa.String(36), sa.ForeignKey("validation_runs.id"), nullable=False), sa.Column("source_document_id", sa.String(36), sa.ForeignKey("source_documents.id"), nullable=False), sa.Column("review_status", sa.String(30), nullable=False), sa.Column("review_json", sa.JSON(), nullable=False), sa.UniqueConstraint("validation_run_id", "source_document_id", name="uq_validation_run_source"))
    if "validation_stages" not in tables:
        op.create_table("validation_stages", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("validation_run_id", sa.String(36), sa.ForeignKey("validation_runs.id"), nullable=False), sa.Column("stage", sa.String(60), nullable=False), sa.Column("input_count", sa.Integer(), nullable=False), sa.Column("success_count", sa.Integer(), nullable=False), sa.Column("failure_count", sa.Integer(), nullable=False), sa.Column("skipped_count", sa.Integer(), nullable=False), sa.Column("duration_ms", sa.Float(), nullable=True), sa.Column("errors_json", sa.JSON(), nullable=False))
    for table, name, column in [("validation_runs", "ix_validation_runs_status", "status"), ("validation_run_sources", "ix_validation_run_sources_validation_run_id", "validation_run_id"), ("validation_run_sources", "ix_validation_run_sources_source_document_id", "source_document_id"), ("validation_stages", "ix_validation_stages_validation_run_id", "validation_run_id"), ("validation_stages", "ix_validation_stages_stage", "stage")]:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}: op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("validation_stages"); op.drop_table("validation_run_sources"); op.drop_table("validation_runs")
