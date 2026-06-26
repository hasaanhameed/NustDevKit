"""Shared slowapi rate limiter — one instance, registered on app.state in main.py."""
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
