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


async def get_current_session(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    store: InMemorySessionStore = Depends(get_session_store),
) -> LMSSession:
    """Resolve the Bearer JWT to the LMS session it represents, or 401."""
    try:
        payload = decode_access_token(credentials.credentials)
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
