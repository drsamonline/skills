"""Record an app walkthrough into frames + a manifest, ready for compose.py.

    from record import Session

    async with Session(root="/path/to/app", url="/index.html", out="/scratch/work/cap") as s:
        await s.record(clip_dict)

A clip is a dict:
    {"id": "clip1", "kicker": "MY APP · 2026", "headline": "One line, 1080px wide",
     "steps": 6, "beats": [beat, ...]}

A beat is a dict with a "kind":
    {"kind": "hold",   "dur": 3.0, "step": 1, "caption": "..."}
    {"kind": "tap",    "sel": "button:has-text('Start')", "step": 2, "caption": "...",
                       "hold": 2.4, "wait": 0.6}
    {"kind": "scroll", "target": "#features" | 480, "step": 3, "caption": "...",
                       "hold": 2.2, "dur": 1.0, "offset": 120}
    {"kind": "type",   "sel": "#search", "text": "memory", "step": 4, "caption": "...",
                       "hold": 2.0}
    {"kind": "script", "fn": coro_fn, "step": 5, "caption": "...", "hold": 2.2}

"fn" is awaited with the page: `async def fn(pg): ...` — the escape hatch for multi-step
setup you do not want on camera (filling a paper, turning a setting on, seeding data).
Set the caption BEFORE anything that changes the screen, or the pre-click frame keeps
the previous step's text.

Output: <out>/<clip id>/f0000.jpg ... and manifest.json with per-frame durations in
seconds and CSS-pixel tap coordinates for the ripple overlay.
"""
import asyncio
import functools
import http.server
import json
import math
import os
import socketserver
import threading

from playwright.async_api import async_playwright

# ---------------------------------------------------------------- config
W, H = 375, 667                 # CSS viewport; a phone width keeps app text large
DPR = 1080 / W                  # -> 1080x1920 screenshots
CHROMIUM = None                 # None = auto: playwright's build, else a system chromium
CHROMIUM_CANDIDATES = ("/usr/local/bin/chromium", "/usr/bin/chromium",
                       "/usr/bin/chromium-browser", "/usr/bin/google-chrome")
CHROME_ARGS = ["--no-sandbox", "--disable-dev-shm-usage", "--force-color-profile=srgb",
               "--hide-scrollbars", "--font-render-hinting=none"]
NO_SCROLLBAR_CSS = "::-webkit-scrollbar{display:none!important}*{scrollbar-width:none}"


def serve(root, port=8000):
    """Serve a directory on 127.0.0.1 in a daemon thread. Returns the port."""
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return port


