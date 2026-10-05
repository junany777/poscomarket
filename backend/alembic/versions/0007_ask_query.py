"""add Ask Steel query audit"""
from alembic import op
import sqlalchemy as sa

revision = "0007_ask_query"
down_revision = "0006_tuning_loop"
branch_labels = None
depends_on = None


def upgrade() -> None:
    if "ask_queries" not in sa.inspect(op.get_bind()).get_table_names():
        op.create_table("ask_queries", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("question", sa.Text(), nullable=False), sa.Column("resolved_question", sa.Text(), nullable=False), sa.Column("intent", sa.String(50), nullable=False), sa.Column("answer_text", sa.Text(), nullable=False), sa.Column("airun_id", sa.String(36), sa.ForeignKey("ai_runs.id"), nullable=True))
        op.create_index("ix_ask_queries_intent", "ask_queries", ["intent"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_ask_queries_intent", table_name="ask_queries")
    op.drop_table("ask_queries")
