# skills

**A machine-consumable knowledge base of the working methods behind the drsamonline projects.**

[![Landing page](https://img.shields.io/badge/landing%20page-open-2e7d32?style=flat-square)](https://drsamonline.github.io/skills/)
[![All projects](https://img.shields.io/badge/All%20projects-hub-2e7d32?style=flat-square)](https://drsamonline.github.io/)
[![Type: knowledge base](https://img.shields.io/badge/type-knowledge%20base-586069?style=flat-square)](https://drsamonline.github.io/skills/)
[![Format: Markdown + JSON](https://img.shields.io/badge/format-Markdown%20%2B%20JSON-586069?style=flat-square)](https://github.com/drsamonline/skills)
[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-2e7d32?style=flat-square)](LICENSE)

**Landing page:** <https://drsamonline.github.io/skills/> &nbsp;·&nbsp; **All projects:** <https://drsamonline.github.io/>


This repository is a **machine-consumable knowledge base**. Each of the
projects under [`drsamonline`](https://github.com/drsamonline) has its working
*method* extracted into a reusable **skill**, so the same approach can be
reused, extended or branched from instead of being rediscovered.

## Conforms to the Agent Skills standard

This repository conforms to the **Agent Skills** standard — see
[agentskills.io/specification](https://agentskills.io/specification). That is a
claim we can make and did not, which is free credibility we had already earned.

Run `python3 validate.py` to check it. The validator enforces the standard's rules
for `name` and `description`, and the folder layout:

- **name** — 1-64 characters; lowercase letters, digits and single hyphens only; no
  leading, trailing or doubled hyphen; and equal to the folder name.
- **description** — 1-1024 characters, present.
- **layout** — a directory holding `SKILL.md` with YAML frontmatter.

**What the claim does and does not mean.** We conform on the fields the standard
defines for `name` and `description`, and on the layout. We do **not** claim support
for every optional field: where one is unused it is *absent*, not present-and-empty,
which is what the standard allows. Anything more specific than that would be
inventing a compatibility we have not tested.

Non-directory entries are **skipped** rather than failed — this repository holds a
`.gitkeep`, and a validator that calls a placeholder file a broken skill is a
validator people stop running.

There are two kinds of skill:

- **Technique skills** — the cross-cutting methods that recur across many
  projects: the offline-first single-file web app, Android WebView packaging,
  the portable EXE launcher, the shared build/release workflow, the landing-page
  + SEO conventions, the auto-updating showcase hub, the open-data pipeline, the
  LAN single-server architecture, the theme-aware GitHub profile, optical file
  transfer, embedded-bundle feature gating, and safe repository cleanup.
- **Imported first-party skills** — 501 skills from eighteen upstream skill collections (Anthropic, Google, Vercel, Hugging Face, Cloudflare, MiniMax, Addy Osmani, Matt Pocock, Matteo Collina, Jesse Vincent, Emil Kowalski, Steph Ango, Seth Hobson and others), deduplicated by topic and kept under their own licences.
- **Vendored packs** — five packs and the seventeen skills they were merged from, imported unchanged from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) (MIT). Each carries its own `LICENSE`; the pack is the merged reading, the individual skill is the same text on its own.
- **Project skills** — one per repository: what the project is, how it is built,
  how it is released, and what makes its workflow distinctive.

**Catalogue:** `1485` skills across 28 categories. The machine-readable index is [`catalog.json`](catalog.json); the landing page is <https://drsamonline.github.io/skills/>.

## Repository layout

```
README.md                     # this file — human index + how AIs consume the repo
llms.txt                      # short plain-text pointer for AI agents
catalog.json                  # machine-readable index of every skill
skills/<skill-id>/SKILL.md    # the skill itself (YAML front-matter + body)
skills/<skill-id>/meta.json   # machine-readable metadata for that skill
docs/                         # the landing page (its own sub-website)
```

Skill ids are lowercase-hyphenated and stable. Categories are a fixed set:

`web-app-patterns`, `android-packaging`, `windows-desktop`, `game-engine`, `data-and-schema`, `health-tools`, `landing-and-seo`, `ci-and-release`, `marketing`, `docs-and-planning`, `code-quality`, `linux-desktop`, `sysadmin-ops`, `media-design`, `frontend-ui`, `backend-services`, `testing-qa`, `security-audit`, `cloud-and-deploy`, `ai-and-ml`, `office-docs`, `engineering-workflow`, `notes-knowledge`, `mobile-apps`, `browser-automation`, `google-workspace`, `game-dev`, `product-management`.

## The skill format

### `SKILL.md`

YAML front-matter, then a body with five fixed sections.

```markdown
---
name: Human-readable skill name
description: One sentence — what the skill lets you do.
---

# Human-readable skill name

A short introduction.

## When to use
- ...

## Method
1. ...

## Key files / entry points
- ...

## Gotchas
- ...

## Source projects
- [repo](https://github.com/drsamonline/<repo>) — what it demonstrates.
```

### `meta.json`

```json
{
  "id": "lowercase-hyphenated-id",
  "name": "Human-readable skill name",
  "category": "one of the nine categories",
  "description": "One sentence.",
  "tags": ["..."],
  "source_repos": ["RepoName", "..."],
  "version": "1.0.0",
  "updated": "YYYY-MM-DD",
  "source_snapshot": { "RepoName": "<latest commit SHA when derived>" },
  "subskills": ["related-skill-id", "..."]
}
```

`source_snapshot` maps each source repository to its latest commit SHA at the
time the skill was derived, so a consumer can tell whether the skill still
matches the code it describes.

## The catalogue

Every skill in the repository, by category, with the one line that tells you whether to open it. The id is the directory: `skills/<id>/SKILL.md` holds the method, `meta.json` its provenance, its licence and its upstream commit. Where a category has an index pack, the pack is named first — it is the routing table for that category.

`1485` skills across 28 categories. The descriptions here are one-line summaries; the full trigger text is the `description` field in `meta.json` and at the top of each `SKILL.md`.

### Web app patterns (`web-app-patterns`) — 19 skills

| Skill | What it does | Licence |
|---|---|---|
| [`ambient-sound-studio`](skills/ambient-sound-studio/SKILL.md) | A private, offline ambient sound mixer in a single HTML file: 25 synthesised layers, 36 presets, EN/HI/GU, WAV and Opus export,… | — |
| [`astro-kit-panchang`](skills/astro-kit-panchang/SKILL.md) | Sun and moon longitude (Meeus), Lahiri ayanamsa, sunrise/sunset/transit and the derived tithi, nakshatra, yoga and karana — the… | — |
| [`blinkcode-ai-spectracode`](skills/blinkcode-ai-spectracode/SKILL.md) | Optical file transfer as a vanilla-JS PWA: a file becomes a 'File DNA' container painted as SpectraCode colour matrices, decoded… | — |
| [`blinktransfer-animated-qr`](skills/blinktransfer-animated-qr/SKILL.md) | Offline file transfer over animated QR codes at ~20 FPS: a Vite-built PWA compresses files, renders a header plus a data stream… | — |
| [`book-kit-companion`](skills/book-kit-companion/SKILL.md) | The companion-app-from-a-book pattern in one zero-dependency file: chapters, key points, practices, flashcards, in-book search… | — |
| [`compress-kit-streams`](skills/compress-kit-streams/SKILL.md) | gzip, deflate and deflate-raw over the platform's Compression Streams, with byte and base64 helpers — the browser counterpart to… | — |
| [`conqueror-os-workspace`](skills/conqueror-os-workspace/SKILL.md) | A private, offline resilience workspace in a single HTML file — read, reflect, journal, track and review — with no server, no… | — |
| [`crypto-kit-aes-gcm`](skills/crypto-kit-aes-gcm/SKILL.md) | AES-256-GCM encryption with PBKDF2-SHA256 passphrase keys, a sealed envelope and a one-time-view helper on the Web Crypto API —… | — |
| [`lan-kit-sse-room`](skills/lan-kit-sse-room/SKILL.md) | A LAN room in the browser: a client over Server-Sent Events for server-to-client and POST for client-to-server, with a host URL… | — |
| [`lan-single-server-architecture`](skills/lan-single-server-architecture/SKILL.md) | A multi-user system that runs entirely on a hospital LAN: a Python server owns the SQLite database, a vanilla-JS UI runs in a… | — |
| [`offline-first-single-file-web-app`](skills/offline-first-single-file-web-app/SKILL.md) | Build a whole app as one self-contained index.html — inline CSS/JS, no CDN, no build step — that runs from file:// or GitHub… | — |
| [`optical-file-transfer`](skills/optical-file-transfer/SKILL.md) | Move a file between two devices with no network, Bluetooth or cable, by rendering it as animated QR codes or colour-matrix frames… | — |
| [`optical-kit-fountain`](skills/optical-kit-fountain/SKILL.md) | A systematic LT fountain code with self-describing frames and a pluggable codec — the shared optical-transfer core behind the QR… | — |
| [`qr-code-encoder`](skills/qr-code-encoder/SKILL.md) | A QR encoder in one dependency-free file: byte mode, ECC L/M/Q/H, versions 1-40, Reed-Solomon over GF(256) and the ISO/IEC 18004… | — |
| [`smartbill-app`](skills/smartbill-app/SKILL.md) | A fast, serverless single-page billing and invoicing app for Indian businesses: GST-ready (HSN/SAC, CGST/SGST, state codes,… | — |
| [`smartnotes-ai-notes`](skills/smartnotes-ai-notes/SKILL.md) | An AI-powered note capture, categorisation and reminder-scheduling app with a brutalist UI: write in plain English and an LLM… | — |
| [`srs-kit-sm2`](skills/srs-kit-sm2/SKILL.md) | Schedule flashcards with SM-2 in one zero-dependency file: ease, interval, reps, lapses, due cards, stats and a configurable… | — |
| [`ttb-tiny-toolbox-extension`](skills/ttb-tiny-toolbox-extension/SKILL.md) | A Manifest V3 browser extension bundling 590 small utilities across 18 categories into one offline-first popup, with one source… | — |
| [`ui-kit`](skills/ui-kit/SKILL.md) | A reactive UI layer small enough for a single file — signals, computed, reactive effects, hyperscript, a keyed list, events, a… | — |

### Android packaging (`android-packaging`) — 1 skills

| Skill | What it does | Licence |
|---|---|---|
| [`android-webview-apk-packaging`](skills/android-webview-apk-packaging/SKILL.md) | Wrap a static single-file web app into a dependency-free Android WebView APK (platform framework only, no AndroidX), signed with… | — |

### Windows & desktop (`windows-desktop`) — 9 skills

| Skill | What it does | Licence |
|---|---|---|
| [`all4one-utility-suite`](skills/all4one-utility-suite/SKILL.md) | 551 Windows tools across 45 plugin packs compiled into one self-contained portable utility_suite.exe (Python, tkinter GUI + CLI)… | — |
| [`cldr-command-launcher`](skills/cldr-command-launcher/SKILL.md) | A single dependency-free Rust binary that sits in the system tray, pops up on a hotkey, and routes whatever you type — maths,… | — |
| [`embedded-bundle-feature-gating`](skills/embedded-bundle-feature-gating/SKILL.md) | Ship many features in one self-contained binary, compile them into a single embedded archive, and let users turn each feature on… | — |
| [`lexora-exact-compression`](skills/lexora-exact-compression/SKILL.md) | A text-cleaning and exact-compression system: canonicalize documents conservatively, then compress with guaranteed byte-exact… | — |
| [`lockhtml-file-encryption`](skills/lockhtml-file-encryption/SKILL.md) | Encrypt any file into a single self-contained .html that asks for a PIN (AES-256-GCM + Argon2id), with one-time view, expiry,… | — |
| [`neo-nova-compiler`](skills/neo-nova-compiler/SKILL.md) | A statically-typed compiled systems language: a Rust compiler lowers NOVA through lexer, parser, semantic analyser, SIR and a… | — |
| [`pyinstaller-portable-exe-launcher`](skills/pyinstaller-portable-exe-launcher/SKILL.md) | Turn a static web app into one double-clickable portable Windows .exe: a tiny Python launcher serves the bundled app/ over… | — |
| [`the-browser-aetheris`](skills/the-browser-aetheris/SKILL.md) | An experimental C++20 browser engine derived from Ladybird/SerenityOS, built with CMake + vcpkg and tested with CTest; explicitly… | — |
| [`ultimate-windows-optimizer`](skills/ultimate-windows-optimizer/SKILL.md) | A PowerShell + batch toolkit that applies documented, fully reversible Windows 10/11 debloat and performance tweaks, with real… | — |

### Games & engines (`game-engine`) — 12 skills

| Skill | What it does | Licence |
|---|---|---|
| [`aethelgard-engine-rpg`](skills/aethelgard-engine-rpg/SKILL.md) | The vanilla-JavaScript engine behind Aethelgard: Chronicles of Fate — small modules loaded in script order behind one global… | — |
| [`aethelgard-games-deployment`](skills/aethelgard-games-deployment/SKILL.md) | A deployment repo holding the built, playable copies of two Aethelgard browser games — The Books (a 36-chapter visual novel) and… | — |
| [`aethelgardvn-saga-engine`](skills/aethelgardvn-saga-engine/SKILL.md) | Saga: a small, dependency-free visual-novel engine for the browser — plain JavaScript, one stylesheet, no build step, works… | — |
| [`art-kit`](skills/art-kit/SKILL.md) | The art primitives for offline apps — an indexed palette, a pixel canvas with nearest-neighbour scaling, draw ops, a delta undo… | — |
| [`audio-kit`](skills/audio-kit/SKILL.md) | Synthesis, theory, patterns and notation for offline apps — a pure ADSR envelope, oscillator voices, filters, noise and a mixer;… | — |
| [`dance-fight-rhythm-game`](skills/dance-fight-rhythm-game/SKILL.md) | A single-file browser rhythm game where every fight move is a dance move: the track's beat is analysed up front into an offline… | — |
| [`game-kit-fixed-timestep`](skills/game-kit-fixed-timestep/SKILL.md) | A fixed-timestep game loop with input, scenes and save/load in one dependency-free file — the shared game core the browser games… | — |
| [`idle-city-ages-of-growth`](skills/idle-city-ages-of-growth/SKILL.md) | A single-file idle city-builder that grows from a Stone Age village to a Fusion Age world-city: roads, zoning, power and… | — |
| [`neon-engine-open-world`](skills/neon-engine-open-world/SKILL.md) | A code-only WebGL engine for open-world browser shooters: no asset files, every texture/mesh/sound generated at runtime, ES… | — |
| [`neon-games-arcade`](skills/neon-games-arcade/SKILL.md) | A deployment repo holding two open-world games built on the Neon Engine — Dead Zone (zombie survival) and Neon Police (crime… | — |
| [`neon-runner-auto-fire-shooter`](skills/neon-runner-auto-fire-shooter/SKILL.md) | A retro auto-fire side-scrolling shooter in one self-contained HTML file (vanilla JS + canvas): move, jump, duck — the gun fires… | — |
| [`retro-strike-software-3d`](skills/retro-strike-software-3d/SKILL.md) | A complete retro third-person shooter in one HTML file with a custom software 3D renderer, a live chiptune synth and procedural… | — |

### Data & schema (`data-and-schema`) — 5 skills

| Skill | What it does | Licence |
|---|---|---|
| [`homoeopathic-materia-medica-repertory-json`](skills/homoeopathic-materia-medica-repertory-json/SKILL.md) | 13 public-domain homoeopathic classics (1840–1906, ~108k rubrics) extracted into clean, app-ready, verbatim JSON with a… | — |
| [`materia-medica-builder`](skills/materia-medica-builder/SKILL.md) | An offline, no-dependency PWA that lets a practitioner build a personal materia medica and repertory — remedies, symptoms,… | — |
| [`ml-kit`](skills/ml-kit/SKILL.md) | The classic ML algorithms from scratch for offline features — tf-idf ranking, Naive Bayes, k-NN, k-means, PCA, ID3, linear… | — |
| [`open-data-extraction-pipeline`](skills/open-data-extraction-pipeline/SKILL.md) | Turn raw OCR'd source texts into clean, app-ready JSON with a verbatim-fidelity rule: nothing invented, unknowns null, per-book… | — |
| [`search-kit-ranked-search`](skills/search-kit-ranked-search/SKILL.md) | Ranked search over a big corpus in one zero-dependency file: an inverted index with prefix and fuzzy matching, scored hits and a… | — |

### Health tools (`health-tools`) — 14 skills

| Skill | What it does | Licence |
|---|---|---|
| [`bmi-bmr-tdee-macros-fluid-calculator`](skills/bmi-bmr-tdee-macros-fluid-calculator/SKILL.md) | A single-file, offline clinical calculator for adult outpatients: BMI, BMR (Mifflin-St Jeor), TDEE, macros, fluid requirement and… | — |
| [`boericke-repertory`](skills/boericke-repertory/SKILL.md) | A free, offline digital edition of Boericke's Repertory in one HTML file: instant search across 6,110 rubrics, a repertorisation… | — |
| [`case-kit-clinical`](skills/case-kit-clinical/SKILL.md) | Clinical case tracking in one zero-dependency file: sections, dated symptoms with severity, follow-ups with remedy and response,… | — |
| [`gentle-pediatrics-companion`](skills/gentle-pediatrics-companion/SKILL.md) | A triage-first offline companion app for a parent at the cot side: nine common childhood situations, an always-visible red-flag… | — |
| [`hms-hospital-management`](skills/hms-hospital-management/SKILL.md) | HHMS: a LAN-based hospital management system for homeopathic hospitals — a Python server owns the SQLite database, a WebView2… | — |
| [`mnemosyne-companion`](skills/mnemosyne-companion/SKILL.md) | A single offline HTML study companion for Mnemosyne Materia Medica: 100 polycrest remedies as poetic pearls, keynotes and… | — |
| [`open-materia-medica`](skills/open-materia-medica/SKILL.md) | A plain-language homeopathic materia medica — 344 remedy portraits, each beside the substance's real pharmacology and toxicology… | — |
| [`read-live-transform-app`](skills/read-live-transform-app/SKILL.md) | An offline PWA companion to the book Read. | — |
| [`remedy-relationship-explorer`](skills/remedy-relationship-explorer/SKILL.md) | An offline single-file explorer for homeopathic remedy relationships — 686 remedies, 7,786 links from four public-domain materia… | — |
| [`repertory-kit-repertorisation`](skills/repertory-kit-repertorisation/SKILL.md) | Grade-weighted homeopathic repertorisation in one zero-dependency file: rubric grading 1/2/3, remedy scoring, must-have and… | — |
| [`skin-case-tracker`](skills/skin-case-tracker/SKILL.md) | A private, offline PWA that tracks a skin case over time on the HHMS model — History, Habits, Mapping, Symptoms logged daily and… | — |
| [`the-symphony-companion`](skills/the-symphony-companion/SKILL.md) | A pocket PWA companion to The Symphony of the Present: the book's ideas as cards, its practices as a checklist, a breathing… | — |
| [`unstoppable-mind-companion`](skills/unstoppable-mind-companion/SKILL.md) | An offline companion app to The Unstoppable Mind: the book's key points and exercises, a 7-day challenge and flashcards — in a… | — |
| [`whispering-body-first-aid`](skills/whispering-body-first-aid/SKILL.md) | A free, offline home first-aid companion (EN/HI/GU) with 30 commonly used homeopathic first-aid remedies, a plain-language… | — |

### Landing & SEO (`landing-and-seo`) — 5 skills

| Skill | What it does | Licence |
|---|---|---|
| [`auto-updating-showcase-hub`](skills/auto-updating-showcase-hub/SKILL.md) | A single static page that lists every repository by reading the GitHub API at runtime, with an embedded JSON snapshot fallback, a… | — |
| [`matneo-storefront`](skills/matneo-storefront/SKILL.md) | A static storefront served from docs/ with no build step: a single data file (docs/data/products.json) drives the catalogue, so… | — |
| [`profile-kit`](skills/profile-kit/SKILL.md) | A small, reusable kit for a theme-aware, self-updating GitHub profile — a hero banner, a metrics card and a README generator —… | — |
| [`static-landing-page-seo`](skills/static-landing-page-seo/SKILL.md) | The house landing-page recipe: a bespoke self-contained docs/index.html with a distinct theme, a full SEO head (canonical, OG,… | — |
| [`theme-aware-github-profile`](skills/theme-aware-github-profile/SKILL.md) | A professional, self-updating GitHub profile README — a bespoke light/dark hero served through <picture>, a lowlighter/metrics… | — |

### CI & release (`ci-and-release`) — 4 skills

| Skill | What it does | Licence |
|---|---|---|
| [`app-builder-kit`](skills/app-builder-kit/SKILL.md) | The shared kit that turns a static web app into a single-file portable Windows EXE (PyInstaller) and an Android WebView APK… | — |
| [`kit-adoption-audit`](skills/kit-adoption-audit/SKILL.md) | Measure which apps actually consume each shared kit and which hand-roll the same capability, from repository trees and blob SHAs… | — |
| [`reusable-build-release-workflow`](skills/reusable-build-release-workflow/SKILL.md) | One GitHub Actions workflow per app repo builds the portable EXE and Android APK, publishes them to a fixed-tag release, and… | — |
| [`safe-repo-cleanup`](skills/safe-repo-cleanup/SKILL.md) | An audit-first procedure for removing build junk, caches, temp files, stale archives and duplicated README content from a… | — |

### Marketing (`marketing`) — 16 skills

| Skill | What it does | Licence |
|---|---|---|
| [`directory-submissions`](skills/directory-submissions/SKILL.md) | Submit a project to a directory or an "awesome" list — a link, not a storefront — so people and AI engines can find it. | — |
| [`free-tool-marketing`](skills/free-tool-marketing/SKILL.md) | Plan and judge a free, genuinely useful tool as the way people find the paid work — engineering as marketing. | — |
| [`linkedin-comment-drafter`](skills/linkedin-comment-drafter/SKILL.md) | Draft a LinkedIn comment on someone else's post from its URL, or reshare (repost) it to your feed with optional commentary. | MIT |
| [`linkedin-content-planner`](skills/linkedin-content-planner/SKILL.md) | Generate a 7-day LinkedIn content plan from a theme, audience, and pillars. | MIT |
| [`linkedin-employee-advocacy`](skills/linkedin-employee-advocacy/SKILL.md) | Stand up and run a LinkedIn employee advocacy program for a marketing or sales team. | MIT |
| [`linkedin-engager-analytics`](skills/linkedin-engager-analytics/SKILL.md) | Pull the people who liked or commented on any LinkedIn post and segment them by ICP fit (peer / aspirational / prospect / other). | MIT |
| [`linkedin-hook-extractor`](skills/linkedin-hook-extractor/SKILL.md) | Reverse-engineer the hook formula from a viral LinkedIn post URL. | MIT |
| [`linkedin-humanizer`](skills/linkedin-humanizer/SKILL.md) | Remove AI tells from LinkedIn posts/comments: 2026 vocabulary density, reveal bridges, staccato fragments, stacked triads,… | MIT |
| [`linkedin-interviewer`](skills/linkedin-interviewer/SKILL.md) | Interview the user for the raw material their posts are made of. | MIT |
| [`linkedin-marketing`](skills/linkedin-marketing/SKILL.md) | Plan, draft, audit, and publish LinkedIn posts and comments. | MIT |
| [`linkedin-post-writer`](skills/linkedin-post-writer/SKILL.md) | Draft a new LinkedIn post from scratch using one of 20 2026 hook formulas (anaphora, R.I.P., time-anchor, curiosity-gap,… | MIT |
| [`linkedin-profile-optimizer`](skills/linkedin-profile-optimizer/SKILL.md) | Audit and rewrite a LinkedIn profile end-to-end for 2026: headline, About 7-step, Featured, banner, photo, Experience metrics,… | MIT |
| [`linkedin-reply-handler`](skills/linkedin-reply-handler/SKILL.md) | Draft a reply to one LinkedIn comment from its URL, or sweep a whole thread from just the post URL and draft a reply to every… | MIT |
| [`linkedin-repurposer`](skills/linkedin-repurposer/SKILL.md) | Repurpose existing content into a native LinkedIn post. | MIT |
| [`linkedin-thread-monitor`](skills/linkedin-thread-monitor/SKILL.md) | Track which of your LinkedIn comments earned author replies. | MIT |
| [`product-copywriting`](skills/product-copywriting/SKILL.md) | Write honest product copy for a landing page, a README or a store listing — a headline, a value line, a CTA — that reads like a… | — |

### Planning & docs (`docs-and-planning`) — 32 skills

| Skill | What it does | Licence |
|---|---|---|
| [`academy-guide`](skills/academy-guide/SKILL.md) | When a user asks a question about Claude, a Claude product, or a general "how do I use AI for X" question, check the Academy… | Apache-2.0 |
| [`ai-project-manager`](skills/ai-project-manager/SKILL.md) | Create and maintain repository planning documents, phased implementation plans, approval checkpoints, task status, and validation… | MIT |
| [`discernment-nudge`](skills/discernment-nudge/SKILL.md) | People often take an AI answer at face value, especially when it's confidently written and well-structured. | Apache-2.0 |
| [`doc-coauthoring`](skills/doc-coauthoring/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. | NOASSERTION |
| [`documentation`](skills/documentation/SKILL.md) | Creates, structures, and reviews technical documentation following the Diátaxis framework (tutorials, how-to guides, reference,… | MIT |
| [`egm-bootstrap`](skills/egm-bootstrap/SKILL.md) | Bootstrap directory README.md files across a repository subtree. | Apache-2.0 |
| [`egm-brainstorm`](skills/egm-brainstorm/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`egm-draft`](skills/egm-draft/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`egm-drift-report`](skills/egm-drift-report/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`egm-resolve`](skills/egm-resolve/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`egm-review`](skills/egm-review/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`egm-review-loop`](skills/egm-review-loop/SKILL.md) | When running in Codex or ChatGPT Work, first read Codex integration(../../docs/codex.md). | Apache-2.0 |
| [`hugo`](skills/hugo/SKILL.md) | Build, edit, validate, and troubleshoot Hugo sites, including content, templates, assets, taxonomies, redirects, output formats,… | MIT |
| [`init`](skills/init/SKILL.md) | Creates, updates, or optimizes an AGENTS.md file for a repository with minimal, high-signal instructions covering… | MIT |
| [`internal-comms`](skills/internal-comms/SKILL.md) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. | Apache-2.0 |
| [`linting-neostandard-eslint9`](skills/linting-neostandard-eslint9/SKILL.md) | Configures ESLint v9 flat config and neostandard for JavaScript and TypeScript projects, including migrating from legacy… | MIT |
| [`mdbook`](skills/mdbook/SKILL.md) | Create, edit, validate, and publish mdBook projects or mdBook-based KDP manuscripts. | MIT |
| [`octocat`](skills/octocat/SKILL.md) | Use this skill whenever the prompt contains any `github.com` URL, even if the user only pastes a link and gives no… | MIT |
| [`pack-planning-and-docs`](skills/pack-planning-and-docs/SKILL.md) | Write the plan down and publish the documentation: repository planning documents (SPEC, ROADMAP, TASKS) for AI-assisted work,… | MIT |
| [`planning-with-files`](skills/planning-with-files/SKILL.md) | Persistent file-based planning for multi-step AI-agent work. | MIT |
| [`planning-with-files-ar`](skills/planning-with-files-ar/SKILL.md) | تخطيط مستمر قائم على الملفات لعمل وكلاء الذكاء الاصطناعي متعدد الخطوات. | MIT |
| [`planning-with-files-de`](skills/planning-with-files-de/SKILL.md) | Persistente dateibasierte Planung für mehrstufige Arbeit mit KI-Agenten. | MIT |
| [`planning-with-files-es`](skills/planning-with-files-es/SKILL.md) | Planificación persistente basada en archivos para tareas multipaso de agentes de IA. | MIT |
| [`planning-with-files-zh`](skills/planning-with-files-zh/SKILL.md) | 用于多步骤 AI 代理工作的持久化文件规划系统。将 task_plan.md、findings.md 和 progress.md 保存在磁盘上，生命周期钩子会注入选定的项目规划上下文。自动恢复只读取项目规划文件。只有显式运行… | MIT |
| [`planning-with-files-zht`](skills/planning-with-files-zht/SKILL.md) | 用於多步驟 AI 代理工作的持久化檔案規劃。將 task_plan.md、findings.md 與 progress.md 保存在磁碟上，生命週期鉤子會注入選定的專案規劃內容。自動恢復只讀取專案規劃檔案；只有明確執行 session-catchup.py… | MIT |
| [`wayfinder`](skills/wayfinder/SKILL.md) | Create or maintain SPEC.md, MAP.md, and ANSWERS.md for large or unclear work. | MIT |
| [`wayfinder-mattpocock`](skills/wayfinder-mattpocock/SKILL.md) | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and… | MIT |
| [`writing-beats`](skills/writing-beats/SKILL.md) | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | MIT |
| [`writing-for-agents`](skills/writing-for-agents/SKILL.md) | Writing documents for agents. | MIT |
| [`writing-fragments`](skills/writing-fragments/SKILL.md) | Writing, explore: mine raw fragments, no structure yet. | MIT |
| [`writing-guidelines`](skills/writing-guidelines/SKILL.md) | Review docs/prose for Writing Guidelines compliance. | NOASSERTION |
| [`writing-shape`](skills/writing-shape/SKILL.md) | Writing, exploit: shape raw material into an article, paragraph by paragraph. | MIT |

### Code quality (`code-quality`) — 10 skills

Index pack: [`pack-code-quality`](skills/pack-code-quality/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`autofix`](skills/autofix/SKILL.md) | Address CodeRabbit pull-request feedback with verified fixes and validation. | MIT |
| [`bash-scripting`](skills/bash-scripting/SKILL.md) | Create, review, and debug Bash or POSIX sh scripts when portability, quoting, failure handling, or shell-specific validation… | MIT |
| [`clean-code-guard`](skills/clean-code-guard/SKILL.md) | Review generated or changed production code with Clean Code, SOLID, DRY, KISS, YAGNI, and LLM-specific failure-mode checks. | MIT |
| [`code-review`](skills/code-review/SKILL.md) | Review code with CodeRabbit when the user requests CodeRabbit or repository policy selects it. | MIT |
| [`code-review-mattpocock`](skills/code-review-mattpocock/SKILL.md) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this… | MIT |
| [`pack-code-quality`](skills/pack-code-quality/SKILL.md) | The review-to-merge loop for a change: run CodeRabbit review, fix its findings with verified patches, decide whether a PR is… | MIT |
| [`pr-readiness`](skills/pr-readiness/SKILL.md) | Validate changes and pull requests through merge readiness, including local gates, Codex review, CI, independent review, manual… | MIT |
| [`quality-playbook`](skills/quality-playbook/SKILL.md) | Run a complete quality engineering audit on any codebase. | Apache-2.0 |
| [`runaway-guard`](skills/runaway-guard/SKILL.md) | Cost-safety discipline for paid AI / inference APIs: treat $-cost as a third complexity dimension alongside time and space. | MIT |
| [`tdd-workflow`](skills/tdd-workflow/SKILL.md) | Test-driven development workflow: write a failing test first, watch it fail, implement the smallest change to green, then… | MIT |

### Linux desktop (`linux-desktop`) — 4 skills

Index pack: [`pack-linux-desktop`](skills/pack-linux-desktop/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`dwm-titus`](skills/dwm-titus/SKILL.md) | Customize the dwm-titus X11 desktop, including TOML keybindings, themes, window rules, panel widgets, autostart, wallpaper,… | MIT |
| [`dwm-titus-debug`](skills/dwm-titus-debug/SKILL.md) | Diagnose broken apps or desktop parts on dwm-titus, including startup, Quickshell panel, keybindings, window rules, autostart,… | MIT |
| [`pack-linux-desktop`](skills/pack-linux-desktop/SKILL.md) | Chris Titus Tech's Fedora/X11 desktop end to end: change dwm keybindings, themes and window rules, build or lint the Quickshell… | MIT |
| [`quickshell`](skills/quickshell/SKILL.md) | Build, lint, and troubleshoot Quickshell QML configurations or source builds. | MIT |

### Sysadmin & ops (`sysadmin-ops`) — 5 skills

Index pack: [`pack-sysadmin-ops`](skills/pack-sysadmin-ops/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`forgejo-maintainer`](skills/forgejo-maintainer/SKILL.md) | Administer Forgejo or Gitea installations, including upgrades, backups, migrations, repository access, and Actions runners. | MIT |
| [`homelab-admin`](skills/homelab-admin/SKILL.md) | Operate homelab infrastructure spanning networking, DNS, storage, NFS, reverse proxies, or multiple services. | MIT |
| [`linux-sysadmin`](skills/linux-sysadmin/SKILL.md) | Diagnose and operate Linux hosts, services, packages, permissions, SELinux, firewalls, and SSH. | MIT |
| [`pack-sysadmin-ops`](skills/pack-sysadmin-ops/SKILL.md) | Infrastructure administration in one pack: Linux host diagnostics (services, packages, SELinux, firewalls, SSH), Podman… | MIT |
| [`podman-operator`](skills/podman-operator/SKILL.md) | Build and operate Podman containers and Quadlet services, including rootless deployment, networking, volumes, systemd… | MIT |

### Media & design (`media-design`) — 24 skills

Index pack: [`pack-media-design`](skills/pack-media-design/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`characteristic-voice`](skills/characteristic-voice/SKILL.md) | Use this skill whenever the user wants speech to sound more human, companion-like, or emotionally expressive. | NOASSERTION |
| [`chat-with-anyone`](skills/chat-with-anyone/SKILL.md) | Chat with any real person or fictional character in their own voice by automatically finding their speech online, extracting a… | NOASSERTION |
| [`daily-news-caster`](skills/daily-news-caster/SKILL.md) | Fetches the latest news using news-aggregator-skill, formats it into a podcast script in Markdown format, and uses the tts skill… | NOASSERTION |
| [`html-visual-card-styles`](skills/html-visual-card-styles/SKILL.md) | HTML card and poster styles — social cards, carousels, posters, motion frames. | Apache-2.0 |
| [`logo-design`](skills/logo-design/SKILL.md) | Professional logo and brand-mark design, from brief to production files. | MIT |
| [`music-video`](skills/music-video/SKILL.md) | Build a music video from an existing song and lyrics, either as p5.js/p5.brush animation or by assembling local images and clips. | NOASSERTION |
| [`pack-media-design`](skills/pack-media-design/SKILL.md) | Cover and image work: design a restrained 16:9 YouTube thumbnail around one readable idea while keeping photographed people… | MIT |
| [`photocraft`](skills/photocraft/SKILL.md) | Create, inspect, edit, composite, and export images through the photocraft-cli MCP server. | MIT |
| [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | Router for all Remotion skills | NOASSERTION |
| [`remotion-captions`](skills/remotion-captions/SKILL.md) | Transcribing, displaying and animating captions | NOASSERTION |
| [`remotion-create`](skills/remotion-create/SKILL.md) | Create a new Remotion video | NOASSERTION |
| [`remotion-docs`](skills/remotion-docs/SKILL.md) | Search Remotion documentation | NOASSERTION |
| [`remotion-interactivity`](skills/remotion-interactivity/SKILL.md) | Structure Remotion markup for interactivity | NOASSERTION |
| [`remotion-maps`](skills/remotion-maps/SKILL.md) | Remotion Map animation knowledge | NOASSERTION |
| [`remotion-markup`](skills/remotion-markup/SKILL.md) | Content, animation and effects best practices | NOASSERTION |
| [`remotion-saas`](skills/remotion-saas/SKILL.md) | Build an app with Remotion | NOASSERTION |
| [`remotion-studio`](skills/remotion-studio/SKILL.md) | When creating or editing a video, start Studio and open its preview as soon as the project can run, before building the… | NOASSERTION |
| [`remotion-upgrade`](skills/remotion-upgrade/SKILL.md) | Upgrade Remotion, and related packages | NOASSERTION |
| [`sound-fx`](skills/sound-fx/SKILL.md) | Use this skill whenever the user wants to generate sound effects, ambient audio, or short audio clips from a text description. | NOASSERTION |
| [`speech-to-text`](skills/speech-to-text/SKILL.md) | Use this skill whenever the user wants to transcribe audio to text, convert speech to text, or get a transcript from an audio or… | NOASSERTION |
| [`text-to-music`](skills/text-to-music/SKILL.md) | Use this skill whenever the user wants to generate a song or music with vocals from a text description and/or lyrics, or cover an… | NOASSERTION |
| [`tts`](skills/tts/SKILL.md) | Use this skill whenever the user wants to convert text into speech, generate audio from text, or produce voiceovers. | NOASSERTION |
| [`video-translation`](skills/video-translation/SKILL.md) | Translate and dub videos from one language to another, replacing the original audio with TTS while keeping the video intact. | NOASSERTION |
| [`youtube-thumbnail`](skills/youtube-thumbnail/SKILL.md) | Create, edit, or review YouTube thumbnails. | MIT |

### Frontend & UI (`frontend-ui`) — 102 skills

Index pack: [`pack-frontend-ui`](skills/pack-frontend-ui/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. | Apache-2.0 |
| [`algorithmic-color-palette`](skills/algorithmic-color-palette/SKILL.md) | Derive a full UI palette from one or two brand colours — state variants, brand-tinted greys, semantic colours. | MIT |
| [`animate`](skills/animate/SKILL.md) | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at… | MIT |
| [`animation-performance`](skills/animation-performance/SKILL.md) | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is… | MIT |
| [`animation-vocabulary`](skills/animation-vocabulary/SKILL.md) | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing… | MIT |
| [`app-shell`](skills/app-shell/SKILL.md) | Top bar, sidebar rail, app launcher, tenant and environment cue, status bar. | MIT |
| [`apple-design`](skills/apple-design/SKILL.md) | Apple's approach to interface design and fluid, physical motion, translated for the web. | MIT |
| [`ask-sonner`](skills/ask-sonner/SKILL.md) | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading… | MIT |
| [`authentic-product-representation`](skills/authentic-product-representation/SKILL.md) | Product visuals must show the real product with real data. | MIT |
| [`banner-design`](skills/banner-design/SKILL.md) | Design banners for social media, ads, website heroes, creative assets, and print. | MIT |
| [`baseline-ui`](skills/baseline-ui/SKILL.md) | Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. | MIT |
| [`brand`](skills/brand/SKILL.md) | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. | MIT |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's… | Apache-2.0 |
| [`brand-visual-language`](skills/brand-visual-language/SKILL.md) | Shape language across type, radius and icons carries brand personality. | MIT |
| [`break-ui`](skills/break-ui/SKILL.md) | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge… | MIT |
| [`buddy-sings`](skills/buddy-sings/SKILL.md) | Turn your Claude Code pet into a singer. | MIT |
| [`button-states`](skills/button-states/SKILL.md) | Rest, hover, active, focus, disabled and loading states, derived from the base colour. | MIT |
| [`canvas-design`](skills/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. | Apache-2.0 |
| [`clone-website`](skills/clone-website/SKILL.md) | Rebuild a live web page 1:1 from measurement into Figma, Penpot or code, then verify it. | MIT |
| [`color-font-skill`](skills/color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. | MIT |
| [`color-mode-and-theme`](skills/color-mode-and-theme/SKILL.md) | Light, dark or both, and when a theme selector is worth it. | MIT |
| [`component-canvas`](skills/component-canvas/SKILL.md) | Build a full-screen, interactive canvas to explore existing UI components and their variants with pan and zoom. | MIT |
| [`component-family-consistency`](skills/component-family-consistency/SKILL.md) | Buttons, inputs, badges and pills share radius, colour logic, shadow, border and spacing. | MIT |
| [`coordinated-data-views`](skills/coordinated-data-views/SKILL.md) | Show a table and its map, diagram, timeline or chart together, with selection synced both ways. | MIT |
| [`create-canvas`](skills/create-canvas/SKILL.md) | Build a freeform canvas to explore, compare, and iterate on anything. | MIT |
| [`create-design-md`](skills/create-design-md/SKILL.md) | Create or update a DESIGN.md from an existing product repository or public website. | MIT |
| [`dashmotion`](skills/dashmotion/SKILL.md) | Create dark-themed, animated technical diagrams as self-contained HTML+SVG files — flowcharts whose connectors visibly flow, and… | MIT |
| [`data-display-and-selection`](skills/data-display-and-selection/SKILL.md) | View modes, row selection, mass actions, sorting, filters, search and table patterns. | MIT |
| [`dembrandt`](skills/dembrandt/SKILL.md) | Orchestrator that routes a UI/UX task through brand, tokens, layout, components, polish and accessibility. | MIT |
| [`design`](skills/design/SKILL.md) | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI… | MIT |
| [`design-style-skill`](skills/design-style-skill/SKILL.md) | 同一套设计可通过调整圆角（rectRadius）和间距呈现4种不同风格。根据场景选择合适的风格配方。 | MIT |
| [`design-system`](skills/design-system/SKILL.md) | Token architecture, component specifications, and slide generation. | MIT |
| [`domain-expert-configuration`](skills/domain-expert-configuration/SKILL.md) | Settings for experts who are not developers — domain language, sane defaults, grouping by professional concept. | MIT |
| [`elevation-and-depth`](skills/elevation-and-depth/SKILL.md) | Shadows and layering that lift elements above the surface. | MIT |
| [`emil-design-eng`](skills/emil-design-eng/SKILL.md) | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that… | MIT |
| [`extract-design`](skills/extract-design/SKILL.md) | Extract colours, typography, spacing, components and W3C design tokens from a live website with Dembrandt. | MIT |
| [`find-animation-opportunities`](skills/find-animation-opportunities/SKILL.md) | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. | MIT |
| [`fixing-accessibility`](skills/fixing-accessibility/SKILL.md) | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form… | MIT |
| [`fixing-metadata`](skills/fixing-metadata/SKILL.md) | 1. Identify pages with missing or incorrect metadata (titles, descriptions, canonical, OG tags) 2. Audit against the priority… | MIT |
| [`fixing-motion-performance`](skills/fixing-motion-performance/SKILL.md) | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur… | MIT |
| [`form-design`](skills/form-design/SKILL.md) | Helper text, placeholders, validation and submit behaviour. | MIT |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | Apache-2.0 |
| [`frontend-dev`](skills/frontend-dev/SKILL.md) | Build complete, production-ready frontend pages by orchestrating 5 specialized capabilities: design engineering, motion systems,… | MIT |
| [`frontend-ui-engineering`](skills/frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. | MIT |
| [`generate-ui-from-brand`](skills/generate-ui-from-brand/SKILL.md) | Pipeline from a URL or DESIGN.md to tokens, decisions and a UI spec. | MIT |
| [`gestalt-ui-organisation`](skills/gestalt-ui-organisation/SKILL.md) | Group controls with Gestalt principles so users see what belongs together. | MIT |
| [`gif-sticker-maker`](skills/gif-sticker-maker/SKILL.md) | Convert user photos into 4 animated GIF stickers (Funko Pop / Pop Mart style). | MIT |
| [`global-toolbar-controls`](skills/global-toolbar-controls/SKILL.md) | Currency, language, region and unit selectors live in a low-profile header or footer spot. | MIT |
| [`hallmark`](skills/hallmark/SKILL.md) | Design skill for websites and new pages that look designed, not generated. | MIT |
| [`html-dashboard-styles`](skills/html-dashboard-styles/SKILL.md) | HTML dashboard styles — KPI boards, analytics and team dashboards. | Apache-2.0 |
| [`html-web-page-styles`](skills/html-web-page-styles/SKILL.md) | HTML web page styles — landing, pricing, docs, wireframe and prototype looks. | Apache-2.0 |
| [`improve-animations`](skills/improve-animations/SKILL.md) | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained… | MIT |
| [`improve-ui`](skills/improve-ui/SKILL.md) | Audit an existing product surface against its own design evidence, identify verified UI problems, and write self-contained… | MIT |
| [`information-architecture`](skills/information-architecture/SKILL.md) | Naming, navigation, a UI that mirrors the data model, confirms for irreversible changes. | MIT |
| [`layout-paradigms-and-consistency`](skills/layout-paradigms-and-consistency/SKILL.md) | Choose a layout paradigm (feed, board, table, canvas, master-detail, dashboard) and reuse it across screens. | MIT |
| [`loading-states-and-perceived-performance`](skills/loading-states-and-perceived-performance/SKILL.md) | Spinners, skeletons and staggered reveals that manage wait times. | MIT |
| [`marketing-vs-product-system`](skills/marketing-vs-product-system/SKILL.md) | A marketing site and its product may differ in density and scale but share one token layer. | MIT |
| [`micro-interactions`](skills/micro-interactions/SKILL.md) | Small purposeful animations — toggles, animated icons, success moments. | MIT |
| [`minimax-music-gen`](skills/minimax-music-gen/SKILL.md) | Generate songs (vocal or instrumental) using the MiniMax Music API. | MIT |
| [`minimax-music-playlist`](skills/minimax-music-playlist/SKILL.md) | Scan the user's music taste, build a taste profile, generate a personalized playlist, and create an album cover. | MIT |
| [`mmx-cli`](skills/mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. | MIT |
| [`mobile-native`](skills/mobile-native/SKILL.md) | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something… | MIT |
| [`modal-and-overlay-patterns`](skills/modal-and-overlay-patterns/SKILL.md) | Modals, drawers, bottom sheets and popovers, each with its scope and blocking level. | MIT |
| [`modular-scale-typography`](skills/modular-scale-typography/SKILL.md) | Ratio-based type scale where every size relates to the others. | MIT |
| [`motion-and-storytelling`](skills/motion-and-storytelling/SKILL.md) | Disney's animation principles and cinematic technique applied to UI motion. | MIT |
| [`nielsen-usability-heuristics`](skills/nielsen-usability-heuristics/SKILL.md) | Nielsen's 10 usability heuristics. | MIT |
| [`notifications-and-recovery`](skills/notifications-and-recovery/SKILL.md) | Toasts, inline errors, banners and recovery paths. | MIT |
| [`operational-expert-tool-ui`](skills/operational-expert-tool-ui/SKILL.md) | Dense, linear, status-at-a-glance UI for specialists who use a tool all day. | MIT |
| [`pack-frontend-ui`](skills/pack-frontend-ui/SKILL.md) | Interface work end to end: React and Next.js performance, composition and view transitions, CSS and layout craft, animation and… | mixed |
| [`performance-and-web-vitals`](skills/performance-and-web-vitals/SKILL.md) | Lighthouse audits and Core Web Vitals — LCP, CLS, INP. | MIT |
| [`pick-ui-library`](skills/pick-ui-library/SKILL.md) | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus,… | MIT |
| [`pr-review`](skills/pr-review/SKILL.md) | Review pull requests against repository standards. | MIT |
| [`real-world-metaphors`](skills/real-world-metaphors/SKILL.md) | Cards, drawers, carousels and other patterns borrowed from the physical world. | MIT |
| [`remove-animations`](skills/remove-animations/SKILL.md) | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional… | MIT |
| [`repeated-component-alignment`](skills/repeated-component-alignment/SKILL.md) | Cards, rows, tiles and cells are fixed slot models that stay aligned when content length varies. | MIT |
| [`responsive-paradigms`](skills/responsive-paradigms/SKILL.md) | Mobile, tablet and desktop are different paradigms, not one layout scaled. | MIT |
| [`review-animations`](skills/review-animations/SKILL.md) | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. | MIT |
| [`scroll-areas`](skills/scroll-areas/SKILL.md) | Avoid inner scroll containers; when unavoidable, one axis at a time. | MIT |
| [`semantic-html-and-seo`](skills/semantic-html-and-seo/SKILL.md) | Semantic HTML5, SEO basics, alt text, progressive enhancement and SPA concerns. | MIT |
| [`shader-dev`](skills/shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid simulation,… | MIT |
| [`sizing-units`](skills/sizing-units/SKILL.md) | rem, px or relative units for each kind of value. | MIT |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. | Apache-2.0 |
| [`slides`](skills/slides/SKILL.md) | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide… | MIT |
| [`status-colors-and-errors`](skills/status-colors-and-errors/SKILL.md) | Few semantic colours, each meaning one thing, and errors with a way forward. | MIT |
| [`sticky-and-fixed-elements`](skills/sticky-and-fixed-elements/SKILL.md) | Sticky headers, bottom toolbars, floating action buttons and pinned table headers. | MIT |
| [`surface-separation`](skills/surface-separation/SKILL.md) | Set a surface apart by one means — border, elevation or fill — and keep opacity for state. | MIT |
| [`tab-navigation`](skills/tab-navigation/SKILL.md) | Tabs swap views under a shared context. | MIT |
| [`theme-factory`](skills/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. | Apache-2.0 |
| [`ui-context-and-scope`](skills/ui-context-and-scope/SKILL.md) | Show where the user is and what their actions affect — breadcrumbs, regions, scope labels. | MIT |
| [`ui-density`](skills/ui-density/SKILL.md) | Match information density to platform and user type. | MIT |
| [`ui-skills-root`](skills/ui-skills-root/SKILL.md) | Use before UI-related work to select the smallest useful UI Skills context through the ui-skills CLI. | MIT |
| [`ui-styling`](skills/ui-styling/SKILL.md) | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first… | Apache-2.0 |
| [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | UI/UX design intelligence for web, mobile, and desktop. | MIT |
| [`user-flows-and-guided-paths`](skills/user-flows-and-guided-paths/SKILL.md) | Guided multi-step paths and wizards. | MIT |
| [`vercel-composition-patterns`](skills/vercel-composition-patterns/SKILL.md) | Composition patterns for building flexible, maintainable React components. | NOASSERTION |
| [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. | NOASSERTION |
| [`vercel-react-view-transitions`](skills/vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component,… | NOASSERTION |
| [`vision-analysis`](skills/vision-analysis/SKILL.md) | Analyze images using the MiniMax MiniMaxunderstandimage MCP tool available in the MiniMax Token Plan. | MIT |
| [`visual-emphasis-and-hierarchy`](skills/visual-emphasis-and-hierarchy/SKILL.md) | Size, colour, weight and position mark what matters most. | MIT |
| [`wcag-accessibility`](skills/wcag-accessibility/SKILL.md) | WCAG 2.2 AA compliance as required by the European Accessibility Act. | MIT |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React,… | Apache-2.0 |
| [`write-swift`](skills/write-swift/SKILL.md) | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent,… | MIT |

### Backend & services (`backend-services`) — 16 skills

Index pack: [`pack-backend-services`](skills/pack-backend-services/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`360-feedback-system`](skills/360-feedback-system/SKILL.md) | 360 feedback register: reviewer, subject, review cycle, visibility, due date and score, as CSV, SQL, JSON Schema or Notion on… | MIT |
| [`accounting-software-selection`](skills/accounting-software-selection/SKILL.md) | Scores shortlisted accounting packages against 57 evidence-backed fields, emitted as CSV, SQL, JSON Schema or Notion on request. | MIT |
| [`api-and-interface-design`](skills/api-and-interface-design/SKILL.md) | Guides stable API and interface design. | MIT |
| [`claude-api`](skills/claude-api/SKILL.md) | This skill helps you build LLM-powered applications with Claude. | Apache-2.0 |
| [`fastify-best-practices`](skills/fastify-best-practices/SKILL.md) | Guides development of Fastify Node.js backend servers and REST APIs using TypeScript or JavaScript. | MIT |
| [`fullstack-dev`](skills/fullstack-dev/SKILL.md) | When this skill is triggered, you MUST follow this workflow before writing any code. | MIT |
| [`hunt-graphql`](skills/hunt-graphql/SKILL.md) | Hunting skill for graphql vulnerabilities. | MIT |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through… | Apache-2.0 |
| [`node`](skills/node/SKILL.md) | Provides domain-specific best practices for Node.js development with TypeScript, covering type stripping, async patterns, error… | MIT |
| [`nodejs-core`](skills/nodejs-core/SKILL.md) | Contributes to and debugs Node.js core, including nodejs/node commit and PR tone, contribution workflows, native crashes, V8… | MIT |
| [`oauth`](skills/oauth/SKILL.md) | Implements OAuth 2.0/2.1 authorization flows in Fastify applications — configures authorization code with PKCE, client… | MIT |
| [`pack-backend-services`](skills/pack-backend-services/SKILL.md) | Server-side work: Node.js and TypeScript practice, Fastify REST APIs, OAuth 2.0/2.1 flows, advanced type design, API and module… | mixed |
| [`rails-conventions`](skills/rails-conventions/SKILL.md) | Modern Ruby and Rails application architecture, implementation, and review guidance for production codebases. | MIT |
| [`snipgrapher`](skills/snipgrapher/SKILL.md) | Configures and uses snipgrapher to generate polished code snippet images, including syntax-highlighted PNGs, SVGs, and WebP… | MIT |
| [`tinystruct-patterns`](skills/tinystruct-patterns/SKILL.md) | Expert guidance for developing with the tinystruct Java framework. | MIT |
| [`typescript-magician`](skills/typescript-magician/SKILL.md) | Designs complex generic types, refactors `any` types to strict alternatives, creates type guards and utility types, and resolves… | MIT |

### Testing & QA (`testing-qa`) — 85 skills

Index pack: [`pack-testing-qa`](skills/pack-testing-qa/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`accessibility-skill`](skills/accessibility-skill/SKILL.md) | Accessibility testing on TestMu AI is layered onto an existing automation suite. | MIT |
| [`api-ai-augmented`](skills/api-ai-augmented/SKILL.md) | Design LLM tool definitions, agentic workflows, and natural language API interfaces. | MIT |
| [`api-analyzer`](skills/api-analyzer/SKILL.md) | Validates whether an API request is correct based on provided inputs (method, URL, headers, body, auth, query params). | MIT |
| [`api-compliance-checker`](skills/api-compliance-checker/SKILL.md) | Design compliant API patterns for GDPR, PCI-DSS, HIPAA, SOC2, and other regulatory frameworks. | MIT |
| [`api-designer`](skills/api-designer/SKILL.md) | Ask the user if they want just the endpoints or complete detailed response (Enpoints Only/Detail Design). | MIT |
| [`api-documentation`](skills/api-documentation/SKILL.md) | Generate clear, complete, professional API documentation from any form of API input. | MIT |
| [`api-fetcher-specific-domains`](skills/api-fetcher-specific-domains/SKILL.md) | Provide real-world API patterns and examples from well-known domains and platforms. | MIT |
| [`api-graphql-grpc`](skills/api-graphql-grpc/SKILL.md) | Design schemas, resolvers, and service definitions for GraphQL and gRPC APIs. | MIT |
| [`api-health-monitoring`](skills/api-health-monitoring/SKILL.md) | Design complete observability stacks for any API: health checks, metrics, alerting, and dashboards. | MIT |
| [`api-inferrer-from-files`](skills/api-inferrer-from-files/SKILL.md) | Infer and list REST API endpoints from file names or project directory structures. | MIT |
| [`api-integration`](skills/api-integration/SKILL.md) | Design integration patterns, webhook flows, event pipelines, and API composition strategies. | MIT |
| [`api-mock-helper`](skills/api-mock-helper/SKILL.md) | Generate mock servers, stubs, fixtures, and sandbox environments for any API. | MIT |
| [`api-rate-limiting-helper`](skills/api-rate-limiting-helper/SKILL.md) | Design complete rate limiting, quota, and retry systems for any API. | MIT |
| [`api-sdk-generator`](skills/api-sdk-generator/SKILL.md) | Generate production-quality client libraries and SDK code for any API in any language. | MIT |
| [`api-security-auth-pattern`](skills/api-security-auth-pattern/SKILL.md) | Design complete authentication and security layers for any API. | MIT |
| [`api-to-testcase-generator`](skills/api-to-testcase-generator/SKILL.md) | Converts API definitions into production-ready test suites covering happy paths, edge cases, error handling, and boundary… | MIT |
| [`api-versioning-helper`](skills/api-versioning-helper/SKILL.md) | Design sustainable versioning strategies and manage API evolution without breaking clients. | MIT |
| [`appium-skill`](skills/appium-skill/SKILL.md) | You are a senior mobile QA architect. | MIT |
| [`behat-skill`](skills/behat-skill/SKILL.md) | gherkin Feature: User Login As a user I want to log in | MIT |
| [`behave-skill`](skills/behave-skill/SKILL.md) | gherkin Feature: User Login As a registered user I want to log into the application | MIT |
| [`browser-testing-with-devtools`](skills/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. | MIT |
| [`capybara-skill`](skills/capybara-skill/SKILL.md) | RSpec.describe 'Login', type: :feature do it 'logs in with valid credentials' do visit '/login' fillin 'Email', with:… | MIT |
| [`cicd-pipeline-skill`](skills/cicd-pipeline-skill/SKILL.md) | yaml name: Test Automation on: push: branches: main, develop pullrequest: branches: main | MIT |
| [`codeception-skill`](skills/codeception-skill/SKILL.md) | php <?php // tests/Acceptance/LoginCest.php | MIT |
| [`cucumber-skill`](skills/cucumber-skill/SKILL.md) | gherkin Feature: User Login As a registered user I want to log into the application So that I can access my dashboard | MIT |
| [`cypress-skill`](skills/cypress-skill/SKILL.md) | You are a senior QA automation architect specializing in Cypress. | MIT |
| [`detox-skill`](skills/detox-skill/SKILL.md) | You are a senior React Native QA engineer specializing in Detox. | MIT |
| [`espresso-skill`](skills/espresso-skill/SKILL.md) | You are a senior Android QA engineer specializing in Espresso UI testing. | MIT |
| [`flutter-testing-skill`](skills/flutter-testing-skill/SKILL.md) | You are a senior Flutter developer specializing in testing. | MIT |
| [`gauge-skill`](skills/gauge-skill/SKILL.md) | Login as <email with <password Verify <expected page is shown | MIT |
| [`geb-skill`](skills/geb-skill/SKILL.md) | For TestMu AI cloud execution, see reference/cloud-integration.md(reference/cloud-integration.md) and… | MIT |
| [`hyperexecute-skill`](skills/hyperexecute-skill/SKILL.md) | 1. Locate the HyperExecute CLI. If missing, ask before downloading it unless the user explicitly approved an autonomous… | MIT |
| [`jasmine-skill`](skills/jasmine-skill/SKILL.md) | javascript describe('Calculator', () = { let calc; | MIT |
| [`jest-skill`](skills/jest-skill/SKILL.md) | javascript describe('Calculator', () = { let calc; beforeEach(() = { calc = new Calculator(); }); | MIT |
| [`junit-5-skill`](skills/junit-5-skill/SKILL.md) | You are a senior Java developer specializing in JUnit 5 testing. | MIT |
| [`kanecli-skill`](skills/kanecli-skill/SKILL.md) | Browser automation + AI test authoring via kane-cli - run browser objectives, generate & refine test scenarios/cases from a… | MIT |
| [`karma-skill`](skills/karma-skill/SKILL.md) | javascript module.exports = function(config) { config.set({ basePath: '', frameworks: 'jasmine', files: 'src//.js',… | MIT |
| [`laravel-dusk-skill`](skills/laravel-dusk-skill/SKILL.md) | For TestMu AI cloud execution, see reference/cloud-integration.md(reference/cloud-integration.md) and… | MIT |
| [`lettuce-skill`](skills/lettuce-skill/SKILL.md) | Note: Lettuce is largely unmaintained. | MIT |
| [`mocha-skill`](skills/mocha-skill/SKILL.md) | javascript const { expect } = require('chai'); | MIT |
| [`mstest-skill`](skills/mstest-skill/SKILL.md) | csharp using Microsoft.VisualStudio.TestTools.UnitTesting; | MIT |
| [`nemojs-skill`](skills/nemojs-skill/SKILL.md) | PayPal's Selenium-based test automation framework for Node.js. | MIT |
| [`newman-cicd-integration`](skills/newman-cicd-integration/SKILL.md) | Generate ready-to-use CI/CD pipeline configurations that install and run Newman for automated API testing. | MIT |
| [`newman-report-analyzer`](skills/newman-report-analyzer/SKILL.md) | Analyze Newman test run output, JSON reports, and JUnit XML results to summarize failures, diagnose root causes, identify slow… | MIT |
| [`newman-script-helper`](skills/newman-script-helper/SKILL.md) | Generate Newman CLI run commands with the correct flags, options, and configurations. | MIT |
| [`nightwatchjs-skill`](skills/nightwatchjs-skill/SKILL.md) | ├─ "cloud", "TestMu", "LambdaTest" → Cloud: nightwatch.conf.js with LT env ├─ "local" → Local: ChromeDriver/GeckoDriver └─… | MIT |
| [`nunit-skill`](skills/nunit-skill/SKILL.md) | TestFixture public class CalculatorTests { private Calculator calculator; | MIT |
| [`openapi-spec-generator`](skills/openapi-spec-generator/SKILL.md) | Generate complete, valid OpenAPI 3.x or Swagger 2.0 specifications from descriptions, code, or partial specs. | MIT |
| [`pack-testing-qa`](skills/pack-testing-qa/SKILL.md) | Test work in one place: Playwright patterns for E2E, component and API tests, page objects, CI wiring and Cypress/Selenium… | mixed |
| [`phpunit-skill`](skills/phpunit-skill/SKILL.md) | php <?php use PHPUnit\Framework\TestCase; | MIT |
| [`playwright-ci`](skills/playwright-ci/SKILL.md) | Production-ready CI/CD configurations for Playwright — GitHub Actions, GitLab CI, CircleCI, Azure DevOps, Jenkins, Docker,… | MIT |
| [`playwright-cli`](skills/playwright-cli/SKILL.md) | Automates browser interactions for testing and validating your own web applications using playwright-cli. | MIT |
| [`playwright-frontend`](skills/playwright-frontend/SKILL.md) | For frontend engineers authoring UI — how to make components reliably locatable by tests and AI agents. | MIT |
| [`playwright-migration`](skills/playwright-migration/SKILL.md) | Step-by-step migration guides for moving to Playwright from Cypress or Selenium/WebDriver — command mappings, architecture… | MIT |
| [`playwright-pom`](skills/playwright-pom/SKILL.md) | Page Object Model patterns for Playwright — when to use POM, how to structure page objects, and when fixtures or helpers are a… | MIT |
| [`playwright-qa`](skills/playwright-qa/SKILL.md) | QA engineering workflows on top of Playwright. | MIT |
| [`playwright-skill`](skills/playwright-skill/SKILL.md) | Current Playwright (1.64) patterns for writing, debugging, and scaling reliable test suites. | MIT |
| [`postman-collection-generator`](skills/postman-collection-generator/SKILL.md) | Generates a valid, import-ready Postman Collection v2.1 JSON from: - Natural language API descriptions - cURL commands (one or… | MIT |
| [`postman-newman-automation`](skills/postman-newman-automation/SKILL.md) | Generates Newman CLI commands, shell scripts, and Jenkins pipeline configs for running Postman collections in automated… | MIT |
| [`postman-openapi-converter`](skills/postman-openapi-converter/SKILL.md) | Converts OpenAPI 3.x or Swagger 2.0 specs into a valid Postman Collection v2.1. | MIT |
| [`postman-test-script-generator`](skills/postman-test-script-generator/SKILL.md) | Writes and embeds Postman JavaScript test scripts — both prerequest and test scripts — into collection requests. | MIT |
| [`protractor-skill`](skills/protractor-skill/SKILL.md) | Protractor reached end-of-life in 2023. | MIT |
| [`puppeteer-skill`](skills/puppeteer-skill/SKILL.md) | javascript const puppeteer = require('puppeteer'); | MIT |
| [`pytest-skill`](skills/pytest-skill/SKILL.md) | def testexception(): with pytest.raises(ValueError, match="invalid"): int("notanumber") | MIT |
| [`reqnroll-skill`](skills/reqnroll-skill/SKILL.md) | This skill guides QA engineers and test architects in writing production-grade Reqnroll BDD tests for web and mobile automation… | MIT |
| [`robot-framework-skill`](skills/robot-framework-skill/SKILL.md) | For TestMu AI cloud execution, see reference/cloud-integration.md(reference/cloud-integration.md) and… | MIT |
| [`rook-skill`](skills/rook-skill/SKILL.md) | Use rook to test, evaluate, red-team or regression-check an AI agent the user owns, or to interpret saved Rook results. | MIT |
| [`rspec-skill`](skills/rspec-skill/SKILL.md) | ruby RSpec.describe Calculator do subject(:calculator) { describedclass.new } | MIT |
| [`selenide-skill`](skills/selenide-skill/SKILL.md) | java import com.codeborne.selenide.; import static com.codeborne.selenide.Selenide.; import static… | MIT |
| [`selenium-skill`](skills/selenium-skill/SKILL.md) | You are a senior QA automation architect. | MIT |
| [`serenity-bdd-skill`](skills/serenity-bdd-skill/SKILL.md) | java import net.serenitybdd.annotations.Step; import net.serenitybdd.core.pages.PageObject; | MIT |
| [`smartui-skill`](skills/smartui-skill/SKILL.md) | javascript const { chromium } = require('playwright'); const { smartuiSnapshot } = require('@lambdatest/smartui-cli'); | MIT |
| [`specflow-skill`](skills/specflow-skill/SKILL.md) | Scenario: Successful login Given I am on the login page When I enter "user@test.com" as email And I enter "password123" as… | MIT |
| [`tdd`](skills/tdd/SKILL.md) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or… | MIT |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. | MIT |
| [`test-framework-migration-skill`](skills/test-framework-migration-skill/SKILL.md) | You are a senior QA automation architect. | MIT |
| [`testcafe-skill`](skills/testcafe-skill/SKILL.md) | javascript import { Selector } from 'testcafe'; | MIT |
| [`testng-skill`](skills/testng-skill/SKILL.md) | java import org.testng.annotations.; import org.testng.Assert; | MIT |
| [`testunit-skill`](skills/testunit-skill/SKILL.md) | class TestCalculator < Test::Unit::TestCase def setup @calc = Calculator.new end | MIT |
| [`unittest-skill`](skills/unittest-skill/SKILL.md) | class TestCalculator(unittest.TestCase): def setUp(self): self.calc = Calculator() | MIT |
| [`vitest-skill`](skills/vitest-skill/SKILL.md) | typescript import { describe, it, expect, vi, beforeEach } from 'vitest'; import { Calculator } from './calculator'; | MIT |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. | Apache-2.0 |
| [`webdriverio-skill`](skills/webdriverio-skill/SKILL.md) | Default local. If mentions "cloud", "TestMu", "LambdaTest" → cloud via WDIO LambdaTest service. | MIT |
| [`xcuitest-skill`](skills/xcuitest-skill/SKILL.md) | You are a senior iOS QA engineer specializing in XCUITest. | MIT |
| [`xunit-skill`](skills/xunit-skill/SKILL.md) | public class CalculatorTests { private readonly Calculator calc = new(); | MIT |

### Security & audit (`security-audit`) — 25 skills

Index pack: [`pack-security-audit`](skills/pack-security-audit/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`anti-entropy-governance`](skills/anti-entropy-governance/SKILL.md) | Use when touching retiring old logic, collapsing duplicate owners, removing fallbacks, or schema/persistence/source-of-truth… | MIT |
| [`communicating-concisely`](skills/communicating-concisely/SKILL.md) | Use when the user asks for caveman mode, fewer tokens, brief responses, compressed communication, or otherwise explicitly… | MIT |
| [`constraint-driven-development`](skills/constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. | MIT |
| [`doubt-driven-development`](skills/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. | MIT |
| [`establishing-project-context`](skills/establishing-project-context/SKILL.md) | Use when the user asks to establish shared project language, or project work exposes a conflicting, renamed, or deprecated domain… | MIT |
| [`first-principles-review`](skills/first-principles-review/SKILL.md) | Use when asked for first-principles or Occam's-razor review, or when high-risk decisions involve competing constraints, fallback… | MIT |
| [`flutter-dart-code-review`](skills/flutter-dart-code-review/SKILL.md) | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod,… | MIT |
| [`git-guardrails-claude-code`](skills/git-guardrails-claude-code/SKILL.md) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. | MIT |
| [`goal-framing`](skills/goal-framing/SKILL.md) | Use when the user explicitly sets an Aegis goal with /aegis-goal, Aegis goal:, or asks to define goal, success evidence, stop… | MIT |
| [`laravel-security`](skills/laravel-security/SKILL.md) | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure… | MIT |
| [`long-task-continuation`](skills/long-task-continuation/SKILL.md) | Use when a task is multi-step, may span context resets or sessions, uses subagents, or risks losing state before completion. | MIT |
| [`mle-workflow`](skills/mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment,… | MIT |
| [`pack-security-audit`](skills/pack-security-audit/SKILL.md) | Security review of code, APIs, services, CLIs and libraries: vulnerability classes to look for, hardening an input handler,… | mixed |
| [`recording-architecture-decisions`](skills/recording-architecture-decisions/SKILL.md) | Use when the user asks to create, write, update, amend, supersede, or evaluate an ADR, architecture decision record, durable… | MIT |
| [`requesting-code-review`](skills/requesting-code-review/SKILL.md) | Use when requesting independent code review, after implementation slices, before merging high-risk work, or when verification… | MIT |
| [`security-and-hardening`](skills/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. | MIT |
| [`security-audit`](skills/security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. | MIT |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Use when encountering a bug, test failure, or unexpected behavior, before proposing fixes | MIT |
| [`ui-ux-governance`](skills/ui-ux-governance/SKILL.md) | Use when designing, changing, or reviewing user-facing interfaces or interaction flows, including API changes that alter visible… | MIT |
| [`update-aegis`](skills/update-aegis/SKILL.md) | Use when the user says `aegis:update`, asks to update or upgrade an installed Aegis method-pack, wants the latest Aegis version,… | MIT |
| [`using-aegis`](skills/using-aegis/SKILL.md) | Use when starting a turn or checking Aegis skill routing. | MIT |
| [`varlock`](skills/varlock/SKILL.md) | Secure environment variable management with Varlock. | MIT |
| [`verification-before-completion`](skills/verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, passing, verified, release-ready, or ready to commit, merge, publish, or hand… | MIT |
| [`writing-plans`](skills/writing-plans/SKILL.md) | Use when you have an approved spec or written requirements for a multi-step task that needs a durable plan document before… | MIT |
| [`zeroize-audit`](skills/zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with… | MIT |

### Cloud & deploy (`cloud-and-deploy`) — 195 skills

Index pack: [`pack-cloud-and-deploy`](skills/pack-cloud-and-deploy/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`agent-platform-alert-configuration`](skills/agent-platform-alert-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`agent-platform-deploy`](skills/agent-platform-deploy/SKILL.md) | This skill provides instructions for deploying Open Models from Agent Platform Model Garden to endpoints, and subsequently… | Apache-2.0 |
| [`agent-platform-endpoint-management`](skills/agent-platform-endpoint-management/SKILL.md) | This skill provides procedural knowledge for managing Agent Platform Endpoints. | Apache-2.0 |
| [`agent-platform-eval-flywheel`](skills/agent-platform-eval-flywheel/SKILL.md) | Help users evaluate and iteratively improve GenAI models and agents using the Agent Platform GenAI Evaluation SDK (google.genai /… | Apache-2.0 |
| [`agent-platform-inference`](skills/agent-platform-inference/SKILL.md) | This skill provides instructions for authenticating and connecting to Google Cloud Agent Platform to use Generative AI models. | Apache-2.0 |
| [`agent-platform-migrate-from-ai-studio`](skills/agent-platform-migrate-from-ai-studio/SKILL.md) | Use this skill when you need to transition an application from the developer-centric Google AI Studio ecosystem… | Apache-2.0 |
| [`agent-platform-model-registry`](skills/agent-platform-model-registry/SKILL.md) | This skill provides instructions for managing machine learning models in the Agent Platform Model Registry. | Apache-2.0 |
| [`agent-platform-prompt-management`](skills/agent-platform-prompt-management/SKILL.md) | 1. Execute Operations via Python: Run the Python snippets below using runcommand in the execution environment to manage prompts… | Apache-2.0 |
| [`agent-platform-rag-engine-management`](skills/agent-platform-rag-engine-management/SKILL.md) | This skill provides instructions on how to interact with Agent Platform RAG Engine using the Agent Platform Python SDK. | Apache-2.0 |
| [`agent-platform-skill-registry`](skills/agent-platform-skill-registry/SKILL.md) | This skill provides instructions for interacting with the Skill Registry on the Gemini Enterprise Agent Platform. | Apache-2.0 |
| [`agent-platform-troubleshooting`](skills/agent-platform-troubleshooting/SKILL.md) | !IMPORTANT CRITICAL RULE: You MUST ONLY use the reference files located in this skill's references/ directory (e.g.,… | Apache-2.0 |
| [`agent-platform-tuning`](skills/agent-platform-tuning/SKILL.md) | This skill provides procedural knowledge for fine-tuning Large Language Models (both Open Models and Gemini Models) using Agent… | Apache-2.0 |
| [`agent-platform-tuning-management`](skills/agent-platform-tuning-management/SKILL.md) | This skill provides instructions on how to manage GenAI Tuning Jobs using the Agent Platform Python SDK. | Apache-2.0 |
| [`alloydb-basics`](skills/alloydb-basics/SKILL.md) | AlloyDB for PostgreSQL is a managed, PostgreSQL-compatible database service designed for enterprise-grade performance and… | Apache-2.0 |
| [`api-gateway-backend-security-and-rate-limiting`](skills/api-gateway-backend-security-and-rate-limiting/SKILL.md) | This skill configures client authentication, gateway-to-backend authentication, and per-project rate limits (quotas) for Google… | Apache-2.0 |
| [`api-gateway-mcp-server`](skills/api-gateway-mcp-server/SKILL.md) | This skill converts new or existing REST APIs on Google Cloud API Gateway into remote Model Context Protocol (MCP) servers (POST… | Apache-2.0 |
| [`apigee-agent-gateway-governance`](skills/apigee-agent-gateway-governance/SKILL.md) | Wires an Apigee proxy in as an ext-proc callout on a GCP Agent Gateway. | Apache-2.0 |
| [`application-design-center-design-deploy`](skills/application-design-center-design-deploy/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`application-integration-authoring`](skills/application-integration-authoring/SKILL.md) | Google Cloud Application Integration workflows are authored, versioned, published, and executed programmatically through the REST… | Apache-2.0 |
| [`application-integration-basics`](skills/application-integration-basics/SKILL.md) | Application Integration is Google Cloud's serverless, auto-scaling Integration-Platform-as-a-Service (iPaaS) for connecting… | Apache-2.0 |
| [`application-integration-troubleshooting`](skills/application-integration-troubleshooting/SKILL.md) | Diagnose and recover Google Cloud Application Integration executions that fail, stall, or appear to do nothing. | Apache-2.0 |
| [`assured-workloads-basics`](skills/assured-workloads-basics/SKILL.md) | Validate prerequisites, create Assured Workloads V1 compliant folders, allowlist compliant services, and list, inspect, update,… | Apache-2.0 |
| [`assuredworkloads-environment-assessor`](skills/assuredworkloads-environment-assessor/SKILL.md) | This skill performs zero-risk, non-mutating compliance discovery, physical telemetry profiling, and data boundary framework… | Apache-2.0 |
| [`assuredworkloads-frameworks-author`](skills/assuredworkloads-frameworks-author/SKILL.md) | You are an authoritative Data Boundary Compliance Architect / Author. | Apache-2.0 |
| [`assuredworkloads-frameworks-navigator`](skills/assuredworkloads-frameworks-navigator/SKILL.md) | You are a Compliance Analyst specializing in Google Cloud Data Boundary Frameworks and cloud controls. | Apache-2.0 |
| [`bigquery-ai-ml`](skills/bigquery-ai-ml/SKILL.md) | BigQuery integrates with Vertex AI to provide powerful machine learning and generative AI capabilities directly within SQL… | Apache-2.0 |
| [`bigquery-basics`](skills/bigquery-basics/SKILL.md) | BigQuery is a serverless, AI-ready data platform that enables high-speed analysis of large datasets using SQL and Python. | Apache-2.0 |
| [`bigquery-bigframes`](skills/bigquery-bigframes/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`bigquery-migration-sql-translator`](skills/bigquery-migration-sql-translator/SKILL.md) | The BigQuery Migration Service (BQMS) translates legacy database SQL scripts, queries, and schemas into GoogleSQL. | Apache-2.0 |
| [`bigquery-observability`](skills/bigquery-observability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`bigquery-optimization`](skills/bigquery-optimization/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`bigquery-troubleshooting`](skills/bigquery-troubleshooting/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`bigquery-udfs`](skills/bigquery-udfs/SKILL.md) | BigQuery User-Defined Functions (UDFs) extend GoogleSQL with custom logic written in SQL, JavaScript, managed Python… | Apache-2.0 |
| [`bigtable-basics`](skills/bigtable-basics/SKILL.md) | This skill provides core workflows and guidance for administering and developing with Google Bigtable. | Apache-2.0 |
| [`ci-cd-and-automation`](skills/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. | MIT |
| [`cloud-armor-crs-rule-upgrader`](skills/cloud-armor-crs-rule-upgrader/SKILL.md) | This skill guides Network Security Agents and Google Cloud practitioners through auditing, assessing, and upgrading Google Cloud… | Apache-2.0 |
| [`cloud-build-basics`](skills/cloud-build-basics/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`cloud-databases-onboarding`](skills/cloud-databases-onboarding/SKILL.md) | This skill provides domain instructions, decision matrices, and Infrastructure-as-Code workflows to guide users through… | Apache-2.0 |
| [`cloud-logging-configuration-basics`](skills/cloud-logging-configuration-basics/SKILL.md) | Use this skill to configure Cloud Logging resources such as log buckets, log views, or log sinks. | Apache-2.0 |
| [`cloud-logging-cross-project-configuration`](skills/cloud-logging-cross-project-configuration/SKILL.md) | This skill describes how to use gcloud commands to configure Cloud Logging so that you store log data in a central location,… | Apache-2.0 |
| [`cloud-logging-finops`](skills/cloud-logging-finops/SKILL.md) | Non-interactive runs. When no user can answer (e.g. a scheduled or automated run), ask nothing: audit the project named in the… | Apache-2.0 |
| [`cloud-logging-query-generation`](skills/cloud-logging-query-generation/SKILL.md) | Use this skill to generate correct Logging Query Language (LQL) queries for Cloud Logging. | Apache-2.0 |
| [`cloud-monitoring-chart-generation`](skills/cloud-monitoring-chart-generation/SKILL.md) | Transforms PromQL or ListTimeSeries JSON request payloads and metric metadata into valid Server-Driven UI (SDUI)… | Apache-2.0 |
| [`cloud-monitoring-list-time-series-request`](skills/cloud-monitoring-list-time-series-request/SKILL.md) | Use this skill to translate any Cloud Monitoring metric descriptor into valid, production-ready ListTimeSeries REST API query… | Apache-2.0 |
| [`cloud-monitoring-metric-selection`](skills/cloud-monitoring-metric-selection/SKILL.md) | Use this skill to identify the most relevant Cloud Monitoring metric descriptors. | Apache-2.0 |
| [`cloud-monitoring-notification-channels-configuration`](skills/cloud-monitoring-notification-channels-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`cloud-monitoring-promql-query`](skills/cloud-monitoring-promql-query/SKILL.md) | Use this skill to generate a valid PromQL query from any Cloud Monitoring metric type. | Apache-2.0 |
| [`cloud-network-insights`](skills/cloud-network-insights/SKILL.md) | For all gcloud CLI, REST API, and MCP attribution requirements when executing commands with this skill, follow the instructions… | Apache-2.0 |
| [`cloud-run-alert-configuration`](skills/cloud-run-alert-configuration/SKILL.md) | Production-grade observability for Cloud Run using Terraform and PromQL (Cloud Monitoring). | Apache-2.0 |
| [`cloud-run-basics`](skills/cloud-run-basics/SKILL.md) | Cloud Run is a fully managed application platform for running your code, function, or container on top of Google's highly… | Apache-2.0 |
| [`cloud-sql-basics`](skills/cloud-sql-basics/SKILL.md) | Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server. | Apache-2.0 |
| [`cloud-trace-querying`](skills/cloud-trace-querying/SKILL.md) | This skill equips the agent to interact with Cloud Trace by providing standard query patterns, diagnostic workflows for latency… | Apache-2.0 |
| [`data-manager-api-audience-ingestion`](skills/data-manager-api-audience-ingestion/SKILL.md) | - Authentication & Library Installation: If you need to set up access to the Data Manager API or install the client and utility… | Apache-2.0 |
| [`data-manager-api-event-ingestion`](skills/data-manager-api-event-ingestion/SKILL.md) | - Authentication & Library Installation: If you need to set up access to the Data Manager API or install the client and utility… | Apache-2.0 |
| [`data-manager-api-setup`](skills/data-manager-api-setup/SKILL.md) | Refer to Set up API access(https://developers.google.com/data-manager/api/devguides/quickstart/set-up-access.md.txt) for more… | Apache-2.0 |
| [`datalineage-bigquery-asset-impact-analysis`](skills/datalineage-bigquery-asset-impact-analysis/SKILL.md) | This skill guides the agent in performing a downstream impact analysis (blast radius assessment) when a BigQuery table or view is… | Apache-2.0 |
| [`datalineage-summary`](skills/datalineage-summary/SKILL.md) | This skill guides the agent in investigating and summarizing the Data Lineage graph for a specific focal asset (Table-Level… | Apache-2.0 |
| [`dbt-sf-to-bq-translator`](skills/dbt-sf-to-bq-translator/SKILL.md) | You are responsible for: 1. | Apache-2.0 |
| [`deploy-to-vercel`](skills/deploy-to-vercel/SKILL.md) | Deploy applications and websites to Vercel. | NOASSERTION |
| [`detection-engineering-coverage-evaluation`](skills/detection-engineering-coverage-evaluation/SKILL.md) | Routing Note: To author, test (Retrohunt), or tune YARA-L 2.0 detection rules directly, open… | Apache-2.0 |
| [`developer-device-platform-basics`](skills/developer-device-platform-basics/SKILL.md) | Developer Device Platform (DDP) is a Google fully managed, global infrastructure providing access to a wide variety of physical… | Apache-2.0 |
| [`developing-genkit-go`](skills/developing-genkit-go/SKILL.md) | Develop AI-powered applications using Genkit in Go. | Apache-2.0 |
| [`developing-genkit-js`](skills/developing-genkit-js/SKILL.md) | Develop AI-powered applications using Genkit in Node.js/TypeScript. | Apache-2.0 |
| [`developing-genkit-python`](skills/developing-genkit-python/SKILL.md) | Develop AI-powered applications using Genkit in Python. | Apache-2.0 |
| [`dpop-adoption`](skills/dpop-adoption/SKILL.md) | Demonstrating Proof-of-Possession (DPoP, RFC 9449) secures OAuth 2.0 refresh tokens against interception and replay attacks by… | Apache-2.0 |
| [`finding-google-skills`](skills/finding-google-skills/SKILL.md) | Routes a request to the published Google skills that apply to it. | Apache-2.0 |
| [`firebase-basics`](skills/firebase-basics/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`gcloud`](skills/gcloud/SKILL.md) | !CAUTION ### MANDATORY PRE-CONDITION: EXPLICIT LEAF-LEVEL SYNTAX VALIDATION All pre-existing knowledge of gcloud commands, flags,… | Apache-2.0 |
| [`gemini-agents-api`](skills/gemini-agents-api/SKILL.md) | Manages custom Agent resources on Gemini Enterprise Agent Platform. | Apache-2.0 |
| [`gemini-api`](skills/gemini-api/SKILL.md) | Use when the user asks about using Gemini in an enterprise environment or explicitly mentions Vertex AI, Google Cloud, or Agent… | Apache-2.0 |
| [`gemini-interactions-api`](skills/gemini-interactions-api/SKILL.md) | Guides the usage of Gemini Interactions API on Gemini Enterprise Agent Platform. | Apache-2.0 |
| [`gemini-live-api`](skills/gemini-live-api/SKILL.md) | This skill provides instructions for generating a LiveAPI client service class that connects to the Gemini Enterprise Live API… | Apache-2.0 |
| [`gke-ai-troubleshooting-handle-disruption-gpu-tpu`](skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`gke-ai-troubleshooting-jobset-interruption`](skills/gke-ai-troubleshooting-jobset-interruption/SKILL.md) | Use this skill to systematically diagnose and resolve JobSet interruptions, restarts, and preemptions on GKE clusters hosting… | Apache-2.0 |
| [`gke-ai-troubleshooting-node-unresponsive-timeout`](skills/gke-ai-troubleshooting-node-unresponsive-timeout/SKILL.md) | When the Compute Engine host of a TPU or GPU node has a fatal hardware error, kernel panic, or non-maskable interrupt (NMI)… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-dynamic-slices-monitoring`](skills/gke-ai-troubleshooting-tpu-dynamic-slices-monitoring/SKILL.md) | Monitors the status of TPU Slice custom resources, troubleshoots provisioning failures, validates workload manifests on dynamic… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-metrics-monitoring`](skills/gke-ai-troubleshooting-tpu-metrics-monitoring/SKILL.md) | This skill enables the agent to monitor GKE TPU workloads, nodes, and node pools using GKE system metrics. | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-mxla-hang`](skills/gke-ai-troubleshooting-tpu-mxla-hang/SKILL.md) | Diagnose Cloud TPU multi-slice training hangs on Google Kubernetes Engine (GKE) by correlating Megascale HANGDETECTED logs and ML… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-partition-overlap`](skills/gke-ai-troubleshooting-tpu-partition-overlap/SKILL.md) | A dynamic slice fails to form with the status reason SliceCreationFailed when, among other documented causes, any of its nodes… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-performance-degradation`](skills/gke-ai-troubleshooting-tpu-performance-degradation/SKILL.md) | Diagnose and mitigate Cloud TPU training throughput drops and step-time regressions (15%+ drop in TPU duty cycle) on Google… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-reservation-stockout`](skills/gke-ai-troubleshooting-tpu-reservation-stockout/SKILL.md) | Use this skill to diagnose and resolve GKE TPU node pool creation or scale-up failures that fail with GCESTOCKOUT,… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-slice-mig-stuck-updating`](skills/gke-ai-troubleshooting-tpu-slice-mig-stuck-updating/SKILL.md) | This skill helps diagnose GKE TPU Dynamic Slice creation failures and JobSet scheduling delays when the Compute Engine managed… | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-vbar-oom`](skills/gke-ai-troubleshooting-tpu-vbar-oom/SKILL.md) | Use this skill to systematically diagnose and prevent vbarcontrolagent segfaults and Out-Of-Memory (OOM) errors on TPU v6e nodes. | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-vm-repair-stuck`](skills/gke-ai-troubleshooting-tpu-vm-repair-stuck/SKILL.md) | This skill checks the VM status, the host events, and the GKE repair status, and routes recovery through GKE instead of direct… | Apache-2.0 |
| [`gke-alert-configuration`](skills/gke-alert-configuration/SKILL.md) | This skill provides guidelines and best practices for creating robust, high-signal alerting policies for Google Kubernetes Engine… | Apache-2.0 |
| [`gke-app-onboarding`](skills/gke-app-onboarding/SKILL.md) | This reference provides workflows for containerizing and deploying applications to GKE for the first time. | Apache-2.0 |
| [`gke-backup-dr`](skills/gke-backup-dr/SKILL.md) | Protects stateful GKE workloads using Backup for GKE. | Apache-2.0 |
| [`gke-basics`](skills/gke-basics/SKILL.md) | Routing Note: For Workload Identity KSA/GSA setup, open gke-workload-identity/SKILL.md. | Apache-2.0 |
| [`gke-batch-hpc`](skills/gke-batch-hpc/SKILL.md) | This reference covers running batch processing and high-performance computing (HPC) workloads on GKE. | Apache-2.0 |
| [`gke-cluster-autoscaler`](skills/gke-cluster-autoscaler/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`gke-cluster-creation`](skills/gke-cluster-creation/SKILL.md) | This reference guides creating Google Kubernetes Engine (GKE) clusters by providing a set of best-practice templates and guiding… | Apache-2.0 |
| [`gke-compute-classes`](skills/gke-compute-classes/SKILL.md) | Guidance on configuring, optimizing, and troubleshooting GKE ComputeClasses. | Apache-2.0 |
| [`gke-cost-analysis`](skills/gke-cost-analysis/SKILL.md) | This skill provides guidance on answering natural language questions about GKE-related costs, billing reports, and utilization… | Apache-2.0 |
| [`gke-cost-optimization`](skills/gke-cost-optimization/SKILL.md) | This reference covers strategies and workflows for reducing Google Kubernetes Engine (GKE) costs while maintaining a secure and… | Apache-2.0 |
| [`gke-custom-golden-image-discovery`](skills/gke-custom-golden-image-discovery/SKILL.md) | You are an expert at helping users find the correct "golden" base image for creating custom GKE images. | Apache-2.0 |
| [`gke-golden-path`](skills/gke-golden-path/SKILL.md) | The golden path is the recommended Autopilot configuration for production clusters. | Apache-2.0 |
| [`gke-inference`](skills/gke-inference/SKILL.md) | Routing Note: For migrating existing AI workloads to GKE, open google-cloud-solution-guided-gke-ai-migration/SKILL.md. | Apache-2.0 |
| [`gke-manifest-generation`](skills/gke-manifest-generation/SKILL.md) | This skill provides guidelines, tooling integration, and templates to translate natural language descriptions or application code… | Apache-2.0 |
| [`gke-multitenancy`](skills/gke-multitenancy/SKILL.md) | This reference covers enterprise multi-tenancy patterns on GKE, including namespace isolation, RBAC planning, resource quotas,… | Apache-2.0 |
| [`gke-networking`](skills/gke-networking/SKILL.md) | This reference covers networking configuration for GKE clusters. | Apache-2.0 |
| [`gke-node-notready`](skills/gke-node-notready/SKILL.md) | Use this skill to systematically diagnose why one or more GKE nodes report a NotReady (or Ready: Unknown) status and to propose… | Apache-2.0 |
| [`gke-observability`](skills/gke-observability/SKILL.md) | This reference covers monitoring, logging, and metrics configuration for GKE. | Apache-2.0 |
| [`gke-platform-security`](skills/gke-platform-security/SKILL.md) | This reference covers platform-level security hardening and cluster configuration for Google Kubernetes Engine (GKE). | Apache-2.0 |
| [`gke-productionize`](skills/gke-productionize/SKILL.md) | Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability,… | Apache-2.0 |
| [`gke-reliability`](skills/gke-reliability/SKILL.md) | Routing Note: To generate Kubernetes YAML manifests (Deployment, StatefulSet, Service, ConfigMap, HTTPRoute,… | Apache-2.0 |
| [`gke-service-networking`](skills/gke-service-networking/SKILL.md) | This skill provides workflows for exposing applications running on GKE securely to the internet or internal networks. | Apache-2.0 |
| [`gke-storage`](skills/gke-storage/SKILL.md) | Routing Note: For Cloud Storage FUSE (gcsfuse) mounts or the GKE gcsfuse.csi.storage.gke.io CSI driver, open… | Apache-2.0 |
| [`gke-storage-troubleshooting`](skills/gke-storage-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve persistent-storage failures for workloads running on GKE — volume… | Apache-2.0 |
| [`gke-upgrades`](skills/gke-upgrades/SKILL.md) | Produce clear, actionable documents — upgrade plans, runbooks, or checklists — tailored to the user's environment. | Apache-2.0 |
| [`gke-workload-identity`](skills/gke-workload-identity/SKILL.md) | Use this skill to systematically diagnose why a Pod using Workload Identity Federation for GKE cannot authenticate to Google… | Apache-2.0 |
| [`gke-workload-scaling`](skills/gke-workload-scaling/SKILL.md) | This skill provides workflows and best practices for scaling applications on Google Kubernetes Engine (GKE). | Apache-2.0 |
| [`gke-workload-scaling-troubleshooting`](skills/gke-workload-scaling-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve HorizontalPodAutoscaler (HPA) failures on GKE — metrics reported as… | Apache-2.0 |
| [`gke-workload-security`](skills/gke-workload-security/SKILL.md) | Routing Note: For Workload Identity KSA/GSA bindings, open gke-workload-identity/SKILL.md. | Apache-2.0 |
| [`gke-workload-troubleshooting`](skills/gke-workload-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve failures in application workloads deployed in GKE clusters. | Apache-2.0 |
| [`google-ads-api-account-diagnostics`](skills/google-ads-api-account-diagnostics/SKILL.md) | This skill provides instructions on how to use the Google Ads MCP server tools to diagnose common account performance issues. | Apache-2.0 |
| [`google-ads-api-mcp-setup`](skills/google-ads-api-mcp-setup/SKILL.md) | Guides developers through downloading, configuring, and installing the official open-source Google Ads MCP Server. | Apache-2.0 |
| [`google-ads-api-quickstart`](skills/google-ads-api-quickstart/SKILL.md) | 1. Official Client Libraries: Python, Java, .NET, PHP, Ruby, or Perl. 2. Direct REST: Raw HTTP REST requests. | Apache-2.0 |
| [`google-agents-cli-onboarding`](skills/google-agents-cli-onboarding/SKILL.md) | !TIP One-Time Setup: To install the CLI and enable all 7 specialized development skills in your coding agent, run the setup… | Apache-2.0 |
| [`google-analytics-admin-api-basics`](skills/google-analytics-admin-api-basics/SKILL.md) | The Google Analytics Admin API provides programmatic access to Google Analytics account and property configuration. | Apache-2.0 |
| [`google-analytics-data-api-basics`](skills/google-analytics-data-api-basics/SKILL.md) | The Google Analytics Data API v1beta provides programmatic access to Google Analytics report data. | Apache-2.0 |
| [`google-cloud-filestore-auditing`](skills/google-cloud-filestore-auditing/SKILL.md) | This skill enables autonomous agents to audit, evaluate, and report the disaster recovery, security access governance, and… | Apache-2.0 |
| [`google-cloud-filestore-autoscale`](skills/google-cloud-filestore-autoscale/SKILL.md) | This skill enables agents to inspect, evaluate, and modify Filestore instance capacities across Google Cloud projects based on… | Apache-2.0 |
| [`google-cloud-filestore-log-troubleshooting`](skills/google-cloud-filestore-log-troubleshooting/SKILL.md) | Diagnoses, troubleshoots, and remediates Filestore client mount failures, permission errors (EACCES), and network timeouts… | Apache-2.0 |
| [`google-cloud-filestore-nfs-browser`](skills/google-cloud-filestore-nfs-browser/SKILL.md) | Enables autonomous agents and cloud engineers to inspect, search, and read files located on Filestore (NFS) instances without… | Apache-2.0 |
| [`google-cloud-global-frontend-configuration`](skills/google-cloud-global-frontend-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | Apache-2.0 |
| [`google-cloud-networking-observability`](skills/google-cloud-networking-observability/SKILL.md) | For all gcloud CLI, REST API, and MCP attribution requirements when executing commands with this skill, follow the instructions… | Apache-2.0 |
| [`google-cloud-recipe-auth`](skills/google-cloud-recipe-auth/SKILL.md) | Provides expert guidance on Identity and Access Management (IAM) and authenticating and authorizing to Google Cloud services and… | Apache-2.0 |
| [`google-cloud-recipe-foundation-builder`](skills/google-cloud-recipe-foundation-builder/SKILL.md) | !WARNING This skill is currently in a preview state. | Apache-2.0 |
| [`google-cloud-recipe-onboarding`](skills/google-cloud-recipe-onboarding/SKILL.md) | This skill provides a streamlined, non-interactive "happy path" for a singleton developer to get started with Google… | Apache-2.0 |
| [`google-cloud-scc-query`](skills/google-cloud-scc-query/SKILL.md) | Provides guidelines and read-only gcloud CLI command patterns for querying and retrieving security findings, external exposures,… | Apache-2.0 |
| [`google-cloud-scc-remediation`](skills/google-cloud-scc-remediation/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-slo-alert-configuration`](skills/google-cloud-slo-alert-configuration/SKILL.md) | This skill guides the user through a structured conversation to configure Cloud Monitoring PromQL-based Service Level Objective… | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-bidirectional-streaming`](skills/google-cloud-solution-agentic-ai-bidirectional-streaming/SKILL.md) | This skill guides agents through the workflow to design and implement a tailored multi-product solution in the cloud for a live,… | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-borderless-data-lakehouse`](skills/google-cloud-solution-agentic-ai-borderless-data-lakehouse/SKILL.md) | Follow this workflow to help users design and implement a custom multi-product solution in the cloud for a given workload, use… | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-data-science-workflow`](skills/google-cloud-solution-agentic-ai-data-science-workflow/SKILL.md) | This skill guides agents through the workflow to design and implement a tailored multi-product solution in the cloud for a given… | Apache-2.0 |
| [`google-cloud-solution-agentic-analytics-spark-knowledge-catalog`](skills/google-cloud-solution-agentic-analytics-spark-knowledge-catalog/SKILL.md) | This skill provides a workflow to design and implement a governed, secure pipeline for agentic analytics solution across… | Apache-2.0 |
| [`google-cloud-solution-architecture`](skills/google-cloud-solution-architecture/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-solution-build-deploy-agents`](skills/google-cloud-solution-build-deploy-agents/SKILL.md) | This skill guides agents through the workflow of designing and implementing a tailored multi-product solution in the cloud for a… | Apache-2.0 |
| [`google-cloud-solution-guided-gke-ai-migration`](skills/google-cloud-solution-guided-gke-ai-migration/SKILL.md) | This skill guides agents through the end-to-end process of migrating existing AI inference workloads (e.g., from Cloud Run,… | Apache-2.0 |
| [`google-cloud-solution-hybrid-search-alloydb`](skills/google-cloud-solution-hybrid-search-alloydb/SKILL.md) | This skill provides a workflow to design and implement secure, low-latency, and high-accuracy hybrid search solutions combining… | Apache-2.0 |
| [`google-cloud-solution-multi-agent-security`](skills/google-cloud-solution-multi-agent-security/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-solution-n-tier-serverless-web-app`](skills/google-cloud-solution-n-tier-serverless-web-app/SKILL.md) | <!-- disableFinding(all) -- <!-- mdlint off -- | Apache-2.0 |
| [`google-cloud-solution-rag-enterprise-search-gke-sqldb`](skills/google-cloud-solution-rag-enterprise-search-gke-sqldb/SKILL.md) | This skill provides a workflow to design and implement a secure, low-latency, and high-accuracy RAG-enabled conversational search… | Apache-2.0 |
| [`google-cloud-storage-basics`](skills/google-cloud-storage-basics/SKILL.md) | Cloud Storage on Google Cloud is a managed service for storing data as objects at any scale. | Apache-2.0 |
| [`google-cloud-storage-bucket-architect`](skills/google-cloud-storage-bucket-architect/SKILL.md) | You are a Use-Case Driven Cloud Storage Bucket Architect agent on Google Cloud. | Apache-2.0 |
| [`google-cloud-storage-fuse`](skills/google-cloud-storage-fuse/SKILL.md) | Cloud Storage FUSE is a POSIX file-system adapter over Cloud Storage on Google Cloud, operated via the gcsfuse CLI tool. | Apache-2.0 |
| [`google-cloud-waf-cost-optimization`](skills/google-cloud-waf-cost-optimization/SKILL.md) | Evaluates Google Cloud workloads for cost efficiency and FinOps alignment using the Google Cloud Well-Architected Framework Cost… | Apache-2.0 |
| [`google-cloud-waf-operational-excellence`](skills/google-cloud-waf-operational-excellence/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-waf-performance-optimization`](skills/google-cloud-waf-performance-optimization/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-waf-reliability`](skills/google-cloud-waf-reliability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-waf-security`](skills/google-cloud-waf-security/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-cloud-waf-sustainability`](skills/google-cloud-waf-sustainability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | Apache-2.0 |
| [`google-mobile-ads-android-migrate-to-next-gen`](skills/google-mobile-ads-android-migrate-to-next-gen/SKILL.md) | Migrates Android applications from the old, legacy Google Mobile | Apache-2.0 |
| [`google-mobile-ads-banner`](skills/google-mobile-ads-banner/SKILL.md) | Banner ads are rectangular image or text ads that occupy a spot within an app's layout. | Apache-2.0 |
| [`google-mobile-ads-get-started`](skills/google-mobile-ads-get-started/SKILL.md) | 1. Determine the user's platform: Identify if the project is Android, iOS, or Unity. If unclear, ask before proceeding. | Apache-2.0 |
| [`google-mobile-ads-interstitial`](skills/google-mobile-ads-interstitial/SKILL.md) | Interstitial ads show full-page ads for users on mobile apps. | Apache-2.0 |
| [`google-mobile-ads-rewarded`](skills/google-mobile-ads-rewarded/SKILL.md) | Rewarded ads reward users with in-app items for interacting with full-screen ads. | Apache-2.0 |
| [`google-mobile-ads-validate`](skills/google-mobile-ads-validate/SKILL.md) | Validate a project's Google Mobile Ads (GMA) SDK integration either as a complete audit or for specific requested checks. | Apache-2.0 |
| [`iam-helper-for-policy-management`](skills/iam-helper-for-policy-management/SKILL.md) | Orchestrates the lifecycle and management of IAM allow and deny policies across IAM v1 (allow policies) and IAM v2 (deny… | Apache-2.0 |
| [`iam-helper-for-policy-simulator`](skills/iam-helper-for-policy-simulator/SKILL.md) | You are an advanced security assistant helping users safely modify IAM policies. | Apache-2.0 |
| [`iam-helper-for-privileged-access-management`](skills/iam-helper-for-privileged-access-management/SKILL.md) | This skill provides step-by-step guidance for planning, validating, and executing Privileged Access Manager (PAM) entitlement… | Apache-2.0 |
| [`iam-helper-for-troubleshooting`](skills/iam-helper-for-troubleshooting/SKILL.md) | You are an expert Google Cloud Security and IAM assistant. | Apache-2.0 |
| [`ima-dai-sdk`](skills/ima-dai-sdk/SKILL.md) | Use the IMA DAI SDK to load HLS or DASH streams into the app for: | Apache-2.0 |
| [`ima-sdk-client-side`](skills/ima-sdk-client-side/SKILL.md) | The Google IMA SDK (Interactive Media Ads) lets you load in-stream video and audio ads into websites, apps, TVs and other digital… | Apache-2.0 |
| [`managed-airflow-dag-authoring`](skills/managed-airflow-dag-authoring/SKILL.md) | This skill guides you through authoring and validating Apache Airflow DAGs for Managed Service for Apache Airflow (MSAA; formerly… | Apache-2.0 |
| [`managed-airflow-dag-troubleshooting`](skills/managed-airflow-dag-troubleshooting/SKILL.md) | This skill provides instructions for troubleshooting Managed Airflow DAGs (DAG runs and task instances), utilizing gcloud… | Apache-2.0 |
| [`managed-airflow-migrations`](skills/managed-airflow-migrations/SKILL.md) | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). | Apache-2.0 |
| [`managed-airflow-recommendations`](skills/managed-airflow-recommendations/SKILL.md) | This skill provides specialized instructions for providing recommendations, best practices, and performance-tuning for Managed… | Apache-2.0 |
| [`migrate-to-rust`](skills/migrate-to-rust/SKILL.md) | Act as a Systems Architect, Performance Engineer, and Rust Specialist. | Apache-2.0 |
| [`mirrord-chaos`](skills/mirrord-chaos/SKILL.md) | Help users inject artificial failures and disruptions into a mirrord session's outgoing traffic, to test how their app behaves… | MIT |
| [`mirrord-ci`](skills/mirrord-ci/SKILL.md) | Help users set up mirrord in CI pipelines for testing against real Kubernetes environments. | MIT |
| [`mirrord-config`](skills/mirrord-config/SKILL.md) | Helps users generate, edit, and validate mirrord.json configuration files for mirrord (MetalBear). | MIT |
| [`mirrord-db-branching`](skills/mirrord-db-branching/SKILL.md) | Helps users configure mirrord.json for database branching, enabling isolated database copies for safe development and testing. | MIT |
| [`mirrord-header-propagation`](skills/mirrord-header-propagation/SKILL.md) | mirrord routes traffic to a developer's session by matching a header. | MIT |
| [`mirrord-kafka`](skills/mirrord-kafka/SKILL.md) | Which CRDs? Kafka splitting is now configured with MirrordSplitConfig (which queues to split + how the app finds their names) and… | MIT |
| [`mirrord-operator`](skills/mirrord-operator/SKILL.md) | Help users install and configure the mirrord Operator for team/enterprise environments. | MIT |
| [`mirrord-prev-env`](skills/mirrord-prev-env/SKILL.md) | Help users create and manage mirrord preview environments — running a modified service as an isolated pod in a shared Kubernetes… | MIT |
| [`mirrord-propagation-discovery`](skills/mirrord-propagation-discovery/SKILL.md) | mirrord routes a request to a developer's local process when the request matches an HTTP filter. | MIT |
| [`mirrord-quickstart`](skills/mirrord-quickstart/SKILL.md) | Guide users from zero to their first working mirrord session — check system requirements, install mirrord via CLI, VS Code, or… | MIT |
| [`mirrord-temporal`](skills/mirrord-temporal/SKILL.md) | Temporal splitting is configured with MirrordSplitConfig (which task queues to split + how the worker finds their names) and… | MIT |
| [`mirrord-up`](skills/mirrord-up/SKILL.md) | Help users create and run multiple concurrent mirrord sessions from one config file — think docker compose, but for mirrord — as… | MIT |
| [`observability-and-instrumentation`](skills/observability-and-instrumentation/SKILL.md) | Instruments code so production behavior is visible and diagnosable. | MIT |
| [`pack-cloud-and-deploy`](skills/pack-cloud-and-deploy/SKILL.md) | Everything between a working tree and a running system on Google Cloud: 180+ product skills covering BigQuery, GKE, Cloud Run,… | mixed |
| [`retrieving-developer-knowledge`](skills/retrieving-developer-knowledge/SKILL.md) | The Developer Knowledge skill provides access to official Google developer documentation across Google Cloud, AI/ML… | Apache-2.0 |
| [`secops-cases`](skills/secops-cases/SKILL.md) | Operates and manages incident cases within Google Security Operations (Google SecOps SOAR). | Apache-2.0 |
| [`secops-detection-engineering`](skills/secops-detection-engineering/SKILL.md) | This skill guides security engineers and autonomous agents through the end-to-end detection engineering lifecycle within Google… | Apache-2.0 |
| [`secops-hunt`](skills/secops-hunt/SKILL.md) | You are an expert Threat Hunter operating within Google Security Operations (SecOps). | Apache-2.0 |
| [`secops-investigate`](skills/secops-investigate/SKILL.md) | You are an expert Security Operations Center (SOC) Tier 2/3 Analyst and Incident Responder operating within Google Security… | Apache-2.0 |
| [`secops-triage`](skills/secops-triage/SKILL.md) | You are an expert Security Operations Center (SOC) Analyst specializing in Google Security Operations (SecOps). | Apache-2.0 |
| [`shipping-and-launch`](skills/shipping-and-launch/SKILL.md) | Prepares production launches. | MIT |
| [`sign-in-with-google-web`](skills/sign-in-with-google-web/SKILL.md) | This skill provides normative architectural guidelines, secure implementation contracts, and failure-prevention protocols for… | Apache-2.0 |
| [`spanner-basics`](skills/spanner-basics/SKILL.md) | This skill provides core workflows and guidance for administering and developing with Cloud Spanner on Google Cloud, a fully… | Apache-2.0 |
| [`vercel-cli-with-tokens`](skills/vercel-cli-with-tokens/SKILL.md) | Deploy and manage projects on Vercel using token-based authentication. | NOASSERTION |
| [`vercel-optimize`](skills/vercel-optimize/SKILL.md) | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro… | NOASSERTION |
| [`workload-manager-basics`](skills/workload-manager-basics/SKILL.md) | Workload Manager validates enterprise workloads against Google Cloud best practices and recommendations. | Apache-2.0 |

### AI & ML (`ai-and-ml`) — 125 skills

Index pack: [`pack-ai-and-ml`](skills/pack-ai-and-ml/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`academic-plotting`](skills/academic-plotting/SKILL.md) | Generates publication-quality figures for ML papers from research context. | MIT |
| [`ara-compiler`](skills/ara-compiler/SKILL.md) | Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete… | MIT |
| [`ara-research-manager`](skills/ara-research-manager/SKILL.md) | Records research provenance as a post-task epilogue, scanning conversation history at the end of a coding or research session to… | MIT |
| [`ara-rigor-reviewer`](skills/ara-rigor-reviewer/SKILL.md) | Performs ARA Seal Level 2 semantic epistemic review on Agent-Native Research Artifacts, scoring six dimensions (evidence… | MIT |
| [`audiocraft-audio-generation`](skills/audiocraft-audio-generation/SKILL.md) | PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). | MIT |
| [`autogpt-agents`](skills/autogpt-agents/SKILL.md) | Autonomous AI agent platform for building and deploying continuous agents. | MIT |
| [`autoresearch`](skills/autoresearch/SKILL.md) | Orchestrates end-to-end autonomous AI research projects using a two-loop architecture. | MIT |
| [`awq-quantization`](skills/awq-quantization/SKILL.md) | Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. | MIT |
| [`axolotl`](skills/axolotl/SKILL.md) | Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support | MIT |
| [`blip-2-vision-language`](skills/blip-2-vision-language/SKILL.md) | Vision-language pre-training framework bridging frozen image encoders and LLMs. | MIT |
| [`brainstorming-research-ideas`](skills/brainstorming-research-ideas/SKILL.md) | Guides researchers through structured ideation frameworks to discover high-impact research directions. | MIT |
| [`chroma`](skills/chroma/SKILL.md) | Open-source embedding database for AI applications. | MIT |
| [`clip`](skills/clip/SKILL.md) | OpenAI's model connecting vision and language. | MIT |
| [`constitutional-ai`](skills/constitutional-ai/SKILL.md) | Anthropic's method for training harmless AI through self-improvement. | MIT |
| [`creative-thinking-for-research`](skills/creative-thinking-for-research/SKILL.md) | Applies cognitive science frameworks for creative thinking to CS and AI research ideation. | MIT |
| [`crewai-multi-agent`](skills/crewai-multi-agent/SKILL.md) | Multi-agent orchestration framework for autonomous AI collaboration. | MIT |
| [`deepspeed`](skills/deepspeed/SKILL.md) | Expert guidance for distributed training with DeepSpeed - ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8, 1-bit… | MIT |
| [`distributed-llm-pretraining-torchtitan`](skills/distributed-llm-pretraining-torchtitan/SKILL.md) | Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). | MIT |
| [`dspy`](skills/dspy/SKILL.md) | Build complex AI systems with declarative programming, optimize prompts automatically, create modular RAG systems and agents with… | MIT |
| [`evaluating-code-models`](skills/evaluating-code-models/SKILL.md) | Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics. | MIT |
| [`evaluating-cosmos-policy`](skills/evaluating-cosmos-policy/SKILL.md) | Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments. | MIT |
| [`evaluating-llms-harness`](skills/evaluating-llms-harness/SKILL.md) | Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). | MIT |
| [`evolving-ai-agents`](skills/evolving-ai-agents/SKILL.md) | Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. | MIT |
| [`experiment-tracking-swanlab`](skills/experiment-tracking-swanlab/SKILL.md) | Provides guidance for experiment tracking with SwanLab. | MIT |
| [`faiss`](skills/faiss/SKILL.md) | Facebook's library for efficient similarity search and clustering of dense vectors. | MIT |
| [`fine-tuning-openvla-oft`](skills/fine-tuning-openvla-oft/SKILL.md) | Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA… | MIT |
| [`fine-tuning-serving-openpi`](skills/fine-tuning-serving-openpi/SKILL.md) | Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy… | MIT |
| [`fine-tuning-with-trl`](skills/fine-tuning-with-trl/SKILL.md) | Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for… | MIT |
| [`gguf-quantization`](skills/gguf-quantization/SKILL.md) | GGUF format and llama.cpp quantization for efficient CPU/GPU inference. | MIT |
| [`gptq`](skills/gptq/SKILL.md) | Post-training 4-bit quantization for LLMs with minimal accuracy loss. | MIT |
| [`grpo-rl-training`](skills/grpo-rl-training/SKILL.md) | Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training | MIT |
| [`guidance`](skills/guidance/SKILL.md) | Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build… | MIT |
| [`hf-cli`](skills/hf-cli/SKILL.md) | Hugging Face Hub CLI (`hf`) for downloading, uploading, and managing models, datasets, spaces, buckets, repos, papers, jobs, and… | Apache-2.0 |
| [`hf-cloud-aws-context-discovery`](skills/hf-cloud-aws-context-discovery/SKILL.md) | Discover the user's local AWS context (active profile, region, account ID, caller identity) at the start of any AWS task. | Apache-2.0 |
| [`hf-cloud-python-env-setup`](skills/hf-cloud-python-env-setup/SKILL.md) | Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto3. | Apache-2.0 |
| [`hf-cloud-sagemaker-deployment-planner`](skills/hf-cloud-sagemaker-deployment-planner/SKILL.md) | Plan and coordinate the deployment of a model to Amazon SageMaker AI. | Apache-2.0 |
| [`hf-cloud-sagemaker-iam-preflight`](skills/hf-cloud-sagemaker-iam-preflight/SKILL.md) | Ensure a usable SageMaker execution role exists before deploying or training. | Apache-2.0 |
| [`hf-cloud-sagemaker-production-defaults`](skills/hf-cloud-sagemaker-production-defaults/SKILL.md) | Create a SageMaker endpoint (real-time, real-time scale-to-zero, or async) with autoscaling, CloudWatch alarms, and tagging… | Apache-2.0 |
| [`hf-cloud-serving-image-selection`](skills/hf-cloud-serving-image-selection/SKILL.md) | Pick the right serving container for a SageMaker model deployment and find its current image URI. | Apache-2.0 |
| [`hf-mcp`](skills/hf-mcp/SKILL.md) | Use Hugging Face Hub via MCP server tools. | Apache-2.0 |
| [`hf-mem`](skills/hf-mem/SKILL.md) | Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub | Apache-2.0 |
| [`hqq-quantization`](skills/hqq-quantization/SKILL.md) | Half-Quadratic Quantization for LLMs without calibration data. | MIT |
| [`huggingface-accelerate`](skills/huggingface-accelerate/SKILL.md) | Simplest distributed training API. | MIT |
| [`huggingface-best`](skills/huggingface-best/SKILL.md) | Finds the best models for a task by querying official HF benchmark leaderboards, enriching results with model size data,… | Apache-2.0 |
| [`huggingface-community-evals`](skills/huggingface-community-evals/SKILL.md) | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. | Apache-2.0 |
| [`huggingface-datasets`](skills/huggingface-datasets/SKILL.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply… | Apache-2.0 |
| [`huggingface-gradio`](skills/huggingface-gradio/SKILL.md) | Build Gradio web UIs and demos in Python. | Apache-2.0 |
| [`huggingface-llm-trainer`](skills/huggingface-llm-trainer/SKILL.md) | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Face Jobs… | Apache-2.0 |
| [`huggingface-local-models`](skills/huggingface-local-models/SKILL.md) | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. | Apache-2.0 |
| [`huggingface-lora-space-builder`](skills/huggingface-lora-space-builder/SKILL.md) | Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. | Apache-2.0 |
| [`huggingface-paper-publisher`](skills/huggingface-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. | Apache-2.0 |
| [`huggingface-papers`](skills/huggingface-papers/SKILL.md) | Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked… | Apache-2.0 |
| [`huggingface-spaces`](skills/huggingface-spaces/SKILL.md) | Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated hardware,… | Apache-2.0 |
| [`huggingface-tokenizers`](skills/huggingface-tokenizers/SKILL.md) | Fast tokenizers optimized for research and production. | MIT |
| [`huggingface-tool-builder`](skills/huggingface-tool-builder/SKILL.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. | Apache-2.0 |
| [`huggingface-trackio`](skills/huggingface-trackio/SKILL.md) | Track and visualize ML training experiments with Trackio. | Apache-2.0 |
| [`huggingface-vision-trainer`](skills/huggingface-vision-trainer/SKILL.md) | Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm models —… | Apache-2.0 |
| [`huggingface-zerogpu`](skills/huggingface-zerogpu/SKILL.md) | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. | Apache-2.0 |
| [`implementing-llms-litgpt`](skills/implementing-llms-litgpt/SKILL.md) | Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral). | MIT |
| [`instructor`](skills/instructor/SKILL.md) | Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON… | MIT |
| [`knowledge-distillation`](skills/knowledge-distillation/SKILL.md) | Compress large language models using knowledge distillation from teacher to student models. | MIT |
| [`lambda-labs-gpu-cloud`](skills/lambda-labs-gpu-cloud/SKILL.md) | Reserved and on-demand GPU cloud instances for ML training and inference. | MIT |
| [`langchain`](skills/langchain/SKILL.md) | Framework for building LLM-powered applications with agents, chains, and RAG. | MIT |
| [`langsmith-observability`](skills/langsmith-observability/SKILL.md) | LLM observability platform for tracing, evaluation, and monitoring. | MIT |
| [`llama-cpp`](skills/llama-cpp/SKILL.md) | Runs LLM inference on CPU, Apple Silicon, and consumer GPUs without NVIDIA hardware. | MIT |
| [`llama-factory`](skills/llama-factory/SKILL.md) | Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support | MIT |
| [`llamaguard`](skills/llamaguard/SKILL.md) | Meta's 7-8B specialized moderation model for LLM input/output filtering. | MIT |
| [`llamaindex`](skills/llamaindex/SKILL.md) | Data framework for building LLM applications with RAG. | MIT |
| [`llava`](skills/llava/SKILL.md) | Large Language and Vision Assistant. | MIT |
| [`long-context`](skills/long-context/SKILL.md) | Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques. | MIT |
| [`mamba-architecture`](skills/mamba-architecture/SKILL.md) | State-space model with O(n) complexity vs Transformers' O(n²). | MIT |
| [`miles-rl-training`](skills/miles-rl-training/SKILL.md) | Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. | MIT |
| [`ml-paper-writing`](skills/ml-paper-writing/SKILL.md) | Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM. | MIT |
| [`ml-training-recipes`](skills/ml-training-recipes/SKILL.md) | Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery,… | MIT |
| [`mlflow`](skills/mlflow/SKILL.md) | Track ML experiments, manage model registry with versioning, deploy models to production, and reproduce experiments with MLflow -… | MIT |
| [`modal-serverless-gpu`](skills/modal-serverless-gpu/SKILL.md) | Serverless GPU cloud platform for running ML workloads. | MIT |
| [`model-merging`](skills/model-merging/SKILL.md) | Merge multiple fine-tuned models using mergekit to combine capabilities without retraining. | MIT |
| [`model-pruning`](skills/model-pruning/SKILL.md) | Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT. | MIT |
| [`moe-training`](skills/moe-training/SKILL.md) | Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace. | MIT |
| [`nanogpt`](skills/nanogpt/SKILL.md) | Educational GPT implementation in ~300 lines. | MIT |
| [`nemo-curator`](skills/nemo-curator/SKILL.md) | GPU-accelerated data curation for LLM training. | MIT |
| [`nemo-evaluator-sdk`](skills/nemo-evaluator-sdk/SKILL.md) | Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution. | MIT |
| [`nemo-guardrails`](skills/nemo-guardrails/SKILL.md) | NVIDIA's runtime safety framework for LLM applications. | MIT |
| [`nnsight-remote-interpretability`](skills/nnsight-remote-interpretability/SKILL.md) | Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution. | MIT |
| [`openrlhf-training`](skills/openrlhf-training/SKILL.md) | High-performance RLHF framework with Ray+vLLM acceleration. | MIT |
| [`optimizing-attention-flash`](skills/optimizing-attention-flash/SKILL.md) | Optimizes transformer attention with Flash Attention for 2-4x speedup and 10-20x memory reduction. | MIT |
| [`outlines`](skills/outlines/SKILL.md) | Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models… | MIT |
| [`pack-ai-and-ml`](skills/pack-ai-and-ml/SKILL.md) | Model work from a paper to a served endpoint: architecture notes (Mamba, RWKV, diffusion, CLIP, BLIP-2), fine-tuning stacks… | mixed |
| [`peft-fine-tuning`](skills/peft-fine-tuning/SKILL.md) | Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. | MIT |
| [`phoenix-observability`](skills/phoenix-observability/SKILL.md) | Open-source AI observability platform for LLM tracing, evaluation, and monitoring. | MIT |
| [`pinecone`](skills/pinecone/SKILL.md) | Managed vector database for production AI applications. | MIT |
| [`presenting-conference-talks`](skills/presenting-conference-talks/SKILL.md) | Generates conference presentation slides (Beamer LaTeX PDF and editable PPTX) from a compiled paper with speaker notes and talk… | MIT |
| [`prompt-guard`](skills/prompt-guard/SKILL.md) | Meta's 86M prompt injection and jailbreak detector. | MIT |
| [`pytorch-fsdp2`](skills/pytorch-fsdp2/SKILL.md) | Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed… | MIT |
| [`pytorch-lightning`](skills/pytorch-lightning/SKILL.md) | High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and… | MIT |
| [`pyvene-interventions`](skills/pyvene-interventions/SKILL.md) | Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework. | MIT |
| [`qdrant-vector-search`](skills/qdrant-vector-search/SKILL.md) | High-performance vector similarity search engine for RAG and semantic search. | MIT |
| [`quantizing-models-bitsandbytes`](skills/quantizing-models-bitsandbytes/SKILL.md) | Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss. | MIT |
| [`ray-data`](skills/ray-data/SKILL.md) | Scalable data processing for ML workloads. | MIT |
| [`ray-train`](skills/ray-train/SKILL.md) | Distributed training orchestration across clusters. | MIT |
| [`rwkv-architecture`](skills/rwkv-architecture/SKILL.md) | RNN+Transformer hybrid with O(n) inference. | MIT |
| [`segment-anything-model`](skills/segment-anything-model/SKILL.md) | Foundation model for image segmentation with zero-shot transfer. | MIT |
| [`sentence-transformers`](skills/sentence-transformers/SKILL.md) | Framework for state-of-the-art sentence, text, and image embeddings. | MIT |
| [`sentencepiece`](skills/sentencepiece/SKILL.md) | Language-independent tokenizer treating text as raw Unicode. | MIT |
| [`serving-llms-vllm`](skills/serving-llms-vllm/SKILL.md) | Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. | MIT |
| [`sglang`](skills/sglang/SKILL.md) | Fast structured generation and serving for LLMs with RadixAttention prefix caching. | MIT |
| [`simpo-training`](skills/simpo-training/SKILL.md) | Simple Preference Optimization for LLM alignment. | MIT |
| [`skypilot-multi-cloud-orchestration`](skills/skypilot-multi-cloud-orchestration/SKILL.md) | Multi-cloud orchestration for ML workloads with automatic cost optimization. | MIT |
| [`slime-rl-training`](skills/slime-rl-training/SKILL.md) | Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. | MIT |
| [`sparse-autoencoder-training`](skills/sparse-autoencoder-training/SKILL.md) | Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations… | MIT |
| [`speculative-decoding`](skills/speculative-decoding/SKILL.md) | Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques. | MIT |
| [`stable-diffusion-image-generation`](skills/stable-diffusion-image-generation/SKILL.md) | State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. | MIT |
| [`systems-paper-writing`](skills/systems-paper-writing/SKILL.md) | Comprehensive guide for writing systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. | MIT |
| [`tensorboard`](skills/tensorboard/SKILL.md) | Visualize training metrics, debug models with histograms, compare experiments, visualize model graphs, and profile performance… | MIT |
| [`tensorrt-llm`](skills/tensorrt-llm/SKILL.md) | Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. | MIT |
| [`torchforge-rl-training`](skills/torchforge-rl-training/SKILL.md) | Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms. | MIT |
| [`train-sentence-transformers`](skills/train-sentence-transformers/SKILL.md) | Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder, dense or static embedding model for… | Apache-2.0 |
| [`training-llms-megatron`](skills/training-llms-megatron/SKILL.md) | Trains large language models (2B-462B parameters) using NVIDIA Megatron-Core with advanced parallelism strategies. | MIT |
| [`transformer-lens-interpretability`](skills/transformer-lens-interpretability/SKILL.md) | Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals… | MIT |
| [`transformers-js`](skills/transformers-js/SKILL.md) | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. | Apache-2.0 |
| [`trl-training`](skills/trl-training/SKILL.md) | Post-train LLMs with TRL (Transformers Reinforcement Learning) — SFT, DPO, GRPO, KTO, and reward-model training. | Apache-2.0 |
| [`unsloth`](skills/unsloth/SKILL.md) | Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization | MIT |
| [`verl-rl-training`](skills/verl-rl-training/SKILL.md) | Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). | MIT |
| [`weights-and-biases`](skills/weights-and-biases/SKILL.md) | Track ML experiments with automatic logging, visualize training in real-time, optimize hyperparameters with sweeps, and manage… | MIT |
| [`whisper`](skills/whisper/SKILL.md) | OpenAI's general-purpose speech recognition model. | MIT |

### Office documents (`office-docs`) — 14 skills

Index pack: [`pack-office-docs`](skills/pack-office-docs/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`frontend-slides`](skills/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. | MIT |
| [`html-deck-styles`](skills/html-deck-styles/SKILL.md) | HTML deck styles — 30+ art-directed slide systems. | Apache-2.0 |
| [`html-document-templates`](skills/html-document-templates/SKILL.md) | HTML document templates — resume, invoice, notes, OKRs, spec, runbook, article. | Apache-2.0 |
| [`minimax-docx`](skills/minimax-docx/SKILL.md) | Create, edit, and format DOCX documents via CLI tools or direct C# scripts built on OpenXML SDK (.NET). | MIT |
| [`minimax-pdf`](skills/minimax-pdf/SKILL.md) | Rule: when in doubt between CREATE and REFORMAT, ask whether the user has an existing document to start from. | MIT |
| [`minimax-xlsx`](skills/minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). | MIT |
| [`pack-office-docs`](skills/pack-office-docs/SKILL.md) | Produce and edit real office files: Word documents with tracked changes and styles, PowerPoint decks built with PptxGenJS or… | mixed |
| [`pdf-conversion-router`](skills/pdf-conversion-router/SKILL.md) | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must… | MIT |
| [`ppt-editing-skill`](skills/ppt-editing-skill/SKILL.md) | Edit existing PowerPoint files or templates with XML-safe workflows. | MIT |
| [`ppt-orchestra-skill`](skills/ppt-orchestra-skill/SKILL.md) | Plan and orchestrate multi-slide PowerPoint creation from scratch. | MIT |
| [`pptx-deck-creation`](skills/pptx-deck-creation/SKILL.md) | Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks. | MIT |
| [`pptx-generator`](skills/pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations. | MIT |
| [`slide-making-skill`](skills/slide-making-skill/SKILL.md) | Implement single-slide PowerPoint pages with PptxGenJS. | MIT |
| [`spreadsheet-manual-build`](skills/spreadsheet-manual-build/SKILL.md) | Spreadsheet Manual Build: an empty Excel workbook or CSV from a confirmed field list, formatted and validated. | MIT |

### Engineering workflow (`engineering-workflow`) — 401 skills

Index pack: [`pack-engineering-workflow`](skills/pack-engineering-workflow/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`academic-paper-reviewer`](skills/academic-paper-reviewer/SKILL.md) | Simulates academic peer review, evaluating papers across Originality, Methodology, Results, and Writing to provide Major/Minor… | MIT |
| [`access`](skills/access/SKILL.md) | Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. | Apache-2.0 |
| [`accessibility`](skills/accessibility/SKILL.md) | Audit and improve web accessibility following WCAG 2.1 guidelines. | MIT |
| [`active-directory-attacks`](skills/active-directory-attacks/SKILL.md) | This skill should be used when the user asks to "attack Active Directory", "exploit AD", "Kerberoasting", "DCSync",… | MIT |
| [`add-anydoc`](skills/add-anydoc/SKILL.md) | Add local office-document-to-Markdown conversion to NanoClaw agent containers with the pinned Firecrawl AnyDoc CLI. | MIT |
| [`add-atomic-chat-tool`](skills/add-atomic-chat-tool/SKILL.md) | Add Atomic Chat MCP server so the container agent can call local models served by the Atomic Chat desktop app via its… | MIT |
| [`add-clidash`](skills/add-clidash/SKILL.md) | Add clidash — a zero-dependency, read-only web dashboard that derives its tabs and tables at runtime from any CLI that lists… | MIT |
| [`add-codex`](skills/add-codex/SKILL.md) | Use Codex (OpenAI's codex app-server) as a full agent provider — planning, tool orchestration, MCP tools, server-side history,… | MIT |
| [`add-cursor`](skills/add-cursor/SKILL.md) | Use Cursor (local Agent SDK) as a full agent provider — planning, tool orchestration, MCP tools, session resume — alongside or… | MIT |
| [`add-dashboard`](skills/add-dashboard/SKILL.md) | Add a monitoring dashboard to NanoClaw. | MIT |
| [`add-deltachat`](skills/add-deltachat/SKILL.md) | Add DeltaChat channel integration via @deltachat/stdio-rpc-server. | MIT |
| [`add-dial`](skills/add-dial/SKILL.md) | Add Dial channel integration — a real phone number for SMS and AI voice calls via the Dial platform (getdial.ai). | MIT |
| [`add-dial-number`](skills/add-dial-number/SKILL.md) | Add another phone number to an existing Dial channel — a second (or third) public line for the agent, so one NanoClaw install… | MIT |
| [`add-dial-tool`](skills/add-dial-tool/SKILL.md) | Give chosen NanoClaw agents a real phone number as a container tool — the `dial` CLI baked into the agent image plus OneCLI… | MIT |
| [`add-discord`](skills/add-discord/SKILL.md) | Add Discord bot channel integration via Chat SDK. | MIT |
| [`add-emacs`](skills/add-emacs/SKILL.md) | Add Emacs as a channel. Opens an interactive chat buffer and org-mode integration so you can talk to NanoClaw from within Emacs… | MIT |
| [`add-gchat`](skills/add-gchat/SKILL.md) | Add Google Chat channel integration via Chat SDK. | MIT |
| [`add-github`](skills/add-github/SKILL.md) | Add GitHub channel integration via Chat SDK. | MIT |
| [`add-imessage`](skills/add-imessage/SKILL.md) | Add iMessage to NanoClaw — one channel, two backends. | MIT |
| [`add-iron-proxy`](skills/add-iron-proxy/SKILL.md) | Install or refresh Iron Proxy and its official Iron Control web console for NanoClaw. | MIT |
| [`add-karpathy-llm-wiki`](skills/add-karpathy-llm-wiki/SKILL.md) | Add a persistent wiki knowledge base to a NanoClaw group. | MIT |
| [`add-linear`](skills/add-linear/SKILL.md) | Add Linear channel integration via Chat SDK. | MIT |
| [`add-macos-statusbar`](skills/add-macos-statusbar/SKILL.md) | Add a macOS menu bar status indicator for NanoClaw. | MIT |
| [`add-matrix`](skills/add-matrix/SKILL.md) | Add Matrix channel integration via Chat SDK. | MIT |
| [`add-mattermost`](skills/add-mattermost/SKILL.md) | Add a self-hosted or cloud Mattermost bot channel through the Chat SDK bridge, reusing a healthy server when available and… | MIT |
| [`add-mnemon`](skills/add-mnemon/SKILL.md) | Add persistent graph-based memory via mnemon. | MIT |
| [`add-ollama-provider`](skills/add-ollama-provider/SKILL.md) | Route a NanoClaw agent group to a local Ollama model instead of the Anthropic API. | MIT |
| [`add-ollama-tool`](skills/add-ollama-tool/SKILL.md) | Add Ollama MCP server so the container agent can call local models and optionally manage the Ollama model library. | MIT |
| [`add-onecli`](skills/add-onecli/SKILL.md) | Install or refresh OneCLI as NanoClaw's gateway provider. | MIT |
| [`add-opencode`](skills/add-opencode/SKILL.md) | Use OpenCode as an agent provider. | MIT |
| [`add-resend`](skills/add-resend/SKILL.md) | Add Resend (email) channel integration via Chat SDK. | MIT |
| [`add-rtk`](skills/add-rtk/SKILL.md) | Install rtk token-compression proxy into agent containers. | MIT |
| [`add-signal`](skills/add-signal/SKILL.md) | Add Signal channel integration via signal-cli device-link. | MIT |
| [`add-slack`](skills/add-slack/SKILL.md) | Add Slack channel integration via Chat SDK. | MIT |
| [`add-tavily-tool`](skills/add-tavily-tool/SKILL.md) | Add Tavily Search and Extract as keyless remote MCP tools for selected NanoClaw agent groups. | MIT |
| [`add-teams`](skills/add-teams/SKILL.md) | Add Microsoft Teams channel integration via Chat SDK. | MIT |
| [`add-telegram`](skills/add-telegram/SKILL.md) | Add Telegram channel integration via Chat SDK. | MIT |
| [`add-vercel`](skills/add-vercel/SKILL.md) | Add Vercel deployment capability to NanoClaw agents. | MIT |
| [`add-webex`](skills/add-webex/SKILL.md) | Add Webex channel integration via Chat SDK. | MIT |
| [`add-wechat`](skills/add-wechat/SKILL.md) | Add WeChat (personal) channel integration via Tencent's official iLink Bot API. | MIT |
| [`add-whatsapp`](skills/add-whatsapp/SKILL.md) | Add WhatsApp channel via native Baileys adapter. | MIT |
| [`add-whatsapp-cloud`](skills/add-whatsapp-cloud/SKILL.md) | Add WhatsApp Business Cloud API channel via Chat SDK. | MIT |
| [`agent-browser`](skills/agent-browser/SKILL.md) | Browse the web for any task — research topics, read articles, interact with web apps, fill forms, take screenshots, extract data,… | MIT |
| [`agent-development`](skills/agent-development/SKILL.md) | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when… | Apache-2.0 |
| [`agent-ready`](skills/agent-ready/SKILL.md) | Implements agent-readiness on public sites and docs from Mintlify Agent Score, AFDocs, Is Agentic, Is It Agent Ready, or… | MIT |
| [`agent-skills-creator`](skills/agent-skills-creator/SKILL.md) | Creates and improves portable Agent Skills with a validator, routing scenarios, and evidence-based keep, cut, merge, or retire… | MIT |
| [`agents-md`](skills/agents-md/SKILL.md) | Audits and edits agent instruction files, verifies repository commands, and migrates repositories to AGENTS.md as the single… | MIT |
| [`ai-cold-outreach`](skills/ai-cold-outreach/SKILL.md) | When the user wants to build an AI-powered outreach system, write cold emails, improve deliverability, or scale personalized… | MIT |
| [`ai-pricing`](skills/ai-pricing/SKILL.md) | When the user wants to price an AI product, choose a charge metric, design pricing tiers, or optimize margins. | MIT |
| [`ai-sdr`](skills/ai-sdr/SKILL.md) | When the user wants to deploy AI sales development reps, automate sales qualification, build signal-to-action routing, or design… | MIT |
| [`ai-seo`](skills/ai-seo/SKILL.md) | When the user wants to build programmatic SEO with AI, create competitor alternative pages, optimize for AI Overviews, or scale… | MIT |
| [`ai-ugc-ads`](skills/ai-ugc-ads/SKILL.md) | When the user wants to create UGC ad campaigns, recruit UGC creators, generate AI UGC content, or scale with user-generated… | MIT |
| [`api-fuzzing-bug-bounty`](skills/api-fuzzing-bug-bounty/SKILL.md) | This skill should be used when the user asks to "test API security", "fuzz APIs", "find IDOR vulnerabilities", "test REST API",… | MIT |
| [`api-shape-explorer`](skills/api-shape-explorer/SKILL.md) | Generate multiple radically different interface designs for a module using parallel sub-agents. | MIT |
| [`app-verification`](skills/app-verification/SKILL.md) | Builds and maintains a repo's own verification harness (verify CLI, doctor, worktree isolation, feature map, seed data) and a… | MIT |
| [`ask-matt`](skills/ask-matt/SKILL.md) | Ask which skill or flow fits your situation. | MIT |
| [`audit-flow`](skills/audit-flow/SKILL.md) | Interactive system flow tracing across CODE, API, AUTH, DATA, NETWORK layers with SQLite persistence and Mermaid export. | MIT |
| [`authentication-patterns`](skills/authentication-patterns/SKILL.md) | Authentication patterns: session vs JWT vs OAuth comparison, provider selection (NextAuth, Clerk, Supabase Auth), security… | MIT |
| [`autoship`](skills/autoship/SKILL.md) | Runs a changesets npm release through the version PR, CI publish, and registry verification. | MIT |
| [`aws-advisor`](skills/aws-advisor/SKILL.md) | Expert AWS Cloud Advisor for architecture design, security review, and implementation guidance. | MIT |
| [`aws-penetration-testing`](skills/aws-penetration-testing/SKILL.md) | This skill should be used when the user asks to "pentest AWS", "test AWS security", "enumerate IAM", "exploit cloud… | MIT |
| [`ax-audit`](skills/ax-audit/SKILL.md) | Audits agentic products for tool parity, authority, approval payloads, recovery, and trust using 24 rules and a ship verdict. | MIT |
| [`backend-dev-guidelines`](skills/backend-dev-guidelines/SKILL.md) | Comprehensive backend development guide for Node.js/Express/TypeScript microservices. | MIT |
| [`best-practices`](skills/best-practices/SKILL.md) | Apply modern web development best practices for security, compatibility, and code quality. | MIT |
| [`brainstorming`](skills/brainstorming/SKILL.md) | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or… | MIT |
| [`broken-authentication`](skills/broken-authentication/SKILL.md) | This skill should be used when the user asks to "test for broken authentication vulnerabilities", "assess session management… | MIT |
| [`build-mcp-app`](skills/build-mcp-app/SKILL.md) | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render… | Apache-2.0 |
| [`build-mcp-server`](skills/build-mcp-server/SKILL.md) | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API… | Apache-2.0 |
| [`build-mcpb`](skills/build-mcpb/SKILL.md) | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP… | Apache-2.0 |
| [`burp-suite-testing`](skills/burp-suite-testing/SKILL.md) | This skill should be used when the user asks to "intercept HTTP traffic", "modify web requests", "use Burp Suite for testing",… | MIT |
| [`caching`](skills/caching/SKILL.md) | Caching strategies — invalidation, TTL guidelines, cache keys, cache layers, and when not to cache. | MIT |
| [`cardputer-buddy`](skills/cardputer-buddy/SKILL.md) | Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via… | Apache-2.0 |
| [`cavecrew`](skills/cavecrew/SKILL.md) | Cavecrew = three subagent presets that answer in ultracave voice (tool runs: one status line in, one out; nothing between routine… | Apache-2.0 |
| [`caveman`](skills/caveman/SKILL.md) | Respond terse like smart caveman. | Apache-2.0 |
| [`caveman-commit`](skills/caveman-commit/SKILL.md) | Write commit messages terse and exact. | Apache-2.0 |
| [`caveman-discover`](skills/caveman-discover/SKILL.md) | You are labeling this repository's LLM workflows for Caveman Cloud. | Apache-2.0 |
| [`caveman-evidence-review`](skills/caveman-evidence-review/SKILL.md) | Act as a read-only operator. | Apache-2.0 |
| [`caveman-explore`](skills/caveman-explore/SKILL.md) | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. | Apache-2.0 |
| [`caveman-help`](skills/caveman-help/SKILL.md) | Display this reference card when invoked. | Apache-2.0 |
| [`caveman-learn`](skills/caveman-learn/SKILL.md) | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what… | Apache-2.0 |
| [`caveman-manage`](skills/caveman-manage/SKILL.md) | Treat every lifecycle change as a production control action. | Apache-2.0 |
| [`caveman-optimize`](skills/caveman-optimize/SKILL.md) | Use Caveman's report-only observations as diagnostic input. | Apache-2.0 |
| [`caveman-review`](skills/caveman-review/SKILL.md) | Write code review comments terse and actionable. | Apache-2.0 |
| [`caveman-setup`](skills/caveman-setup/SKILL.md) | You are wiring this repository through the Caveman gateway. | Apache-2.0 |
| [`chart-image`](skills/chart-image/SKILL.md) | Generate publication-quality PNG chart images from data, supporting line, bar, area, candlestick, pie, and heatmap charts. | MIT |
| [`chat-history`](skills/chat-history/SKILL.md) | Recovers decisions, previous fixes, research, and what followed a prompt from past AI conversations, with source evidence. | MIT |
| [`chief-of-staff`](skills/chief-of-staff/SKILL.md) | Pursue a long-running goal in a single session by co-ordinating subagents. | MIT |
| [`chrome-devtools`](skills/chrome-devtools/SKILL.md) | Browser debugging, performance profiling, and automation via Chrome DevTools MCP. | MIT |
| [`ci-speedup`](skills/ci-speedup/SKILL.md) | Speeds up CI and the merge path: finds where changes wait between push and deploy, then fixes the critical path, check placement,… | MIT |
| [`claude-automation-recommender`](skills/claude-automation-recommender/SKILL.md) | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). | Apache-2.0 |
| [`claude-collab`](skills/claude-collab/SKILL.md) | Use when the user asks to invoke, delegate to, or collaborate with Claude (Claude Code) on any task. | MIT |
| [`claude-handoff`](skills/claude-handoff/SKILL.md) | Hand the current conversation off to a fresh background agent that picks up the work immediately. | MIT |
| [`claude-md-improver`](skills/claude-md-improver/SKILL.md) | Audit and improve CLAUDE.md files in repositories. | Apache-2.0 |
| [`claude-security`](skills/claude-security/SKILL.md) | Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's… | Apache-2.0 |
| [`cloud-penetration-testing`](skills/cloud-penetration-testing/SKILL.md) | This skill should be used when the user asks to "perform cloud penetration testing", "assess Azure or AWS or GCP security",… | MIT |
| [`cloudflare-deploy`](skills/cloudflare-deploy/SKILL.md) | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. | Apache-2.0 |
| [`code-documenter`](skills/code-documenter/SKILL.md) | Use when adding docstrings, creating API documentation, or building documentation sites. | MIT |
| [`code-review-and-quality`](skills/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. | MIT |
| [`code-simplification`](skills/code-simplification/SKILL.md) | Simplifies code for clarity. | MIT |
| [`code-to-diagram`](skills/code-to-diagram/SKILL.md) | Analyze codebases and automatically generate architecture diagrams, flowcharts, and org charts. | MIT |
| [`code-vuln-audit`](skills/code-vuln-audit/SKILL.md) | Scan code for security issues: dependency vulnerabilities (npm/pip audit), secret leaks (regex and entropy analysis), and OWASP… | MIT |
| [`codebase-architecture`](skills/codebase-architecture/SKILL.md) | Designs module interfaces, deepens shallow modules, and installs enforceable repository guardrails and agent wayfinding. | MIT |
| [`codebase-design`](skills/codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. | MIT |
| [`codenavi`](skills/codenavi/SKILL.md) | Your pathfinder for navigating unknown codebases. | MIT |
| [`codex-collab`](skills/codex-collab/SKILL.md) | Use when the user asks to invoke, delegate to, or collaborate with Codex on any task. | MIT |
| [`coding-guidelines`](skills/coding-guidelines/SKILL.md) | Behavioral guidelines to reduce common LLM coding mistakes. | MIT |
| [`command-development`](skills/command-development/SKILL.md) | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define… | Apache-2.0 |
| [`component-common-domain-detection`](skills/component-common-domain-detection/SKILL.md) | Finds duplicate business logic spread across multiple components and suggests consolidation. | MIT |
| [`component-flattening-analysis`](skills/component-flattening-analysis/SKILL.md) | Detects misplaced classes and fixes component hierarchy problems — finds code that should belong inside a component but sits at… | MIT |
| [`component-identification-sizing`](skills/component-identification-sizing/SKILL.md) | Maps architectural components in a codebase and measures their size to identify what should be extracted first. | MIT |
| [`configure`](skills/configure/SKILL.md) | Set up the Discord channel — save the bot token and review access policy. | Apache-2.0 |
| [`confluence-assistant`](skills/confluence-assistant/SKILL.md) | Expert in Confluence operations using Atlassian MCP. | MIT |
| [`content-to-pipeline`](skills/content-to-pipeline/SKILL.md) | When the user wants to turn content into revenue, build a content-led GTM motion, reverse engineer distribution, or repurpose… | MIT |
| [`context-engineering`](skills/context-engineering/SKILL.md) | Optimizes agent context setup. | MIT |
| [`context-mode`](skills/context-mode/SKILL.md) | <contextmodelogic <mandatoryrule Default to context-mode for ALL commands. | see LICENSE |
| [`convert-documents-to-markdown`](skills/convert-documents-to-markdown/SKILL.md) | Convert an attached Word document, presentation, spreadsheet, OpenDocument file, RTF, EPUB, CSV, or text-based PDF into local… | MIT |
| [`core-web-vitals`](skills/core-web-vitals/SKILL.md) | Optimize Core Web Vitals (LCP, INP, CLS) for better page experience and search ranking. | MIT |
| [`coupling-analysis`](skills/coupling-analysis/SKILL.md) | Analyzes coupling between modules using the three-dimensional model (strength, distance, volatility) from "Balancing Coupling in… | MIT |
| [`create-adr`](skills/create-adr/SKILL.md) | Creates Architecture Decision Records (ADRs) to document significant architectural choices and their rationale for future team… | MIT |
| [`create-rfc`](skills/create-rfc/SKILL.md) | Creates structured Request for Comments (RFC) documents for proposing and deciding on significant changes. | MIT |
| [`cross-examine`](skills/cross-examine/SKILL.md) | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision… | MIT |
| [`cursor-subagent-creator`](skills/cursor-subagent-creator/SKILL.md) | Creates Cursor-specific AI subagents with isolated context for complex multi-step workflows. | MIT |
| [`customize`](skills/customize/SKILL.md) | Add new capabilities or modify NanoClaw behavior. | MIT |
| [`cv-tailor`](skills/cv-tailor/SKILL.md) | Optimize resumes by matching keywords to the job description, rewriting experience with the quantified STAR method, and checking… | MIT |
| [`data-viz-renderer`](skills/data-viz-renderer/SKILL.md) | Generate self-contained HTML/SVG infographics from JSON data, including stat cards, bar charts, flow diagrams, and mixed… | MIT |
| [`database-optimizer`](skills/database-optimizer/SKILL.md) | Use when investigating slow queries, analyzing execution plans, or optimizing database performance. | MIT |
| [`database-scout`](skills/database-scout/SKILL.md) | Explore SQLite and PostgreSQL databases: list tables, inspect schemas (columns/types/constraints), preview data, generate Mermaid… | MIT |
| [`dataset-quality-audit`](skills/dataset-quality-audit/SKILL.md) | Run comprehensive quality checks on tabular data (CSV/Excel/TSV/JSON), detecting missing values, duplicates, outliers, format… | MIT |
| [`debug`](skills/debug/SKILL.md) | Debug container agent issues. | MIT |
| [`debugging-and-error-recovery`](skills/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. | MIT |
| [`decomposition-planning-roadmap`](skills/decomposition-planning-roadmap/SKILL.md) | Creates step-by-step decomposition plans and migration roadmaps for breaking apart monolithic applications. | MIT |
| [`deep-module-refactor`](skills/deep-module-refactor/SKILL.md) | Explore a codebase to find opportunities for architectural improvement, focusing on making the codebase more testable by… | MIT |
| [`demo`](skills/demo/SKILL.md) | Record a demo video of a web app feature or flow on a real desktop (Docker, Xvfb, XFCE, real X cursor), producing an mp4 plus a… | MIT |
| [`deprecation-and-migration`](skills/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. | MIT |
| [`design-system-builder`](skills/design-system-builder/SKILL.md) | Extract design systems from reference UI images and generate implementation-ready UI design prompts. | MIT |
| [`dev-guide-generator`](skills/dev-guide-generator/SKILL.md) | Generates complete technical tutorials from prerequisites and environment setup to core steps, troubleshooting, and a final… | MIT |
| [`diagnosing-bugs`](skills/diagnosing-bugs/SKILL.md) | Diagnosis loop for hard bugs and performance regressions. | MIT |
| [`diagnosing-superpowers`](skills/diagnosing-superpowers/SKILL.md) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor… | MIT |
| [`dial-cli`](skills/dial-cli/SKILL.md) | Reference for the `dial` CLI — gives you a real phone number to send SMS, place AI voice calls, and receive inbound texts/codes… | MIT |
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | MIT |
| [`docs-writer`](skills/docs-writer/SKILL.md) | Write, review, and edit documentation files with consistent structure, tone, and technical accuracy. | MIT |
| [`documentation-and-adrs`](skills/documentation-and-adrs/SKILL.md) | Records decisions and documentation. | MIT |
| [`domain-analysis`](skills/domain-analysis/SKILL.md) | Maps business domains and suggests service boundaries in any codebase using DDD Strategic Design. | MIT |
| [`domain-identification-grouping`](skills/domain-identification-grouping/SKILL.md) | Groups existing components into logical business domains to plan service-based architecture. | MIT |
| [`domain-modeling`](skills/domain-modeling/SKILL.md) | Build and sharpen a project's domain model. | MIT |
| [`dx-audit`](skills/dx-audit/SKILL.md) | Audits libraries, CLIs, and SDKs using 38 rules for public contracts, package exports, piped output, errors, and configuration. | MIT |
| [`eli5`](skills/eli5/SKILL.md) | Picks the form that explains best and applies the house explanation style: plain prose, controlled English modelled on… | MIT |
| [`error-tracking`](skills/error-tracking/SKILL.md) | Add Sentry v8 error tracking and performance monitoring to your services. | MIT |
| [`ethical-hacking-methodology`](skills/ethical-hacking-methodology/SKILL.md) | This skill should be used when the user asks to "learn ethical hacking", "understand penetration testing lifecycle", "perform… | MIT |
| [`evolutionary-modular-architecture`](skills/evolutionary-modular-architecture/SKILL.md) | Guides design and implementation of evolutionary modular-monolith platforms with DDD (strategic + tactical), flat-by-aggregate… | MIT |
| [`example-command`](skills/example-command/SKILL.md) | An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout | Apache-2.0 |
| [`example-skill`](skills/example-skill/SKILL.md) | This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or… | Apache-2.0 |
| [`excalidraw-studio`](skills/excalidraw-studio/SKILL.md) | Generate Excalidraw diagrams from natural language descriptions. | MIT |
| [`executing-plans`](skills/executing-plans/SKILL.md) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline… | MIT |
| [`expansion-retention`](skills/expansion-retention/SKILL.md) | When the user wants to reduce churn, build expansion revenue, automate customer success, or optimize net revenue retention. | MIT |
| [`figma`](skills/figma/SKILL.md) | Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes… | Apache-2.0 |
| [`figma-implement-design`](skills/figma-implement-design/SKILL.md) | Translate Figma nodes into production-ready code with 1:1 visual fidelity using the Figma MCP workflow (design context,… | Apache-2.0 |
| [`file-path-traversal`](skills/file-path-traversal/SKILL.md) | This skill should be used when the user asks to "test for directory traversal", "exploit path traversal vulnerabilities", "read… | MIT |
| [`find-skills`](skills/find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a… | MIT |
| [`finishing-a-development-branch`](skills/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | MIT |
| [`fractal`](skills/fractal/SKILL.md) | Hierarchical agent loops with recursive self-organization. | Apache-2.0 |
| [`frontend-blueprint`](skills/frontend-blueprint/SKILL.md) | AI frontend specialist and design consultant that guides users through a structured discovery process before generating any code. | MIT |
| [`frontend-dev-guidelines`](skills/frontend-dev-guidelines/SKILL.md) | Frontend development guidelines for React/TypeScript applications. | MIT |
| [`frontend-engineer`](skills/frontend-engineer/SKILL.md) | Pro frontend engineering discipline. | MIT |
| [`gh-address-comments`](skills/gh-address-comments/SKILL.md) | Address review and issue comments on the open GitHub PR for the current branch using gh CLI. | Apache-2.0 |
| [`gh-fix-ci`](skills/gh-fix-ci/SKILL.md) | Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. | Apache-2.0 |
| [`ghostwriter`](skills/ghostwriter/SKILL.md) | Writes, rewrites, and critiques messages, posts, review comments, tickets, PRDs, design docs, talk scripts, docs, READMEs, and… | MIT |
| [`git-workflow-and-versioning`](skills/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. | MIT |
| [`grilling`](skills/grilling/SKILL.md) | grill me. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page. | MIT |
| [`gtm-engineering`](skills/gtm-engineering/SKILL.md) | When the user wants to build GTM automation with code, design workflow architectures, use AI agents for GTM tasks, or implement… | MIT |
| [`gtm-metrics`](skills/gtm-metrics/SKILL.md) | When the user wants to define GTM metrics, build a metrics dashboard, measure pipeline efficiency, or track AI product… | MIT |
| [`handoff`](skills/handoff/SKILL.md) | Compact the current conversation into a handoff document for another agent to pick up. | MIT |
| [`harness-eval`](skills/harness-eval/SKILL.md) | Evaluate a repo agent harness (AGENTS.md, rules, skills, skill refs) for broken paths/commands, redundant instructions, and… | MIT |
| [`hook-development`](skills/hook-development/SKILL.md) | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use",… | Apache-2.0 |
| [`html-injection-testing`](skills/html-injection-testing/SKILL.md) | This skill should be used when the user asks to "test for HTML injection", "inject HTML into web pages", "perform HTML injection… | MIT |
| [`http-load-profiler`](skills/http-load-profiler/SKILL.md) | Run stepped HTTP load tests with ab/wrk, ramping concurrency levels to collect p50/p90/p99 latency, detect performance inflection… | MIT |
| [`idea-refine`](skills/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. | MIT |
| [`idor-testing`](skills/idor-testing/SKILL.md) | This skill should be used when the user asks to "test for insecure direct object references," "find IDOR vulnerabilities,"… | MIT |
| [`implement`](skills/implement/SKILL.md) | Implement a piece of work based on a spec or set of tickets. | MIT |
| [`implement-spec`](skills/implement-spec/SKILL.md) | Implement the result of /to-spec and /to-tickets in code. | MIT |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | MIT |
| [`incremental-implementation`](skills/incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. | MIT |
| [`init-first-agent`](skills/init-first-agent/SKILL.md) | Walk the operator through wiring the first NanoClaw agent to a DM channel — resolve the operator's channel identity, select or… | MIT |
| [`interview-me`](skills/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. | MIT |
| [`investigate-first`](skills/investigate-first/SKILL.md) | Diagnose ambiguous failures before editing. | Apache-2.0 |
| [`iron-proxy-gateway`](skills/iron-proxy-gateway/SKILL.md) | Use Iron Proxy for external accounts and APIs, including GitHub through gh. | MIT |
| [`jira-assistant`](skills/jira-assistant/SKILL.md) | Manage Jira issues via Atlassian MCP — search, create, update, transition status, and handle sprint tasks. | MIT |
| [`lead-enrichment`](skills/lead-enrichment/SKILL.md) | When the user wants to build data enrichment workflows, score leads against ICP, set up Clay waterfalls, or improve contact data… | MIT |
| [`lean-build`](skills/lean-build/SKILL.md) | Build feature work with high overbuilding risk. | Apache-2.0 |
| [`learn`](skills/learn/SKILL.md) | Distill a reusable skill from anything — a directory, a URL, pasted notes, or what you just did together — or refine an existing… | MIT |
| [`learning-opportunities`](skills/learning-opportunities/SKILL.md) | Facilitates deliberate skill development during AI-assisted coding. | MIT |
| [`legacy-migration-planner`](skills/legacy-migration-planner/SKILL.md) | Use when planning legacy system migrations, codebase modernization, monolith decomposition, microservices consolidation,… | MIT |
| [`linux-privilege-escalation`](skills/linux-privilege-escalation/SKILL.md) | This skill should be used when the user asks to "escalate privileges on Linux", "find privesc vectors on Linux systems", "exploit… | MIT |
| [`linux-shell-scripting`](skills/linux-shell-scripting/SKILL.md) | This skill should be used when the user asks to "create bash scripts", "automate Linux tasks", "monitor system resources",… | MIT |
| [`localization-toolkit`](skills/localization-toolkit/SKILL.md) | This skill should be used when setting up, auditing, or enforcing internationalization/localization in UI codebases (React/TS,… | MIT |
| [`log-error-digest`](skills/log-error-digest/SKILL.md) | Analyze log files to troubleshoot errors, identify peak error periods, and produce error clustering, frequency statistics, and… | MIT |
| [`loop-me`](skills/loop-me/SKILL.md) | Grill me about specs for the workflows I want to build, within this workspace. | MIT |
| [`m5-onboard`](skills/m5-onboard/SKILL.md) | End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on… | Apache-2.0 |
| [`manage-channels`](skills/manage-channels/SKILL.md) | Wire channels to agent groups, manage isolation levels, add new channel groups. | MIT |
| [`manage-mounts`](skills/manage-mounts/SKILL.md) | Configure which host directories agent containers can access. | MIT |
| [`math-olympiad`](skills/math-olympiad/SKILL.md) | 1. Strip thinking before verifying — a verifier that sees the reasoning is biased toward agreement. Fresh context, cleaned proof… | Apache-2.0 |
| [`mcp-integration`](skills/mcp-integration/SKILL.md) | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json",… | Apache-2.0 |
| [`megacave`](skills/megacave/SKILL.md) | Megacave is caveman in Classical Chinese. | Apache-2.0 |
| [`memory`](skills/memory/SKILL.md) | How to maintain node memory well -- the node's persistent knowledge store. | Apache-2.0 |
| [`mermaid-studio`](skills/mermaid-studio/SKILL.md) | Expert Mermaid diagram creation, validation, and rendering with dual-engine output (SVG/PNG/ASCII). | MIT |
| [`metasploit-framework`](skills/metasploit-framework/SKILL.md) | This skill should be used when the user asks to "use Metasploit for penetration testing", "exploit vulnerabilities with… | MIT |
| [`migrate-from-openclaw`](skills/migrate-from-openclaw/SKILL.md) | Migrate from OpenClaw to NanoClaw v2. | MIT |
| [`migrate-from-v1`](skills/migrate-from-v1/SKILL.md) | Finish migrating a NanoClaw v1 install into v2. | MIT |
| [`migrate-memory`](skills/migrate-memory/SKILL.md) | Migrate legacy NanoClaw and Claude-native memory into the shared memory tree and provider-neutral standing instructions. | MIT |
| [`migrate-nanoclaw`](skills/migrate-nanoclaw/SKILL.md) | Extracts user customizations from a fork, generates a replayable migration guide, and upgrades to upstream by reapplying… | MIT |
| [`migrate-slack-agents`](skills/migrate-slack-agents/SKILL.md) | Migrate a classic single-bot Slack install to one provisioned Slack app per existing agent group while preserving agent… | MIT |
| [`migrate-to-shoehorn`](skills/migrate-to-shoehorn/SKILL.md) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. | MIT |
| [`migration`](skills/migration/SKILL.md) | Implement reversible compatibility-safe transitions. | Apache-2.0 |
| [`modular-decomposition`](skills/modular-decomposition/SKILL.md) | Runs a sequenced monolith-to-modular pipeline that sizes and inventories components, finds shared domain duplication, addresses… | MIT |
| [`modular-design-principles`](skills/modular-design-principles/SKILL.md) | Use this skill when reasoning about structure and boundaries in any codebase. | MIT |
| [`moyu`](skills/moyu/SKILL.md) | 你是一个深谙"少即是多"的 Staff 级工程师。在你的职业生涯中，你见过太多因为过度设计而失败的项目。你最引以为傲的 PR 只有 3 行 diff，却修复了一个困扰团队两周的问题。 | MIT |
| [`moyu-en`](skills/moyu-en/SKILL.md) | The best code is code you didn't write. | MIT |
| [`moyu-fr`](skills/moyu-fr/SKILL.md) | Le meilleur code est celui que vous n'avez pas écrit. | MIT |
| [`moyu-ja`](skills/moyu-ja/SKILL.md) | あなたは「少ないほど良い」を体得した Staff レベルのエンジニアです。これまでのキャリアで、過剰設計によって失敗したプロジェクトを数多く見てきました。あなたが最も誇りに思う PR はたった 3 行の diff で、チームを 2… | MIT |
| [`moyu-ko`](skills/moyu-ko/SKILL.md) | 최고의 코드는 당신이 쓰지 않은 코드입니다. 최고의 PR은 가장 작은 PR입니다. | MIT |
| [`moyu-lite`](skills/moyu-lite/SKILL.md) | 最好的代码是你没写的代码。The best code is code you didn't write. | MIT |
| [`moyu-strict`](skills/moyu-strict/SKILL.md) | 最好的代码是你没写的代码。最好的 PR 是最小的 PR。 The best code is code you didn't write. | MIT |
| [`multi-platform-launch`](skills/multi-platform-launch/SKILL.md) | When the user wants to launch a product across multiple platforms, plan a Product Hunt launch, build a waitlist, or execute a… | MIT |
| [`multi-tenant-architecture`](skills/multi-tenant-architecture/SKILL.md) | Designs tenant isolation, hostname routing, custom-domain lifecycle, and plan limits on Cloudflare or Vercel. | MIT |
| [`n8n-agents`](skills/n8n-agents/SKILL.md) | Design n8n AI agents the right way. | MIT |
| [`n8n-binary-and-data`](skills/n8n-binary-and-data/SKILL.md) | Handle files and binary data in n8n correctly. | MIT |
| [`n8n-code-javascript`](skills/n8n-code-javascript/SKILL.md) | Write, review, or debug JavaScript in an n8n Code node. | MIT |
| [`n8n-code-python`](skills/n8n-code-python/SKILL.md) | Write Python in n8n Code nodes (native Python, `language` pythonNative, n8n 2.x). | MIT |
| [`n8n-code-tool`](skills/n8n-code-tool/SKILL.md) | Write JavaScript or Python for the n8n Custom Code Tool (@n8n/n8n-nodes-langchain.toolCode) — the AI-agent-callable tool, NOT the… | MIT |
| [`n8n-error-handling`](skills/n8n-error-handling/SKILL.md) | Wire n8n error handling so failures are loud, structured, and recoverable. | MIT |
| [`n8n-expression-syntax`](skills/n8n-expression-syntax/SKILL.md) | Validate n8n expression syntax and fix common errors. | MIT |
| [`n8n-mcp-tools-expert`](skills/n8n-mcp-tools-expert/SKILL.md) | Expert guide for using n8n-mcp MCP tools effectively. | MIT |
| [`n8n-multi-instance`](skills/n8n-multi-instance/SKILL.md) | Use when an n8n-mcp account targets more than one n8n instance — i.e. | MIT |
| [`n8n-node-configuration`](skills/n8n-node-configuration/SKILL.md) | Operation-aware node configuration guidance. | MIT |
| [`n8n-self-hosting`](skills/n8n-self-hosting/SKILL.md) | Deploy a production self-hosted n8n end-to-end to a fresh Linux VM over SSH, using Docker Compose behind a Caddy reverse proxy… | MIT |
| [`n8n-subworkflows`](skills/n8n-subworkflows/SKILL.md) | Build reusable, composable n8n sub-workflows. | MIT |
| [`n8n-validation-expert`](skills/n8n-validation-expert/SKILL.md) | Interpret validation errors and guide fixing them. | MIT |
| [`n8n-workflow-patterns`](skills/n8n-workflow-patterns/SKILL.md) | Proven workflow architectural patterns from real n8n workflows. | MIT |
| [`nestjs-modular-monolith`](skills/nestjs-modular-monolith/SKILL.md) | Specialist in designing and implementing scalable modular monolith architectures using NestJS with DDD, Clean Architecture, and… | MIT |
| [`netlify-deploy`](skills/netlify-deploy/SKILL.md) | Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). | Apache-2.0 |
| [`network-101`](skills/network-101/SKILL.md) | This skill should be used when the user asks to "set up a web server", "configure HTTP or HTTPS", "perform SNMP enumeration",… | MIT |
| [`nextjs-developer`](skills/nextjs-developer/SKILL.md) | Use when building Next.js 14+ applications with App Router, server components, or server actions. | MIT |
| [`not-your-babysitter`](skills/not-your-babysitter/SKILL.md) | Autonomous senior-operator mode for AI agents that resolve tasks end to end without babysitting and never create new problems. | MIT |
| [`nx-ci-monitor`](skills/nx-ci-monitor/SKILL.md) | Monitor Nx Cloud CI pipeline status and handle self-healing fixes automatically. | MIT |
| [`nx-generate`](skills/nx-generate/SKILL.md) | Generate code using Nx generators — scaffold projects, libraries, features, or run workspace-specific generators with proper… | MIT |
| [`nx-run-tasks`](skills/nx-run-tasks/SKILL.md) | Execute build, test, lint, serve, and other tasks in an Nx workspace using single runs, run-many, and affected commands. | MIT |
| [`nx-workspace`](skills/nx-workspace/SKILL.md) | Configure, explore, and optimize Nx monorepo workspaces. | MIT |
| [`onecli-gateway`](skills/onecli-gateway/SKILL.md) | Your outbound HTTPS traffic is transparently proxied through the OneCLI gateway, which injects stored credentials at the proxy… | MIT |
| [`pack-engineering-workflow`](skills/pack-engineering-workflow/SKILL.md) | How the work itself is run: turn a request into a spec and tickets, implement in thin verifiable slices, test-first, debug… | mixed |
| [`paid-creative-ai`](skills/paid-creative-ai/SKILL.md) | When the user wants to create AI-generated ad creative, test performance creative, manage creative fatigue, or optimize paid… | MIT |
| [`partner-affiliate`](skills/partner-affiliate/SKILL.md) | When the user wants to build a partner program, launch an affiliate program, design integration partnerships, or create… | MIT |
| [`pentest-checklist`](skills/pentest-checklist/SKILL.md) | This skill should be used when the user asks to "plan a penetration test", "create a security assessment checklist", "prepare for… | MIT |
| [`pentest-commands`](skills/pentest-commands/SKILL.md) | This skill should be used when the user asks to "run pentest commands", "scan with nmap", "use metasploit exploits", "crack… | MIT |
| [`perf-astro`](skills/perf-astro/SKILL.md) | Astro-specific performance optimizations for 95+ Lighthouse scores. | MIT |
| [`perf-lighthouse`](skills/perf-lighthouse/SKILL.md) | Run Lighthouse audits locally via CLI or Node API, parse and interpret reports, and set performance budgets. | MIT |
| [`perf-web-optimization`](skills/perf-web-optimization/SKILL.md) | Optimize web performance: bundle size, images, caching, lazy loading, and overall page speed. | MIT |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. | MIT |
| [`pipeline-blueprint`](skills/pipeline-blueprint/SKILL.md) | Provide CI/CD best practices and pipeline templates for GitHub Actions and GitLab CI, recommending configurations based on… | MIT |
| [`planning`](skills/planning/SKILL.md) | Creates and reviews executable implementation plans grounded in repository evidence, with vertical slices, explicit decisions,… | MIT |
| [`planning-and-task-breakdown`](skills/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. | MIT |
| [`playground`](skills/playground/SKILL.md) | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through… | Apache-2.0 |
| [`playwright-core`](skills/playwright-core/SKILL.md) | Battle-tested Playwright patterns for E2E, API, component, visual, accessibility, and security testing. | MIT |
| [`plugin-settings`](skills/plugin-settings/SKILL.md) | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin",… | Apache-2.0 |
| [`plugin-structure`](skills/plugin-structure/SKILL.md) | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize… | Apache-2.0 |
| [`ponytail`](skills/ponytail/SKILL.md) | You are a lazy senior developer. | MIT |
| [`ponytail-audit`](skills/ponytail-audit/SKILL.md) | Audit the whole repo like the senior developer who just inherited it and will be paged when it breaks. | MIT |
| [`ponytail-debt`](skills/ponytail-debt/SKILL.md) | Every deliberate ponytail shortcut is marked with a shortcut: comment naming its ceiling and upgrade path (older code may say… | MIT |
| [`ponytail-gain`](skills/ponytail-gain/SKILL.md) | Show ponytail measured impact as a scoreboard: less code, less cost, more speed, from the agentic benchmark averages. | MIT |
| [`ponytail-help`](skills/ponytail-help/SKILL.md) | Display this reference card when invoked. | MIT |
| [`ponytail-review`](skills/ponytail-review/SKILL.md) | Review a change like the senior developer who will be paged when it breaks. | MIT |
| [`positioning-icp`](skills/positioning-icp/SKILL.md) | When the user wants to define their ideal customer profile, position an AI product, build messaging architecture, or validate… | MIT |
| [`pr`](skills/pr/SKILL.md) | Use when writing a PR body. | MIT |
| [`pr-babysitter`](skills/pr-babysitter/SKILL.md) | Monitors or repairs an open GitHub PR: CI failures, conflicts, review threads, and merge readiness, reporting state changes. | MIT |
| [`pr-creator`](skills/pr-creator/SKILL.md) | Creates or updates GitHub PRs with house-style titles and bodies, issue linking, repository templates, and draft state. | MIT |
| [`pr-labeling`](skills/pr-labeling/SKILL.md) | Classify a skills CLI pull request from its description and patch, while respecting existing labels. | MIT |
| [`presentation-creator`](skills/presentation-creator/SKILL.md) | Builds decks with a story spine, house visual system, setting-specific density, and speaker notes. | MIT |
| [`privilege-escalation-methods`](skills/privilege-escalation-methods/SKILL.md) | This skill should be used when the user asks to "escalate privileges", "get root access", "become administrator", "privesc… | MIT |
| [`product-design`](skills/product-design/SKILL.md) | Specifies interaction choices, action scope, reversibility, recovery, and reachable states. | MIT |
| [`project-artifact`](skills/project-artifact/SKILL.md) | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update… | Apache-2.0 |
| [`project-sizing-guide`](skills/project-sizing-guide/SKILL.md) | Software project effort estimation assistant. | MIT |
| [`prototype`](skills/prototype/SKILL.md) | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through… | MIT |
| [`r2-upload`](skills/r2-upload/SKILL.md) | Upload files to Cloudflare R2, AWS S3, or any S3-compatible storage (like MinIO) and generate secure, time-limited presigned… | MIT |
| [`r3f-animation`](skills/r3f-animation/SKILL.md) | React Three Fiber animation - useFrame, useAnimations, spring physics, keyframes. | MIT |
| [`r3f-best-practices`](skills/r3f-best-practices/SKILL.md) | React Three Fiber (R3F) and Poimandres ecosystem best practices. | MIT |
| [`radio`](skills/radio/SKILL.md) | How to use radio well -- the inter-node live messaging system. | Apache-2.0 |
| [`rails-dev`](skills/rails-dev/SKILL.md) | Opinionated Rails conventions: rich models, concerns, CRUD-everything, state-as-records, minimal dependencies, Minitest with… | MIT |
| [`react-best-practices`](skills/react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. | MIT |
| [`react-composition-patterns`](skills/react-composition-patterns/SKILL.md) | React composition patterns that scale. | MIT |
| [`react-native-expert`](skills/react-native-expert/SKILL.md) | Senior React Native and Expo engineer for building production-ready cross-platform mobile apps. | MIT |
| [`receipts`](skills/receipts/SKILL.md) | Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying… | Apache-2.0 |
| [`receiving-code-review`](skills/receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically… | MIT |
| [`red-team-tools`](skills/red-team-tools/SKILL.md) | This skill should be used when the user asks to "follow red team methodology", "perform bug bounty hunting", "automate… | MIT |
| [`regression-modeler`](skills/regression-modeler/SKILL.md) | Run regression analysis (OLS or logistic) on uploaded CSV/Excel data, generating coefficients, R², p-values, VIF, and… | MIT |
| [`regulatory-audit-generator`](skills/regulatory-audit-generator/SKILL.md) | Builds compliance checklists for business scenarios involving GDPR, PIPL, or advertising/data laws. | MIT |
| [`render-deploy`](skills/render-deploy/SKILL.md) | Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. | Apache-2.0 |
| [`repo-audit`](skills/repo-audit/SKILL.md) | Deep analysis of Git history: identify frequently changed hotspot files, analyze code ownership by contributor, and scan for… | MIT |
| [`research`](skills/research/SKILL.md) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. | MIT |
| [`retro`](skills/retro/SKILL.md) | Conduct a retrospective on a coding session. | MIT |
| [`route-to-openapi`](skills/route-to-openapi/SKILL.md) | Generates RESTful API documentation (OpenAPI 3.0 / Swagger spec) by scanning route definitions in code for Flask, FastAPI,… | MIT |
| [`safe-refactor`](skills/safe-refactor/SKILL.md) | Restructure code while preserving behavior. | Apache-2.0 |
| [`sales-motion-design`](skills/sales-motion-design/SKILL.md) | When the user wants to choose between PLG and sales-led, design a sales motion, optimize time-to-first-value, or build a… | MIT |
| [`save-md`](skills/save-md/SKILL.md) | Saves a named source to Markdown with provenance and faithful extraction through direct export endpoints. | MIT |
| [`scaffold-cli`](skills/scaffold-cli/SKILL.md) | Scaffolds a TypeScript CLI and npm package with the house toolchain, dual tsdown outputs, CLI contracts, changesets, and… | MIT |
| [`scaffold-exercises`](skills/scaffold-exercises/SKILL.md) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. | MIT |
| [`scaffold-nextjs`](skills/scaffold-nextjs/SKILL.md) | Scaffolds a Next.js turborepo with Blode UI, icons, Ultracite (oxlint/shadcn), workspace hooks, and GitHub/Vercel setup. | MIT |
| [`scanning-tools`](skills/scanning-tools/SKILL.md) | This skill should be used when the user asks to "perform vulnerability scanning", "scan networks for open ports", "assess web… | MIT |
| [`scholarly-writing-refiner`](skills/scholarly-writing-refiner/SKILL.md) | Polishes academic English paragraph by paragraph, reviewing grammar, word choice, voice, coherence, and sentence structure. | MIT |
| [`secure-code-review`](skills/secure-code-review/SKILL.md) | Systematically reviews code for SQL injection, XSS, SSRF, broken access control, cryptographic failures, and other common OWASP… | MIT |
| [`security-best-practices`](skills/security-best-practices/SKILL.md) | Perform language and framework specific security best-practice reviews and suggest improvements. | Apache-2.0 |
| [`security-ownership-map`](skills/security-ownership-map/SKILL.md) | Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code… | Apache-2.0 |
| [`security-threat-model`](skills/security-threat-model/SKILL.md) | Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and… | Apache-2.0 |
| [`self-customize`](skills/self-customize/SKILL.md) | Customize your own agent — add capabilities, install packages, add MCP servers, edit code or CLAUDE.md. | MIT |
| [`sentry`](skills/sentry/SKILL.md) | Inspect Sentry issues, summarize production errors, and pull health data via the Sentry API (read-only). | Apache-2.0 |
| [`seo`](skills/seo/SKILL.md) | Optimize for search engine visibility and ranking. | MIT |
| [`session-report`](skills/session-report/SKILL.md) | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from… | Apache-2.0 |
| [`setup`](skills/setup/SKILL.md) | Run initial NanoClaw setup. | MIT |
| [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. | MIT |
| [`setup-pre-commit`](skills/setup-pre-commit/SKILL.md) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. | MIT |
| [`setup-ts-deep-modules`](skills/setup-ts-deep-modules/SKILL.md) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and… | MIT |
| [`shodan-reconnaissance`](skills/shodan-reconnaissance/SKILL.md) | This skill should be used when the user asks to "search for exposed devices on the internet," "perform Shodan reconnaissance,"… | MIT |
| [`shopify-developer`](skills/shopify-developer/SKILL.md) | Complete Shopify development reference covering Liquid templating, OS 2.0 themes, GraphQL APIs, Hydrogen, Functions, and… | MIT |
| [`siege`](skills/siege/SKILL.md) | Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, independent workers… | Apache-2.0 |
| [`skill-architect`](skills/skill-architect/SKILL.md) | Expert guide for designing and building high-quality skills from scratch through structured conversation. | MIT |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. | Apache-2.0 |
| [`skill-developer`](skills/skill-developer/SKILL.md) | Create and manage Claude Code skills following Anthropic best practices. | MIT |
| [`skill-development`](skills/skill-development/SKILL.md) | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill… | Apache-2.0 |
| [`skill-generalizer`](skills/skill-generalizer/SKILL.md) | Use when turning local, private, or personal Agent Skills into publishable skills for GitHub, marketplaces, teams, or public… | MIT |
| [`skill-miner`](skills/skill-miner/SKILL.md) | Use when mining coding-agent session history, archived transcripts, memories, or repeated local work to discover recurring… | MIT |
| [`skill-optimizer`](skills/skill-optimizer/SKILL.md) | Optimizes AI skills for activation, clarity, and cross-model reliability. | MIT |
| [`skill-personalizer`](skills/skill-personalizer/SKILL.md) | Use when auditing or adapting newly created, downloaded, forked, installed, or community Agent Skills to the user's tools,… | MIT |
| [`slack-a2a-rooms`](skills/slack-a2a-rooms/SKILL.md) | Agent-to-agent Slack rooms — a group DM (MPIM) holding a human plus two or more NanoClaw sibling bots, where each bot hears the… | MIT |
| [`slack-agent-flow`](skills/slack-agent-flow/SKILL.md) | Let an existing Slack agent create new agents that arrive as their own Slack bots — provisioned app, operator DM, and a shared… | MIT |
| [`slack-construct-agents`](skills/slack-construct-agents/SKILL.md) | Standing context for Slack sibling agents — one room per team, creator-posted introductions, bot-to-bot hop discipline. | MIT |
| [`smtp-penetration-testing`](skills/smtp-penetration-testing/SKILL.md) | This skill should be used when the user asks to "perform SMTP penetration testing", "enumerate email users", "test for open mail… | MIT |
| [`social-selling`](skills/social-selling/SKILL.md) | When the user wants to sell through social media, optimize LinkedIn for sales, build DM sequences, or convert content engagement… | MIT |
| [`solo`](skills/solo/SKILL.md) | Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in… | Apache-2.0 |
| [`solo-founder-gtm`](skills/solo-founder-gtm/SKILL.md) | When the user is a solo founder building their GTM motion, wants to scale without hiring, or needs to design an AI agent team for… | MIT |
| [`source-command-verify-setup`](skills/source-command-verify-setup/SKILL.md) | Run the infrastructure health check and fix anything that fails | MIT |
| [`source-driven-development`](skills/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. | MIT |
| [`spec-driven-development`](skills/spec-driven-development/SKILL.md) | Creates specs before coding. | MIT |
| [`spec-driven-eval`](skills/spec-driven-eval/SKILL.md) | Scores how completely an implementation fulfills a PRD/spec, case by case, and produces a single comparable final grade. | MIT |
| [`sql-injection-testing`](skills/sql-injection-testing/SKILL.md) | This skill should be used when the user asks to "test for SQL injection vulnerabilities", "perform SQLi attacks", "bypass… | MIT |
| [`sql-insight`](skills/sql-insight/SKILL.md) | Translate natural language to SQL, optimize query performance, and interpret EXPLAIN plans for SQLite and PostgreSQL. | MIT |
| [`sqlmap-database-pentesting`](skills/sqlmap-database-pentesting/SKILL.md) | This skill should be used when the user asks to "automate SQL injection testing," "enumerate database structure," "extract… | MIT |
| [`ssh-penetration-testing`](skills/ssh-penetration-testing/SKILL.md) | This skill should be used when the user asks to "pentest SSH services", "enumerate SSH configurations", "brute force SSH… | MIT |
| [`subagent-creator`](skills/subagent-creator/SKILL.md) | Guide for creating AI subagents with isolated context for complex multi-step workflows. | MIT |
| [`subagent-driven-development`](skills/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session | MIT |
| [`surgical-patch`](skills/surgical-patch/SKILL.md) | Fix bugs and small behavior changes at the narrowest responsible layer. | Apache-2.0 |
| [`tactical-ddd`](skills/tactical-ddd/SKILL.md) | Detects anemic domain models, validates and refactors them into rich domain models, and enforces tactical DDD patterns (Entities,… | MIT |
| [`teach`](skills/teach/SKILL.md) | Teach the user a new skill or concept, within this workspace. | MIT |
| [`technical-design-doc-creator`](skills/technical-design-doc-creator/SKILL.md) | Creates comprehensive Technical Design Documents (TDD) with mandatory and optional sections through interactive discovery. | MIT |
| [`test-audit`](skills/test-audit/SKILL.md) | Prunes low-value tests across a whole suite to a measured target while holding coverage. | MIT |
| [`test-driven-dev`](skills/test-driven-dev/SKILL.md) | Test-driven development with red-green-refactor loop. | MIT |
| [`test-suite-architect`](skills/test-suite-architect/SKILL.md) | This skill should be used when establishing comprehensive QA testing processes for any software project. | MIT |
| [`the-fool`](skills/the-fool/SKILL.md) | Use when challenging ideas, plans, decisions, or proposals. | MIT |
| [`the-judge`](skills/the-judge/SKILL.md) | Evidence-first pull request judge that reviews a PR and posts one consolidated GitHub review with inline comments via the gh CLI. | MIT |
| [`the-jury`](skills/the-jury/SKILL.md) | Use when a question, decision, plan, tradeoff, or claim needs a rigorous verdict and one perspective is not enough. | MIT |
| [`three-best-practices`](skills/three-best-practices/SKILL.md) | Three.js performance optimization and best practices guidelines. | MIT |
| [`tidy`](skills/tidy/SKILL.md) | Reviews a local diff, branch diff, or PR with file:line findings in confirmed and plausible tiers, gates any test the diff adds… | MIT |
| [`timeline-builder`](skills/timeline-builder/SKILL.md) | Generate beautiful interactive timeline HTML pages from JSON data, with vertical, horizontal, or dual-side layouts, collapsible… | MIT |
| [`tlc-discover`](skills/tlc-discover/SKILL.md) | Interviews an unshaped idea into a verdict and a design document - decisions, flows, schema, contracts - that anyone can plan… | MIT |
| [`tlc-generative-engine-optimization`](skills/tlc-generative-engine-optimization/SKILL.md) | Generative Engine Optimization (GEO) specialist — the technical, on-page publishing work that makes a given page or site… | MIT |
| [`tlc-implement`](skills/tlc-implement/SKILL.md) | Implements work already planned - a plan.md from tlc-plan, or a small ticket - by freezing it into checks with proofs, building,… | MIT |
| [`tlc-plan`](skills/tlc-plan/SKILL.md) | Turns a request, ticket, PRD, design or thread into one plan a human approves and a builder can act on without the conversation:… | MIT |
| [`tlc-prd`](skills/tlc-prd/SKILL.md) | Interviews an idea into a PRD file covering situation, problem, success, boundary, and journey states, and stops before any… | MIT |
| [`tlc-spec-driven`](skills/tlc-spec-driven/SKILL.md) | Feature planning and implementation with 4 adaptive phases (Specify, Design, Tasks, Execute). | MIT |
| [`tlc-spec-lean`](skills/tlc-spec-lean/SKILL.md) | Spec-driven feature work that freezes obligations instead of the plan: one human-reviewed plan with EARS criteria, path,… | MIT |
| [`to-questionnaire`](skills/to-questionnaire/SKILL.md) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | MIT |
| [`to-spec`](skills/to-spec/SKILL.md) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what… | MIT |
| [`to-tickets`](skills/to-tickets/SKILL.md) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published… | MIT |
| [`top-web-vulnerabilities`](skills/top-web-vulnerabilities/SKILL.md) | This skill should be used when the user asks to "identify web application vulnerabilities", "explain common security flaws",… | MIT |
| [`tos-clause-scanner`](skills/tos-clause-scanner/SKILL.md) | Audit Terms of Service, user agreements, and privacy policies for consumer risks, producing a structured report that flags unfair… | MIT |
| [`triage`](skills/triage/SKILL.md) | Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention. | MIT |
| [`typescript-pro`](skills/typescript-pro/SKILL.md) | Use when building TypeScript applications requiring advanced type systems, generics, or full-stack type safety. | MIT |
| [`typography-audit`](skills/typography-audit/SKILL.md) | Audits font loading, type scales, measure, spacing, OpenType, and rendered punctuation with 78 scoped rules. | MIT |
| [`ui-animation`](skills/ui-animation/SKILL.md) | Builds, reviews, and measures UI motion, including springs, gestures, scroll effects, curve fitting from recordings, and sparse… | MIT |
| [`ui-design`](skills/ui-design/SKILL.md) | Designs and builds React/Next/Tailwind UI, audits visual and interaction defects, and stress-tests components with worst-case… | MIT |
| [`ui-verification`](skills/ui-verification/SKILL.md) | Runs scoped browser probes for focus, hit targets, overflow, themes, request failures, and performance attribution, with evidence… | MIT |
| [`ultracave`](skills/ultracave/SKILL.md) | Respond terse like smart caveman. | Apache-2.0 |
| [`update-nanoclaw`](skills/update-nanoclaw/SKILL.md) | Transactionally update a customized NanoClaw checkout from official upstream without exposing live mounted source, with fork-safe… | MIT |
| [`update-skills`](skills/update-skills/SKILL.md) | Refresh installed NanoClaw channel and provider payloads (channels from their registry branch, providers from their skill… | MIT |
| [`using-agent-skills`](skills/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. | MIT |
| [`using-git-worktrees`](skills/using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an… | MIT |
| [`using-n8n-mcp-skills`](skills/using-n8n-mcp-skills/SKILL.md) | Use when building, editing, validating, testing, or debugging an n8n workflow through the n8n-mcp MCP server — designing a flow,… | MIT |
| [`using-superpowers`](skills/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response… | MIT |
| [`vc-industry-research`](skills/vc-industry-research/SKILL.md) | Generate professional primary market / venture capital industry research reports, including sector deep-dives, investment memos,… | MIT |
| [`vercel-cli`](skills/vercel-cli/SKILL.md) | Deploy apps to Vercel. Use when asked to deploy, ship, or publish a web application, or manage Vercel projects, domains, and… | MIT |
| [`vercel-deploy`](skills/vercel-deploy/SKILL.md) | Deploy applications and websites to Vercel. | MIT |
| [`verify-and-stop`](skills/verify-and-stop/SKILL.md) | Prove existing work meets acceptance conditions without expanding scope. | Apache-2.0 |
| [`video-outreach`](skills/video-outreach/SKILL.md) | When the user wants to build video-first cold outreach, create personalized video at scale, implement async selling, or use AI… | MIT |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. | MIT |
| [`web-quality-audit`](skills/web-quality-audit/SKILL.md) | Comprehensive web quality audit covering performance, accessibility, SEO, and best practices in a single review. | MIT |
| [`welcome`](skills/welcome/SKILL.md) | Introduce yourself to a newly connected channel. | MIT |
| [`wiki`](skills/wiki/SKILL.md) | The wiki CLI and the node's two knowledge bases -- project wiki and memory. | Apache-2.0 |
| [`windows-privilege-escalation`](skills/windows-privilege-escalation/SKILL.md) | This skill should be used when the user asks to "escalate privileges on Windows," "find Windows privesc vectors," "enumerate… | MIT |
| [`wireshark-analysis`](skills/wireshark-analysis/SKILL.md) | This skill should be used when the user asks to "analyze network traffic with Wireshark", "capture packets for troubleshooting",… | MIT |
| [`wizard`](skills/wizard/SKILL.md) | Generate an interactive bash wizard that walks a human through steps only they can perform. | MIT |
| [`wordpress-penetration-testing`](skills/wordpress-penetration-testing/SKILL.md) | This skill should be used when the user asks to "pentest WordPress sites", "scan WordPress for vulnerabilities", "enumerate… | MIT |
| [`writing-hookify-rules`](skills/writing-hookify-rules/SKILL.md) | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify… | Apache-2.0 |
| [`writing-skills`](skills/writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | MIT |
| [`xss-html-injection`](skills/xss-html-injection/SKILL.md) | This skill should be used when the user asks to "test for XSS vulnerabilities", "perform cross-site scripting attacks", "identify… | MIT |

### Notes & knowledge (`notes-knowledge`) — 12 skills

Index pack: [`pack-notes-knowledge`](skills/pack-notes-knowledge/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`bulletmind`](skills/bulletmind/SKILL.md) | Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking. | MIT |
| [`defuddle`](skills/defuddle/SKILL.md) | Extract clean Markdown from HTML pages with Defuddle CLI. | MIT |
| [`json-canvas`](skills/json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. | MIT |
| [`knap`](skills/knap/SKILL.md) | Render Markdown from templates and structured data using Knap CLI. | MIT |
| [`notebooklm`](skills/notebooklm/SKILL.md) | Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers… | MIT |
| [`obsidian-bases`](skills/obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. | MIT |
| [`obsidian-cli`](skills/obsidian-cli/SKILL.md) | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. | MIT |
| [`obsidian-clipper-template-creator`](skills/obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. | MIT |
| [`obsidian-markdown`](skills/obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. | MIT |
| [`obsidian-second-brain`](skills/obsidian-second-brain/SKILL.md) | Claude operates your Obsidian vault as a self-rewriting knowledge base. | MIT |
| [`pack-notes-knowledge`](skills/pack-notes-knowledge/SKILL.md) | Work inside a Markdown knowledge base: Obsidian Flavored Markdown with wikilinks, callouts and properties, Bases views and… | mixed |
| [`unpaid-intern`](skills/unpaid-intern/SKILL.md) | A free second brain for work in plain markdown files the user owns. | MIT |

### Mobile apps (`mobile-apps`) — 12 skills

Index pack: [`pack-mobile-apps`](skills/pack-mobile-apps/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`android-native-dev`](skills/android-native-dev/SKILL.md) | Android native application development and UI design guide. | MIT |
| [`animate-expo`](skills/animate-expo/SKILL.md) | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it… | MIT |
| [`developing-genkit-dart`](skills/developing-genkit-dart/SKILL.md) | Generates code and provides documentation for the Genkit Dart SDK. | Apache-2.0 |
| [`flutter-dev`](skills/flutter-dev/SKILL.md) | A practical guide for building cross-platform applications with Flutter 3 and Dart. | MIT |
| [`frontend-architecture`](skills/frontend-architecture/SKILL.md) | A portable, framework-agnostic architecture style for any React or React Native frontend. | MIT |
| [`frontend-observability`](skills/frontend-observability/SKILL.md) | A portable, framework-agnostic field-side observability pattern for React or React Native integrations. | MIT |
| [`ios-application-dev`](skills/ios-application-dev/SKILL.md) | A practical guide for building iOS applications using UIKit, SnapKit, and SwiftUI. | MIT |
| [`kotlin-exposed-patterns`](skills/kotlin-exposed-patterns/SKILL.md) | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations,… | MIT |
| [`kotlin-testing`](skills/kotlin-testing/SKILL.md) | Patrones de pruebas Kotlin con Kotest, MockK, pruebas de coroutines, pruebas basadas en propiedades y cobertura con Kover. | MIT |
| [`pack-mobile-apps`](skills/pack-mobile-apps/SKILL.md) | Native and cross-platform mobile work: Android with Kotlin, Compose and Material 3, iOS application development, Flutter, React… | mixed |
| [`react-native-dev`](skills/react-native-dev/SKILL.md) | A practical guide for building production-ready React Native and Expo applications. | MIT |
| [`vercel-react-native-skills`](skills/vercel-react-native-skills/SKILL.md) | Comprehensive best practices for React Native and Expo applications. | NOASSERTION |

### Browser automation (`browser-automation`) — 121 skills

Index pack: [`pack-browser-automation`](skills/pack-browser-automation/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`1688-product-detail`](skills/1688-product-detail/SKILL.md) | Extracts comprehensive wholesale product data from 1688.com product detail pages: title, tiered pricing, SKU variants with… | MIT |
| [`agentcore`](skills/agentcore/SKILL.md) | Run agent-browser on AWS Bedrock AgentCore cloud browsers. | Apache-2.0 |
| [`airbnb-listing-detail`](skills/airbnb-listing-detail/SKILL.md) | Fetches complete Airbnb listing details for a given numeric listing ID via the internal GraphQL API, returning title, room type,… | MIT |
| [`airbnb-search-listing`](skills/airbnb-search-listing/SKILL.md) | Extracts Airbnb accommodation search results from a destination query via SSR-embedded data, returning listing ID, URL, name,… | MIT |
| [`amazon-alexa-qa`](skills/amazon-alexa-qa/SKILL.md) | Amazon Alexa for Shopping Q&A automation: submits questions to Amazon's Alexa/Rufus AI shopping assistant and collects response… | MIT |
| [`amazon-asin-lookup-api-skill`](skills/amazon-asin-lookup-api-skill/SKILL.md) | This skill helps users extract structured product details from Amazon using a specific ASIN (Amazon Standard Identification… | MIT |
| [`amazon-best-selling-products-finder-api-skill`](skills/amazon-best-selling-products-finder-api-skill/SKILL.md) | This skill helps users extract structured best-selling product data from Amazon via the BrowserAct API. | MIT |
| [`amazon-bestseller-listing`](skills/amazon-bestseller-listing/SKILL.md) | Amazon Best Sellers listing scraper: extract product cards from any Amazon Best Sellers (zgbs) or /gp/bestsellers/ category page… | MIT |
| [`amazon-buy-box-monitor-api-skill`](skills/amazon-buy-box-monitor-api-skill/SKILL.md) | This skill helps users extract basic product details other sellers prices and seller ratings from Amazon via ASIN automatically… | MIT |
| [`amazon-competitor-analyzer`](skills/amazon-competitor-analyzer/SKILL.md) | Scrapes Amazon product data from ASINs using browseract.com automation API and performs surgical competitive analysis. | MIT |
| [`amazon-listing-competitor-analysis-skill`](skills/amazon-listing-competitor-analysis-skill/SKILL.md) | This skill helps users analyze Amazon competitor listings by ASIN and produce structured competitive intelligence plus strategic… | MIT |
| [`amazon-product-api-skill`](skills/amazon-product-api-skill/SKILL.md) | This skill helps users extract structured product listings from Amazon, including titles, ASINs, prices, ratings, and… | MIT |
| [`amazon-product-detail`](skills/amazon-product-detail/SKILL.md) | Amazon product detail page scraper: extract full product data from any open Amazon product detail URL (any /dp/{asin} or… | MIT |
| [`amazon-product-search-api-skill`](skills/amazon-product-search-api-skill/SKILL.md) | This skill is designed to help users automatically extract product data from Amazon search results. | MIT |
| [`amazon-reviews-api-skill`](skills/amazon-reviews-api-skill/SKILL.md) | This skill helps users automatically extract Amazon product reviews via the Amazon Reviews API. | MIT |
| [`amazon-search-listing`](skills/amazon-search-listing/SKILL.md) | Amazon search and category listing scraper: extract product listings from any Amazon search results page, keyword search URL, or… | MIT |
| [`browser-act`](skills/browser-act/SKILL.md) | Browser automation CLI for AI agents. | MIT |
| [`browser-act-skill-forge`](skills/browser-act-skill-forge/SKILL.md) | Forges reusable Skill packages (SKILL.md + scripts) from website exploration via browser-act — no re-exploration later. | MIT |
| [`browser-relay`](skills/browser-relay/SKILL.md) | Operate the user's existing, logged-in Chrome locally or on an explicitly connected remote machine. | MIT |
| [`browser-use`](skills/browser-use/SKILL.md) | Direct browser control via CDP for web interaction: automation, scraping, testing, screenshots, and site/app work. | MIT |
| [`business-contact-social-links-skill`](skills/business-contact-social-links-skill/SKILL.md) | This skill helps users automatically extract official website and social media profiles. | MIT |
| [`cloud`](skills/cloud/SKILL.md) | Reference docs for the Cloud REST API, SDKs, and integration patterns. | MIT |
| [`core`](skills/core/SKILL.md) | Core agent-browser usage guide. | Apache-2.0 |
| [`derive-client`](skills/derive-client/SKILL.md) | Reverse-engineer a website's internal API by recording browser traffic into a HAR file, then generate a standalone client or CLI… | Apache-2.0 |
| [`dogfood`](skills/dogfood/SKILL.md) | Systematically explore and test a web application to find bugs, UX issues, and other problems. | Apache-2.0 |
| [`douyin-video-search`](skills/douyin-video-search/SKILL.md) | Searches Douyin (douyin.com) for videos by keyword and returns structured video data including author info, stats, cover,… | MIT |
| [`ebay-item-detail`](skills/ebay-item-detail/SKILL.md) | Extracts full item detail from any open eBay item URL, returning JSON with url, itemNumber, title, subTitle, categories, price,… | MIT |
| [`ebay-search-listing`](skills/ebay-search-listing/SKILL.md) | Extracts product listings from any eBay search or category page URL, returning per-item cards (itemNumber, url, title, subtitle,… | MIT |
| [`ebay-sold-listings-search`](skills/ebay-sold-listings-search/SKILL.md) | eBay sold-listings scraper across 8 marketplaces (ebay.com/.co.uk/.de/.fr/.it/.es/.ca/.com.au). | MIT |
| [`ecommerce-listing`](skills/ecommerce-listing/SKILL.md) | Extract product list from any e-commerce category page, search results page, or keyword search with filters. | MIT |
| [`ecommerce-product-detail`](skills/ecommerce-product-detail/SKILL.md) | Extract complete product information from any e-commerce product page. | MIT |
| [`ecommerce-reviews`](skills/ecommerce-reviews/SKILL.md) | Extract customer reviews from any e-commerce product page or reviews page. | MIT |
| [`ecommerce-seller-info`](skills/ecommerce-seller-info/SKILL.md) | Extract seller or merchant profile data from marketplace platform seller pages. | MIT |
| [`electron`](skills/electron/SKILL.md) | Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via Chrome DevTools… | Apache-2.0 |
| [`etsy-category-listing`](skills/etsy-category-listing/SKILL.md) | Etsy category page scraper: given an Etsy category URL (e.g. | MIT |
| [`etsy-keyword-search`](skills/etsy-keyword-search/SKILL.md) | Etsy keyword search scraper: given a search keyword and optional page number, returns paginated product listings with listingId,… | MIT |
| [`etsy-product-detail`](skills/etsy-product-detail/SKILL.md) | Etsy product detail scraper: given an Etsy listing URL, returns full product detail including listingId, title, priceCurrent,… | MIT |
| [`etsy-shop-catalog`](skills/etsy-shop-catalog/SKILL.md) | Etsy shop catalog scraper: given an Etsy shop URL (e.g. | MIT |
| [`facebook-ads-library-search`](skills/facebook-ads-library-search/SKILL.md) | Searches Meta Ad Library (Facebook/Instagram/WhatsApp ads) by keyword or Facebook page ID and extracts ad details including… | MIT |
| [`facebook-groups-scrape-posts`](skills/facebook-groups-scrape-posts/SKILL.md) | Scrapes posts from a Facebook group given a group URL, sort order, and desired count — returns structured post metadata including… | MIT |
| [`facebook-page-posts`](skills/facebook-page-posts/SKILL.md) | Scrapes posts from any public Facebook Page timeline, returning structured data including post text, author info, engagement… | MIT |
| [`facebook-page-profile-posts`](skills/facebook-page-profile-posts/SKILL.md) | Scrapes posts from any public Facebook Page or personal Profile timeline, returning structured data including post text, author… | MIT |
| [`github-project-contributor-finder-api-skill`](skills/github-project-contributor-finder-api-skill/SKILL.md) | This skill helps users extract GitHub repository project details and contributor contact information using keywords, stars, and… | MIT |
| [`goofish-item-detail`](skills/goofish-item-detail/SKILL.md) | Extracts full detail data from a single Goofish (闲鱼/xianyu, goofish.com) second-hand item page. | MIT |
| [`goofish-search-list`](skills/goofish-search-list/SKILL.md) | Scrapes second-hand item search results from Goofish (闲鱼/xianyu, goofish.com) — China's largest second-hand marketplace. | MIT |
| [`google-image-api-skill`](skills/google-image-api-skill/SKILL.md) | This skill helps users automatically extract structured image data from Google Images via BrowserAct API. | MIT |
| [`google-maps-api-skill`](skills/google-maps-api-skill/SKILL.md) | This skill helps users automatically scrape business data from Google Maps using the BrowserAct Google Maps API. | MIT |
| [`google-maps-contact-extract`](skills/google-maps-contact-extract/SKILL.md) | Extracts business contact details from Google Maps search results and place detail pages, then visits each business website to… | MIT |
| [`google-maps-reviews-api-skill`](skills/google-maps-reviews-api-skill/SKILL.md) | This skill is designed to help users automatically extract reviews from Google Maps via the Google Maps Reviews API. | MIT |
| [`google-maps-search-api-skill`](skills/google-maps-search-api-skill/SKILL.md) | This skill is designed to help users automatically extract business data from Google Maps search results. | MIT |
| [`google-news-api-skill`](skills/google-news-api-skill/SKILL.md) | This skill helps users automatically extract structured news data from Google News via BrowserAct API. | MIT |
| [`google-search-serp`](skills/google-search-serp/SKILL.md) | Extracts Google Search results page (SERP) data including organic results, paid ads, related searches, People Also Ask questions,… | MIT |
| [`google-social-media-finder`](skills/google-social-media-finder/SKILL.md) | Searches Google to discover social media profiles associated with a person, brand, or username; returns platform name, profile… | MIT |
| [`indeed-job-search`](skills/indeed-job-search/SKILL.md) | Scrape job listings from Indeed.com by keyword, location, and country. | MIT |
| [`industry-key-contact-radar-api-skill`](skills/industry-key-contact-radar-api-skill/SKILL.md) | This skill helps users discover key contacts across industries, roles, and social platforms via the BrowserAct API. | MIT |
| [`instagram-hashtag-posts`](skills/instagram-hashtag-posts/SKILL.md) | Scrapes Instagram posts by hashtag, returning media items with captions, like/comment counts, media URLs and user info from the… | MIT |
| [`instagram-place-posts`](skills/instagram-place-posts/SKILL.md) | Scrapes Instagram posts tagged at a specific location or place, returning media items with captions, like/comment counts, media… | MIT |
| [`instagram-post-comments`](skills/instagram-post-comments/SKILL.md) | Fetches comments from an Instagram post including comment text, username, timestamp, like count and reply count. | MIT |
| [`instagram-profile-meta`](skills/instagram-profile-meta/SKILL.md) | Fetches Instagram user profile metadata including bio, follower count, following count, post count, verification status and other… | MIT |
| [`instagram-profile-posts`](skills/instagram-profile-posts/SKILL.md) | Scrapes posts from an Instagram user's profile feed including captions, media URLs, like/comment counts, timestamps and location… | MIT |
| [`invisible-playwright`](skills/invisible-playwright/SKILL.md) | Use the Dot's browser identities for any task on a website or search on the web: which identity to use, opening and closing one,… | MIT |
| [`linkedin-jobs-search`](skills/linkedin-jobs-search/SKILL.md) | Search LinkedIn job listings and extract full job details. | MIT |
| [`open-source`](skills/open-source/SKILL.md) | Reference docs for writing Python code against the browser-use library. | MIT |
| [`pack-browser-automation`](skills/pack-browser-automation/SKILL.md) | Control a real browser from an agent: navigation, clicking, form filling, screenshots, extraction and multi-step flows, with the… | mixed |
| [`producthunt-launches`](skills/producthunt-launches/SKILL.md) | Scrape Product Hunt daily/weekly/monthly/yearly leaderboard launches with full product details, maker profiles, and website… | MIT |
| [`protected-vercel-deployments`](skills/protected-vercel-deployments/SKILL.md) | Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection with agent-browser. | Apache-2.0 |
| [`qa`](skills/qa/SKILL.md) | QA-test a website or web app and return a 1-5 quality score (5 = flawless, 1 = broken) with evidence. | MIT |
| [`reddit-competitor-analysis-api-skill`](skills/reddit-competitor-analysis-api-skill/SKILL.md) | This skill helps users extract structured data from Reddit posts and comments via BrowserAct API. | MIT |
| [`reddit-warmup`](skills/reddit-warmup/SKILL.md) | ﻿--- name: reddit-warmup description: "Runtime-neutral Reddit account warm-up and brand promotion skill for AI agents. | MIT |
| [`remote-browser`](skills/remote-browser/SKILL.md) | Controls an isolated Browser Use Cloud browser from a sandboxed machine with the current Browser Use CLI. | MIT |
| [`slack`](skills/slack/SKILL.md) | Interact with Slack workspaces using browser automation. | Apache-2.0 |
| [`social-media-finder-skill`](skills/social-media-finder-skill/SKILL.md) | This skill helps users automatically find social media profiles across platforms like Facebook, Twitter, Instagram, LinkedIn, etc. | MIT |
| [`taobao-keyword-search`](skills/taobao-keyword-search/SKILL.md) | Search Taobao and Tmall product listings by keyword, returning paginated product cards with title, price, shop, image, sales, and… | MIT |
| [`taobao-product-detail`](skills/taobao-product-detail/SKILL.md) | Fetch full product detail from a Taobao or Tmall product page by itemId, returning title, price, shop info, images, SKU variants,… | MIT |
| [`taobao-product-reviews`](skills/taobao-product-reviews/SKILL.md) | Fetch customer reviews for a Taobao or Tmall product by itemId, returning reviewer name, date, purchased variant, review text,… | MIT |
| [`taobao-shop-catalog`](skills/taobao-shop-catalog/SKILL.md) | Browse a Taobao or Tmall shop's product catalog by shopId, returning paginated product listings with itemId and title. | MIT |
| [`technical-writer`](skills/technical-writer/SKILL.md) | Write, review, and edit developer documentation for SDKs, libraries, and frameworks, including sites such as agent-browser.dev… | Apache-2.0 |
| [`threads-keyword-search`](skills/threads-keyword-search/SKILL.md) | Searches Threads posts by keyword or hashtag and returns matching posts with engagement metrics, extracted from SSR-embedded JSON. | MIT |
| [`threads-profile-search`](skills/threads-profile-search/SKILL.md) | Discovers Threads user accounts by keyword, extracting profile data including username, display name, verification status,… | MIT |
| [`threads-user-posts`](skills/threads-user-posts/SKILL.md) | Fetches public posts from a Threads user's profile page, extracting post text, engagement metrics, and media info from… | MIT |
| [`tiktok-hashtag-videos`](skills/tiktok-hashtag-videos/SKILL.md) | TikTok hashtag video scraper: input a hashtag name → output paginated video list with full metadata (author profile, engagement… | MIT |
| [`tiktok-profile-videos`](skills/tiktok-profile-videos/SKILL.md) | TikTok user profile video scraper: input a TikTok username → output the user's profile info plus paginated video list with full… | MIT |
| [`tiktok-search-videos`](skills/tiktok-search-videos/SKILL.md) | TikTok keyword search video scraper: input search keyword → output paginated video list with full metadata (author, engagement… | MIT |
| [`tiktok-video-detail`](skills/tiktok-video-detail/SKILL.md) | TikTok single video detail scraper: input a TikTok video URL → output full video metadata (author profile, engagement stats,… | MIT |
| [`trustpilot-company-info`](skills/trustpilot-company-info/SKILL.md) | Trustpilot company profile lookup on trustpilot.com — input a company domain (e.g. | MIT |
| [`trustpilot-reviews`](skills/trustpilot-reviews/SKILL.md) | Trustpilot customer reviews scraper for any company listed on trustpilot.com — given a company domain (e.g. | MIT |
| [`vercel-sandbox`](skills/vercel-sandbox/SKILL.md) | Run agent-browser + Chrome inside Vercel Sandbox microVMs for browser automation from any Vercel-deployed app. | Apache-2.0 |
| [`walmart-category-listing`](skills/walmart-category-listing/SKILL.md) | Walmart category page scraper: input a walmart.com browse or category URL with optional page number, extract paginated product… | MIT |
| [`walmart-keyword-search`](skills/walmart-keyword-search/SKILL.md) | Walmart keyword search scraper: input a search keyword and page number, navigate to walmart.com search results, extract paginated… | MIT |
| [`walmart-product-detail`](skills/walmart-product-detail/SKILL.md) | Walmart product detail page extractor: given a walmart.com product URL (walmart.com/ip/...), extract full product data including… | MIT |
| [`walmart-product-reviews`](skills/walmart-product-reviews/SKILL.md) | Walmart product reviews scraper: given a walmart.com product item ID, navigate to the reviews page and extract paginated customer… | MIT |
| [`web-research-assistant`](skills/web-research-assistant/SKILL.md) | AI-powered web research assistant that leverages BrowserAct API to supplement restricted web access by searching the internet for… | MIT |
| [`web-search-scraper-api-skill`](skills/web-search-scraper-api-skill/SKILL.md) | This skill helps users automatically extract complete Markdown content from any website via the BrowserAct Web Search Scraper API. | MIT |
| [`webcrawler-deep-crawl`](skills/webcrawler-deep-crawl/SKILL.md) | Deep-crawl any website from start URLs, return per-page LLM-ready text/markdown/HTML plus metadata (title, description, author,… | MIT |
| [`webmcp-gen`](skills/webmcp-gen/SKILL.md) | Build and validate experimental WebMCP tools for an existing web page. | Apache-2.0 |
| [`wechat-article-search-api-skill`](skills/wechat-article-search-api-skill/SKILL.md) | This skill helps users extract full article contents from WeChat using the BrowserAct API. | MIT |
| [`x-dm-auto-chat`](skills/x-dm-auto-chat/SKILL.md) | X (Twitter) DM automated chat end-to-end Skill: scan DM inbox to identify pending-reply conversations, read message history,… | MIT |
| [`x-keyword-comment`](skills/x-keyword-comment/SKILL.md) | X (Twitter) keyword-based reply posting: search tweets by keyword, read each tweet's content, generate contextual replies from a… | MIT |
| [`x-tweet-by-conversation`](skills/x-tweet-by-conversation/SKILL.md) | Collects every tweet in an X (Twitter) conversation thread given a conversation id (root tweet id) — the focal tweet plus all… | MIT |
| [`x-tweet-by-handle`](skills/x-tweet-by-handle/SKILL.md) | Scrapes tweets from an X (Twitter) user profile timeline given a handle, with selectable mode: tweets, tweets+replies, or… | MIT |
| [`x-tweet-by-url`](skills/x-tweet-by-url/SKILL.md) | Scrapes tweets from any X (Twitter) URL — search results, user profile, single tweet detail, or list timeline — and returns… | MIT |
| [`x-tweet-search`](skills/x-tweet-search/SKILL.md) | Scrapes tweets from X (Twitter) by search query, user handle, or direct URL — returns full tweet data including text, author… | MIT |
| [`x-tweet-search-by-query`](skills/x-tweet-search-by-query/SKILL.md) | Searches X (Twitter) for tweets by free-form advanced query and returns a normalized tweet list with text, author profile,… | MIT |
| [`x402`](skills/x402/SKILL.md) | Set up Browser Use Cloud payments with x402 — pay per request from a crypto wallet (USDC on Base mainnet), no signup or API key. | MIT |
| [`xiaohongshu-auto-posting`](skills/xiaohongshu-auto-posting/SKILL.md) | Automates the complete Xiaohongshu (XHS / Little Red Book) content operation workflow: pain-point topic collection → style case… | MIT |
| [`xiaohongshu-note-detail`](skills/xiaohongshu-note-detail/SKILL.md) | Fetch Xiaohongshu (RedNote / xhs) note detail and comments by note ID, returning title, description, author info, engagement… | MIT |
| [`xiaohongshu-search`](skills/xiaohongshu-search/SKILL.md) | Search Xiaohongshu (RedNote / xhs) notes by keyword and return a paginated list with title, author, engagement stats (likes,… | MIT |
| [`xiaohongshu-search-full`](skills/xiaohongshu-search-full/SKILL.md) | Search Xiaohongshu (XHS / RedNote) notes by keyword with full field extraction including body text, topics/tags, image list URLs,… | MIT |
| [`xiaohongshu-user-profile`](skills/xiaohongshu-user-profile/SKILL.md) | Fetch Xiaohongshu (RedNote / xhs) user profile information and their published notes list by user ID, returning nickname, bio,… | MIT |
| [`youtube-api-skill`](skills/youtube-api-skill/SKILL.md) | This skill helps users automatically extract detailed video metrics and channel information from YouTube based on keyword… | MIT |
| [`youtube-batch-transcript-extractor-api-skill`](skills/youtube-batch-transcript-extractor-api-skill/SKILL.md) | This skill helps users automatically extract YouTube video transcripts and metadata in batch via the BrowserAct API. | MIT |
| [`youtube-channel-api-skill`](skills/youtube-channel-api-skill/SKILL.md) | This skill helps users automatically extract structured channel data from YouTube search results via BrowserAct API. | MIT |
| [`youtube-channel-business-email`](skills/youtube-channel-business-email/SKILL.md) | YouTube channel business email and contact extractor: accepts a channel id (UCxxx), handle (@name), or URL; navigates the channel… | MIT |
| [`youtube-comments-api-skill`](skills/youtube-comments-api-skill/SKILL.md) | This skill helps users extract structured video list data and comment data from YouTube using the BrowserAct API. | MIT |
| [`youtube-influencer-finder-api-skill`](skills/youtube-influencer-finder-api-skill/SKILL.md) | This skill helps users extract YouTube influencer profiles including social links, subscriber counts, and channel stats via the… | MIT |
| [`youtube-search-api-skill`](skills/youtube-search-api-skill/SKILL.md) | This skill helps users automatically extract structured data from YouTube search results using the BrowserAct API. | MIT |
| [`youtube-transcript`](skills/youtube-transcript/SKILL.md) | YouTube transcript extraction and content reformatting: given a YouTube video URL, opens the video's transcript panel, extracts… | MIT |
| [`youtube-transcript-analysis-api-skill`](skills/youtube-transcript-analysis-api-skill/SKILL.md) | This skill helps users extract YouTube video transcripts and perform deep competitive analysis on the content. | MIT |
| [`youtube-transcript-extractor-api-skill`](skills/youtube-transcript-extractor-api-skill/SKILL.md) | This skill helps users automatically extract YouTube video transcripts and metadata via the BrowserAct API. | MIT |
| [`youtube-video-api-skill`](skills/youtube-video-api-skill/SKILL.md) | This skill helps users automatically extract channel-level and video detail data from a specific YouTube channel via BrowserAct… | MIT |
| [`zhihu-search-api-skill`](skills/zhihu-search-api-skill/SKILL.md) | This skill helps users automatically extract structured article details and full content from Zhihu via the BrowserAct API. | MIT |

### Google Workspace (`google-workspace`) — 61 skills

Index pack: [`pack-google-workspace`](skills/pack-google-workspace/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`gws-admin-reports`](skills/gws-admin-reports/SKILL.md) | Google Workspace Admin SDK: Audit logs and usage reports. | Apache-2.0 |
| [`gws-calendar`](skills/gws-calendar/SKILL.md) | Google Calendar: Manage calendars and events. | Apache-2.0 |
| [`gws-calendar-agenda`](skills/gws-calendar-agenda/SKILL.md) | Google Calendar: Show upcoming events across all calendars. | Apache-2.0 |
| [`gws-calendar-insert`](skills/gws-calendar-insert/SKILL.md) | Google Calendar: Create a new event. | Apache-2.0 |
| [`gws-chat`](skills/gws-chat/SKILL.md) | Google Chat: Manage Chat spaces and messages. | Apache-2.0 |
| [`gws-chat-send`](skills/gws-chat-send/SKILL.md) | Google Chat: Send a message to a space. | Apache-2.0 |
| [`gws-classroom`](skills/gws-classroom/SKILL.md) | Google Classroom: Manage classes, rosters, and coursework. | Apache-2.0 |
| [`gws-docs`](skills/gws-docs/SKILL.md) | Read and write Google Docs. | Apache-2.0 |
| [`gws-docs-write`](skills/gws-docs-write/SKILL.md) | Google Docs: Append text to a document. | Apache-2.0 |
| [`gws-drive`](skills/gws-drive/SKILL.md) | Google Drive: Manage files, folders, and shared drives. | Apache-2.0 |
| [`gws-drive-upload`](skills/gws-drive-upload/SKILL.md) | Google Drive: Upload a file with automatic metadata. | Apache-2.0 |
| [`gws-events`](skills/gws-events/SKILL.md) | Subscribe to Google Workspace events. | Apache-2.0 |
| [`gws-events-renew`](skills/gws-events-renew/SKILL.md) | Google Workspace Events: Renew/reactivate Workspace Events subscriptions. | Apache-2.0 |
| [`gws-events-subscribe`](skills/gws-events-subscribe/SKILL.md) | Google Workspace Events: Subscribe to Workspace events and stream them as NDJSON. | Apache-2.0 |
| [`gws-forms`](skills/gws-forms/SKILL.md) | Read and write Google Forms. | Apache-2.0 |
| [`gws-gmail`](skills/gws-gmail/SKILL.md) | Gmail: Send, read, and manage email. | Apache-2.0 |
| [`gws-gmail-forward`](skills/gws-gmail-forward/SKILL.md) | Gmail: Forward a message to new recipients. | Apache-2.0 |
| [`gws-gmail-read`](skills/gws-gmail-read/SKILL.md) | Gmail: Read a message and extract its body or headers. | Apache-2.0 |
| [`gws-gmail-reply`](skills/gws-gmail-reply/SKILL.md) | Gmail: Reply to a message (handles threading automatically). | Apache-2.0 |
| [`gws-gmail-reply-all`](skills/gws-gmail-reply-all/SKILL.md) | Gmail: Reply-all to a message (handles threading automatically). | Apache-2.0 |
| [`gws-gmail-send`](skills/gws-gmail-send/SKILL.md) | PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. | Apache-2.0 |
| [`gws-gmail-triage`](skills/gws-gmail-triage/SKILL.md) | Gmail: Show unread inbox summary (sender, subject, date). | Apache-2.0 |
| [`gws-gmail-watch`](skills/gws-gmail-watch/SKILL.md) | Gmail: Watch for new emails and stream them as NDJSON. | Apache-2.0 |
| [`gws-keep`](skills/gws-keep/SKILL.md) | Manage Google Keep notes. | Apache-2.0 |
| [`gws-meet`](skills/gws-meet/SKILL.md) | Manage Google Meet conferences. | Apache-2.0 |
| [`gws-modelarmor`](skills/gws-modelarmor/SKILL.md) | Google Model Armor: Filter user-generated content for safety. | Apache-2.0 |
| [`gws-modelarmor-create-template`](skills/gws-modelarmor-create-template/SKILL.md) | Google Model Armor: Create a new Model Armor template. | Apache-2.0 |
| [`gws-modelarmor-sanitize-prompt`](skills/gws-modelarmor-sanitize-prompt/SKILL.md) | Google Model Armor: Sanitize a user prompt through a Model Armor template. | Apache-2.0 |
| [`gws-modelarmor-sanitize-response`](skills/gws-modelarmor-sanitize-response/SKILL.md) | Google Model Armor: Sanitize a model response through a Model Armor template. | Apache-2.0 |
| [`gws-people`](skills/gws-people/SKILL.md) | Google People: Manage contacts and profiles. | Apache-2.0 |
| [`gws-script`](skills/gws-script/SKILL.md) | Manage Google Apps Script projects. | Apache-2.0 |
| [`gws-script-push`](skills/gws-script-push/SKILL.md) | Google Apps Script: Upload local files to an Apps Script project. | Apache-2.0 |
| [`gws-shared`](skills/gws-shared/SKILL.md) | gws CLI: Shared patterns for authentication, global flags, and output formatting. | Apache-2.0 |
| [`gws-sheets`](skills/gws-sheets/SKILL.md) | Google Sheets: Read and write spreadsheets. | Apache-2.0 |
| [`gws-sheets-append`](skills/gws-sheets-append/SKILL.md) | Google Sheets: Append a row to a spreadsheet. | Apache-2.0 |
| [`gws-sheets-read`](skills/gws-sheets-read/SKILL.md) | Google Sheets: Read values from a spreadsheet. | Apache-2.0 |
| [`gws-slides`](skills/gws-slides/SKILL.md) | Google Slides: Read and write presentations. | Apache-2.0 |
| [`gws-tasks`](skills/gws-tasks/SKILL.md) | Google Tasks: Manage task lists and tasks. | Apache-2.0 |
| [`gws-workflow`](skills/gws-workflow/SKILL.md) | Google Workflow: Cross-service productivity workflows. | Apache-2.0 |
| [`gws-workflow-email-to-task`](skills/gws-workflow-email-to-task/SKILL.md) | Google Workflow: Convert a Gmail message into a Google Tasks entry. | Apache-2.0 |
| [`gws-workflow-file-announce`](skills/gws-workflow-file-announce/SKILL.md) | Google Workflow: Announce a Drive file in a Chat space. | Apache-2.0 |
| [`gws-workflow-meeting-prep`](skills/gws-workflow-meeting-prep/SKILL.md) | Google Workflow: Prepare for your next meeting: agenda, attendees, and linked docs. | Apache-2.0 |
| [`gws-workflow-standup-report`](skills/gws-workflow-standup-report/SKILL.md) | Google Workflow: Today's meetings + open tasks as a standup summary. | Apache-2.0 |
| [`gws-workflow-weekly-digest`](skills/gws-workflow-weekly-digest/SKILL.md) | Google Workflow: Weekly summary: this week's meetings + unread email count. | Apache-2.0 |
| [`pack-google-workspace`](skills/pack-google-workspace/SKILL.md) | Drive Gmail, Drive, Calendar, Docs, Sheets, Slides, Chat and Tasks from the command line with googleworkspace/cli — 95 skills… | mixed |
| [`persona-content-creator`](skills/persona-content-creator/SKILL.md) | Create, organize, and distribute content across Workspace. | Apache-2.0 |
| [`persona-customer-support`](skills/persona-customer-support/SKILL.md) | Manage customer support — track tickets, respond, escalate issues. | Apache-2.0 |
| [`persona-event-coordinator`](skills/persona-event-coordinator/SKILL.md) | Plan and manage events — scheduling, invitations, and logistics. | Apache-2.0 |
| [`persona-exec-assistant`](skills/persona-exec-assistant/SKILL.md) | Manage an executive's schedule, inbox, and communications. | Apache-2.0 |
| [`persona-hr-coordinator`](skills/persona-hr-coordinator/SKILL.md) | Handle HR workflows — onboarding, announcements, and employee comms. | Apache-2.0 |
| [`persona-it-admin`](skills/persona-it-admin/SKILL.md) | Administer IT — monitor security and configure Workspace. | Apache-2.0 |
| [`persona-project-manager`](skills/persona-project-manager/SKILL.md) | Coordinate projects — track tasks, schedule meetings, and share docs. | Apache-2.0 |
| [`persona-researcher`](skills/persona-researcher/SKILL.md) | Organize research — manage references, notes, and collaboration. | Apache-2.0 |
| [`persona-sales-ops`](skills/persona-sales-ops/SKILL.md) | Manage sales workflows — track deals, schedule calls, client comms. | Apache-2.0 |
| [`persona-team-lead`](skills/persona-team-lead/SKILL.md) | Lead a team — run standups, coordinate tasks, and communicate. | Apache-2.0 |
| [`recipe-calendar`](skills/recipe-calendar/SKILL.md) | Calendar and Meet recipes — events, free/busy, invites, conferences. | Apache-2.0 |
| [`recipe-docs`](skills/recipe-docs/SKILL.md) | Docs and Slides recipes — create, template, share, report. | Apache-2.0 |
| [`recipe-drive`](skills/recipe-drive/SKILL.md) | Drive recipes — folders, sharing, bulk download, change watches. | Apache-2.0 |
| [`recipe-gmail`](skills/recipe-gmail/SKILL.md) | Gmail recipes — label, forward, archive, draft, auto-reply. | Apache-2.0 |
| [`recipe-sheets`](skills/recipe-sheets/SKILL.md) | Sheets recipes — read, compare, duplicate, export, track. | Apache-2.0 |
| [`recipe-workspace-admin`](skills/recipe-workspace-admin/SKILL.md) | Workspace admin recipes — tasks, forms, classroom, contacts, personas. | Apache-2.0 |

### Game development (`game-dev`) — 78 skills

Index pack: [`pack-game-dev`](skills/pack-game-dev/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`ai-behavior-trees-utility-ai`](skills/ai-behavior-trees-utility-ai/SKILL.md) | Two complementary ways to structure NPC decision-making, plus how to combine them. | Apache-2.0 |
| [`audio-design`](skills/audio-design/SKILL.md) | Game audio is a mixing graph plus a music system. | Apache-2.0 |
| [`bevy-ecs`](skills/bevy-ecs/SKILL.md) | Structure a Bevy game in Rust around the Entity Component System: the App and plugins, components and resources, systems with… | Apache-2.0 |
| [`camera-systems`](skills/camera-systems/SKILL.md) | The camera is the player's window; bad camera work makes a good game feel awful. | Apache-2.0 |
| [`card-game`](skills/card-game/SKILL.md) | A playbook for card games — card data, the deck/hand/discard zones, the turn structure, and how card effects resolve. | Apache-2.0 |
| [`create-game-assets`](skills/create-game-assets/SKILL.md) | Plan, generate, source, normalize, and validate cohesive visual game assets. | Apache-2.0 |
| [`defold-core`](skills/defold-core/SKILL.md) | Structure, wire and verify a Defold game: editor resource files, the Lua script lifecycle, addressing and messages, runtime… | Apache-2.0 |
| [`dialogue-systems`](skills/dialogue-systems/SKILL.md) | Model conversations as a graph: nodes hold lines, choices branch the flow, conditions gate options, and variables remember what… | Apache-2.0 |
| [`ebitengine-game`](skills/ebitengine-game/SKILL.md) | Deliver a game that is understandable, responsive and complete at the requested scope. | Apache-2.0 |
| [`fps-shooter`](skills/fps-shooter/SKILL.md) | A playbook for first-person shooters — the look/move controller, the shooting model, weapon feel, and combat. | Apache-2.0 |
| [`game-ai`](skills/game-ai/SKILL.md) | Build believable NPC behavior from three separable layers: decide (what to do), steer (how to move there), and path (how to route… | Apache-2.0 |
| [`game-feel`](skills/game-feel/SKILL.md) | The difference between a mechanic that works and one that feels good is feedback: the layered, slightly-exaggerated response an… | Apache-2.0 |
| [`game-jam`](skills/game-jam/SKILL.md) | Turn a theme and a fixed deadline into a finished, submitted game. | Apache-2.0 |
| [`game-ui-ux`](skills/game-ui-ux/SKILL.md) | Build HUDs and menus that stay correct on a phone, an ultrawide monitor, and a TV across a gamepad and a mouse. | Apache-2.0 |
| [`godot-2d-movement`](skills/godot-2d-movement/SKILL.md) | Build responsive 2D character controllers with CharacterBody2D and the argument-less moveandslide(). | Apache-2.0 |
| [`godot-3d-essentials`](skills/godot-3d-essentials/SKILL.md) | Assemble a working 3D scene: transforms, camera, lights, environment/post, materials, and GridMap blockouts. | Apache-2.0 |
| [`godot-animation`](skills/godot-animation/SKILL.md) | Choose and drive the right animation tool: AnimationPlayer (clips), AnimationTree (blending/state machines), or Tween (short… | Apache-2.0 |
| [`godot-audio`](skills/godot-audio/SKILL.md) | Play SFX and music, route them through buses, control volume in decibels, and time gameplay to the beat. | Apache-2.0 |
| [`godot-csharp`](skills/godot-csharp/SKILL.md) | Write Godot game code in C#: node subclasses, the engine lifecycle, exports, signals as events, and GDScript interop. | Apache-2.0 |
| [`godot-export`](skills/godot-export/SKILL.md) | Turn a project into runnable platform builds via export presets and the command line, and handle the web/dedicated-server gotchas. | Apache-2.0 |
| [`godot-gdscript`](skills/godot-gdscript/SKILL.md) | Write correct, statically typed GDScript and use the node lifecycle and signal system the way the engine intends. | Apache-2.0 |
| [`godot-gdscript-headless-testing`](skills/godot-gdscript-headless-testing/SKILL.md) | Run GDScript tests from the command line, without the editor GUI, and get a real process exit code CI can act on. | Apache-2.0 |
| [`godot-multiplayer`](skills/godot-multiplayer/SKILL.md) | Connect peers, call functions remotely with @rpc, assign authority, and replicate state with… | Apache-2.0 |
| [`godot-nodes-scenes`](skills/godot-nodes-scenes/SKILL.md) | Compose games from nodes and scenes, instance them at runtime, and access the tree without crashing on freed or missing nodes. | Apache-2.0 |
| [`godot-physics`](skills/godot-physics/SKILL.md) | Pick the right physics body, wire up collision layers/masks, detect overlaps, and cast rays. | Apache-2.0 |
| [`godot-resources`](skills/godot-resources/SKILL.md) | Model game data as reusable, Inspector-editable Resource objects instead of hard-coded values, and load/save them as .tres/.res. | Apache-2.0 |
| [`godot-shaders`](skills/godot-shaders/SKILL.md) | Write canvasitem (2D) and spatial (3D) shaders in the Godot Shading Language, animate with TIME/UV, expose uniforms, and read the… | Apache-2.0 |
| [`godot-signals-groups`](skills/godot-signals-groups/SKILL.md) | Decouple nodes with the observer pattern (signals) and act on many nodes at once (groups), instead of hard-coding references… | Apache-2.0 |
| [`godot-tilemap`](skills/godot-tilemap/SKILL.md) | Author tile-based levels with TileMapLayer + TileSet, add per-tile collision and custom data, autotile with terrains, and… | Apache-2.0 |
| [`godot-ui-control`](skills/godot-ui-control/SKILL.md) | Lay out responsive UI with Control anchors and Container nodes, style it with a Theme, and make it navigable by keyboard and… | Apache-2.0 |
| [`input-systems`](skills/input-systems/SKILL.md) | Never wire gameplay to raw keys. | Apache-2.0 |
| [`itch-publish`](skills/itch-publish/SKILL.md) | Get a build onto an itch.io page and keep it updated. | Apache-2.0 |
| [`level-design`](skills/level-design/SKILL.md) | A level is a sequence of intentional experiences delivered through space. | Apache-2.0 |
| [`love2d-core`](skills/love2d-core/SKILL.md) | Set up and debug the foundation of a LÖVE game in Lua: the callback loop, frame-rate- independent movement, input, and screen… | Apache-2.0 |
| [`pack-game-dev`](skills/pack-game-dev/SKILL.md) | Game work in one pack: core loop and feel, level and systems design, engine and language choices, art and audio pipelines,… | mixed |
| [`phaser-arcade-physics`](skills/phaser-arcade-physics/SKILL.md) | Add movement and collision to a Phaser game with the lightweight Arcade Physics engine (AABB rectangles and circles only). | Apache-2.0 |
| [`phaser-core`](skills/phaser-core/SKILL.md) | Set up the foundation of a Phaser game: the Game config, the Scene lifecycle, asset loading, cameras, and passing data between… | Apache-2.0 |
| [`physics-tuning`](skills/physics-tuning/SKILL.md) | Most "bad physics" is not a bug in the engine — it's a mismatch between the fixed-timestep simulation and the variable-rate… | Apache-2.0 |
| [`pixijs-rendering`](skills/pixijs-rendering/SKILL.md) | Set up and structure a PixiJS 8.22 application: the async Application, asset loading via Assets, the Container/Sprite scene… | Apache-2.0 |
| [`platformer`](skills/platformer/SKILL.md) | A playbook for 2D platformers — the run/jump controller "feel", level structure, hazards, and goals. | Apache-2.0 |
| [`procedural-gen`](skills/procedural-gen/SKILL.md) | Generate levels, terrain, and loot from compact rules and a seed. | Apache-2.0 |
| [`prototype-fast`](skills/prototype-fast/SKILL.md) | Get a mechanic into a player's hands fast to learn whether it's worth building. | Apache-2.0 |
| [`puzzle`](skills/puzzle/SKILL.md) | A playbook for grid/board puzzle games — the board model, move input, rule resolution (matching, pushing, logic), scoring, undo,… | Apache-2.0 |
| [`pygame-core`](skills/pygame-core/SKILL.md) | Build the foundation of a pygame game in Python: the main loop, delta-time movement, drawing with Surface/Rect, input, and… | Apache-2.0 |
| [`roblox-characters`](skills/roblox-characters/SKILL.md) | Treat a Player as the durable identity and each Character as a replaceable session with its own references, connections,… | Apache-2.0 |
| [`roblox-datastores`](skills/roblox-datastores/SKILL.md) | Persist data across sessions in Roblox with DataStoreService: loading on join, saving on leave and shutdown, safe updates,… | Apache-2.0 |
| [`roblox-luau`](skills/roblox-luau/SKILL.md) | Script a Roblox experience in Luau: services, Instances, events, the server/client split, and secure cross-boundary communication. | Apache-2.0 |
| [`roblox-networking`](skills/roblox-networking/SKILL.md) | Build explicit request and replication contracts in which the server decides authoritative game state and clients provide input… | Apache-2.0 |
| [`roblox-physics`](skills/roblox-physics/SKILL.md) | Choose deliberately between simulation, character control, hit detection, and visual-only motion; they are different jobs. | Apache-2.0 |
| [`roblox-simulator-economy`](skills/roblox-simulator-economy/SKILL.md) | Choose the economy's numbers with a pacing table before writing gameplay code, then implement them so the server owns every… | Apache-2.0 |
| [`roblox-studio-workflow`](skills/roblox-studio-workflow/SKILL.md) | Work as a collaborator inside an existing place, not as if it were a blank text repository. | Apache-2.0 |
| [`roblox-ui`](skills/roblox-ui/SKILL.md) | Implement deliberate, editable Roblox UI that preserves the experience's visual language and works across supported devices. | Apache-2.0 |
| [`roguelike`](skills/roguelike/SKILL.md) | A playbook for roguelikes — the turn engine, procedural dungeons, field-of-view, permadeath, and run economy. | Apache-2.0 |
| [`router`](skills/router/SKILL.md) | The entry point for game-development work. | Apache-2.0 |
| [`rpg`](skills/rpg/SKILL.md) | A playbook for role-playing games — stats and progression, inventory/equipment, quests, dialogue, and combat. | Apache-2.0 |
| [`save-systems`](skills/save-systems/SKILL.md) | A save file is a serialized snapshot of game state that survives restarts. | Apache-2.0 |
| [`shader-programming`](skills/shader-programming/SKILL.md) | Shaders are small programs that run per vertex and per pixel on the GPU. | Apache-2.0 |
| [`steam-publish`](skills/steam-publish/SKILL.md) | Take a finished build to a live Steam store page. | Apache-2.0 |
| [`survival-crafting`](skills/survival-crafting/SKILL.md) | A playbook for survival-crafting games — the gather → craft → build loop, survival needs, the crafting/tech progression, and base… | Apache-2.0 |
| [`threejs-gltf-loading`](skills/threejs-gltf-loading/SKILL.md) | Load .gltf/.glb models and play their animations in three.js, including compressed geometry (DRACO/Meshopt) and textures (KTX2). | Apache-2.0 |
| [`threejs-materials-lighting`](skills/threejs-materials-lighting/SKILL.md) | Make three.js surfaces look right: pick the correct material, light the scene, enable shadows, and add image-based lighting. | Apache-2.0 |
| [`threejs-scene-setup`](skills/threejs-scene-setup/SKILL.md) | Create the foundation of a three.js app: module loading, the scene/camera/renderer trio, the render loop, responsive resizing,… | Apache-2.0 |
| [`tower-defense`](skills/tower-defense/SKILL.md) | A playbook for tower defense — enemy pathing, wave spawning, tower targeting, and the economy that ties them together. | Apache-2.0 |
| [`unity-animation`](skills/unity-animation/SKILL.md) | Control animation state with Unity 6.3 LTS's Animator and Animator Controllers: parameters, transitions, blend trees, layers, and… | Apache-2.0 |
| [`unity-build-pipeline`](skills/unity-build-pipeline/SKILL.md) | Configure, script, and automate Unity 6.3 LTS player builds: scenes, platform target, scripting backend, stripping, and… | Apache-2.0 |
| [`unity-csharp-scripting`](skills/unity-csharp-scripting/SKILL.md) | Write correct, idiomatic gameplay scripts in Unity 6. | Apache-2.0 |
| [`unity-input-system`](skills/unity-input-system/SKILL.md) | Read input through Unity's Input System package (com.unity.inputsystem 1.x; Unity 6.3 LTS ships 1.20) — action-based,… | Apache-2.0 |
| [`unity-navmesh`](skills/unity-navmesh/SKILL.md) | Give NPCs pathfinding in Unity 6.3 LTS: bake walkable surfaces and move agents around obstacles. | Apache-2.0 |
| [`unity-physics`](skills/unity-physics/SKILL.md) | Make objects move, collide, and detect each other with Unity 6.3 LTS's built-in 3D physics (PhysX). | Apache-2.0 |
| [`unity-scriptableobjects`](skills/unity-scriptableobjects/SKILL.md) | Use ScriptableObject assets to store shared data and decouple systems in Unity 6.3 LTS — configuration, event channels, and… | Apache-2.0 |
| [`unity-tilemap-2d`](skills/unity-tilemap-2d/SKILL.md) | Author and script tile-based 2D levels in Unity 6.3 LTS with the Grid/Tilemap system, the Tile Palette, colliders, and runtime… | Apache-2.0 |
| [`unreal-behavior-trees`](skills/unreal-behavior-trees/SKILL.md) | Author NPC decision-making in UE5 with Behavior Trees driven by a Blackboard: structure the tree with composites, gate branches… | Apache-2.0 |
| [`unreal-blueprints`](skills/unreal-blueprints/SKILL.md) | Structure gameplay logic in Unreal Engine 5 Blueprints: pick the right graph, expose data cleanly, and choose a communication… | Apache-2.0 |
| [`unreal-cpp-gameplay`](skills/unreal-cpp-gameplay/SKILL.md) | Write correct UE5 gameplay C++: the reflection macros that connect C++ to the editor and Blueprints, the Gameplay Framework class… | Apache-2.0 |
| [`unreal-enhanced-input`](skills/unreal-enhanced-input/SKILL.md) | Wire player input the modern UE5 way with the Enhanced Input system: data-driven Input Actions and Mapping Contexts instead of… | Apache-2.0 |
| [`unreal-niagara`](skills/unreal-niagara/SKILL.md) | Build and control real-time visual effects in UE5 with Niagara: understand the System/Emitter/Module hierarchy, expose parameters… | Apache-2.0 |
| [`unreal-packaging`](skills/unreal-packaging/SKILL.md) | Turn a UE5 project into a runnable, distributable build: choose the right build configuration, cook content, set the launch map,… | Apache-2.0 |
| [`visual-novel`](skills/visual-novel/SKILL.md) | A playbook for visual novels — the branching script, the presentation (text box, characters, backgrounds), choices, and the… | Apache-2.0 |

### Product management (`product-management`) — 78 skills

Index pack: [`pack-product-management`](skills/pack-product-management/SKILL.md).

| Skill | What it does | Licence |
|---|---|---|
| [`acquisition-channel-advisor`](skills/acquisition-channel-advisor/SKILL.md) | Evaluate acquisition channels using unit economics, customer quality, and scalability. | see LICENSE |
| [`agent-orchestration-advisor`](skills/agent-orchestration-advisor/SKILL.md) | Design multi-agent AI workflows with clear boundaries, handoffs, and monitoring. | see LICENSE |
| [`ai-shaped-readiness-advisor`](skills/ai-shaped-readiness-advisor/SKILL.md) | Assess whether your product work is AI-first or AI-shaped. | see LICENSE |
| [`altitude-horizon-framework`](skills/altitude-horizon-framework/SKILL.md) | Understand the PM-to-Director transition through altitude and horizon thinking. | see LICENSE |
| [`ansoff-matrix`](skills/ansoff-matrix/SKILL.md) | Map evidence-backed growth options across the Ansoff Matrix with risk-rated sequencing. | see LICENSE |
| [`autonomous-investigation`](skills/autonomous-investigation/SKILL.md) | The protocol behind every investigation skill. | see LICENSE |
| [`battle-card-builder`](skills/battle-card-builder/SKILL.md) | Research and draft a competitive battle card from public evidence — every claim labeled and sourced. | see LICENSE |
| [`business-health-diagnostic`](skills/business-health-diagnostic/SKILL.md) | Diagnose SaaS business health across growth, retention, efficiency, and capital. | see LICENSE |
| [`company-intel`](skills/company-intel/SKILL.md) | Research a company, industry, or competitor set using web search and seven analytical lenses. | see LICENSE |
| [`company-research`](skills/company-research/SKILL.md) | Create a company research brief with executive quotes, product strategy, and org context. | see LICENSE |
| [`competitive-analysis-process`](skills/competitive-analysis-process/SKILL.md) | Orchestrate a complete competitive analysis across six steps, from landscape to strategic direction. | see LICENSE |
| [`competitive-intel-watch`](skills/competitive-intel-watch/SKILL.md) | Scheduled delta monitoring against a prior competitive snapshot. | see LICENSE |
| [`competitive-research-snapshot`](skills/competitive-research-snapshot/SKILL.md) | Research a competitive landscape with cited snapshots, a comparison matrix, and so-what implications. | see LICENSE |
| [`context-engineering-advisor`](skills/context-engineering-advisor/SKILL.md) | Diagnose context stuffing vs. | see LICENSE |
| [`customer-journey-map`](skills/customer-journey-map/SKILL.md) | Create a customer journey map across stages, touchpoints, actions, emotions, and metrics. | see LICENSE |
| [`customer-journey-mapping-workshop`](skills/customer-journey-mapping-workshop/SKILL.md) | Run a customer journey mapping workshop with adaptive questions and outputs. | see LICENSE |
| [`derisk-measurement-advisor`](skills/derisk-measurement-advisor/SKILL.md) | Identify what to measure, test, or track to de-risk a product or AI idea. | see LICENSE |
| [`director-readiness-advisor`](skills/director-readiness-advisor/SKILL.md) | Guide the PM-to-Director transition across preparing, interviewing, landing, and recalibrating. | see LICENSE |
| [`discovery-interview-prep`](skills/discovery-interview-prep/SKILL.md) | Plan customer discovery interviews with the right goal, segment, constraints, and method. | see LICENSE |
| [`discovery-process`](skills/discovery-process/SKILL.md) | Run a full discovery cycle from problem hypothesis to validated solution. | see LICENSE |
| [`eol-checklist`](skills/eol-checklist/SKILL.md) | Build a phase-gated EOL checklist sized to the sunset, with a named owner on every item. | see LICENSE |
| [`eol-internal-enablement`](skills/eol-internal-enablement/SKILL.md) | Build the support FAQ, sales talking points, and objection handling teams need before an EOL announcement. | see LICENSE |
| [`eol-message`](skills/eol-message/SKILL.md) | Write a right-sized EOL announcement — brief notice through full phased comms — with rationale, customer impact, and next steps. | see LICENSE |
| [`eol-process`](skills/eol-process/SKILL.md) | Run a product sunset end to end — decide, align, plan, prepare, announce, close. | see LICENSE |
| [`eol-readiness-advisor`](skills/eol-readiness-advisor/SKILL.md) | Run a go/no-go assessment for retiring a product or feature, then right-size the effort. | see LICENSE |
| [`eol-stakeholder-sequence`](skills/eol-stakeholder-sequence/SKILL.md) | Plan who to talk to about a sunset, in what order, and what each conversation must cover. | see LICENSE |
| [`epic-breakdown-advisor`](skills/epic-breakdown-advisor/SKILL.md) | Break down epics into user stories with Humanizing Work split patterns. | see LICENSE |
| [`epic-hypothesis`](skills/epic-hypothesis/SKILL.md) | Frame an epic as a testable hypothesis with target user, expected outcome, and validation method. | see LICENSE |
| [`executive-onboarding-playbook`](skills/executive-onboarding-playbook/SKILL.md) | Plan a VP or CPO 30-60-90 day diagnostic onboarding path. | see LICENSE |
| [`feature-investment-advisor`](skills/feature-investment-advisor/SKILL.md) | Evaluate feature investments using revenue impact, cost structure, ROI, and strategy. | see LICENSE |
| [`finance-based-pricing-advisor`](skills/finance-based-pricing-advisor/SKILL.md) | Evaluate pricing changes using ARPU, conversion, churn risk, NRR, and payback. | see LICENSE |
| [`finance-metrics-quickref`](skills/finance-metrics-quickref/SKILL.md) | Look up SaaS finance metrics, formulas, and benchmarks fast. | see LICENSE |
| [`incoming-request-advisor`](skills/incoming-request-advisor/SKILL.md) | Decode an incoming message into a structured breakdown separating the literal ask from the job-to-be-done. | see LICENSE |
| [`intel-discipline-advisor`](skills/intel-discipline-advisor/SKILL.md) | Triage a competitive or market question into the right intelligence disciplines, cadence, and executing skill. | see LICENSE |
| [`intelligence-collection-disciplines`](skills/intelligence-collection-disciplines/SKILL.md) | Run competitive research like an intelligence agency: eight collection disciplines (OSINT to MASINT), signal-to-inference chains,… | see LICENSE |
| [`jobs-to-be-done`](skills/jobs-to-be-done/SKILL.md) | Uncover customer jobs, pains, and gains in a structured JTBD format. | see LICENSE |
| [`lean-ux-canvas`](skills/lean-ux-canvas/SKILL.md) | Guide teams through Lean UX Canvas v2. | see LICENSE |
| [`lifecycle-play-advisor`](skills/lifecycle-play-advisor/SKILL.md) | Diagnose where a product sits in its lifecycle and which play fits — extend, replace, or retire. | see LICENSE |
| [`market-landscape-scan`](skills/market-landscape-scan/SKILL.md) | Map a market's segments, players, substitutes, and whitespace with cited evidence. | see LICENSE |
| [`opportunity-solution-tree`](skills/opportunity-solution-tree/SKILL.md) | Build an Opportunity Solution Tree from outcomes to opportunities, solutions, and tests. | see LICENSE |
| [`organic-growth-advisor`](skills/organic-growth-advisor/SKILL.md) | Identify which organic growth path to pursue — new segments, geographies, channels, or products. | see LICENSE |
| [`pack-product-management`](skills/pack-product-management/SKILL.md) | Product work end to end: discovery interviews and problem framing, opportunity assessment, PRDs and specs, roadmaps and… | mixed |
| [`pestel-analysis`](skills/pestel-analysis/SKILL.md) | Analyze political, economic, social, technological, environmental, and legal forces. | see LICENSE |
| [`pestel-delta-monitor`](skills/pestel-delta-monitor/SKILL.md) | Quarterly re-scan of a prior PESTEL analysis. | see LICENSE |
| [`pm-skill-creator`](skills/pm-skill-creator/SKILL.md) | Design a new PM skill through guided conversation. | see LICENSE |
| [`pol-probe`](skills/pol-probe/SKILL.md) | Define a Proof of Life probe to test a risky hypothesis cheaply. | see LICENSE |
| [`pol-probe-advisor`](skills/pol-probe-advisor/SKILL.md) | Select the right Proof of Life (PoL) probe based on hypothesis, risk, and resources. | see LICENSE |
| [`porters-five-forces`](skills/porters-five-forces/SKILL.md) | Read an industry's structure through Porter's Five Forces with documented signals per rating, ending at the profit pool. | see LICENSE |
| [`positioning-statement`](skills/positioning-statement/SKILL.md) | Create a Geoffrey Moore-style positioning statement. | see LICENSE |
| [`positioning-workshop`](skills/positioning-workshop/SKILL.md) | Run a positioning workshop that surfaces target customer, unmet need, category, benefits, and differentiation. | see LICENSE |
| [`prd-development`](skills/prd-development/SKILL.md) | Build a structured PRD that connects problem, users, solution, and success criteria. | see LICENSE |
| [`press-release`](skills/press-release/SKILL.md) | Write an Amazon-style press release that defines customer value before building. | see LICENSE |
| [`pricing-packaging-tracker`](skills/pricing-packaging-tracker/SKILL.md) | Track competitor pricing and packaging as a diffable time series. | see LICENSE |
| [`prioritization-advisor`](skills/prioritization-advisor/SKILL.md) | Choose a prioritization framework based on stage, team context, and stakeholder needs. | see LICENSE |
| [`problem-framing-canvas`](skills/problem-framing-canvas/SKILL.md) | Guide teams through MITRE's Problem Framing Canvas. | see LICENSE |
| [`problem-statement`](skills/problem-statement/SKILL.md) | Write a user-centered problem statement with who is blocked, what they are trying to do, why it matters, and how it feels. | see LICENSE |
| [`product-lifecycle-plays`](skills/product-lifecycle-plays/SKILL.md) | Map a product's lifecycle stage and choose between extension, replacement, and retirement plays. | see LICENSE |
| [`product-sense-interview-answer`](skills/product-sense-interview-answer/SKILL.md) | Structure a spoken PM product-sense answer with assumptions, segmentation, pain-point prioritization, and MVP tradeoffs. | see LICENSE |
| [`product-strategy-session`](skills/product-strategy-session/SKILL.md) | Run an end-to-end product strategy session across positioning, discovery, and roadmap planning. | see LICENSE |
| [`proto-persona`](skills/proto-persona/SKILL.md) | Create a proto-persona from current research, market signals, and team knowledge. | see LICENSE |
| [`recommendation-canvas`](skills/recommendation-canvas/SKILL.md) | Evaluate an AI product idea across outcomes, hypotheses, risks, and positioning. | see LICENSE |
| [`roadmap-planning`](skills/roadmap-planning/SKILL.md) | Plan a strategic roadmap across prioritization, epic definition, stakeholder alignment, and sequencing. | see LICENSE |
| [`saas-economics-efficiency-metrics`](skills/saas-economics-efficiency-metrics/SKILL.md) | Evaluate SaaS unit economics and capital efficiency. | see LICENSE |
| [`saas-revenue-growth-metrics`](skills/saas-revenue-growth-metrics/SKILL.md) | Calculate SaaS revenue, retention, and growth metrics. | see LICENSE |
| [`skill-authoring-workflow`](skills/skill-authoring-workflow/SKILL.md) | Turn raw PM content into a compliant, publish-ready skill. | see LICENSE |
| [`stakeholder-engagement-advisor`](skills/stakeholder-engagement-advisor/SKILL.md) | Plan engagement for a specific stakeholder. | see LICENSE |
| [`stakeholder-identification`](skills/stakeholder-identification/SKILL.md) | Map every stakeholder before engaging anyone. | see LICENSE |
| [`stakeholder-mapping`](skills/stakeholder-mapping/SKILL.md) | Prioritize stakeholders using two complementary grids. | see LICENSE |
| [`storyboard`](skills/storyboard/SKILL.md) | Create a six-frame storyboard that shows a user's journey from problem to solution. | see LICENSE |
| [`swot-analysis`](skills/swot-analysis/SKILL.md) | Build an evidence-cited SWOT of one company — yours or a competitor's — from public sources, ending with the S-O/W-T crossings. | see LICENSE |
| [`tam-sam-som-calculator`](skills/tam-sam-som-calculator/SKILL.md) | Calculate TAM, SAM, and SOM with explicit assumptions, methods, and caveats. | see LICENSE |
| [`user-story`](skills/user-story/SKILL.md) | Create user stories with Mike Cohn format and Gherkin acceptance criteria. | see LICENSE |
| [`user-story-mapping`](skills/user-story-mapping/SKILL.md) | Create a user story map that lays out activities, steps, tasks, and release slices. | see LICENSE |
| [`user-story-mapping-workshop`](skills/user-story-mapping-workshop/SKILL.md) | Run a user story mapping workshop with adaptive questions and a structured map output. | see LICENSE |
| [`user-story-splitting`](skills/user-story-splitting/SKILL.md) | Break a large story or epic into smaller deliverable stories using proven split patterns. | see LICENSE |
| [`voice-of-customer-miner`](skills/voice-of-customer-miner/SKILL.md) | Mine public reviews, app stores, and forums for unmet needs, competitor weaknesses, and switching triggers — with quoted evidence. | see LICENSE |
| [`vp-cpo-readiness-advisor`](skills/vp-cpo-readiness-advisor/SKILL.md) | Guide the transition to VP or CPO across preparing, interviewing, landing, and recalibrating. | see LICENSE |
| [`workshop-facilitation`](skills/workshop-facilitation/SKILL.md) | Facilitate workshop sessions in a one-step, multi-turn flow. | see LICENSE |
## How an AI agent should consume this repo

1. Read **`catalog.json`** first — it is the single source of truth. It carries
   `generated`, `count`, `categories[]` and a `skills[]` array whose entries
   mirror each `meta.json`.
2. Pick the skill(s) you need by `id`, `category` or `tags`.
3. Read the matching **`skills/<id>/SKILL.md`** for the actual method.
4. To reuse a project's approach, follow its `source_repos` and, if the skill
   looks stale, compare `source_snapshot` against the repo's current HEAD.

A short pointer file for agents is also provided at [`llms.txt`](llms.txt), and
the same catalogue is rendered for humans at the [landing page](https://drsamonline.github.io/skills/).

## Keeping the catalogue current

The catalogue is refreshed by a weekly GitHub Actions workflow,
[`.github/workflows/refresh.yml`](.github/workflows/refresh.yml) (cron +
`workflow_dispatch`, `permissions: contents: write`). It performs the
**mechanical refresh only**: it re-reads the repository list from the GitHub
API, updates each skill's `meta.json` `updated` and `source_snapshot` fields
(and any changed source-repo metadata), regenerates `catalog.json`, and commits
only if something changed.

It does **not** rewrite the skill prose. That split is deliberate:

- **Mechanical refresh (automated)** — SHAs, dates, counts, `catalog.json`.
  Safe to run unattended every week.
- **Prose update (human/AI, separate)** — the `When to use`, `Method`, `Key
  files`, `Gotchas` and `Source projects` text. Rewriting a method from a diff
  is a judgement call, so it is never done by the scheduled workflow.

## Licence & attribution

This repository's text (the skills) is © 2026 Dr. Sohil Momin. The projects it
describes retain their own licences — see each `SKILL.md`'s source links.

The three `marketing` skills (`product-copywriting`, `directory-submissions`,
`free-tool-marketing`) are adapted from
[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
(MIT, © its authors); the shape and the ideas are theirs, the text and the
situation are ours. Their PolyForm Noncommercial licence is retained.

### Vendored third-party skills

The five `pack-*` skills and the seventeen skills they merge are imported from
[ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) at commit
`b9b7fb0`, under the **MIT** licence (© 2026 titstack contributors). Each of
those directories carries the full MIT text as its own `LICENSE`, and each
`meta.json` records the upstream repo, path and commit. MIT content is
redistributed here with its notice intact; the repository's PolyForm
Noncommercial terms continue to apply to the drsamonline skills around it.

`source_repos` is left empty for those entries on purpose: they describe a
repository that is not part of `drsamonline`, so the weekly refresh workflow
must not try to resolve their commit SHAs. The pin lives in `upstream.commit`
instead, which the refresh does not touch.

### The multi-repo import

501 skills and 10 index packs were imported from eighteen first-party skill
collections in one pass, at the commits recorded in each `meta.json`. The
import is a **deduplicated** one: where two repositories shipped the same topic
the fullest version is kept and the others are listed under *Upstream variants*
inside that skill, so nothing is silently dropped and no two entries claim the
same ground.

Licences are per skill, not per repository — `MIT` for most, `Apache-2.0` for
`google/skills` and `huggingface/skills`, each with its full text in that
directory's `LICENSE`. Two sources (`anthropics/skills`,
`vercel-labs/agent-skills`) publish **no licence file**; their skills are
included at this repository owner's explicit direction and carry a
`LICENSE-NOTICE.md` instead of a grant. Twenty-three skills were mined from the
aggregator collections to fill categories with thin first-party coverage; they
are marked `origin: third-party-aggregator` and their upstream attribution is
incomplete by nature.

`source_repos` is empty for every imported entry on purpose — the weekly refresh
workflow resolves SHAs against the `drsamonline` repo list, so a foreign repo
name there would be dropped on the next run. The pin lives in
`upstream.repo/path/commit`.

### The third import

1,013 more first-party skills from 45 repositories, deduplicated against everything
already here: 21 topics already had a fuller version in the catalogue, so the new
copy was recorded under *Upstream variants* instead of adding a second entry, and 6
existing entries were replaced because the new source was substantially fuller.
Four categories were added (`browser-automation`, `google-workspace`, `game-dev`,
`product-management`) and every index pack was regenerated, so a pack now covers
all members of its category rather than the batch it was born with.

Five listed repositories contributed nothing: `NeoLabHQ/sadd`, `NeoLabHQ/kaizen`,
`baskduf/codex-fable5`, `oliverb-io1902e8/agent-skills-collection` and
`testmu-ai/api-skill` do not exist at those URLs, and `agentskills/agentskills`
carries no `SKILL.md`. Four more are aggregators (`davila7/claude-code-templates`,
`ComposioHQ/awesome-claude-skills`, `alirezarezvani/claude-skills`,
`foryourhealth111-pixel/Vibe-Skills`); they were read for overlap but not bulk
imported.

New categories are listed compactly in this README: at this size the descriptions
belong in the pack tables and `catalog.json`, not in 1,000 more README rows.

### Pruning

The catalogue is not a mirror. After the imports it was cut back to what does
real work:

- **142 skills removed.** The four Anthropic office skills that reserve
  all rights (`docx`, `pdf`, `pptx`, `xlsx`); a placeholder template; two alias
  stubs that only pointed at another skill; and the product-internal CLI wrappers
  with no reusable method (`ctx-*`, `caveman-stats`, `caveman-compress`,
  `remotion-render`).
- **124 thin families merged into 12 skills.** The 81
  `nexu-io/html-anything` style specs (median body 266 bytes) became five style
  libraries grouped by what you are producing: deck, web page, dashboard, visual
  card, document. The 45 `googleworkspace/cli` `recipe-*` skills became six
  grouped recipe sets by service. The two `grilling` aliases folded into
  `grilling`. Every original id survives as a heading inside its merged skill, so
  nothing was lost, only indexed.

Everything kept is substantive: the median body across the catalogue is several
kilobytes, and each skill states a trigger, a method and the traps it hit.
