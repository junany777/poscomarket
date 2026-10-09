from collections import Counter
from datetime import datetime, timedelta, timezone
import re

import httpx

from app.core.config import settings


MANUFACTURING_CATEGORIES = {
    "AUTOMOTIVE": ("자동차", ("자동차", "현대차", "기아", "모비스", "만도", "타이어")),
    "SHIPBUILDING": ("조선", ("조선", "선박", "해양", "한화오션", "중공업", "조선해양")),
    "CONSTRUCTION": ("건설", ("건설", "건축", "토목", "플랜트", "현대건설", "두산건설")),
    "ENERGY": ("에너지", ("에너지", "발전", "전력", "태양광", "풍력", "수소", "연료전지")),
    "HOME_APPLIANCE": ("가전", ("가전", "냉장고", "세탁기", "에어컨", "lg전자", "삼성전자")),
    "MACHINERY": ("기계", ("기계", "장비", "로봇", "공작기계", "두산밥캣", "효성중공업")),
    "SEMICONDUCTOR": ("반도체", ("반도체", "웨이퍼", "sk하이닉스", "db하이텍", "하이닉스")),
}

HARD_EXCLUSION_RULES = (
    ("FINANCIAL_PRODUCT_DOCUMENT", ("집합투자증권",)),
    ("OWNERSHIP_ONLY", ("주식등의대량보유상황보고서", "임원ㆍ주요주주특정증권등소유상황보고서")),
    ("SECURITIES_OFFERING_ONLY", ("소액공모공시서류(지분증권)", "주식관련사채등의발행결과")),
    ("GOVERNANCE_ONLY", ("주주총회소집", "대표이사변경", "임원변경", "감사보고서")),
)

STRONG_RELEVANCE_KEYWORDS = (
    "신규시설투자", "시설투자", "설비투자", "공장신설", "공장건설", "증설", "생산능력", "생산라인", "설비도입",
    "착공", "준공", "생산개시", "생산중단", "생산재개", "가동중단", "가동재개", "공장폐쇄",
    "단일판매ㆍ공급계약체결", "공급계약", "수주", "납품", "프로젝트", "플랜트", "공사계약", "구매계약", "조달계약", "장기공급",
    "계약해지", "계약취소", "프로젝트취소", "신사업", "사업목적추가", "합병", "영업양수", "영업양도", "분할", "인수",
    "합작법인", "공동투자", "연구개발", "기술도입", "기술이전", "제품출시", "상용화", "환경규제", "배출규제", "탄소",
    "공급망", "현지조달", "원재료조달", "생산거점", "안전조치", "설비교체",
)

CONDITIONAL_RELEVANCE_RULES = (
    ("FINANCING_PURPOSE_UNKNOWN", ("유상증자", "사채발행", "차입", "자금조달"), ("시설자금", "공장", "증설", "생산라인", "신사업", "인수", "설비")),
    ("ACQUISITION_PURPOSE_UNKNOWN", ("타법인주식및출자증권취득",), ("경영권", "생산능력", "기술", "공급망", "합작사업", "인수")),
    ("IR_CONTENT_MISSING", ("기업설명회",), ("시설투자", "설비투자", "공장", "증설", "생산", "수주", "신사업", "공급망")),
    ("PHYSICAL_IMPACT_UNKNOWN", ("중대재해",), ("가동", "공사중단", "프로젝트", "설비", "공장")),
)


