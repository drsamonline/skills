---
name: repo-provenance-manifest
description: Record and check per-file provenance with tools/manifest.py — the MANIFEST.json gate that decides, from three blob SHAs, whether a file is safe for a generator to overwrite. Use when a workflow writes into a repository, when a generated file has to be told apart from a hand-written one, or when a build must refuse to clobber source.
metadata:
  title: "Per-file provenance with MANIFEST.json"
---

# Per-file provenance with MANIFEST.json

A repository that both generates files and holds hand-written ones cannot tell them
apart from git alone. `tools/manifest.py` answers that with one file at the repo root,
`MANIFEST.json`, and a three-way blob comparison: the SHA recorded in the manifest, the
SHA committed at `HEAD`, and the SHA of the file in the working tree. It needs no history
and no author detection, so it is correct at `fetch-depth: 1` — which is what every
generator checkout in this estate uses.

## When to use

- A workflow or generator is about to write files into a repository and must not
  overwrite something a human wrote.
- A build has to fail closed on "this file is not mine", rather than on "this file changed".
- You need to prove which version of which tool produced a file.
- You are adopting the gate in a new repository, or debugging a `refuse`/`drift` verdict.

## Method

1. **Put `tools/manifest.py` at the repo root** — the same file every repo carries, not a
   variant. It is invoked as `python3 tools/manifest.py <command>`.
2. **Know the four classes.** Every entry carries `class`: `generated` (a tool writes it),
   `canonical` (pinned, e.g. a workflow caller), `hand` (a person wrote it), `agent` (an
   agent wrote it), `locked` (never rewritten). A repo-level `"locked": true` short-circuits
   every path to `locked` and refuses all recording.
3. **Record what you wrote**, in the same run that wrote it:
   `tools/manifest.py record <path>... --producer <tool>@<sha> --class generated`.
   `record` refuses a path whose previous class is `hand`, `agent`, `locked` or `canonical`
   unless `--force` is passed — that refusal is the point, not an obstacle.
4. **Check before writing.** `tools/manifest.py check <path>...` prints one JSON object per
   path with `manifest_sha`, `committed_sha`, `worktree_sha` and a `status`. Read the exit
   code, not the prose.
5. **Read the exit codes as the verdict.** `0` clean or `new` (file absent, safe to create);
   `3` `unrecorded`, `deleted`, `uncommitted` or `committed-drift` — refuse, this is a human
   decision; `4` `protected` or `locked` — refuse by class. Any other code is a hard error
   and the caller must fail closed: a checker that cannot run must not authorise a write.
6. **Claim a file as yours when a human made it:** `claim <path> --as hand`. **Lock the repo**
   while it is under repair: `lock --reason "<why>"`, then `unlock`. `status` prints the whole
   manifest; `version` prints the schema.
7. **Wrap it in code, do not shell out twice.** `tools/_gate.py` carries the same semantics as
   three helpers — `_manifest_check(paths)` (True only when every path is clean or `new`),
   `_manifest_record(...)` (silent on success, a warning on failure) and `_producer(tool)`
   (returns `tool@<blob sha of the writing file>`). Generators copy these seventy lines
   because they run where `manifest.py` may not exist yet; forge's own tools import
   `_gate.py` instead.
8. **Prove the commit landed.** `tools/commit-and-verify.sh "<message>" [branch] -- <path>...`
   records each blob SHA, commits and pushes with backoff, then fetches the branch and
   compares. Success is blob-SHA equality; a `git` exit code is not evidence.

## Key files

- `tools/manifest.py` — the gate itself; schema 1, `RC_CLEAN=0`, `RC_DRIFT=3`, `RC_PROTECTED=4`.
- `MANIFEST.json` at the repo root — `{"schema": 1, "locked": false, "files": {"<path>": {"sha", "producer", "class", "at"}}}`.
- `tools/_gate.py` — `_manifest_check`, `_manifest_record`, `_producer`, for Python tools that
  run beside `manifest.py` (present in `forge`, `registry`, `control-panel`).
- `tools/commit-and-verify.sh` — the "did the data land?" verdict, F-97; exit `0` only when
  every named file is on the branch with the intended bytes.
- `LOCKED.md` — the default `lock --reason`, read by a human who finds the repo refusing.

## Gotchas

- **The file is copied, and the copy is the point.** Measured 2026-11-23: `tools/manifest.py`
  is present in 68 of the 153 repositories scanned and all 68 are byte-identical — one file,
  not a family of forks. If you are editing it in one repo, you are forking the gate.
- **`new` is not `clean`.** Both exit `0`, but `new` means the file does not exist yet and the
  generator is allowed to create it; a check that treats them the same will authorise a
  creation it never intended.
- **`unrecorded` is the window the manifest exists to close.** A file present on disk or in
  `HEAD` with no manifest entry is refused, not adopted.
- **`sha_worktree` uses `git hash-object --path=` on purpose.** Without `-C <root>` a caller
  invoked from a subdirectory resolves the wrong tree; without `--path` clean/smudge filters
  do not fire and the SHA disagrees with what `git add` would store.
- **`record` will not downgrade `canonical`.** A generator that records the pinned
  `build-apps.yml` caller without `--class canonical` is refused, because `record` would
  otherwise let any tool reclassify a pinned file as generated.
- **A hard error must fail closed.** The documented contract is that any exit code other than
  `0`, `3` or `4` is a hard error; callers that map "anything not 0" to "skip the write" are
  safe, callers that map it to "proceed" are not.

## Source projects

- [forge](https://github.com/drsamonline/forge) — owns the gate, `_gate.py` and `commit-and-verify.sh`.
- [registry](https://github.com/drsamonline/registry) — a generator that runs the gate beside `manifest.py`.
- [control-panel](https://github.com/drsamonline/control-panel) — the third `_gate.py` consumer.
- [All4ONE](https://github.com/drsamonline/All4ONE), [HCS](https://github.com/drsamonline/HCS), [HMS](https://github.com/drsamonline/HMS) — repositories carrying the identical `tools/manifest.py`.
- [app-thermals](https://github.com/drsamonline/app-thermals) — an app repo with the gate and its own `tools/` checks side by side.
