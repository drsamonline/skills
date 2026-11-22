---
name: album-music-page
description: Build an album-wise music page that hosts no audio at all: a generated manifest points every track at the platform that hosts it, the page plays through that platform's own player, and adding a track is one line in a link list plus a rebuild.
metadata:
  title: "Music page"
---

# Music page — a manifest-driven album shelf

An album-wise music page served from Pages. Audio is **not** hosted in the repository: each track
points at the platform that hosts it (SoundCloud, Suno, Flow Music, Newgrounds, Freesound) and the
page plays it through that platform's own player, or opens a new tab where no player page exists.

## When to use

- The media is too large, or too encumbered, to host — but you still want one page that presents it well.
- Tracks arrive from several platforms and you want one shelf rather than five embeds.
- The catalogue changes often enough that hand-editing the page would rot.

## Method

1. Keep three layers apart: `sources/seed.json` (the crawled catalogue: profiles, tracks, licences, duplicates, takes), `sources/<platform>.links.txt` (one URL per line), and `data/tracks.json` (the generated manifest the page reads).
2. Never hand-edit the generated manifest; `tools/build_manifest.py` turns seed + link lists into it, and the workflow runs that on every push.
3. Split the CI into **rebuild** and **deploy**: `rebuild.yml` regenerates the manifest, `deploy.yml` publishes. One job that does both hides a broken rebuild behind a successful deploy.
4. Record the licence and the duplicate decision in the seed, so a track that exists on two platforms is one entry with two links.
5. Where a platform has no embeddable player, link out in a new tab — do not fake a player.

## Key files / entry points

- `data/tracks.json` — the manifest (generated).
- `sources/seed.json`, `sources/*.links.txt` — the inputs.
- `tools/build_manifest.py` — seed + links -> manifest.
- `.github/workflows/` — rebuild on push, deploy to Pages.

## Gotchas

- Adding a track is three steps (link list, re-crawl or paste the row, push) and skipping the middle one leaves the page stale while CI stays green.
- A crawl is a snapshot: a deleted track on the platform stays on the page until the seed is re-crawled.
- Embeds load third-party code; a page that promises "no tracking" cannot quietly embed five players without saying so.

## Source projects

- [music](https://github.com/drsamonline/music)
