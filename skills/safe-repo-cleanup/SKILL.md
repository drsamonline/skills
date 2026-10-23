---
name: safe-repo-cleanup
description: An audit-first procedure for removing build junk, caches, temp files, stale archives and duplicated README content from a repository without deleting anything that is referenced, committed source or a landing-page asset.
metadata:
  title: "Safe repository cleanup"
---

# Safe repository cleanup

A repository that has been built and rebuilt for years collects two kinds of mess: **files that were never meant to be committed** (`__pycache__/`, editor droppings, stray logs and archives) and **README drift** (a badge pasted in twice, two stacked badge blocks, an intro paragraph that appears at the top and again below it). Both are safe to fix — but only if the fix is audited before it is applied. Deleting by pattern (`rm -rf dist build`) is how a repository loses a directory that was, in that project, committed *source* rather than output. The method below is deliberately conservative: classify every path first, reference-check every candidate, delete only the high-confidence set, and hand anything uncertain to a human.

## When to use

- A repository has accumulated build junk, caches, temp files, stale archives or duplicated README content and you want it gone without risk.
- You are asked to "clean up" or "tidy" a repository and need a procedure that cannot do damage when followed literally.
- A README has drifted — a duplicated H1, a badge appearing twice (once as Markdown, once as HTML), two stacked badge blocks, or a repeated intro/tagline — and you want it de-duplicated.
- A repository tree has grown hard to read and you want the junk removed while the site, the build and the releases keep working.

## Method

1. **Audit first — enumerate the whole tree.** List every tracked path (`git ls-files`) and every untracked path in the working tree, and write the list down before deleting anything. You are auditing a list, not browsing a directory; a path you never enumerated is a path you cannot safely judge.

2. **Classify every path into exactly one bucket.** Go through the list and put each path into **HIGH-CONFIDENCE JUNK**, **AMBIGUOUS** or **KEEP**, using the three lists below. Classify first and delete later — never the other way round.

   - **Safe to delete (high confidence).** Byte-cache and environment junk that no project can depend on: `__pycache__/`, `*.pyc`, `*.pyo`, `.DS_Store`, `Thumbs.db`, `desktop.ini`, `*.log`, `*.tmp`, `*.bak`, `*.old`, `*.orig`, `*.rej`, `*~`, `*.swp`, `node_modules/`, `.venv/`, `venv/`, `*.egg-info/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.coverage`, `htmlcov/`, and **stale committed archives** — a checked-in `.zip`/`.tar.gz` that is a build output, not a source asset.

   - **Never delete.** Anything that is source, or that a human or a machine reads on purpose: source files; `README*`; `LICENSE*`; `.github/**`; `docs/**` landing pages **and their assets**; anything referenced from a README, a workflow or a page; configuration files; `.gitignore`; `.nojekyll`; `CNAME`; tests; and medical disclaimers.

   - **Ambiguous — report, do not delete.** Build-output directories that in *some* projects hold committed source — `dist/`, `build/`, `out/`, `target/`, `bin/`, `obj/`, `vendor/`; minified files; `*.map`; binaries (`*.exe`, `*.apk`, `*.dll`); data files; and anything you are unsure about. These are decisions, not cleanups.

3. **Check every candidate against references before deleting it.** For each path in the HIGH-CONFIDENCE set, grep the README, the workflows (`.github/**`), the landing pages (`docs/**`) and any manifest (`package.json`, `pyproject.toml`, a build script) for the filename. **A referenced file is never junk** — if a workflow copies it, a page links it or a manifest names it, it moves to KEEP no matter how disposable its name looks.

4. **Delete only the high-confidence set.** Delete exactly the paths that survived step 3. Do not delete anything from the ambiguous list, and do not delete a whole directory by name — delete the enumerated files inside it.

5. **Report the ambiguous set for a human decision.** List each ambiguous path with one line on why it might be junk and one line on what it might be. Deleting these is a judgement call about the project, so it belongs to the owner, not to the cleanup pass.

6. **Commit per repo with a clear message.** One commit per repository, scoped to that repository, with a message that says what was removed and why (e.g. `chore: remove committed build caches and stale archives`). A per-repo commit is what makes a wrong deletion easy to find and revert.

7. **De-duplicate the README.** Fix drift in the same pass, using the rules below. Prefer the repository's own hand-made badges over generic ones — a bespoke badge is the project's, a generic shield is noise.

