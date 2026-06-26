from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.core.limiter import limiter
from app.mcp import mcp
from app.routes import assistant, auth, service
from app.services.lms_session import LMSAjaxError, LMSAuthError


mcp_app = mcp.http_app(path="/")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Gateway that authenticates against NUST LMS on the user's behalf and "
        "proxies the Moodle AJAX service behind a clean bearer-token API."
    ),
    lifespan=mcp_app.lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    # Bearer-header auth (not cookies), so credentialed CORS isn't needed.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# slowapi needs the limiter on app.state so the route decorator and 429 handler share it.
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth.router)
app.include_router(service.router)
app.include_router(assistant.router)

app.mount("/mcp", mcp_app)


@app.exception_handler(LMSAjaxError)
async def handle_lms_ajax_error(_: Request, exc: LMSAjaxError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": exc.detail})


@app.exception_handler(LMSAuthError)
async def handle_lms_auth_error(_: Request, exc: LMSAuthError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": "Session expired; please log in again."},
    )


@app.get("/health", tags=["Meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
