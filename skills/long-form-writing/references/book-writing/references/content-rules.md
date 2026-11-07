# Writing and honesty rules

These rules keep a book that talks about evidence honest. They are not style preferences; treat them as constraints.

## Sourcing

- **Every substantive claim is one of three things:** attributed to a named source, presented as a classical or observational finding, or removed.
- **Never write "research shows", "studies say", or "science tells us"** without naming the study or author in the same breath.
- **Mark folklore as folklore.** Popular figures (for example the "twenty-one-day rule") get flagged as folklore and their origin stated, not repeated as fact.
- **No invented studies, authors, dates, or statistics.** If it cannot be named, it does not go in.
- **Attribute contested claims to whoever makes them**, rather than asserting them in the book's own voice.
- **Add a note on sources** at the end of the bibliography stating that the case material is illustrative and composite, and that no statistic is presented as measured unless attributed.

## Case material

- Any recurring character is a **composite**, built from common patterns, not a real person.
- **Label every scene** drawn from that character's life as an illustrative composite case.
- Never imply a composite case is a clinical record.

## Deduplication across the whole book

- Keep a running `99_DEDUP_REGISTRY.md` of phrases and concepts already used.
- Deduplicate across the **whole book**, not just within a chapter. A phrase that
  appeared in chapter 2 must not reappear in chapter 9.
- **For a series, keep a `99_SERIES_DEDUP_REGISTRY.md` as well.** A phrase,
  framing or example already used in an earlier book must not repeat in a later
  one, and each book must still stand alone for a reader who starts with it.
- Vary the fixed structural sentences (chapter openers, callout leads) so they
  do not read as a template.

## Visuals and tables

- **Every visual is an SVG**, embedded in the DOCX. No external image links. The
  only bitmaps allowed are the author's own artwork — a scanned sketch or a
  photograph — cleaned with `prep_sketch.py` and placed with
  `booklib.sketch_block()`. See `references/sketches.md`.
- **Every table is fully populated.** No "TBD", no empty rows, no placeholders.
- **A book carries figures, not just prose.** Any process, comparison, hierarchy
  or classification in the text gets a matching figure — a flowchart, cycle,
  tree, timeline, matrix, comparison or chart. A chapter with no figure is
  unusual; aim for at least one figure per chapter.
- **Figures must be large and legible.** Draw on a 640-unit canvas with a
  `viewBox` only (never a fixed width/height), type ≥ 14 units, strokes ≥ 1.6,
  aspect ratio between ~0.2 and 1.15. Build them with `figlib` rather than
  hand-drawing. See `references/figures.md`.
- Keep SVGs print-safe: one colour scheme, no low-contrast text.

## Chapter anatomy

Each chapter carries a consistent shape:

- An opening `lead` line that states the chapter's single idea.
- Body sections with `h2` headings.
- At least one callout (a one-line rule or a named trap).
- At least one illustrative composite case.
- An **honest limit** section: what the idea does not explain, and when to hand the problem to a qualified professional.
- A closing "your one move this chapter" exercise, deliberately short.

## Honest limits, every time

Where a topic touches mental health, say plainly:

- The book is general information, not diagnosis or treatment.
- For trauma, severe phobias, panic that floods, persistent low mood, compulsion, or genuine danger, self-directed exercises are not the tool; a qualified clinician is.
- Asking for support is not a failure of the method.

## Language

This section is the **canonical banned-word list**; the QA gate points here
rather than repeating it.

- **Do not claim a book is undetectable by AI detectors** or anything of the sort. Report heuristics only, if at all.
- **Avoid a set of overused words**: delve, tapestry, underscore, testament, realm, navigate, robust, leverage, comprehensive, ever-evolving, stands as a testament, shed light, foster, seamless, crucial, pivotal, multifaceted, moreover, furthermore, it is important to note.
- **Em dashes: at most about six per thousand words.** Prefer commas, colons, and full stops.
- **Vary sentence length.** Each section should contain at least one short sentence (under six words) and at least one long one (over twenty-five words). Flat, even rhythm reads as machine-written.
- **No filler.** If a sentence can be deleted without losing meaning, delete it.
- **Concrete over abstract.** Name the thing.
- **Reducing AI tells is a heuristic, never a guarantee.** Never claim a book is
  undetectable by AI detectors. What is worth doing: measure em-dash density,
  sentence-length burstiness and stock-phrase hits; convert a majority of
  em-dashes into varied alternatives (comma clause, colon, semicolon,
  parenthesis — chosen by rule, not the same swap each time); rotate a few
  formulaic recurring phrases through synonyms. Re-measure and report honest
  before/after numbers.

## Editions and languages

- **Write each language natively.** Do not machine-translate the manuscript and call it an edition; mirror the structure and write the prose in the target language.
- **One stylesheet, byte-identical across languages.** Confirm with an md5 of the `<style>` block.
- **Watermark "the author's name" on every interior page**, every edition, every
  format — a **small boxed name in the footer**, not a large background mark.
- **No ISBN printed anywhere.**
- **Indic-language editions are eBook-only** unless the user says otherwise; do not promise a paperback.
- **The author bio uses only facts the author supplied.** Keep one canonical bio and reuse it across every edition and language.

## Before delivery

- Re-read your own output for the banned words and for any unattributed claim.
- Confirm the honest-limits sections are present.
- Confirm the composite labels are present.
- Confirm the footer watermark box appears on every interior page (cover and
  back cover excepted).
- State the known limitations to the user (DOCX reflow, grayscale PDF text, font substitution on machines without the script fonts).

## When the manuscript is supplied by the user

- The user's words are final: do not rewrite, "improve" or re-draft supplied
  prose.
- Write only the matter the book structurally needs — copyright, an epigraph
  drawn from the book's own text, a glossary of terms actually used, an index,
  About the Author, back-cover copy — and only from the book or the author's own
  notes.
- Never invent a bio fact, a blurb claim, a dedication or a review. Keep the
  canonical bio and its ordering rule (`assets/author-bio-template.md`).
