# Progress

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
