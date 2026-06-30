# NustDevKit

**Developer portal and REST API gateway for the NUST LMS.**

NustDevKit wraps the NUST Learning Management System (Moodle) behind a clean, authenticated REST API — so students and developers can query their academic data (courses, deadlines, notifications, grades) without touching Moodle's session cookies or internal AJAX conventions.

Live at **[nustdevkit.com](https://www.nustdevkit.com)**

---

## What's Inside

| Component | Description |
|-----------|-------------|
| **Gateway** (`ndk_backend/`) | FastAPI app. Authenticates against the LMS, manages sessions server-side, and proxies data over a bearer-token API. |
| **Portal** (`ndk_frontend/`) | Scalar-powered API reference. Hosted on S3 + CloudFront at `nustdevkit.com`. |
| **MCP Server** | Self-hosted FastMCP server at `/mcp/` (Streamable HTTP, OAuth 2.0 + PKCE). Lets AI assistants (Claude, Cursor, etc.) call LMS data as tools. |
| **Docs Assistant** | Groq-backed streaming chat widget embedded in the portal. Answers questions about the API and SDKs. |
| **SDKs** | APIMatic-generated clients for TypeScript, Python, Java, .NET, Go, PHP, and Ruby — downloadable from the portal. |

---

## Architecture

```
Browser / AI assistant
        │
        ▼
   CloudFront CDN
   (nustdevkit.com)
        │
        ▼
      S3 Bucket          ──── static portal (HTML, OpenAPI spec, SDKs)
        
   api.nustdevkit.com
        │
        ▼
     Caddy (TLS)         ──── reverse proxy, Let's Encrypt cert
        │
        ▼
  FastAPI Gateway        ──── bearer-token auth, rate limiting, in-memory sessions
  (Docker on EC2)
        │
        ▼
   NUST LMS (Moodle)     ──── upstream: AJAX + token-REST endpoints
```

---

## Project Structure

```
NustDevKit/
├── ndk_backend/              # FastAPI gateway
│   ├── main.py               # App entry point, middleware, MCP mount
│   ├── app/
│   │   ├── core/             # Config, JWT, rate limiter
│   │   ├── routes/           # auth, oauth, service endpoints, assistant
│   │   ├── services/         # LMSSession (httpx client), session store
│   │   ├── schemas/          # Pydantic request/response models
│   │   ├── dependencies/     # FastAPI dependencies (auth resolution)
│   │   ├── oauth/            # OAuth 2.0 flow: store, token verifier, login page
│   │   ├── mcp/              # FastMCP server + tools (courses, calendar, notifications)
│   │   └── assistant/        # Groq streaming assistant + knowledge base
│   ├── docker/
│   │   └── Dockerfile
│   └── requirements.txt
│
├── ndk_frontend/             # Static portal (Scalar)
│   ├── index.html            # Custom header, chat widget, Scalar config
│   ├── openapi.yaml          # Processed spec (generated — do not edit directly)
│   └── sdks/                 # Downloadable SDK zips
│
├── src/                      # Source spec and portal content
│   └── spec/openapi.yaml     # Edit this — run `npm run sync` to propagate
│
├── portal/                   # APIMatic-generated reference (source of the SDKs & docs)
│   ├── static/sdks/          # SDK zips — the build copies these into ndk_frontend/sdks/
│   └── llms-pages/           # Per-language Markdown docs, one folder per SDK:
│       └── <language>/       #   (python, typescript, java, net-standard-library, go, php, ruby)
│           ├── getting-started/    # Install + client initialization
│           ├── api-endpoints/      # One doc per endpoint (params, example usage)
│           ├── models/             # One doc per model/enum (fields + import)
│           └── sdk-infrastructure/ # Client config, auth, errors, logging
│
├── scripts/                  # Build scripts
│   ├── sync-spec.mjs         # Copies spec + assets to ndk_frontend/
│   └── inject-code-samples.mjs  # Injects SDK/MCP code samples into spec
│
└── .github/workflows/
    ├── deploy-backend.yml    # Build → push to ECR → redeploy on EC2
    └── deploy-frontend.yml   # Sync ndk_frontend/ to S3 + invalidate CloudFront
```

> **Reading the SDK docs:** for hands-on usage of a specific SDK, open `portal/llms-pages/<language>/`. Start with `getting-started/` (install + client setup), then `api-endpoints/` for the call you need and `models/` for any request/response types it references. These are the per-SDK READMEs APIMatic generates; the live portal's Code Examples are extracted from the same source.

---

## Local Development

### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker Desktop (optional, for container testing)

### Backend

```bash
cd ndk_backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # fill in JWT_SECRET and GROQ_API_KEY
uvicorn main:app --reload
```

Gateway runs at `http://127.0.0.1:8000`. Interactive docs at `/docs`.

### Frontend

```bash
npm install
npm run sync    # processes src/spec/openapi.yaml → ndk_frontend/openapi.yaml
npm run dev     # syncs and starts a local file server
```

Portal opens at `http://localhost:3000`.

---

## Environment Variables

All settings are loaded from `.env` (or environment). Required in production:

| Variable | Description |
|----------|-------------|
| `JWT_SECRET` | Secret used to sign gateway JWTs. Generate with `python -c "import secrets; print(secrets.token_hex(32))"`. |
| `GROQ_API_KEY` | Groq API key for the docs assistant. Leave empty to disable the assistant (returns 503). |

Optional overrides:

| Variable | Default | Description |
|----------|---------|-------------|
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `720` | JWT lifetime (12 h). |
| `SESSION_IDLE_MINUTES` | `60` | Sliding idle TTL for in-memory LMS sessions. |
| `AUTH_LOGIN_RATE_LIMIT` | `5/minute` | Per-IP rate limit on `POST /auth/login`. |
| `ASSISTANT_RATE_LIMIT` | `15/minute` | Per-IP rate limit on the assistant. |
| `CORS_ORIGINS` | `["*"]` | Allowed CORS origins. |
| `LMS_BASE_URL` | `https://lms.nust.edu.pk/portal` | Upstream LMS base URL. |

---

## Docker

Build and run locally:

```bash
cd ndk_backend
docker build -f docker/Dockerfile -t nustdevkit .
docker run -p 8000:8000 \
  -e JWT_SECRET="your-secret" \
  -e GROQ_API_KEY="your-key" \
  nustdevkit
```

> **Single worker only.** Sessions are stored in-process. Do not run multiple replicas without migrating the session store to Redis first.

---

## Deployment

The project is deployed on AWS:

| Service | Role |
|---------|------|
| EC2 t3.micro (Mumbai) | Runs the Docker container |
| Amazon ECR | Private Docker image registry |
| Caddy | TLS termination + reverse proxy on the EC2 |
| S3 | Hosts the static frontend |
| CloudFront | CDN for the frontend |
| Elastic IP | Static IP for the EC2 instance |

CI/CD is handled by GitHub Actions:
- Push to `main` with changes under `ndk_backend/` → builds image, pushes to ECR, redeploys on EC2.
- Push to `main` with changes under `ndk_frontend/` → syncs to S3, invalidates CloudFront cache.

**Updating the API spec:**

```bash
# Edit src/spec/openapi.yaml, then:
npm run sync
git add ndk_frontend/openapi.yaml
git commit -m "Update spec"
git push
```

---

## API Overview

All `/service/*` endpoints require a bearer token. `POST /auth/login`, `POST /assistant/ask`, `GET /health`, and the OAuth/discovery routes are open (the assistant is rate-limited instead). Service routes are named after the underlying Moodle function they proxy:

```
POST   /auth/login          # Authenticate → JWT
POST   /auth/logout         # Invalidate session

GET    /service/core_webservice_get_site_info                                 # User ID, name, site info
GET    /service/core_course_get_recent_courses                                # Recently accessed courses
GET    /service/core_course_get_enrolled_courses_by_timeline_classification   # Courses filtered by timeline
GET    /service/core_course_get_contents                                      # Course sections and files
GET    /service/core_calendar_get_action_events_by_timesort                   # Upcoming deadlines
GET    /service/core_calendar_get_action_events_by_course                     # Deadlines for a specific course
GET    /service/message_popup_get_popup_notifications                         # Popup notifications

POST   /assistant/ask       # Streaming docs assistant (Groq, open + rate-limited)
GET    /health              # Liveness check
/mcp/                       # FastMCP endpoint (Streamable HTTP, OAuth-protected)
```

Full reference: [nustdevkit.com](https://www.nustdevkit.com)

---

## MCP Server

The gateway is also a Model Context Protocol server, so AI assistants that support MCP (Claude Code, Claude Desktop, Cursor, etc.) can call the LMS as a set of tools.

- **Endpoint:** `https://api.nustdevkit.com/mcp/`
- **Transport:** Streamable HTTP
- **Auth:** OAuth 2.0 with PKCE — you log in once through a hosted page; the client never sees your credentials and obtains tokens automatically.

### Connecting (Claude Code example)

Add the server to your project's `.mcp.json` — no token needed, the client runs the OAuth flow for you:

```json
{
  "mcpServers": {
    "nust-lms": {
      "type": "http",
      "url": "https://api.nustdevkit.com/mcp/"
    }
  }
}
```

On first connect, the client opens a browser to the gateway's login page. Enter your NUST LMS credentials there; once it says "Authentication successful," return to the assistant and the tools are live.

### Available tools

| Tool | Returns |
|------|---------|
| `get_my_account` | User ID, name, and site info |
| `list_recent_courses` | Recently accessed courses |
| `list_courses_by_timeline` | Courses filtered by timeline (past / in-progress / future) |
| `list_course_contents` | Sections and files for a course |
| `list_upcoming_deadlines` | Upcoming deadlines across all courses |
| `list_course_deadlines` | Deadlines for a specific course |
| `list_popup_notifications` | Popup notifications |

### How auth works

The OAuth flow is **stateless** — for public PKCE clients, security rests on PKCE plus a loopback redirect, so the gateway stores no per-client records. The endpoints are: `/.well-known/oauth-authorization-server` (discovery), `/oauth/register` (dynamic client registration), `/oauth/authorize` (login page), and `/oauth/token` (code → token exchange). Tokens are verified at the MCP door by a custom `GatewayTokenVerifier`.

> **Note:** LMS sessions and OAuth tokens live in the server's memory (single worker). A redeploy or a session timing out means you re-authenticate — if a tool returns `401: Session expired`, just reconnect and log in again.

---

## Contributing

1. Fork the repo and create a branch off `main`.
2. Backend changes: edit under `ndk_backend/`, test locally with `uvicorn main:app --reload`.
3. Spec changes: edit `src/spec/openapi.yaml`, run `npm run sync`, commit both files.
4. Open a pull request — CI will run on merge.

---

## License

Copyright (c) 2026 Hasaan Hameed. All rights reserved. See [LICENSE](LICENSE) for details.
