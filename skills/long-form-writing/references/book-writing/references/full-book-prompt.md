# The one-shot full-book prompt (template)

A prompt that asks for a complete book in a **single uninterrupted output**,
rather than the five-phase pipeline. The five-phase workflow is preferred because
it verifies as it builds; reach for this template only when the user explicitly
wants one-pass generation (e.g. a quick clinical monograph), and still run the QA
gate over whatever it produces.

It was written for a clinical-homeopathy book, so it carries that domain's
requirements (the red-flags chapter, the safety notices, the audience tracks).
Adapt the intake and the 14-part sequence to the actual book.

## The prompt

```
Act as an expert clinical author, book designer, and front-end engineer.

In this first turn, reply ONLY with this exact sentence:
"Please provide: (1) Book Title, (2) Subtitle, (3) Clinical Topic & Focus, and (4) Recurring Characters (names, roles, ages)."

When I reply with those 4 details, generate the COMPLETE, fully realized, publication-ready HTML book in ONE uninterrupted output. No chat, no introductory text, no summary, no markdown wrapper, no truncation, no placeholder comments. Start immediately with <!DOCTYPE html> and end with </html>.

CORE EXECUTION SPECIFICATIONS (ENFORCE STRICTLY UPON RECEIVING DETAILS):

1. AUTHOR & METADATA (NO HALLUCINATIONS):
- Author: Dr. Sohil Momin, B.H.M.S.
- Author Bio: Homoeopathic physician, Resident Medical Officer in hospital practice, and medical author with over 15 years of bedside and clinical experience.
- Integrity Rule: Zero physical print hallucinations (no fake ISBNs, fake street publishers, or fabricated historic dates). State clearly: Open Digital Monograph Edition. All cases are anonymized clinical composites.

2. PRINT ARCHITECTURE & CSS:
- Form factor: Strict A4 print CSS (@page { size: A4; margin: 0; }, .page { width: 210mm; min-height: 297mm; page-break-after: always; break-after: page; box-sizing: border-box; }).
- Typography: Serif body ("Iowan Old Style", Palatino, Georgia, serif), 10.5–11.5pt, line-height 1.55–1.62, margins 18–20mm.
- Theme System: Select one topic-appropriate palette and define CSS variables strictly: --ink, --accent, --accent-2, --accent-3, --paper, --line, --warn, --gold.
- Layout Components: Drop caps, running folios (title/section/page), pull quotes, .box (.warn, .gold, .accent), .rx cards (<dl> layout), .flow containers.
- Visuals: 100% inline, hand-coded SVGs only (line-art/pen-and-ink style). Required: Cover artwork, author portrait sketch, flowcharts for every clinical chapter, and back colophon emblem. No external URLs, no raster assets.

3. CLINICAL PEDAGOGY & VOICE:
- Bedside Storytelling Mode: Never present dry lecture bullets. Every principle, rubric, remedy, and red flag must arrive wrapped inside a concrete scene featuring the recurring characters.
- Rhythm: Hard sentence length variance. No consecutive passive voice.
- Banned Vocabulary: delve, tapestry, realm, navigate the landscape, in today's world, it's important to note, unlock, embark, moreover, furthermore, in conclusion, journey, leverage, robust, seamless.

4. MEDICAL SAFETY & ETHICS (NON-NEGOTIABLE):
- Explicitly state: Homeopathy never replaces emergency resuscitation, mechanical ventilation, IV fluids, surgical consults, or indicated antibiotics.
- Dedicated early Red Flags chapter: Every danger sign dramatized through a scene explaining why immediate hospital referral is mandatory.
- Explicit notice: Contested scientific evidence base; NO homeopathic vaccines; dosage advice is general guidance subject to a licensed clinician.

5. MANDATORY 14-PART UNBROKEN SEQUENCE:
1. Cover Page (Kicker, Title, Subtitle, Author, Hand-coded SVG illustration)
2. Safety Notice & Red Flags Box
3. About the Author (Factual bio, Author SVG sketch, composite notice)
4. Introduction & Reader Tracks (Caregiver, Student, Teacher pathways)
5. Page-Indexed Table of Contents
6. Part Dividers (Numeral, title, standalone narrative vignette)
7. Clinical Chapters (Story lead-in, hand-coded SVG flowchart with caption, .rx remedy cards with modalities/mini-scenes, safety box, 3 study questions)
8. Student & Master Section (Non-verbal case intake, repertory funnel, look-alike remedy comparison table, 10 student prescribing mistakes)
9. Solved Casebook (Minimum 5 complete cases with "Write your prescription first" prompt, differential, and follow-up)
10. Conclusion & Colophon (Narrative close returning to characters)
11. Plain-English Glossary (20+ terms without jargon)
12. Quick Reference Table & Master Index
13. Closing Verse (Centered original poem)
14. Back Cover (Summary, pull quote, colophon SVG, disclaimer)

Respond now ONLY with the required intake prompt.
```

## How it maps to this skill

- The **14-part sequence** is this skill's front matter + body + back matter,
  spelled out for a clinical monograph. The skill's Phase 4 already builds the
  glossary, index, bibliography and colophon; the extra here is the dedicated
  early **Red Flags** chapter and the **Reader Tracks** page.
- The **safety notices** are `references/clinical-safety.md`; the **banned
  vocabulary** is `content-rules.md` §Language; the **inline-SVG-only** rule is
  `references/figures.md`.
- The **theme variables** (`--ink`, `--accent`, `--paper`, …) are the same idea as
  `scripts/themes.py`; a topic-appropriate palette is one `THEMES` entry.
- Because it demands one unbroken output, it skips the phased verification. If you
  use it, still run the QA gate (`qa-checklist.md`) and `verify_figures.py` on the
  result.
