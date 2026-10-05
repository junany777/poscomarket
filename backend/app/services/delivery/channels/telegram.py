import httpx

from app.core.config import settings
from app.services.delivery.base import DeliveryMessage, DeliveryResult


class TelegramAdapter:
    async def send(self, message: DeliveryMessage, channel) -> DeliveryResult:
        if not settings.telegram_bot_token:
            return DeliveryResult(False, error_code="TELEGRAM_TOKEN_MISSING", error_message="TELEGRAM_BOT_TOKEN is not configured", retryable=False)
        chat_id = (channel.config_json or {}).get("chat_id")
        if not chat_id:
            return DeliveryResult(False, error_code="TELEGRAM_CHAT_ID_MISSING", error_message="chat_id is missing", retryable=False)
        url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.post(url, json={"chat_id": chat_id, "text": message.body, "disable_web_page_preview": False})
            if response.status_code == 200:
                payload = response.json().get("result", {})
                return DeliveryResult(True, external_message_id=str(payload.get("message_id")) if payload.get("message_id") else None)
            retryable = response.status_code == 429 or response.status_code >= 500
            return DeliveryResult(False, error_code=f"TELEGRAM_HTTP_{response.status_code}", error_message="Telegram API rejected the message", retryable=retryable)
        except httpx.HTTPError as exc:
            return DeliveryResult(False, error_code="TELEGRAM_NETWORK_ERROR", error_message=str(exc)[:240], retryable=True)
