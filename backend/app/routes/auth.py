"""Authentication routes: exchange NUST LMS credentials for a gateway token."""
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials

from app.core.security import create_access_token, decode_access_token
from app.dependencies import bearer_scheme
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.lms_session import LMSSession
from app.services.session_store import InMemorySessionStore, get_session_store

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
async def login(
    body: LoginRequest,
    store: InMemorySessionStore = Depends(get_session_store),
) -> TokenResponse:
    """Log into NUST LMS on the user's behalf and return a bearer token.

    The live LMS session (cookie + sesskey) is kept server-side; the caller only
    ever receives the gateway JWT.
    """
    lms = LMSSession()
    try:
        ok = await lms.login(body.email.strip().lower(), body.password)
    except NotImplementedError:
        # LMSSession not yet ported — surface clearly during scaffolding.
        await lms.close()
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="LMSSession.login() is not implemented yet (port pending).",
        )
    except Exception:
        await lms.close()
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Upstream LMS login failed.",
        )

    if not ok:
        await lms.close()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid LMS credentials.",
        )

    session_id = await store.create(lms)
    return TokenResponse(access_token=create_access_token(session_id))


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    store: InMemorySessionStore = Depends(get_session_store),
) -> None:
    """Invalidate the current session and release its upstream LMS client."""
    try:
        session_id = decode_access_token(credentials.credentials).get("sub")
    except jwt.PyJWTError:
        session_id = None

    if session_id:
        session = await store.pop(session_id)
        if session is not None:
            await session.close()
    return None
