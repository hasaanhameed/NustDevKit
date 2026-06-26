"""Groq-backed answer generation for the docs assistant.

Builds a grounded system prompt (instructions + the language's knowledge) and streams the
model's answer token-by-token. Knowledge is concatenated, never .format()-ed, so the
braces inside the spec/SDK docs are left untouched.
"""
from collections.abc import AsyncIterator

from groq import AsyncGroq

from app.assistant.knowledge import get_knowledge, label_for
from app.core.config import settings

_INSTRUCTIONS = """You are the NUST LMS Developer Hub assistant, embedded in the API \
documentation portal. You help developers use the NUST LMS REST API and its SDKs.

Rules:
- STAY ON TOPIC. You only answer questions about the NUST LMS API — its authentication, \
endpoints, parameters, responses, and SDK usage — and about using this documentation \
portal. If the user asks about anything else (general knowledge, current events, other \
products, opinions, unrelated code), politely decline in ONE sentence and steer them \
back, e.g.: "I can only help with the NUST LMS Developer Hub — its API, auth, and SDKs. \
Ask me about logging in, courses, deadlines, or notifications." Do NOT answer the \
off-topic question even if you know the answer.
- Answer only from the documentation provided below. If something about the API is not \
covered, say you are not sure rather than inventing endpoints, parameters, or fields.
- Be concise: a short explanation plus a focused example. Keep answers brief.
- Prefer showing the HTTP request (method, path, query params) with a short curl example. \
The user is working in {label}; if they ask for {label} SDK code, describe the workflow \
(install the SDK, create a client with the bearer token, then call the method for that \
endpoint) and tell them to confirm exact method names in the SDK's own docs, which are \
not included here.
- Cite endpoint paths (e.g. GET /service/core_course_get_recent_courses) when relevant.
- The API is read-only and scoped to the authenticated user; there is no way to modify \
data or look up other users."""


def is_configured() -> bool:
    return bool(settings.groq_api_key)


def _build_system_prompt(language: str) -> str:
    instructions = _INSTRUCTIONS.format(label=label_for(language))
    knowledge = get_knowledge(language)
    return (
        f"{instructions}\n\n"
        "=== DOCUMENTATION START ===\n"
        f"{knowledge}\n"
        "=== DOCUMENTATION END ==="
    )


def _client() -> AsyncGroq:
    return AsyncGroq(
        api_key=settings.groq_api_key,
        timeout=settings.assistant_timeout_seconds,
        max_retries=settings.assistant_max_retries,
    )


async def open_stream(question: str, language: str, history: list[dict[str, str]]):
    """Start the Groq completion. The HTTP request is made here, so a Groq outage,
    5xx, or timeout raises *before* streaming begins — letting the route return a
    clean 502 rather than a half-sent 200.
    """
    messages: list[dict[str, str]] = [
        {"role": "system", "content": _build_system_prompt(language)}
    ]
    messages.extend(history)
    messages.append({"role": "user", "content": question})
    return await _client().chat.completions.create(
        model=settings.assistant_model,
        messages=messages,
        temperature=0.2,
        stream=True,
    )


async def iter_stream(stream) -> AsyncIterator[str]:
    """Yield answer text from an already-opened stream (mid-stream errors propagate)."""
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
