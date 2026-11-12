from fastapi import FastAPI

from app.api.routes.datasets import router as datasets_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API for the NEXUS social network intelligence platform.",
    version="0.1.0",
)

app.include_router(datasets_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