class Rec:
    """Collects frames for one clip."""

    def __init__(self, page, outdir, meta):
        self.pg, self.dir, self.meta = page, outdir, meta
        os.makedirs(outdir, exist_ok=True)
        self.frames, self.caption, self.step, self.n = [], "", 1, 0

    async def snap(self, dur, caption=None, step=None):
        if caption is not None:
            self.caption = caption
        if step is not None:
            self.step = step
        path = f"{self.dir}/f{self.n:04d}.jpg"
        self.n += 1
        await self.pg.screenshot(path=path, type="jpeg", quality=93)
        self.frames.append({"file": path, "dur": dur, "caption": self.caption,
                            "step": self.step, "tap": None, "ripple": None})

    async def _ripple(self, x, y):
        last = self.frames[-1]
        for t in (0.0, 0.3, 0.6, 0.85, 1.0):
            self.frames.append({"file": last["file"], "dur": 0.08, "caption": last["caption"],
                                "step": last["step"], "tap": [x, y], "ripple": t})

    async def tap(self, sel, wait=0.6):
        el = self.pg.locator(sel).first
        try:
            await el.scroll_into_view_if_needed(timeout=4000)
        except Exception:
            pass
        box = await el.bounding_box()
        await self.snap(0.35)                      # the frame before the tap
        if box:
            await self._ripple(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        await el.click(timeout=10000)
        await self.pg.wait_for_timeout(int(wait * 1000))

    async def abs_y(self, sel):
        return await self.pg.evaluate(
            "(s)=>{const e=document.querySelector(s); if(!e) return null;"
            "return e.getBoundingClientRect().top + window.scrollY;}", sel)

    async def scroll_to(self, y, dur=1.0, steps=9):
        y0 = await self.pg.evaluate("window.scrollY")
        for i in range(1, steps + 1):
            ease = 0.5 - 0.5 * math.cos(math.pi * i / steps)   # ease in-out
            await self.pg.evaluate(f"window.scrollTo(0,{y0 + (y - y0) * ease})")
            await self.snap(dur / steps)

    def save(self):
        total = round(sum(f["dur"] for f in self.frames), 2)
        meta = dict(self.meta, total=total, frames=len(self.frames))
        with open(f"{self.dir}/manifest.json", "w") as fh:
            json.dump({"meta": meta, "frames": self.frames}, fh)
        print(f"  {self.meta['id']}: {len(self.frames)} frames, {total:.1f}s")
        return total


class Session:
    """Browser + local server + a fresh context per clip."""

    def __init__(self, root, url, out, port=8000):
        self.root, self.url, self.out, self.port = root, url, out, port

    async def __aenter__(self):
        serve(self.root, self.port)
        self._pw = await async_playwright().start()
        self.browser = await self._launch()
        return self

    async def _launch(self):
        """Use an explicit binary, else playwright's build, else a system chromium."""
        if CHROMIUM:
            return await self._pw.chromium.launch(executable_path=CHROMIUM, args=CHROME_ARGS)
        try:
            return await self._pw.chromium.launch(args=CHROME_ARGS)
        except Exception as e:
            for path in CHROMIUM_CANDIDATES:
                if os.path.exists(path):
                    return await self._pw.chromium.launch(executable_path=path, args=CHROME_ARGS)
            raise RuntimeError(
                "no chromium available: run `playwright install chromium`, or install a "
                "system chromium and set CHROMIUM to its path") from e

    async def __aexit__(self, *exc):
        await self.browser.close()
        await self._pw.stop()

    async def page(self):
        """A fresh context, so no clip inherits another clip's state."""
        ctx = await self.browser.new_context(
            viewport={"width": W, "height": H}, device_scale_factor=DPR,
            is_mobile=True, has_touch=True)
        pg = await ctx.new_page()
        pg.on("pageerror", lambda e: print("  PAGE ERROR:", e))
        await pg.goto(f"http://127.0.0.1:{self.port}{self.url}", wait_until="load")
        await pg.add_style_tag(content=NO_SCROLLBAR_CSS)
        await pg.wait_for_timeout(900)
        return ctx, pg

    async def record(self, clip):
        ctx, pg = await self.page()
        meta = {k: clip[k] for k in ("id", "kicker", "headline", "steps")}
        rec = Rec(pg, f"{self.out}/{clip['id']}", meta)
        for beat in clip["beats"]:
            kind = beat["kind"]
            # caption first: the frame captured before an action must already carry its text
            rec.caption = beat.get("caption", rec.caption)
            rec.step = beat.get("step", rec.step)

            if kind == "hold":
                await rec.snap(beat["dur"])
            elif kind == "tap":
                await rec.tap(beat["sel"], wait=beat.get("wait", 0.6))
                await rec.snap(beat.get("hold", 2.2))
            elif kind == "scroll":
                target = beat["target"]
                y = target if isinstance(target, (int, float)) else await rec.abs_y(target)
                y = 0 if y is None else max(0, y if isinstance(target, (int, float))
                                            else y - beat.get("offset", 120))
                await rec.scroll_to(y, dur=beat.get("dur", 1.0))
                await rec.snap(beat.get("hold", 2.0))
            elif kind == "type":
                el = pg.locator(beat["sel"]).first
                try:
                    await el.scroll_into_view_if_needed(timeout=4000)   # a field below the fold
                except Exception:                                       # types invisibly
                    pass
                await rec.snap(0.35)
                await el.fill(beat["text"])
                await pg.wait_for_timeout(350)
                await rec.snap(beat.get("hold", 2.0))
            elif kind == "script":
                await beat["fn"](pg)
                await rec.snap(beat.get("hold", 2.0))
            else:
                raise ValueError(f"unknown beat kind: {kind}")
        total = rec.save()
        await ctx.close()
        return total
