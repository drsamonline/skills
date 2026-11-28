# Layout — 1080x1920

Every number below is what `scripts/compose.py` ships with. Change them in one place; if you move text into the bottom third, read the safe-area note first.

## The frame

| Region | y range | What lives there | Notes |
|---|---|---|---|
| Top edge | 0–100 | nothing | Instagram overlays "Reels" and the camera affordance here |
| Kicker + step counter | 104 | small caps, accent colour, left / right aligned | 25 px semibold |
| Headline | 140 | one line, 58→46 px bold, shrinks to fit | two lines only if a single line cannot fit at 46 px |
| Step caption | 226 | up to 2 lines, 37 px regular | changes every beat |
| Progress line | 344–351 | 7 px rounded bar, fills left to right | reads as a timeline, costs nothing |
| App card | 372–1830 | the screenshot, 820x1458, radius 26 | 9:16, so the whole phone screen shows |
| Bottom 90 px | 1830–1920 | background only | Instagram's caption and buttons cover roughly the bottom 350 px |

## Why the card instead of full-bleed

Full-bleed app screenshots look more authentic but leave nowhere to put text: the app's own header and tab bar occupy the top and bottom, and the middle is the content you want visible. A card at 820 px wide keeps app body text at roughly 13–14 pt on a phone, which is readable, and gives you a dedicated band for the headline and caption.

If the app has no mobile layout, the card is not optional — a desktop screenshot scaled to 1080 wide makes 12 px UI text illegible.

## Safe areas

Instagram covers:

- **bottom ~350 px** — caption, handle, audio, and the CTA button;
- **right ~180 px** — like, comment, share, save;
- **top ~100 px** — "Reels" label.

Consequence: a caption bar pinned to the bottom of the app card is invisible on Instagram even though it looks correct in a video player. That is why captions sit above the card, and why the card's bottom edge is allowed to sit under the overlay (it only holds the app's tab bar).

## End card

Centred block, roughly y 660–1120:

- kicker (reuses the clip's kicker unless `END_CARD["kicker"]` is set),
- headline — 104 px bold, usually "Buy now",
- price line — 40 px, optional,
- URL pill — 32 px bold in the accent colour, 30 px padding, keeps the pill off the frame edges,
- note — 33 px muted, e.g. the UPI ID.

Two seconds is enough to read a short URL and not enough to be annoying. The clip's fade-out starts inside the end card, which is intentional.

## Rebranding

`BRAND` in `scripts/compose.py` is the whole theme: two background colours, the glow, accent, ink, muted, three font paths, headline sizes, caption sizes. Swap the accent and the two background stops and the whole look changes; nothing else needs touching.

Fonts are whatever is installed. Check with `fc-match -f '%{file}\n' "Noto Sans:bold"` and confirm the glyphs you need exist — the rupee sign (U+20B9) is missing from some sans fonts and renders as an empty box:

```python
from fontTools.ttLib import TTFont
print(0x20B9 in TTFont(path).getBestCmap())
```
