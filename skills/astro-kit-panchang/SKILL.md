---
name: astro-kit-panchang
description: Sun and moon longitude (Meeus), Lahiri ayanamsa, sunrise/sunset/transit and the derived tithi, nakshatra, yoga and karana — the astronomy core for an offline panchang.
metadata:
  title: "Panchang astronomy core"
---

# Panchang astronomy core

`Astro` computes what an Indian almanac needs, from the maths in the file: solar
and lunar longitude (Meeus), the Lahiri ayanamsa, sunrise, sunset and solar
transit, the moon's phase and illumination, and the derived tithi, nakshatra,
yoga and karana. Zero dependencies, no ephemeris file.

## When to use

- An app must show today's panchang, a muhurat, or rahu-kaal, offline.
- You need sunrise/sunset or the moon's phase for a place and a date.
- You are about to embed an ephemeris table — the maths here is smaller.

## Method

1. Call `Astro.panchang({ y, m, d, h }, { lat, lon })` for one instant and place.
2. Read the derived limbs — `p.tithi.name`, `p.nakshatra.name`, `p.paksha`,
   `p.pada` — and the solar data at `p.sun.sunriseUTC`, `sunsetUTC`,
   `transitUTC`.
3. Convert UTC to the user's offset yourself; the kit is deliberately
   timezone-free.
4. Use `elongation`, `illumination` and the phase for anything about the moon.
5. Cache one computation per day per place rather than recomputing per render.

## Key files

- `astro-kit.js` — `panchang`, longitude, elongation, ayanamsa, sunrise/sunset/
  transit, illumination.
- `test-node.js` — reference values cross-checked against an independent
  ephemeris (PyEphem), agreeing to better than 0.05° on elongation.

## Gotchas

- `sunriseUTC` is **UTC**. Adding the offset is the caller's job, and getting it
  wrong shifts rahu-kaal by whole hours without any error.
- The ayanamsa is Lahiri and approximate. Do not present the output as an
  observatory-grade ephemeris.
- `app-panchang` is the only adopter and it vendors `astro-kit.js`, so a fix here
  has to be re-vendored there.
- Accuracy is the kit's own; there is no external library to blame. The test
  file's tolerances are the honest statement of what it claims.

## Source projects

- [astro-kit](https://github.com/drsamonline/astro-kit) — the astronomy core.
- [app-panchang](https://github.com/drsamonline/app-panchang) — tithi, nakshatra, yoga, karana, rahu-kaal and muhurat, computed offline.
