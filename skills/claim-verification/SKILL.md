---
name: claim-verification
description: Turn the claims a project makes — in its docs, its UI, its test coverage, its platform support — into checks that run, and prove each guard actually fires before trusting it. Use when a build is green but nobody has verified the product, when adding a guard or CI check, when a feature "works" only because it compiles, or when the same bug keeps coming back.
metadata:
  title: "Verify the claim, not the code"
---

# Verify the claim, not the code

A green build says the code compiles and the tests you wrote pass. It says
nothing about whether the product does what it says. This skill is the method
for closing that gap: find the claims, make each one a command, and prove the
command fails when the claim is false.

## When to use

- A suite is green and the product has still not been looked at.
- You are about to add a CI guard, a smoke test or a check script.
- A feature is "done" because it compiles on three platforms.
- The same class of bug has shipped twice.
- Someone asks "does X actually work?" and the answer would be a guess.

## Method

1. **List the claims, not the code.** Read the README, the user guide, the
   release notes and the UI copy, and write down every statement that asserts
   behaviour: "every operation is ported", "the app shows the equivalent
   command", "the passphrase is prompted for", "works on Windows". These are
   the things that can be false while every test passes.

2. **Rank by cost of being wrong.** A wrong number in a README is cheap; a
   documented feature that does not exist, or a destructive operation that
   reports success without doing the work, is expensive. Verify the expensive
   ones first.

3. **Make each claim a command that can fail.** Not a script that prints; a
   check with a non-zero exit and a message naming what broke. Where the claim
   is about a document, parse the document and compare it to the code's own
   source of truth (a manifest, a schema, an enum) rather than to a second
   hand-written copy.

4. **Drive the product where it runs.** Render the interface, dispatch the
   keystroke, click the button, run the operation against a real file. A
   claim about behaviour cannot be checked by reading the code that implements
   it.

5. **Prove the guard fires.** Break the thing deliberately and watch the check
   fail with the right message. A guard that has never failed is a guard
   nobody knows works. Restore, watch it pass, and only then commit it.

6. **Keep the probe.** Every ad-hoc verification you run in a shell and throw
   away is verification that disappears tomorrow. If a check found something
   worth knowing, it belongs in the repository.

7. **Run the checks in CI, on the platform that matters.** A Windows-only code
   path is not verified by a Linux run. If a runner has the capability — a
   desktop session, a browser, a PE parser — use it rather than assuming.

8. **Read numbers from the run, never type them.** Test counts, coverage,
   ported-operation counts. A number copied by hand drifts the first time the
   suite grows.

## What this found, as a catalogue

Each of these was green in CI when it was found, in a project with 180 tests
and three-platform builds.

| Claim | How it was checked | What was actually true |
|---|---|---|
| "The app shows the equivalent command for every operation" | Ported the app's command builder and the CLI's argument parser into one script and ran all 87 generated commands through the parser | The commands were all correct — but the **Run button enabled while a required flag was empty**, offering an action it knew would fail |
| "The passphrase is prompted for" | Searched the CLI for any prompt code | None existed. The documented command **failed to parse**. The doc described a feature never written |
| "`pulse priority --commit` works" | Ran every documented command through the parser | `commit` was not a declared parameter, so the parser demanded a value. One line in the global switch list |
| "The smoke test exercises every ported operation" | Compared the commands in the workflow against the manifest | 76 of 87. Four were reachable and became checks; the rest were named as gaps |
| "The window manager works" | Launched a window on a Windows runner, snapped it, re-read its geometry | It did work — and **`rollup` reported the height it asked for, not the one Windows allowed** |
| "Paths print correctly" | Compared one captured output across platforms | Windows printed `smoke\a.txt` where every example showed `smoke/a.txt`; em dashes rendered as `â€”`; the capture file was CRLF |
| "Contrast is fine" | Computed WCAG ratios from the token values | Five pairs failed AA; the least legible colour carried every field label |
| "The demo is current" | Regenerated it and diffed | The captured output was hand-kept and had drifted; nothing regenerated it |

## Guards worth having

Each one exists because it caught a real mistake, and each was proven by
breaking the thing it watches.

- **Names that no longer exist** — grep for the old identifier after a rename.
- **A count that cannot drift** — assert the declared total against the
  manifest that drives the code.
- **Documented commands parse** — run every example in the docs through the
  real parser.
- **Built artefacts are current** — rebuild and diff against what is committed.
- **Published pages resolve** — serve the site and fetch every reference.
- **The interface loads** — headless browser, assert the DOM came up.
- **The interface behaves** — drive it: type, switch, press the shortcut, check
  the result.
- **A tag matches the version** — compare the tag to the package manifest
  before publishing.

## Gotchas

- **Test the test.** Several "findings" in the source project were bugs in the
  harness: reading `rect.width` where the data carried edges, typing into the
  wrong input because it came first in the DOM, and a `git checkout -- dir`
  that updated the index as well as the working tree, so a staleness check
  compared a thing to itself. Run the harness against a known-good state first.
- **A guard that reports instead of failing is not a guard.** Report-only mode
  is a reasonable first step to find out whether your check is even correct;
  it is not where a check should live.
- **Regex surgery on source needs word boundaries.** Matching
  `path.to_string_lossy()` without one turned `out_path` into
  `out_savehorse_core::display_path(&path)`, across fourteen sites, and the
  repair pass made it worse. Use a boundary, then check every replacement
  names a variable that exists.
- **ES modules do not load from `file://`** without
  `--allow-file-access-from-files`. A headless check that omits it reports the
  app as blank and sends you hunting a bug that is not there.
- **`unwrap_or_default()` and `let _ =` hide failures** where the value
  matters. Audit them; keep the ones that are genuinely optional and turn the
  rest into errors.
- **Two writers to one branch race.** A delivery bot that commits on its own
  schedule will cancel your runs and lose your pushes; fetch, rebase and push
  in one command, and expect it.
- **Proving a guard fires is not optional.** Of eight guards added in the
  source project, every one was checked by breaking its subject — and two were
  wrong on the first attempt.

## Related

- `doc-claims-guard` — the narrower case: prose that nothing recomputes. This
  skill covers that plus UI behaviour, platform parity and coverage.
- `code-review-and-release-gate` — the ship-or-block judgement this feeds.
- `debugging-and-recovery` — once a check has found the defect.

## Source projects

- [`drsamonline/savehorse`](https://github.com/drsamonline/savehorse) — thirteen
  Rust crates, a CLI and a Tauri desktop app; 87 operations, 181 tests, eight
  guards, and every bug in the catalogue above found by verifying a claim
  rather than reading code.
