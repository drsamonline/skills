---
name: knowledge-capture-and-recall
description: "Synthesise many sources into one attributed answer, and recall what was decided before. Use when combining search results across sources, deduplicating overlapping findings, scoring confidence from freshness and authority, or when a question needs historical context — 'what did we decide about X', 'why did we do Y', 'have I seen this before'."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Knowledge capture and recall"
  category: "notes-knowledge"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "knowledge-synthesis, memory-recall"
---

# Knowledge capture and recall

Capture and recall are the same discipline from opposite ends: every claim carries its source, conflicts are surfaced rather than resolved silently, and what you cannot attribute you do not assert. Synthesis works forward from a result set; recall works backward from a question into past sessions.

## When to use

- Multiple search results, documents or sources must become one coherent answer.
- The same fact appears in several places and needs deduplication with attribution kept.
- A question depends on a past decision, debugging note or previous conversation.

## Method

1. Synthesis: group the result set by claim, not by source. Collapse duplicates, keeping the most authoritative and most recent instance and noting the others.
2. Keep what should not be deduplicated: distinct figures, different dates, different scopes and contradictory claims all stay separate.
3. Attribute every claim to its source and name the source type (web, chat, email, cloud storage, database).
4. Score confidence from two axes: freshness and authority. Express it plainly ('one recent primary source', 'two secondary sources that disagree') rather than as a fake percentage.
5. Surface conflicts explicitly: say which sources disagree and what would settle it. Never pick one silently.
6. Scale the summary to the result set: quote and cite for 1–5 results, group and cite for 5–15, cluster by theme with representative citations for 15+.
7. Write narrative, not a list of results, and offer more detail when the set was large.
8. Recall: search past sessions with the memory tool when the question is about a past decision, a prior debugging session, or project history.
9. When unsure what to search, search broad terms first, then narrow; when a transcript format is unrecognised, read the referenced file directly instead of giving up.
10. Report what you found with its source and date, and say plainly when nothing was found.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`knowledge-synthesis`](references/knowledge-synthesis/) | Cross-source synthesis: deduplication priority, attribution, confidence, conflict handling, summarisation by set size. |
| [`memory-recall`](references/memory-recall/) | Searching and citing past sessions, with the query strategy and output format. |

## Key files / entry points

- `references/knowledge-synthesis/` — deduplication priority, attribution format, confidence levels, summarisation strategies, anti-patterns.
- `references/memory-recall/` — the recall steps, collection selection, query construction and output format.

## Gotchas

- A list of raw results is not a synthesis.
- Silently choosing one side of a conflict is the failure this skill exists to prevent.
- Deduplicating two different figures into one number invents a fact.
- A confidence number with no basis is worse than a plain sentence about the evidence.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `knowledge-synthesis` — no licence file shipped with the source
- `memory-recall` — no licence file shipped with the source
