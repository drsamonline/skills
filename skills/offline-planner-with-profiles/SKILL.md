---
name: offline-planner-with-profiles
description: Build an offline-first planner with day, week, month and year views, multiple PIN-locked profiles and zero networking code — a tool that feels local, ships as a PWA and a desktop release, and never phones home.
metadata:
  title: "Planner Pro"
---

# Planner Pro — a planner that behaves like a tool, not a website

Day, week, month and year planning in one quiet screen. Multi-profile, PIN-locked, no accounts, no
servers — and, unusually, **no networking code at all**: the promise is enforced by the absence of
a fetch, not by a policy.

## When to use

- The app is a personal tool and a server would only add a failure mode.
- Several people (or several contexts) share one device and each needs a locked profile.
- The claim "works offline" has to be structural — nothing to call, so nothing to fail.

## Method

1. Choose the smallest stack that still feels like an app: vanilla JS, ~210 KB, zero runtime dependencies.
2. Model the four time scales (day, week, month, year) over **one** store of dated items; each view is a projection, never its own data.
3. Lock each profile with a PIN and keep profiles separate at the storage key level, so unlocking one does not expose another.
4. Keep networking out of the codebase: no fetch, no analytics, no font CDN. The absence is the guarantee.
5. Ship both shapes — a PWA for the browser and a desktop release — from the same sources.
6. Keep e2e checks over the real views (122 at the time of writing); a planner breaks in the calendar arithmetic, not in the button styles.

## Key files / entry points

- The four views (day/week/month/year) over one dated-item store.
- The profile and PIN layer — one storage namespace per profile.
- The PWA manifest and the release build.

## Gotchas

- Month arithmetic is where planners break: a task on the 31st has no 31st in the next month, and "clamp or carry" is a decision you must make once.
- A PIN in a local app is a lock, not encryption — say which, especially in a multi-profile household.
- Profile isolation is a storage-key decision; a shared cache or a single JSON blob defeats it.

## Source projects

- [planner-pro](https://github.com/drsamonline/planner-pro)
