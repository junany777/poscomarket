"""add intelligence evaluation framework"""

from alembic import op
import sqlalchemy as sa

revision = "0005_evaluation_framework"
down_revision = "0004_event_clustering"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    tables = set(sa.inspect(bind).get_table_names())
    if "evaluation_runs" not in tables:
        op.create_table("evaluation_runs", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("name", sa.String(160), nullable=False), sa.Column("dataset_version", sa.String(80), nullable=False), sa.Column("pipeline_version", sa.String(80), nullable=False), sa.Column("prompt_version", sa.String(80), nullable=False), sa.Column("model", sa.String(100), nullable=False), sa.Column("started_at", sa.DateTime(timezone=True), nullable=False), sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True), sa.Column("status", sa.String(30), nullable=False), sa.Column("summary_json", sa.JSON(), nullable=False))
    if "evaluation_case_results" not in tables:
        op.create_table("evaluation_case_results", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("evaluation_run_id", sa.String(36), sa.ForeignKey("evaluation_runs.id"), nullable=False), sa.Column("case_id", sa.String(120), nullable=False), sa.Column("source_document_id", sa.String(36), sa.ForeignKey("source_documents.id"), nullable=True), sa.Column("event_correct", sa.Boolean(), nullable=True), sa.Column("cluster_correct", sa.Boolean(), nullable=True), sa.Column("strategy_score", sa.Float(), nullable=True), sa.Column("application_correct", sa.Boolean(), nullable=True), sa.Column("component_correct", sa.Boolean(), nullable=True), sa.Column("material_category_correct", sa.Boolean(), nullable=True), sa.Column("product_correct", sa.Boolean(), nullable=True), sa.Column("grade_guardrail_pass", sa.Boolean(), nullable=True), sa.Column("opportunity_quality", sa.String(30), nullable=True), sa.Column("action_quality", sa.Float(), nullable=True), sa.Column("errors_json", sa.JSON(), nullable=False), sa.Column("review_notes", sa.Text(), nullable=True))
    if "human_evaluations" not in tables:
        op.create_table("human_evaluations", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("evaluation_case_result_id", sa.String(36), sa.ForeignKey("evaluation_case_results.id"), nullable=False), sa.Column("reviewer", sa.String(120), nullable=False), sa.Column("dimension", sa.String(60), nullable=False), sa.Column("score", sa.Float(), nullable=True), sa.Column("label", sa.String(60), nullable=True), sa.Column("comment", sa.Text(), nullable=True))
    for table, name, column in [("evaluation_runs", "ix_evaluation_runs_dataset_version", "dataset_version"), ("evaluation_runs", "ix_evaluation_runs_status", "status"), ("evaluation_case_results", "ix_evaluation_case_results_evaluation_run_id", "evaluation_run_id"), ("evaluation_case_results", "ix_evaluation_case_results_case_id", "case_id"), ("evaluation_case_results", "ix_evaluation_case_results_source_document_id", "source_document_id"), ("human_evaluations", "ix_human_evaluations_evaluation_case_result_id", "evaluation_case_result_id")]:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}:
            op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("human_evaluations")
    op.drop_table("evaluation_case_results")
    op.drop_table("evaluation_runs")
