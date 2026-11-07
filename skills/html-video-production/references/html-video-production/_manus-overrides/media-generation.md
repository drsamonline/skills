# Manus Media Contract — Three-Tier Priority Model

This file is the single source of truth for **how speech, music, images, sound effects, and audio transcription are produced inside the `html-video-production` skill in Manus**. It overrides any conflicting media instructions in the bundled upstream HyperFrames skills under `references/`. Whenever an upstream file describes a different path — including workflow-local `audio.mjs`, `media-use/audio/scripts/audio.mjs`, `media-use/scripts/resolve.mjs`, HeyGen, ElevenLabs, or AWS Lambda — this contract wins.

## The model in one screen

| Tier | What | When | Examples |
| --- | --- | --- | --- |
| **Tier 1 — Manus native** | `generate_speech`, `generate_music`, `generate_image` | **Default for all generative media.** Always prefer this. | Voiceover, score/underscore, product images, icons, background plates |
| **Tier 2 — Local open-source fallback (permitted)** | `npx hyperframes transcribe` (whisper.cpp), `npx hyperframes remove-background` (U2-Net), bundled Pixabay SFX, `npx hyperframes tts` (Kokoro) | When no native tool fits, or the task has no native equivalent. Free, local, offline. | Word-level caption timing, subject cutout/matting, quick SFX, last-resort voice |
| **Tier 3 — Hard prohibited** | `npx hyperframes init`, `npx hyperframes skills update`, `hyperframes lambda *`, and paid HeyGen/ElevenLabs branches | Never. | — |

> Why tiers rather than a blanket ban: the permitted CLI media fallbacks run local open-source models, not paid cloud APIs. The genuine violations are the auto-pull commands, paid cloud rendering, and paid/provider-auth media paths.

---

## Tier 1 — Manus-native generation (the default path)

### Hard rules

1. **Narration / voiceover** → `generate_speech`.
2. **Background music / underscore / stings** → `generate_music`. Never compose with ffmpeg or call a third-party music API.
3. **Raster images / icons / product shots / textured backgrounds** not supplied by the user → `generate_image` (or its native edit/variation equivalent). Never use placeholder image services or assume runtime-fetched images.
4. **Word-level timestamps** → use Tier 2 `transcribe`; `generate_speech` does not return word timings.
5. **Always generate the asset before referencing it** in HTML. No `<audio src>` / `<img src>` may point to a path that does not yet exist.
6. **Do not surface a provider choice.** Manus native tools are the chosen default; do not prompt for HeyGen, ElevenLabs, a CLI credential, or an API key.

Read the `tts-prompter` skill for speech prompt construction and the `music-prompter` skill for music prompt construction. This document is the integration contract for slotting their outputs into a HyperFrames project.

### The critical substitution: do not run upstream media orchestrators

Do **not** run any of these upstream media paths:

- `references/media-use/audio/scripts/audio.mjs` — shared TTS + BGM + SFX engine → `audio_meta.json`.
- `references/media-use/scripts/resolve.mjs` — asset resolver → `.media/manifest.jsonl`.
- A workflow-local `references/<workflow>/scripts/audio.mjs` — workflow-specific TTS + BGM + SFX engine → `audio_meta.json`.

Instead, generate each asset with Tier-1 tools and **hand-write the ledger files those scripts would have produced**, so the downstream pipeline (captions, duration sync, assembly, render) consumes them transparently. The schemas are below.

### `audio_meta.json` — hand-written (id-keyed; consumed by caption/assembly steps)

For a workflow that expects `assets/voice/<id>.wav`, place voice files there; for the new `media-use` layout, `.media/audio/voice/<id>.wav` is also valid when that is the project convention. Place BGM at `assets/bgm/track.wav` or `.media/audio/bgm/track.wav` to match the active workflow. The `words` array is the caption-timing source — fill it from a Tier-2 `transcribe` pass.

```json
{
  "tts_provider": "manus-generate_speech",
  "voice_id": "<the Manus voice you used>",
  "bgm": { "path": "assets/bgm/track.wav", "volume": 0.15, "mode": "generate", "query": null, "duration_s": 12.3 },
  "bgm_pending": false, "bgm_provider": "manus-generate_music", "bgm_pid": null, "bgm_log": null,
  "bgm_mode": "generate", "bgm_target_duration_s": 12.3, "bgm_seed_duration_s": null, "bgm_loop_count": null,
  "voices": [
    { "id": "01", "path": "assets/voice/01.wav", "duration_s": 3.2,
      "words": [ { "id": "w0", "text": "Hello", "start": 0.0, "end": 0.4 } ] }
  ],
  "sfx": [
    { "id": "01", "name": "whoosh", "file": "assets/sfx/whoosh.mp3", "source": "bundled-pixabay",
      "offset_s": 0, "duration_s": 0.8, "volume": 1 }
  ],
  "total_duration_s": 12.3
}
```

