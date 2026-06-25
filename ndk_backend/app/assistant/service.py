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
documentation portal. Help developers use the NUST LMS REST API.

Rules:
- Answer ONLY from the documentation provided below. If something is not covered, say you \
are not sure rather than inventing endpoints, parameters, or fields.
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


async def stream_answer(
    question: str, language: str, history: list[dict[str, str]]
) -> AsyncIterator[str]:
    """Yield the assistant's answer token-by-token for the given question/language/history."""
    messages: list[dict[str, str]] = [
        {"role": "system", "content": _build_system_prompt(language)}
    ]
    messages.extend(history)
    messages.append({"role": "user", "content": question})

    client = AsyncGroq(api_key=settings.groq_api_key)
    stream = await client.chat.completions.create(
        model=settings.assistant_model,
        messages=messages,
        temperature=0.2,
        stream=True,
    )
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
