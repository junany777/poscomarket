from app.core.config import settings
from app.models.entities import Alert, Company, Event, Opportunity, ProductMatch, Watchlist
from app.services.delivery.base import DeliveryMessage


def format_alert_message(alert: Alert, watchlist: Watchlist | None = None, opportunity: Opportunity | None = None, company: Company | None = None, event: Event | None = None, product: ProductMatch | None = None) -> DeliveryMessage:
    lines = [f"🔔 {alert.priority} {'Opportunity' if opportunity else 'Event'}", "", company.name if company else "기업 정보 없음", alert.title]
    if event: lines += ["", f"Event: {event.primary_event_type}"]
    if product and product.product_family: lines += [f"Product: {product.product_family}"]
    if opportunity: lines += [f"Score: {opportunity.score:.0f}"]
    if watchlist: lines += [f"Watchlist: {watchlist.name}"]
    matched = (alert.match_reason_json or {}).get("matched_rules", [])
    if matched: lines += ["", "Why matched"] + [f"• {item['dimension']} {item['operator']} {item['expected']} (actual: {item['actual']})" for item in matched[:5]]
    if settings.app_public_url and opportunity: lines += ["", f"Open: {settings.app_public_url.rstrip('/')}/#opportunity/{opportunity.id}"]
    text = "\n".join(lines)
    return DeliveryMessage(title=alert.title, body=text[:3900], priority=alert.priority, action_url=f"{settings.app_public_url.rstrip('/')}/#opportunity/{opportunity.id}" if settings.app_public_url and opportunity else None, metadata={"alert_id": alert.id})
