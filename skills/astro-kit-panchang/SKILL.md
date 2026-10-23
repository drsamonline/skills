---
name: astro-kit-panchang
description: Compute the sun and moon longitude, ayanamsa, sunrise/sunset and the panchang limbs (tithi, nakshatra, yoga, karana) from Meeus's series, and verify them against published ephemeris values.
metadata:
  title: "Astronomical primitives for a panchang"
---

# Astronomical primitives for a panchang

## When to use

When an app needs an Indian almanac — tithi, nakshatra, muhurat, sunrise — or any
solar/lunar position. Do this in a **kit**, not in the app: the app should stay a
calendar and a UI.

## Method

1. **Julian day** from the date (UTC), then work in Julian centuries `T` from J2000.
2. **Solar apparent longitude** (Meeus ch. 25): mean longitude `L0`, mean anomaly
   `M`, equation of centre `C`, then subtract `0.00569 + 0.00478·sin(Ω)` for
   aberration and nutation.
3. **Lunar longitude** (Meeus ch. 47): `L′` plus a periodic series. The first
   ~25 terms give ~0.005°, plenty for a panchang.
4. **Ayanamsa** (Lahiri, linear approximation) to convert tropical → sidereal.
5. **Sunrise/sunset**: the standard sunrise equation — mean solar noon `J*`,
   solar transit, declination, hour angle `ω`, then `J_transit ± ω/360`.
6. **Panchang limbs** from the elongation `e = (moonLong − sunLong) mod 360`:
   `tithi = ⌊e/12⌋`, `nakshatra` from sidereal moon longitude `/ (360/27)`,
   `yoga` from `(sunLong + moonLong) mod 360`, `karana` from `⌊e/6⌋`.

## Key files

- `astro-kit.js` — `Astro.jd`, `sunLongitude`, `moonLongitude`, `ayanamsa`,
  `sunriseSunset`, `tithi`, `nakshatra`, `yoga`, `karana`, `moonPhase`, `panchang`.
- `test-node.js` — verified against the Meeus worked examples.

## Gotchas

- **Verify against published values, not intuition.** Meeus example 25.b (sun,
  JDE 2448908.5 → 199.90895°) and 47.a (moon, JDE 2448724.5 → 133.162655°) are
  the anchors. A wrong constant shows up immediately.
- **The sunrise `n` term is an integer.** `n = ceil(J − 2451545 + 0.0008)`, not the
  raw JD — using the raw JD puts the transit at midnight and sunrise negative.
- **State the precision.** ~0.01–0.05° ⇒ a boundary within about a minute. Never
  present panchang timings as exact; local tradition differs too.
- **Timezone is the app's job.** The kit returns UTC; the app adds the offset.

## Source projects

`astro-kit` (the shared core); `app-panchang` / `panchang` (the thin apps).
