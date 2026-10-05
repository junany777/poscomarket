# Render 백엔드 배포

이 저장소는 `render.yaml`을 기준으로 FastAPI 백엔드를 Render Web Service에 배포할 수 있습니다.

## Render 설정

1. Render에서 `New → Blueprint`를 선택합니다.
2. GitHub 저장소 `junany777/poscomarket`를 연결합니다.
3. `render.yaml`의 `poscomarket-api` 서비스를 확인하고 배포합니다.
4. Render가 발급한 실제 URL을 확인합니다. 예상 형식은 `https://<service-name>.onrender.com`입니다.
5. 서비스의 Environment에 다음 비밀값을 입력합니다.

```text
DART_API_KEY=<OpenDART 인증키>
OPENAI_API_KEY=<사용하는 경우에만 입력>
```

인증키는 `render.yaml`, GitHub Pages 파일, 브라우저 번들에 입력하지 않습니다.

## 배포 명령

Blueprint를 사용하지 않는 경우 다음 값을 입력합니다.

```text
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
Health Check Path: /health
```

## 배포 확인

Render URL이 `https://poscomarket-api.onrender.com`으로 발급된 경우 다음 주소를 확인합니다.

```text
https://poscomarket-api.onrender.com/health
https://poscomarket-api.onrender.com/api/v1/dart/health
```

두 요청이 정상 응답하고 `/api/v1/dart/health`의 `connected`가 `true`이면 OpenDART 연결이 완료된 것입니다.

## GitHub Pages 연결

Render가 발급한 실제 URL을 받은 뒤 `api-config.js`의 GitHub Pages용 값을 다음처럼 설정합니다.

```js
window.POSCO_API_BASE_URL = "https://실제-render-서비스-주소.onrender.com";
```

그 후 `main` 브랜치에 push하면 GitHub Pages가 재배포됩니다. Render 서비스 URL은 임의로 만들지 말고 Render 대시보드에 표시된 실제 URL을 사용합니다.

## 운영 참고

현재 Blueprint는 MVP 실행을 위해 SQLite를 사용합니다. Render의 기본 파일 시스템은 영속 저장소가 아니므로, 운영 데이터 보존이 필요하면 Render PostgreSQL을 만들고 `DATABASE_URL`을 PostgreSQL 연결 문자열로 교체해야 합니다.
