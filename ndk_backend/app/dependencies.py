"""Shared FastAPI dependencies — primarily resolving the bearer token to a
live, server-side LMS session.
"""
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token
from app.services.lms_session import LMSSession
from app.services.session_store import InMemorySessionStore, get_session_store

bearer_scheme = HTTPBearer(auto_error=True)


async def resolve_session_from_token(
    token: str,
    store: InMemorySessionStore,
) -> LMSSession:
    """Resolve a raw Bearer JWT string to the live LMS session it represents.

    Single source of truth for bearer auth, shared by the REST routes (which get
    the token from FastAPI's HTTPBearer dependency) and the MCP tools (which read
    it from the raw Authorization header). Raises HTTP 401 on invalid/expired
    tokens or lost sessions.
    """
    try:
        payload = decode_access_token(token)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    session_id = payload.get("sub")
    session = await store.get(session_id) if session_id else None
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired; please log in again",
        )
    return session


async def get_current_session(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    store: InMemorySessionStore = Depends(get_session_store),
) -> LMSSession:
    """Resolve the Bearer JWT to the LMS session it represents, or 401."""
    return await resolve_session_from_token(credentials.credentials, store)
