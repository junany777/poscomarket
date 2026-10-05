from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import AIRun, AskQuery
from app.services.ask_steel.intent import AskIntent, classify
from app.services.ask_steel.retrieval import get_opportunity_context, get_evidence_for_opportunities, search_event_clusters, search_opportunities


def _citation(item: dict) -> dict:
    return {"source_document_id": item.get("source_document_id"), "evidence_id": item.get("id"), "title": item.get("title"), "source_name": item.get("source_name"), "source_url": item.get("source_url"), "published_at": item.get("published_at"), "quote_text": item.get("quote_text")}


def _answer(question: str, intent: AskIntent, opportunities: list[dict], events: list[dict], citations: list[dict], context: dict | None = None) -> tuple[str, list[str], list[str]]:
    missing, follow_up = [], []
    lowered = question.lower()
    if any(token in lowered for token in ("ev", "전기차")) and any(token in lowered for token in ("무조건", "always", "자동으로")) and not any(token in lowered for token in ("traction motor", "motor core", "stator", "rotor", "구동 모터", "모터 코어")):
        return "아니요. EV 투자만으로 Hyper NO를 확정할 수 없습니다. 구동·트랙션 모터, 모터 코어, stator/rotor와 전기강판 요구사항이 확인될 때 Hyper NO가 강한 후보가 됩니다.", ["구동 모터 또는 모터 코어 여부", "저손실·자기 특성 등 기술 요구사항"], []
    if not opportunities and not events:
        return "현재 저장된 Intelligence에서는 해당 조건에 맞는 결과를 찾지 못했습니다. 회사명, 제품군 또는 기간 조건을 넓혀 보세요.", ["회사명을 확인해 주세요.", "최근 기간을 넓혀 보세요."], []
    if context:
        opp, event, demand, product, cluster, strategy = context["opportunity"], context["event"], context["demand"], context["product"], context["cluster"], context["strategy"]
        if intent.needs_product_knowledge or intent.intent in {"OPPORTUNITY_EXPLAIN", "PRODUCT_OPPORTUNITY"}:
            product_name = product.product_family if product else None
            answer = f"{opp.title}는 {opp.score:.0f}점 Opportunity입니다.\n\nFACT: {event.summary if event else '저장된 Event가 없습니다.'}\n\nINFERENCE: {(demand.reasoning_summary if demand else '철강 수요 추론이 없습니다.')}"
            if product_name:
                answer += f"\n\nPOSCO 제품군: {product_name}\n제품 매칭 근거: {product.reasoning_summary}"
            else:
                answer += "\n\nPOSCO 제품군은 현재 지식 또는 입력 정보가 부족해 PRODUCT_KNOWLEDGE_PENDING 상태입니다."
            if product and not product.candidate_grades_json:
                answer += "\n정확 Grade는 현재 정보만으로 결정할 수 없습니다. 적용 부품, 두께, 성형·가공 조건과 고객 승인 정보가 필요합니다."
            answer += f"\n\n점수 근거: {opp.score_breakdown_json or {}}"
            return answer, missing, follow_up
    if intent.intent == "TREND_SUMMARY":
        if len(events) < 2:
            return "현재 저장된 사건이 1건 이하라 업계 전체 추세로 일반화하기 어렵습니다. 단일 최근 신호로만 해석해 주세요.", ["추세 판단을 위해 관련 EventCluster가 더 필요합니다."], []
        answer = f"최근 저장된 {len(events)}개 EventCluster에서 반복적으로 관찰되는 신호를 요약합니다.\n\n" + "\n".join(f"- {event['title']} ({event['event_type']})" for event in events[:5])
        return answer, missing, follow_up
    answer = "\n".join([f"{item['score']:.0f}점 · {item['title']} · {item.get('product_family') or '제품군 확인 필요'}" for item in opportunities[:5]])
    return f"조건에 맞는 Opportunity {len(opportunities)}건을 찾았습니다.\n\n{answer}", missing, follow_up


def ask_steel(db: Session, question: str, mode: str = "STANDARD") -> dict:
    if not question or len(question) > settings.ask_max_question_chars:
        raise ValueError(f"question must be between 1 and {settings.ask_max_question_chars} characters")
    intent = classify(question)
    opportunities = search_opportunities(db, intent)
    events = search_event_clusters(db, intent)
    context = get_opportunity_context(db, opportunities[0]["id"]) if intent.intent in {"PRODUCT_OPPORTUNITY", "OPPORTUNITY_EXPLAIN", "EVIDENCE_LOOKUP"} and opportunities else None
    citations = get_evidence_for_opportunities(db, opportunities)
    answer, missing, follow_up = _answer(question, intent, opportunities, events, [_citation(item) for item in citations], context)
    now = datetime.now(timezone.utc).isoformat()
    trace = {"question": question, "intent": intent.intent, "opportunity_ids": [item["id"] for item in opportunities], "event_cluster_ids": [item["id"] for item in events], "evidence_ids": [item["id"] for item in citations], "product_files": [context["product"].product_file] if context and context.get("product") and context["product"].product_file else [], "mode": mode}
    airun = AIRun(run_type="ASK_STEEL_ANSWER", model="deterministic-retrieval", prompt_version="ask-answer-v1", input_reference=question[:180], output_json={"trace": trace, "answer": answer}, status="SUCCESS", started_at=now, completed_at=now)
    db.add(airun); db.flush()
    db.add(AskQuery(question=question, resolved_question=question, intent=intent.intent, answer_text=answer, airun_id=airun.id))
    db.commit()
    return {"answer": answer, "intent": intent.intent, "citations": [_citation(item) for item in citations], "related_opportunities": opportunities, "related_events": events, "product_matches": [{"product_family": context["product"].product_family, "product_file": context["product"].product_file, "reasoning_summary": context["product"].reasoning_summary} for _ in [0] if context and context.get("product")], "missing_information": missing, "follow_up_questions": follow_up, "meta": {"applied_period": "최근 30일" if intent.date_from else None, "retrieval_first": True}}
