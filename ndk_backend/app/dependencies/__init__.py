"""Shared FastAPI dependencies.

Public names are re-exported here so call sites import from `app.dependencies`
regardless of which submodule a dependency lives in. Add new cross-cutting
dependencies (rate limiting, pagination, DB sessions, ...) as sibling modules.
"""
from app.dependencies.auth import (
    bearer_scheme,
    get_current_session,
    resolve_session_from_token,
)

__all__ = [
    "bearer_scheme",
    "get_current_session",
    "resolve_session_from_token",
]
