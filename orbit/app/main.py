from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Orbit personal AI operating system backend.",
)


@app.get("/")
def root() -> dict:
    return {
        "service": "orbit-api",
        "status": "running",
        "environment": settings.app_env,
    }


@app.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "service": "orbit-api",
    }