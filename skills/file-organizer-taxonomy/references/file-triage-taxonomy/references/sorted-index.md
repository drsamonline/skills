# Sorted files index

A running record of every file the agent has moved: where it came from,
where it went, and why. Two files, same content, both at the root of My
Drive.

This is not the location map. The map says where a file **is** right now;
this index says what the agent **did**. The map is rebuilt each run. The
index is appended and never rebuilt, so the history survives every run.

## The files

- **Name:** `Sorted Files Index.html`
  - One self-contained page. Inline CSS only, no external fonts, scripts,
    stylesheets or images. It must open with no network.
  - Every destination is a real hyperlink to that file's Drive
    `webViewLink`, opening in a new tab.
  - Newest run at the top.
- **Name:** `Sorted Files Index.txt`
  - The same rows as plain text, one line per file, pipe-delimited:
    `date | run | from | to | bucket | confidence | reason | link`
  - Newest run at the top, same order as the HTML. No markup, no columns
    to align, no wrapping — one record per line so it stays readable in
    any viewer and greppable.

Both are written in the same pass from the same move list, so they can
never disagree. If one cannot be written, say which in the chat reply.

Never create a second copy of either. Find the existing file by name in
the root first and append to its content. Only create it if it does not
exist. If two copies of a format already exist, append to the newest and
flag the duplicate — do not delete the other.

Tools, once per format: `GOOGLEDRIVE_FIND_FILE` (`name = 'Sorted Files
Index.html'` — or `'Sorted Files Index.txt'` — `and 'root' in parents and
trashed = false`, fields `id,webViewLink`), create with
`GOOGLEDRIVE_UPLOAD_FILE` into the root, append with
`GOOGLEDRIVE_EDIT_FILE` on the stable `file_id`. Both are plain
binary-content files, not Google Docs native files.

## When it is written

- **EXECUTE run:** always, after the moves have succeeded, before the run
  is reported complete. A move that is not in the index did not happen as
  far as the owner can tell.
- **DRY RUN:** never. Nothing moved, so there is nothing to record. Do not
  create the files on a dry run.

If a run moves nothing, still write both files with a run block saying
zero files moved, so the owner can see the run happened.

## What goes in it

1. **Header** — title, `Last updated` timestamp in IST, scope (My Drive
   root).
2. **Summary** — runs recorded, files moved in total, files moved in the
   latest run, files skipped, duplicates found.
3. **Run blocks, newest first.** Each block headed `Run N — <date> IST —
   <count> files moved`, then its rows.
4. **Skipped files** — files seen and deliberately left alone, with the
   reason (in use, linked from a Google Sheet or Site, shared link, low
   confidence). They were not sorted, so they belong here and not in the
   move rows.
5. **Duplicates** — exact duplicates sent to `_REVIEW_DELETE/`, listed
   with the copy they match.

Each move row carries: date moved, run number, original path, new path,
bucket, confidence, one-line reason, and the Drive link.

## Rules

- **Append only.** Never rewrite, reorder or drop an existing row. Adding
  a run means adding a block above the previous ones.
- **Never edit history to look tidy.** If a later run moves a file again,
  that is a new row. Both rows stay.
- **A row outlives the file.** If the destination no longer exists, keep
  the row. The index records what happened, not what survives.
- **No invented rows.** Only files the agent actually moved appear. A
  proposed move that the owner did not execute is not in the index.
- **Batches.** If one run moves more than 5,000 files, append in explicit
  batches of 5,000 and state the batch boundaries and the remaining
  count. Do not sample and do not truncate silently.

## Shape

HTML: a summary line, then one `<details>` block per run, newest open by
default and older ones closed, each holding a plain `<table>` with the
seven columns. Keep it readable — a single table of 20,000 rows is not an
index.

TXT: header lines, blank line, then per run a `Run N — date — count`
heading and its pipe-delimited rows. No alignment padding, no tabs.
