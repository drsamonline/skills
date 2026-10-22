---
name: TTB — Tiny Toolbox browser extension
description: A Manifest V3 browser extension bundling 590 small utilities across 18 categories into one offline-first popup, with one source tree assembled per browser by a small build.
---

# TTB — Tiny Toolbox browser extension

TTB is a Manifest V3 extension that gathers 590 tiny utilities (text, calculations, developer helpers, page tools, data, design, finance, media, security, accessibility) into one fast, offline-first popup — Chrome, Edge, Firefox and Safari. One source tree is assembled per browser by `npm run build`; a tool that needs an API a browser does not provide is disabled and says so plainly instead of failing silently.

## When to use

- You want to add a small utility to a cross-browser extension rather than a new app.
- You need one codebase that targets Chrome, Firefox and Safari with a per-browser capability matrix.
- You want an offline-first popup with no remote code.

## Method

1. Keep one source tree; use `npm run build` to assemble a per-browser bundle (Manifest V3 for Chrome/Edge/Brave/Opera/Vivaldi; `sidebar_action` for Firefox; converted with Xcode for Safari). Per-browser config lives in `browsers/*.json`.
2. Register the 590 tools with metadata (id, name, category, required browser APIs) so the catalogue and the disable-when-unsupported logic are data-driven (`ALL_TOOLS.md`).
3. When a required API is missing, disable the tool and show why — never fail silently.
4. Use the side panel (`side_panel` / `sidebar_action`) where available; gate History/bookmarks/downloads/cache/font-list tools to browsers that expose them.
5. Validate on every push with `.github/workflows/validate.yml`; keep a `BROWSER_SUPPORT.md` capability matrix.
6. No framework, no telemetry, no remote code — every tool is pure client-side computation.
7. Capture real screenshots from headless Chrome for the docs.

## Key files / entry points

- `manifest.json`, `background.js` — the MV3 shell.
- `browsers/chrome.json` (and siblings) — per-browser config consumed by the build.
- `ALL_TOOLS.md` — the catalogue; `BROWSER_SUPPORT.md` — the capability matrix.
- `.github/workflows/validate.yml`.

## Gotchas

- Safari does not expose history/bookmarks/downloads; those tools must disable cleanly there.
- MV3 forbids remote code — keep everything bundled and offline.
- Firefox packaging differs (temporary add-on / AMO signing), so the build must emit a Firefox-specific manifest.
- Keep the popup light: 590 tools must stay lazy so the popup opens instantly.

## Source projects

- [TTB](https://github.com/drsamonline/TTB) — 590 tools, 18 categories, Manifest V3, MIT.

