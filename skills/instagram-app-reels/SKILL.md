---
name: instagram-app-reels
description: Turn a web app into vertical Instagram Reels — drive the real app in headless Chromium, capture every step, and compose 1080x1920 clips with burned-in captions, step counters and an optional buy/CTA end card. Use this whenever the user wants a video tutorial, screen recording, demo video, walkthrough, product tour or "clips to post on Instagram / Reels / Shorts / TikTok" of an app, site, repo or prototype — including "record the steps", "make a video of my app", "make a promo video", "give me clips", "screen record this flow" or "add text to the video". Also use it when they ask to re-cut, re-caption or re-time clips made this way. No phone, emulator or screen recorder is needed, because the frames come from the app rendering itself.
metadata:
  title: "Recording an app into Instagram reels"
---

# Recording an app into Instagram reels

Produce short vertical clips of a real, running app: the app's own pixels, driven step by step, with captions burned into the video so the clip works with the sound off.

Four moves, in this order — **run the app locally → dry-run every selector → record frames → compose and encode.** Most of the wasted time in this job comes from recording first and discovering at the end that a control was invisible at that viewport, a caption sat under Instagram's own UI, or the encode ran 20% long.

## When to use

- A project needs a demo, tutorial or promo video for Reels, Shorts or TikTok, and the only source is the app itself.
- Someone asks to "record the steps", "make a video of my app", "give me clips to post", or "add text to the video".
- Existing clips need re-cutting, re-captioning or re-timing — frames are reusable, interactions are not.
- Not for editing a screen recording that already exists on a phone (that is a video-editor job), and not for a slideshow of static screenshots with no interaction.

## Method

1. **Serve the app locally.** Clone the repo (`git clone --depth 1`) and serve the directory; never point the recorder at the live site, where network flakiness and cookie banners ruin takes. `scripts/record.py` starts its own server, so nothing is left running afterwards.
2. **Render once and look.** Load the page headless, screenshot it, open the screenshot, and read the console (`page.on("pageerror")`). A JS error is a broken app, not a broken recorder.
3. **Dry-run every control** with `examples/dry_run.py`: it prints the box size and computed `display` for each candidate selector and screenshots after each click. Anything reporting `h: 0` renders invisible at this viewport no matter how cleanly the selector resolves — pick a different beat rather than filming a control nobody can see.
4. **Record at a phone viewport, scaled up.** `375x667` CSS pixels at `device_scale_factor = 1080/375` yields exactly `1080x1920`, and a 16px label occupies ~4% of frame width instead of ~3%. That is what makes app text readable in a vertical video without cropping later.
5. **Write the beats** as data: `{"kind": "tap" | "scroll" | "hold" | "type" | "script", "caption": ..., "step": n}`. Set the caption *before* the action — the pre-click frame and its ripple still show the previous screen.
6. **Pace it.** 2.0–2.6 s of hold after each action, ~0.35 s before it, ~1 s per scroll. Six or seven beats lands at 22–25 s, which is the length that gets watched.
7. **Compose and encode** with `scripts/compose.py`: brand background, the screenshot in a rounded card, one-line headline, per-step caption, step counter, progress line, optional end card. Repeat each still `round(dur*30)` times and pass `-r 30` on the **input** as well as the output.
8. **Verify the encode, not the source images.** Compare `ffmpeg -i` durations against the manifest total (within 0.5 s), then extract frames at the opening, middle and end card and actually look at them. Check each caption against what is on screen in that frame.
9. **Write the post copy** — hook, 2–4 sentences, CTA, hashtags. Caption links are not clickable on Instagram, so the burned-in end card is what carries the URL, and the same link belongs in the bio.

## Key files / entry points

- `scripts/record.py` — local server, browser session (fresh context per clip), beat runner, frame manifest.
- `scripts/compose.py` — 1080x1920 compositor, end card, ffmpeg encode. Edit `BRAND` for colours and fonts, `END_CARD` for the call to action.
- `references/layout.md` — the pixel grid, Instagram's safe areas, and what to change to rebrand.
- `references/gotchas.md` — the failures this method has hit, with the fix for each.
- `examples/dry_run.py` — the visibility check, as a template.
- `examples/clips_example.py` — a real three-clip build, as shipped.

## Gotchas

- **Every clip comes out ~20% too long.** The concat demuxer assumes 25 fps for stills, so frames counted at 30 fps play back 1.2x long. Fix by frame repetition plus `-r 30` on the input; a 22 s clip reporting 26.8 s is this bug.
- **A control exists but is invisible.** Elements can render at zero height at a phone width while still being clickable. The click succeeds, the screen never changes, and the caption describes something the viewer cannot see.
- **Selectors that match twice.** A desktop rail button and a mobile tab button often share `[data-view="..."]`; the desktop one is `display:none`, so Playwright waits for visibility and times out. Target the mobile element explicitly.
- **State leaking between clips.** Each clip is a separate post, so it must stand alone: a fresh browser context per clip resets localStorage, scroll position and half-finished flows.
- **Captions in the bottom 350 px.** That band is Instagram's caption, handle and CTA. Keep the headline and step caption in the top band above the app card and let the app fill the middle.
- **A caption bar pinned to the bottom of the card** looks correct in a video player and is unreadable on Instagram.
- **A headline that wraps to two lines with one short word.** Shrink the font (58 → 46 px) until it fits one line; the wrapped version collides with the card.
- **Drawing a pill onto a card-sized layer.** The layer must be canvas-sized, or the shape clips at the layer edge and the text runs out of it — it looks like "the pill is too narrow" and is really a coordinate-space bug.
- **Missing glyphs.** The rupee sign, arrows and some dashes are absent from many sans fonts and render as boxes; check the cmap before shipping a price.
- **Focus rings** left by a programmatic click read as "this is selected" for the rest of the clip — `document.activeElement.blur()`.

## Source projects

- `ntet-homoeopathy-cbt` — the three shipped Reels (exam blueprint, 15-day plan, CBT practice flow) were recorded with these scripts against this app. `examples/clips_example.py` is that build, including the silent `script` beat that fills a 20-question paper off-camera so the results screen has real data in it.
