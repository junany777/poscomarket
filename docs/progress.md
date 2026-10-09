# Progress

## 2026-10-09 — OpenDART POSCO Relevance Gate

- 공시 주체 기업명만으로 산업을 분류해 금융상품명에 포함된 제조기업 이름으로 인한 오분류를 제거했다.
- 생산·설비·프로젝트·계약·기술·공급망 변화가 확인된 공시만 공개 Data에 남기는 결정론적 POSCO 연관성 필터를 추가했다.
- 금융상품, 단순 주식보유, 임원 보유, 용도 불명 자금조달, 내용 없는 IR 안내를 제외하고 사유 코드와 재평가 여부를 보존한다.
- 적용처와 제품 지식 근거가 확인된 신호만 POSCO 주요기회로 승격하도록 제한했다.
- `backend/tests/test_dart_relevance.py`의 회귀 테스트 12개와 Python/JavaScript 문법 검사를 통과했다.
- 전체 테스트 실행은 기존 `test_delivery.py`가 존재하지 않는 `priority_for_score`를 import해 수집 단계에서 중단됐다.
- 조건부 공시의 상세 본문 자동 수집은 아직 없으며, 해당 건은 `body_fetched=false`, `reevaluation_required=true`로 공개 분석에서 제외한다.

## 2026-10-05 — Operations / Admin Monitoring

- 기존 CollectionRun, SourceDocument, AIRun, Opportunity, AlertDelivery, Digest, EvaluationRun을 활용한 운영 집계 서비스를 추가했다.
- `/api/v1/admin/*` 요약·상세 API와 `#operations` 관리자 화면을 추가했다.
- 결정론적 시스템 상태, 백로그 경고/임계 상태, 장시간 실행 작업, 제품 지식 공백, 품질 회귀를 표시한다.
- 안전한 SourceDocument 재처리 API는 FAILED/REVIEW_REQUIRED 상태만 허용한다.
- `compileall` 및 `node --check`를 실행했다. 현재 런타임에 pytest 패키지가 없어 pytest는 실행하지 못했다.

## 2026-10-05 — Real-World E2E Validation

- ValidationRun, ValidationRunSource, ValidationStage 모델과 `0011_validation` 마이그레이션을 추가했다.
- 통제 데이터 검증 및 명시적 네트워크 검증을 위한 `app.services.validation.cli`를 추가했다.
- evidence·고아 레코드·중복 감사, 단계별 지표, 품질 게이트, JSON/CSV 리포트를 추가했다.
- `DELIVERY_DRY_RUN`/`VALIDATION_MODE`로 외부 알림 전송을 안전하게 차단한다.
- 실제 네트워크 검증은 외부 소스와 의존성 설치가 필요한 명시적 운영 단계이며 이번 변경에서 자동 실행하지 않았다.

## 2026-10-05 — Performance / Cost Optimization

- ValidationRun 기반 PerformanceBenchmark와 benchmark/compare CLI를 추가했다.
- AIRun cache key, cache hit, 재사용 원본 추적을 추가했다.
- Product Brain 상세 파일에 mtime 기반 안전한 in-process cache와 load 통계를 추가했다.
- 운영 API에 최신 성능 벤치마크를 포함하고, 관리자 화면에 성능 KPI를 추가했다.
- 리스트 API의 기본/최대 페이지 크기를 제한하고 Opportunity의 중복 ProductMatch join을 제거했다.
- 실제 before/after 수치는 validation run과 의존성 설치 후 benchmark 실행 전에는 생성하지 않았다.

## 2026-10-05 — Deployment Readiness

- staging/production 환경 검증, 명시적 CORS/Host 제한, request ID, version metadata를 추가했다.
- PostgreSQL pool 설정과 required knowledge 파일 확인을 추가했다.
- backend non-root 이미지, 정적 frontend Nginx 이미지, production compose와 migration one-shot 서비스를 추가했다.
- scheduler/worker/API/frontend/PostgreSQL 프로세스의 시작 명령과 영속 volume을 문서화했다.
- smoke test, deployment guide, deployment checklist, backup/restore/rollback 런북을 추가했다.
- Docker daemon, backend dependencies, staging DB가 현재 환경에 없어 실제 이미지 빌드·migration·staging smoke는 실행하지 않았다.
