---
name: eon-commando
description: A retro run-and-gun platformer shipped as one self-contained HTML file: the source is concatenated by a build script, and the same page runs from Pages, an EXE, an APK or a LAN server.
metadata:
  title: "Eon Commando — assembled single-file game"
---

# Eon Commando — assembled single-file game

A run-and-gun platformer that ships as one HTML file. Unlike the hand-written single-file apps, this one is **assembled**: `build.py` concatenates `src/00_head.html` and the rest of the parts into `index.html`, so the source stays readable and the deliverable stays one file.

## When to use

- You want a single-file deliverable whose source is still split into readable parts.
- You are building a canvas game with generated (not bundled) audio.
- You need the same build to run from Pages, a portable EXE, an APK and a LAN host.

## Method

1. Keep the game in numbered parts under `src/` and assemble with `build.py` into `index.html`; never edit the assembled file.
2. Mirror the build into `docs/play/index.html` so Pages serves the same bytes that ship.
3. Ship `manifest.json` + `sw.js` for installability, and a `docs/demo/` copy for the landing page's embedded demo.
4. Offer the LAN route with `server/lan-host.js` — the same page served over the room's Wi-Fi — instead of inventing a second build for it.
5. Record what changed per version in `CHANGELOG.md` and the offline work in `OFFLINE-ENHANCEMENTS.md`; the README keeps a release-by-release list.
6. Release through `.github/workflows/build-apps.yml` (the shared caller), not a hand-written workflow.

## Key files / entry points

- `src/00_head.html` and the numbered parts; `build.py` — the assembler.
- `index.html` (built), `docs/play/index.html` (served).
- `server/lan-host.js` — the LAN route; `manifest.json`, `docs/play/sw.js`.
- `CHANGELOG.md`, `OFFLINE-ENHANCEMENTS.md`.

## Gotchas

- An assembled file is generated output — a fix made in `index.html` disappears on the next build.
- Two copies of the game (root and `docs/play/`) drift unless the build writes both.
- Chiptune generated at runtime keeps the file small; shipping audio files breaks the one-file promise.
- A `manifest.json` referencing icons that are not in the tree installs a blank tile.

## Source projects

- [eon-commando](https://github.com/drsamonline/eon-commando) — the `src/` + `build.py` assembly and the multi-target delivery.