class DartClient:
    """Small, secret-safe OpenDART client for connectivity and disclosure reads."""

    def __init__(self) -> None:
        self.api_key = settings.dart_api_key
        self.base_url = settings.dart_base_url.rstrip("/")

    def _dates(self, bgn_de: str | None, end_de: str | None) -> tuple[str, str]:
        end = datetime.now(timezone.utc).date()
        start = end - timedelta(days=7)
        return bgn_de or start.strftime("%Y%m%d"), end_de or end.strftime("%Y%m%d")

    async def _request(self, params: dict) -> dict:
        async with httpx.AsyncClient(timeout=settings.dart_timeout_seconds) as client:
            response = await client.get(f"{self.base_url}/list.json", params={"crtfc_key": self.api_key, **params})
            response.raise_for_status()
            payload = response.json()
        return payload if isinstance(payload, dict) else {}

    async def health(self) -> dict:
        checked_at = datetime.now(timezone.utc).isoformat()
        if not self.api_key:
            return {"provider": "OpenDART", "configured": False, "connected": False, "status": "NOT_CONFIGURED", "message": "DART_API_KEY가 설정되지 않았습니다.", "checked_at": checked_at}
        today = datetime.now(timezone.utc).strftime("%Y%m%d")
        try:
            payload = await self._request({"bgn_de": today, "end_de": today, "page_no": 1, "page_count": 1})
            dart_status = str(payload.get("status", ""))
            connected = dart_status in {"000", "013"}
            return {"provider": "OpenDART", "configured": True, "connected": connected, "status": "CONNECTED" if connected else "API_ERROR", "message": "OpenDART 응답을 확인했습니다." if connected else str(payload.get("message", "OpenDART 응답 오류")), "checked_at": checked_at}
        except (httpx.HTTPError, ValueError) as exc:
            return {"provider": "OpenDART", "configured": True, "connected": False, "status": "NETWORK_ERROR", "message": f"OpenDART 연결 실패: {type(exc).__name__}", "checked_at": checked_at}

    async def disclosures(self, bgn_de: str | None = None, end_de: str | None = None, corp_code: str | None = None, industry: str | None = None, page_no: int = 1, page_count: int = 20, include_audit: bool = False) -> dict:
        if not self.api_key:
            return {"provider": "OpenDART", "configured": False, "connected": False, "status": "NOT_CONFIGURED", "message": "DART_API_KEY가 설정되지 않았습니다.", "items": [], "total_count": 0, "page_no": page_no, "page_count": page_count}
        bgn_de, end_de = self._dates(bgn_de, end_de)
        params = {"bgn_de": bgn_de, "end_de": end_de, "page_no": page_no, "page_count": page_count}
        if corp_code:
            params["corp_code"] = corp_code
        try:
            payload = await self._request(params)
            dart_status = str(payload.get("status", ""))
            connected = dart_status in {"000", "013"}
            items = [self._normalize(item) for item in (payload.get("list") or [])]
            # DART returns mixed industries in one chronological list. Read a few
            # pages so the manufacturing-only view is not dominated by unrelated
            # financial disclosures.
            raw_total_count = int(payload.get("total_count") or 0)
            max_pages = min(5, max(1, (raw_total_count + page_count - 1) // page_count))
            for next_page in range(page_no + 1, page_no + max_pages):
                if len([item for item in items if item.get("posco_relevance", {}).get("decision") == "KEEP_DATA"]) >= 30:
                    break
                next_payload = await self._request({**params, "page_no": next_page})
                if str(next_payload.get("status", "")) not in {"000", "013"}:
                    break
                items.extend(self._normalize(item) for item in (next_payload.get("list") or []))
            items, audit, metrics = self._filter_relevant_items(items, industry)
            excluded = [item for item in audit if item.get("posco_relevance", {}).get("decision") != "KEEP_DATA"]
            exclusion_reasons = Counter(item.get("posco_relevance", {}).get("reason_code", "UNKNOWN") for item in excluded)
            result = {"provider": "OpenDART", "configured": True, "connected": connected, "status": "CONNECTED" if connected else "API_ERROR", "message": "POSCO 연관 공시가 없습니다." if not items and connected else ("POSCO 연관 공시를 조회했습니다." if connected else str(payload.get("message", "OpenDART 응답 오류"))), "items": items, "total_count": len(items), "evaluated_count": metrics["evaluated_count"], "kept_count": metrics["kept_count"], "excluded_count": metrics["excluded_count"], "non_target_issuer_count": metrics["non_target_issuer_count"], "exclusion_reasons": dict(exclusion_reasons), "raw_total_count": raw_total_count, "page_no": int(payload.get("page_no") or page_no), "page_count": page_count, "manufacturing_only": True, "posco_relevance_only": True, "industries": [{"code": code, "name_ko": name} for code, (name, _) in MANUFACTURING_CATEGORIES.items()], "period": {"bgn_de": bgn_de, "end_de": end_de}}
            if include_audit:
                result["relevance_audit"] = audit
            return result
        except (httpx.HTTPError, ValueError) as exc:
            return {"provider": "OpenDART", "configured": True, "connected": False, "status": "NETWORK_ERROR", "message": f"OpenDART 연결 실패: {type(exc).__name__}", "items": [], "total_count": 0, "page_no": page_no, "page_count": page_count}

    async def analysis(self, bgn_de: str | None = None, end_de: str | None = None) -> dict:
        result = await self.disclosures(bgn_de=bgn_de, end_de=end_de, page_count=100)
        return self._build_analysis(result)

    @staticmethod
    def _build_analysis(result: dict) -> dict:
        items = result.get("items", [])
        signal_rules = {
            "CAPEX": ("투자", "시설", "증설", "공장", "생산능력", "설비"),
            "CONTRACT": ("공급계약", "수주", "계약", "납품"),
            "CORPORATE_ACTION": ("합병", "분할", "인수", "자회사", "최대주주"),
            "FINANCING": ("유상증자", "사채", "차입", "자금", "대출"),
            "GOVERNANCE": ("대표이사", "임원", "주주총회", "감사", "지배구조"),
        }
        industry_counts = {code: sum(item.get("industry_code") == code for item in items) for code in MANUFACTURING_CATEGORIES}
        company_counts: dict[str, int] = {}
        signals: list[dict] = []
        for item in items:
            company = item.get("corp_name") or "기업명 확인 필요"
            company_counts[company] = company_counts.get(company, 0) + 1
            text = f"{item.get('report_name') or ''} {item.get('remarks') or ''}"
            matched = [code for code, keywords in signal_rules.items() if any(keyword in text for keyword in keywords)]
            score = min(100, 35 + len(matched) * 15 + (15 if item.get("industry_code") in {"AUTOMOTIVE", "SEMICONDUCTOR", "ENERGY"} else 0))
            if matched:
                relevance = item.get("posco_relevance") or {}
                signals.append({"score": score, "signal_types": matched, "industry_code": item.get("industry_code"), "industry_name": item.get("industry_name"), "corp_name": company, "report_name": item.get("report_name"), "remarks": item.get("remarks"), "receipt_no": item.get("receipt_no"), "receipt_date": item.get("receipt_date"), "url": item.get("url"), "relevance_decision": relevance.get("decision"), "relevance_reason_code": relevance.get("reason_code"), "matched_evidence": relevance.get("matched_evidence", []), "reevaluation_required": relevance.get("reevaluation_required", False)})
        signals.sort(key=lambda item: (item["score"], item.get("receipt_date") or ""), reverse=True)
        return {"provider": result.get("provider"), "connected": result.get("connected"), "status": result.get("status"), "period": result.get("period"), "manufacturing_only": True, "posco_relevance_only": True, "summary": {"filtered_disclosures": len(items), "excluded_disclosures": result.get("excluded_count", 0), "raw_disclosures": result.get("raw_total_count", 0), "industry_counts": industry_counts, "top_companies": sorted(({"corp_name": name, "count": count} for name, count in company_counts.items()), key=lambda item: item["count"], reverse=True)[:10], "signal_counts": {code: sum(code in signal.get("signal_types", []) for signal in signals) for code in signal_rules}, "high_priority_signals": len([signal for signal in signals if signal["score"] >= 65])}, "signals": signals[:20], "limitations": ["산업 분류는 공시 주체의 기업명 기준이며 POSCO 철강 수요 연결성이 확인된 공시만 표시합니다.", "자금조달·M&A·IR 등 조건부 문서는 공시 본문에서 생산·설비·프로젝트 근거가 확인되기 전까지 제외됩니다.", "공시는 투자 판단의 단독 근거가 아니며 원문과 추가 기업 조사가 필요합니다."]}

    @staticmethod
    def _normalize(item: dict) -> dict:
        receipt_no = item.get("rcept_no")
        corp_name = str(item.get("corp_name") or "")
        industry_code, industry_name = DartClient._classify_manufacturing(corp_name)
        normalized = {"corp_code": item.get("corp_code"), "corp_name": item.get("corp_name"), "stock_code": item.get("stock_code"), "report_name": item.get("report_nm"), "receipt_no": receipt_no, "receipt_date": item.get("rcept_dt"), "filer_name": item.get("flr_nm"), "remarks": item.get("rm"), "industry_code": industry_code, "industry_name": industry_name, "manufacturing_relevant": bool(industry_code), "url": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={receipt_no}" if receipt_no else None}
        normalized["posco_relevance"] = DartClient._assess_posco_relevance(normalized)
        return normalized

    @staticmethod
    def _classify_manufacturing(corp_name: str) -> tuple[str | None, str | None]:
        text = corp_name.lower()
        for code, (name, keywords) in MANUFACTURING_CATEGORIES.items():
            if any(keyword.lower() in text for keyword in keywords):
                return code, name
        return None, None

    @staticmethod
    def _legacy_industry_candidate(corp_name: str, report_name: str) -> tuple[str | None, str | None]:
        text = f"{corp_name} {report_name}".lower()
        for code, (name, keywords) in MANUFACTURING_CATEGORIES.items():
            if any(keyword.lower() in text for keyword in keywords):
                return code, name
        return None, None

    @staticmethod
    def _filter_relevant_items(items: list[dict], industry: str | None = None) -> tuple[list[dict], list[dict], dict]:
        requested = industry.upper() if industry else None
        audit: list[dict] = []
        for item in items:
            legacy_code, _ = DartClient._legacy_industry_candidate(str(item.get("corp_name") or ""), str(item.get("report_name") or ""))
            candidate_code = item.get("industry_code") or legacy_code
            if candidate_code and (not requested or candidate_code == requested):
                audit.append(item)
        kept = [item for item in audit if item.get("posco_relevance", {}).get("decision") == "KEEP_DATA"]
        excluded = [item for item in audit if item.get("posco_relevance", {}).get("decision") != "KEEP_DATA"]
        metrics = {
            "evaluated_count": len(audit),
            "kept_count": len(kept),
            "excluded_count": len(excluded),
            "non_target_issuer_count": sum(item.get("posco_relevance", {}).get("reason_code") == "NON_TARGET_ISSUER" for item in excluded),
        }
        return kept, audit, metrics

    @staticmethod
    def _compact(value: str) -> str:
        return re.sub(r"[^0-9a-zA-Z가-힣]", "", value).lower()

    @staticmethod
    def _assess_posco_relevance(item: dict) -> dict:
        report = DartClient._compact(str(item.get("report_name") or ""))
        remarks = DartClient._compact(str(item.get("remarks") or ""))
        evidence_text = f"{report} {remarks}"
        if not item.get("industry_code"):
            return {"decision": "EXCLUDE", "reason_code": "NON_TARGET_ISSUER", "matched_evidence": [], "missing_evidence": ["대상 산업 공시 주체"], "reevaluation_required": False, "evidence_source": "OpenDART list.json", "evidence_text": str(item.get("report_name") or ""), "body_fetched": False, "reevaluated_at": None}
        for reason_code, keywords in HARD_EXCLUSION_RULES:
            matched = [keyword for keyword in keywords if DartClient._compact(keyword) in report]
            if matched:
                return {"decision": "EXCLUDE", "reason_code": reason_code, "matched_evidence": matched, "missing_evidence": ["생산·설비·프로젝트 변화"], "reevaluation_required": False, "evidence_source": "OpenDART list.json", "evidence_text": str(item.get("report_name") or ""), "body_fetched": False, "reevaluated_at": None}
        for reason_code, triggers, recovery_terms in CONDITIONAL_RELEVANCE_RULES:
            matched = [keyword for keyword in triggers if DartClient._compact(keyword) in report]
            if matched:
                recovered = [keyword for keyword in recovery_terms if DartClient._compact(keyword) in evidence_text]
                if not recovered:
                    return {"decision": "EXCLUDE", "reason_code": reason_code, "matched_evidence": matched, "missing_evidence": list(recovery_terms), "reevaluation_required": True, "evidence_source": "OpenDART list.json", "evidence_text": str(item.get("report_name") or ""), "body_fetched": False, "reevaluated_at": None}
                return {"decision": "KEEP_DATA", "reason_code": "PHYSICAL_CHANGE_EVIDENCE", "matched_evidence": matched + recovered, "missing_evidence": [], "reevaluation_required": False, "evidence_source": "OpenDART list.json", "evidence_text": f"{item.get('report_name') or ''} {item.get('remarks') or ''}".strip(), "body_fetched": False, "reevaluated_at": None}
        matched = [keyword for keyword in STRONG_RELEVANCE_KEYWORDS if DartClient._compact(keyword) in evidence_text]
        if matched:
            return {"decision": "KEEP_DATA", "reason_code": "STRATEGIC_PHYSICAL_CHANGE", "matched_evidence": matched, "missing_evidence": [], "reevaluation_required": False, "evidence_source": "OpenDART list.json", "evidence_text": f"{item.get('report_name') or ''} {item.get('remarks') or ''}".strip(), "body_fetched": False, "reevaluated_at": None}
        return {"decision": "EXCLUDE", "reason_code": "PHYSICAL_CHANGE_NOT_FOUND", "matched_evidence": [], "missing_evidence": ["생산·프로젝트·설비 변화", "철강 수요 연결 근거"], "reevaluation_required": True, "evidence_source": "OpenDART list.json", "evidence_text": str(item.get("report_name") or ""), "body_fetched": False, "reevaluated_at": None}
