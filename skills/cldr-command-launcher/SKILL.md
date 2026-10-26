---
name: cldr-command-launcher
description: A single dependency-free Rust binary that sits in the system tray, pops up on a hotkey, and routes whatever you type — maths, unit conversion, a path, an app, or a web search.
metadata:
  title: "CLDR — command launcher"
---

# CLDR — command launcher

CLDR (Command Line Dispatch & Route) is a single-binary command launcher for Windows and Linux. Bound to a hotkey it stays resident and summons a command window; type anything and it routes it to the right action — `[CALC]` for maths/unit conversion, `[OK]` to open a path, `[RUN]` to spawn an app, `[WEB]` for a search — and shows the result inline. No Electron, no Qt/GTK, no async runtime, no clipboard access.

## When to use

- You want a tiny resident launcher that does not pull in a GUI toolkit or an async runtime.
- You need a routing table from typed input to actions (calc, path, app, search).
- You want one binary that builds for both Windows and Linux in CI.

## Method

1. Write a single Rust binary (`Cargo.toml`) that creates a tray icon and registers a global hotkey; on press, show a small input window.
2. Route the typed string: try a maths/unit-conversion evaluator, then a filesystem path check, then a known app/command, then fall back to a web search (e.g. DuckDuckGo).
3. Avoid heavy dependencies on purpose — no Electron, no Qt/GTK, no async runtime, no clipboard access — to keep idle CPU near 0% and the binary small.
4. Build and release with `.github/workflows/build-release.yml` for Windows and Linux.
5. Document usage in `docs/USER_GUIDE.md`, `docs/SETUP_GUIDE.md` and `docs/SHORTCUTS.md`; ship the landing page in `docs/`.
6. Retain the attribution watermark required by the PolyForm Noncommercial + attribution licence.

## Key files / entry points

- `Cargo.toml`, `Cargo.lock`, `src/` — the single binary.
- `.github/workflows/build-release.yml`.
- `docs/USER_GUIDE.md`, `docs/SETUP_GUIDE.md`, `docs/SHORTCUTS.md`, `docs/index.html`.
- `assets/cldr-icon.svg`.

## Gotchas

- Global hotkeys and tray icons are platform-specific; keep the abstraction small and test both Windows and Linux.
- The licence requires the attribution notice to be retained in all copies — do not strip the watermark.
- Do not add a runtime 'just for convenience'; the design goals are no async runtime and near-zero idle CPU.

## Source projects

- [CLDR](https://github.com/drsamonline/CLDR) — Rust, MIT + attribution, Windows/Linux.

