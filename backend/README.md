# Steel Market Intelligence Backend MVP

## Run locally

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
# 환경변수 파일을 함께 로드하려면:
uvicorn app.main:app --reload --env-file .env
```

## Docker Compose

```powershell
docker compose up --build
```

The default local database is SQLite. Set `DATABASE_URL` to PostgreSQL for the deployment environment. The OpenAI key is optional for this deterministic vertical slice and is reserved for the structured-output adapters.

## Migrations and tests

```powershell
alembic upgrade head
pytest
```

The deterministic fixture traces:

`Source → CAPACITY_EXPANSION → ELECTRIFICATION → EV_MOTOR → MOTOR_CORE → NON_ORIENTED_ELECTRICAL_STEEL → HYPER_NO → Opportunity`

## Endpoints

- `GET /health`
- `POST /api/v1/sources`
- `GET /api/v1/sources/{source_id}`
- `POST /api/v1/intelligence/run/{source_id}`
- `GET /api/v1/opportunities`
- `GET /api/v1/opportunities/{opportunity_id}`

## OpenDART 공시 연결

OpenDART 인증키는 `backend/.env`의 `DART_API_KEY`로만 관리합니다. 키를 프론트엔드나 API 응답에 전달하지 않습니다.

- 연결 상태: `GET /api/v1/dart/health`
- 최근 제조업 공시 조회: `GET /api/v1/dart/disclosures?page_count=100`
- 공시 분석: `GET /api/v1/dart/analysis`
- 산업별 공시 조회: `GET /api/v1/dart/disclosures?industry=AUTOMOTIVE`
- 기간 조회: `GET /api/v1/dart/disclosures?bgn_de=20261001&end_de=20261005`

공시는 자동차, 조선, 건설, 에너지, 가전, 기계, 반도체 키워드 분류를 통과한 항목만 반환합니다. 분류는 OpenDART 목록 응답의 기업명·공시명에 기반한 보수적 라우팅이며, 산업 코드가 확인되지 않는 공시는 화면에서 제외합니다.

서버 실행 시 반드시 `.env`를 로드하세요.

```powershell
uvicorn app.main:app --reload --env-file .env
```

Opportunity detail returns source, exact evidence quotes, event, strategies, steel-demand hypothesis, product match, score breakdown, and recommended actions.

## News Collector and Event Clustering

수집기는 `backend/config/news_sources.yaml` 레지스트리의 RSS/Atom/HTML_INDEX 소스만 처리합니다. 기본 소스는 검증 전 비활성화되어 있습니다.

- 수집: `POST /api/v1/collectors/run`
- 실행 이력: `GET /api/v1/collectors/runs`
- Event Cluster: `GET /api/v1/event-clusters`, `GET /api/v1/event-clusters/{id}`
- 수동 병합: `POST /api/v1/event-clusters/merge`
- 기존 Event 백필: `python -m app.services.intelligence.event_clustering.backfill`
- 자동 임계값 85, 검토 구간 70–84, 후보 최대 20건, 최근 30일 탐색

## Alert Delivery

Alert 생성과 외부 전송은 분리되어 있습니다. 활성 Watchlist 구독이 있으면 `AlertDelivery`가 `PENDING`으로 생성되고, worker가 Telegram adapter를 통해 처리합니다.

- 채널: `POST/GET/PATCH/DELETE /api/v1/delivery-channels`
- 연결 테스트: `POST /api/v1/delivery-channels/{id}/test`
- 구독: `POST/GET/PATCH/DELETE /api/v1/delivery-subscriptions`
- 처리: `POST /api/v1/deliveries/process` (본문 `{"limit":20,"dry_run":true}`)
- 이력: `GET /api/v1/deliveries`, `GET /api/v1/deliveries/{id}`
- 재시도: `POST /api/v1/deliveries/{id}/retry`
- worker: `python -m app.services.delivery.worker`
- 기존 Alert enqueue: `python -m app.services.delivery.cli enqueue-existing`

Telegram bot token은 `TELEGRAM_BOT_TOKEN` 환경변수로만 관리하며 API 응답에 포함하지 않습니다. 정상 발송은 `DELIVERED`, 네트워크/429/5xx는 제한된 횟수만 `RETRY_PENDING`, 400/401/403 등은 `FAILED`로 종료합니다.

## Daily / Weekly Intelligence Digest

다이제스트는 저장된 EventCluster, Opportunity, HIGH Alert, 산업·제품 분포와 Evidence를 기간별로 집계합니다. 동일한 유형·기간은 재생성하지 않는 idempotency 규칙을 사용하며, 근거가 부족한 경우 `EARLY_SIGNAL`로 표시합니다.

- 생성: `POST /api/v1/digests/generate` (본문 `{"digest_type":"DAILY"}` 또는 `WEEKLY`)
- 조회: `GET /api/v1/digests`, `GET /api/v1/digests/{id}`
- Telegram 다이제스트 구독: `POST/GET/PATCH/DELETE /api/v1/digest-subscriptions`
- 알림·다이제스트 처리: `POST /api/v1/deliveries/process`
- 수동 실행: `python -m app.services.digest.cli --type daily`
- 스케줄러: `DIGEST_SCHEDULER_ENABLED=true python -m app.services.digest.scheduler`

기본 스케줄은 한국시간 매일 08:00, 매주 월요일 08:00이며 `DIGEST_*` 환경변수로 조정합니다. Telegram 자격증명은 기존과 동일하게 `TELEGRAM_BOT_TOKEN` 환경변수로만 관리합니다.

## Operations / Admin Monitoring

운영 모니터링은 기존 도메인 테이블을 실시간 집계하며 별도 관측 인프라를 추가하지 않습니다.

- 화면: `#operations` (운영 모니터링)
- 요약: `GET /api/v1/admin/overview?period=24h|7d|30d`
- 상태: `GET /api/v1/admin/health`
- 수집: `GET /api/v1/admin/collection`
- 파이프라인: `GET /api/v1/admin/pipeline`
- AI 실행: `GET /api/v1/admin/ai-runs`
- 제품 지식 공백: `GET /api/v1/admin/knowledge-gaps`
- 전송·다이제스트·품질: `GET /api/v1/admin/delivery`, `GET /api/v1/admin/digest`, `GET /api/v1/admin/quality`
- 안전한 재처리: `POST /api/v1/admin/sources/{id}/reprocess` (FAILED/REVIEW_REQUIRED만 허용)

