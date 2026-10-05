from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class DeliveryMessage:
    title: str
    body: str
    priority: str
    action_url: str | None = None
    metadata: dict = field(default_factory=dict)


@dataclass
class DeliveryResult:
    success: bool
    external_message_id: str | None = None
    error_code: str | None = None
    error_message: str | None = None
    retryable: bool = False


class DeliveryAdapter(Protocol):
    async def send(self, message: DeliveryMessage, channel) -> DeliveryResult: ...
