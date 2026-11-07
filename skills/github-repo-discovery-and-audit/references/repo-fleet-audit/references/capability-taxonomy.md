# The capability taxonomy

Nineteen columns, fixed across the fleet. Each entry gives the question the column answers, the
evidence that justifies a mark, and the false positive to avoid. A cell is marked only when you can
point at the source, the README or the UI that proves it.

The taxonomy is deliberately about **user-facing capability**, not implementation. "Zero dependencies"
is a capability because it changes what the user can do (open the file on a plane, trust the artefact,
read the code). "Uses a framework" is not a capability.

The codes and labels are also a machine-readable file, `capability-codes.json`, which the workbook loads
to fix the matrix column order. Edit both together or the report and the workbook will disagree.

---

## A. Delivery — how it reaches the user

| Code | Column | Mark it when | Do not mark it when |
|---|---|---|---|
| `OF` | Offline / no network at runtime | The app works with the network unplugged, and the repo says so or the code proves it (no `fetch`, no CDN, no font service, no analytics). | It merely *caches* after a first load and needs that first load. Note that separately. |
| `PWA` | Installable (service worker) | A `sw.js` (or equivalent) is present. **Prefer the objective file check** over the claim — a repo can ship a service worker and never tell the user, which is a finding in itself. | The landing page says "installable" and there is no service worker. |
| `SF` | Single-file deliverable | One HTML or one source file carries the whole app. Engines loaded lazily on demand still count. | The app is a folder of modules that happens to have an `index.html`. |
| `ZD` | Zero runtime dependencies | No package manager, no CDN, no vendored framework required to run. A single vendored library that is bundled *is* still zero-dependency at runtime — say so in the note. | The build has no deps but the bundle includes a framework. |

## B. Reach — who it serves

| Code | Column | Mark it when | Do not mark it when |
|---|---|---|---|
| `I18N` | Multilingual UI (en / hi / gu or similar) | The user can switch language and the strings actually change. | Content is in another script but there is no UI layer (a Devanagari poem is not i18n). |
| `LAN` | LAN / room / multi-device | Two devices on one network share state, with a transport in the code (SSE, WebSocket, POST polling). | The word "LAN" appears in the description. This is the column most likely to be polluted by a filename. |

## C. Trust — what it does with the user's data

| Code | Column | Mark it when | Do not mark it when |
|---|---|---|---|
| `CR` | Encryption & key handling | There is a real primitive: a KDF (PBKDF2, Argon2), authenticated encryption (AES-GCM), public-key recipients, sealed envelopes, decoy volumes. Name the primitive in the note. | A password gates the UI but the data is in plaintext in localStorage. |
| `EX` | Data export | The user can get their data out in a usable format: ZIP, CSV, JSON, XLSX, SQLite, PDF. | There is a "backup" button that writes an opaque blob nobody else can read — note that as a limitation instead. |

## D. Capability — what it actually does

| Code | Column | Mark it when | Do not mark it when |
|---|---|---|---|
| `SE` | Indexed / ranked search | There is an index, ranking, prefix or fuzzy matching over a real corpus. | A `filter()` over a 30-item list. |
| `CL` | Clinical decision support | It ranks, scores, correlates or orients a clinical decision — repertorisation, dosing, remedy matching, red flags. | It stores clinical data without computing anything over it. |
| `CA` | Longitudinal case records | Records accumulate per subject over time, with a schema and a history. | A one-shot form. |
| `ME` | Media / PDF / audio processing | It transforms media: merge, split, compress, resize, strip EXIF, synthesise, master, analyse a beat grid. | It displays media. |
| `GA` | Game / interactive simulation | It is played, not used: a game, a simulation, an idle builder, a rhythm toy. | It gamifies a tool (streaks, badges) — that is a feature of `UT`. |
| `EN` | Reusable engine or kit | The artefact is *for other developers*: a runtime, an engine, a shared library, a compiler, a compression core. | It has internal modules. Every app does. |
| `TO` | Build / CI / meta tooling | It operates on the fleet or the build rather than on an end user: dashboards, workflow mappers, release packaging, licence checkers, backups. | It is an app with a CI workflow. |
| `CO` | Bundled reference corpus | It ships substantial reference content the user reads or searches: books, rubrics, remedy portraits, datasets. | It ships sample data. |
| `OP` | Optical transfer | Data moves over QR codes, colour matrices or light, with a camera on the other side. | It displays a QR code as a link. |
| `UT` | General utility / toolbox | It is a tool, a converter, a calculator, a launcher, a cleaner — the user's own work on their own machine. | It is a domain application. |
| `ED` | Teaching / curriculum | There is a progression designed to teach: exercises, checks, starters that must fail, a course order. | It has a help page. |

---

## The objective convention flags

These are booleans, checkable by file existence, and they make a conformance table for free. They are
*not* capabilities — do not merge them into the matrix above.

The `landing` and `play` paths below are one estate's house layout, shipped as defaults in
`conformance.json`. Point `05_classify.py --conformance conformance.json` at your own paths if yours
differ; a conformance table that measures someone else's folder names is worse than none.

`sw` and the `PWA` capability detect the same file. Keep both — one is a user-facing capability, the
other a checkable flag — but take one answer: when `PWA` is marked, `sw` is true. The workbook enforces
this so the two cannot diverge.

| Flag | Check |
|---|---|
| landing | `docs/index.html` or `index.html` at the root |
| play | a runnable app under `docs/play/` |
| sw | a `sw.js` anywhere |
| tests | a `test*` / `selftest*` file or a `tests/` directory |
| ci | anything under `.github/workflows/` |
| licence | `LICENSE*` or `LICENCE*` |
| changelog | `CHANGELOG*` |
| readme | `README*` |

Report the totals and, more usefully, the **gaps**: repositories with no test, no CI, or a service
worker they never advertise. Those are the cheapest improvements available and they are invisible
until someone counts.

## Classifying honestly

- **Read the entry point first.** The primary HTML page's headings are the most reliable description of
  what the app does, because they are written for a user rather than for a maintainer.
- **Read the named units.** A file list of `repertorise`, `score`, `matrix`, `explain` tells you the
  capability is real; a file list of `render`, `init`, `handleClick` tells you nothing.
- **When in doubt, leave it out and note it.** A false positive in the matrix propagates into every
  recommendation downstream. A false negative costs one line of prose.
- **Keep a note per repo.** One sentence, written while you still have the source open, saying what
  this repo is and whether it is well placed in the fleet. This note becomes the catalogue in the
  report and it is much cheaper to write now than to reconstruct later.
