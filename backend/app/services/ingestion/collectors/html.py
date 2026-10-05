from urllib.parse import urljoin

from bs4 import BeautifulSoup

from app.services.ingestion.article_parser import parse_article
from app.services.ingestion.collectors.base import CollectedItem
from app.services.ingestion.fetcher import HttpFetcher
from app.services.ingestion.normalizer import normalize_text


class HtmlIndexCollector:
    def __init__(self, fetcher: HttpFetcher):
        self.fetcher = fetcher

    async def collect(self, source: dict) -> list[CollectedItem]:
        selectors = source.get("selectors", {})
        async with self.fetcher.client() as client:
            index_html = await self.fetcher.fetch_text(client, source["url"])
            soup = BeautifulSoup(index_html, "html.parser")
            links = []
            for link in soup.select(selectors.get("link", "a[href]")):
                href = link.get("href")
                if href:
                    links.append((normalize_text(link.get_text(" ", strip=True)), urljoin(source["url"], href)))
            items = []
            for link_title, url in links[: source.get("max_items", 30)]:
                try:
                    article_html = await self.fetcher.fetch_text(client, url)
                    parsed = parse_article(article_html, selectors)
                    title = parsed["title"] or link_title
                    if title and parsed["content"]:
                        items.append(CollectedItem(title=title, url=url, content=parsed["content"], language=source.get("language", "en")))
                except Exception:
                    continue
        return items
