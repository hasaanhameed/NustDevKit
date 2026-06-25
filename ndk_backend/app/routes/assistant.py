"""Docs-assistant route: streamed, grounded Q&A over the API docs.

Open access (no auth) but rate-limited per client IP via slowapi. The model call is
billed to the server's Groq key, so the limit caps cost/abuse.
"""
from typing import Literal

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.assistant.knowledge import SUPPORTED_LANGUAGES
from app.assistant.service import is_configured, stream_answer
from app.core.config import settings

router = APIRouter(prefix="/assistant", tags=["Assistant"])

# Shared with main.py (app.state.limiter) so the decorator and handler agree.
limiter = Limiter(key_func=get_remote_address)


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)
    language: str = "python"
    history: list[Message] = Field(default_factory=list)


@router.post("/ask")
@limiter.limit(settings.assistant_rate_limit)
async def ask(request: Request, body: AskRequest) -> StreamingResponse:
    if not is_configured():
        raise HTTPException(status_code=503, detail="Assistant is not configured (no GROQ_API_KEY).")

    question = body.question.strip()[: settings.assistant_max_question_chars]
    if not question:
        raise HTTPException(status_code=422, detail="Question is empty.")

    language = body.language if body.language in SUPPORTED_LANGUAGES else "python"
    history = [m.model_dump() for m in body.history[-settings.assistant_max_history :]]

    async def gen():
        try:
            async for delta in stream_answer(question, language, history):
                yield delta
        except Exception:  # noqa: BLE001 — surface a friendly note instead of a broken stream
            yield "\n\n_(the assistant hit an error — please try again)_"

    return StreamingResponse(gen(), media_type="text/plain; charset=utf-8")
