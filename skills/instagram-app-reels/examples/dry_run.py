"""Template for step 3 — dry-run every control your story needs, then LOOK at the shots.

    python3 examples/dry_run.py

Edit ROOT / URL / CANDIDATES, run it, open the PNGs it writes, and only then write the
clip beats. Anything that reports h=0 or display=none at this viewport will not show up
in the video, no matter how nicely the selector resolves.
"""
import asyncio
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (os.environ.get("REEL_SCRIPTS"),
             os.path.join(HERE, "..", "scripts"),
             "/scratch/skills/instagram-app-reels/scripts"):
    if cand and os.path.exists(os.path.join(cand, "record.py")):
        sys.path.insert(0, cand)
        break
else:
    raise SystemExit("cannot find record.py — set REEL_SCRIPTS to the skill's scripts/ dir")
from record import Session  # noqa: E402

ROOT = "/path/to/app"           # directory to serve
URL = "/index.html"             # page to open
OUT = "/scratch/work/dry"       # where the PNGs go

# One entry per control you intend to use, in story order.
CANDIDATES = [
    ("nav-practice", '.tab-btn[data-view="practice"]'),
    ("start-paper", '[data-paper="sprint"]'),
    ("first-option", "#qOptions .opt"),
    ("submit", "#submitBtn"),
]


async def main():
    os.makedirs(OUT, exist_ok=True)
    async with Session(root=ROOT, url=URL, out="/scratch/work/_unused", port=8810) as s:
        ctx, pg = await s.page()
        for name, sel in CANDIDATES:
            report = await pg.evaluate(
                """(sel)=>{const e=document.querySelector(sel);
                   if(!e) return {missing:true};
                   const r=e.getBoundingClientRect(), cs=getComputedStyle(e);
                   return {w:Math.round(r.width), h:Math.round(r.height),
                           top:Math.round(r.top), display:cs.display, vis:cs.visibility,
                           text:(e.innerText||'').slice(0,40)};}""", sel)
            print(f"{name:14} {sel:38} {report}")
            if report.get("missing") or report.get("h", 0) == 0:
                print(f"   ^^ NOT VISIBLE — pick another beat or another selector")
                continue
            try:
                await pg.click(sel, timeout=5000)
                await pg.wait_for_timeout(600)
                await pg.screenshot(path=f"{OUT}/{name}.png")
            except Exception as e:
                print(f"   click failed: {e}")
        await ctx.close()


asyncio.run(main())
