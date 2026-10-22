---
name: LAN single-server architecture
description: A multi-user system that runs entirely on a hospital LAN: a Python server owns the SQLite database, a vanilla-JS UI runs in a WebView2 client, and the server is discovered by UDP broadcast — no internet, no cloud.
---

# LAN single-server architecture

HMS (HHMS) is a hospital management system that runs on the local network with a **server-owned database**. Architecture: `HHMS-Client.exe` (a WebView2 UI) talks HTTP/JSON over the LAN to `HHMS-Server.exe`, which is the only component that touches the shared SQLite database. There is no internet dependency and no cloud lock-in. The server runs migrations on boot, seeds a demo dataset on a pristine database, and advertises itself on the LAN over UDP (port 38541) so clients can auto-discover it.

## When to use

- Multiple workstations must share one dataset on a network with no (or unreliable) internet.
- A single machine should own the data and be the only writer, avoiding sync conflicts.
- You need a client that feels native on Windows but is built from the web stack.

## Method

1. Server: a Python ASGI app (FastAPI + uvicorn) with SQLAlchemy (async) over SQLite (`aiosqlite`; `asyncpg` optional). Only the server opens the database; clients never touch it.
2. Schema changes are **Alembic migrations**, numbered and committed (`0001_…`, `0002_…`). The server runs migrations automatically at startup so an install upgrades itself.
3. Startup bootstrap: create the default admin on first run (disable via an env flag in production), and seed a full demo dataset **only when the database is pristine** — opt out with an env var. Provide a `--smoke-test` mode that bootstraps in-process, serves briefly and probes `/health`, so CI can validate a freshly built bundle.
4. Discovery: the server listens for/dispatches UDP discovery on a fixed port (38541); the client broadcasts to find the server and stores the chosen host for next launch (same-origin auto-connect).
5. Transport: plain HTTP/JSON over the LAN. Keep it simple — no TLS needed inside a trusted LAN, but do harden auth (JWT, login rate limiting, secret-key rotation).
6. Client: a native Windows WebView2 shell that loads the HTML/CSS/vanilla-JS UI; the UI is served by the server at `/` (or from local files) and calls the JSON API.
7. Packaging: build single-file server binaries for Windows and Linux (PyInstaller) plus Inno/NSIS installers, and publish them with a tag-driven release pipeline (test gate → dual-platform build → checksums → one release; a rolling `nightly` prerelease plus permanent `vX.Y.Z` tags).
8. Test the LAN path explicitly: multi-client LAN tests, clean-install simulation, client startup/restore, and installer CI QA — these are what catch discovery and migration regressions.
9. Keep governance files in the repo (`.ai/` project constitution, coding rules, decisions, state) so long-running work stays coherent across sessions.

## Key files / entry points

- `backend/app/server.py` — standalone launcher (migrations, admin bootstrap, demo seed, uvicorn, `--smoke-test`).
- `backend/app/network/discovery.py` — LAN discovery (UDP 38541).
- `backend/app/api/v1/endpoints/*` — API routers; `backend/app/models`, `backend/app/services`.
- `backend/alembic/versions/*` — numbered migrations.
- `frontend/` — HTML/CSS/vanilla-JS client UI; `client/` — the WebView2 Windows host.
- `scripts/deploy/build-server.sh`, `build-installer.ps1` — server bundle + installer builds.
- `.github/workflows/release.yml` — test gate → dual-platform build → checksums → release.
- `.ai/PROJECT_CONSTITUTION.md`, `CODING_RULES.md`, `DECISIONS.md` — project governance.

## Gotchas

- One writer: never let a client open the SQLite file directly — all access goes through the server API or you get corruption.
- Run migrations at startup and make them idempotent; a failed migration on an operator's machine is the worst failure mode.
- Seed demo data only on a pristine database and behind a flag; never touch an install that already holds real data.
- Discovery must be robust to multiple subnets and to a server that has not started yet — cache the last good host and allow manual entry.
- `/health` plus a smoke-test path lets CI validate a built binary without a manual start-and-poll cycle.
- There is no hosted demo for a LAN app — seed a demo dataset on first run instead of promising a web demo.

## Source projects

- [HMS](https://github.com/drsamonline/HMS) — HHMS, the LAN hospital management system (FastAPI + SQLite + WebView2 client, UDP discovery, Inno/NSIS installers, 566 backend tests).

