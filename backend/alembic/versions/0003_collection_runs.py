"""add collection run tracking"""

from alembic import op
import sqlalchemy as sa

revision = "0003_collection_runs"
down_revision = "0002_opportunity_score_breakdown"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "collection_runs" in inspector.get_table_names():
        return
    op.create_table(
        "collection_runs",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("source_code", sa.String(length=100), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("items_seen", sa.Integer(), nullable=False),
        sa.Column("items_new", sa.Integer(), nullable=False),
        sa.Column("items_duplicate", sa.Integer(), nullable=False),
        sa.Column("items_failed", sa.Integer(), nullable=False),
        sa.Column("error_summary", sa.Text(), nullable=True),
    )
    op.create_index("ix_collection_runs_source_code", "collection_runs", ["source_code"])
    op.create_index("ix_collection_runs_status", "collection_runs", ["status"])


def downgrade() -> None:
    op.drop_index("ix_collection_runs_status", table_name="collection_runs")
    op.drop_index("ix_collection_runs_source_code", table_name="collection_runs")
    op.drop_table("collection_runs")
