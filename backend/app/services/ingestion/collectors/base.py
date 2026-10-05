from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol


@dataclass
class CollectedItem:
    title: str
    url: str
    content: str
    published_at: str | None = None
    external_id: str | None = None
    language: str = "en"
    metadata: dict = field(default_factory=dict)


class Collector(Protocol):
    async def collect(self, source: dict) -> list[CollectedItem]: ...
