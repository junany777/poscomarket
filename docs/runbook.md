# 운영 런북

## Collector failure

1. `/api/v1/admin/collection`에서 실패 소스와 `CollectionRun.error_summary`를 확인합니다.
2. 소스 레지스트리의 enabled/type/URL을 확인합니다.
3. 기존 collector 실행 API를 수동 실행합니다.
4. 반복 실패 시 해당 소스를 비활성화하고 운영 모니터링에 기록합니다.

## Pipeline failure

1. `/api/v1/admin/pipeline`에서 backlog age와 failure stage를 확인합니다.
2. `FAILED` 또는 `REVIEW_REQUIRED` SourceDocument만 `POST /api/v1/admin/sources/{id}/reprocess`로 재처리합니다.
3. evidence와 중간 산출물을 확인하고 원인별로 수정 후 새 validation run을 생성합니다.

## AI failure

1. `/api/v1/admin/ai-runs`에서 run type, model, error를 확인합니다.
2. 실패율과 지연이 회복될 때까지 validation은 dry-run으로 유지합니다.
3. 실패 레코드를 삭제하거나 결과를 수동으로 성공 처리하지 않습니다.

## Delivery failure

1. `/api/v1/admin/delivery`에서 `FAILED`, `RETRY_PENDING`, oldest pending을 확인합니다.
2. 원인 수정 후 기존 `POST /api/v1/deliveries/{id}/retry`를 사용합니다.
3. validation에서는 `DELIVERY_DRY_RUN=true`를 유지합니다.

## Digest failure

1. `/api/v1/admin/digest`에서 digest 상태와 전송 상태를 확인합니다.
2. 기존 `POST /api/v1/digests/{id}/regenerate`를 사용합니다.
3. 근거가 부족한 요약은 `EARLY_SIGNAL`로 유지합니다.

## Knowledge pending

`/api/v1/admin/knowledge-gaps`의 빈도·고점수 차단·최근성 순위를 검토합니다. 기준선 검증 중에는 개별 사례를 통과시키기 위해 Product Brain 파일을 추가하지 않습니다.

## Quality regression

1. `/api/v1/admin/quality`에서 baseline delta와 critical error를 확인합니다.
2. evidence fabrication, grade hallucination, forbidden product route, false merge를 우선 조사합니다.
3. 프롬프트 자동 롤백은 수행하지 않고 baseline을 보존한 뒤 수정 후 새 validation run을 생성합니다.

## Deploy

1. 최신 Evaluation, E2E, Performance benchmark gate를 확인합니다.
2. PostgreSQL 백업을 외부 저장소에 생성합니다.
3. `alembic current`와 `alembic heads`를 확인합니다.
4. staging에서 `alembic upgrade head` 후 smoke test를 실행합니다.
5. migration 성공 후에만 새 backend image와 worker/scheduler를 시작합니다.

## Rollback

애플리케이션은 이전 이미지로 되돌릴 수 있지만, migration은 자동 `downgrade`하지 않습니다. schema가 이전 앱과 호환되는지 확인하고, 비호환이면 백업 복구 계획을 적용합니다.

## Database restore

빈 staging DB를 만들고 외부 `pg_dump` 백업을 `pg_restore`한 뒤 `alembic current`, health, admin health, smoke test와 데이터 무결성 검사를 순서대로 실행합니다. 복구 파일·소요 시간·결과를 기록합니다.

## Scheduler / worker outage

News Scheduler와 Digest Scheduler는 각각 한 인스턴스만 유지합니다. Delivery Worker가 중단되면 PENDING/RETRY_PENDING backlog와 oldest age를 확인한 뒤 재시작합니다. 운영 화면이 stale 상태를 표시하지 않는 경우 배포를 중지합니다.
