from datetime import datetime, timedelta, timezone

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

    async def disclosures(self, bgn_de: str | None = None, end_de: str | None = None, corp_code: str | None = None, industry: str | None = None, page_no: int = 1, page_count: int = 20) -> dict:
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
                if len([item for item in items if item["industry_code"]]) >= 30:
                    break
                next_payload = await self._request({**params, "page_no": next_page})
                if str(next_payload.get("status", "")) not in {"000", "013"}:
                    break
                items.extend(self._normalize(item) for item in (next_payload.get("list") or []))
            items = [item for item in items if item["industry_code"] and (not industry or item["industry_code"] == industry.upper())]
            return {"provider": "OpenDART", "configured": True, "connected": connected, "status": "CONNECTED" if connected else "API_ERROR", "message": "제조업 관련 공시가 없습니다." if not items and connected else ("OpenDART 공시를 조회했습니다." if connected else str(payload.get("message", "OpenDART 응답 오류"))), "items": items, "total_count": len(items), "raw_total_count": raw_total_count, "page_no": int(payload.get("page_no") or page_no), "page_count": page_count, "manufacturing_only": True, "industries": [{"code": code, "name_ko": name} for code, (name, _) in MANUFACTURING_CATEGORIES.items()], "period": {"bgn_de": bgn_de, "end_de": end_de}}
        except (httpx.HTTPError, ValueError) as exc:
            return {"provider": "OpenDART", "configured": True, "connected": False, "status": "NETWORK_ERROR", "message": f"OpenDART 연결 실패: {type(exc).__name__}", "items": [], "total_count": 0, "page_no": page_no, "page_count": page_count}

    async def analysis(self, bgn_de: str | None = None, end_de: str | None = None) -> dict:
        result = await self.disclosures(bgn_de=bgn_de, end_de=end_de, page_count=100)
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
                signals.append({"score": score, "signal_types": matched, "industry_code": item.get("industry_code"), "industry_name": item.get("industry_name"), "corp_name": company, "report_name": item.get("report_name"), "remarks": item.get("remarks"), "receipt_date": item.get("receipt_date"), "url": item.get("url")})
        signals.sort(key=lambda item: (item["score"], item.get("receipt_date") or ""), reverse=True)
        return {"provider": result.get("provider"), "connected": result.get("connected"), "status": result.get("status"), "period": result.get("period"), "manufacturing_only": True, "summary": {"filtered_disclosures": len(items), "raw_disclosures": result.get("raw_total_count", 0), "industry_counts": industry_counts, "top_companies": sorted(({"corp_name": name, "count": count} for name, count in company_counts.items()), key=lambda item: item["count"], reverse=True)[:10], "signal_counts": {code: sum(code in signal.get("signal_types", []) for signal in signals) for code in signal_rules}, "high_priority_signals": len([signal for signal in signals if signal["score"] >= 65])}, "signals": signals[:20], "limitations": ["산업 분류는 기업명·공시명 키워드 기반의 보수적 분류입니다.", "공시는 투자 판단의 단독 근거가 아니며 원문과 추가 기업 조사가 필요합니다."]}

    @staticmethod
    def _normalize(item: dict) -> dict:
        receipt_no = item.get("rcept_no")
        corp_name = str(item.get("corp_name") or "")
        report_name = str(item.get("report_nm") or "")
        industry_code, industry_name = DartClient._classify_manufacturing(corp_name, report_name)
        return {"corp_code": item.get("corp_code"), "corp_name": item.get("corp_name"), "stock_code": item.get("stock_code"), "report_name": item.get("report_nm"), "receipt_no": receipt_no, "receipt_date": item.get("rcept_dt"), "filer_name": item.get("flr_nm"), "remarks": item.get("rm"), "industry_code": industry_code, "industry_name": industry_name, "manufacturing_relevant": bool(industry_code), "url": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={receipt_no}" if receipt_no else None}

    @staticmethod
    def _classify_manufacturing(corp_name: str, report_name: str) -> tuple[str | None, str | None]:
        text = f"{corp_name} {report_name}".lower()
        for code, (name, keywords) in MANUFACTURING_CATEGORIES.items():
            if any(keyword.lower() in text for keyword in keywords):
                return code, name
        return None, None
