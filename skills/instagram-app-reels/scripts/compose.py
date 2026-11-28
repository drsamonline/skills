"""Compose recorded frames into 1080x1920 Instagram clips and encode them.

    python3 compose.py --cap /scratch/work/cap --out /scratch/work/out clip1 clip2

Reads <cap>/<clip>/manifest.json (written by record.py), writes <out>/<clip>.mp4.

Edit BRAND and END_CARD for the look and the call to action. Everything else is
geometry that has already been tuned for Instagram's safe areas — see
references/layout.md before moving things around.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --------------------------------------------------------------- brand
BRAND = {
    "bg_top": (12, 30, 27),
    "bg_bottom": (6, 14, 12),
    "glow": (13, 107, 98, 62),
    "accent": (127, 216, 198),
    "ink": (244, 249, 247),
    "muted": (150, 176, 170),
    "caption_ink": (226, 238, 234),
    "font_bold": "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "font_regular": "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "font_semibold": "/usr/share/fonts/truetype/noto/NotoSans-SemiBold.ttf",
    "headline_sizes": (58, 54, 50, 46),   # shrink until the headline fits one line
    "caption_size": 37,
    "caption_size_small": 33,
}

# ------------------------------------------------------------- end card
END_CARD = {
    "enabled": True,
    "dur": 2.0,
    "kicker": None,                 # None = reuse the clip's kicker
    "headline": "Buy now",
    "price": "₹1,499 · one time · 12 months · one user",
    "url": "example.com/your-page",
    "note": "",                     # e.g. "UPI · yourid@bank"
}

# ------------------------------------------------------------- geometry
CW, CH = 1080, 1920
CX, CY, CWD, CHT = 130, 372, 820, 1458          # app card
SRC_W, SRC_H = 375, 667                          # the CSS viewport used by record.py
FPS = 30


def _f(path, size):
    """Load a font, falling back through the brand fonts if this weight is not installed."""
    for p in (path, BRAND["font_bold"], BRAND["font_regular"]):
        if p and os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def bg_canvas():
    im = Image.new("RGB", (CW, CH), BRAND["bg_bottom"])
    d = ImageDraw.Draw(im)
    t0, b0 = BRAND["bg_top"], BRAND["bg_bottom"]
    for y in range(CH):
        t = y / CH
        d.line([(0, y), (CW, y)],
               fill=(int(t0[0] + (b0[0] - t0[0]) * t),
                     int(t0[1] + (b0[1] - t0[1]) * t),
                     int(t0[2] + (b0[2] - t0[2]) * t)))
    glow = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([CX - 260, CY - 320, CX + CWD + 260, CY + 420],
                                 fill=BRAND["glow"])
    im = Image.alpha_composite(im.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(140)))
    d = ImageDraw.Draw(im)
    for x in range(0, CW, 44):
        for y in range(0, CH, 44):
            d.point((x, y), fill=(255, 255, 255, 8))
    return im


def card_shadow():
    sh = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle(
        [CX - 6, CY + 10, CX + CWD + 6, CY + CHT + 26], 34, fill=(0, 0, 0, 130))
    return sh.filter(ImageFilter.GaussianBlur(30))


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, font, small, maxw, maxlines=2):
    lines = wrap(draw, text, font, maxw)
    if len(lines) > maxlines:
        font, lines = small, wrap(draw, text, small, maxw)[:maxlines]
    return lines, font


def shadowed(im, xy, text, font, fill, blur=8, alpha=180):
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((xy[0], xy[1] + 3), text, font=font, fill=(0, 0, 0, alpha))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(im).text(xy, text, font=font, fill=fill)


def compose_frame(bg, shadow, f, meta, t, total):
    im = bg.copy()
    im.alpha_composite(shadow)

    shot = Image.open(f["file"]).convert("RGB").resize((CWD, CHT), Image.LANCZOS)
    mask = Image.new("L", (CWD, CHT), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, CWD, CHT], 26, fill=255)
    im.paste(shot, (CX, CY), mask)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([CX, CY, CX + CWD, CY + CHT], 26, outline=(255, 255, 255, 34), width=2)

    d.text((CX, 104), meta["kicker"], font=_f(BRAND["font_semibold"], 25), fill=BRAND["accent"])
    sc = f"{f['step']:02d} / {meta['steps']:02d}"
    fs = _f(BRAND["font_semibold"], 24)
    d.text((CX + CWD - d.textlength(sc, font=fs), 104), sc, font=fs, fill=BRAND["muted"])

    head, font = None, None
    for size in BRAND["headline_sizes"]:
        cand = _f(BRAND["font_bold"], size)
        if d.textlength(meta["headline"], font=cand) <= CWD:
            head, font = [meta["headline"]], cand
            break
    if head is None:
        font = _f(BRAND["font_bold"], BRAND["headline_sizes"][-1])
        head = wrap(d, meta["headline"], font, CWD)[:2]
    y = 140
    for ln in head:
        shadowed(im, (CX, y), ln, font, BRAND["ink"])
        y += int(font.size * 1.16)
    d = ImageDraw.Draw(im)

    cap_font = _f(BRAND["font_regular"], BRAND["caption_size"])
    small = _f(BRAND["font_regular"], BRAND["caption_size_small"])
    cap, cfont = fit_lines(d, f["caption"] or "", cap_font, small, CWD, maxlines=2)
    cy = 226
    for ln in cap:
        shadowed(im, (CX, cy), ln, cfont, BRAND["caption_ink"], blur=7, alpha=165)
        cy += int(cfont.size * 1.24)

    d = ImageDraw.Draw(im)
    pw = int(CWD * min(1.0, t / total))
    d.rounded_rectangle([CX, 344, CX + CWD, 351], 4, fill=(255, 255, 255, 32))
    if pw > 4:
        d.rounded_rectangle([CX, 344, CX + pw, 351], 4, fill=BRAND["accent"])

    if f.get("tap"):
        rx = CX + f["tap"][0] * (CWD / SRC_W)
        ry = CY + f["tap"][1] * (CHT / SRC_H)
        tr = f["ripple"] or 0
        ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        r = 26 + 46 * tr
        od.ellipse([rx - r, ry - r, rx + r, ry + r], outline=(255, 255, 255, int(235 * (1 - tr))), width=4)
        od.ellipse([rx - 13, ry - 13, rx + 13, ry + 13], fill=(255, 255, 255, int(210 * (1 - tr))))
        im.alpha_composite(ov)
    return im.convert("RGB")


def end_card(meta):
    im = bg_canvas()
    d = ImageDraw.Draw(im)
    kicker = END_CARD["kicker"] or meta["kicker"]
    f_k, f_h = _f(BRAND["font_semibold"], 30), _f(BRAND["font_bold"], 104)
    f_p, f_u = _f(BRAND["font_regular"], 40), _f(BRAND["font_bold"], 32)
    f_n = _f(BRAND["font_regular"], 33)

    d.text(((CW - d.textlength(kicker, font=f_k)) / 2, 660), kicker, font=f_k, fill=BRAND["accent"])
    d.text(((CW - d.textlength(END_CARD["headline"], font=f_h)) / 2, 712),
           END_CARD["headline"], font=f_h, fill=BRAND["ink"])
    if END_CARD["price"]:
        d.text(((CW - d.textlength(END_CARD["price"], font=f_p)) / 2, 858),
               END_CARD["price"], font=f_p, fill=(196, 214, 208))
    if END_CARD["url"]:
        tw = d.textlength(END_CARD["url"], font=f_u)
        x1, x2 = (CW - tw) / 2 - 30, (CW + tw) / 2 + 30
        d.rounded_rectangle([x1, 950, x2, 1036], 22, fill=(8, 16, 14, 235),
                            outline=BRAND["accent"] + (110,), width=2)
        d.text(((CW - tw) / 2, 968), END_CARD["url"], font=f_u, fill=BRAND["accent"])
    if END_CARD["note"]:
        d.text(((CW - d.textlength(END_CARD["note"], font=f_n)) / 2, 1082),
               END_CARD["note"], font=f_n, fill=BRAND["muted"])
    return im.convert("RGB")


def build(cap_dir, out_dir, clip, end_card_on=True):
    src = f"{cap_dir}/{clip}"
    man = json.load(open(f"{src}/manifest.json"))
    meta, frames = man["meta"], man["frames"]
    total = sum(f["dur"] for f in frames)

    work = f"{out_dir}/{clip}"
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work, exist_ok=True)
    bg, shadow = bg_canvas(), card_shadow()

    concat, t = [], 0.0
    for i, f in enumerate(frames):
        im = compose_frame(bg, shadow, f, meta, t, total)
        path = f"{work}/c{i:04d}.jpg"
        im.save(path, quality=90)
        # repeat each still once per output frame: exact CFR timing, no drift
        concat.extend([f"file '{path}'\n"] * max(1, round(f["dur"] * FPS)))
        t += f["dur"]

    if end_card_on and END_CARD["enabled"]:
        path = f"{work}/c_end.jpg"
        end_card(meta).save(path, quality=92)
        concat.extend([f"file '{path}'\n"] * round(END_CARD["dur"] * FPS))
        total += END_CARD["dur"]

    open(f"{work}/list.txt", "w").write("".join(concat))

    out = f"{out_dir}/{clip}.mp4"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    vf = (f"scale={CW}:{CH}:in_range=full:out_range=tv,format=yuv420p,"
          f"fade=t=in:st=0:d=0.35,fade=t=out:st={max(0, total - 0.5):.2f}:d=0.5")
    cmd = [ff, "-y", "-f", "concat", "-safe", "0", "-r", str(FPS), "-i", f"{work}/list.txt",
           "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ffmpeg failed:", r.stderr[-1500:])
        return None
    print(f"{clip}: {total:.1f}s -> {out}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", required=True, help="directory holding <clip>/manifest.json")
    ap.add_argument("--out", required=True, help="where the mp4s go")
    ap.add_argument("--no-end-card", action="store_true")
    ap.add_argument("clips", nargs="*", help="clip ids; default all directories with a manifest")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    clips = a.clips or [d for d in sorted(os.listdir(a.cap))
                        if os.path.exists(f"{a.cap}/{d}/manifest.json")]
    for c in clips:
        build(a.cap, a.out, c, end_card_on=not a.no_end_card)
