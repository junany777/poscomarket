"""store deterministic opportunity score components"""
from alembic import op
import sqlalchemy as sa

revision = "0002_score_breakdown"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade():
    inspector = sa.inspect(op.get_bind())
    columns = {column["name"] for column in inspector.get_columns("opportunities")}
    if "score_breakdown_json" not in columns:
        op.add_column("opportunities", sa.Column("score_breakdown_json", sa.JSON(), nullable=True))


def downgrade():
    inspector = sa.inspect(op.get_bind())
    columns = {column["name"] for column in inspector.get_columns("opportunities")}
    if "score_breakdown_json" in columns:
        op.drop_column("opportunities", "score_breakdown_json")
