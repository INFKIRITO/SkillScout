from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    app_name: str = "JobGenie AI"
    env: str = "development"

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
