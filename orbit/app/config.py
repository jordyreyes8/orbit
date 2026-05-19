from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Orbit"
    app_env: str = "local"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    postgres_user: str = "orbit"
    postgres_password: str = "orbit"
    postgres_db: str = "orbit"
    postgres_host: str = "db"
    postgres_port: int = 5432

    database_url: str = "postgresql://orbit:orbit@db:5432/orbit"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()