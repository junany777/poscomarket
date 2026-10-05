import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import Company, Event, EventCluster, EventClusterDecisionLog, Opportunity, SourceDocument


EVENT_TYPE_COMPATIBILITY = {
    "NEW_FACTORY": {"NEW_FACTORY", "CAPACITY_EXPANSION"},
    "CAPACITY_EXPANSION": {"CAPACITY_EXPANSION", "NEW_FACTORY"},
    "CONTRACT": {"CONTRACT", "PROCUREMENT"},
    "PROCUREMENT": {"PROCUREMENT", "CONTRACT"},
}
LIFECYCLE_TYPES = {"ANNOUNCED", "APPROVED", "IN_PROGRESS", "COMMERCIAL", "COMPLETED", "DELAYED", "CANCELLED"}


@dataclass(frozen=True)
class EventClusterDecision:
    cluster_id: str | None
    decision: str
    score: float
    confidence: float
    reasons: list[str]


def _tokens(value: str | None) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9가-힣]{2,}", (value or "").lower()) if token not in {"the", "and", "with", "company", "plans"}}


def _title_similarity(a: str, b: str) -> float:
    left, right = _tokens(a), _tokens(b)
    overlap = len(left & right) / max(1, len(left | right))
    sequence = SequenceMatcher(None, a.lower(), b.lower()).ratio()
    return max(overlap, sequence * 0.8)


def _event_date(event: Event) -> datetime:
    for candidate in (event.event_date, event.created_at.isoformat() if event.created_at else None):
        if candidate:
            try:
                return datetime.fromisoformat(candidate.replace("Z", "+00:00")).replace(tzinfo=timezone.utc)
            except ValueError:
                continue
    return datetime.now(timezone.utc)


def _compatible(left: str, right: str) -> bool:
    return right in EVENT_TYPE_COMPATIBILITY.get(left, {left})


def generate_candidates(db: Session, event: Event) -> list[EventCluster]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=settings.event_cluster_lookback_days)
    query = select(EventCluster).where(EventCluster.last_seen_at >= cutoff, EventCluster.primary_event_type.in_(list(EVENT_TYPE_COMPATIBILITY.get(event.primary_event_type, {event.primary_event_type}))))
    if event.company_id:
        query = query.where(EventCluster.primary_company_id == event.company_id)
    clusters = list(db.scalars(query.order_by(EventCluster.last_seen_at.desc()).limit(settings.event_cluster_max_candidates)))
    event_day = _event_date(event)
    return [cluster for cluster in clusters if abs((_event_date(event) - _event_date(db.get(Event, cluster.canonical_event_id))).days) <= settings.event_cluster_date_tolerance_days] if clusters else []


def score_candidate(event: Event, cluster: EventCluster, canonical: Event, source: SourceDocument | None = None) -> tuple[float, list[str]]:
    score = 0.0
    reasons = []
    if event.company_id and event.company_id == cluster.primary_company_id:
        score += 25; reasons.append("same_company")
    if event.primary_event_type == cluster.primary_event_type:
        score += 20; reasons.append("same_event_type")
    else:
        score += 10; reasons.append("compatible_event_type")
    gap = abs((_event_date(event) - _event_date(canonical)).days)
    if gap <= settings.event_cluster_date_tolerance_days:
        score += max(0, 15 - gap); reasons.append("date_proximity")
    title_score = _title_similarity(event.title, canonical.title)
    if title_score >= 0.25:
        score += round(10 * title_score, 2); reasons.append("title_similarity")
    left_meta, right_meta = event.metadata_json or {}, canonical.metadata_json or {}
    if left_meta.get("application") and left_meta.get("application") == right_meta.get("application"):
        score += 5; reasons.append("application_match")
    if left_meta.get("component") and left_meta.get("component") == right_meta.get("component"):
        score += 5; reasons.append("component_match")
    if left_meta.get("project_name") and left_meta.get("project_name") == right_meta.get("project_name"):
        score += 15; reasons.append("project_match")
    if set((left_meta.get("numeric_facts") or {}).keys()) & set((right_meta.get("numeric_facts") or {}).keys()):
        score += 5; reasons.append("numeric_fact_match")
    if source and source.metadata_json.get("source_authority") in {"OFFICIAL", "PRIMARY"}:
        score += 5; reasons.append("authoritative_source")
    lifecycle_left = left_meta.get("lifecycle_status")
    lifecycle_right = right_meta.get("lifecycle_status")
    if lifecycle_left in LIFECYCLE_TYPES and lifecycle_right in LIFECYCLE_TYPES and lifecycle_left != lifecycle_right:
        return min(score, settings.event_cluster_review_threshold - 1), reasons + ["different_lifecycle_stage"]
    return min(100.0, round(score, 2)), reasons


