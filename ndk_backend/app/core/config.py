"""Application settings, loaded from environment / .env (pydantic-settings)."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # --- App ---
    app_name: str = "NUST LMS Developer Hub Gateway"
    app_version: str = "1.0.0"

    # --- Auth / JWT ---
    # NOTE: the default is for local dev only. Set a long random JWT_SECRET in .env
    # for anything exposed to real users.
    jwt_secret: str = "dev-insecure-change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 720  # 12 hours

    # --- Upstream NUST LMS (Moodle) ---
    # Includes the /portal path segment; login + AJAX endpoints hang off this.
    lms_base_url: str = "https://lms.nust.edu.pk/portal"
    # NUST LMS has TLS chain quirks; the proven NustPulse client disables verify.
    lms_verify_ssl: bool = False
    lms_user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    # --- CORS ---
    cors_origins: list[str] = ["*"]

    # --- Docs assistant (Groq) ---
    # Required to run the assistant; leave empty to disable it (route returns 503).
    groq_api_key: str = ""
    assistant_model: str = "openai/gpt-oss-120b"
    assistant_rate_limit: str = "15/minute"  # per client IP (slowapi)
    assistant_max_question_chars: int = 2000
    assistant_max_history: int = 8  # messages of context kept per request


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
