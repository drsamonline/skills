# OMM JSON Schema v1.1 — app-ready output format

Two document types, one shared envelope. Every file is a single JSON object.
Design goals: (a) trivial to load and search in a browser app, (b) every string
traces back to the printed source, (c) nothing invented.

## Shared envelope

```json
{
  "schema_version": "1.1",
  "type": "repertory" | "materia_medica",
  "book": {
    "id": "hering-repertory-1889",
    "title": "Repertory to Hering's Condensed Materia Medica",
    "author": "Homoeopathic Medical Society of the State of Pennsylvania",
    "year": 1889,
    "publisher": "Globe Printing House, Philadelphia",
    "language": "en",
    "public_domain": true,
    "source_file": "data/source_txt/hering.txt",
    "extraction_date": "2026-10-14",
    "pipeline_version": "omm_pipeline 1.1",
    "coverage_note": "…",                    // optional; omitted when not needed
    "public_domain_note": "…",               // optional
    "copyright_jurisdictions": ["IN", "GB"], // optional
    "counts": { "...": "filled by the validator" }
  },
  "...": "type-specific payload below"
}
```

Optional `book` fields — written only when supplied, so they cost nothing otherwise:
- `coverage_note` — any coverage caveat (e.g. the count was not checked against the
  book's own index) stated plainly instead of implying completeness.
- `public_domain_note` — rights note when the term is not uniform across countries.
- `copyright_jurisdictions` — the ISO codes the public-domain claim covers.
Pass them with `--coverage-note`, `--public-domain-note`, `--copyright-jurisdictions`
(comma-separated). `references/workflow.md` says when each applies.

## type = "repertory"

```json
{
  "sections": [
    {
      "id": "hering-repertory-1889-s1",
      "title": "Repertory Of Symptoms Of The Lower Extremities",
      "rubrics": [
        {
          "text": "Abscess of knee, gouty, with pain and loss of sleep",
          "remedies": [0, 1]
        },
        {
          "text": "Ache, in sacro-ischiatic foramen, worse on pressure",
          "remedies": [[1, 2, "-"]]
        }
      ]
    }
  ],
  "remedy_table": [
    { "abbrev": "Guaiacum", "name": "Guaiacum" },
    { "abbrev": "Natrum ars", "name": "Natrum arsenicosum" }
  ]
}
```

Field notes:
- `sections[]` mirrors the book's own chapters (taken from its CONTENTS page).
- `rubrics[].text` — the symptom string, **verbatim** from the source (light OCR cleanup only).
- `rubrics[].parent` — for repertories with sub-entries (Drake: `Sweat of the Feet,
  Constant` → `Morning`), the heading the entry refines; `null` for a top-level
  rubric. The app renders `parent ? parent + ', ' + text : text`.
- `rubrics[].note` — verbatim prose attached to the rubric (Jahr Part II: the
  clinical remarks). Where a source carries remedy lists inside prose, the note is
  authoritative; `remedies[]` holds only the tokens confidently matched to the
  curated alias table and may be an incomplete subset.
- `rubrics[].remedies` — a list of **codes into `remedy_table`**. A code is an
  integer for a default link (grade not printed, polarity `"+"`, no note); when the
  grade, polarity or a note is non-default it is a `[code, grade, polarity]` (or
  `[code, grade, polarity, note]`) list. Resolve with `remedy_table[code].abbrev`.
  This shared-table form is the DEFAULT (`--no-refs` restores inline
  `{"abbrev": …}` objects).
- `remedy_table[]` — one entry per distinct printed remedy token, in first-seen
  order: `{ "abbrev": <verbatim as printed>, "name": <canonical, if known> }`. A
  missing `name` means the token is not in `remedy_aliases.csv` yet — the token is
  still shown, but no full name is asserted. A name is a property of the **token**:
  sources that attach a name per link (some do, some don't) are normalised so a
  token resolved anywhere is resolved everywhere.
- grade and polarity follow the same rules as before: `grade` is an integer 1–3
  **only if the source prints one** (never defaulted to 1); `polarity` is `"+"` or
  `"-"`, defaulting to `"+"`.
- `rubrics[].id` is **omitted by default** — it is position-derivable. The loader
  assigns `f"{book.id}-r{i:05d}"`, where `i` is the 1-based index of the rubric
  counting across all sections in order. Section `id`s are kept (their numbers are
  not contiguous once empty sections are dropped). Materia medica remedy/symptom
  `id`s are likewise omitted, derived as `f"{book.id}-{i:04d}"` and
  `f"{remedy_id}-s{j:04d}"`. `--keep-ids` writes them all out.

## type = "materia_medica"

```json
{
  "remedies": [
    {
      "id": "boericke-mm-1901-0001",
      "name": "Aconitum napellus",
      "abbrev": "Acon",
      "common_name": null,
      "kingdom": null,
      "family": null,
      "clinical_indications": ["Fever", "Inflammation"],
      "sections": {
        "relationships": [ { "kind": "complementary", "remedies": ["Ars", "Bell"] } ],
        "dosages": [],
        "antidotes": []
      },
      "symptoms": [
        {
          "id": "boericke-mm-1901-0001-s0001",
          "chapter": "Mind",
          "text": "<verbatim from source>",
          "grade": null,
          "modalities": [ { "dir": "worse", "text": "night" } ]
        }
      ]
    }
  ]
}
```

Field notes:
- `clinical_indications` — the disease/condition list a remedy is indicated in,
  when the source prints one (Jahr prints a semicolon-separated list before the
  symptoms). Empty list when absent.
- `chapter` is one of the body-system vocabulary (Mind, Head, Stomach, …) when the
  source prints section headers; otherwise `"General"`.
- `modalities[].dir` ∈ `worse | better | ws` (`ws` = unspecified).
- `kingdom` / `family` / `common_name` stay `null` unless the source states them.
  Do not fill them from outside knowledge.

## Size guidance for the app
- One JSON per book, named `{author-last}-{title-slug}-{year}.json`.
- A large book (e.g. 12k rubrics) is ~3 MB. If that is too heavy for the front end,
  split per section at load time or serve `sections[]` as separate files keyed by
  `section.id`. The pipeline can emit either; ask before splitting.

## Version compatibility (v1.0 ↔ v1.1)

Two shapes are valid and the pipeline reads both:

- **v1.0** — the legacy form still on disk in the repo: remedies inline as
  `{"abbrev", "grade", "polarity", "name"}` objects, `remedy_index` instead of
  `remedy_table`, ids present, no lean omission.
- **v1.1** — what the pipeline now emits: lean (defaults omitted), remedies as codes
  into `remedy_table`, position-derivable ids omitted.

`validate` accepts either. `compress` upgrades a v1.0 file to the v1.1 encoding
losslessly, except that per-link remedy names are normalised to the token level (a
name asserted on any link resolves the token everywhere). Re-running an extract
writes v1.1 directly. This skill's `references/schema.md` is the canonical contract
for both; the repo's `SCHEMA.md` (v1.0) describes only the legacy shape.

## Invariants the validator enforces
1. `schema_version` is `1.0` or `1.1`, and `type` is present and correct.
2. `book.id`, `book.title`, `book.source_file`, `book.extraction_date` present.
3. Repertory: at least one rubric; every rubric has non-empty `text`; ids, when
   present, are unique (omitted by default — see the id note above); every remedy
   resolves to an `abbrev` (inline, or via `remedy_table`).
4. Materia medica: at least one remedy; every remedy has a `name`.
5. QC gate (not a hard error): ≥ 90 % of rubric texts must be findable verbatim
   in the source; below that the QC report flags a warning.

## Field defaults and the "lean" encoding

Every field has a documented default, and **a missing key means exactly that
default** (project decision 2026-10-15). The pipeline therefore omits defaults on
write — this is the *lean* encoding and it is ON by default:

| field | default when the key is absent |
|---|---|
| `rubrics[].parent`, `rubrics[].note` | `null` |
| `remedies[].grade` | `null` (grade not printed) |
| `remedies[].polarity` | `"+"` |
| `remedies[].note` | `null` |
| `remedy_table[].name` | absent (token not resolved) |
| materia medica `canonical_name` / `common_name` / `kingdom` / `family` | `null` |

Arrays (`clinical_indications`, `modalities`, `relationships`, `dosages`,
`antidotes`) and the `sections` object are always written, even when empty, so app
code can iterate without a null guard. Read the omitted scalars as
`rubric.parent ?? null`, `remedy.polarity ?? "+"`, `remedy.grade ?? null`. The
decoded data is identical to the full form — only redundant default keys are gone.
Pass `--full` to write every key explicitly (for debugging or a strict consumer).
In the default refs form a remedy's defaults are carried by the bare integer code
itself (see `rubrics[].remedies` above), so the `remedies[]` rows apply to the
`--no-refs` form.

## Output formats and sizes

Measured on the real collection (`drsamonline/homoeopathic-materia-medica-repertory-json`,
2026-11-04): 161 repertory files (352,568 rubrics, 1,513,393 remedy links) and 6
materia medica files (39,770 symptoms). Each row is the whole corpus at that stage.

**Repertory**

| format | size | vs indented |
|---|---|---|
| JSON, indented (`--indent`) | 226.7 MB | 100 % |
| JSON, compact | 146.2 MB | 64.5 % |
| JSON, compact + lean | 113.3 MB | 50.0 % |
| JSON, lean + refs | 55.3 MB | 24.4 % |
| JSON, lean + refs + no ids (**default**) | 42.4 MB | 18.7 % |
| gzip of the default (`--gzip`) | 8.1 MB | 3.6 % |
| brotli of the default (`--brotli`) | 6.6 MB | 2.9 % |

**Materia medica**

| format | size | vs indented |
|---|---|---|
| JSON, indented | 11.3 MB | 100 % |
| JSON, lean + refs + no ids (**default**) | 7.1 MB | 62.8 % |
| gzip of the default | 1.9 MB | 17.1 % |
| brotli of the default | 1.4 MB | 12.8 % |

Materia medica compresses far less than repertories: its symptom text is unique
prose and there is no repeated remedy table to collapse, so only ids and defaults
come off. Do not expect repertory-scale ratios there.

Note: this counts every repertory file, including the modern
`repertorium-publicum-2008` (74,480 rubrics). `catalog.json`'s `repertory_rubrics`
total (307,998) does **not** match the on-disk sum — recount from the files before
publishing a figure (see "Count from the files" in SKILL.md).

- **Compact + lean + remedy-refs + no-ids JSON is the DEFAULT.** Every extract
  command writes it. Pass `--indent` to pretty-print (eyeballing / hand-diffing),
  `--full` to keep every key, `--no-refs` to keep inline remedy objects, and
  `--keep-ids` to write the derivable ids. All forms parse to identical data —
  indentation is insignificant whitespace between tokens, never inside a string.
- **`--gzip` and `--brotli` write `.json.gz` / `.json.br` sidecars** beside the
  JSON. Brotli is the smallest (about 18 % under gzip here). Serve a `.br` file
  with `Content-Encoding: br` and the browser decodes it transparently; for a
  client-side fetch with no server config, use the gzip sidecar:
  `const s = (await fetch(url)).body.pipeThrough(new DecompressionStream('gzip'));
   const data = await new Response(s).json();`
- **`compress`** reports every size for an existing file and writes the smallest
  form (brotli if installed, else gzip):
  `python3 scripts/omm_pipeline.py compress --json <file> [--out <file>.br]`.
  Use it to decide which form to ship.
- **Keys stay readable.** Shortening key names was measured and gives no gain on the
  compressed artifact (gzip/brotli already collapse the repeated keys), so the JSON
  keeps full, self-describing names.
- **SQLite** (`python3 scripts/omm_pipeline.py to-sqlite --json <file> --db <db>`)
  is the queryable form. It is NOT smaller if you keep text keys and many indexes
  (a naive version came out larger than the JSON). Use integer primary keys, keep
  only the indexes you need, and `VACUUM`.
- SQLite's real advantage is not size but **query speed and partial loading** — a
  browser app can ask "which remedies for `Stomach > pain`" without parsing 38 MB.

### SQLite schema produced by `to-sqlite`
```
book(id, type, schema_version, title, author, year, publisher, source_file,
     extraction_date, counts)
section(id INTEGER PK, book_id, ordinal, title)              -- repertory
rubric(id INTEGER PK, book_id, section_id, text, parent, note)
remedy_link(rubric_id, abbrev, grade, polarity, note)
remedy_index(book_id, abbrev, name, resolved)
mm_remedy(id INTEGER PK, book_id, name, abbrev, canonical_name, common_name,
          kingdom, family)                                    -- materia medica
mm_symptom(id INTEGER PK, remedy_id, chapter, text, grade)
```
Indexes: `rubric(section_id)`, `remedy_link(rubric_id)`, `remedy_link(abbrev)`,
`mm_symptom(remedy_id)`.

## Changelog

**v1.1 (2026-10-15)** — size/compression pass; decoded data unchanged in meaning.
- Repertory remedies are now **codes into a shared `remedy_table`** instead of
  inline `{"abbrev": …}` objects (the old `remedy_index` is folded into the table).
  `--no-refs` restores the inline form.
- Fields equal to their documented default are **omitted** (the *lean* encoding);
  `--full` writes every key.
- Position-derivable ids (rubric ids, and materia medica remedy/symptom ids) are
  **omitted**; the loader re-assigns them. `--keep-ids` restores them.
- Optional `book.coverage_note`, `book.public_domain_note` and
  `book.copyright_jurisdictions` for honest coverage and rights statements.
- Output is compact by default; `--gzip` / `--brotli` write compressed sidecars,
  and `compress` reports every size and emits the smallest.
- Bumped from v1.0 because the repertory payload shape changed (not merely resized).

**v1.0** — first app-ready contract: shared envelope, repertory
`sections → rubrics → remedies`, materia medica `remedies → symptoms`.
