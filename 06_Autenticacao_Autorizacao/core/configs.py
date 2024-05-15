from typing import Any

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/curso"
    DBBaseModel: Any = declarative_base()

    """
    # No terminal
    > python
    > import secrets
    > token: str = secrets.token_urlsafe(32)
    > token
    """
    JWT_SECRET: str = "Y9JNPm50Ijjxoro44s53N0-1TaFDgPUbg-i0S9uxujg"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
