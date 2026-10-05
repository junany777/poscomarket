from app.core.exceptions import InvalidEvidence


def validate_evidence_quote(source_text: str, quote_text: str) -> bool:
    return bool(quote_text) and quote_text in source_text


def require_evidence_quote(source_text: str, quote_text: str) -> None:
    if not validate_evidence_quote(source_text, quote_text):
        raise InvalidEvidence("Evidence quote must be an exact substring of the source document")