If a workflow describes subset merges (`audio.mjs --only tts,bgm,sfx`, `sync-durations`, `fetch-sfx`), regenerate or patch the relevant keys of this same file by hand. Downstream steps only read the JSON; they do not require the script to have written it.

### `.media/manifest.jsonl` — hand-written (one JSON record per line)

When a workflow uses the `media-use` resolver, generate the image with `generate_image`, save it under `.media/images/`, and append one line per asset. Directory map: `bgm` → `.media/audio/bgm`, `sfx` → `.media/audio/sfx`, `voice` → `.media/audio/voice`, `image|icon|brand` → `.media/images`, `video` → `.media/video`. IDs are `<type>_<NNN>` zero-padded. You may regenerate `.media/index.md` by hand or leave it; downstream reads the `.jsonl` ledger.

```json
{ "id":"image_001", "type":"image", "path":".media/images/image_001.png", "source":"generated", "description":"<intent>", "width":1920, "height":1080, "transparent":false, "provenance": { "provider":"manus-generate_image", "prompt":"<intent>" } }
```

### Speech details

- **Write `narration.txt` first**: it is the exact string passed to `generate_speech`, including pronunciation fixes such as `API` → `A P I`. Keep it separate from human-readable `SCRIPT.md`.
- **Use SSML** for pacing: `<break time="...ms"/>`, `<prosody rate/pitch/volume>`, and `<emphasis>`.
- **Place the WAV** with `data-duration="auto"` so HyperFrames reads true duration via ffprobe, or declare duration explicitly after measuring it.

```html
<audio id="narration" data-start="0" data-duration="auto" data-track-index="2" src="assets/voice/01.wav" data-volume="1"></audio>
```

### Music details

- Decide **role** (underscore / lead bed / sting), **mood arc**, and **duration** (composition length plus a 0.5-second tail; native music does not auto-trim).
- Use `data-volume="0.10–0.20"` under narration, `0.50–0.70` when music leads, and `1.0` for stings.

```html
<audio id="bg-music" data-start="0" data-duration="auto" data-track-index="3" src="assets/bgm/track.wav" data-volume="0.15"></audio>
```

### Image details

- **Generate** product/marketing images, icons/logos not supplied in `assets/`, background plates, and variations of existing images.
- **Do not generate** pure CSS/GSAP shapes, registry iconography (`hyperframes add <name>`), or charts. Build charts as live SVG or Canvas, not flat PNG.
- Match the output frame: **16:9 (1920×1080)**, **9:16 (1080×1920)**, or square only for an explicit feed asset.
- Give every generated image a motion treatment; never embed it as a flat, static card.

---

## Tier 2 — permitted local open-source fallbacks

Use a Tier-2 path only when Tier 1 does not fit.

| Tool | Engine (local OSS) | Use it for |
| --- | --- | --- |
| `npx hyperframes transcribe <audio>` | whisper.cpp | **Word-level caption timing** — the recommended way to fill `words[]` in `audio_meta.json`, even when the voice came from Tier 1. |
| `npx hyperframes remove-background <img>` | U2-Net | Subject cutout / matting. Manus has no native equivalent, so this is preferred. |
| Bundled SFX `assets/sfx/*.mp3` | Pixabay Content License | Drop-in sound effects. Always allowed; reference directly with no API call. |
| `npx hyperframes tts <text>` | Kokoro-82M | **Last-resort** voice only, when `generate_speech` is unavailable. |

---

## Tier 3 — hard prohibitions (never)

1. **`npx hyperframes init` and `npx hyperframes skills update`.** Both can re-fetch skills from GitHub and overwrite these Manus-patched files, silently re-enabling disabled paths. **Scaffold manually**: `mkdir <project> && cd <project> && npm init -y && npm install hyperframes`, then author composition HTML. `npx hyperframes capture <url>` is permitted because it does not re-pull skills.
2. **`hyperframes lambda *`** — paid AWS cloud rendering. **Render locally** with `npx hyperframes render`; add `--docker --strict` for long or large jobs.
3. **HeyGen/ElevenLabs paid branches** inside the upstream audio/resolver scripts. **Never set `HEYGEN_API_KEY` or `ELEVENLABS_API_KEY`**, never sign in to unlock their branches, and never run the orchestrators. The contract’s native-tool-plus-ledger path replaces them.

---

## Cross-references

- [`modifications.md`](modifications.md) — every upstream file Manus modified, for Apache 2.0 §4(b).
- `references/media-use/` — upstream media and resolver docs (read for ledger schemas only; do **not** run its orchestrators).
- `references/embedded-captions/` and `references/hyperframes-core/` — caption authoring and asset placement (consume the `words` timing produced above).
