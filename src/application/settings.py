from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./db/example.db"


appSettings = AppSettings()
