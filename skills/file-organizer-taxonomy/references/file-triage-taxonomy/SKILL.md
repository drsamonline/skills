---
name: file-triage-taxonomy
description: >
  Classification, naming and recording rules for the File Organizer agent.
  Bucket assignment from the owner's real folders, linked-file protection,
  duplicate handling, and the two Drive artifacts — the location map and
  the sorted files index. Use on every run before any file is moved.
---

# file-triage-taxonomy

Gives the organizer agent a fixed classification scheme and a naming
convention so that runs are repeatable and two runs a month apart produce
the same structure.

## When to use

On every run of the file organization agent, before any file is moved.

## One-time setup — read the config

Instance specifics live in `references/taxonomy.md`: the default folder,
the allowed buckets, naming fields, do-not-touch paths, and read-depth
default. Read its **Setup status** line first. If it does not read
`configured`, stop — the clone has no real folder list. Do not invent a
folder tree.

## Classification

Assign each file to exactly one bucket from the config. If no category
fits, assign `_UNSORTED` and say why. Do not invent categories.

`OTHER/` is a source, not a destination. Files already sitting in it are
classified like any other file and moved out to their correct bucket at
high confidence; below that they stay put and are listed under `_REVIEW`.
Nothing new is ever routed into `OTHER/`, and the folder itself is never
merged, renamed or deleted.

Assign confidence: high, medium, or low. Anything below high goes to
`_REVIEW` rather than being moved silently.

Linked files are never sorted. A file that is referenced from a Google
Sheet, embedded in or linked from a Google Site, linked from a Google
Doc, or reachable through a shared link is not moved, renamed or copied,
whatever its bucket or confidence. List it as skipped with the reason. A
broken link in the owner's sheet or site costs more than a tidy folder.

## Naming convention

The config decides. `references/taxonomy.md` currently sets naming to
**keep original names** — move only. No renaming, no re-formatting, no
version suffixes, no date stamping.

Rename only if the config itself names a pattern. The optional pattern
is:

```
YYYY-MM-DD_<entity>_<doctype>_<version>.<ext>
```

with entity / doctype / version meanings as recorded in the config. If
any field cannot be determined, keep the original filename and flag the
file. Do not guess a date. A pattern printed in this file is not
permission to use it — the config must name it.

## Duplicate detection procedure

1. Compute a content hash for every file.
2. Group by identical hash. These are exact duplicates. List each with
   `duplicate_of` set to the copy it matches. On an EXECUTE run, move
   them to `_REVIEW_DELETE/` for the owner to confirm. The agent never
   deletes a file itself.
3. For documents with different hashes but very similar content, report
   them as near duplicates with a similarity note. Do not move or merge
   them. Let the human decide which is current.
4. Never assume the newest file is the correct one. The user decides
   which copy to keep.
5. Overlapping folders — two folders holding the same kind of material —
   are named in the report as a consolidation proposal. No folder is
   merged, renamed or removed by the agent.

## Sorted files index

Every file the agent moves is recorded in the sorted files index — an
append-only ledger of what moved, from where, to where, and why — written
as `Sorted Files Index.html` and `Sorted Files Index.txt` at the root of
My Drive on every EXECUTE run, and never on a dry run. Follow
`references/sorted-index.md`.

Two artifacts, two jobs. The location map (`references/location-map.md`)
says where a file is now and is rebuilt each run. The index says what the
agent did and is appended, never rebuilt. Files skipped because they are
in use or linked appear in both — as in-use in the map, as skipped in the
index.

## Output contract

Return a table with these columns and no others:

```
current_path | proposed_path | category | confidence | reason | duplicate_of | action
```

## Failure handling

If the target folder is larger than you can process in one pass, do not
sample. Process it in explicit batches, report the batch boundaries, and
tell the user how many files remain.
