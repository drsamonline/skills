---
name: lumen
description: Structure a local-first photo library so the engine is testable without a render surface: Flutter for the UI, Riverpod for state, SQLite for the index, and a core layer that never imports a widget.
metadata:
  title: "Lumen"
---

# Lumen — an offline photo library with a strictly one-directional core

A photo library that never phones home: it reads folders you already keep, indexes them, and computes thumbnails, edits, faces, albums and duplicates on your machine. The reusable part is the layer discipline.

## When to use

- You are writing a Flutter app whose real work is a data engine — indexing, thumbnails, a database — and you want that work testable without pumping widgets.
- The app must be offline by construction, not by policy.
- You want a LAN view of local data without a cloud service.

## Method

1. Keep three layers, strictly one-directional: **`ui -> state -> core`**. Nothing in `core` imports Flutter widgets, which is what lets `test/db_test.dart` exercise the engine with no render surface.
2. Put the platform glue in `lib/main.dart` (including SQLite factory selection) and `lib/app.dart` (theme, first-run routing), not in `core`.
3. In `core`, one directory per concern: `models/` (Photo, Album, Person, Face, EditRecipe), `db/` (AppDatabase plus one DAO per aggregate), `scan/` (EXIF reader, scanner, thumbnails, watcher, exporter), `lan/` (HttpServer, web gallery page, UDP beacon), `app_paths.dart` (one writable directory, thumb sharding), `settings.dart` (behaviour, not data).
4. Make rescans incremental: a file whose size and mtime are unchanged is never re-opened, so rescanning a large library after adding one folder takes seconds.
5. Serve the LAN gallery from the app's own `HttpServer` with a UDP beacon for discovery — no external service, no account.

## Key files / entry points

- `lib/core/` — the engine (models, db, scan, lan).
- `lib/state/` — Riverpod providers and ChangeNotifier controllers.
- `lib/ui/` — screens and widgets only.
- `ARCHITECTURE.md` — the layering rule, written down.
- `test/` — engine tests that need no widgets.

## Gotchas

- One import of a Flutter widget from `core` is enough to make the engine untestable; the rule only works if it is absolute.
- Settings and data are different things: behaviour belongs in `SharedPreferences`, the library belongs in SQLite.
- Thumbnail sharding in `app_paths.dart` exists because a single directory with tens of thousands of thumbs is a slow directory.
- A rescan that re-reads every file defeats the point of an incremental index — compare size and mtime first.

## Source projects

- [lumen](https://github.com/drsamonline/lumen) — the three-layer split, the incremental scanner and the LAN gallery.
