from dataclasses import dataclass


DEFAULT_KEYWORDS = {"steel", "steelmaking", "automotive", "ev", "battery", "construction", "energy", "포스코", "철강", "자동차", "전기차", "배터리", "건설", "에너지"}


@dataclass(frozen=True)
class RelevanceResult:
    relevant: bool
    score: float
    matched_keywords: list[str]


def assess_relevance(title: str, content: str, source: dict, threshold: float = 2) -> RelevanceResult:
    text = f"{title} {content}".lower()
    keywords = set(source.get("keywords", [])) | DEFAULT_KEYWORDS
    matched = sorted({word for word in keywords if word.lower() in text})
    score = float(len(matched))
    if source.get("type") == "OFFICIAL":
        score += 1
    return RelevanceResult(score >= threshold, score, matched)
