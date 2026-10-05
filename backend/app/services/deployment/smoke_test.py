import json
import os
import sys
from urllib.error import URLError
from urllib.request import Request, urlopen


def check(base_url: str, path: str) -> tuple[bool, str]:
    try:
        with urlopen(Request(base_url.rstrip("/") + path, headers={"Accept": "application/json"}), timeout=10) as response:
            return response.status < 400, f"HTTP {response.status}"
    except (URLError, TimeoutError, ValueError) as exc:
        return False, str(exc)[:160]


def main() -> None:
    base_url = os.getenv("SMOKE_BASE_URL", "http://localhost:8000")
    checks = [("backend liveness", "/health"), ("admin readiness", "/api/v1/admin/health"), ("version metadata", "/api/v1/admin/version")]
    results = []
    for name, path in checks:
        passed, detail = check(base_url, path); results.append({"name": name, "status": "PASS" if passed else "FAIL", "detail": detail}); print(f"{results[-1]['status']} {name}: {detail}")
    print(json.dumps({"base_url": base_url, "checks": results}, ensure_ascii=False))
    raise SystemExit(0 if all(item["status"] == "PASS" for item in results) else 1)


if __name__ == "__main__": main()
