"""add alert delivery layer"""
from alembic import op
import sqlalchemy as sa

revision = "0009_alert_delivery"
down_revision = "0008_watchlists_alerts"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind(); tables = set(sa.inspect(bind).get_table_names())
    if "delivery_channels" not in tables:
        op.create_table("delivery_channels", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("user_id", sa.String(36), nullable=True), sa.Column("channel_type", sa.String(30), nullable=False), sa.Column("name", sa.String(160), nullable=False), sa.Column("enabled", sa.Boolean(), nullable=False), sa.Column("config_json", sa.JSON(), nullable=False))
    if "alert_delivery_subscriptions" not in tables:
        op.create_table("alert_delivery_subscriptions", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("watchlist_id", sa.String(36), sa.ForeignKey("watchlists.id"), nullable=True), sa.Column("user_id", sa.String(36), nullable=True), sa.Column("delivery_channel_id", sa.String(36), sa.ForeignKey("delivery_channels.id"), nullable=False), sa.Column("enabled", sa.Boolean(), nullable=False), sa.Column("minimum_priority", sa.String(20), nullable=True))
    if "alert_deliveries" not in tables:
        op.create_table("alert_deliveries", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("alert_id", sa.String(36), sa.ForeignKey("alerts.id"), nullable=False), sa.Column("delivery_channel_id", sa.String(36), sa.ForeignKey("delivery_channels.id"), nullable=False), sa.Column("status", sa.String(30), nullable=False), sa.Column("attempt_count", sa.Integer(), nullable=False), sa.Column("last_attempt_at", sa.DateTime(timezone=True), nullable=True), sa.Column("delivered_at", sa.DateTime(timezone=True), nullable=True), sa.Column("external_message_id", sa.String(160), nullable=True), sa.Column("error_code", sa.String(60), nullable=True), sa.Column("error_message", sa.Text(), nullable=True), sa.Column("message_snapshot", sa.JSON(), nullable=False), sa.UniqueConstraint("alert_id", "delivery_channel_id", name="uq_alert_delivery_alert_channel"))
    specs = [("delivery_channels", "ix_delivery_channels_user_id", "user_id"), ("delivery_channels", "ix_delivery_channels_channel_type", "channel_type"), ("delivery_channels", "ix_delivery_channels_enabled", "enabled"), ("alert_delivery_subscriptions", "ix_alert_delivery_subscriptions_watchlist_id", "watchlist_id"), ("alert_delivery_subscriptions", "ix_alert_delivery_subscriptions_delivery_channel_id", "delivery_channel_id"), ("alert_delivery_subscriptions", "ix_alert_delivery_subscriptions_enabled", "enabled"), ("alert_deliveries", "ix_alert_deliveries_alert_id", "alert_id"), ("alert_deliveries", "ix_alert_deliveries_delivery_channel_id", "delivery_channel_id"), ("alert_deliveries", "ix_alert_deliveries_status", "status")]
    for table, name, column in specs:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}: op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("alert_deliveries"); op.drop_table("alert_delivery_subscriptions"); op.drop_table("delivery_channels")