전체 상태는 DATABASE, NEWS_COLLECTOR, INTELLIGENCE_PIPELINE, OPENAI, ALERT_DELIVERY, DIGEST, EVALUATION의 결정론적 상태를 합성합니다. 임계값은 `OPS_*` 환경변수로 조정하며, 운영 화면은 AI가 상태를 판정하지 않습니다.

## Real-World E2E Validation

검증은 일반 CI와 분리된 명시적 명령으로 실행합니다. 실데이터 수집은 `run-real`에서만 수행하며, 기본적으로 외부 전송은 dry-run입니다.

```powershell
python -m app.services.validation.cli run-real --source-limit 100 --delivery-dry-run
python -m app.services.validation.cli report --run RUN_ID
python -m app.services.validation.cli quality-gate --run RUN_ID
```

통제된 기존 데이터 검증은 다음처럼 실행합니다.

```powershell
python -m app.services.validation.cli run --source-limit 50
```

검증 실행은 SourceDocument ID, 단계별 입력·성공·실패·소요시간, evidence 무결성, 고아 레코드, 중복, 운영 상태를 보존합니다. 기준선 검증 중 제품 지식 파일을 자동으로 추가하지 않습니다.

## Performance / Cost Benchmark

성능 수치는 실제 ValidationRun에 대해서만 기록합니다. 가격표가 설정되지 않은 경우 비용 대신 호출 수·입출력 토큰만 보고합니다.

```powershell
python -m app.services.performance.cli benchmark --validation-run VALIDATION_RUN_ID
python -m app.services.performance.cli compare --baseline BASELINE_BENCHMARK_ID --candidate CANDIDATE_BENCHMARK_ID
```