8. **Re-verify after the change.** Re-render the landing page and re-run the build/release workflow's first step, so a broken reference is caught in the same pass that removed it.

### README de-duplication

- **Duplicated H1.** A README should carry exactly one `# Title`. If the title appears twice — usually after a paste that kept the old heading — delete the duplicate and keep the first.
- **A badge appearing twice, once as Markdown and once as HTML.** The same badge is often present as `[![alt](img)](url)` and again as `<a href="url"><img …></a>`. Keep one form (Markdown, unless the block is HTML-only) and drop the other.
- **Two stacked badge blocks.** A hand-written badge row and a generated one can end up back to back. Keep the repository's own hand-made set and remove the generic duplicate.
- **Repeated header / intro / tagline blocks.** A title-then-tagline-then-title-again, or the same one-line description above and below the badges, is drift. Keep the first occurrence and remove the repeats.
- **Prefer the repo's own badges.** When two badges say the same thing, keep the one the project made for itself — its own colours, its own wording — and remove the generic one.

## Key files / entry points

- The **enumerated file tree** (`git ls-files` plus a working-tree walk) — the audit list every deletion is drawn from; keep it until the commit is made.
- `.github/workflows/**` — the first place to grep for a candidate filename: a workflow that copies a path makes it referenced, and therefore not junk.
- `README*`, `docs/**` — the other reference surfaces (badges, links, assets) and the files README de-duplication edits.
- `.gitignore` — read it to see what the project *intended* never to commit; anything it lists that is nevertheless tracked is a strong junk candidate, and anything tracked that it does not list deserves a second look.
- The repository manifest (`package.json`, `pyproject.toml`, a build script) — the third reference surface, where a filename can be named even if no page links it.

## Gotchas

- **A referenced file is never junk.** This one rule prevents almost every accident: if a README, a workflow, a landing page or a manifest names the file, it stays. Grep before you delete, every time.
- **A build directory may be committed *source*.** `dist/`, `build/`, `out/`, `bin/` and `obj/` are outputs in most projects and committed source in some (a no-build project that serves a pre-built folder, a repo that ships a vendored tree). Verify what a directory *is* in this project; never assume from its name.
- **Generated artefacts usually belong on Releases, not in the tree.** A built `.exe`/`.apk`/archive that is genuinely wanted should be attached to a GitHub Release (a permanent `/releases/latest/download/<asset>` URL), not committed — so "this binary is needed" is not by itself a reason to keep it in the tree.
- **The GitHub API cannot delete a directory in one call.** There is no "remove directory" endpoint; a directory must be emptied file by file (each deletion is a call, and each needs the file's blob SHA), and the empty directory disappears only when its last file is gone. Plan a directory removal as a loop over its files, not a single request.
- **Deletions are recoverable from git history — but a wrong deletion in a live repo still costs.** `git revert` brings a file back, yet the window between deletion and revert is time a live site or a release pipeline spends broken. Recoverable is not the same as free; that is why the audit and the reference check come first.
- **A README may carry an auto-generated region between marker comments.** Text between `<!-- BADGES:START -->` / `<!-- BADGES:END -->` (or `PROJECTS`, or any such pair) is regenerated by a workflow and must never be hand-edited — a manual change there is overwritten on the next run and reads as the workflow "losing" your edit.
- **Writing a file through the GitHub API can silently truncate a line at the first `?`.** A shields.io badge's `?style=…` query — and the line's closing `)` — gets stripped, leaving broken Markdown that renders as literal text. Write the file base64-encoded, then re-read it through the contents API to prove the line is intact.

## Source projects

- [skills](https://github.com/drsamonline/skills) — the knowledge base that documents this procedure and applies it to its own tree.
- [NEO](https://github.com/drsamonline/NEO) — a committed Rust `target/` build tree removed.
- [HMS](https://github.com/drsamonline/HMS) — committed PyInstaller build output (`build/dist/HHMS-Server`, `build/dist/VERSION`) removed.
- [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — a stale Vite `dist/` build removed.
- [conqueror-os](https://github.com/drsamonline/conqueror-os) — `dist/` audited and kept (a referenced, CI-enforced committed single-file build).
- [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) — `dist/` audited and kept (a referenced standalone download).
- [retro-strike](https://github.com/drsamonline/retro-strike) — `dist/` audited and kept (referenced by a README badge/link).
- [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) — `build/` audited and kept (`build/build.js` is a source script).
- [SmartNotes](https://github.com/drsamonline/SmartNotes) — a committed `node_modules/` removed.
