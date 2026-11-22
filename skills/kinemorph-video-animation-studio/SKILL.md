---
name: kinemorph-video-animation-studio
description: Build a browser animation studio that turns a paragraph into a scored, styled show and exports frame-exact MP4 through WebCodecs — React + TypeScript over PixiJS, a GSAP timeline, a Tone.js generative score, and a committed build.
metadata:
  title: "Kinemorph"
---

# Kinemorph — an animation studio that exports real video

The heavy sibling of Kinemotif: a React + TypeScript editor over a PixiJS WebGL renderer, a
generative Tone.js score, and frame-exact MP4 export through WebCodecs. Where Kinemotif is one
dependency-free HTML file, this is a proper application — and the point of the pair is knowing
which one a job needs.

## When to use

- The deliverable is a **video file**, not a web page: a reel, a clip for a channel, a file someone can upload.
- You need frame-exact export — the encoder is stepped by the clock you choose, not by how fast the machine renders.
- Per-scene styling matters: a show inherits one art style or cycles through several, and transitions draw each side in its own palette.

## Method

1. Split the paragraph into sentences; each sentence becomes a scene. Structure first, art second.
2. Keep the art styles as data (10 of them, from Pixel Arcade to Swiss Grid) and let any scene override the show's default — per-scene style is what stops a long show looking like one template.
3. Drive the timeline from one clock. For export, advance that clock in exact frame steps and render each step to a canvas, so the MP4 is the same on a slow machine.
4. Encode with WebCodecs (`VideoEncoder`), mux the frames, and offer WebM/VP9 as the fallback where H.264 is unavailable.
5. Generate the score with Tone.js and export a WAV stem alongside the video, so the audio survives a re-edit.
6. Commit the build output (`studio/`) and let Pages serve it — a static host with no CI build is one less thing that can break.

## Key files / entry points

- `src/` — the React/TypeScript studio.
- `studio/` — the committed build that Pages serves.
- `npm run dev` · `npm run build` · `npm run typecheck` — Node 20+, no other tooling.

## Gotchas

- **Portrait is a reflow, not a crop.** Four formats (16:9, 9:16, 1:1, 4:5) mean the layout has to recompute, and a crop of a 16:9 composition loses the text.
- Feature parity with the lighter sibling is a trap: Kinemotif has `zoom` and `blinds` transitions that this one does not. Say so, rather than pretending the two are interchangeable.
- WebCodecs is Chromium-first; the export path needs a visible "not available here" state rather than a spinner that never ends.

## Source projects

- [kinemorph](https://github.com/drsamonline/kinemorph)
