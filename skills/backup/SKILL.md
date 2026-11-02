---
name: backup
description: Snapshot a repository before a merge replaces it: a reusable GitHub workflow plus a zero-dependency script that compresses, timestamps and rotates dumps to keep the newest hundred, with a restore test.
metadata:
  title: "Pre-merge repository snapshot"
---

# Pre-merge repository snapshot

Before a merge overwrites a repository's code, take the state that is about to be replaced and store it compressed, timestamped, in a separate dumps repository. The script is one file, the workflow is reusable, and the rotation keeps the newest hundred so the dumps repo cannot grow without bound.

## When to use

- You are about to replace a repository's contents with a merge and want the old state recoverable.
- You need a backup job that runs from CI with no dependencies and no interactive auth.
- You want rotation with a rule you can state in one sentence.

## Method

1. Run `backup.py` with the target repository and the dumps destination; it archives the tree, stamps it with a timestamp and writes the dump.
2. Wire it in with `.github/workflows/backup.yml` *before* the step that merges, so the snapshot is of the state that is about to go.
3. Let the manifest be derived from the directory listing rather than hand-written — a manifest you edit by hand lies eventually.
4. Rotate to the newest hundred dumps; the rule is a count, not an age, so it is predictable.
5. Keep `tests/test_backup.py` proving a dump can actually be restored — a backup that has never been restored is an untested file copy.
6. Read `TOKEN.md` before making the dumps repository public: the dumps contain the whole history of the code.

## Key files / entry points

- `backup.py` — the whole tool; `tests/test_backup.py` — the restore proof.
- `.github/workflows/backup.yml` — the reusable workflow.
- `TOKEN.md` — the credential and visibility rules.

## Gotchas

- A backup taken *after* the merge backs up the thing you wanted to be able to undo.
- Hand-maintained manifests drift from the directory; derive the manifest from what is on disk.
- Rotating by age deletes unpredictably; rotating by count is a rule you can explain.
- A dumps repository is a full copy of the code — treat its visibility as a separate decision.

## Source projects

- [backup](https://github.com/drsamonline/backup) — the script, the reusable workflow, the rotation and the restore test.
