# NustDevKit Gateway (`ndk_backend`)

FastAPI gateway that logs into NUST LMS (Moodle) on the user's behalf and proxies
the Moodle AJAX service behind a clean **username/password → bearer token** API.
The ephemeral Moodle `sesskey` is handled entirely server-side, so SDK users never
deal with it.

## Architecture

```
SDK user ──(username + password)──▶  POST /auth/login
                                       │  LMSSession.login()  (gets cookie + sesskey)
                                       ◀──  { access_token: <JWT>, token_type: "bearer" }

SDK user ──(Bearer JWT)──▶  GET /service/<moodle_method>?<params>
                                       │  resolve JWT → live LMS session (in-memory)
                                       │  LMSSession.call_ajax(method, args) → Moodle (POST)
                                       ◀──  data
```

The reads are exposed as **GET** with query params; the gateway translates each into
the underlying Moodle AJAX call (which Moodle requires to be a POST). Sessions are held
**in memory** (no database) — on process restart or sesskey expiry, the user logs in
again.

## Layout

```
ndk_backend/
  main.py                  FastAPI app / entrypoint
  requirements.txt
  .env.example
  app/
    core/
      config.py            Settings (pydantic-settings)
      security.py          JWT issue/verify
    routes/
      auth.py              POST /auth/login, /auth/logout
      service.py           the 8 proxied LMS endpoints (GET)
    schemas/
      auth.py              LoginRequest, TokenResponse
      service.py           request models + enums for the LMS endpoints
    services/
      lms_session.py       Moodle login + sesskey + call_ajax (ported from NustPulse)
      session_store.py     in-memory token → LMSSession
    dependencies.py        Bearer JWT → live LMS session
```

## Run

```bash
cd ndk_backend
python -m venv .venv && .venv\Scripts\activate   # Windows (use source .venv/bin/activate on *nix)
pip install -r requirements.txt
cp .env.example .env        # then edit JWT_SECRET
uvicorn main:app --reload
```

Interactive docs at http://127.0.0.1:8000/docs, health at `/health`.

## Notes

- `app/services/lms_session.py` performs the real NUST LMS login (logintoken + cookie
  flow) and forwards AJAX calls; it disables TLS verification by default to match NUST's
  cert setup (`LMS_VERIFY_SSL`).
- The Scalar API reference + SDKs live in `../ndk_frontend` and are built from
  `../src/spec/openapi.yaml` via the repo's `npm run sync`.
