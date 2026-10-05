# 배포 연결 설정

## GitHub Pages와 OpenDART

GitHub Pages는 정적 프론트엔드만 제공하므로 OpenDART API 키를 직접 넣을 수 없습니다. `DART_API_KEY`는 반드시 FastAPI 백엔드의 환경변수(`backend/.env`)에만 보관해야 합니다.

공개 배포를 완료하려면 다음 두 가지가 필요합니다.

1. FastAPI 백엔드를 HTTPS 주소로 배포합니다.
2. 배포된 프론트엔드의 `api-config.js`에서 `window.POSCO_API_BASE_URL`을 해당 주소로 설정합니다.

예시:

```js
window.POSCO_API_BASE_URL = "https://api.example.com";
```

백엔드 환경변수 예시:

```env
DART_API_KEY=발급받은_OpenDART_키
CORS_ALLOWED_ORIGINS=https://junany777.github.io
```

현재처럼 공개 백엔드 주소가 없는 상태에서 GitHub Pages가 `localhost:8000`을 호출하면, 방문자의 컴퓨터에 백엔드가 없기 때문에 연결할 수 없습니다. 이 경우 화면에는 가짜 연결 성공 대신 `공개 백엔드 주소 필요`가 표시됩니다.
