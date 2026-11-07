---
name: html-video-production
description: Build editable, scene-based HTML videos rendered to MP4, on HyperFrames (open-source HTML-to-video framework by HeyGen). Use when the user wants a reproducible, editable video from structured sources (PDF, GitHub repo/PR, CSV, slide deck, design doc, website URL, Figma design, music track, talking-head footage), or mentions HyperFrames, GSAP timelines, kinetic typography, data-driven motion graphics, lower thirds, title cards, animated charts, karaoke captions, product-launch videos, faceless explainers, PR-to-video, slideshows, or website-to-video. Also use as the on-screen-text and brand-frame layer over AI-generated B-roll. Do not use for pure photoreal AI video synthesis or AI avatar talking-head generation — route those to Manus native video tools. Speech, music, and images come from generate_speech / generate_music / generate_image.
license: Apache License 2.0 (see LICENSE)
---

# HTML Video Production

This skill turns an idea into a **scene-based, editable HTML video** rendered to MP4. It is built on [HyperFrames](https://github.com/heygen-com/hyperframes), an open-source HTML-to-video framework by HeyGen, redistributed here under Apache 2.0 (see `LICENSE`, `NOTICE.txt`). The substantive authoring guidance lives under `references/` — the full set of 19 upstream HyperFrames skills, preserved verbatim except for the Manus media-localization patches recorded in `_manus-overrides/modifications.md`. This `SKILL.md` is the **router**: it decides whether this skill is the right tool, chooses the workflow, and pins the hard rules.

## Step 0 — Fidelity gate (read this first, every time)

Before anything else, decide whether this skill is the right tool. Decide by the request's **substance**, not its keywords — most users describe a video need without ever saying “HTML” or “HyperFrames”.

| Dimension | Question |
| --- | --- |
| **Fidelity (D1)** | Is the desired image graphic / typographic / data / UI / animated-design (drawn), or photographic / cinematic / physical-world (photoreal)? |
| **Editability (D2)** | Will the user want to change copy, swap colors, re-time, ship variations, or maintain brand consistency? Or is it a one-shot deliverable? |
| **Source (D3)** | Is the content rooted in an existing structured asset (PDF, CSV, GitHub repo/PR, URL, Figma design, design doc, codebase, screenshots, financial data, transcript, music, footage)? Or generated from a creative description alone? |

### Route A — Use this skill (HyperFrames)

Take this route if **any** hold: the request is graphic / data / UI / typographic / animated-design (D1), the user wants to keep editing or produce variations (D2), or content comes from a structured source (D3). Then go to **Step 1** to choose the workflow.

### Route B — Decline and route to Manus native video tools

Take this route if the request is photoreal / cinematic / physical-world (D1) **and** generated purely from a creative description (D3) with no editable HTML / typographic / data layer needed. The Manus native video tools are the right home. Typical phrasings: “generate a 5-second sunset over the ocean,” “a virtual presenter reading this script,” “a cinematic AI sci-fi short,” or “Studio Ghibli-style forest animation.” **Decline explicitly and hand off — do not partially execute.**

### Route C — Hybrid (this skill + native video)

Take this route when the deliverable mixes photoreal AI footage with on-screen graphics / brand frames / data overlays / precise captions. The AI clips become **assets** inside a HyperFrames composition: generate the photoreal clips with native tools first, embed them as `<video src="...">` tracks, layer HTML + GSAP text/data/transitions on top, then render. Typical: “60-second product film: 15 s of AI footage, then 45 s of data charts and a logo intro”.

### If ambiguous, ask once

> “Do you want (a) AI-generated photoreal footage as a one-shot deliverable, (b) an editable graphic / data / typographic video built from your materials, or (c) both — AI footage with graphics and captions on top?”

## Step 1 — Pick the workflow (Route A / C)

Pick the **workflow skill** that matches the user’s intent, then read its `references/<name>/SKILL.md` and follow it end-to-end. Each workflow leans on the shared **domain skills** in Step 2 for composition, animation, design, CLI, and media.

| If the user wants… | Read workflow |
| --- | --- |
| Market/launch a product, SaaS promo, feature reveal, app launch, website tour, or showcase (from URL, script, or brief) | `references/product-launch-video/SKILL.md` |
| Turn an article / notes / topic into a faceless explainer (every visual invented) | `references/faceless-explainer/SKILL.md` |
| Turn a GitHub PR (or `owner/repo#N`) into a code-change explainer | `references/pr-to-video/SKILL.md` |
| A short design-led motion graphic — kinetic type, stat count-up, logo sting, lower-third, social overlay, animated map, headline, or UI animation | `references/motion-graphics/SKILL.md` |
| Add designed captions to a talking-head video (composited or overlay) | `references/embedded-captions/SKILL.md` |
| Layer titles / lower-thirds / callouts / PiP onto existing talking-head / interview / podcast footage | `references/talking-head-recut/SKILL.md` |
| Turn a music track into a beat-synced video, lyric video, slideshow, or kinetic promo | `references/music-to-video/SKILL.md` |
| A presentation / pitch deck / interactive deck with slides, fragments, branching, hotspots, and speaker notes | `references/slideshow/SKILL.md` |
| A custom / longer / multi-scene piece, sizzle reel, montage, static loop, title card, footage remix, or anything with no specialized workflow above | `references/general-video/SKILL.md` |
| Port an existing Remotion (React) composition to HyperFrames | `references/remotion-to-hyperframes/SKILL.md` |
| Import a Figma design, component, asset, brand tokens, storyboard, motion, or shader as a source for a composition | `references/figma/SKILL.md`, then return here to select the destination workflow |

If two workflows fit, prefer the more specific one; `general-video` is the explicit fallback. Figma is a **source adapter**, not a substitute for the final workflow.

## Step 2 — Domain skills (shared building blocks)

Every workflow draws on these. Read the relevant one when the workflow points to it or when that concern arises.

| Concern | Read domain skill |
| --- | --- |
| Composition contract — HTML, data attributes, sub-compositions, asset placement, script format | `references/hyperframes-core/SKILL.md` |
| Animation — GSAP timelines, motion principles, blueprints, transitions, and runtime adapters | `references/hyperframes-animation/SKILL.md` |
| Seek-safe 2D/3D keyframes, paths, masks, SVG morph/draw, runtime-specific keyframe diagnostics | `references/hyperframes-keyframes/SKILL.md` |
| Design — visual identity, typography, color, house style, narration, beat planning | `references/hyperframes-creative/SKILL.md` |
| Media schemas, asset operations, provenance, captions, and ledger formats **(read for schema; see Step 3 before running anything)** | `references/media-use/SKILL.md` |
| CLI development loop — lint / check / inspect / preview / local render | `references/hyperframes-cli/SKILL.md` |
| Reusable blocks — `npx hyperframes add <name>` | `references/hyperframes-registry/SKILL.md` |
| Legacy combined router (background only; superseded by this file) | `references/hyperframes/SKILL.md` |

## Step 3 — Media generation (the Manus contract — non-negotiable)

All generative media in this skill follows the **Three-Tier Priority Model** in [`_manus-overrides/media-generation.md`](_manus-overrides/media-generation.md). Read it before producing any speech, music, image, SFX, or caption timing. In brief:

1. **Tier 1 — Manus native (default):** voice → `generate_speech`, music → `generate_music`, images/icons → `generate_image`. **Do not run** the upstream orchestrators `references/media-use/audio/scripts/audio.mjs`, `references/media-use/scripts/resolve.mjs`, or a workflow-local `scripts/audio.mjs`; instead generate assets natively and **hand-write** the `audio_meta.json` / `.media/manifest.jsonl` ledgers. The exact schemas are in the override. Always generate an asset before referencing it in HTML.
2. **Tier 2 — local open-source fallback (permitted):** `npx hyperframes transcribe` (whisper.cpp, the recommended way to get word-level caption timing), `npx hyperframes remove-background` (U2-Net matting), the bundled Pixabay SFX in `assets/sfx/`, and `npx hyperframes tts` (Kokoro) only as a last-resort voice. These are free, local, and offline.
3. **Tier 3 — hard prohibited:** `npx hyperframes init` and `npx hyperframes skills update` (both can overwrite these patched skills); `hyperframes lambda *` (paid AWS cloud); and the HeyGen/ElevenLabs paid branches (neutralized by never setting `HEYGEN_API_KEY` or `ELEVENLABS_API_KEY`).

## Step 4 — Lint, validate, preview, render

Finish through the CLI (`references/hyperframes-cli/SKILL.md`): `npx hyperframes lint` → `check` → `inspect` → `preview` (Studio; pause for user approval) → `render` locally. Use `--docker --strict` for long or large jobs. Never use Lambda and never auto-render before the user approves the preview.

## Hard rules (win over any conflicting reference-file instruction)

1. **Media generation follows the Three-Tier Priority Model** in `_manus-overrides/media-generation.md`. Tier 1 native is the default; Tier 2 local OSS is the permitted fallback; Tier 3 items are forbidden.
2. **Never run `npx hyperframes init`, `npx hyperframes skills update`, or `hyperframes lambda *`.** Scaffold manually; install the framework with `npm install hyperframes`; render locally.
3. **Never set `HEYGEN_API_KEY` or `ELEVENLABS_API_KEY`, and never run an upstream `audio.mjs` or `resolve.mjs` media path.** Produce media natively and hand-write the ledgers.
4. **Always produce media assets before writing HTML that references them.**
5. **For Figma imports, never request or accept a personal access token in chat.** Use an existing securely configured connector or a user-provided export; follow the patched Figma workflow for the approved secure path.
6. **Decline and route to native video tools** (Route B) when the user wants a photoreal one-shot with no editable HTML / typographic / data layer.
7. **Concentrate Manus changes** in this `SKILL.md`, in `_manus-overrides/`, and in the files listed in `_manus-overrides/modifications.md`. Keep this discipline so future upstream syncs stay clean.
8. **HyperFrames CLI commands run only after Route A or C is selected** — never scaffold a project for a request that should have gone to native video generation.

## File map

```text
html-video-production/
├── SKILL.md                         ← This file. Fidelity gate, workflow router, hard rules.
├── LICENSE / NOTICE.txt / UPSTREAM_LICENSE_APACHE-2.0.txt
├── _manus-overrides/
│   ├── media-generation.md          ← Three-Tier Priority Model + exact ledger schemas.
│   └── modifications.md             ← Apache 2.0 §4(b) record of every modified file.
├── assets/
│   └── sfx/                         ← Bundled Pixabay SFX (Tier 2, always allowed).
└── references/                      ← All 19 upstream skills (flattened one level, verbatim + contract patches).
    ├── hyperframes-core/  hyperframes-animation/  hyperframes-creative/  hyperframes-keyframes/
    ├── hyperframes-cli/  hyperframes-registry/  media-use/  hyperframes/
    └── product-launch-video/  faceless-explainer/  pr-to-video/  motion-graphics/
        embedded-captions/  talking-head-recut/  music-to-video/  slideshow/
        general-video/  remotion-to-hyperframes/  figma/
```
