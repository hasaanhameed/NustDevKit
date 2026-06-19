"""NustDevKit gateway — entrypoint.

Run from the backend/ directory:
    uvicorn main:app --reload
"""
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.routes import auth, service
from app.services.lms_session import LMSAjaxError, LMSAuthError

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
    # Auth is via the Authorization: Bearer header (not cookies), so credentialed
    # CORS isn't needed — keeping this False lets allow_origins=["*"] work for
    # browser-based test requests from the docs (Scalar "Send").
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(service.router)


@app.exception_handler(LMSAjaxError)
async def handle_lms_ajax_error(_: Request, exc: LMSAjaxError) -> JSONResponse:
    # A Moodle method rejected the call — surface its exception as a 400.
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": exc.detail})


@app.exception_handler(LMSAuthError)
async def handle_lms_auth_error(_: Request, exc: LMSAuthError) -> JSONResponse:
    # Lost/expired LMS session — the caller should log in again.
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": "Session expired; please log in again."},
    )


@app.get("/health", tags=["Meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
