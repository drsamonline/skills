---
name: hms-hospital-management
description: HHMS: a LAN-based hospital management system for homeopathic hospitals — a Python server owns the SQLite database, a WebView2 client talks HTTP/JSON, and the server is found by UDP discovery; no internet, no cloud.
metadata:
  title: "HMS — Homeopathic Hospital Management System"
---

# HMS — Homeopathic Hospital Management System

HHMS is a LAN-based hospital management system purpose-built for homeopathic hospitals and clinics. `HHMS-Client.exe` (a WebView2 UI) talks HTTP/JSON over the LAN to `HHMS-Server.exe`, which is the only component that touches the shared SQLite database. It covers clinical (registration, OPD queue, case records, ICD-11, prescriptions, IPD/beds, investigations, annual rollover), operational (billing, pharmacy stock ledger, procurement, masters, dashboards) and reporting/printing (statistics, 16 print envelopes, PDF, scheduling) — with 566 backend tests passing.

## When to use

- You are building a multi-user system that must run on a hospital LAN with no internet.
- You want the reference for the server-owned-database + WebView2-client architecture.
- You need UDP LAN discovery, Alembic migrations and dual-platform release packaging.

## Method

1. Server: FastAPI + uvicorn with SQLAlchemy (async) over SQLite; only the server opens the database. Run Alembic migrations at startup and bootstrap a default admin on first run (disable via env in production).
2. Seed a full demo dataset automatically on a pristine database (opt out with an env var); never touch an install that already holds real data.
3. Provide a `--smoke-test` mode that bootstraps in-process, serves briefly and probes `/health`, so CI validates a built binary without a manual start.
4. LAN discovery over UDP port 38541; the client broadcasts to find the server and remembers the last good host (same-origin auto-connect).
5. Client: a native Windows WebView2 shell loading the HTML/CSS/vanilla-JS UI; the server serves the GUI at `/` and the JSON API.
6. Harden auth: JWT, login rate limiting, secret-key rotation runbook, audit logs.
7. Package single-file server binaries (Windows/Linux) + Inno/NSIS installers and release them with the tag-driven pipeline (test gate → dual-platform build → checksums → one release; rolling `nightly` + permanent `v*.*.*`).
8. Keep governance in `.ai/` (constitution, coding rules, decisions, state) and document everything under `docs/` (master spec, DB entities/schema, API spec, security, UI/print standards, testing, deployment).

## Key files / entry points

- `backend/app/server.py`, `backend/app/network/discovery.py`, `backend/app/api/v1/endpoints/*`, `backend/alembic/versions/*`.
- `frontend/` (UI), `client/` (WebView2 host), `docs/` (specifications), `.ai/` (governance).
- `scripts/deploy/build-server.sh`, `build-installer.ps1`.
- `.github/workflows/release.yml`.

## Gotchas

- One writer: clients must never open the SQLite file directly — all access goes through the server API.
- Seed demo data only on a pristine DB and behind a flag; a bad seed on a real install is unrecoverable.
- There is no hosted web demo for a LAN app — seed demo data on first run instead.
- The licence is proprietary (EULA); personal use free, commercial/non-profit use needs written permission.
- Migrations must be idempotent and safe on operator machines; a failed startup migration is the worst failure.

## Source projects

- [HMS](https://github.com/drsamonline/HMS) — proprietary EULA v1.0, 566 backend tests, v0.0.1.

