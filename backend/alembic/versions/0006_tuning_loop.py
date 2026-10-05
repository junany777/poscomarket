"""add prompt/rule tuning candidates"""
from alembic import op
import sqlalchemy as sa

revision = "0006_tuning_loop"
down_revision = "0005_evaluation_framework"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    tables = set(sa.inspect(bind).get_table_names())
    if "prompt_changes" not in tables:
        op.create_table("prompt_changes", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("prompt_name", sa.String(100), nullable=False), sa.Column("from_version", sa.String(40), nullable=True), sa.Column("to_version", sa.String(40), nullable=False), sa.Column("change_reason", sa.Text(), nullable=False), sa.Column("target_error_codes_json", sa.JSON(), nullable=False), sa.Column("evaluation_run_before", sa.String(36), nullable=True), sa.Column("evaluation_run_after", sa.String(36), nullable=True), sa.Column("status", sa.String(30), nullable=False))
    if "tuning_candidates" not in tables:
        op.create_table("tuning_candidates", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("source_evaluation_run_id", sa.String(36), sa.ForeignKey("evaluation_runs.id"), nullable=True), sa.Column("error_code", sa.String(80), nullable=False), sa.Column("root_cause", sa.String(80), nullable=False), sa.Column("affected_stage", sa.String(80), nullable=False), sa.Column("proposed_fix_type", sa.String(30), nullable=False), sa.Column("proposed_change", sa.Text(), nullable=False), sa.Column("expected_metric", sa.String(120), nullable=False), sa.Column("status", sa.String(30), nullable=False), sa.Column("baseline_run_id", sa.String(36), nullable=True), sa.Column("candidate_run_id", sa.String(36), nullable=True), sa.Column("decision_json", sa.JSON(), nullable=False))
    for table, name, column in [("prompt_changes", "ix_prompt_changes_prompt_name", "prompt_name"), ("prompt_changes", "ix_prompt_changes_status", "status"), ("tuning_candidates", "ix_tuning_candidates_source_evaluation_run_id", "source_evaluation_run_id"), ("tuning_candidates", "ix_tuning_candidates_error_code", "error_code"), ("tuning_candidates", "ix_tuning_candidates_status", "status")]:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}:
            op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("tuning_candidates")
    op.drop_table("prompt_changes")
