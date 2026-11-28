"""A complete three-clip build, as actually shipped for an exam-prep app.

    python3 examples/clips_example.py          # records frames into /scratch/work/cap
    python3 scripts/compose.py --cap /scratch/work/cap --out /scratch/work/out

Selectors here belong to one specific app — the shapes (beats, holds, step numbers) are
what you reuse. Two habits worth copying:

  * the silent `script` beat fills a form without burning 15 s of screen time on it,
  * every clip opens on a state the viewer can recognise, so it works standalone in a
    feed where nobody saw the previous clip.
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

ROOT = "/scratch/work/ntet"
URL = "/app/index.html"


async def fill_paper(pg, n=18):
    """Answer most of a 20-question paper off-camera.

    The app can reveal its own key with instant feedback on; we read the correct option
    from the DOM, leave two answers deliberately wrong, then turn the setting back off.
    """
    async def instant(on):
        if await pg.evaluate("()=>document.querySelector('#instantToggle').checked") != on:
            await pg.evaluate("()=>document.querySelector('#instantToggle').click()")
            await pg.wait_for_timeout(150)

    await instant(True)
    for _ in range(n):
        await pg.click('#qOptions .opt[data-opt="0"]')
        await pg.wait_for_timeout(120)
        key = await pg.evaluate("()=>{const e=document.querySelector('#qOptions .opt.is-correct');"
                                "return e?+e.getAttribute('data-opt'):0;}")
        qidx = int((await pg.inner_text("#qIndex")).split("/")[0].replace("Q", "").strip())
        if qidx not in (6, 13) and key != 0:
            await pg.click(f'#qOptions .opt[data-opt="{key}"]')
            await pg.wait_for_timeout(50)
        if qidx < 20:
            await pg.click("#nextQ")
            await pg.wait_for_timeout(60)
    await instant(False)
    await pg.evaluate("()=>document.activeElement && document.activeElement.blur()")


CLIPS = [
    {
        "id": "clip1", "kicker": "NTET 2026 · HOMOEOPATHY",
        "headline": "Know where the 100 marks sit", "steps": 6,
        "beats": [
            {"kind": "hold", "dur": 3.0, "step": 1,
             "caption": "100 questions. 120 minutes. 50% to qualify."},
            {"kind": "tap", "sel": "button:has-text('By weight')", "step": 2, "hold": 2.4,
             "caption": "Sort by weight — and the marks concentrate."},
            {"kind": "scroll", "target": "#weightageBars", "step": 2, "hold": 2.2,
             "caption": "Units 1, 4 and 6 alone carry 50 marks."},
            {"kind": "tap", "sel": '#weightageBars .bar-row[data-unit="6"]', "step": 3, "hold": 2.4,
             "caption": "Tap a unit to see what it actually asks."},
            {"kind": "scroll", "target": "#inspectorCard", "step": 4, "hold": 2.4, "dur": 1.2,
             "caption": "Syllabus points, key terms, its study days."},
            {"kind": "tap", "sel": "#inspectorJump", "step": 5, "hold": 2.4, "wait": 0.7,
             "caption": "One tap takes you to that study day."},
            {"kind": "hold", "dur": 2.8, "step": 6,
             "caption": "Blueprint → plan → practice. That's the whole loop."},
        ],
    },
    {
        "id": "clip2", "kicker": "NTET 2026 · HOMOEOPATHY",
        "headline": "15 days, one idea at a time", "steps": 6,
        "beats": [
            {"kind": "tap", "sel": '.tab-btn[data-view="plan"]', "step": 1, "hold": 2.4,
             "caption": "15 days, three phases, short sittings."},
            {"kind": "scroll", "target": "#dayGrid", "step": 2, "hold": 2.2, "dur": 0.9,
             "caption": "One tile per day. Ticked as you go."},
            {"kind": "tap", "sel": '#dayGrid .day-tile[data-day="1"]', "step": 3, "hold": 2.4,
             "caption": "Day 1 — the three levels of teaching."},
            {"kind": "scroll", "target": "#dayNotes", "step": 4, "hold": 2.4, "dur": 1.1,
             "caption": "Four plain-English points. No jargon."},
            {"kind": "scroll", "target": "#dayTraps", "step": 5, "hold": 2.4,
             "caption": "Then three exam traps and one task."},
            {"kind": "tap", "sel": "#dayTerms .term-chip", "step": 6, "hold": 2.6, "wait": 0.8,
             "caption": "Every term opens a one-sentence definition."},
            {"kind": "hold", "dur": 2.2,
             "caption": "Read it after OPD. Fifteen minutes a day."},
        ],
    },
    {
        "id": "clip3", "kicker": "NTET 2026 · HOMOEOPATHY",
        "headline": "Rehearse the real CBT", "steps": 7,
        "beats": [
            {"kind": "tap", "sel": '.tab-btn[data-view="practice"]', "step": 1, "hold": 2.4,
             "caption": "Six papers, built to the real pattern."},
            {"kind": "tap", "sel": '[data-paper="sprint"]', "step": 2, "hold": 2.4, "wait": 0.7,
             "caption": "Start small: 20 questions, 20 minutes."},
            {"kind": "scroll", "target": 190, "step": 3, "hold": 1.6, "dur": 0.6,
             "caption": "Answer. The clock runs like the exam."},
            {"kind": "tap", "sel": "#qOptions .opt", "step": 3, "hold": 2.2,
             "caption": "Answer. The clock runs like the exam."},
            {"kind": "tap", "sel": "#flagQ", "step": 4, "hold": 1.8,
             "caption": "Flag whatever you are unsure of."},
            {"kind": "tap", "sel": "#nextQ", "step": 4, "hold": 1.8,
             "caption": "Move on. Nothing gets lost."},
            {"kind": "script", "fn": fill_paper, "step": 5, "hold": 2.4,
             "caption": "Then drill the one unit you keep missing."},
            {"kind": "tap", "sel": "#submitBtn", "step": 6, "hold": 2.0,
             "caption": "Submit when the clock stops."},
            {"kind": "tap", "sel": "#confirmYes", "step": 7, "hold": 2.6, "wait": 1.2,
             "caption": "Score, unit accuracy, and the rationale for every key."},
            {"kind": "hold", "dur": 2.6,
             "caption": "Then you know exactly what to fix next."},
        ],
    },
]


async def main():
    async with Session(root=ROOT, url=URL, out="/scratch/work/cap", port=8802) as s:
        for clip in CLIPS:
            await s.record(clip)


if __name__ == "__main__":
    asyncio.run(main())
