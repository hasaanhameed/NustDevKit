# NUST LMS API — Developer Guide

This guide is the hand-written companion to the OpenAPI spec. The spec lists the exact
parameters and response shapes; this guide explains the flows, the gotchas, and how the
pieces fit together.

## What this API is

A REST gateway over the NUST LMS (Moodle). You authenticate once with your NUST LMS
username and password, get a **bearer token**, and call clean REST endpoints. The gateway
logs into Moodle on your behalf and manages the underlying session server-side, so you
never deal with Moodle's `sesskey` or cookies.

- **Base URL (local dev):** `http://127.0.0.1:8000`
- The API is **read-only** and scoped to **your own** account. There is no endpoint to
  modify data or to look up other users.

## Authentication flow (do this first)

1. `POST /auth/login` with JSON `{ "username": "...", "password": "..." }` (your NUST LMS
   credentials). Username looks like `johndoe.bscs23seecs`.
2. The response is `{ "access_token": "<JWT>", "token_type": "bearer" }`.
3. Send that token on **every** other request as the header
   `Authorization: Bearer <access_token>`.

The token represents a live LMS session held in memory on the gateway. If the gateway
restarts or the session expires, you get a `401` — just log in again.

## Finding your own user ID

Some endpoints need your numeric Moodle **user ID** (e.g. popup notifications wants it as
`useridto`). Get it from:

- `GET /service/core_webservice_get_site_info` → returns `userid`, `fullname`, `username`,
  profile picture, and site info.

So the chain for notifications is: **site-info → take `userid` → pass it as `useridto`**.

## The endpoints at a glance

- **Courses**
  - `GET /service/core_course_get_recent_courses?limit=10` — your recently accessed courses.
  - `GET /service/core_course_get_enrolled_courses_by_timeline_classification?offset=0&limit=50&classification=inprogress&sort=fullname`
    — your enrolled courses, filtered by timeline.
  - `GET /service/core_course_get_contents?courseid=<id>` — everything posted in a course:
    sections (weeks/topics) → modules (files, pages, URLs, assignments) → file metadata.
- **Calendar / deadlines** (Moodle "action events" = assignment/quiz/lab due dates)
  - `GET /service/core_calendar_get_action_events_by_timesort?limitnum=20&timesortfrom=0`
    — upcoming deadlines across all courses.
  - `GET /service/core_calendar_get_action_events_by_course?courseid=<id>` — one course's deadlines.
- **Account**
  - `GET /service/core_webservice_get_site_info` — your identity + site info.
- **Notifications**
  - `GET /service/message_popup_get_popup_notifications?useridto=<your-userid>&limit=20&offset=0`
    — your bell notifications (graded, replies, reminders) and unread count.

## Parameter gotchas

- **`timesortfrom` / `timesortto` are Unix timestamps in seconds.** Pass `0` for
  `timesortfrom` to mean "no lower bound" (all events). To see only *upcoming* deadlines,
  pass the current epoch time (`int(time.time())` in Python, `Math.floor(Date.now()/1000)`
  in JS).
- **`classification`** (enrolled courses) is one of:
  `all`, `inprogress`, `past`, `future`, `favourites`, `hidden`, `allincludinghidden`.
  Note it is `favourites` (British spelling), not `favourite`.
- **`sort`** (enrolled courses) is one of: `fullname`, `shortname`, `id`, `idnumber`, `timeaccess`.
- **`useridto`** (popup notifications) is passed as a **string**, and it is *your own*
  user ID (from site-info).
- **Course-content file URLs** point at Moodle's `pluginfile.php`. They are not publicly
  fetchable — downloading the bytes needs the session/token. The file names and metadata
  come back directly; downloading is a separate authenticated request.

## Common recipes

- **"What's posted in my course X?"** → `core_course_get_recent_courses` (or enrolled
  courses) to find the `courseid`, then `core_course_get_contents?courseid=...`.
- **"My deadlines this week"** → `core_calendar_get_action_events_by_timesort` with
  `timesortfrom` = now (epoch seconds).
- **"My notifications"** → `core_webservice_get_site_info` for `userid`, then
  `message_popup_get_popup_notifications?useridto=<userid>`.

## SDKs

Per-language SDKs (TypeScript, Python, Java, .NET/C#, Go, PHP, Ruby) are generated from
this spec and downloadable from the docs portal. Workflow: download the zip for your
language, install it, get a token from `POST /auth/login`, initialize the client with that
token, then call the methods (each maps to one endpoint above). The per-language SDK docs
included alongside this guide show the exact method names and example usage.

## AI assistants (MCP)

The same API is exposed as an **MCP server** at `/mcp/` (Streamable HTTP transport), so AI
assistants can call it as tools. It is protected by **OAuth 2.0 with PKCE** — you do NOT
paste a bearer token. Instead, add the server URL (`https://api.nustdevkit.com/mcp/`) to your
MCP client; on first connect the client opens a hosted login page where you enter your NUST
LMS credentials, and it obtains its tokens automatically (the assistant never sees your
password). Desktop clients (Claude Code, Claude Desktop, Cursor, VS Code) use a config entry
with `"type": "http"` and the URL; web assistants (Claude.ai, ChatGPT) add it as a custom
connector with the same URL. Login/logout are never MCP tools — authentication is handled by
the OAuth flow. The available tools are read-only: account info, recent courses, courses by
timeline, course contents, upcoming deadlines, course deadlines, and popup notifications.

## Boundaries (what NOT to claim)

- No write/update/delete operations — the API is read-only.
- No lookup of other users' data — everything is scoped to the authenticated user.
- If a question asks for something not covered by the spec or this guide, say you're not
  sure rather than inventing an endpoint, parameter, or field.
