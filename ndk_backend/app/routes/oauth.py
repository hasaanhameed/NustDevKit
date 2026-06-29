import base64
import hashlib
import logging
import os
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

from app.core.security import create_access_token
from app.oauth.store import OAuthStore, get_oauth_store
from app.services.lms_session import LMSSession, LMSUpstreamError
from app.services.session_store import InMemorySessionStore, get_session_store

router = APIRouter(tags=["OAuth"])

logger = logging.getLogger("uvicorn.error")

_LOGIN_HTML = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../oauth/login.html")).read()


def _render_login(
    client_id: str,
    redirect_uri: str,
    code_challenge: str,
    code_challenge_method: str,
    state: str,
    error: str = "",
) -> str:
    return (
        _LOGIN_HTML
        .replace("{% if error %}", "" if error else "<!--")
        .replace("{% endif %}", "" if error else "-->")
        .replace("{{ error }}", error)
        .replace('value="{{ client_id }}"', f'value="{client_id}"')
        .replace('value="{{ redirect_uri }}"', f'value="{redirect_uri}"')
        .replace('value="{{ code_challenge }}"', f'value="{code_challenge}"')
        .replace('value="{{ code_challenge_method }}"', f'value="{code_challenge_method}"')
        .replace('value="{{ state }}"', f'value="{state}"')
    )


def _verify_pkce(code_verifier: str, code_challenge: str, method: str) -> bool:
    if method == "S256":
        digest = hashlib.sha256(code_verifier.encode()).digest()
        expected = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
        return expected == code_challenge
    return False


# ---------------------------------------------------------------------------
# Dynamic client registration — RFC 7591
# ---------------------------------------------------------------------------

@router.post("/oauth/register", status_code=status.HTTP_201_CREATED)
async def register_client(
    request: Request,
    oauth: OAuthStore = Depends(get_oauth_store),
) -> JSONResponse:
    body = await request.json()
    redirect_uris = body.get("redirect_uris", [])
    client_name = body.get("client_name", "")

    if not redirect_uris:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "invalid_client_metadata", "error_description": "redirect_uris is required"},
        )

    client = oauth.register_client(redirect_uris=redirect_uris, client_name=client_name)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "client_id": client.client_id,
            "client_secret": client.client_secret,
            "redirect_uris": client.redirect_uris,
            "client_name": client.client_name,
            "grant_types": ["authorization_code"],
            "response_types": ["code"],
            "token_endpoint_auth_method": "client_secret_post",
        },
    )


# ---------------------------------------------------------------------------
# Authorization endpoint — serves the login page
# ---------------------------------------------------------------------------

@router.get("/oauth/authorize")
async def authorize_get(
    client_id: str,
    redirect_uri: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str = "S256",
    state: str = "",
    oauth: OAuthStore = Depends(get_oauth_store),
) -> HTMLResponse:
    client = oauth.get_client(client_id)
    if client is None or redirect_uri not in client.redirect_uris:
        return HTMLResponse("<h1>Invalid client or redirect_uri</h1>", status_code=400)

    html = _render_login(
        client_id=client_id,
        redirect_uri=redirect_uri,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        state=state,
    )
    return HTMLResponse(html)


