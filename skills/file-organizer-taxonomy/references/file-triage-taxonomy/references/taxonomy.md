# Folder map

This file holds the instance-specific bucket list for the file organizer.
The build interview fills it from the user's actual folders; every later
run reads it. Do not invent buckets.

## Setup status

- **Status:** configured

The agent runs only when this line reads `configured`. If it reads
`unconfigured`, the clone has no real folder list — stop. Do not fall
back to a made-up tree.

## Default folder

- **Path:** `My Drive` (Drive root — entire Drive)

## Buckets

One line per allowed bucket. The agent may not create categories
outside this list. Always keep the three review paths. `OTHER/` appears
here because the folder exists; it is a source only, never a
destination.

```
SELL/                    sales / selling material
DrAppSync/               app sync and app data
Saved from Chrome/       pages and files saved from the browser
Google AI Studio/        AI Studio projects and exports
My Articles/             his own written articles
dr sohil/                personal-professional material under his name
FinArt/                  finance and investment work
Reddit/                  Reddit saves and exports
LIG/                     his house and its housing-society documents
AIAPGET EXAM DATA 4.7 (File responses)/   AIAPGET 4.7 file responses
C4H/                     C4H trust documents — a trust of his
PERSONAL DOCUMENTS/      personal paperwork — certificates, tax, IDs, legal
CERTIFICATES/            certificates and course records
OTHER/                   owner's manual drawer — source only, see owner rules
Bills/                   bills and receipts
CoinbaseWalletBackups/   crypto wallet backups
GUJARATI ISLAM/          Gujarati Islami material
Books/                   books, monographs, materia medica
Music/                   audio
GUJARATI BIBLE/          Gujarati Bible material
_UNSORTED/               classified but no fitting bucket
_REVIEW/                 low confidence, needs a human
_REVIEW_DELETE/          exact duplicates — owner confirms by hand
```

The owner's current folder structure is kept exactly as arranged. Bucket
names above are his folder names verbatim — do not rename, regroup or
reorder them.

## Owner rules

- **Organise, do not restructure.** The existing top-level folders stay.
  Do not collapse them into a new top-level scheme.
- **`OTHER/` is the owner's own drawer, and a valid source.** He created
  it by hand for files he could not sort. Classify its contents like
  files anywhere else and move them out to the correct bucket when
  confidence is high. Anything below high confidence stays in `OTHER/`
  and is listed under `_REVIEW`. Never route a new file into `OTHER/`,
  never merge it, never rename it, never delete it — it stays his drawer
  even when empty. Files the agent cannot classify go to `_UNSORTED/`,
  never to `OTHER/`.
- **Duplicates and overlapping folders.** Exact duplicates — identical
  content hash — are listed with `duplicate_of` and moved to
  `_REVIEW_DELETE/` on an EXECUTE run; the agent never deletes anything
  itself. Near duplicates are reported with a similarity note and left
  where they are. Folders holding the same kind of material are named in
  the report as a consolidation proposal for the owner; no folder is
  ever merged, renamed or removed by the agent.
- **Route before inventing.** First try to place a loose file into a
  folder that already exists. Only if nothing fits, propose a new folder
  or subfolder in the plan — do not create one without the owner saying
  EXECUTE.
- **Linked and in-use files are untouchable.** Never move, rename or copy
  a file that is referenced from a Google Sheet, embedded in or linked
  from a Google Site, linked from a Google Doc, open in an editor, or
  reachable through a shared link. This holds whatever its bucket and
  however high the confidence — a broken link in his sheet or site costs
  more than an untidy folder. List it as skipped with the reason, and say
  where the link comes from when that is known.
- **Be safe than sorry.** When in doubt, flag for review rather than act.

Every bucket is now defined. `C4H/` is the trust's own paperwork —
deeds, registrations, filings, trust correspondence. `LIG/` is the house
and its housing society — ownership papers, society records, maintenance
and notices. A file that could sit in either belongs where its subject
sits, not where it arrived from.

No folder list is assumed. The bucket list above is the only authority;
if it is empty or reads `unconfigured`, stop.

## Naming

- **Pattern:** keep original names — the owner does not want file names
  changed. No renaming, no re-formatting, no version suffixes. Move only.
- **Entity field:** unused
- **Doctype field:** unused
- **Version field:** unused

If a field cannot be read from the file, keep the original filename. Do
not guess a date.

## Do not touch

- Any file currently in use, or linked from a Google Doc or Sheet, or
  embedded in / referenced by a website, or reachable through a shared
  link. Do not move, rename, copy or touch these. List them as skipped
  with the reason.
- Nothing else was named. When unsure whether a file is in use, treat it
  as in use and flag it for review.

## Read depth default

- in-depth — open and read each file before classifying it. Filenames are
  not to be trusted.

## Cadence

- ongoing — this agent keeps organizing. Do not ask one-time vs ongoing.
