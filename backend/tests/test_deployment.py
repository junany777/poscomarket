from app.core.deployment import missing_runtime_values


def test_production_config_requires_public_runtime_values():
    missing = missing_runtime_values("production", "", "", "*", "*", True, None)
    assert {"DATABASE_URL", "APP_PUBLIC_URL", "OPENAI_API_KEY", "CORS_ALLOWED_ORIGINS without wildcard", "ALLOWED_HOSTS without wildcard"} <= set(missing)


def test_development_config_can_use_local_defaults():
    assert missing_runtime_values("development", "sqlite:///./steel_insight.db", "", "*", "*", False, None) == []
