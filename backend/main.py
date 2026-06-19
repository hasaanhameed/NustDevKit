"""NustDevKit gateway — entrypoint.

Run from the backend/ directory:
    uvicorn main:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes import auth, service

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Gateway that authenticates against NUST LMS on the user's behalf and "
        "proxies the Moodle AJAX service behind a clean bearer-token API."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(service.router)


@app.get("/health", tags=["Meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
