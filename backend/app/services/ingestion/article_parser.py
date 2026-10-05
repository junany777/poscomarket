from bs4 import BeautifulSoup


def parse_article(html: str, selectors: dict | None = None) -> dict:
    selectors = selectors or {}
    soup = BeautifulSoup(html, "html.parser")
    for node in soup(["script", "style", "noscript", "nav", "footer"]):
        node.decompose()
    title_node = soup.select_one(selectors.get("title", "h1, h2, title"))
    content_node = soup.select_one(selectors.get("content", "article, main, .content, body"))
    title = title_node.get_text(" ", strip=True) if title_node else ""
    content = content_node.get_text(" ", strip=True) if content_node else soup.get_text(" ", strip=True)
    return {"title": title[:500], "content": content}
