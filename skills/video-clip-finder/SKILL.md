---
name: video-clip-finder
description: "Find the compelling moments in a long video — funny dialogue or repeated impact actions such as chops, hits, throws, drumbeats — cut them as standalone clips, reformat 16:9 to 9:16, time-warp a reveal, and burn word-by-word captions. Use for 'make shorts from this', 'find funny moments', 'cut on each chop', 'action montage', or any clipify request. Not for generating new footage."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Find and cut short clips from long video"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "clipify"
---

# Find and cut short clips from long video

Two modes over the same pipeline: **dialogue** (transcribe, find the funny or quotable stretches) and **action** (detect repeated transients, cut on each strike). Both then trim, reframe and caption. The single discipline that makes it work is verifying that the event is *visible*, not just audible, before rendering anything.

## When to use

- A long video must become vertical shorts or a highlight reel.
- The user names clipify, or asks to cut on each chop/hit/punch/drumbeat.
- A slow scenic shot needs tightening without losing the arc (speed-ramp rather than trim).

## Method

1. Choose the mode from the request: dialogue for talking-head or narrative footage, action for repeated percussive events.
2. Dialogue mode: transcribe with whisper and pick candidate windows from the transcript. Do not whisper a feature-length source when a short clip will do — whisper the trimmed clip after step 3.
3. Action mode: detect transients on the audio track to get candidate strike times.
4. **Verify every candidate is in frame** before rendering: sample one frame at each candidate time and look at it. Audio detection finds the sound of a chop, not whether the chopper is visible. Skipping this is the most common reason a cut is rejected.
5. Trim with stream copy for speed; re-encode only when a cut must be frame-accurate.
6. Decide the output format, then for 16:9 → 9:16 choose pan-between-faces (fast-cut dialogue) or split-screen (both faces always visible). Iterate the ROI at most twice — motion differencing is forgiving, and a box covering mouth and chin works even if it is not perfectly centred.
7. For a slow reveal that must stay whole, speed-ramp instead of trimming: 2x with atempo keeps the audio pitch.
8. Caption the trimmed clip: re-run whisper on the clip so timestamps are relative to its start, then burn word-by-word captions in the house style.
9. Deliver the clips with their source timestamps and say which candidates were rejected and why.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`clipify`](references/clipify/) | The complete clip-finding method: two modes, frame verification, trim, reframe (pan or split-screen), speed-ramp, word-by-word captions, delivery. |

## Key files / entry points

- `references/clipify/` — full modes, tooling, ROI guidance, reframing recipes and the pitfalls list from prior runs.

## Gotchas

- Audio detection is not visual detection — run the frame check first, every time.
- Do not over-tune the crop: two iterations maximum.
- Trimming drops part of an arc; speed-ramping keeps it.
- A box that covers hands or a mic will cut into the face on movement.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `clipify` — carries its own LICENSE file