def _conflicts(events: list[Event]) -> list[dict]:
    fields: dict[str, list[dict]] = {}
    for event in events:
        for field, value in (event.metadata_json or {}).get("numeric_facts", {}).items():
            fields.setdefault(field, []).append({"value": value, "event_id": event.id, "source_document_id": event.source_document_id})
    return [{"field": field, "values": values} for field, values in fields.items() if len({str(item["value"]) for item in values}) > 1]


def _refresh_cluster(db: Session, cluster: EventCluster) -> None:
    members = list(db.scalars(select(Event).where(Event.event_cluster_id == cluster.id).order_by(Event.created_at.asc())))
    if not members:
        return
    canonical = db.get(Event, cluster.canonical_event_id) if cluster.canonical_event_id else members[0]
    ranked = sorted(members, key=lambda item: (bool((item.metadata_json or {}).get("source_authority") in {"OFFICIAL", "PRIMARY"}), len(item.summary or ""), item.confidence), reverse=True)
    canonical = ranked[0]
    for member in members:
        member.is_canonical = member.id == canonical.id
    cluster.canonical_event_id = canonical.id
    cluster.primary_company_id = canonical.company_id
    cluster.primary_event_type = canonical.primary_event_type
    cluster.title = canonical.title
    cluster.summary = canonical.summary
    cluster.event_date = canonical.event_date
    cluster.location = canonical.location
    cluster.source_count = len({member.source_document_id for member in members})
    cluster.first_seen_at = min(member.created_at for member in members)
    cluster.last_seen_at = max(member.created_at for member in members)
    cluster.cluster_metadata_json = {**(cluster.cluster_metadata_json or {}), "conflicts": _conflicts(members), "canonical_event_id": canonical.id}
    if cluster.cluster_metadata_json["conflicts"]:
        cluster.status = "UPDATED"


def assign_event_to_cluster(db: Session, event: Event, source: SourceDocument | None = None) -> EventClusterDecision:
    candidates = generate_candidates(db, event)
    best: tuple[float, EventCluster, list[str]] | None = None
    for cluster in candidates:
        canonical = db.get(Event, cluster.canonical_event_id)
        if not canonical:
            continue
        score, reasons = score_candidate(event, cluster, canonical, source)
        if best is None or score > best[0]:
            best = (score, cluster, reasons)
    if not best or best[0] < settings.event_cluster_auto_threshold:
        now = datetime.now(timezone.utc)
        decision = "NEW_CLUSTER" if not best or best[0] < settings.event_cluster_review_threshold else "REVIEW_REQUIRED"
        cluster = EventCluster(primary_company_id=event.company_id, primary_event_type=event.primary_event_type, title=event.title, summary=event.summary, event_date=event.event_date, location=event.location, status="ACTIVE" if decision == "NEW_CLUSTER" else "REVIEW_REQUIRED", confidence=event.confidence, source_count=0, first_seen_at=now, last_seen_at=now, cluster_metadata_json={})
        db.add(cluster); db.flush()
        event.event_cluster_id = cluster.id
        _refresh_cluster(db, cluster)
        db.add(EventClusterDecisionLog(event_id=event.id, candidate_cluster_id=cluster.id, score=best[0] if best else 0, decision=decision, reasons_json=best[2] if best else ["no_candidate"]))
        db.flush()
        return EventClusterDecision(cluster.id, decision, best[0] if best else 0, event.confidence, best[2] if best else ["no_candidate"])
    score, cluster, reasons = best
    decision = "AUTO_CLUSTER" if score >= settings.event_cluster_auto_threshold else "REVIEW_REQUIRED"
    if decision == "REVIEW_REQUIRED":
        return EventClusterDecision(None, decision, score, score / 100, reasons)
    event.event_cluster_id = cluster.id
    _refresh_cluster(db, cluster)
    db.add(EventClusterDecisionLog(event_id=event.id, candidate_cluster_id=cluster.id, score=score, decision=decision, reasons_json=reasons))
    db.flush()
    return EventClusterDecision(cluster.id, decision, score, score / 100, reasons)


def detect_cluster_material_change(old_canonical_event: Event | None, new_canonical_event: Event | None) -> dict:
    if not old_canonical_event or not new_canonical_event:
        return {"changed": True, "fields": ["canonical_event"]}
    old = old_canonical_event.metadata_json or {}
    new = new_canonical_event.metadata_json or {}
    fields = [field for field in {"numeric_facts", "location", "lifecycle_status", "application", "component"} if old.get(field) != new.get(field)]
    return {"changed": bool(fields), "fields": sorted(fields)}


def merge_clusters(db: Session, source_cluster_id: str, target_cluster_id: str) -> EventCluster:
    source = db.get(EventCluster, source_cluster_id)
    target = db.get(EventCluster, target_cluster_id)
    if not source or not target:
        raise ValueError("Both source and target clusters are required")
    for event in db.scalars(select(Event).where(Event.event_cluster_id == source.id)):
        event.event_cluster_id = target.id
    source.status = "MERGED"
    _refresh_cluster(db, target)
    db.commit()
    return target
