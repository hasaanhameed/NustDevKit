# NustDevKit Gateway

FastAPI gateway that logs into NUST LMS (Moodle) on the user's behalf and proxies
the Moodle AJAX service behind a clean **username/password → bearer token** API.
The ephemeral Moodle `sesskey` is handled entirely server-side, so SDK users never
deal with it.

## Architecture

```
SDK user ──(email + password)──▶  POST /auth/login
                                     │  LMSSession.login()  (gets cookie + sesskey)
                                     ◀──  { access_token: <JWT>, token_type: "bearer" }

SDK user ──(Bearer JWT)──▶  POST /service/<moodle_method>
                                     │  resolve JWT → live LMS session (in-memory)
                                     │  LMSSession.call_ajax(method, args) → Moodle
                                     ◀──  data
```

Sessions are held **in memory** (no database). On process restart or sesskey
expiry, the user logs in again. Swap `app/services/session_store.py` for a
SQLite/Redis-backed store later if you need persistence or auto-refresh.

## Layout

```
backend/
  main.py                  # FastAPI app / entrypoint
  requirements.txt
  .env.example
  app/
    core/
      config.py            # Settings (pydantic-settings)
      security.py          # JWT issue/verify
    routes/
      auth.py              # POST /auth/login, /auth/logout
      service.py           # the 8 proxied LMS endpoints
    schemas/
      auth.py              # LoginRequest, TokenResponse
      service.py           # request models for the LMS endpoints
    services/
      lms_session.py       # ⟵ PORT TARGET: your NustPulse LMSSession goes here
      session_store.py     # in-memory session id → LMSSession
    dependencies.py        # bearer token → live LMS session
```

## Run

```bash
cd backend
python -m venv .venv && .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # then edit JWT_SECRET
uvicorn main:app --reload
```

Interactive docs at http://127.0.0.1:8000/docs, health at `/health`.

## Before it works end-to-end

`app/services/lms_session.py` is a **port target** — paste your existing NustPulse
`LMSSession` (login + sesskey scrape) and implement `call_ajax()` to forward Moodle
AJAX calls. Until then, `/auth/login` returns `501 Not Implemented` by design.
