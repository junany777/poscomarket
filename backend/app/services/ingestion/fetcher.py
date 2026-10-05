import asyncio

import httpx


class FetchError(RuntimeError):
    pass


class HttpFetcher:
    def __init__(self, timeout: float = 20, retries: int = 2, max_concurrency: int = 5, user_agent: str = "SteelMarketIntelligence/0.1"):
        self.timeout = timeout
        self.retries = retries
        self._semaphore = asyncio.Semaphore(max_concurrency)
        self.user_agent = user_agent

    async def fetch_text(self, client: httpx.AsyncClient, url: str) -> str:
        async with self._semaphore:
            last_error: Exception | None = None
            for attempt in range(self.retries + 1):
                try:
                    response = await client.get(url, timeout=self.timeout, headers={"User-Agent": self.user_agent})
                    response.raise_for_status()
                    return response.text
                except (httpx.HTTPError, TimeoutError) as exc:
                    last_error = exc
                    if attempt < self.retries:
                        await asyncio.sleep(0.25 * (attempt + 1))
            raise FetchError(f"fetch failed: {url}") from last_error

    def client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(follow_redirects=True)
