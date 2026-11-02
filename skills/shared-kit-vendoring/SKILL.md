---
name: shared-kit-vendoring
description: How the fleet ships a shared kit inside a no-build app: copy the kit file into the app, pin the version you copied, and know which copies have already drifted.
metadata:
  title: "Vendoring a shared kit into an app"
---

# Vendoring a shared kit into an app

A no-build single-file app cannot `npm install`, so a shared kit reaches it by **copying the kit file into the app** — `web-kit.js` beside `docs/play/index.html`, `export-kit.js` beside it, `lan-kit.js` in `public/`. That is a legitimate choice, but it is a pin, not an import, and the fleet already shows what happens when nobody writes the pin down: byte-identical copies in most apps and divergent copies in a few.

## When to use

- An app with no build step needs a kit the fleet already has.
- You are deciding where a kit file lives inside an app (`docs/play/`, `vendor/`, `public/`, `dist/`).
- You are auditing which apps are on which kit version.

## Method

1. Copy the kit's `*.js` from the kit repository, unchanged, into one place in the app: `docs/play/` for the served copy, `vendor/` when the app has several build outputs.
2. Record the kit version you copied — the kit's `VERSION` or the commit — in the app's README or `CHANGELOG.md`, beside the file.
3. Load the kit with a plain `<script>` before the app's own script; kits attach a global (`Loom` for `web-kit`, `Export`, `Lan`, `CryptoKit`, …) and also export for Node.
4. When the kit changes, re-copy deliberately and bump the recorded version in the same commit — never edit the vendored file to fix an app bug.
5. Audit drift by comparing the vendored file against the kit's file, not by reading the app; identical bytes are the only proof a copy is current.

## Key files / entry points

- The kit's own `*.js` and `VERSION` — the source of truth.
- The app's vendored copy (`docs/play/web-kit.js`, `vendor/export-kit.js`, `public/lan-kit.js`).
- The app's `CHANGELOG.md` — where the pin belongs.

## Gotchas

- A vendored copy is frozen: an app that copied `web-kit.js` before a fix keeps the bug, and nothing warns it.
- The same kit can be vendored at two paths in one app (`web-kit.js` and `docs/play/web-kit.js`); a fix applied to one is not a fix.
- Editing the vendored file to patch an app is how a kit forks silently — patch the kit and re-copy.
- A kit copied into `dist/` is generated output; copying into it by hand means the next build deletes the change.

## Source projects

- [web-kit](https://github.com/drsamonline/web-kit) — the runtime most apps vendor, loaded as `Loom`.
- [export-kit](https://github.com/drsamonline/export-kit) — vendored for save/ZIP/CSV.
- [lan-kit](https://github.com/drsamonline/lan-kit) — vendored for the LAN room client.
- [frame-kit](https://github.com/drsamonline/frame-kit) — vendored by the optical-transfer apps.
