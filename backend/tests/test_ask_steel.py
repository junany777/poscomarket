from app.services.ask_steel.intent import classify


def test_korean_opportunity_intent_and_aliases():
    intent = classify("현대차 최근 Hyper NO Opportunity 보여줘")
    assert intent.intent == "PRODUCT_OPPORTUNITY"
    assert intent.company_names == ["Hyundai Motor"]
    assert intent.product_families == ["HYPER_NO"]
    assert intent.date_from is not None


def test_evidence_and_trend_intents():
    assert classify("근거 기사 보여줘").intent == "EVIDENCE_LOOKUP"
    assert classify("최근 자동차 철강 수요 추세").intent == "TREND_SUMMARY"
