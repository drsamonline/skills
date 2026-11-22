---
name: curated-list-directory
description: Run a curated directory of single-file, local-first web apps: a submission path that does not rot, one criterion applied literally (one HTML file, dependencies embedded), and enough structure that a reader can tell a maintained list from an abandoned one.
metadata:
  title: "Single-file web app directories"
---

# Single-file web app directories — curating a list people submit to

Four lists of the same idea: single-file web apps and local-first tools. Between them they are the
evidence that this family's constraint — one HTML file, dependencies embedded, no network — is a
movement rather than a personal preference.

## When to use

- You are publishing a curated list and want it to be *checkable*: one criterion, applied literally.
- The list accepts submissions and needs a path that does not become an inbox of broken links.
- You need to distinguish your list from the other three that look identical.

## Method

1. State the criterion in one sentence and apply it mechanically: *one `.html` file with every dependency embedded*. A list whose criterion is fuzzy is a bookmarks folder.
2. Make the criterion testable — if a submission needs a folder, a build step or a CDN, it fails, and the failure reason is written on the submission.
3. Keep the entries uniform: name, one-line what, link, and the criterion evidence. No entry is a paragraph.
4. Provide a submission path that is a pull request against a data file, not an email.
5. Distinguish the lists: a *directory* (browsable, searchable), a *list* (a README), and a *community* (submissions) are three different products — pick one and say which.

## Key files / entry points

- The data file or README that holds the entries.
- The submission instructions.
- The landing page, where there is one.

## Gotchas

- Four lists of the same thing is four times the maintenance: link to the others rather than duplicating their entries.
- A link checker is the difference between a live list and an archive; run it in CI.
- "Local-first" and "single-file" are different claims — a local-first tool can ship as ten files, and a single-file app can phone home.

## Source projects

- [awesome-singlefile-tools](https://github.com/drsamonline/awesome-singlefile-tools)
- [iamsingle-sfwa-directory](https://github.com/drsamonline/iamsingle-sfwa-directory)
- [Single-File-Web-Apps](https://github.com/drsamonline/Single-File-Web-Apps)
- [local-first-tools](https://github.com/drsamonline/local-first-tools)
