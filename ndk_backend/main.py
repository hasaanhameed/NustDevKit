from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.core.limiter import limiter
from app.mcp import mcp
from app.routes import assistant, auth, oauth, service
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
app.include_router(oauth.router)
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


@app.get("/.well-known/oauth-authorization-server", tags=["Meta"], include_in_schema=False)
async def oauth_metadata(request: Request) -> JSONResponse:
    base = _base_url(request)
    return JSONResponse({
        "issuer": base,
        "authorization_endpoint": f"{base}/oauth/authorize",
        "token_endpoint": f"{base}/oauth/token",
        "registration_endpoint": f"{base}/oauth/register",
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code", "refresh_token"],
        "code_challenge_methods_supported": ["S256"],
    })


def _base_url(request: Request) -> str:
    proto = request.headers.get("x-forwarded-proto", "https")
    host = request.headers.get("host", "api.nustdevkit.com")
    return f"{proto}://{host}"


# RFC 9728 — tells an MCP client which authorization server protects /mcp. Clients
# probe this at the site root (and the /mcp-suffixed variant), so we serve it here
# rather than under the mounted MCP app. Required by stricter (web) MCP clients.
@app.get("/.well-known/oauth-protected-resource", tags=["Meta"], include_in_schema=False)
@app.get("/.well-known/oauth-protected-resource/mcp", tags=["Meta"], include_in_schema=False)
async def oauth_protected_resource(request: Request) -> JSONResponse:
    base = _base_url(request)
    return JSONResponse({
        "resource": f"{base}/mcp/",
        "authorization_servers": [base],
    })
