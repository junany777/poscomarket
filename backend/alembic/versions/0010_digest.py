"""daily and weekly intelligence digests"""
from alembic import op
import sqlalchemy as sa

revision = "0010_digest"
down_revision = "0009_alert_delivery"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    tables = set(sa.inspect(bind).get_table_names())
    if "intelligence_digests" not in tables:
        op.create_table("intelligence_digests",
            sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("digest_type", sa.String(20), nullable=False), sa.Column("period_start", sa.DateTime(timezone=True), nullable=False), sa.Column("period_end", sa.DateTime(timezone=True), nullable=False), sa.Column("title", sa.String(200), nullable=False), sa.Column("executive_summary", sa.Text(), nullable=False), sa.Column("status", sa.String(30), nullable=False), sa.Column("event_count", sa.Integer(), nullable=False), sa.Column("opportunity_count", sa.Integer(), nullable=False), sa.Column("high_priority_count", sa.Integer(), nullable=False), sa.Column("content_json", sa.JSON(), nullable=False), sa.Column("generated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("model", sa.String(100), nullable=True), sa.Column("prompt_version", sa.String(80), nullable=True), sa.Column("airun_id", sa.String(36), sa.ForeignKey("ai_runs.id"), nullable=True))
    if "digest_subscriptions" not in tables:
        op.create_table("digest_subscriptions",
            sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("delivery_channel_id", sa.String(36), sa.ForeignKey("delivery_channels.id"), nullable=False), sa.Column("digest_type", sa.String(20), nullable=False), sa.Column("enabled", sa.Boolean(), nullable=False), sa.Column("minimum_opportunity_score", sa.Float(), nullable=True), sa.Column("industries_json", sa.JSON(), nullable=False), sa.Column("product_families_json", sa.JSON(), nullable=False))
    if "digest_deliveries" not in tables:
        op.create_table("digest_deliveries",
            sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("digest_id", sa.String(36), sa.ForeignKey("intelligence_digests.id"), nullable=False), sa.Column("delivery_channel_id", sa.String(36), sa.ForeignKey("delivery_channels.id"), nullable=False), sa.Column("status", sa.String(30), nullable=False), sa.Column("attempt_count", sa.Integer(), nullable=False), sa.Column("delivered_at", sa.DateTime(timezone=True), nullable=True), sa.Column("external_message_id", sa.String(160), nullable=True), sa.Column("error_code", sa.String(60), nullable=True), sa.Column("error_message", sa.Text(), nullable=True), sa.Column("message_snapshot", sa.JSON(), nullable=False), sa.UniqueConstraint("digest_id", "delivery_channel_id", name="uq_digest_delivery_digest_channel"))
    for table, name, column in [("intelligence_digests", "ix_intelligence_digests_digest_type", "digest_type"), ("intelligence_digests", "ix_intelligence_digests_period_start", "period_start"), ("intelligence_digests", "ix_intelligence_digests_period_end", "period_end"), ("intelligence_digests", "ix_intelligence_digests_status", "status"), ("digest_subscriptions", "ix_digest_subscriptions_delivery_channel_id", "delivery_channel_id"), ("digest_subscriptions", "ix_digest_subscriptions_digest_type", "digest_type"), ("digest_subscriptions", "ix_digest_subscriptions_enabled", "enabled"), ("digest_deliveries", "ix_digest_deliveries_digest_id", "digest_id"), ("digest_deliveries", "ix_digest_deliveries_delivery_channel_id", "delivery_channel_id"), ("digest_deliveries", "ix_digest_deliveries_status", "status")]:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}: op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("digest_deliveries")
    op.drop_table("digest_subscriptions")
    op.drop_table("intelligence_digests")
