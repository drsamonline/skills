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
5. Audit drift by **structure, not bytes**. Ask which names the kit exposes, which the copy exposes, and which the app actually calls — a copy that differs only in a lint header (`/* global module */` vs `/* global module, btoa, atob */`) is not out of date, and `forge`'s `tools/kit-drift.py` was written because a byte check reported nine good copies as drift.
6. Read the verdict in the fleet's own vocabulary: **BROKEN** (the copy is missing a name the app calls — fix it), **HARVEST** (the copy exposes a name the kit does not — the kit is behind the app, so the instruction is to the kit), **STALE** (an older generation the app does not call — report, do not touch).

## Key files / entry points

- The kit's own `*.js` and `VERSION` — the source of truth.
- The app's vendored copy (`docs/play/web-kit.js`, `vendor/export-kit.js`, `public/lan-kit.js`).
- The app's `CHANGELOG.md` — where the pin belongs.
- `forge`'s `tools/kit-drift.py` and `registry/drift.json` — the fleet's own drift measurement (71 copies: 59 in sync, 8 cosmetic, 3 stale, 1 harvest, on the 2026-11-16 run).
- `forge`'s `tools/kit-audit.py` and `registry/audit.json` — the signal scan: 86 repos scanned, 111 hand-rolled patterns a kit exists to replace (76 web-kit, 22 export-kit, 6 compress-kit, 5 crypto-kit, 2 srs-kit).

## Gotchas

- **A vendored copy is frozen, and that is allowed.** The owner's ruling is that a working app is never changed to match its kit — not by a refresh, not by a copy-over (`PROMPTS/retrofit.md` in `forge`). A stale copy is a reason to update the **kit**; failing a build for it would fail it for something no legal action can fix, every week, forever.
- **A version label is not a version.** Measured 2026-11-16: `case-kit.js` is vendored in `app-encrypted-case-log` and `app-thermals` at v0.2.0 and in `case-kit` at v0.2.0 — three files, two different builds, same label. Compare structure, never the number alone.
- **One kit can be two generations in the fleet.** `export-kit.js` is vendored in 12 repos; 15 copies are v1.0.0 while the kit repository itself is v2.0.0. `web-kit.js` is in 25 repos in three distinct builds. `lan-kit.js` is in 4 repos in 4 different builds (v0.1.0, v0.2.0, v1.1.0 and the kit's own v1.1.0).
- **A kit may have absorbed another kit.** `frame-kit` absorbed `optical-kit` and `tokens-kit` absorbed `motion-kit` on 2026-11-12 — a vendored `optical-kit.js` or `motion-kit.js` is a different file, not an older version of the surviving kit.
- The same kit can be vendored at two paths in one app (`web-kit.js` and `docs/play/web-kit.js`); a fix applied to one is not a fix.
- Editing the vendored file to patch an app is how a kit forks silently — patch the kit and re-copy.
- A kit copied into `dist/` is generated output; copying into it by hand means the next build deletes the change.

## Source projects

- [web-kit](https://github.com/drsamonline/web-kit) — the runtime most apps vendor, loaded as `Loom`.
- [export-kit](https://github.com/drsamonline/export-kit) — vendored for save/ZIP/CSV.
- [lan-kit](https://github.com/drsamonline/lan-kit) — vendored for the LAN room client.
- [frame-kit](https://github.com/drsamonline/frame-kit) — vendored by the optical-transfer apps.
