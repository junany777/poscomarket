from datetime import datetime, timedelta, timezone

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import Alert, AlertDelivery, AlertDeliverySubscription, Company, DigestDelivery, DigestSubscription, Event, IntelligenceDigest, Opportunity, ProductMatch, Watchlist
from app.services.delivery.channels.telegram import TelegramAdapter
from app.services.delivery.formatter import format_alert_message


PRIORITY_RANK = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}


def enqueue_alert(db: Session, alert_id: str) -> list[str]:
    alert = db.get(Alert, alert_id)
    if not alert: return []
    subscriptions = list(db.scalars(select(AlertDeliverySubscription).where(AlertDeliverySubscription.enabled, AlertDeliverySubscription.watchlist_id == alert.watchlist_id)))
    created = []
    for subscription in subscriptions:
        channel = db.get(__import__("app.models.entities", fromlist=["DeliveryChannel"]).DeliveryChannel, subscription.delivery_channel_id)
        if not channel or not channel.enabled or (subscription.minimum_priority and PRIORITY_RANK.get(alert.priority, 1) < PRIORITY_RANK.get(subscription.minimum_priority, 1)): continue
        existing = db.scalar(select(AlertDelivery).where(AlertDelivery.alert_id == alert.id, AlertDelivery.delivery_channel_id == channel.id))
        if existing: continue
        watchlist = db.get(Watchlist, alert.watchlist_id)
        opportunity = db.get(Opportunity, alert.opportunity_id) if alert.opportunity_id else None
        event = db.get(Event, opportunity.event_id) if opportunity else None
        company = db.get(Company, event.company_id) if event and event.company_id else None
        product = db.get(ProductMatch, opportunity.product_match_id) if opportunity and opportunity.product_match_id else None
        message = format_alert_message(alert, watchlist, opportunity, company, event, product)
        db.add(AlertDelivery(alert_id=alert.id, delivery_channel_id=channel.id, status="PENDING", message_snapshot={"title": message.title, "body": message.body, "priority": message.priority, "action_url": message.action_url}))
        db.flush(); created.append(alert.id)
    db.commit(); return created


def recover_stale(db: Session) -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(seconds=settings.delivery_stale_seconds)
    for row in db.scalars(select(AlertDelivery).where(AlertDelivery.status == "SENDING", AlertDelivery.last_attempt_at < cutoff)): row.status = "RETRY_PENDING"
    db.commit()


async def process_pending(db: Session, limit: int | None = None, dry_run: bool = False) -> dict:
    from app.models.entities import DeliveryChannel
    recover_stale(db)
    rows = list(db.scalars(select(AlertDelivery).where(AlertDelivery.status.in_(["PENDING", "RETRY_PENDING"])).order_by(desc(AlertDelivery.created_at)).limit(limit or settings.delivery_worker_batch_size)))
    result = {"processed": 0, "delivered": 0, "failed": 0, "retry_pending": 0, "skipped": 0}
    for row in rows:
        channel = db.get(DeliveryChannel, row.delivery_channel_id)
        if not channel or not channel.enabled: row.status = "SKIPPED"; result["skipped"] += 1; continue
        if dry_run or settings.delivery_dry_run or settings.validation_mode: result["processed"] += 1; continue
        row.status = "SENDING"; row.attempt_count += 1; row.last_attempt_at = datetime.now(timezone.utc); db.commit()
        alert = db.get(Alert, row.alert_id)
        message = type("Message", (), row.message_snapshot)()
        if channel.channel_type == "TELEGRAM":
            from app.services.delivery.base import DeliveryMessage
            outcome = await TelegramAdapter().send(DeliveryMessage(message.title, message.body, message.priority, message.action_url), channel)
        else:
            outcome = type("Result", (), {"success": False, "error_code": "CHANNEL_UNSUPPORTED", "error_message": "channel adapter not implemented", "retryable": False, "external_message_id": None})()
        result["processed"] += 1
        if outcome.success:
            row.status = "DELIVERED"; row.delivered_at = datetime.now(timezone.utc); row.external_message_id = outcome.external_message_id; result["delivered"] += 1
        elif outcome.retryable and row.attempt_count < settings.delivery_max_attempts:
            row.status = "RETRY_PENDING"; row.error_code = outcome.error_code; row.error_message = outcome.error_message; result["retry_pending"] += 1
        else:
            row.status = "FAILED"; row.error_code = outcome.error_code; row.error_message = outcome.error_message; result["failed"] += 1
        db.commit()
    return result


