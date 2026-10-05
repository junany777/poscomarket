import feedparser

from app.services.ingestion.article_parser import parse_article
from app.services.ingestion.collectors.base import CollectedItem
from app.services.ingestion.fetcher import HttpFetcher
from app.services.ingestion.normalizer import normalize_text


class RssCollector:
    def __init__(self, fetcher: HttpFetcher):
        self.fetcher = fetcher

    async def collect(self, source: dict) -> list[CollectedItem]:
        async with self.fetcher.client() as client:
            raw = await self.fetcher.fetch_text(client, source["url"])
        feed = feedparser.parse(raw)
        items = []
        for entry in feed.entries:
            title = normalize_text(entry.get("title", ""))
            summary = normalize_text(entry.get("summary", "") or entry.get("description", ""))
            url = entry.get("link", "")
            if not title or not url:
                continue
            items.append(CollectedItem(title=title, url=url, content=summary, published_at=entry.get("published", entry.get("updated")), external_id=entry.get("id"), language=source.get("language", "en"), metadata={"feed_id": entry.get("id")}))
        return items
