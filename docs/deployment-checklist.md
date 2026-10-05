# Deployment Checklist

## Staging gate

- [ ] Backend tests pass
- [ ] Frontend syntax/build check pass
- [ ] `alembic upgrade head` succeeds on clean DB
- [ ] Previous-schema migration tested
- [ ] `docker compose config` succeeds
- [ ] Backend/frontend images build
- [ ] Production/staging secrets configured outside Git
- [ ] CORS and allowed hosts are explicit
- [ ] DB backup completed
- [ ] Restore test completed and recorded
- [ ] `/health` passes
- [ ] `/api/v1/admin/health` passes
- [ ] `python -m app.services.deployment.smoke_test` passes
- [ ] News scheduler, delivery worker, digest scheduler each have one instance
- [ ] Delivery dry-run/test channel verified
- [ ] Latest evaluation, E2E, and performance gates reviewed

## Pilot gate

- [ ] 5–10 validated sources only
- [ ] Separate staging/pilot database
- [ ] Explicit pilot users/network access
- [ ] Test Telegram channel only
- [ ] Daily digest enabled first
- [ ] No critical quality regression
- [ ] Backlog, delivery failures and scheduler freshness monitored

## Production classification

`PRODUCTION_READY` requires a completed controlled pilot, validated restore/rollback, passing quality/E2E/performance gates, stable workers/schedulers, and no unresolved critical failures. Without those artifacts the release remains `STAGING_READY` or `PILOT_READY`.
