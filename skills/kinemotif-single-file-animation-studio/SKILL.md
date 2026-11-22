---
name: kinemotif-single-file-animation-studio
description: Turn a paragraph into a moving, scored presentation inside a single dependency-free HTML file — six art styles, real shape morphing, a synthesised soundtrack, and an export that is one offline file.
metadata:
  title: "Kinemotif"
---

# Kinemotif — a paragraph into a scored show, in one HTML file

A self-contained HTML animation studio: paste a story, choose a look, and it builds a multi-scene
presentation that draws its own artwork, morphs between scenes and synthesises an original
soundtrack while it plays. The finished show exports as a single `.html` file that runs offline.

## When to use

- The output must be **one file** that opens by double-click, with no server, no install and no network.
- There are no assets and no fonts to ship: every pixel is Canvas 2D and every note is Web Audio.
- You want the same product in two weights — this one for a web page, Kinemorph for a video file.

## Method

1. Keep the source in `src/*.js` + `src/style.css` and build with `python3 build.py` into `studio/kinemotif.html`. Python is the only tool; there is no bundler.
2. Six art styles, chosen per scene or cycled through a set — style is a function of scene data, never a global mode.
3. Real shape morphing between scenes: interpolate the geometry, do not cross-fade two pictures.
4. Score it with Web Audio at play time; the soundtrack is generated, so it costs nothing to ship and nothing to license.
5. Export the show as one HTML file by inlining the show data into the same template that plays it — the export path and the play path share code, which is why they cannot drift.
6. Keep the demo topics in the app so a first-time visitor has something to press before they have written anything.

## Key files / entry points

- `studio/kinemotif.html` — the built studio (open it directly).
- `src/` — the sources; `build.py` concatenates them.
- `build.py` — the whole build system.

## Gotchas

- The build is string concatenation into one file; a stray `</script>` inside a template literal ends the document early and the symptom is a blank page, not an error.
- Generated audio must not autoplay: it starts on the user's first press, which the flow already requires.
- An exported show embeds its data, so a large paragraph produces a large file — warn before export rather than after.

## Source projects

- [kinemotif](https://github.com/drsamonline/kinemotif)
