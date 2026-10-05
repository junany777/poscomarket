# Deployment Guide

## 지원 프로세스

배포는 다음 프로세스를 분리합니다.

- `frontend`: 정적 HTML을 Nginx로 제공하며 `/api`를 backend로 프록시
- `backend`: FastAPI API
- `migrate`: `alembic upgrade head`를 한 번 실행하는 일회성 프로세스
- `news-scheduler`: `python -m app.services.ingestion.scheduler`
- `delivery-worker`: `python -m app.services.delivery.worker`
- `digest-scheduler`: `python -m app.services.digest.scheduler`
- `postgres`: 영속 Docker volume 사용

## 환경 구성

1. 개발은 `backend/.env.example`을 복사해 `backend/.env`로 사용합니다.
2. staging/production은 `.env.production.example`을 복사해 별도 secret 저장소에서 값을 채웁니다.
3. `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`, DB 비밀번호는 이미지·Git·프론트 번들에 넣지 않습니다.
4. staging/production에서는 `APP_PUBLIC_URL`, `CORS_ALLOWED_ORIGINS`, `ALLOWED_HOSTS`, `DATABASE_URL`이 필수입니다.

## 빌드와 시작

```powershell
docker compose -f docker-compose.yml config
docker compose --env-file .env.production -f docker-compose.prod.yml config
docker compose --env-file .env.production -f docker-compose.prod.yml build
docker compose --env-file .env.production -f docker-compose.prod.yml up -d postgres
```

## 마이그레이션

배포 전 DB 백업 후 다음 순서를 지킵니다.

```powershell
docker compose --env-file .env.production -f docker-compose.prod.yml run --rm migrate alembic current
docker compose --env-file .env.production -f docker-compose.prod.yml run --rm migrate alembic heads
docker compose --env-file .env.production -f docker-compose.prod.yml run --rm migrate alembic upgrade head
```

마이그레이션이 실패하면 새 backend를 시작하지 않고 현재 DB와 로그를 보존합니다. `alembic downgrade`는 자동 롤백 수단으로 사용하지 않으며, 애플리케이션을 이전 이미지로 되돌릴 수 있고 schema가 호환되는 경우에만 rollback합니다.

## 백업·복구

```powershell
pg_dump --format=custom --file=steel_insight_YYYYMMDD_HHMM.dump "$env:DATABASE_URL"
createdb steel_insight_restore
pg_restore --clean --if-exists --dbname="$env:RESTORE_DATABASE_URL" steel_insight_YYYYMMDD_HHMM.dump
```

백업 파일은 애플리케이션 컨테이너 외부에 보관합니다. staging에서 복구 후 `alembic current`, `/health`, `/api/v1/admin/health`, smoke test와 데이터 무결성 검증을 수행하고 복구 시간·파일·결과를 기록합니다.

## Smoke test

```powershell
$env:SMOKE_BASE_URL='https://staging.example.com'
cd backend
python -m app.services.deployment.smoke_test
```

이 검사는 liveness, admin readiness, version/knowledge metadata만 확인하며 Telegram 테스트 발송이나 외부 뉴스 수집을 자동 실행하지 않습니다.

## 롤백과 장애 대응

- API 장애: 이전 backend image로 되돌리고 schema 호환 여부를 확인합니다.
- migration 실패: 새 버전을 중지하고 DB 백업을 보존합니다.
- OpenAI 장애: 수집을 중단하지 않고 `READY_FOR_INTELLIGENCE` backlog를 운영 화면에서 관찰합니다.
- Telegram 장애: AlertDelivery를 `RETRY_PENDING`/`FAILED`로 유지하고 기존 retry API를 사용합니다.
- scheduler 장애: 해당 프로세스만 재시작하고 collection/digest stale 상태를 확인합니다.
- 운영 장애가 해소되기 전 public exposure를 확대하지 않습니다.
