# File location map

The owner's map of where everything lives. Two files with the same
content, kept up to date, so he can find any file by browsing one page
instead of searching Drive.

This is not the sorted files index. The map answers "where is it now"
and is rebuilt every run; `references/sorted-index.md` answers "what did
the agent move" and is appended, never rebuilt. Two artifacts, two jobs —
do not merge them or write one in place of the other.

## The files

Two files, same content, both at the root of My Drive:

- **Name:** `File Location Map.html`
  - A single self-contained HTML page. Inline CSS only, no external
    fonts, scripts, stylesheets or images. It must open correctly with no
    network.
  - Every file entry is a real hyperlink to that file's Drive
    `webViewLink`, opening in a new tab.
  - Note for the owner, once: Drive does not preview HTML inline, so this
    one opens in a browser rather than in the Drive viewer.
- **Name:** `File Location Map.md`
  - The same tree in Markdown. Nested bullet lists, one bullet per folder
    and per file, each file a Markdown link to its `webViewLink`.
  - No HTML in this file. Plain headings and lists only.

Both are written on the same run from the same walk of Drive, so they can
never disagree. If one cannot be written, say which.

Never create a second copy of either. Find the existing file by its own
name in the root first and update its content. Only create it if it does
not exist. If two copies of the same format already exist, update the
newest and flag the duplicate in the chat summary — do not delete the
other.

Tools, run once per format: find with `GOOGLEDRIVE_FIND_FILE` (`name =
'File Location Map.html'` — or `'File Location Map.md'` — `and 'root' in
parents and trashed = false`, fields including `id,webViewLink`), create
with `GOOGLEDRIVE_UPLOAD_FILE` into the root, and refresh with
`GOOGLEDRIVE_EDIT_FILE` using the stable `file_id`. Both are plain
binary-content files, so `GOOGLEDRIVE_EDIT_FILE` works on them; Google
Docs native files are not involved.

## When it is written

- **EXECUTE run:** always, both formats, before the run is reported
  complete. They must reflect the Drive as it is after the moves.
- **DRY RUN:** write them only if no map exists yet, as a baseline of the
  current state. Never overwrite an existing map from a dry run — nothing
  has moved, so the files would only lose the previous run's record.

If either file cannot be written, say which one and why in the chat
reply. A run is not complete while a map is stale and the owner has not
been told.

## What goes in it

1. **Header** — title, `Last updated` timestamp in IST, the scope (My
   Drive root), and the run mode and run number it was written from.
2. **Summary** — files seen, moved, skipped, flagged, duplicates found.
3. **The tree** — every top-level folder in the bucket list, in the order
   the owner has them, each one collapsible. Under each: its subfolders,
   then its files.
4. **Loose files at the root** — anything not yet inside a folder.
5. **Review sections** — `_UNSORTED`, `_REVIEW`, `_REVIEW_DELETE` when
   they exist, listed separately so he can see what needs his decision.
6. **In-use files** — a short list of files skipped because they are in
   use or linked, with the reason. He needs to know they were seen and
   deliberately left alone.

Each file entry shows: the file name as a link, the file type, and the
last-modified date. Each folder entry shows how many files it holds.

## Shape

Use collapsible `<details>` blocks per top-level folder, open by default
only for folders with fewer than 20 files. Keep the markup plain and
readable — a long flat table of thousands of rows is not a map.

In the Markdown version, collapsible blocks become heading levels: `##`
per top-level folder, `###` per subfolder, files as bullets underneath,
each one a Markdown link. Same order, same entries, same counts.

If a folder holds more than 200 files, list the first 200 by name and add
one line: `+ N more files in this folder`. Do not silently truncate.

## Depth

Walk the whole scope breadth-first: list a folder, then recurse into its
subfolders, collecting name, mime type, modified time and `webViewLink`
for every file. Do not stop at the first level. Do not open or download
file contents just to build the map — metadata and links are enough.
