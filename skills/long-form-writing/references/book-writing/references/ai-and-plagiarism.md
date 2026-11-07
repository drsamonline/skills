# AI-tell and plagiarism checking, and fixing

Run this in **Phase 5**, before the final build, and again on the built HTML.
The goal is not to fool a detector — it is to make the prose measurably human and
to prove every borrowed idea is attributed.

## What is honest to claim

- **Never claim a text is "undetectable" by AI detectors.** Detector scores vary
  run to run and flag human writing. Report heuristics and honest numbers only.
- **A true plagiarism scan needs a licensed corpus** (Turnitin, iThenticate,
  Copyscape). Say so; do not imply a heuristic is that scan.
- The strongest defence is structural: a named source beside every substantive
  claim, short attributed quotations, and a voice that varies.

## The AI-tell check

```
python3 ai_check.py <content_module> --draft <supplied-manuscript> --report AI_Plagiarism_Report.md
```

It measures and prints:

| Metric | Human-like target |
|---|---|
| sentence-length **standard deviation** | high — 8+ (flat machine prose ~4–6) |
| shortest / longest sentence | a wide range, incl. one under 6 words and one over 25 |
| **em-dash density** | ≤ ~6 per 1,000 words |
| **stock AI phrases** | 0 (list in `content-rules.md`) |
| **internal 6-gram repeats** | structural only (labels, headings) |
| **overlap with the supplied draft** | expected — the author's own carried-forward text |

### Fixing the flags

- **Flat rhythm / low sd:** break a run of medium sentences — cut one to three
  words, let one run long. Do not add filler; cut instead.
- **Em-dashes:** convert to a comma clause, a colon, a semicolon or a
  parenthesis — vary the swap, do not use the same substitute each time.
- **Stock phrases:** rotate each through a plain synonym.
- **Repeated structural sentences:** vary chapter openers, callout leads and
  composite-scene labels so they stop reading as a template.
- **Re-measure** after fixing and report the before/after numbers.

## The plagiarism check

1. **Quotation inventory.** List every quoted phrase; confirm each is short and
   attributed in the same sentence. `ai_check.py` prints them.
2. **No extended passage reproduced.** Longer ideas are paraphrased and credited
   in prose, and listed in the Bibliography.
3. **Spot-check distinctive phrases.** Search a few phrases written for the book;
   no verbatim match is the expected result for original phrasing.
4. **Draft overlap is not plagiarism** when it is the author's own supplied text
   carried forward — label it as such.
5. **Attribution audit.** Confirm every substantive claim maps to a named source
   in `99_AUDIT_LOG.md`. Contested claims are given as the view of whoever holds
   them, not asserted.

## Deliver

Save `AI_Plagiarism_Report.md` (measurements + reading + limitations) and deliver
it alongside the book. It is a supporting file, not part of the manuscript.
