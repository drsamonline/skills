# skills

**A machine-consumable knowledge base of the working methods behind the drsamonline projects.**

[![Landing page](https://img.shields.io/badge/landing%20page-open-2e7d32?style=flat-square)](https://drsamonline.github.io/skills/)
[![All projects](https://img.shields.io/badge/All%20projects-hub-2e7d32?style=flat-square)](https://drsamonline.github.io/)
[![Type: knowledge base](https://img.shields.io/badge/type-knowledge%20base-586069?style=flat-square)](https://drsamonline.github.io/skills/)
[![Format: Markdown + JSON](https://img.shields.io/badge/format-Markdown%20%2B%20JSON-586069?style=flat-square)](https://github.com/drsamonline/skills)
[![License: MIT](https://img.shields.io/badge/license-PolyForm Noncommercial-2e7d32?style=flat-square)](LICENSE)

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
- **Project skills** — one per repository: what the project is, how it is built,
  how it is released, and what makes its workflow distinctive.

**Catalogue:** `59` skills across 9 categories. The machine-readable index is [`catalog.json`](catalog.json); the landing page is <https://drsamonline.github.io/skills/>.

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

`web-app-patterns`, `android-packaging`, `windows-desktop`, `game-engine`, `data-and-schema`, `health-tools`, `landing-and-seo`, `ci-and-release`, `marketing`.

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
  "category": "one of the eight categories",
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

### Web app patterns (`web-app-patterns`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`ambient-sound-studio`](skills/ambient-sound-studio/SKILL.md) | A private, offline ambient sound mixer in a single HTML file: 25 synthesised layers, 36 presets, EN/HI/GU, WAV and Opus export, installable PWA. | [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio) | 1.0.0 |
| [`blinkcode-ai-spectracode`](skills/blinkcode-ai-spectracode/SKILL.md) | Optical file transfer as a vanilla-JS PWA: a file becomes a 'File DNA' container painted as SpectraCode colour matrices, decoded by camera with marker detection, homography and Reed-Solomon error correction. | [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) | 1.0.0 |
| [`blinktransfer-animated-qr`](skills/blinktransfer-animated-qr/SKILL.md) | Offline file transfer over animated QR codes at ~20 FPS: a Vite-built PWA compresses files, renders a header plus a data stream of 1600-byte frames, and reassembles them on a receiver camera. | [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) | 1.0.0 |
| [`conqueror-os-workspace`](skills/conqueror-os-workspace/SKILL.md) | A private, offline resilience workspace in a single HTML file — read, reflect, journal, track and review — with no server, no account and no dependencies. | [conqueror-os](https://github.com/drsamonline/conqueror-os) | 1.0.0 |
| [`lan-single-server-architecture`](skills/lan-single-server-architecture/SKILL.md) | A multi-user system that runs entirely on a hospital LAN: a Python server owns the SQLite database, a vanilla-JS UI runs in a WebView2 client, and the server is discovered by UDP broadcast — no internet, no cloud. | [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`offline-first-single-file-web-app`](skills/offline-first-single-file-web-app/SKILL.md) | Build a whole app as one self-contained index.html — inline CSS/JS, no CDN, no build step — that runs from file:// or GitHub Pages, works offline, and persists data locally. | [conqueror-os](https://github.com/drsamonline/conqueror-os), [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio), [neon-runner](https://github.com/drsamonline/neon-runner), [boericke-repertory](https://github.com/drsamonline/boericke-repertory), [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator), [retro-strike](https://github.com/drsamonline/retro-strike), [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) | 1.0.0 |
| [`optical-file-transfer`](skills/optical-file-transfer/SKILL.md) | Move a file between two devices with no network, Bluetooth or cable, by rendering it as animated QR codes or colour-matrix frames and reading them back with a camera. | [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER), [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) | 1.0.0 |
| [`smartbill-app`](skills/smartbill-app/SKILL.md) | A fast, serverless single-page billing and invoicing app for Indian businesses: GST-ready (HSN/SAC, CGST/SGST, state codes, reverse charge), 100% local IndexedDB storage and A4 print layout. | [smartbill-app](https://github.com/drsamonline/smartbill-app) | 1.0.0 |
| [`smartnotes-ai-notes`](skills/smartnotes-ai-notes/SKILL.md) | An AI-powered note capture, categorisation and reminder-scheduling app with a brutalist UI: write in plain English and an LLM classifies, prioritises, titles and extracts dates. | [SmartNotes](https://github.com/drsamonline/SmartNotes) | 1.0.0 |
| [`ttb-tiny-toolbox-extension`](skills/ttb-tiny-toolbox-extension/SKILL.md) | A Manifest V3 browser extension bundling 590 small utilities across 18 categories into one offline-first popup, with one source tree assembled per browser by a small build. | [TTB](https://github.com/drsamonline/TTB) | 1.0.0 |

### Android packaging (`android-packaging`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`android-webview-apk-packaging`](skills/android-webview-apk-packaging/SKILL.md) | Wrap a static single-file web app into a dependency-free Android WebView APK (platform framework only, no AndroidX), signed with a shared debug key, built by Gradle in CI. | [app-builder](https://github.com/drsamonline/app-builder), [open-materia-medica](https://github.com/drsamonline/open-materia-medica) | 1.0.0 |

### Windows & desktop (`windows-desktop`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`all4one-utility-suite`](skills/all4one-utility-suite/SKILL.md) | 551 Windows tools across 45 plugin packs compiled into one self-contained portable utility_suite.exe (Python, tkinter GUI + CLI) — an embedded bundle with per-pack enable/disable, guided dependency gating and an audit that verifies every tool. | [All4ONE](https://github.com/drsamonline/All4ONE) | 2.0.0 |
| [`cldr-command-launcher`](skills/cldr-command-launcher/SKILL.md) | A single dependency-free Rust binary that sits in the system tray, pops up on a hotkey, and routes whatever you type — maths, unit conversion, a path, an app, or a web search. | [CLDR](https://github.com/drsamonline/CLDR) | 1.0.0 |
| [`embedded-bundle-feature-gating`](skills/embedded-bundle-feature-gating/SKILL.md) | Ship many features in one self-contained binary, compile them into a single embedded archive, and let users turn each feature on or off — while telling them honestly when one needs something the machine does not have. | [All4ONE](https://github.com/drsamonline/All4ONE) | 1.0.0 |
| [`lexora-exact-compression`](skills/lexora-exact-compression/SKILL.md) | A text-cleaning and exact-compression system: canonicalize documents conservatively, then compress with guaranteed byte-exact recovery (decode(encode(C)) == C), on low-resource hardware. | [lexora](https://github.com/drsamonline/lexora) | 1.0.0 |
| [`lockhtml-file-encryption`](skills/lockhtml-file-encryption/SKILL.md) | Encrypt any file into a single self-contained .html that asks for a PIN (AES-256-GCM + Argon2id), with one-time view, expiry, recipient keys, hidden volumes, Shamir shares and age interop — via a Python CLI and a browser GUI. | [lockhtml](https://github.com/drsamonline/lockhtml) | 1.0.0 |
| [`neo-nova-compiler`](skills/neo-nova-compiler/SKILL.md) | A statically-typed compiled systems language: a Rust compiler lowers NOVA through lexer, parser, semantic analyser, SIR and a lowerer to four backends (C, JavaScript, Rust, WebAssembly), with runtime, package manager, LSP and debugger. | [NEO](https://github.com/drsamonline/NEO) | 1.0.0 |
| [`pyinstaller-portable-exe-launcher`](skills/pyinstaller-portable-exe-launcher/SKILL.md) | Turn a static web app into one double-clickable portable Windows .exe: a tiny Python launcher serves the bundled app/ over 127.0.0.1 and opens the browser, frozen by PyInstaller --onefile. | [app-builder](https://github.com/drsamonline/app-builder), [All4ONE](https://github.com/drsamonline/All4ONE) | 1.0.0 |
| [`the-browser-aetheris`](skills/the-browser-aetheris/SKILL.md) | An experimental C++20 browser engine derived from Ladybird/SerenityOS, built with CMake + vcpkg and tested with CTest; explicitly not production-ready and honest about provenance. | [The_Browser](https://github.com/drsamonline/The_Browser) | 1.0.0 |
| [`ultimate-windows-optimizer`](skills/ultimate-windows-optimizer/SKILL.md) | A PowerShell + batch toolkit that applies documented, fully reversible Windows 10/11 debloat and performance tweaks, with real logging, real registry/service backups and a one-shot undo. | [ULTIMATE-WINDOWS-OPTIMIZER](https://github.com/drsamonline/ULTIMATE-WINDOWS-OPTIMIZER) | 1.0.0 |

### Games & engines (`game-engine`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`aethelgard-engine-rpg`](skills/aethelgard-engine-rpg/SKILL.md) | The vanilla-JavaScript engine behind Aethelgard: Chronicles of Fate — small modules loaded in script order behind one global (window.Game), no build step, no dependencies, fully offline, moddable. | [Aethelgard-Engine](https://github.com/drsamonline/Aethelgard-Engine) | 1.0.0 |
| [`aethelgard-games-deployment`](skills/aethelgard-games-deployment/SKILL.md) | A deployment repo holding the built, playable copies of two Aethelgard browser games — The Books (a 36-chapter visual novel) and Chronicles of Fate (a deep single-player RPG) — so GitHub Pages can serve them. | [aethelgard-games](https://github.com/drsamonline/aethelgard-games) | 1.0.0 |
| [`aethelgardvn-saga-engine`](skills/aethelgardvn-saga-engine/SKILL.md) | Saga: a small, dependency-free visual-novel engine for the browser — plain JavaScript, one stylesheet, no build step, works offline — built to make Aethelgard: The Books. | [AethelgardVN](https://github.com/drsamonline/AethelgardVN) | 1.0.0 |
| [`dance-fight-rhythm-game`](skills/dance-fight-rhythm-game/SKILL.md) | A single-file browser rhythm game where every fight move is a dance move: the track's beat is analysed up front into an offline beat grid, and on-beat hits score PERFECT for 60% extra damage. | [dance-fight](https://github.com/drsamonline/dance-fight) | 1.0.0 |
| [`idle-city-ages-of-growth`](skills/idle-city-ages-of-growth/SKILL.md) | A single-file idle city-builder that grows from a Stone Age village to a Fusion Age world-city: roads, zoning, power and happiness, running itself while you plan and expand. | [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) | 1.0.0 |
| [`neon-engine-open-world`](skills/neon-engine-open-world/SKILL.md) | A code-only WebGL engine for open-world browser shooters: no asset files, every texture/mesh/sound generated at runtime, ES modules with a vendored three.js, so a full game ships under 1 MB. | [neon-engine](https://github.com/drsamonline/neon-engine) | 1.0.0 |
| [`neon-games-arcade`](skills/neon-games-arcade/SKILL.md) | A deployment repo holding two open-world games built on the Neon Engine — Dead Zone (zombie survival) and Neon Police (crime response) — each a self-contained playable folder with a mod loader. | [neon-games](https://github.com/drsamonline/neon-games) | 1.0.0 |
| [`neon-runner-auto-fire-shooter`](skills/neon-runner-auto-fire-shooter/SKILL.md) | A retro auto-fire side-scrolling shooter in one self-contained HTML file (vanilla JS + canvas): move, jump, duck — the gun fires itself — with 60+ assertions, minified to ~176 KB. | [neon-runner](https://github.com/drsamonline/neon-runner) | 1.0.0 |
| [`retro-strike-software-3d`](skills/retro-strike-software-3d/SKILL.md) | A complete retro third-person shooter in one HTML file with a custom software 3D renderer, a live chiptune synth and procedural arenas — no engine, no build step, no dependencies. | [retro-strike](https://github.com/drsamonline/retro-strike) | 1.0.0 |

### Data & schema (`data-and-schema`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`homoeopathic-materia-medica-repertory-json`](skills/homoeopathic-materia-medica-repertory-json/SKILL.md) | 13 public-domain homoeopathic classics (1840–1906, ~108k rubrics) extracted into clean, app-ready, verbatim JSON with a self-describing schema, per-book QC and a reproducible pipeline (CC0). | [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) | 1.0.0 |
| [`materia-medica-builder`](skills/materia-medica-builder/SKILL.md) | An offline, no-dependency PWA that lets a practitioner build a personal materia medica and repertory — remedies, symptoms, rubrics, a custom marking scale — and export it in eight formats. | [MATERIA-MEDICA-BUILDER](https://github.com/drsamonline/MATERIA-MEDICA-BUILDER) | 1.0.0 |
| [`open-data-extraction-pipeline`](skills/open-data-extraction-pipeline/SKILL.md) | Turn raw OCR'd source texts into clean, app-ready JSON with a verbatim-fidelity rule: nothing invented, unknowns null, per-book QC, a self-describing schema and a reproducible pipeline. | [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json), [MATERIA-MEDICA-BUILDER](https://github.com/drsamonline/MATERIA-MEDICA-BUILDER) | 1.0.0 |

### Health tools (`health-tools`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`bmi-bmr-tdee-macros-fluid-calculator`](skills/bmi-bmr-tdee-macros-fluid-calculator/SKILL.md) | A single-file, offline clinical calculator for adult outpatients: BMI, BMR (Mifflin-St Jeor), TDEE, macros, fluid requirement and body composition, with Indian/WHO cut-offs and EN/HI/GU UI. | [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) | 1.0.0 |
| [`boericke-repertory`](skills/boericke-repertory/SKILL.md) | A free, offline digital edition of Boericke's Repertory in one HTML file: instant search across 6,110 rubrics, a repertorisation chart over 1,461 remedies, a remedy browser, cases and print/export. | [boericke-repertory](https://github.com/drsamonline/boericke-repertory) | 1.0.0 |
| [`gentle-pediatrics-companion`](skills/gentle-pediatrics-companion/SKILL.md) | A triage-first offline companion app for a parent at the cot side: nine common childhood situations, an always-visible red-flag check, and gentle remedy orientation from the book Gentle Pediatrics. | [gentle-pediatrics-companion](https://github.com/drsamonline/gentle-pediatrics-companion) | 1.0.0 |
| [`hms-hospital-management`](skills/hms-hospital-management/SKILL.md) | HHMS: a LAN-based hospital management system for homeopathic hospitals — a Python server owns the SQLite database, a WebView2 client talks HTTP/JSON, and the server is found by UDP discovery; no internet, no cloud. | [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`mnemosyne-companion`](skills/mnemosyne-companion/SKILL.md) | A single offline HTML study companion for Mnemosyne Materia Medica: 100 polycrest remedies as poetic pearls, keynotes and spaced-repetition drills, in three drill modes. | [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) | 1.0.0 |
| [`open-materia-medica`](skills/open-materia-medica/SKILL.md) | A plain-language homeopathic materia medica — 344 remedy portraits, each beside the substance's real pharmacology and toxicology — as a static web edition plus a hand-written Android companion app. | [open-materia-medica](https://github.com/drsamonline/open-materia-medica) | 1.0.0 |
| [`read-live-transform-app`](skills/read-live-transform-app/SKILL.md) | An offline PWA companion to the book Read. Live. Transform. — a practical reading of the Qur'an in 74 chapters: read the verse, live the practice, keep the change. | [read-live-transform-app](https://github.com/drsamonline/read-live-transform-app) | 1.0.0 |
| [`remedy-relationship-explorer`](skills/remedy-relationship-explorer/SKILL.md) | An offline single-file explorer for homeopathic remedy relationships — 686 remedies, 7,786 links from four public-domain materia medicas — visualised as an interactive graph with keynotes, quizzes and a Tauri desktop build. | [remedy-relationship-explorer](https://github.com/drsamonline/remedy-relationship-explorer) | 1.0.0 |
| [`skin-case-tracker`](skills/skin-case-tracker/SKILL.md) | A private, offline PWA that tracks a skin case over time on the HHMS model — History, Habits, Mapping, Symptoms logged daily and read as a 90-day pattern engine; it records, it does not diagnose. | [skin-case-tracker](https://github.com/drsamonline/skin-case-tracker) | 1.0.0 |
| [`the-symphony-companion`](skills/the-symphony-companion/SKILL.md) | A pocket PWA companion to The Symphony of the Present: the book's ideas as cards, its practices as a checklist, a breathing timer, a gratitude journal and attributed quotations — pure CSS tabs, offline. | [the-symphony-companion](https://github.com/drsamonline/the-symphony-companion) | 1.0.0 |
| [`unstoppable-mind-companion`](skills/unstoppable-mind-companion/SKILL.md) | An offline companion app to The Unstoppable Mind: the book's key points and exercises, a 7-day challenge and flashcards — in a single ~30 KB file with no JavaScript at all. | [unstoppable-mind-companion](https://github.com/drsamonline/unstoppable-mind-companion) | 1.0.0 |
| [`whispering-body-first-aid`](skills/whispering-body-first-aid/SKILL.md) | A free, offline home first-aid companion (EN/HI/GU) with 30 commonly used homeopathic first-aid remedies, a plain-language symptom finder, dosing and handling guidance, and emergency signs. | [whispering-body-first-aid](https://github.com/drsamonline/whispering-body-first-aid) | 1.0.0 |

### Landing & SEO (`landing-and-seo`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`auto-updating-showcase-hub`](skills/auto-updating-showcase-hub/SKILL.md) | A single static page that lists every repository by reading the GitHub API at runtime, with an embedded JSON snapshot fallback, a curated map for hand-written copy, and a scheduled workflow that refreshes the snapshot. | [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io) | 1.0.0 |
| [`matneo-storefront`](skills/matneo-storefront/SKILL.md) | A static storefront served from docs/ with no build step: a single data file (docs/data/products.json) drives the catalogue, so new products are added by editing JSON, not markup. | [Matneo](https://github.com/drsamonline/Matneo) | 1.0.0 |
| [`profile-kit`](skills/profile-kit/SKILL.md) | A small, reusable kit for a theme-aware, self-updating GitHub profile — a hero banner, a metrics card and a README generator — extracted from the drsamonline profile so another account can adopt the whole thing instead of rebuilding it. | [profile-kit](https://github.com/drsamonline/profile-kit) | 1.0.0 |
| [`static-landing-page-seo`](skills/static-landing-page-seo/SKILL.md) | The house landing-page recipe: a bespoke self-contained docs/index.html with a distinct theme, a full SEO head (canonical, OG, Twitter, JSON-LD, robots), robots.txt, sitemap.xml, .nojekyll and a themed 404. | [app-builder](https://github.com/drsamonline/app-builder), [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json), [neon-runner](https://github.com/drsamonline/neon-runner), [conqueror-os](https://github.com/drsamonline/conqueror-os) | 1.0.0 |
| [`theme-aware-github-profile`](skills/theme-aware-github-profile/SKILL.md) | A professional, self-updating GitHub profile README — a bespoke light/dark hero served through <picture>, a lowlighter/metrics card rendered twice with extras_css palettes, and a daily workflow that regenerates a badge row and a categorised project list from the GitHub API between HTML comment markers. | [drsamonline](https://github.com/drsamonline/drsamonline), [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io), [profile-kit](https://github.com/drsamonline/profile-kit) | 1.0.0 |

### CI & release (`ci-and-release`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`app-builder-kit`](skills/app-builder-kit/SKILL.md) | The shared kit that turns a static web app into a single-file portable Windows EXE (PyInstaller) and an Android WebView APK (Gradle), consumed by app repos through one reusable GitHub Actions workflow. | [app-builder](https://github.com/drsamonline/app-builder) | 1.0.0 |
| [`reusable-build-release-workflow`](skills/reusable-build-release-workflow/SKILL.md) | One GitHub Actions workflow per app repo builds the portable EXE and Android APK, publishes them to a fixed-tag release, and gives permanent /releases/latest/download/<asset> URLs. | [app-builder](https://github.com/drsamonline/app-builder), [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`safe-repo-cleanup`](skills/safe-repo-cleanup/SKILL.md) | An audit-first procedure for removing build junk, caches, temp files, stale archives and duplicated README content from a repository without deleting anything that is referenced, committed source or a landing-page asset. | [skills](https://github.com/drsamonline/skills) | 1.0.0 |

### Marketing (`marketing`)

How a project is written about and how people find it — the discipline the system was missing. Adapted from the PolyForm Noncommercial-licensed [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) pack and rewritten to this system's rules (offline-first, no ads, no trackers).

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`directory-submissions`](skills/directory-submissions/SKILL.md) | Submit a project to a directory or an "awesome" list — a link, not a storefront — after checking its criteria, setting the repo's topics and writing a description per audience. | [drsamonline.github.io](https://github.com/drsamonline/drsamonline.github.io), [forge](https://github.com/drsamonline/forge) | 1.0.0 |
| [`free-tool-marketing`](skills/free-tool-marketing/SKILL.md) | Engineering as marketing: plan and judge a free, genuinely useful tool as the way people find the paid work — honestly, with no ads and no trackers. | [All4ONE](https://github.com/drsamonline/All4ONE), [TTB](https://github.com/drsamonline/TTB), [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) | 1.0.0 |
| [`product-copywriting`](skills/product-copywriting/SKILL.md) | Honest product copy for a landing page, README or store listing: diagnose first, lead with the reader's problem, gate every line, and cut the AI tells. | [open-materia-medica](https://github.com/drsamonline/open-materia-medica), [neon-runner](https://github.com/drsamonline/neon-runner), [Matneo](https://github.com/drsamonline/Matneo) | 1.0.0 |

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
