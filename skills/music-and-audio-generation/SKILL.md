---
name: music-and-audio-generation
description: "Generate music, songs and soundtracks — instrumentals, vocals from lyrics, covers and style transfer, stem extraction, repainting a weak section, continuation — and craft the prompt that gets them. Use for background music, a jingle, a soundtrack for a video, or any request that reaches a music generation model. Covers prompt structure, the nine dimensions, and multi-clip continuity."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Music and audio generation"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "acestep, music-prompter"
---

# Music and audio generation

Two halves of one job: the **prompt** decides what the model aims at, and the **pipeline** decides how you get a usable track out of it (variations, stems, repaint, continuation). Duration is the constraint that shapes everything else — under three minutes is always one call.

## When to use

- Background music, a jingle, a soundtrack bed for a video, or a full song with vocals.
- A generated track needs a weak section repaired, a longer continuation, or its stems split out.
- A cover or style transfer of existing audio is wanted.

## Method

1. Write the prompt before touching the model. Describe the *sound and feeling*, never the melody; use the nine dimensions (genre, mood, instrumentation, tempo, key, production, vocals, structure, references) as the checklist.
2. Structure the prompt in the fixed order the model follows: duration, then style, then arrangement breakdown, then vocal direction. Use metadata parameters for BPM and key rather than writing '120 BPM' into the caption.
3. If the requested duration is 180 seconds or less, use a single call and pack every section (verse, chorus, bridge, outro) into one prompt. Above 184 seconds, plan an arrangement and use the multi-clip continuity strategy: lock the always-identical dimensions across clips, align state precisely at each transition, then post-process.
4. Negative direction goes in prose inside the prompt ('instrumental only, no vocals', 'avoid dark mood') — there is no negative-prompt field.
5. Generate variations (four is the usual batch) and pick one; state why the pick fits the scene.
6. Vary BPM and key across scenes in a video — the same preset for every scene is the fastest way to make a soundtrack sound canned.
7. Fix weak output by repainting the section rather than regenerating the whole track; extend by continuing from the existing audio.
8. Split stems when the edit needs to duck or drop a layer, and never describe the melody you want — describe the sound.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`acestep`](references/acestep/) | The generation and repair pipeline on ACE-Step 1.5: variations, presets, vocals, covers, repaint, continuation, stems. |
| [`music-prompter`](references/music-prompter/) | The prompt craft: duration rules, the nine-dimension framework, standard structure, in-text negatives, multi-clip continuity. |

## Key files / entry points

- `references/music-prompter/` — the prompting framework: duration awareness, the nine dimensions, standard prompt structure, multi-clip continuity.
- `references/acestep/` — the generation pipeline: setup, variations, presets, vocals, covers, repaint, continuation, stems, and the fallback path.

## Gotchas

- Contradictory styles in one prompt ('classical strings' and 'hardcore metal') produce mush.
- Putting BPM or key in the caption instead of the metadata parameters loses the control.
- Long-form requests need an arrangement plan, not a longer prompt.
- Always append 'instrumental only, no vocals' when the user wants background music.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `acestep` — no licence file shipped with the source
- `music-prompter` — no licence file shipped with the source
