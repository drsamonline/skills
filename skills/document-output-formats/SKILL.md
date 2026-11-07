---
name: document-output-formats
description: "Produce the finished artefact from written content: a print-ready PDF via Typst, a Marp slide deck, or a styled HTML page from Markdown. Use when a report, paper, resume, handout, deck or web page must come out of Markdown or structured text with real typography and page layout. Not for editing an existing Word file or a spreadsheet."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Document output formats (PDF, slides, HTML)"
  category: "office-docs"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "typst-pdf-maker, marp-slide, markdown-to-html"
---

# Document output formats (PDF, slides, HTML)

Three output channels, one input shape. Choose by what the reader does with it: **print or archive** → Typst PDF; **present** → Marp deck; **read in a browser** → HTML. Then keep the source as Markdown so the same content can be re-emitted into another channel without retyping.

## When to use

- A Markdown or structured document must become a polished PDF with control over typography and page breaks.
- A slide deck is wanted from Markdown with a chosen theme.
- Markdown must become a styled, standalone HTML page, or a static-site pipeline needs the conversion rules.

## Method

1. Pick the channel from the reader's job — archive/print, present, or browse — before touching a template.
2. For PDFs: build a compact content manifest first (sections, figures, tables, acceptance criteria), choose one base template or skill-owned theme, and compile a minimum preflight with the exact imports before styling anything.
3. Apply rhythm in a fixed order: user or publication hard constraints, then the template's global layout, then package component rules, then the house theme, then generic starting values.
4. Route ambiguity back to the user as one question rather than guessing a layout; record the answer in the manifest and re-plan.
5. For decks: choose the theme deliberately (default, minimal, colourful, dark, gradient, tech, business), keep one idea per slide, and read the syntax reference before writing slides. A 'make it look good' request means apply the quality checklist, not a random restyle.
6. For HTML: pick the converter that matches the environment (`marked` for a quick JS path, `pandoc` for a document pipeline), and never enable the unsafe-HTML escape hatch in production output.
7. Verify each output the way its consumer will: page count and no widows/orphans for PDF, aspect ratio and overflow for slides, and rendering plus links for HTML.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`typst-pdf-maker`](references/typst-pdf-maker/) | Typst PDF production: content manifest, base selection, preflight, rhythm order, verification. |
| [`marp-slide`](references/marp-slide/) | Marp decks: seven themes, syntax, image layouts, quality checklist. |
| [`markdown-to-html`](references/markdown-to-html/) | Markdown → HTML conversion rules with `marked` and `pandoc` references, security notes, flavours. |

## Key files / entry points

- `references/typst-pdf-maker/` — the Typst routing workflow, content manifest, base selection, preflight and verification checklist.
- `references/marp-slide/` — Marp syntax, seven themes, image layouts and the quality checklist.
- `references/markdown-to-html/` — conversion rules per Markdown construct plus `marked` and `pandoc` references.

## Gotchas

- Styling before the base is chosen means restyling everything after.
- A deck is not a document — one idea per slide, and never a wall of body text.
- `safe: false` in a Markdown renderer turns user content into injected HTML.
- Tables and code blocks are where PDF page breaks go wrong; set break control on them explicitly.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `typst-pdf-maker` — no licence file shipped with the source
- `marp-slide` — no licence file shipped with the source
- `markdown-to-html` — no licence file shipped with the source
