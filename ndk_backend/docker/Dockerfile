# NustDevKit gateway — container image.
#
# Single-stage on python:3.12-slim: every dependency ships prebuilt manylinux wheels,
# so no compiler/build tools are needed — there is nothing for a builder stage to strip,
# and with --no-cache-dir the image is already minimal. (Alpine is avoided on purpose:
# musl has no wheels for cryptography/pydantic-core, forcing slow source builds and a
# larger image.)
FROM python:3.12-slim

# No .pyc files, unbuffered logs, no pip cache or version nag.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install dependencies first so this layer is cached and only rebuilds when
# requirements.txt changes (not on every code edit).
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Application code (the .dockerignore keeps out venv, caches, .env, git).
COPY . .

# Run as an unprivileged user.
RUN useradd --create-home --uid 10001 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Liveness check against the gateway's /health (no curl in slim — use stdlib).
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2).status==200 else 1)"

# Single worker is required: sessions live in-process (in-memory store), so multiple
# workers would not share login state. Do NOT add --workers.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
