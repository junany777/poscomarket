import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


INTENTS = {"OPPORTUNITY_SEARCH", "OPPORTUNITY_EXPLAIN", "EVENT_SEARCH", "EVENT_EXPLAIN", "COMPANY_INTELLIGENCE", "PRODUCT_OPPORTUNITY", "EVIDENCE_LOOKUP", "TREND_SUMMARY", "COMPARISON", "UNKNOWN"}
COMPANIES = {"현대차": "Hyundai Motor", "현대자동차": "Hyundai Motor", "hyundai": "Hyundai Motor", "기아": "Kia", "삼성전자": "Samsung Electronics", "hd현대": "HD Hyundai"}
PRODUCTS = {"hyper no": "HYPER_NO", "hyper_no": "HYPER_NO", "하이퍼 no": "HYPER_NO", "posmac super": "POSMAC_SUPER", "포스맥 슈퍼": "POSMAC_SUPER", "atos": "ATOS", "아토스": "ATOS", "gi": "GALVANIZED_STEEL", "eg": "ELECTRO_GALVANIZED_STEEL"}


@dataclass
class AskIntent:
    intent: str
    company_names: list[str] = field(default_factory=list)
    industries: list[str] = field(default_factory=list)
    event_types: list[str] = field(default_factory=list)
    product_families: list[str] = field(default_factory=list)
    applications: list[str] = field(default_factory=list)
    components: list[str] = field(default_factory=list)
    date_from: datetime | None = None
    date_to: datetime | None = None
    minimum_score: int | None = None
    needs_product_knowledge: bool = False


def classify(question: str) -> AskIntent:
    q = question.lower()
    companies = [canonical for alias, canonical in COMPANIES.items() if alias in q]
    products = [canonical for alias, canonical in PRODUCTS.items() if alias in q]
    minimum = int(re.search(r"(\d{2,3})\s*점", q).group(1)) if re.search(r"(\d{2,3})\s*점", q) else None
    if any(word in q for word in ("왜", "이유", "판단", "점수가 높", "why")) and products:
        intent = "PRODUCT_OPPORTUNITY" if products else "OPPORTUNITY_EXPLAIN"
    elif any(word in q for word in ("근거", "기사", "source", "evidence")):
        intent = "EVIDENCE_LOOKUP"
    elif any(word in q for word in ("추세", "트렌드", "trend")):
        intent = "TREND_SUMMARY"
    elif any(word in q for word in ("비교", "compare")):
        intent = "COMPARISON"
    elif any(word in q for word in ("사건", "event", "보도한")):
        intent = "EVENT_SEARCH"
    elif any(word in q for word in ("회사", "기업", "company")) and companies:
        intent = "COMPANY_INTELLIGENCE"
    elif products or any(word in q for word in ("기회", "opportunity", "영업")):
        intent = "PRODUCT_OPPORTUNITY" if products else "OPPORTUNITY_SEARCH"
    else:
        intent = "UNKNOWN"
    date_from = datetime.now(timezone.utc) - timedelta(days=30) if any(word in q for word in ("최근", "최신", "요즘", "recent", "latest")) else None
    return AskIntent(intent=intent, company_names=companies, product_families=products, minimum_score=minimum, date_from=date_from, date_to=datetime.now(timezone.utc) if date_from else None, needs_product_knowledge=bool(products or any(word in q for word in ("제품", "grade", "등급", "왜 hyper", "왜 posmac"))))
