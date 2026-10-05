from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import Alert, Company, Event, EventCluster, Opportunity, ProductMatch, SteelDemandHypothesis, StrategyInference, WatchRule, Watchlist
from app.services.alerts.matcher import RULE_TYPES, OPERATORS, match_watchlist


def priority_for_score(score: float | None) -> str:
    if score is None: return "LOW"
    return "HIGH" if score >= 80 else "MEDIUM" if score >= 60 else "LOW"


def validate_rule(rule: dict, db: Session) -> dict:
    dimension, operator = str(rule.get("dimension", "")).upper(), str(rule.get("operator", "")).upper()
    if dimension not in RULE_TYPES or operator not in OPERATORS: raise ValueError("invalid watch rule dimension or operator")
    value = rule.get("value")
    if value is None: raise ValueError("watch rule value is required")
    if dimension == "COMPANY":
        company = db.get(Company, str(value))
        if not company:
            company = db.scalar(select(Company).where(Company.normalized_name == str(value).lower()))
        if not company: raise ValueError("company rule must reference an existing company")
        value = company.id
    elif dimension in {"OPPORTUNITY_SCORE", "OPPORTUNITY_CONFIDENCE", "PRODUCT_MATCH_CONFIDENCE", "EVENT_CONFIDENCE"}:
        value = float(value)
    elif dimension in {"INDUSTRY", "EVENT_TYPE", "STRATEGY", "APPLICATION", "COMPONENT", "MATERIAL_CATEGORY", "PRODUCT_FAMILY", "OPPORTUNITY_STATUS"}:
        value = value if isinstance(value, list) else str(value).upper()
        allowed = {
            "INDUSTRY": {"AUTOMOTIVE", "SHIPBUILDING", "CONSTRUCTION", "ENERGY", "HOME_APPLIANCE", "MACHINERY", "SEMICONDUCTOR"},
            "PRODUCT_FAMILY": {"HYPER_NO", "ATOS", "AUTOMOTIVE_STEEL", "GALVANIZED_STEEL", "ELECTRO_GALVANIZED_STEEL", "POSMAC_1_5", "POSMAC_3_0", "POSMAC_SUPER"},
            "APPLICATION": {"EV_MOTOR", "VEHICLE_BODY", "COMMERCIAL_VEHICLE"},
            "COMPONENT": {"MOTOR_CORE", "STRUCTURAL_MEMBER", "TRUCK_FRAME"},
        }.get(dimension)
        if allowed and any(str(item).upper() not in allowed for item in (value if isinstance(value, list) else [value])): raise ValueError(f"invalid canonical value for {dimension}")
    return {"dimension": dimension, "operator": operator, "value": value}


def _context(db: Session, opportunity: Opportunity | None = None, cluster: EventCluster | None = None) -> tuple[dict, EventCluster | None]:
    event = db.get(Event, opportunity.event_id) if opportunity else (db.get(Event, cluster.canonical_event_id) if cluster and cluster.canonical_event_id else None)
    company = db.get(Company, event.company_id) if event and event.company_id else None
    demand = db.scalar(select(SteelDemandHypothesis).where(SteelDemandHypothesis.event_id == event.id)) if event else None
    strategy = db.scalar(select(StrategyInference).where(StrategyInference.event_id == event.id)) if event else None
    product = db.get(ProductMatch, opportunity.product_match_id) if opportunity and opportunity.product_match_id else None
    actual_cluster = cluster or (db.get(EventCluster, event.event_cluster_id) if event and event.event_cluster_id else None)
    return {"COMPANY": company.id if company else None, "INDUSTRY": (company.industry_code if company else None) or (demand.industry_code if demand else None), "EVENT_TYPE": event.primary_event_type if event else None, "STRATEGY": strategy.strategy_code if strategy else None, "APPLICATION": demand.application_code if demand else None, "COMPONENT": demand.component_code if demand else None, "MATERIAL_CATEGORY": demand.material_category if demand else None, "PRODUCT_FAMILY": product.product_family if product else None, "OPPORTUNITY_SCORE": opportunity.score if opportunity else None, "OPPORTUNITY_STATUS": opportunity.status if opportunity else None, "OPPORTUNITY_CONFIDENCE": opportunity.confidence if opportunity else None, "PRODUCT_MATCH_CONFIDENCE": product.confidence if product else None, "EVENT_CONFIDENCE": event.confidence if event else None}, actual_cluster


def _create_alert(db: Session, watchlist: Watchlist, rules: list[WatchRule], values: dict, match: dict, opportunity: Opportunity | None, cluster: EventCluster | None, alert_type: str) -> Alert | None:
    if not match["matched"]: return None
    existing = db.scalar(select(Alert).where(Alert.watchlist_id == watchlist.id, Alert.opportunity_id == (opportunity.id if opportunity else None), Alert.event_cluster_id == (cluster.id if cluster else None), Alert.alert_type == alert_type, Alert.status != "DISMISSED"))
    if existing: return None
    title = opportunity.title if opportunity else (cluster.title if cluster else watchlist.name)
    score = opportunity.score if opportunity else None
    alert = Alert(watchlist_id=watchlist.id, watch_rule_snapshot_json=[{"dimension": rule.rule_type, "operator": rule.operator, "value": rule.value_json} for rule in rules], event_cluster_id=cluster.id if cluster else None, opportunity_id=opportunity.id if opportunity else None, alert_type=alert_type, title=title, summary=f"{watchlist.name} 조건과 일치하는 Intelligence가 감지되었습니다.", priority=priority_for_score(score), status="NEW", match_reason_json={"matched_rules": match["matched_rules"]})
    db.add(alert); return alert


def evaluate_opportunity(db: Session, opportunity_id: str) -> list[str]:
    opportunity = db.get(Opportunity, opportunity_id)
    if not opportunity: return []
    values, cluster = _context(db, opportunity=opportunity)
    created = []
    for watchlist in db.scalars(select(Watchlist).where(Watchlist.enabled)):
        rules = list(db.scalars(select(WatchRule).where(WatchRule.watchlist_id == watchlist.id, WatchRule.enabled)))
        alert = _create_alert(db, watchlist, rules, values, match_watchlist(watchlist, rules, values), opportunity, cluster, "OPPORTUNITY_MATCH")
        if alert: created.append(alert.id)
    db.commit()
    try:
        from app.services.delivery import enqueue_alert
        for alert_id in created: enqueue_alert(db, alert_id)
    except Exception:
        pass
    return created


def evaluate_event_cluster(db: Session, cluster_id: str) -> list[str]:
    cluster = db.get(EventCluster, cluster_id)
    if not cluster: return []
    values, cluster = _context(db, cluster=cluster)
    created = []
    for watchlist in db.scalars(select(Watchlist).where(Watchlist.enabled)):
        rules = list(db.scalars(select(WatchRule).where(WatchRule.watchlist_id == watchlist.id, WatchRule.enabled)))
        alert = _create_alert(db, watchlist, rules, values, match_watchlist(watchlist, rules, values), None, cluster, "EVENT_MATCH")
        if alert: created.append(alert.id)
    db.commit()
    try:
        from app.services.delivery import enqueue_alert
        for alert_id in created: enqueue_alert(db, alert_id)
    except Exception:
        pass
    return created
