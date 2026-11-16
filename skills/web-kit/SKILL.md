---
name: web-kit
description: The one-file runtime every offline app in the fleet kept re-writing: namespaced localStorage plus a small IndexedDB wrapper, English/Hindi/Gujarati strings, CSV out, light/dark tokens, focus trap and announcements, PWA registration, SEO meta and JSON-LD, and a DOM helper — as a single global `Loom`, working from file:// as well as Pages.
metadata:
  title: "Web kit — the shared offline-first runtime"
---

# Web kit — the shared offline-first runtime

Every single-file app in the fleet was re-implementing the same eight things. This kit is that
code once: one dependency-free file that attaches a `Loom` global with `storage`, `i18n`, `csv`,
`theme`, `a11y`, `pwa`, `seo` and `ui`. It makes no network call and needs no build step.

## When to use

- An offline app needs to persist settings or records and you are about to write another `localStorage` wrapper.
- The app must speak more than one language — English, Hindi and Gujarati ship in the kit.
- You need CSV export, a light/dark switch, a focus trap, an announcement for screen readers, a service-worker registration or SEO meta/JSON-LD, and you want one file rather than five.

## Method

1. Drop `web-kit.js` beside `index.html` and load it with a plain `<script src>`; for a truly single-file app, inline the whole file in a `<script>` block. It also exports for Node.
2. Start the theme before first paint with `Loom.theme.apply()`, and switch with `Loom.theme.set(mode)` / `Loom.theme.toggle()`.
3. Persist with `Loom.storage.get(name, fallback)` / `set(name, value)` — JSON-safe and namespaced under `loom:` — and move large blobs to the IndexedDB side with `put(db, store, k, v)`, `getItem(...)`, `all(db, store)`.
4. Read strings through `Loom.i18n.t(key)`, add a language with `setLang`, and extend the dictionary with `Loom.extend`/`Loom.i18n.extend` rather than editing the kit.
5. Export tables with `Loom.csv.toCSV(rows)` and `Loom.csv.download(name, text)`.
6. Use `Loom.a11y.trapFocus(el)` in every dialog and `Loom.a11y.announce(msg)` for anything that changes without focus moving.
7. Register the service worker through `Loom.pwa.register(sw)` and set the address-bar colour with `Loom.pwa.themeColor(color)`; write the head with `Loom.seo.title/description/jsonld`.
8. Build DOM with `Loom.ui.el(tag, props, children)` instead of string concatenation.
9. Verify with `node test-node.js`; the worked example is `demo/index.html` and the assertion page is `test/index.html`.

## Key files / entry points

- `web-kit.js` — the whole kit; `Loom.storage` (13), `Loom.i18n` (86), `Loom.csv` (106), `Loom.theme` (180), `Loom.a11y` (201), `Loom.pwa` (229), `Loom.seo` (245), `Loom.ui` (263).
- `docs/API.md` — the call-by-call reference.
- `demo/index.html` — a working mini-app: counter, theme toggle, language switch, CSV export.
- `test/index.html`, `test-node.js` — the assertion pages.
- `design.css`, `DESIGN.md` — the visual layer the tokens feed.
- `VERSION` — the version a vendored copy should be pinned to.

## Gotchas

- **The storage prefix is fixed at `loom:`.** An app that already saves under its own prefix cannot adopt this store without orphaning what its users saved — every read would miss. Adopt on a new app, or migrate deliberately.
- **A stale vendored copy is a reason to update the kit, never to rewire the app.** Kits in this fleet are one-way (`PROMPTS/retrofit.md` in `forge`); a working app is not changed to match its kit.
- **A drift report that lists extra names `del` and `dicts` is not a defect.** `del` was renamed `remove` and `dicts` was an internal of an older i18n; that copy is simply an earlier generation.
- **Read the copy in front of you.** Measured 2026-11-16 across 138 checkouts, `web-kit.js` is vendored in 25 repos in three distinct builds, so the API you have may be older than this file.
- **`Loom.theme.apply()` must run before the first paint** or the page flashes the wrong mode.

## Source projects

- [web-kit](https://github.com/drsamonline/web-kit) — the kit itself, its API, demo and tests.
- [app-jacquard](https://github.com/drsamonline/app-jacquard), [app-clip-loom](https://github.com/drsamonline/app-clip-loom), [app-endpoints](https://github.com/drsamonline/app-endpoints), [base-bench](https://github.com/drsamonline/base-bench), [conqueror-os](https://github.com/drsamonline/conqueror-os) — vendored copies that show the adoption shape.
