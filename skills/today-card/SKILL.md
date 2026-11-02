---
name: today-card
description: A minimal single-page daily card: the date, one intention, one task and a streak, stored locally, shipped as one HTML file on top of the shared runtime.
metadata:
  title: "Today Card — one card for the day"
---

# Today Card — one card for the day

The smallest app in the fleet, and deliberately so: one card showing the date, one intention, one task and a streak. It is built on the shared `web-kit` runtime and shipped as `docs/app.html`, which makes it the clearest example of how little an app needs to be when the runtime is already there.

## When to use

- You want the minimum viable offline app: one screen, local storage, no accounts.
- You need a worked example of `web-kit` carrying storage and export so the app itself is a few hundred lines.
- You are prototyping a daily-habit surface before committing to a bigger build.

## Method

1. Put the whole app in `docs/app.html` and vendor `web-kit.js` beside it as `docs/web-kit.js`.
2. Store the day's card keyed by date, so a new day starts empty without a migration step.
3. Compute the streak from the stored dates rather than keeping a counter — a counter drifts the first time a day is skipped.
4. Serve the landing page from `docs/index.html` and release through `.github/workflows/build-apps.yml`, which also produces the EXE and APK.
5. Keep the file small enough to read in one sitting; that is the product.

## Key files / entry points

- `docs/app.html` — the app.
- `docs/web-kit.js` — the vendored runtime.
- `docs/index.html` — landing page; `.github/workflows/build-apps.yml` — releases.

## Gotchas

- A streak counter stored as a number cannot survive a missed day without a repair rule; derive it from the dates.
- A date key must be the user's local date, not UTC, or the card turns over at the wrong hour.
- Vendoring `web-kit.js` means the app freezes that version — re-copy deliberately when the kit changes.
- One screen is a constraint worth keeping: the second field is the beginning of a different app.

## Source projects

- [today-card](https://github.com/drsamonline/today-card) — the minimal app-over-`web-kit` shape.
