---
name: ai-video-generation
description: "Generate a video clip with the muapi.ai model stack: character sheets, storyboards, image-to-video, UGC ads, product ads, music videos, cartoon dance and UI mockups. Use when the user wants an AI-generated video or ad from a photo, a brief, a lyric or a storyboard, or names Seedance, Nano-Banana, GPT-Image-2 or muapi. Not for editing footage that already exists (use video-clip-finder) or for code-driven motion graphics (use html-video-production)."
license: "per source — see references/*/LICENSE"
metadata:
  title: "AI video generation (Muapi model stack)"
  category: "media-design"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "muapi-ai-fight-scene, muapi-animal-video-generator, muapi-cartoon-dance-animation, muapi-music-video, muapi-product-video-ad-maker, muapi-social-media-video, muapi-ugc-video-factory, muapi-ui-design"
---

# AI video generation (Muapi model stack)

Eight recipes that share one shape: an **image phase** that locks identity and composition, then a **video phase** that animates that still and lets the model generate native audio. Almost every bad result traces back to a vague still or a vague director prompt, not to the video model. Fix the still first; it is also the cheap thing to regenerate.

## When to use

- A short video is wanted from a product photo, a person photo, a brief, a lyric sheet or a brand voice.
- The output is a social ad, a UGC testimonial, a product film, a fight/action scene, a cartoon dance, a music video, or a set of UI mockups.
- The user names a muapi model (Seedance 2.0, Nano-Banana, GPT-Image-2) or says 'muapi'.

## Method

1. Pick the recipe from the table below — it fixes the phase order, the models and the aspect ratio. Do not blend two recipes in one run.
2. Write the image prompt in cinematography language: shot size, lens, camera position, light source and quality, palette, texture. Vague adjectives ('beautiful', '8k', 'amazing') buy nothing.
3. Vary shot size aggressively across a sequence — never two WIDEs in a row — and land every impact or payoff on a close-up or extreme close-up.
4. Generate the still (or the storyboard) and look at it before spending on video. If one cell of a storyboard reads badly, regenerate the storyboard with that cell's note bolded ('CELL 7 must be an ECU on the right fist'); it is cheaper than re-running the video.
5. Animate with image-to-video, passing the still as the reference and a director prompt that repeats camera move, subject motion and audio direction. Always give sound direction: these models generate audio.
6. Keep identity locked when a person or product must survive the transition: same face shape, eyes, nose, lips, jawline, skin tone, hairstyle; legible logo and product text.
7. For brand work, read the brand files (brand-identity, ICP, messaging) before writing a word, and make the storyboard visibly match the palette and tone you read.
8. Present the finished video, then state which phase to re-run if the result is off — video phase first, storyboard second.
9. Ask before any single generation call whose cost is unusually high (the music-video recipe sets the bar at 50 credits); never auto-confirm a large spend.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`muapi-ai-fight-scene`](references/muapi-ai-fight-scene/) | 16-cell storyboard then Seedance 2.0 i2v; the only recipe that plans cut density explicitly. |
| [`muapi-animal-video-generator`](references/muapi-animal-video-generator/) | Anthropomorphic animal vlogger in a real setting, image then video. |
| [`muapi-cartoon-dance-animation`](references/muapi-cartoon-dance-animation/) | Photo → Pixar-style 3D character → motion-transfer animation driven by a reference dance video. |
| [`muapi-music-video`](references/muapi-music-video/) | N keyframes from a song theme, each animated, plus matching music. |
| [`muapi-product-video-ad-maker`](references/muapi-product-video-ad-maker/) | Simple product photo → premium product render → cinematic video ad. |
| [`muapi-social-media-video`](references/muapi-social-media-video/) | Brand-aware social video: read brand files, write post + storyboard, craft a Seedance director prompt. Start here for anything with a brand. |
| [`muapi-ugc-video-factory`](references/muapi-ugc-video-factory/) | Person photo + product photo → vertical 9:16 UGC ad, hero image then Seedance VIP image-to-video with native audio. |
| [`muapi-ui-design`](references/muapi-ui-design/) | High-fidelity mobile/web UI mockups on Atomic Design principles — image generation, no video phase. |

## Key files / entry points

- `references/muapi-social-media-video/` — brand-aware social video; the fullest director-prompt reference (camera intents, platform specs, prompt checklist).
- `references/muapi-ugc-video-factory/` — person + product → 9:16 UGC ad.
- `references/muapi-product-video-ad-maker/` — product photo → cinematic ad.
- `references/muapi-ai-fight-scene/` — the storyboard-first action recipe.
- `references/muapi-cartoon-dance-animation/`, `references/muapi-animal-video-generator/`, `references/muapi-music-video/`, `references/muapi-ui-design/` — the remaining recipes, each self-contained.

## Gotchas

- Reading the brand files and then ignoring them is the most common failure: the storyboard has to match the palette and tone, not just cite the file.
- Sound is generated, not added later — a prompt with no audio direction gets generic ambience.
- UI mockups must be flat or glassmorphic and must not contain hands, phones or desks, or the model produces a photograph of a screen instead of a design.
- Regenerate the cheap phase: video before storyboard is wrong; storyboard before video is right.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `muapi-ai-fight-scene` — no licence file shipped with the source
- `muapi-animal-video-generator` — no licence file shipped with the source
- `muapi-cartoon-dance-animation` — no licence file shipped with the source
- `muapi-music-video` — no licence file shipped with the source
- `muapi-product-video-ad-maker` — no licence file shipped with the source
- `muapi-social-media-video` — no licence file shipped with the source
- `muapi-ugc-video-factory` — no licence file shipped with the source
- `muapi-ui-design` — no licence file shipped with the source
