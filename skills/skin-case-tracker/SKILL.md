---
name: Skin Case Tracker
description: A private, offline PWA that tracks a skin case over time on the HHMS model — History, Habits, Mapping, Symptoms logged daily and read as a 90-day pattern engine; it records, it does not diagnose.
---

# Skin Case Tracker

HHMS Skin-Case Tracker is a private, offline browser app for tracking a skin case over time, built on the book's **HHMS** dashboard: History, Habits, Mapping and Symptoms logged day by day and read as a 90-day pattern engine. The companion app to *The Skin Is a Liar*. It records; it does not diagnose. Data stays on the device.

## When to use

- You are building a privacy-first longitudinal health tracker with a pattern view.
- You want the HHMS (History/Habits/Mapping/Symptoms) capture model.
- You need a single-file PWA with local-only storage.

## Method

1. Keep the app single-file, offline, PWA-installable; publish at `docs/play/` and a landing page at `docs/index.html`.
2. Capture four streams — History, Habits, Mapping, Symptoms — with fast daily logging.
3. Compute a 90-day pattern view over the logged data; keep it descriptive (patterns, not diagnoses).
4. Store everything on-device; offer export/import so the user owns the record.
5. Use the shared badges and state the privacy stance prominently; version in `docs/badges/version.svg`.
6. Build EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/index.html` — the app; `docs/index.html` — landing page.
- `docs/badges/*.svg` — live demo, privacy, version, licence badges.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Record, do not diagnose — never surface a condition name as a conclusion.
- Health data must stay local; no telemetry, no sync, no account.
- A 90-day pattern needs consistent daily capture; design for a 10-second entry.
- Keep the medical disclaimer and the book attribution.

## Source projects

- [skin-case-tracker](https://github.com/drsamonline/skin-case-tracker) — v7.0, free to use, all rights reserved.

