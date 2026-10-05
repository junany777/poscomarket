from pathlib import Path

from app.core.config import settings


def missing_runtime_values(environment: str, database_url: str, app_public_url: str, cors_allowed_origins: str, allowed_hosts: str, openai_required: bool, openai_api_key: str | None) -> list[str]:
    missing = []
    if environment not in {"development", "staging", "production"}: missing.append("APP_ENV")
    if environment in {"staging", "production"}:
        if not database_url: missing.append("DATABASE_URL")
        if not app_public_url: missing.append("APP_PUBLIC_URL")
        if openai_required and not openai_api_key: missing.append("OPENAI_API_KEY")
        if not cors_allowed_origins or "*" in cors_allowed_origins.split(","): missing.append("CORS_ALLOWED_ORIGINS without wildcard")
        if not allowed_hosts or "*" in allowed_hosts.split(","): missing.append("ALLOWED_HOSTS without wildcard")
    return missing


def validate_runtime_config() -> None:
    environment = settings.app_env.lower()
    missing = missing_runtime_values(environment, settings.database_url, settings.app_public_url, settings.cors_allowed_origins, settings.allowed_hosts, settings.openai_required, settings.openai_api_key)
    if missing: raise RuntimeError("Missing runtime configuration: " + ", ".join(missing))


def required_knowledge_files() -> list[str]:
    root = Path(__file__).resolve().parents[3]
    return ["knowledge/taxonomy/materials.md", "knowledge/posco/index.md"]


def check_required_knowledge_files() -> dict:
    root = Path(__file__).resolve().parents[3]
    files = [{"path": relative, "exists": (root / relative).exists()} for relative in required_knowledge_files()]
    return {"passed": all(item["exists"] for item in files), "files": files}
