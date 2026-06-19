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
    lms_base_url: str = "https://lms.nust.edu.pk"

    # --- CORS ---
    cors_origins: list[str] = ["*"]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
