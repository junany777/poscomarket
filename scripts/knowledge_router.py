"""Route DART change signals through the POSCO knowledge index.

This module deliberately uses the master router as the source of truth.  A
signal may be important without being specific enough to recommend a product;
in that case the route is kept explicit and marked as requiring application
conditions instead of guessing a grade or product family.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


class PoscoKnowledgeRouter:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.index_path = root / "knowledge" / "posco" / "index.md"
        self.registry = self._load_registry()

    def _load_registry(self) -> dict[str, dict[str, str]]:
        registry: dict[str, dict[str, str]] = {}
        if not self.index_path.exists():
            return registry
        pattern = re.compile(r"^\|\s*([A-Z0-9_]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|", re.MULTILINE)
        for code, name, category, relative_file in pattern.findall(self.index_path.read_text(encoding="utf-8")):
            path = self.root / "knowledge" / "posco" / relative_file
            registry[code] = {
                "product_family": code,
                "name": name.strip(),
                "category": category.strip(),
                "knowledge_file": relative_file,
                "available": path.exists(),
            }
        return registry

    def _candidate(self, code: str, reason: str, confidence: int, priority: str = "PRIMARY") -> dict[str, Any]:
        item = self.registry.get(code)
        if not item:
            return {"product_family": code, "knowledge_file": None, "available": False, "priority": priority, "confidence": confidence, "reason": reason}
        return {**item, "priority": priority, "confidence": confidence, "reason": reason}

    @staticmethod
    def _text(signal: dict[str, Any]) -> str:
        return " ".join(str(signal.get(key) or "") for key in ("corp_name", "report_name", "remarks", "evidence_text")).lower()

    def route(self, signal: dict[str, Any]) -> dict[str, Any]:
        industry = str(signal.get("industry_code") or "")
        text = self._text(signal)
        signal_types = signal.get("signal_types") or []
        candidates: list[dict[str, Any]] = []
        application = "UNKNOWN"
        component = "UNKNOWN"
        requirements = ["공시 원문에서 적용처·부품·사양 확인"]
        demand = "산업별 철강 수요 확인 필요"
        status = "APPLICATION_CONDITION_REQUIRED"

        if industry == "AUTOMOTIVE":
            demand = "자동차 차체·구조 및 구동 부품용 강재"
            if any(word in text for word in ("전기차", "ev", "모터", "구동", "모터코어")):
                application, component = "EV_MOTOR", "구동 모터·모터코어"
                requirements = ["저철손", "전기적 효율", "모터 적용 조건"]
                candidates = [self._candidate("HYPER_NO", "applications.md의 EV_MOTOR → HYPER_NO 라우팅", 90)]
                status = "KNOWLEDGE_MATCH"
            elif any(word in text for word in ("배터리", "차체", "바디", "섀시", "샤시")):
                application, component = "EV_BODY_STRUCTURE", "차체·구조 부품"
                requirements = ["고강도", "성형성", "용접성"]
                candidates = [self._candidate("AUTOMOTIVE_STEEL", "POSCO index의 자동차 차체·구조용 후보", 82), self._candidate("ATOS", "POSCO index의 자동차 구조용 후보", 78, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("AUTOMOTIVE_STEEL", "자동차 산업 후보. 적용 부품 확인 후 세부 라우팅", 55), self._candidate("ATOS", "자동차 구조용 후보. 적용 부품 확인 후 세부 라우팅", 50, "ALTERNATIVE")]

        elif industry == "SHIPBUILDING":
            demand = "선박·해양 구조용 강재"
            if any(word in text for word in ("lng", "액화천연가스", "저온", "극저온")):
                application, component = "LNG_TANK", "LNG 탱크·저온 구조"
                requirements = ["저온 인성", "용접성", "저온 운전"]
                candidates = [self._candidate("CRYOGENIC_PLATE", "applications.md의 LNG_TANK 적용처 후보", 88)]
                status = "KNOWLEDGE_MATCH"
            elif any(word in text for word in ("해양", "offshore", "해상풍력")):
                application, component = "OFFSHORE_STRUCTURE", "해양 구조물"
                requirements = ["후판 구조 강도", "용접성", "해양 환경 내구성"]
                candidates = [self._candidate("OFFSHORE_PLATE", "applications.md의 해양 구조 적용처 후보", 86)]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("SHIPBUILDING_PLATE", "POSCO index의 조선 산업 후보. 선종·부품 확인 필요", 62)]

        elif industry == "ENERGY":
            demand = "에너지 인프라·발전·배관 설비용 강재"
            if any(word in text for word in ("풍력", "해상풍력", "offshore")):
                application, component = "OFFSHORE_WIND", "풍력 타워·해양 구조"
                requirements = ["후판 구조 강도", "해양 환경 내구성", "용접성"]
                candidates = [self._candidate("OFFSHORE_PLATE", "applications.md의 OFFSHORE_WIND 후보", 88), self._candidate("CONSTRUCTION_PLATE", "applications.md의 OFFSHORE_WIND 대체 후보", 68, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            elif any(word in text for word in ("수소", "가스", "배관", "파이프", "pipeline")):
                application, component = "HYDROGEN_PIPELINE", "배관·라인파이프"
                requirements = ["압력·인성", "수소 환경 적합성", "용접성"]
                candidates = [self._candidate("LINE_PIPE_PLATE", "applications.md의 배관·파이프 적용처 후보", 84), self._candidate("API_STEEL", "POSCO index의 에너지 배관 후보", 78, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            elif any(word in text for word in ("발전", "전력", "보일러", "압력")):
                application, component = "POWER_PLANT", "발전·압력 설비"
                requirements = ["압력용기 성능", "고온 운전", "용접성"]
                candidates = [self._candidate("PRESSURE_VESSEL_PLATE", "applications.md의 발전·압력 설비 후보", 82), self._candidate("ANCOR", "에너지용 특수 환경 후보. 부식 조건 확인 필요", 62, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("API_STEEL", "에너지 산업 후보. 배관·발전·풍력 적용처 확인 필요", 45), self._candidate("OFFSHORE_PLATE", "에너지 산업 후보. 해양·풍력 여부 확인 필요", 42, "ALTERNATIVE")]

        elif industry == "CONSTRUCTION":
            demand = "건축·토목·플랜트 구조 및 외장용 강재"
            if any(word in text for word in ("태양광", "solar")):
                application, component = "SOLAR_STRUCTURE", "태양광 구조물"
                requirements = ["내식성", "외부 환경 내구성", "가공성"]
                candidates = [self._candidate("GALVANIZED_STEEL", "applications.md의 SOLAR_STRUCTURE 후보", 86), self._candidate("POSMAC_3_0", "applications.md의 SOLAR_STRUCTURE 내식 후보", 82, "ALTERNATIVE"), self._candidate("POSMAC_SUPER", "applications.md의 고내식 대안 후보", 76, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("CONSTRUCTION_PLATE", "POSCO index의 건설 산업 후보. 구조·외장 적용처 확인 필요", 55), self._candidate("GALVANIZED_STEEL", "건설 외장·내식 적용 가능성 확인 필요", 48, "ALTERNATIVE")]

        elif industry == "MACHINERY":
            demand = "산업기계·중장비·로봇 구조 및 내마모용 강재"
            if any(word in text for word in ("굴삭", "버킷", "마모", "wear")):
                application, component = "EXCAVATOR_BUCKET", "굴삭기 버킷·마모 부품"
                requirements = ["내마모성", "충격 인성", "가공성"]
                candidates = [self._candidate("POS_AR", "applications.md의 EXCAVATOR_BUCKET → POS_AR 후보", 88)]
                status = "KNOWLEDGE_MATCH"
            elif any(word in text for word in ("크레인", "붐", "중장비", "구조")):
                application, component = "HEAVY_EQUIPMENT", "중장비 구조 부품"
                requirements = ["고강도", "피로 강도", "용접성"]
                candidates = [self._candidate("POS_TEN", "applications.md의 중장비·붐 구조 후보", 84)]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("POS_TEN", "기계 산업 구조용 후보. 부품·하중 확인 필요", 48), self._candidate("POS_AR", "기계 산업 내마모 후보. 마모 부품 여부 확인 필요", 45, "ALTERNATIVE")]

        elif industry == "HOME_APPLIANCE":
            demand = "가전 외판·내판 및 기능성 강재"
            if any(word in text for word in ("냉장고", "세탁기", "에어컨", "hvac", "외판")):
                application, component = "HOME_APPLIANCE_BODY", "가전 외판·내판"
                requirements = ["표면 품질", "성형성", "도금·도장성"]
                candidates = [self._candidate("ELECTRO_GALVANIZED_STEEL", "가전 외판·표면 품질 후보", 78), self._candidate("COLD_ROLLED_STEEL", "가전 성형용 기본 소재 후보", 72, "ALTERNATIVE"), self._candidate("POSMAC_1_5", "내식 요구가 있는 외장 대안 후보", 60, "ALTERNATIVE")]
                status = "KNOWLEDGE_MATCH"
            else:
                candidates = [self._candidate("COLD_ROLLED_STEEL", "가전 산업 후보. 제품·부품 확인 필요", 45), self._candidate("ELECTRO_GALVANIZED_STEEL", "가전 표면·내식 후보. 제품·부품 확인 필요", 42, "ALTERNATIVE")]

        elif industry == "SEMICONDUCTOR":
            demand = "반도체 팹·장비·클린룸 투자 관련 강재 수요"
            if any(word in text for word in ("팹", "fab", "클린룸", "장비", "웨이퍼")):
                application, component = "SEMICONDUCTOR_FAB", "팹·클린룸·장비 구조"
                requirements = ["청정도", "내식성", "표면·구조 요구사항"]
            # The current POSCO router does not expose a semiconductor product
            # family. Keep this as a knowledge gap instead of guessing.
            status = "PRODUCT_FAMILY_UNKNOWN"

        available = [item for item in candidates if item.get("available")]
        unavailable = [item["product_family"] for item in candidates if not item.get("available")]
        if candidates and not available:
            status = "DETAIL_SOURCE_PENDING"
        route_reason = f"{application} / {component} / {', '.join(requirements)}"
        signal_names = {
            "CAPEX": "투자·증설",
            "CONTRACT": "계약·수주",
            "CORPORATE_ACTION": "기업행위",
            "FINANCING": "자금조달",
            "GOVERNANCE": "지배구조",
        }
        signal_label = "·".join(signal_names.get(code, code) for code in signal_types) or "변화 신호 확인 필요"
        strategy_views = {
            "CAPEX": "투자·증설이 실제 생산능력 확대와 소재 수요로 전환되는지 확인",
            "CONTRACT": "계약·수주가 신규 프로젝트와 공급망 진입 기회로 이어지는지 확인",
            "CORPORATE_ACTION": "기업행위가 사업 포트폴리오와 고객 전략 변화로 이어지는지 확인",
            "FINANCING": "자금조달 목적이 성장 투자·재무 보완 중 어디에 해당하는지 구분",
            "GOVERNANCE": "지배구조 변화가 의사결정과 사업 방향에 미치는 영향을 확인",
        }
        strategy_statement = " / ".join(strategy_views.get(code, "공시 원문에서 전략적 의미를 추가 확인") for code in signal_types)
        return {
            "status": status,
            "application_code": application,
            "component": component,
            "material_requirements": requirements,
            "steel_demand": demand,
            "product_candidates": available[:3],
            "unavailable_product_families": unavailable,
            "route_reason": route_reason,
            "signal_label": signal_label,
            "strategy_statement": strategy_statement,
            "router_source": "knowledge/posco/index.md + knowledge/taxonomy/applications.md",
            "product_fit": max((int(item["confidence"]) for item in available), default=0),
            "role_insights": {
                "executive": f"{demand} 변화가 실제 투자·수주로 이어지는지 확인하고, {application} 적용처 확정 여부를 점검",
                "marketing": f"고객의 {component} 투자 일정과 소재 승인·납품 접점을 확인",
                "engineering": f"{', '.join(requirements)}를 공시 원문·사양서로 검증한 뒤 제품 후보를 확정",
            },
        }


def enrich_signals(analysis: dict[str, Any], root: Path) -> dict[str, Any]:
    router = PoscoKnowledgeRouter(root)
    signals = analysis.get("signals") or []
    for signal in signals:
        signal["knowledge_route"] = router.route(signal)
    analysis["knowledge_router"] = {
        "source": "knowledge/posco/index.md",
        "taxonomy": "knowledge/taxonomy/applications.md",
        "max_product_files": 3,
        "available_product_families": sum(1 for item in router.registry.values() if item.get("available")),
        "registered_product_families": len(router.registry),
    }
    return analysis
