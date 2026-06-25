"""Knowledge base for the docs assistant — free-tier build.

Groq's free plan caps requests at ~6-8K tokens/minute, far below the full spec + SDK
docs (~31K). So the assistant is grounded in a single compact, hand-written guide
(`knowledge.md`, ~1.3K tokens) — enough to answer auth / endpoint / parameter questions
while staying under the free-tier limit.

To switch back to the richer full-context build (full OpenAPI spec + per-language SDK
docs), upgrade the Groq tier and restore spec/SDK assembly here.
"""
from functools import lru_cache
from pathlib import Path

_CURATED = Path(__file__).parent / "knowledge.md"

# Languages offered in the widget selector. On the free tier we don't ship per-language
# SDK docs, so this only frames which SDK answers should mention (see the system prompt).
LANGS: dict[str, tuple[str, str]] = {
    "typescript": ("ts_generic_lib", "TypeScript"),
    "python": ("python_generic_lib", "Python"),
    "java": ("java_eclipse_jre_lib", "Java"),
    "csharp": ("cs_net_standard_lib", ".NET (C#)"),
    "go": ("go_generic_lib", "Go"),
    "php": ("php_generic_lib_v2", "PHP"),
    "ruby": ("ruby_generic_lib", "Ruby"),
}

SUPPORTED_LANGUAGES = list(LANGS)


def label_for(language: str) -> str:
    entry = LANGS.get(language)
    return entry[1] if entry else "your"


@lru_cache(maxsize=1)
def _guide() -> str:
    try:
        return _CURATED.read_text(encoding="utf-8")
    except OSError:
        return ""


def get_knowledge(language: str) -> str:
    """The grounding knowledge for a request.

    Free-tier build: language-agnostic (the compact guide). The selected language only
    affects how answers are framed, not the knowledge content.
    """
    return _guide()
