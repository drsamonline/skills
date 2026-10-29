---
name: remotion-maps
description: Remotion Map animation knowledge
license: see LICENSE-NOTICE.md
metadata:
  title: "remotion maps"
  origin: "remotion-dev/skills"
  upstream-path: "skills/remotion-maps/SKILL.md"
  upstream-commit: "30d4553ecd46fbc5212fd0ff006ae43af522158b"
  category: "media-design"
---

# Remotion Maps

Choose exactly one technique from the intended shot, then load only that technique's `TECHNIQUE.md`.
Every technique directory is self-contained and may be removed without breaking the others.

## [Static map](techniques/static-map/TECHNIQUE.md)

- Requires you grab a satellite image and mount it in a `<Img>` tag, and animate on top

## [Mapbox](techniques/mapbox/TECHNIQUE.md)

- Requires a Mapbox key
- Nicer styles by default
- Map can display a round globe when zoomed out
- Includes nice 3D buildings such as the Eiffel tower

## [MapLibre](techniques/maplibre/TECHNIQUE.md)

- Requires no API key, fully free
- Does not include 3D building

## [MapTiler](techniques/maptiler/TECHNIQUE.md)

- Uses MapTiler
- Annotations can be drawn on top of geographic features: borders, rivers, labels

## [CesiumJS](techniques/cesium/TECHNIQUE.md)

- Flythroughs through terrain and mountains
- "Flight simulator" perspective

## Provenance

Imported from [remotion-dev/skills](https://github.com/remotion-dev/skills) at commit `30d4553`, path `skills/remotion-maps/SKILL.md`. The upstream repository publishes no licence file; included at the catalogue owner's direction, all rights with its authors — see `LICENSE-NOTICE.md`.
