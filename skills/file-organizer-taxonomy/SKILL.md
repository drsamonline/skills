---
name: file-organizer-taxonomy
description: "Classification, naming and recording rules for sorting a drive: bucket assignment from the owner's real folders, linked-file protection, duplicate handling, and the two artefacts — a location map and a sorted files index. Use on every run before any file is moved, and whenever a file-sorting or Drive-cleanup agent needs its rules."
license: "per source — see references/*/LICENSE"
metadata:
  title: "File organizer taxonomy"
  category: "sysadmin-ops"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "file-triage-taxonomy"
---

# File organizer taxonomy

The rules exist to stop an agent inventing structure. Categories come from the owner's actual folder list, not from a plausible taxonomy; anything that does not fit is left unsorted with a reason; and nothing is deleted by the agent. Every move is recorded twice — where it went, and what moved.

## When to use

- A drive or folder tree is being sorted for the first time or on a recurring run.
- A file-sorting agent needs its bucket map and naming convention.
- Duplicates or near-duplicates must be identified without being destroyed.

## Method

1. Read the configuration first. If the folder list is not configured, stop — do not invent categories.
2. Assign each file to a bucket that exists in the configuration. If nothing fits, assign `_UNSORTED` and say why.
3. Apply the naming convention exactly as configured, including any date pattern it names. A pattern printed in documentation is not permission to use it.
4. Protect linked files: anything referenced from a document, a sheet or a shortcut is never moved.
5. Detect duplicates by content, then group near-duplicates with a similarity note. Never move, merge or delete them — list them for the owner to decide. Never assume the newest file is the correct one.
6. Route obvious junk to the review-and-delete folder for the owner to confirm; the agent never deletes.
7. Never route anything new into the catch-all folder, and never rename that folder itself.
8. Write both artefacts: the location map (what went where) and the sorted files index (what moved, from, to, when, why).
9. Report the counts and every `_UNSORTED` assignment with its reason.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`file-triage-taxonomy`](references/file-triage-taxonomy/) | The bucket, naming, duplicate and recording rules, plus the two Drive artefacts and the failure contract. |

## Key files / entry points

- `references/file-triage-taxonomy/` — classification rules, naming convention, duplicate procedure, output contract, failure handling.

## Gotchas

- Inventing a category is worse than leaving a file unsorted.
- A guessed date in a filename is a silent data error.
- Moving a linked file breaks the document that references it.
- Deleting a duplicate destroys the only copy the owner remembers.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `file-triage-taxonomy` — no licence file shipped with the source
