# Gotchas

Failures this method has actually hit, with the fix. Skim before recording; each one costs a full re-record if you find it at the end.

## Recording

**A control exists but is invisible.** A palette, panel or button in the DOM can render at zero height at a phone width while still being clickable. The click "succeeds", the screen never changes, and the clip shows a caption about something the viewer cannot see. Check the box, not the selector:

```python
await pg.evaluate("(s)=>{const e=document.querySelector(s); const r=e.getBoundingClientRect();"
                  "return {h:r.height, display:getComputedStyle(e).display};}", sel)
```

If it is zero, either walk up the ancestors to find the hidden parent, or pick a different beat. Do not fake the panel.

**Selectors that match twice.** `[data-view="practice"]` often exists as both a desktop rail button and a mobile tab button; the desktop one is `display:none`, so Playwright waits for visibility and times out. Target the mobile one explicitly (`.tab-btn[data-view="practice"]`) or use `.first` only after checking which is visible.

**State leaking between clips.** Each clip is a separate post, so it should start clean. A fresh browser context per clip (`Session.page()`) resets localStorage, scroll position, and any half-finished flow. Without it, clip 3 opens on the results screen of clip 2.

**The pre-click frame carries the next caption.** If you set the caption after clicking, the 0.35 s frame before the click and the ripple frames still show the previous step's text while the screen is already changing. Set the caption first — `record.py` does this in `Session.record`.

**Focus rings.** A programmatic `element.click()` via `evaluate` leaves a focus outline on the button, which reads as "this is selected" for the rest of the clip. Blur it: `document.activeElement.blur()`.

**Trial counters and rate limits.** Apps with a free-trial quota count what your recording does. Answering 20 questions consumes 20 trial questions; that only affects the throwaway browser profile, but if the app writes to a server, use a test account.

**Service workers serving stale assets.** A PWA can keep serving the old build after you change files. In the recording context, `await ctx.add_init_script("navigator.serviceWorker && navigator.serviceWorker.getRegistrations().then(r=>r.forEach(x=>x.unregister()))")`, or serve with a cache-busting query string.

**Slow first paint.** Screenshot before fonts and layout settle and you get a flash of unstyled text in frame 1. Wait ~900 ms after `load`, and check the first screenshot.

## Encoding

**Every clip comes out ~20% too long.** The concat demuxer assumes 25 fps for stills, so a list of frames counted at 30 fps plays back 1.2x long. `compose.py` fixes it by repeating each still `round(dur*30)` times and passing `-r 30` on the *input* as well as the output. Verify after encoding — `ffmpeg -i out.mp4` and compare with the manifest total. A 22 s clip that reports 26.8 s is this bug.

**Colours look washed out or crushed.** JPEG input is full-range; without `scale=in_range=full:out_range=tv` the H.264 output is tagged oddly (`yuvj420p`). Keep the `scale` filter and `-pix_fmt yuv420p`.

**The video will not upload.** Instagram wants H.264 in an MP4 with `+faststart`. `-movflags +faststart` moves the index to the front; without it some uploaders reject the file.

## Composition

**Text drawn outside its rounded box.** If you draw a pill onto a layer, the layer must be the size of the canvas, not the size of the pill — otherwise the shape clips at the layer edge and the text runs out of it. This looks like "the pill is too narrow" and is really a coordinate-space bug.

**A headline that wraps to two lines with one short word.** Shrink the font until it fits on one line (58 → 46 px) instead of letting it wrap; the wrapped version collides with the card and looks like a mistake.

**Captions nobody can read.** See the safe-area table in `layout.md`: the bottom 350 px is Instagram's, not yours.

**Missing glyphs.** The rupee sign, arrows and some dashes are absent from many sans fonts and render as boxes. Check the cmap before shipping a price.

## Delivery

- No audio track. Instagram lets the user add trending audio; a silent MP4 is not a defect.
- One file per clip, named for its content (`ntet-reel-1-blueprint.mp4`), not `final_v2.mp4`.
- Re-encoding to change one caption means re-running compose, not re-recording — frames are cheap to reuse, interactions are not.
