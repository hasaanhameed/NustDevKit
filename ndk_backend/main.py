from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
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
    # Auth is via the Authorization: Bearer header (not cookies), so credentialed
    # CORS isn't needed — keeping this False lets allow_origins=["*"] work for
    # browser-based test requests from the docs (Scalar "Send").
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Per-IP rate limiting for the assistant route (slowapi). Registered on app.state so
# the @limiter.limit decorator and the 429 handler share one limiter instance.
app.state.limiter = assistant.limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth.router)
app.include_router(service.router)
app.include_router(assistant.router)

# Mount the MCP server. AI assistants connect to http://<host>/mcp with their
# bearer token; each tool resolves that token to the caller's live LMS session.
app.mount("/mcp", mcp_app)


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