AIRun은 SourceDocument content hash·pipeline/prompt/rule 버전 조합으로 안전하게 재사용하며, cache hit와 원본 AIRun ID를 보존합니다. Product Brain 상세 파일은 mtime 기반 in-process cache를 사용하고 변경 시 무효화합니다.

## Prompt / Rule Tuning

- 활성 프롬프트는 `app/prompts/registry.yaml`에서 단일 버전으로 해석합니다.
- 결정론적 중요 규칙은 `app/rules/registry.yaml`에서 버전 관리합니다.
- baseline 실행: `python -m app.services.evaluation.cli run --dataset mvp-v1`
- 부분 평가: `python -m app.services.evaluation.cli run --dataset mvp-v1 --subset DIRECT_POSITIVE`
- 실행 비교: `python -m app.services.evaluation.cli compare --baseline RUN_ID --candidate RUN_ID --target-metric strategy_precision`
- 품질 게이트: `python -m app.services.evaluation.cli quality-gate --run RUN_ID`
- 튜닝 후보는 자동으로 프롬프트를 수정하지 않으며, API와 DB에 제안·상태·결정 이력을 남깁니다.

## Example source

```json
{
  "source_type": "NEWS",
  "source_name": "TEST_SOURCE",
  "source_url": "https://example.com/article",
  "title": "Automaker expands EV traction motor production capacity",
  "published_at": "2026-10-01T00:00:00Z",
  "content": "The automaker announced an expansion of EV traction motor production capacity in North America."
}
```
# News Collector

뉴스 수집기는 `backend/config/news_sources.yaml`의 선언형 레지스트리만 읽습니다. 기본 예시는 `enabled: false`이므로 URL·선택자 검증 후 개별 소스를 활성화해야 합니다.

- 지원 수집기: `RSS`, `ATOM`, `HTML_INDEX`
- 흐름: fetch → parse → normalize → relevance filter → deduplicate → `SourceDocument`
- 실행: `POST /api/v1/collectors/run` (본문 예: `{"source_codes":["POSCO_NEWSROOM"],"dry_run":true}`)
- 소스/실행 이력: `GET /api/v1/collectors/sources`, `GET /api/v1/collectors/runs`
- 자동 지능화는 `AUTO_RUN_INTELLIGENCE=false`가 기본이며, 수집기 내부에서 LLM을 직접 호출하지 않습니다.
- 스케줄러는 `NEWS_SCHEDULER_ENABLED=false`가 기본이고 별도 프로세스로 운영합니다. 테스트는 외부 네트워크를 사용하지 않습니다.

### 국내 제조업·철강 뉴스 출처

`backend/config/news_sources.yaml`에 다음 출처를 등록했습니다.

- 네이버 뉴스 철강·제조업 검색 결과
- 페로타임즈
- 철강금속신문
- 스틸데일리
- 스틸웨어(SteelWhere)
- 스틸인포시스
- 한국철강협회

수집기는 공개 RSS 또는 공개 뉴스 목록의 제목·요약·원문 링크를 수집하고, 철강·제조업 키워드 관련성 필터와 content hash 중복 제거를 적용합니다. 각 매체의 이용약관·로봇 정책·콘텐츠 이용범위를 확인한 뒤 운영 환경에서 호출 빈도와 저장 범위를 조정해야 합니다.

수동 수집:

```powershell
Invoke-RestMethod -Uri http://localhost:8000/api/v1/collectors/run `
  -Method Post -ContentType 'application/json' `
  -Body '{"source_codes":["NAVER_NEWS_STEEL_MANUFACTURING","FERROTIMES","SNM_NEWS","STEELDAILY","STEELWHERE","STEELINFOSYS","KOSA_NEWS"],"dry_run":false}'
```

출처를 지정하지 않은 수집 요청은 OpenDART만 실행합니다. 네이버·전문 매체를 함께 수집하려면 `source_codes`에 원하는 코드만 추가합니다. 대시보드의 `수집 출처` 화면에서도 같은 선택을 할 수 있습니다.