def enqueue_digest(db: Session, digest_id: str) -> list[str]:
    digest = db.get(IntelligenceDigest, digest_id)
    if not digest or digest.status != "READY": return []
    created = []
    for subscription in db.scalars(select(DigestSubscription).where(DigestSubscription.enabled, DigestSubscription.digest_type == digest.digest_type)):
        channel = db.get(__import__("app.models.entities", fromlist=["DeliveryChannel"]).DeliveryChannel, subscription.delivery_channel_id)
        if not channel or not channel.enabled: continue
        if db.scalar(select(DigestDelivery).where(DigestDelivery.digest_id == digest.id, DigestDelivery.delivery_channel_id == channel.id)): continue
        content = digest.content_json or {}
        top = content.get("top_opportunities", [])[:5]
        if subscription.minimum_opportunity_score is not None and not any(float(item.get("score") or 0) >= subscription.minimum_opportunity_score for item in top): continue
        if subscription.product_families_json and not any(item.get("product_family") in subscription.product_families_json for item in top): continue
        if subscription.industries_json:
            trend_codes = {item.get("code") for group in content.get("industry_trends", []) for item in group.get("items", [])}
            if not trend_codes.intersection(set(subscription.industries_json)): continue
        lines = [f"📊 {digest.title}", "", "Executive Summary", digest.executive_summary]
        if top: lines += ["", "Top Opportunities"] + [f"• {item.get('company') or '기업'} · {item.get('product_family') or '제품 확인 필요'} · {item.get('score', 0):.0f}" for item in top]
        if content.get("watchlist_highlights"): lines += ["", f"High Priority Alerts: {len(content['watchlist_highlights'])}"]
        if settings.app_public_url: lines += ["", f"Open: {settings.app_public_url.rstrip('/')}/#digests/{digest.id}"]
        body = "\n".join(lines)[:3900]
        db.add(DigestDelivery(digest_id=digest.id, delivery_channel_id=channel.id, status="PENDING", message_snapshot={"title": digest.title, "body": body, "priority": "HIGH"}))
        db.flush(); created.append(digest.id)
    db.commit(); return created


async def process_digest_pending(db: Session, limit: int | None = None, dry_run: bool = False) -> dict:
    from app.models.entities import DeliveryChannel
    rows = list(db.scalars(select(DigestDelivery).where(DigestDelivery.status.in_(["PENDING", "RETRY_PENDING"])).order_by(DigestDelivery.created_at).limit(limit or settings.delivery_worker_batch_size)))
    result = {"processed": 0, "delivered": 0, "failed": 0, "retry_pending": 0}
    for row in rows:
        channel = db.get(DeliveryChannel, row.delivery_channel_id)
        if not channel or not channel.enabled: row.status = "SKIPPED"; db.commit(); continue
        if dry_run or settings.delivery_dry_run or settings.validation_mode: result["processed"] += 1; continue
        row.status = "SENDING"; row.attempt_count += 1; db.commit()
        snapshot = row.message_snapshot
        from app.services.delivery.base import DeliveryMessage
        outcome = await TelegramAdapter().send(DeliveryMessage(snapshot["title"], snapshot["body"], snapshot.get("priority", "HIGH")), channel) if channel.channel_type == "TELEGRAM" else None
        result["processed"] += 1
        if outcome and outcome.success: row.status = "DELIVERED"; row.delivered_at = datetime.now(timezone.utc); row.external_message_id = outcome.external_message_id; result["delivered"] += 1
        elif outcome and outcome.retryable and row.attempt_count < settings.delivery_max_attempts:
            row.status = "RETRY_PENDING"; row.error_code = outcome.error_code; row.error_message = outcome.error_message; result["retry_pending"] += 1
        else: row.status = "FAILED"; row.error_code = outcome.error_code if outcome else "CHANNEL_UNSUPPORTED"; row.error_message = outcome.error_message if outcome else "channel adapter not implemented"; result["failed"] += 1
        db.commit()
    return result
