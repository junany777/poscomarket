import hashlib
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from app.services.ingestion.collectors.base import CollectedItem


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").replace("\u00a0", " ")).strip()


def canonicalize_url(url: str) -> str:
    parts = urlsplit((url or "").strip())
    query = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if not key.lower().startswith("utm_") and key.lower() not in {"fbclid", "gclid"}]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/") or "/", urlencode(query), ""))


def normalize_item(item: CollectedItem) -> CollectedItem:
    item.title = normalize_text(item.title)
    item.content = normalize_text(item.content)
    item.url = canonicalize_url(item.url)
    item.metadata = {**item.metadata, "canonical_url": item.url, "content_hash": hashlib.sha256(item.content.encode("utf-8")).hexdigest()}
    return item
