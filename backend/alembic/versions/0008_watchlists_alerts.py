"""add watchlist and alert domain"""
from alembic import op
import sqlalchemy as sa

revision = "0008_watchlists_alerts"
down_revision = "0007_ask_query"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind(); tables = set(sa.inspect(bind).get_table_names())
    if "watchlists" not in tables:
        op.create_table("watchlists", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("user_id", sa.String(36), nullable=True), sa.Column("name", sa.String(160), nullable=False), sa.Column("description", sa.Text(), nullable=True), sa.Column("enabled", sa.Boolean(), nullable=False))
    if "watch_rules" not in tables:
        op.create_table("watch_rules", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("watchlist_id", sa.String(36), sa.ForeignKey("watchlists.id"), nullable=False), sa.Column("rule_type", sa.String(50), nullable=False), sa.Column("operator", sa.String(20), nullable=False), sa.Column("value_json", sa.JSON(), nullable=False), sa.Column("enabled", sa.Boolean(), nullable=False))
    if "alerts" not in tables:
        op.create_table("alerts", sa.Column("id", sa.String(36), primary_key=True), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False), sa.Column("watchlist_id", sa.String(36), sa.ForeignKey("watchlists.id"), nullable=False), sa.Column("watch_rule_snapshot_json", sa.JSON(), nullable=False), sa.Column("event_cluster_id", sa.String(36), sa.ForeignKey("event_clusters.id"), nullable=True), sa.Column("opportunity_id", sa.String(36), sa.ForeignKey("opportunities.id"), nullable=True), sa.Column("alert_type", sa.String(40), nullable=False), sa.Column("title", sa.String(500), nullable=False), sa.Column("summary", sa.Text(), nullable=False), sa.Column("priority", sa.String(20), nullable=False), sa.Column("status", sa.String(20), nullable=False), sa.Column("match_reason_json", sa.JSON(), nullable=False), sa.Column("read_at", sa.DateTime(timezone=True), nullable=True), sa.Column("dismissed_at", sa.DateTime(timezone=True), nullable=True))
    specs = [("watchlists", "ix_watchlists_user_id", "user_id"), ("watchlists", "ix_watchlists_enabled", "enabled"), ("watch_rules", "ix_watch_rules_watchlist_id", "watchlist_id"), ("watch_rules", "ix_watch_rules_rule_type", "rule_type"), ("alerts", "ix_alerts_watchlist_id", "watchlist_id"), ("alerts", "ix_alerts_event_cluster_id", "event_cluster_id"), ("alerts", "ix_alerts_opportunity_id", "opportunity_id"), ("alerts", "ix_alerts_priority", "priority"), ("alerts", "ix_alerts_status", "status")]
    for table, name, column in specs:
        if name not in {item["name"] for item in sa.inspect(bind).get_indexes(table)}: op.create_index(name, table, [column], unique=False)


def downgrade() -> None:
    op.drop_table("alerts"); op.drop_table("watch_rules"); op.drop_table("watchlists")
