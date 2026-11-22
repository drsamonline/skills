---
name: cobble-a-city-from-small-things
description: Turn a personal journal into something you can walk through: each saved moment becomes a building, colour encodes what kind of moment it was and height encodes how much it mattered, offline and private with an encrypted share.
metadata:
  title: "Cobble"
---

# Cobble — a private city built from small things

A city assembled from scraps of noticing. Save a moment — the warm loaf in the window, a sentence
on a train, the light on wet pavement — and a building appears: colour is what kind of moment it
was, height is how much it mattered. Come back in a year and see what you made.

## When to use

- A record has to be **felt** rather than read: the same data as a list is a diary, as a city it is a place you return to.
- The data is personal, so the app is offline, local-only, and the share is encrypted rather than uploaded.
- You want a sample dataset that shows the thing off before the user has any data of their own.

## Method

1. Fix two encodings and keep them: **colour = kind**, **height = weight**. Every later feature has to fit those two channels or it does not belong on the skyline.
2. Store moments as a plain list with a timestamp; the city is a *view* of the list, rebuilt on load, never the storage format.
3. Add a demo city (`?demo=1`) built from a fixed sample so the first visit is not an empty grid.
4. Ship search and a timeline over the same data — the city is one way in, not the only way.
5. Make the share **encrypted**: the payload is sealed before it leaves the device, so a shared city is still the owner's data.
6. Export the whole thing (JSON, and an image of the city) so nothing is trapped in the app.

## Key files / entry points

- `app/` — the application.
- `docs/` — documentation and the landing page.
- `ENHANCEMENTS.md` — the ordered list of what is not built yet, kept out of the README on purpose.

## Gotchas

- A visual encoding is a promise: changing what height means breaks every city a user has already built.
- "Offline, editable, searchable" all describe the *same* store — if search indexes a cache instead of the moments, the two drift.
- A demo mode that writes to the real store contaminates the user's city; keep `?demo=1` read-only.

## Source projects

- [Cobble](https://github.com/drsamonline/Cobble)