@router.post("/oauth/authorize", response_model=None)
async def authorize_post(
    request: Request,
    client_id: str = Form(...),
    redirect_uri: str = Form(...),
    code_challenge: str = Form(...),
    code_challenge_method: str = Form(...),
    state: str = Form(""),
    username: str = Form(...),
    password: str = Form(...),
    oauth: OAuthStore = Depends(get_oauth_store),
    store: InMemorySessionStore = Depends(get_session_store),
) -> HTMLResponse | RedirectResponse:
    client = oauth.get_client(client_id)
    if client is None or redirect_uri not in client.redirect_uris:
        return HTMLResponse("<h1>Invalid client or redirect_uri</h1>", status_code=400)

    lms = LMSSession()
    try:
        ok = await lms.login(username.strip(), password)
    except LMSUpstreamError:
        await lms.close()
        html = _render_login(
            client_id=client_id,
            redirect_uri=redirect_uri,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            state=state,
            error="The NUST LMS is currently unreachable. Please try again shortly.",
        )
        return HTMLResponse(html, status_code=200)

    if not ok:
        await lms.close()
        html = _render_login(
            client_id=client_id,
            redirect_uri=redirect_uri,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            state=state,
            error="Invalid username or password.",
        )
        return HTMLResponse(html, status_code=200)

    session_id = await store.create(lms)
    code = oauth.create_auth_code(
        client_id=client_id,
        redirect_uri=redirect_uri,
        session_id=session_id,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    )

    params = {"code": code}
    if state:
        params["state"] = state
    return RedirectResponse(
        url=f"{redirect_uri}?{urlencode(params)}",
        status_code=status.HTTP_302_FOUND,
    )


# ---------------------------------------------------------------------------
# Token endpoint — code exchange + refresh
# ---------------------------------------------------------------------------

@router.post("/oauth/token")
async def token(
    grant_type: str = Form(...),
    code: str = Form(None),
    redirect_uri: str = Form(None),
    client_id: str = Form(None),
    code_verifier: str = Form(None),
    refresh_token: str = Form(None),
    oauth: OAuthStore = Depends(get_oauth_store),
    store: InMemorySessionStore = Depends(get_session_store),
) -> JSONResponse:

    if grant_type == "authorization_code":
        if not code or not redirect_uri or not client_id or not code_verifier:
            logger.warning(
                "token exchange missing params: code=%s redirect_uri=%s client_id=%s code_verifier=%s",
                bool(code), bool(redirect_uri), bool(client_id), bool(code_verifier),
            )
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_request", "error_description": "Missing required parameters"},
            )

        auth_code = oauth.consume_auth_code(code)
        if auth_code is None:
            logger.warning("token exchange: auth code not found or expired")
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_grant", "error_description": "Authorization code is invalid or expired"},
            )

        if auth_code.client_id != client_id or auth_code.redirect_uri != redirect_uri:
            logger.warning(
                "token exchange mismatch: client_id stored=%r sent=%r | redirect_uri stored=%r sent=%r",
                auth_code.client_id, client_id, auth_code.redirect_uri, redirect_uri,
            )
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_grant", "error_description": "client_id or redirect_uri mismatch"},
            )

        if not _verify_pkce(code_verifier, auth_code.code_challenge, auth_code.code_challenge_method):
            logger.warning(
                "token exchange PKCE fail: method=%r stored_challenge=%r",
                auth_code.code_challenge_method, auth_code.code_challenge,
            )
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_grant", "error_description": "PKCE verification failed"},
            )

        access_token = create_access_token(auth_code.session_id)
        new_refresh = oauth.create_refresh_token(client_id=client_id, session_id=auth_code.session_id)

        return JSONResponse({
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": 720 * 60,
            "refresh_token": new_refresh,
        })

    if grant_type == "refresh_token":
        if not refresh_token:
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_request", "error_description": "refresh_token is required"},
            )

        entry = oauth.consume_refresh_token(refresh_token)
        if entry is None:
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_grant", "error_description": "Refresh token is invalid or already used"},
            )

        session = await store.get(entry.session_id)
        if session is None:
            return JSONResponse(
                status_code=400,
                content={"error": "invalid_grant", "error_description": "Session has expired; please log in again"},
            )

        access_token = create_access_token(entry.session_id)
        new_refresh = oauth.create_refresh_token(client_id=entry.client_id, session_id=entry.session_id)

        return JSONResponse({
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": 720 * 60,
            "refresh_token": new_refresh,
        })

    return JSONResponse(
        status_code=400,
        content={"error": "unsupported_grant_type"},
    )
