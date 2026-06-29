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
| **MCP Server** | Self-hosted FastMCP server at `/mcp`. Lets AI assistants (Claude, Cursor, ChatGPT) call LMS data as tools. |
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
│   │   ├── routes/           # auth, service endpoints, assistant
│   │   ├── services/         # LMSSession (httpx client), session store
│   │   ├── schemas/          # Pydantic request/response models
│   │   ├── dependencies/     # FastAPI dependencies (auth resolution)
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
├── scripts/                  # Build scripts
│   ├── sync-spec.mjs         # Copies spec + assets to ndk_frontend/
│   └── inject-code-samples.mjs  # Injects SDK/MCP code samples into spec
│
└── .github/workflows/
    ├── deploy-backend.yml    # Build → push to ECR → redeploy on EC2
    └── deploy-frontend.yml   # Sync ndk_frontend/ to S3 + invalidate CloudFront
```

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

All endpoints (except `POST /auth/login` and `GET /health`) require a bearer token.

```
POST   /auth/login          # Authenticate → JWT
POST   /auth/logout         # Invalidate session

GET    /service/account/site-info          # User ID, name, site info
GET    /service/courses/recent             # Recently accessed courses
GET    /service/courses/by-timeline        # Courses filtered by timeline
GET    /service/courses/{id}/contents      # Course sections and files
GET    /service/calendar/upcoming          # Upcoming deadlines
GET    /service/calendar/course/{id}       # Deadlines for a specific course
GET    /service/notifications/site         # Site notifications
GET    /service/notifications/popup        # Popup notifications

POST   /assistant/ask       # Streaming docs assistant (Groq)
GET    /health              # Liveness check
/mcp                        # FastMCP endpoint (SSE)
```

Full reference: [nustdevkit.com](https://www.nustdevkit.com)

---

## MCP Server

The gateway is also a Model Context Protocol server. AI assistants that support MCP can call it as a set of tools:

```json
{
  "mcpServers": {
    "nust-lms": {
      "url": "https://api.nustdevkit.com/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

Available tools: `get_account_info`, `list_recent_courses`, `list_courses_by_timeline`, `list_upcoming_deadlines`, `list_course_deadlines`, `get_site_notifications`, `list_popup_notifications`.

---

## Contributing

1. Fork the repo and create a branch off `main`.
2. Backend changes: edit under `ndk_backend/`, test locally with `uvicorn main:app --reload`.
3. Spec changes: edit `src/spec/openapi.yaml`, run `npm run sync`, commit both files.
4. Open a pull request — CI will run on merge.

---

## License

Copyright (c) 2026 Hasaan Hameed. All rights reserved. See [LICENSE](LICENSE) for details.
