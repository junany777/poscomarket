import pytest
from pathlib import Path
import sys

from app.services.dart.client import DartClient

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from knowledge_router import PoscoKnowledgeRouter, enrich_signals  # noqa: E402


def raw_item(corp_name: str, report_name: str, remarks: str = "") -> dict:
    return {
        "corp_code": "00000000",
        "corp_name": corp_name,
        "stock_code": "000000",
        "report_nm": report_name,
        "rcept_no": "20261009000001",
        "rcept_dt": "20261009",
        "flr_nm": corp_name,
        "rm": remarks,
    }


@pytest.mark.parametrize(
    ("corp_name", "report_name", "reason_code"),
    [
        ("삼성전자", "주식등의대량보유상황보고서(일반)", "OWNERSHIP_ONLY"),
        ("유진로봇", "임원ㆍ주요주주특정증권등소유상황보고서", "OWNERSHIP_ONLY"),
        ("한울반도체", "주요사항보고서(유상증자결정)", "FINANCING_PURPOSE_UNKNOWN"),
        ("현대모비스", "기업설명회(IR)개최(안내공시)", "IR_CONTENT_MISSING"),
        ("KCC건설", "중대재해발생", "PHYSICAL_IMPACT_UNKNOWN"),
    ],
)
def test_excludes_disclosures_without_steel_demand_bridge(corp_name, report_name, reason_code):
    normalized = DartClient._normalize(raw_item(corp_name, report_name))

    assert normalized["posco_relevance"]["decision"] == "EXCLUDE"
    assert normalized["posco_relevance"]["reason_code"] == reason_code


def test_industry_classification_uses_issuer_not_financial_product_title():
    normalized = DartClient._normalize(
        raw_item("교보자산운용", "투자설명서(집합투자증권)(삼성전자투게더)")
    )

    assert normalized["industry_code"] is None
    assert normalized["posco_relevance"]["reason_code"] == "NON_TARGET_ISSUER"


def test_keeps_direct_project_contract_and_negative_demand_signal():
    contract = DartClient._normalize(raw_item("동부건설", "단일판매ㆍ공급계약체결"))
    cancellation = DartClient._normalize(raw_item("한화오션", "프로젝트취소 및 생산중단"))

    assert contract["posco_relevance"]["decision"] == "KEEP_DATA"
    assert cancellation["posco_relevance"]["decision"] == "KEEP_DATA"


def test_conditionally_keeps_financing_when_facility_purpose_is_present():
    normalized = DartClient._normalize(
        raw_item("한울반도체", "주요사항보고서(유상증자결정)", "신규 생산라인 시설자금")
    )

    assert normalized["posco_relevance"]["decision"] == "KEEP_DATA"
    assert normalized["posco_relevance"]["reason_code"] == "PHYSICAL_CHANGE_EVIDENCE"


def test_analysis_uses_only_relevance_filtered_items():
    kept = DartClient._normalize(raw_item("동부건설", "단일판매ㆍ공급계약체결"))
    result = {
        "provider": "OpenDART",
        "connected": True,
        "status": "CONNECTED",
        "raw_total_count": 14,
        "excluded_count": 13,
        "items": [kept],
    }

    analysis = DartClient._build_analysis(result)

    assert analysis["summary"]["filtered_disclosures"] == 1
    assert analysis["summary"]["excluded_disclosures"] == 13
    assert len(analysis["signals"]) == 1
    assert analysis["signals"][0]["corp_name"] == "동부건설"
    assert analysis["signals"][0]["relevance_reason_code"] == "STRATEGIC_PHYSICAL_CHANGE"


def test_fourteen_item_regression_keeps_one_and_audits_thirteen():
    samples = [
        ("삼성전자", "주식등의대량보유상황보고서(일반)"),
        ("KCC건설", "중대재해발생"),
        ("한울반도체", "소액공모공시서류(지분증권)"),
        ("한울반도체", "주요사항보고서(유상증자결정)"),
        ("동진건설", "소액공모공시서류(지분증권)"),
        ("동부건설", "단일판매ㆍ공급계약체결"),
        ("태영건설", "유상증자또는주식관련사채등의발행결과(자율공시)"),
        ("한화오션", "타법인주식및출자증권취득결정"),
        ("한화오션", "유상증자결정"),
        ("LSK아이로봇", "주식등의대량보유상황보고서(일반)"),
        ("교보자산운용", "투자설명서(집합투자증권)(삼성전자투게더)"),
        ("교보자산운용", "투자설명서(집합투자증권)(삼성전자투게더30)"),
        ("유진로봇", "임원ㆍ주요주주특정증권등소유상황보고서"),
        ("현대모비스", "기업설명회(IR)개최(안내공시)"),
    ]
    normalized = [DartClient._normalize(raw_item(company, report)) for company, report in samples]

    kept, audit, metrics = DartClient._filter_relevant_items(normalized)

    assert metrics == {"evaluated_count": 14, "kept_count": 1, "excluded_count": 13, "non_target_issuer_count": 2}
    assert kept[0]["corp_name"] == "동부건설"
    assert len(audit) == 14
    assert all(item["posco_relevance"].get("reason_code") for item in audit)


def test_unknown_application_does_not_expose_product_candidate():
    router = PoscoKnowledgeRouter(ROOT)
    route = router.route({"industry_code": "CONSTRUCTION", "corp_name": "태양광건설", "report_name": "단일판매ㆍ공급계약체결", "signal_types": ["CONTRACT"]})

    assert route["application_code"] == "UNKNOWN"
    assert route["product_candidates"] == []
    assert route["product_fit"] == 0


def test_priority_summary_uses_verified_knowledge_match():
    analysis = {"summary": {"high_priority_signals": 1}, "signals": [{"industry_code": "CONSTRUCTION", "corp_name": "동부건설", "report_name": "단일판매ㆍ공급계약체결", "signal_types": ["CONTRACT"]}]}

    enrich_signals(analysis, ROOT)

    assert analysis["signals"][0]["priority_eligible"] is False
    assert analysis["summary"]["high_priority_signals"] == 0
    assert analysis["summary"]["high_signal_score_count"] == 1
