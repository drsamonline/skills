---
name: All4ONE — portable Windows utility suite
description: 551 Windows tools across 45 plugin packs compiled into one portable utility_suite.exe (Python, tkinter GUI + CLI), with lazy metadata-registered handlers and an audit that verifies every tool.
---

# All4ONE — portable Windows utility suite

Utility Suite is a free, portable Windows toolbox: file ops, hashing, PDF/Office batch, image/audio/video, network diagnostics, registry helpers, disk cleaning and security audits — 551 tools across 45 plugin packs, shipped as a single `utility_suite.exe` you can keep on a USB stick. Zero installs, zero telemetry, MIT licensed, with a tkinter GUI and a CLI over one engine.

## When to use

- You want to add a Windows utility to a large, well-organised portable toolkit rather than a new repo.
- You need a pattern for lazily-loaded, metadata-registered tools that degrade gracefully when an optional dependency is missing.
- You want to ship a big Python app as one unsigned portable EXE built in CI.

## Method

1. Organise tools into domain packages (`archive_tools/`, `audio_tools/`, `…`), each exporting handlers. Register every tool with metadata (id, name, category, declared optional dependencies) so the catalogue is data-driven (`TOOL_CATALOG.md` mirrors it).
2. Load tool implementations lazily: import on demand so start-up stays fast and a missing optional dependency disables exactly one tool, never the suite.
3. Expose two frontends over one engine — a tkinter GUI and a CLI — so scripting and clicking share the same handlers.
4. Verify the registry with `audit.py`, which checks that every declared tool has a working handler (551/551 on each release).
5. Build the single-file EXE in CI: `.github/workflows/build-windows-exe.yml` (PyInstaller on `windows-latest`); `.github/workflows/ci.yml` runs Linux-side validation on every push.
6. Version in `VERSION.txt` and document in `USER_GUIDE.md`, `DEVELOPER_GUIDE.md`, `INSTALLATION.md`, `COMPILATION.md`, `EXPANSION_CATALOG.md`.
7. Release the EXE through GitHub Releases so users download one portable binary; the toolkit needs no internet at runtime.

## Key files / entry points

- `utility_suite` entry points and the domain packages (`archive_tools/`, `audio_tools/`, …).
- `audit.py` — registry verification.
- `TOOL_CATALOG.md` — the generated catalogue of all 551 tools.
- `.github/workflows/build-windows-exe.yml`, `.github/workflows/ci.yml`.
- `VERSION.txt`, `CHANGELOG.md`, `USER_GUIDE.md`, `DEVELOPER_GUIDE.md`.

## Gotchas

- The EXE is unsigned — SmartScreen will warn on first run. Document 'More info → Run anyway'.
- A missing optional dependency must disable one tool, not crash the suite; that graceful degradation is the whole point of the metadata registry.
- Keep the Linux CI validation meaningful even though the artefact is Windows-only — it catches handler regressions cheaply.
- Zero telemetry and no background services are promises in the README; do not add an updater that phones home.

## Source projects

- [All4ONE](https://github.com/drsamonline/All4ONE) — the utility suite repo (v3.0.6, 551 tools, 45 packs).

