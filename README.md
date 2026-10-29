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

**Catalogue:** `605` skills across 24 categories. The machine-readable index is [`catalog.json`](catalog.json); the landing page is <https://drsamonline.github.io/skills/>.

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

`web-app-patterns`, `android-packaging`, `windows-desktop`, `game-engine`, `data-and-schema`, `health-tools`, `landing-and-seo`, `ci-and-release`, `marketing`, `linux-desktop`, `sysadmin-ops`, `code-quality`, `docs-and-planning`, `media-design`, `frontend-ui`, `backend-services`, `testing-qa`, `security-audit`, `cloud-and-deploy`, `ai-and-ml`, `office-docs`, `engineering-workflow`, `notes-knowledge`, `mobile-apps`.

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

### Web app patterns (`web-app-patterns`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`ambient-sound-studio`](skills/ambient-sound-studio/SKILL.md) | A private, offline ambient sound mixer in a single HTML file: 25 synthesised layers, 36 presets, EN/HI/GU, WAV and Opus export, installable PWA. | [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio) | 1.0.0 |
| [`astro-kit-panchang`](skills/astro-kit-panchang/SKILL.md) | Sun and moon longitude (Meeus), Lahiri ayanamsa, sunrise/sunset/transit and the derived tithi, nakshatra, yoga and karana — the astronomy core for an offline panchang. | [astro-kit](https://github.com/drsamonline/astro-kit), [app-panchang](https://github.com/drsamonline/app-panchang) | 1.0.0 |
| [`blinkcode-ai-spectracode`](skills/blinkcode-ai-spectracode/SKILL.md) | Optical file transfer as a vanilla-JS PWA: a file becomes a 'File DNA' container painted as SpectraCode colour matrices, decoded by camera with marker detection, homography and Reed-Solomon error correction. | [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) | 1.0.0 |
| [`blinktransfer-animated-qr`](skills/blinktransfer-animated-qr/SKILL.md) | Offline file transfer over animated QR codes at ~20 FPS: a Vite-built PWA compresses files, renders a header plus a data stream of 1600-byte frames, and reassembles them on a receiver camera. | [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) | 1.0.0 |
| [`book-kit-companion`](skills/book-kit-companion/SKILL.md) | The companion-app-from-a-book pattern in one zero-dependency file: chapters, key points, practices, flashcards, in-book search and reading progress with notes. | [book-kit](https://github.com/drsamonline/book-kit), [whispering-body-first-aid](https://github.com/drsamonline/whispering-body-first-aid), [gentle-pediatrics-companion](https://github.com/drsamonline/gentle-pediatrics-companion), [the-symphony-companion](https://github.com/drsamonline/the-symphony-companion), [unstoppable-mind-companion](https://github.com/drsamonline/unstoppable-mind-companion), [read-live-transform-app](https://github.com/drsamonline/read-live-transform-app) | 1.0.0 |
| [`compress-kit-streams`](skills/compress-kit-streams/SKILL.md) | gzip, deflate and deflate-raw over the platform's Compression Streams, with byte and base64 helpers — the browser counterpart to lexora. | [compress-kit](https://github.com/drsamonline/compress-kit), [lexora](https://github.com/drsamonline/lexora), [kent-repertory-explorer](https://github.com/drsamonline/kent-repertory-explorer), [offline-pdf-toolkit](https://github.com/drsamonline/offline-pdf-toolkit) | 1.0.0 |
| [`conqueror-os-workspace`](skills/conqueror-os-workspace/SKILL.md) | A private, offline resilience workspace in a single HTML file — read, reflect, journal, track and review — with no server, no account and no dependencies. | [conqueror-os](https://github.com/drsamonline/conqueror-os) | 1.0.0 |
| [`crypto-kit-aes-gcm`](skills/crypto-kit-aes-gcm/SKILL.md) | AES-256-GCM encryption with PBKDF2-SHA256 passphrase keys, a sealed envelope and a one-time-view helper on the Web Crypto API — the one place crypto lives. | [crypto-kit](https://github.com/drsamonline/crypto-kit), [lockhtml](https://github.com/drsamonline/lockhtml), [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log), [seance](https://github.com/drsamonline/seance) | 1.0.0 |
| [`lan-kit-sse-room`](skills/lan-kit-sse-room/SKILL.md) | A LAN room in the browser: a client over Server-Sent Events for server-to-client and POST for client-to-server, with a host URL helper — no internet, no accounts. | [lan-kit](https://github.com/drsamonline/lan-kit), [canteen-lan](https://github.com/drsamonline/canteen-lan), [chalk-lan](https://github.com/drsamonline/chalk-lan), [app-companion-forge](https://github.com/drsamonline/app-companion-forge) | 1.0.0 |
| [`lan-single-server-architecture`](skills/lan-single-server-architecture/SKILL.md) | A multi-user system that runs entirely on a hospital LAN: a Python server owns the SQLite database, a vanilla-JS UI runs in a WebView2 client, and the server is discovered by UDP broadcast — no internet, no cloud. | [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`offline-first-single-file-web-app`](skills/offline-first-single-file-web-app/SKILL.md) | Build a whole app as one self-contained index.html — inline CSS/JS, no CDN, no build step — that runs from file:// or GitHub Pages, works offline, and persists data locally. | [conqueror-os](https://github.com/drsamonline/conqueror-os), [ambient-sound-studio](https://github.com/drsamonline/ambient-sound-studio), [neon-runner](https://github.com/drsamonline/neon-runner), [boericke-repertory](https://github.com/drsamonline/boericke-repertory), [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator), [retro-strike](https://github.com/drsamonline/retro-strike), [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth) | 1.0.0 |
| [`optical-file-transfer`](skills/optical-file-transfer/SKILL.md) | Move a file between two devices with no network, Bluetooth or cable, by rendering it as animated QR codes or colour-matrix frames and reading them back with a camera. | [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER), [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) | 1.0.0 |
| [`optical-kit-fountain`](skills/optical-kit-fountain/SKILL.md) | A systematic LT fountain code with self-describing frames and a pluggable codec — the shared optical-transfer core behind the QR and colour-matrix senders. | [optical-kit](https://github.com/drsamonline/optical-kit), [frame-kit](https://github.com/drsamonline/frame-kit), [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER), [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai), [helioprism](https://github.com/drsamonline/helioprism) | 1.0.0 |
| [`qr-code-encoder`](skills/qr-code-encoder/SKILL.md) | A QR encoder in one dependency-free file: byte mode, ECC L/M/Q/H, versions 1-40, Reed-Solomon over GF(256) and the ISO/IEC 18004 block tables — for rendering a code offline without shipping a QR library. | [TTB](https://github.com/drsamonline/TTB), [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER), [helioprism](https://github.com/drsamonline/helioprism), [optical-kit](https://github.com/drsamonline/optical-kit) | 1.0.0 |
| [`smartbill-app`](skills/smartbill-app/SKILL.md) | A fast, serverless single-page billing and invoicing app for Indian businesses: GST-ready (HSN/SAC, CGST/SGST, state codes, reverse charge), 100% local IndexedDB storage and A4 print layout. | [smartbill-app](https://github.com/drsamonline/smartbill-app) | 1.0.0 |
| [`smartnotes-ai-notes`](skills/smartnotes-ai-notes/SKILL.md) | An AI-powered note capture, categorisation and reminder-scheduling app with a brutalist UI: write in plain English and an LLM classifies, prioritises, titles and extracts dates. | [SmartNotes](https://github.com/drsamonline/SmartNotes) | 1.0.0 |
| [`srs-kit-sm2`](skills/srs-kit-sm2/SKILL.md) | Schedule flashcards with SM-2 in one zero-dependency file: ease, interval, reps, lapses, due cards, stats and a configurable cadence. | [srs-kit](https://github.com/drsamonline/srs-kit), [conqueror-os](https://github.com/drsamonline/conqueror-os), [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) | 1.0.0 |
| [`ttb-tiny-toolbox-extension`](skills/ttb-tiny-toolbox-extension/SKILL.md) | A Manifest V3 browser extension bundling 590 small utilities across 18 categories into one offline-first popup, with one source tree assembled per browser by a small build. | [TTB](https://github.com/drsamonline/TTB) | 1.0.0 |
| [`ui-kit`](skills/ui-kit/SKILL.md) | A reactive UI layer small enough for a single file — signals, computed, reactive effects, hyperscript, a keyed list, events, a hash router and two-way form binding. Zero runtime dependencies, no build step. | [ui-kit](https://github.com/drsamonline/ui-kit), [web-kit](https://github.com/drsamonline/web-kit) | 1.0.0 |

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
| [`art-kit`](skills/art-kit/SKILL.md) | The art primitives for offline apps — an indexed palette, a pixel canvas with nearest-neighbour scaling, draw ops, a delta undo stack, dithering (Bayer + Floyd-Steinberg), median-cut quantisation, sprite sheets, the isometric mapping and a sketch loop. Zero dependencies, single file, no assets. | [art-kit](https://github.com/drsamonline/art-kit), [game-kit](https://github.com/drsamonline/game-kit) | 1.0.0 |
| [`audio-kit`](skills/audio-kit/SKILL.md) | Synthesis, theory, patterns and notation for offline apps — a pure ADSR envelope, oscillator voices, filters, noise and a mixer; notes, scales and chords; a pattern sequencer; a staff layout; byte sonification; and honest mastering helpers. Zero dependencies, single file, no audio assets. | [audio-kit](https://github.com/drsamonline/audio-kit), [game-kit](https://github.com/drsamonline/game-kit) | 1.0.0 |
| [`dance-fight-rhythm-game`](skills/dance-fight-rhythm-game/SKILL.md) | A single-file browser rhythm game where every fight move is a dance move: the track's beat is analysed up front into an offline beat grid, and on-beat hits score PERFECT for 60% extra damage. | [dance-fight](https://github.com/drsamonline/dance-fight) | 1.0.0 |
| [`game-kit-fixed-timestep`](skills/game-kit-fixed-timestep/SKILL.md) | A fixed-timestep game loop with input, scenes and save/load in one dependency-free file — the shared game core the browser games should run on. | [game-kit](https://github.com/drsamonline/game-kit), [neon-runner](https://github.com/drsamonline/neon-runner), [retro-strike](https://github.com/drsamonline/retro-strike), [dance-fight](https://github.com/drsamonline/dance-fight), [Scrap-and-Gun](https://github.com/drsamonline/Scrap-and-Gun), [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth), [neon-games](https://github.com/drsamonline/neon-games) | 1.0.0 |
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
| [`ml-kit`](skills/ml-kit/SKILL.md) | The classic ML algorithms from scratch for offline features — tf-idf ranking, Naive Bayes, k-NN, k-means, PCA, ID3, linear regression, Markov chains and grammar generation. Zero dependencies, single file. | [ml-kit](https://github.com/drsamonline/ml-kit), [search-kit](https://github.com/drsamonline/search-kit) | 1.0.0 |
| [`open-data-extraction-pipeline`](skills/open-data-extraction-pipeline/SKILL.md) | Turn raw OCR'd source texts into clean, app-ready JSON with a verbatim-fidelity rule: nothing invented, unknowns null, per-book QC, a self-describing schema and a reproducible pipeline. | [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json), [MATERIA-MEDICA-BUILDER](https://github.com/drsamonline/MATERIA-MEDICA-BUILDER) | 1.0.0 |
| [`search-kit-ranked-search`](skills/search-kit-ranked-search/SKILL.md) | Ranked search over a big corpus in one zero-dependency file: an inverted index with prefix and fuzzy matching, scored hits and a vocabulary size. | [search-kit](https://github.com/drsamonline/search-kit), [app-poets-studio](https://github.com/drsamonline/app-poets-studio), [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log), [open-materia-medica](https://github.com/drsamonline/open-materia-medica) | 1.0.0 |

### Health tools (`health-tools`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`bmi-bmr-tdee-macros-fluid-calculator`](skills/bmi-bmr-tdee-macros-fluid-calculator/SKILL.md) | A single-file, offline clinical calculator for adult outpatients: BMI, BMR (Mifflin-St Jeor), TDEE, macros, fluid requirement and body composition, with Indian/WHO cut-offs and EN/HI/GU UI. | [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) | 1.0.0 |
| [`boericke-repertory`](skills/boericke-repertory/SKILL.md) | A free, offline digital edition of Boericke's Repertory in one HTML file: instant search across 6,110 rubrics, a repertorisation chart over 1,461 remedies, a remedy browser, cases and print/export. | [boericke-repertory](https://github.com/drsamonline/boericke-repertory) | 1.0.0 |
| [`case-kit-clinical`](skills/case-kit-clinical/SKILL.md) | Clinical case tracking in one zero-dependency file: sections, dated symptoms with severity, follow-ups with remedy and response, a timeline, a summary and a plain-JSON interchange record. | [case-kit](https://github.com/drsamonline/case-kit), [skin-case-tracker](https://github.com/drsamonline/skin-case-tracker), [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log), [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`gentle-pediatrics-companion`](skills/gentle-pediatrics-companion/SKILL.md) | A triage-first offline companion app for a parent at the cot side: nine common childhood situations, an always-visible red-flag check, and gentle remedy orientation from the book Gentle Pediatrics. | [gentle-pediatrics-companion](https://github.com/drsamonline/gentle-pediatrics-companion) | 1.0.0 |
| [`hms-hospital-management`](skills/hms-hospital-management/SKILL.md) | HHMS: a LAN-based hospital management system for homeopathic hospitals — a Python server owns the SQLite database, a WebView2 client talks HTTP/JSON, and the server is found by UDP discovery; no internet, no cloud. | [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`mnemosyne-companion`](skills/mnemosyne-companion/SKILL.md) | A single offline HTML study companion for Mnemosyne Materia Medica: 100 polycrest remedies as poetic pearls, keynotes and spaced-repetition drills, in three drill modes. | [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) | 1.0.0 |
| [`open-materia-medica`](skills/open-materia-medica/SKILL.md) | A plain-language homeopathic materia medica — 344 remedy portraits, each beside the substance's real pharmacology and toxicology — as a static web edition plus a hand-written Android companion app. | [open-materia-medica](https://github.com/drsamonline/open-materia-medica) | 1.0.0 |
| [`read-live-transform-app`](skills/read-live-transform-app/SKILL.md) | An offline PWA companion to the book Read. Live. Transform. — a practical reading of the Qur'an in 74 chapters: read the verse, live the practice, keep the change. | [read-live-transform-app](https://github.com/drsamonline/read-live-transform-app) | 1.0.0 |
| [`remedy-relationship-explorer`](skills/remedy-relationship-explorer/SKILL.md) | An offline single-file explorer for homeopathic remedy relationships — 686 remedies, 7,786 links from four public-domain materia medicas — visualised as an interactive graph with keynotes, quizzes and a Tauri desktop build. | [remedy-relationship-explorer](https://github.com/drsamonline/remedy-relationship-explorer) | 1.0.0 |
| [`repertory-kit-repertorisation`](skills/repertory-kit-repertorisation/SKILL.md) | Grade-weighted homeopathic repertorisation in one zero-dependency file: rubric grading 1/2/3, remedy scoring, must-have and exclude filters, ranked results. | [repertory-kit](https://github.com/drsamonline/repertory-kit), [boericke-repertory](https://github.com/drsamonline/boericke-repertory), [kent-repertory-explorer](https://github.com/drsamonline/kent-repertory-explorer), [homoeopathic-materia-medica-repertory-json](https://github.com/drsamonline/homoeopathic-materia-medica-repertory-json) | 1.0.0 |
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
| [`app-builder-kit`](skills/app-builder-kit/SKILL.md) | The shared kit that turns a static web app into a single-file portable Windows EXE (PyInstaller) and an Android WebView APK (Gradle), consumed by app repos through one reusable GitHub Actions workflow. | [app-builder](https://github.com/drsamonline/app-builder) | 1.1.0 |
| [`kit-adoption-audit`](skills/kit-adoption-audit/SKILL.md) | Measure which apps actually consume each shared kit and which hand-roll the same capability, from repository trees and blob SHAs alone, before proposing a kit create, update or retire. | [skills](https://github.com/drsamonline/skills), [web-kit](https://github.com/drsamonline/web-kit), [forge](https://github.com/drsamonline/forge), [repertory-kit](https://github.com/drsamonline/repertory-kit), [srs-kit](https://github.com/drsamonline/srs-kit) | 1.0.0 |
| [`reusable-build-release-workflow`](skills/reusable-build-release-workflow/SKILL.md) | One GitHub Actions workflow per app repo builds the portable EXE and Android APK, publishes them to a fixed-tag release, and gives permanent /releases/latest/download/<asset> URLs. | [app-builder](https://github.com/drsamonline/app-builder), [HMS](https://github.com/drsamonline/HMS) | 1.0.0 |
| [`safe-repo-cleanup`](skills/safe-repo-cleanup/SKILL.md) | An audit-first procedure for removing build junk, caches, temp files, stale archives and duplicated README content from a repository without deleting anything that is referenced, committed source or a landing-page asset. | [skills](https://github.com/drsamonline/skills), [NEO](https://github.com/drsamonline/NEO), [HMS](https://github.com/drsamonline/HMS), [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER), [conqueror-os](https://github.com/drsamonline/conqueror-os), [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion), [retro-strike](https://github.com/drsamonline/retro-strike), [idle-city-ages-of-growth](https://github.com/drsamonline/idle-city-ages-of-growth), [SmartNotes](https://github.com/drsamonline/SmartNotes) | 1.0.0 |

### Marketing (`marketing`)

How a project is written about and how people find it — the discipline the system was missing. Adapted from the PolyForm Noncommercial-licensed [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) pack and rewritten to this system's rules (offline-first, no ads, no trackers).

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`directory-submissions`](skills/directory-submissions/SKILL.md) | Submit a project to a directory or an "awesome" list — a link, not a storefront — so people and AI engines can find it. |  | 1.0.0 |
| [`free-tool-marketing`](skills/free-tool-marketing/SKILL.md) | Plan and judge a free, genuinely useful tool as the way people find the paid work — engineering as marketing. |  | 1.0.0 |
| [`product-copywriting`](skills/product-copywriting/SKILL.md) | Write honest product copy for a landing page, a README or a store listing — a headline, a value line, a CTA — that reads like a person wrote it and a competitor could not. |  | 1.0.0 |

### Linux desktop (`linux-desktop`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`dwm-titus`](skills/dwm-titus/SKILL.md) | Customize the dwm-titus X11 desktop, including TOML keybindings, themes, window rules, panel widgets, autostart, wallpaper, picom, lock, and LightDM. Use for end-user changes, not diagnosis. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`dwm-titus-debug`](skills/dwm-titus-debug/SKILL.md) | Diagnose broken apps or desktop parts on dwm-titus, including startup, Quickshell panel, keybindings, window rules, autostart, portals, picom, lock, and crashes. Read-only unless asked; not host services. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`pack-linux-desktop`](skills/pack-linux-desktop/SKILL.md) | Chris Titus Tech's Fedora/X11 desktop end to end: change dwm keybindings, themes and window rules, build or lint the Quickshell panel, and diagnose a broken session read-only. Use for any change to, or failure of, a dwm-titus desktop. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`quickshell`](skills/quickshell/SKILL.md) | Build, lint, and troubleshoot Quickshell QML configurations or source builds. Use for shell.qml, Quickshell modules, qmllint setup, runtime validation, packaging, and version-matched API guidance. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |

### Sysadmin & ops (`sysadmin-ops`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`forgejo-maintainer`](skills/forgejo-maintainer/SKILL.md) | Administer Forgejo or Gitea installations, including upgrades, backups, migrations, repository access, and Actions runners. Use for application-specific operations, not general Linux host troubleshooting. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`homelab-admin`](skills/homelab-admin/SKILL.md) | Operate homelab infrastructure spanning networking, DNS, storage, NFS, reverse proxies, or multiple services. Use for cross-system work rather than an isolated host, application, or container problem. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`linux-sysadmin`](skills/linux-sysadmin/SKILL.md) | Diagnose and operate Linux hosts, services, packages, permissions, SELinux, firewalls, and SSH. Use for host-level work that is not primarily an application-specific or container task. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`pack-sysadmin-ops`](skills/pack-sysadmin-ops/SKILL.md) | Infrastructure administration in one pack: Linux host diagnostics (services, packages, SELinux, firewalls, SSH), Podman containers and Quadlet units, Forgejo/Gitea upgrades, backups and runners, and cross-system homelab work. Use for operations that span a host, its containers and its services. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`podman-operator`](skills/podman-operator/SKILL.md) | Build and operate Podman containers and Quadlet services, including rootless deployment, networking, volumes, systemd integration, and troubleshooting. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |

### Code quality (`code-quality`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`autofix`](skills/autofix/SKILL.md) | Address CodeRabbit pull-request feedback with verified fixes and validation. Run publication and repeated review cycles only within the user's authorized scope. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`bash-scripting`](skills/bash-scripting/SKILL.md) | Create, review, and debug Bash or POSIX sh scripts when portability, quoting, failure handling, or shell-specific validation matters. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`code-review`](skills/code-review/SKILL.md) | Review code with CodeRabbit when the user requests CodeRabbit or repository policy selects it. Do not replace a required Codex review. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`pack-code-quality`](skills/pack-code-quality/SKILL.md) | The review-to-merge loop for a change: run CodeRabbit review, fix its findings with verified patches, decide whether a PR is actually merge-ready, and write the portable Bash that runs the gates. Use when reviewing a diff, answering review feedback, or judging a PR. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`pr-readiness`](skills/pr-readiness/SKILL.md) | Validate changes and pull requests through merge readiness, including local gates, Codex review, CI, independent review, manual evidence, and unresolved review threads. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |

### Planning & docs (`docs-and-planning`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`ai-project-manager`](skills/ai-project-manager/SKILL.md) | Create and maintain repository planning documents, phased implementation plans, approval checkpoints, task status, and validation evidence for AI-assisted development work. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`hugo`](skills/hugo/SKILL.md) | Build, edit, validate, and troubleshoot Hugo sites, including content, templates, assets, taxonomies, redirects, output formats, and deployment configuration. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`mdbook`](skills/mdbook/SKILL.md) | Create, edit, validate, and publish mdBook projects or mdBook-based KDP manuscripts. Use for book.toml, SUMMARY.md, themes, preprocessors, CI, and manuscript conversion. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`pack-planning-and-docs`](skills/pack-planning-and-docs/SKILL.md) | Write the plan down and publish the documentation: repository planning documents (SPEC, ROADMAP, TASKS) for AI-assisted work, Wayfinder's SPEC/MAP/ANSWERS for foggy destinations, Hugo sites, and mdBook books or KDP manuscripts. Use when a task needs a durable plan or a documentation site. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`wayfinder`](skills/wayfinder/SKILL.md) | Create or maintain SPEC.md, MAP.md, and ANSWERS.md for large or unclear work. Invoke only with /wayfinder or $wayfinder; do not use for ordinary planning or implementation. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |

### Media & design (`media-design`)

| Skill | Description | Source repos | Ver |
|---|---|---|---|
| [`pack-media-design`](skills/pack-media-design/SKILL.md) | Cover and image work: design a restrained 16:9 YouTube thumbnail around one readable idea while keeping photographed people exactly as they are, and create, composite or export layered images through the photocraft-cli MCP server. Use when a thumbnail, logo, cover or photo composite is needed. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`photocraft`](skills/photocraft/SKILL.md) | Create, inspect, edit, composite, and export images through the photocraft-cli MCP server. Use for image work, layered artwork, photo edits, logos, and thumbnail assembly; combine with task-specific design skills when applicable. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |
| [`youtube-thumbnail`](skills/youtube-thumbnail/SKILL.md) | Create, edit, or review YouTube thumbnails. Always use when a YouTube thumbnail or video cover is requested; keep the design restrained and preserve photographed people exactly. | [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) | 1.0.0 |

### Frontend & UI (`frontend-ui`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-frontend-ui`](skills/pack-frontend-ui/SKILL.md) | Interface work end to end: React and Next.js performance, composition and view transitions, CSS and layout craft, animation and motion, visual design… | **pack** | mixed |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`animate`](skills/animate/SKILL.md) | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose,… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`animation-performance`](skills/animation-performance/SKILL.md) | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`animation-vocabulary`](skills/animation-vocabulary/SKILL.md) | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`apple-design`](skills/apple-design/SKILL.md) | Apple's approach to interface design and fluid, physical motion, translated for the web. | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`ask-sonner`](skills/ask-sonner/SKILL.md) | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating,… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`break-ui`](skills/break-ui/SKILL.md) | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items,… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`buddy-sings`](skills/buddy-sings/SKILL.md) | Turn your Claude Code pet into a singer. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`canvas-design`](skills/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`color-font-skill`](skills/color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`design-style-skill`](skills/design-style-skill/SKILL.md) | 同一套设计可通过调整圆角（rectRadius）和间距呈现4种不同风格。根据场景选择合适的风格配方。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`emil-design-eng`](skills/emil-design-eng/SKILL.md) | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`find-animation-opportunities`](skills/find-animation-opportunities/SKILL.md) | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`frontend-dev`](skills/frontend-dev/SKILL.md) | Build complete, production-ready frontend pages by orchestrating 5 specialized capabilities: design engineering, motion systems, AI-generated assets,… | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`frontend-ui-engineering`](skills/frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`gif-sticker-maker`](skills/gif-sticker-maker/SKILL.md) | Convert user photos into 4 animated GIF stickers (Funko Pop / Pop Mart style). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`improve-animations`](skills/improve-animations/SKILL.md) | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`minimax-music-gen`](skills/minimax-music-gen/SKILL.md) | Generate songs (vocal or instrumental) using the MiniMax Music API. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`minimax-music-playlist`](skills/minimax-music-playlist/SKILL.md) | Scan the user's music taste, build a taste profile, generate a personalized playlist, and create an album cover. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`mmx-cli`](skills/mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`mobile-native`](skills/mobile-native/SKILL.md) | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`pick-ui-library`](skills/pick-ui-library/SKILL.md) | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`pr-review`](skills/pr-review/SKILL.md) | Review pull requests against repository standards. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`remove-animations`](skills/remove-animations/SKILL.md) | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`review-animations`](skills/review-animations/SKILL.md) | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`shader-dev`](skills/shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid simulation, particle systems,… | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`theme-factory`](skills/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`vercel-composition-patterns`](skills/vercel-composition-patterns/SKILL.md) | Composition patterns for building flexible, maintainable React components. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`vercel-react-view-transitions`](skills/vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and… | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`vision-analysis`](skills/vision-analysis/SKILL.md) | Analyze images using the MiniMax MiniMaxunderstandimage MCP tool available in the MiniMax Token Plan. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`write-swift`](skills/write-swift/SKILL.md) | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent,… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |

### Backend & services (`backend-services`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-backend-services`](skills/pack-backend-services/SKILL.md) | Server-side work: Node.js and TypeScript practice, Fastify REST APIs, OAuth 2.0/2.1 flows, advanced type design, API and module boundaries, and… | **pack** | mixed |
| [`360-feedback-system`](skills/360-feedback-system/SKILL.md) | 360 feedback register: reviewer, subject, review cycle, visibility, due date and score, as CSV, SQL, JSON Schema or Notion on request. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`accounting-software-selection`](skills/accounting-software-selection/SKILL.md) | Scores shortlisted accounting packages against 57 evidence-backed fields, emitted as CSV, SQL, JSON Schema or Notion on request. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`api-and-interface-design`](skills/api-and-interface-design/SKILL.md) | Guides stable API and interface design. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`claude-api`](skills/claude-api/SKILL.md) | This skill helps you build LLM-powered applications with Claude. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`fastify-best-practices`](skills/fastify-best-practices/SKILL.md) | Guides development of Fastify Node.js backend servers and REST APIs using TypeScript or JavaScript. | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`fullstack-dev`](skills/fullstack-dev/SKILL.md) | When this skill is triggered, you MUST follow this workflow before writing any code. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`hunt-graphql`](skills/hunt-graphql/SKILL.md) | Hunting skill for graphql vulnerabilities. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`node`](skills/node/SKILL.md) | Provides domain-specific best practices for Node.js development with TypeScript, covering type stripping, async patterns, error handling, streams,… | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`nodejs-core`](skills/nodejs-core/SKILL.md) | Contributes to and debugs Node.js core, including nodejs/node commit and PR tone, contribution workflows, native crashes, V8 performance, node-gyp… | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`oauth`](skills/oauth/SKILL.md) | Implements OAuth 2.0/2.1 authorization flows in Fastify applications — configures authorization code with PKCE, client credentials, device flow,… | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`snipgrapher`](skills/snipgrapher/SKILL.md) | Configures and uses snipgrapher to generate polished code snippet images, including syntax-highlighted PNGs, SVGs, and WebP exports with custom… | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`tinystruct-patterns`](skills/tinystruct-patterns/SKILL.md) | Expert guidance for developing with the tinystruct Java framework. | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`typescript-magician`](skills/typescript-magician/SKILL.md) | Designs complex generic types, refactors `any` types to strict alternatives, creates type guards and utility types, and resolves TypeScript compiler… | [mcollina/skills](https://github.com/mcollina/skills) | MIT |

### Testing & QA (`testing-qa`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-testing-qa`](skills/pack-testing-qa/SKILL.md) | Test work in one place: Playwright patterns for E2E, component and API tests, page objects, CI wiring and Cypress/Selenium migration, browser testing… | **pack** | mixed |
| [`browser-testing-with-devtools`](skills/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`playwright-ci`](skills/playwright-ci/SKILL.md) | Production-ready CI/CD configurations for Playwright — GitHub Actions, GitLab CI, CircleCI, Azure DevOps, Jenkins, Docker, parallel sharding,… | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-cli`](skills/playwright-cli/SKILL.md) | Automates browser interactions for testing and validating your own web applications using playwright-cli. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-core`](skills/playwright-core/SKILL.md) | Battle-tested Playwright patterns for writing and debugging reliable E2E, API, component, visual, accessibility, and security tests. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-frontend`](skills/playwright-frontend/SKILL.md) | For frontend engineers authoring UI — how to make components reliably locatable by tests and AI agents. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-migration`](skills/playwright-migration/SKILL.md) | Step-by-step migration guides for moving to Playwright from Cypress or Selenium/WebDriver — command mappings, architecture changes, and incremental… | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-pom`](skills/playwright-pom/SKILL.md) | Page Object Model patterns for Playwright — when to use POM, how to structure page objects, and when fixtures or helpers are a better fit. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-qa`](skills/playwright-qa/SKILL.md) | QA engineering workflows on top of Playwright. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`playwright-skill`](skills/playwright-skill/SKILL.md) | Current Playwright (1.64) patterns for writing, debugging, and scaling reliable test suites. | [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) | MIT |
| [`tdd`](skills/tdd/SKILL.md) | Test-driven development. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`verification-before-completion`](skills/verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |

### Security & audit (`security-audit`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-security-audit`](skills/pack-security-audit/SKILL.md) | Security review of code, APIs, services, CLIs and libraries: vulnerability classes to look for, hardening an input handler, adversarial review of a… | **pack** | mixed |
| [`constraint-driven-development`](skills/constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`doubt-driven-development`](skills/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`flutter-dart-code-review`](skills/flutter-dart-code-review/SKILL.md) | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX,… | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`git-guardrails-claude-code`](skills/git-guardrails-claude-code/SKILL.md) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`laravel-security`](skills/laravel-security/SKILL.md) | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment… | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`mle-workflow`](skills/mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`security-and-hardening`](skills/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`security-audit`](skills/security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | MIT |
| [`zeroize-audit`](skills/zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level… | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |

### Cloud & deploy (`cloud-and-deploy`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-cloud-and-deploy`](skills/pack-cloud-and-deploy/SKILL.md) | Everything between a working tree and a running system on Google Cloud: 180+ product skills covering BigQuery, GKE, Cloud Run, Vertex, Apigee, Cloud… | **pack** | mixed |
| [`agent-platform-alert-configuration`](skills/agent-platform-alert-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-deploy`](skills/agent-platform-deploy/SKILL.md) | This skill provides instructions for deploying Open Models from Agent Platform Model Garden to endpoints, and subsequently undeploying them to clean… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-endpoint-management`](skills/agent-platform-endpoint-management/SKILL.md) | This skill provides procedural knowledge for managing Agent Platform Endpoints. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-eval-flywheel`](skills/agent-platform-eval-flywheel/SKILL.md) | Help users evaluate and iteratively improve GenAI models and agents using the Agent Platform GenAI Evaluation SDK (google.genai / agentplatform). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-inference`](skills/agent-platform-inference/SKILL.md) | This skill provides instructions for authenticating and connecting to Google Cloud Agent Platform to use Generative AI models. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-migrate-from-ai-studio`](skills/agent-platform-migrate-from-ai-studio/SKILL.md) | Use this skill when you need to transition an application from the developer-centric Google AI Studio ecosystem (generativelanguage.googleapis.com)… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-model-registry`](skills/agent-platform-model-registry/SKILL.md) | This skill provides instructions for managing machine learning models in the Agent Platform Model Registry. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-prompt-management`](skills/agent-platform-prompt-management/SKILL.md) | 1. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-rag-engine-management`](skills/agent-platform-rag-engine-management/SKILL.md) | This skill provides instructions on how to interact with Agent Platform RAG Engine using the Agent Platform Python SDK. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-skill-registry`](skills/agent-platform-skill-registry/SKILL.md) | This skill provides instructions for interacting with the Skill Registry on the Gemini Enterprise Agent Platform. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-troubleshooting`](skills/agent-platform-troubleshooting/SKILL.md) | !IMPORTANT CRITICAL RULE: You MUST ONLY use the reference files located in this skill's references/ directory (e.g., references/field-manual.md,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-tuning`](skills/agent-platform-tuning/SKILL.md) | This skill provides procedural knowledge for fine-tuning Large Language Models (both Open Models and Gemini Models) using Agent Platform's tuning… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`agent-platform-tuning-management`](skills/agent-platform-tuning-management/SKILL.md) | This skill provides instructions on how to manage GenAI Tuning Jobs using the Agent Platform Python SDK. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`alloydb-basics`](skills/alloydb-basics/SKILL.md) | AlloyDB for PostgreSQL is a managed, PostgreSQL-compatible database service designed for enterprise-grade performance and availability. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`api-gateway-backend-security-and-rate-limiting`](skills/api-gateway-backend-security-and-rate-limiting/SKILL.md) | This skill configures client authentication, gateway-to-backend authentication, and per-project rate limits (quotas) for Google Cloud API Gateway… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`api-gateway-mcp-server`](skills/api-gateway-mcp-server/SKILL.md) | This skill converts new or existing REST APIs on Google Cloud API Gateway into remote Model Context Protocol (MCP) servers (POST… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`apigee-agent-gateway-governance`](skills/apigee-agent-gateway-governance/SKILL.md) | Wires an Apigee proxy in as an ext-proc callout on a GCP Agent Gateway. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`application-design-center-design-deploy`](skills/application-design-center-design-deploy/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`application-integration-authoring`](skills/application-integration-authoring/SKILL.md) | Google Cloud Application Integration workflows are authored, versioned, published, and executed programmatically through the REST API… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`application-integration-basics`](skills/application-integration-basics/SKILL.md) | Application Integration is Google Cloud's serverless, auto-scaling Integration-Platform-as-a-Service (iPaaS) for connecting Google Cloud services and… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`application-integration-troubleshooting`](skills/application-integration-troubleshooting/SKILL.md) | Diagnose and recover Google Cloud Application Integration executions that fail, stall, or appear to do nothing. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`assured-workloads-basics`](skills/assured-workloads-basics/SKILL.md) | Validate prerequisites, create Assured Workloads V1 compliant folders, allowlist compliant services, and list, inspect, update, or delete existing… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`assuredworkloads-environment-assessor`](skills/assuredworkloads-environment-assessor/SKILL.md) | This skill performs zero-risk, non-mutating compliance discovery, physical telemetry profiling, and data boundary framework recommendation across… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`assuredworkloads-frameworks-author`](skills/assuredworkloads-frameworks-author/SKILL.md) | You are an authoritative Data Boundary Compliance Architect / Author. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`assuredworkloads-frameworks-navigator`](skills/assuredworkloads-frameworks-navigator/SKILL.md) | You are a Compliance Analyst specializing in Google Cloud Data Boundary Frameworks and cloud controls. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-ai-ml`](skills/bigquery-ai-ml/SKILL.md) | BigQuery integrates with Vertex AI to provide powerful machine learning and generative AI capabilities directly within SQL queries using built-in… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-basics`](skills/bigquery-basics/SKILL.md) | BigQuery is a serverless, AI-ready data platform that enables high-speed analysis of large datasets using SQL and Python. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-bigframes`](skills/bigquery-bigframes/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-migration-sql-translator`](skills/bigquery-migration-sql-translator/SKILL.md) | The BigQuery Migration Service (BQMS) translates legacy database SQL scripts, queries, and schemas into GoogleSQL. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-observability`](skills/bigquery-observability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-optimization`](skills/bigquery-optimization/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-troubleshooting`](skills/bigquery-troubleshooting/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigquery-udfs`](skills/bigquery-udfs/SKILL.md) | BigQuery User-Defined Functions (UDFs) extend GoogleSQL with custom logic written in SQL, JavaScript, managed Python (python-3.11), or hosted… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`bigtable-basics`](skills/bigtable-basics/SKILL.md) | This skill provides core workflows and guidance for administering and developing with Google Bigtable. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`ci-cd-and-automation`](skills/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`cloud-armor-crs-rule-upgrader`](skills/cloud-armor-crs-rule-upgrader/SKILL.md) | This skill guides Network Security Agents and Google Cloud practitioners through auditing, assessing, and upgrading Google Cloud Armor security… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-build-basics`](skills/cloud-build-basics/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-databases-onboarding`](skills/cloud-databases-onboarding/SKILL.md) | This skill provides domain instructions, decision matrices, and Infrastructure-as-Code workflows to guide users through discovering their exact… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-logging-configuration-basics`](skills/cloud-logging-configuration-basics/SKILL.md) | Use this skill to configure Cloud Logging resources such as log buckets, log views, or log sinks. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-logging-cross-project-configuration`](skills/cloud-logging-cross-project-configuration/SKILL.md) | This skill describes how to use gcloud commands to configure Cloud Logging so that you store log data in a central location, regardless of the point… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-logging-finops`](skills/cloud-logging-finops/SKILL.md) | Non-interactive runs. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-logging-query-generation`](skills/cloud-logging-query-generation/SKILL.md) | Use this skill to generate correct Logging Query Language (LQL) queries for Cloud Logging. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-monitoring-chart-generation`](skills/cloud-monitoring-chart-generation/SKILL.md) | Transforms PromQL or ListTimeSeries JSON request payloads and metric metadata into valid Server-Driven UI (SDUI)… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-monitoring-list-time-series-request`](skills/cloud-monitoring-list-time-series-request/SKILL.md) | Use this skill to translate any Cloud Monitoring metric descriptor into valid, production-ready ListTimeSeries REST API query parameters (name,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-monitoring-metric-selection`](skills/cloud-monitoring-metric-selection/SKILL.md) | Use this skill to identify the most relevant Cloud Monitoring metric descriptors. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-monitoring-notification-channels-configuration`](skills/cloud-monitoring-notification-channels-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-monitoring-promql-query`](skills/cloud-monitoring-promql-query/SKILL.md) | Use this skill to generate a valid PromQL query from any Cloud Monitoring metric type. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-network-insights`](skills/cloud-network-insights/SKILL.md) | For all gcloud CLI, REST API, and MCP attribution requirements when executing commands with this skill, follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-run-alert-configuration`](skills/cloud-run-alert-configuration/SKILL.md) | Production-grade observability for Cloud Run using Terraform and PromQL (Cloud Monitoring). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-run-basics`](skills/cloud-run-basics/SKILL.md) | Cloud Run is a fully managed application platform for running your code, function, or container on top of Google's highly scalable infrastructure. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-sql-basics`](skills/cloud-sql-basics/SKILL.md) | Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`cloud-trace-querying`](skills/cloud-trace-querying/SKILL.md) | This skill equips the agent to interact with Cloud Trace by providing standard query patterns, diagnostic workflows for latency and errors, and tools… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`data-manager-api-audience-ingestion`](skills/data-manager-api-audience-ingestion/SKILL.md) | - Authentication & Library Installation: If you need to set up access to the Data Manager API or install the client and utility libraries, refer to… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`data-manager-api-event-ingestion`](skills/data-manager-api-event-ingestion/SKILL.md) | - Authentication & Library Installation: If you need to set up access to the Data Manager API or install the client and utility libraries, refer to… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`data-manager-api-setup`](skills/data-manager-api-setup/SKILL.md) | Refer to Set up API access(https://developers.google.com/data-manager/api/devguides/quickstart/set-up-access.md.txt) for more details. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`datalineage-bigquery-asset-impact-analysis`](skills/datalineage-bigquery-asset-impact-analysis/SKILL.md) | This skill guides the agent in performing a downstream impact analysis (blast radius assessment) when a BigQuery table or view is reported as broken,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`datalineage-summary`](skills/datalineage-summary/SKILL.md) | This skill guides the agent in investigating and summarizing the Data Lineage graph for a specific focal asset (Table-Level Lineage) or specific… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`dbt-sf-to-bq-translator`](skills/dbt-sf-to-bq-translator/SKILL.md) | You are responsible for: 1. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`deploy-to-vercel`](skills/deploy-to-vercel/SKILL.md) | Deploy applications and websites to Vercel. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`detection-engineering-coverage-evaluation`](skills/detection-engineering-coverage-evaluation/SKILL.md) | Routing Note: To author, test (Retrohunt), or tune YARA-L 2.0 detection rules directly, open secops-detection-engineering/SKILL.md. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`developer-device-platform-basics`](skills/developer-device-platform-basics/SKILL.md) | Developer Device Platform (DDP) is a Google fully managed, global infrastructure providing access to a wide variety of physical and virtual devices. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`developing-genkit-go`](skills/developing-genkit-go/SKILL.md) | Develop AI-powered applications using Genkit in Go. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`developing-genkit-js`](skills/developing-genkit-js/SKILL.md) | Develop AI-powered applications using Genkit in Node.js/TypeScript. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`developing-genkit-python`](skills/developing-genkit-python/SKILL.md) | Develop AI-powered applications using Genkit in Python. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`dpop-adoption`](skills/dpop-adoption/SKILL.md) | Demonstrating Proof-of-Possession (DPoP, RFC 9449) secures OAuth 2.0 refresh tokens against interception and replay attacks by cryptographically… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`finding-google-skills`](skills/finding-google-skills/SKILL.md) | Routes a request to the published Google skills that apply to it. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`firebase-basics`](skills/firebase-basics/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gcloud`](skills/gcloud/SKILL.md) | !CAUTION ### MANDATORY PRE-CONDITION: EXPLICIT LEAF-LEVEL SYNTAX VALIDATION All pre-existing knowledge of gcloud commands, flags, flag values, and… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gemini-agents-api`](skills/gemini-agents-api/SKILL.md) | Manages custom Agent resources on Gemini Enterprise Agent Platform. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gemini-api`](skills/gemini-api/SKILL.md) | Use when the user asks about using Gemini in an enterprise environment or explicitly mentions Vertex AI, Google Cloud, or Agent Platform. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gemini-interactions-api`](skills/gemini-interactions-api/SKILL.md) | Guides the usage of Gemini Interactions API on Gemini Enterprise Agent Platform. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gemini-live-api`](skills/gemini-live-api/SKILL.md) | This skill provides instructions for generating a LiveAPI client service class that connects to the Gemini Enterprise Live API over WebSockets. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-handle-disruption-gpu-tpu`](skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-jobset-interruption`](skills/gke-ai-troubleshooting-jobset-interruption/SKILL.md) | Use this skill to systematically diagnose and resolve JobSet interruptions, restarts, and preemptions on GKE clusters hosting large-scale AI/ML… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-node-unresponsive-timeout`](skills/gke-ai-troubleshooting-node-unresponsive-timeout/SKILL.md) | When the Compute Engine host of a TPU or GPU node has a fatal hardware error, kernel panic, or non-maskable interrupt (NMI) lockup, the guest OS… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-dynamic-slices-monitoring`](skills/gke-ai-troubleshooting-tpu-dynamic-slices-monitoring/SKILL.md) | Monitors the status of TPU Slice custom resources, troubleshoots provisioning failures, validates workload manifests on dynamic slices, and performs… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-metrics-monitoring`](skills/gke-ai-troubleshooting-tpu-metrics-monitoring/SKILL.md) | This skill enables the agent to monitor GKE TPU workloads, nodes, and node pools using GKE system metrics. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-mxla-hang`](skills/gke-ai-troubleshooting-tpu-mxla-hang/SKILL.md) | Diagnose Cloud TPU multi-slice training hangs on Google Kubernetes Engine (GKE) by correlating Megascale HANGDETECTED logs and ML Diagnostics… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-partition-overlap`](skills/gke-ai-troubleshooting-tpu-partition-overlap/SKILL.md) | A dynamic slice fails to form with the status reason SliceCreationFailed when, among other documented causes, any of its nodes are already used by… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-performance-degradation`](skills/gke-ai-troubleshooting-tpu-performance-degradation/SKILL.md) | Diagnose and mitigate Cloud TPU training throughput drops and step-time regressions (15%+ drop in TPU duty cycle) on Google Kubernetes Engine (GKE)… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-reservation-stockout`](skills/gke-ai-troubleshooting-tpu-reservation-stockout/SKILL.md) | Use this skill to diagnose and resolve GKE TPU node pool creation or scale-up failures that fail with GCESTOCKOUT, ZONERESOURCEPOOLEXHAUSTED, or… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-slice-mig-stuck-updating`](skills/gke-ai-troubleshooting-tpu-slice-mig-stuck-updating/SKILL.md) | This skill helps diagnose GKE TPU Dynamic Slice creation failures and JobSet scheduling delays when the Compute Engine managed instance groups (MIGs)… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-vbar-oom`](skills/gke-ai-troubleshooting-tpu-vbar-oom/SKILL.md) | Use this skill to systematically diagnose and prevent vbarcontrolagent segfaults and Out-Of-Memory (OOM) errors on TPU v6e nodes. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-ai-troubleshooting-tpu-vm-repair-stuck`](skills/gke-ai-troubleshooting-tpu-vm-repair-stuck/SKILL.md) | This skill checks the VM status, the host events, and the GKE repair status, and routes recovery through GKE instead of direct Compute Engine changes. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-alert-configuration`](skills/gke-alert-configuration/SKILL.md) | This skill provides guidelines and best practices for creating robust, high-signal alerting policies for Google Kubernetes Engine workloads using… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-app-onboarding`](skills/gke-app-onboarding/SKILL.md) | This reference provides workflows for containerizing and deploying applications to GKE for the first time. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-backup-dr`](skills/gke-backup-dr/SKILL.md) | Protects stateful GKE workloads using Backup for GKE. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-basics`](skills/gke-basics/SKILL.md) | Routing Note: For Workload Identity KSA/GSA setup, open gke-workload-identity/SKILL.md. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-batch-hpc`](skills/gke-batch-hpc/SKILL.md) | This reference covers running batch processing and high-performance computing (HPC) workloads on GKE. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-cluster-autoscaler`](skills/gke-cluster-autoscaler/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-cluster-creation`](skills/gke-cluster-creation/SKILL.md) | This reference guides creating Google Kubernetes Engine (GKE) clusters by providing a set of best-practice templates and guiding through mode… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-compute-classes`](skills/gke-compute-classes/SKILL.md) | Guidance on configuring, optimizing, and troubleshooting GKE ComputeClasses. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-cost-analysis`](skills/gke-cost-analysis/SKILL.md) | This skill provides guidance on answering natural language questions about GKE-related costs, billing reports, and utilization analysis. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-cost-optimization`](skills/gke-cost-optimization/SKILL.md) | This reference covers strategies and workflows for reducing Google Kubernetes Engine (GKE) costs while maintaining a secure and reliable posture. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-custom-golden-image-discovery`](skills/gke-custom-golden-image-discovery/SKILL.md) | You are an expert at helping users find the correct "golden" base image for creating custom GKE images. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-golden-path`](skills/gke-golden-path/SKILL.md) | The golden path is the recommended Autopilot configuration for production clusters. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-inference`](skills/gke-inference/SKILL.md) | Routing Note: For migrating existing AI workloads to GKE, open google-cloud-solution-guided-gke-ai-migration/SKILL.md. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-manifest-generation`](skills/gke-manifest-generation/SKILL.md) | This skill provides guidelines, tooling integration, and templates to translate natural language descriptions or application code changes into… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-multitenancy`](skills/gke-multitenancy/SKILL.md) | This reference covers enterprise multi-tenancy patterns on GKE, including namespace isolation, RBAC planning, resource quotas, and network… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-networking`](skills/gke-networking/SKILL.md) | This reference covers networking configuration for GKE clusters. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-node-notready`](skills/gke-node-notready/SKILL.md) | Use this skill to systematically diagnose why one or more GKE nodes report a NotReady (or Ready: Unknown) status and to propose safe remediations. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-observability`](skills/gke-observability/SKILL.md) | This reference covers monitoring, logging, and metrics configuration for GKE. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-platform-security`](skills/gke-platform-security/SKILL.md) | This reference covers platform-level security hardening and cluster configuration for Google Kubernetes Engine (GKE). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-productionize`](skills/gke-productionize/SKILL.md) | Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability, security, reliability,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-reliability`](skills/gke-reliability/SKILL.md) | Routing Note: To generate Kubernetes YAML manifests (Deployment, StatefulSet, Service, ConfigMap, HTTPRoute, PodDisruptionBudget), open… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-service-networking`](skills/gke-service-networking/SKILL.md) | This skill provides workflows for exposing applications running on GKE securely to the internet or internal networks. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-storage`](skills/gke-storage/SKILL.md) | Routing Note: For Cloud Storage FUSE (gcsfuse) mounts or the GKE gcsfuse.csi.storage.gke.io CSI driver, open google-cloud-storage-fuse/SKILL.md. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-storage-troubleshooting`](skills/gke-storage-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve persistent-storage failures for workloads running on GKE — volume attach/mount errors, disk… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-upgrades`](skills/gke-upgrades/SKILL.md) | Produce clear, actionable documents — upgrade plans, runbooks, or checklists — tailored to the user's environment. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-workload-identity`](skills/gke-workload-identity/SKILL.md) | Use this skill to systematically diagnose why a Pod using Workload Identity Federation for GKE cannot authenticate to Google Cloud APIs. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-workload-scaling`](skills/gke-workload-scaling/SKILL.md) | This skill provides workflows and best practices for scaling applications on Google Kubernetes Engine (GKE). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-workload-scaling-troubleshooting`](skills/gke-workload-scaling-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve HorizontalPodAutoscaler (HPA) failures on GKE — metrics reported as <unknown, FailedGet events,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-workload-security`](skills/gke-workload-security/SKILL.md) | Routing Note: For Workload Identity KSA/GSA bindings, open gke-workload-identity/SKILL.md. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`gke-workload-troubleshooting`](skills/gke-workload-troubleshooting/SKILL.md) | Use this skill to systematically diagnose and resolve failures in application workloads deployed in GKE clusters. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-ads-api-account-diagnostics`](skills/google-ads-api-account-diagnostics/SKILL.md) | This skill provides instructions on how to use the Google Ads MCP server tools to diagnose common account performance issues. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-ads-api-mcp-setup`](skills/google-ads-api-mcp-setup/SKILL.md) | Guides developers through downloading, configuring, and installing the official open-source Google Ads MCP Server. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-ads-api-quickstart`](skills/google-ads-api-quickstart/SKILL.md) | 1. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-agents-cli-onboarding`](skills/google-agents-cli-onboarding/SKILL.md) | !TIP One-Time Setup: To install the CLI and enable all 7 specialized development skills in your coding agent, run the setup command: bash uvx… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-analytics-admin-api-basics`](skills/google-analytics-admin-api-basics/SKILL.md) | The Google Analytics Admin API provides programmatic access to Google Analytics account and property configuration. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-analytics-data-api-basics`](skills/google-analytics-data-api-basics/SKILL.md) | The Google Analytics Data API v1beta provides programmatic access to Google Analytics report data. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-filestore-auditing`](skills/google-cloud-filestore-auditing/SKILL.md) | This skill enables autonomous agents to audit, evaluate, and report the disaster recovery, security access governance, and architectural reliability… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-filestore-autoscale`](skills/google-cloud-filestore-autoscale/SKILL.md) | This skill enables agents to inspect, evaluate, and modify Filestore instance capacities across Google Cloud projects based on configured thresholds. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-filestore-log-troubleshooting`](skills/google-cloud-filestore-log-troubleshooting/SKILL.md) | Diagnoses, troubleshoots, and remediates Filestore client mount failures, permission errors (EACCES), and network timeouts (ETIMEDOUT) across… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-filestore-nfs-browser`](skills/google-cloud-filestore-nfs-browser/SKILL.md) | Enables autonomous agents and cloud engineers to inspect, search, and read files located on Filestore (NFS) instances without needing local NFS… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-global-frontend-configuration`](skills/google-cloud-global-frontend-configuration/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-networking-observability`](skills/google-cloud-networking-observability/SKILL.md) | For all gcloud CLI, REST API, and MCP attribution requirements when executing commands with this skill, follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-recipe-auth`](skills/google-cloud-recipe-auth/SKILL.md) | Provides expert guidance on Identity and Access Management (IAM) and authenticating and authorizing to Google Cloud services and APIs, covering human… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-recipe-foundation-builder`](skills/google-cloud-recipe-foundation-builder/SKILL.md) | !WARNING This skill is currently in a preview state. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-recipe-onboarding`](skills/google-cloud-recipe-onboarding/SKILL.md) | This skill provides a streamlined, non-interactive "happy path" for a singleton developer to get started with Google Cloud(https://cloud.google.com/). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-scc-query`](skills/google-cloud-scc-query/SKILL.md) | Provides guidelines and read-only gcloud CLI command patterns for querying and retrieving security findings, external exposures, toxic combinations,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-scc-remediation`](skills/google-cloud-scc-remediation/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-slo-alert-configuration`](skills/google-cloud-slo-alert-configuration/SKILL.md) | This skill guides the user through a structured conversation to configure Cloud Monitoring PromQL-based Service Level Objective (SLO) alerting… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-bidirectional-streaming`](skills/google-cloud-solution-agentic-ai-bidirectional-streaming/SKILL.md) | This skill guides agents through the workflow to design and implement a tailored multi-product solution in the cloud for a live, bidirectional… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-borderless-data-lakehouse`](skills/google-cloud-solution-agentic-ai-borderless-data-lakehouse/SKILL.md) | Follow this workflow to help users design and implement a custom multi-product solution in the cloud for a given workload, use case, or requirement. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-agentic-ai-data-science-workflow`](skills/google-cloud-solution-agentic-ai-data-science-workflow/SKILL.md) | This skill guides agents through the workflow to design and implement a tailored multi-product solution in the cloud for a given workload, use case,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-agentic-analytics-spark-knowledge-catalog`](skills/google-cloud-solution-agentic-analytics-spark-knowledge-catalog/SKILL.md) | This skill provides a workflow to design and implement a governed, secure pipeline for agentic analytics solution across structured and unstructured… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-architecture`](skills/google-cloud-solution-architecture/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-build-deploy-agents`](skills/google-cloud-solution-build-deploy-agents/SKILL.md) | This skill guides agents through the workflow of designing and implementing a tailored multi-product solution in the cloud for a given workload, use… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-guided-gke-ai-migration`](skills/google-cloud-solution-guided-gke-ai-migration/SKILL.md) | This skill guides agents through the end-to-end process of migrating existing AI inference workloads (e.g., from Cloud Run, Gemini API, Gemini… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-hybrid-search-alloydb`](skills/google-cloud-solution-hybrid-search-alloydb/SKILL.md) | This skill provides a workflow to design and implement secure, low-latency, and high-accuracy hybrid search solutions combining structured dataset… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-multi-agent-security`](skills/google-cloud-solution-multi-agent-security/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-n-tier-serverless-web-app`](skills/google-cloud-solution-n-tier-serverless-web-app/SKILL.md) | <!-- disableFinding(all) -- <!-- mdlint off -- | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-solution-rag-enterprise-search-gke-sqldb`](skills/google-cloud-solution-rag-enterprise-search-gke-sqldb/SKILL.md) | This skill provides a workflow to design and implement a secure, low-latency, and high-accuracy RAG-enabled conversational search solution for… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-storage-basics`](skills/google-cloud-storage-basics/SKILL.md) | Cloud Storage on Google Cloud is a managed service for storing data as objects at any scale. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-storage-bucket-architect`](skills/google-cloud-storage-bucket-architect/SKILL.md) | You are a Use-Case Driven Cloud Storage Bucket Architect agent on Google Cloud. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-storage-fuse`](skills/google-cloud-storage-fuse/SKILL.md) | Cloud Storage FUSE is a POSIX file-system adapter over Cloud Storage on Google Cloud, operated via the gcsfuse CLI tool. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-cost-optimization`](skills/google-cloud-waf-cost-optimization/SKILL.md) | Evaluates Google Cloud workloads for cost efficiency and FinOps alignment using the Google Cloud Well-Architected Framework Cost Optimization pillar. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-operational-excellence`](skills/google-cloud-waf-operational-excellence/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-performance-optimization`](skills/google-cloud-waf-performance-optimization/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-reliability`](skills/google-cloud-waf-reliability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-security`](skills/google-cloud-waf-security/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-cloud-waf-sustainability`](skills/google-cloud-waf-sustainability/SKILL.md) | MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read and follow the instructions in Usage… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-android-migrate-to-next-gen`](skills/google-mobile-ads-android-migrate-to-next-gen/SKILL.md) | Migrates Android applications from the old, legacy Google Mobile | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-banner`](skills/google-mobile-ads-banner/SKILL.md) | Banner ads are rectangular image or text ads that occupy a spot within an app's layout. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-get-started`](skills/google-mobile-ads-get-started/SKILL.md) | 1. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-interstitial`](skills/google-mobile-ads-interstitial/SKILL.md) | Interstitial ads show full-page ads for users on mobile apps. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-rewarded`](skills/google-mobile-ads-rewarded/SKILL.md) | Rewarded ads reward users with in-app items for interacting with full-screen ads. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`google-mobile-ads-validate`](skills/google-mobile-ads-validate/SKILL.md) | Validate a project's Google Mobile Ads (GMA) SDK integration either as a complete audit or for specific requested checks. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`iam-helper-for-policy-management`](skills/iam-helper-for-policy-management/SKILL.md) | Orchestrates the lifecycle and management of IAM allow and deny policies across IAM v1 (allow policies) and IAM v2 (deny policies). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`iam-helper-for-policy-simulator`](skills/iam-helper-for-policy-simulator/SKILL.md) | You are an advanced security assistant helping users safely modify IAM policies. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`iam-helper-for-privileged-access-management`](skills/iam-helper-for-privileged-access-management/SKILL.md) | This skill provides step-by-step guidance for planning, validating, and executing Privileged Access Manager (PAM) entitlement CRUD operations,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`iam-helper-for-troubleshooting`](skills/iam-helper-for-troubleshooting/SKILL.md) | You are an expert Google Cloud Security and IAM assistant. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`ima-dai-sdk`](skills/ima-dai-sdk/SKILL.md) | Use the IMA DAI SDK to load HLS or DASH streams into the app for: | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`ima-sdk-client-side`](skills/ima-sdk-client-side/SKILL.md) | The Google IMA SDK (Interactive Media Ads) lets you load in-stream video and audio ads into websites, apps, TVs and other digital platforms. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`managed-airflow-dag-authoring`](skills/managed-airflow-dag-authoring/SKILL.md) | This skill guides you through authoring and validating Apache Airflow DAGs for Managed Service for Apache Airflow (MSAA; formerly Cloud Composer)… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`managed-airflow-dag-troubleshooting`](skills/managed-airflow-dag-troubleshooting/SKILL.md) | This skill provides instructions for troubleshooting Managed Airflow DAGs (DAG runs and task instances), utilizing gcloud composer, gcloud logging… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`managed-airflow-migrations`](skills/managed-airflow-migrations/SKILL.md) | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`managed-airflow-recommendations`](skills/managed-airflow-recommendations/SKILL.md) | This skill provides specialized instructions for providing recommendations, best practices, and performance-tuning for Managed Service for Apache… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`migrate-to-rust`](skills/migrate-to-rust/SKILL.md) | Act as a Systems Architect, Performance Engineer, and Rust Specialist. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`observability-and-instrumentation`](skills/observability-and-instrumentation/SKILL.md) | Instruments code so production behavior is visible and diagnosable. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`retrieving-developer-knowledge`](skills/retrieving-developer-knowledge/SKILL.md) | The Developer Knowledge skill provides access to official Google developer documentation across Google Cloud, AI/ML (ai.google.dev, ADK, TensorFlow),… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`secops-cases`](skills/secops-cases/SKILL.md) | Operates and manages incident cases within Google Security Operations (Google SecOps SOAR). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`secops-detection-engineering`](skills/secops-detection-engineering/SKILL.md) | This skill guides security engineers and autonomous agents through the end-to-end detection engineering lifecycle within Google Security Operations… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`secops-hunt`](skills/secops-hunt/SKILL.md) | You are an expert Threat Hunter operating within Google Security Operations (SecOps). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`secops-investigate`](skills/secops-investigate/SKILL.md) | You are an expert Security Operations Center (SOC) Tier 2/3 Analyst and Incident Responder operating within Google Security Operations (SecOps). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`secops-triage`](skills/secops-triage/SKILL.md) | You are an expert Security Operations Center (SOC) Analyst specializing in Google Security Operations (SecOps). | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`shipping-and-launch`](skills/shipping-and-launch/SKILL.md) | Prepares production launches. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`sign-in-with-google-web`](skills/sign-in-with-google-web/SKILL.md) | This skill provides normative architectural guidelines, secure implementation contracts, and failure-prevention protocols for integrating Sign In… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`spanner-basics`](skills/spanner-basics/SKILL.md) | This skill provides core workflows and guidance for administering and developing with Cloud Spanner on Google Cloud, a fully managed,… | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`vercel-cli-with-tokens`](skills/vercel-cli-with-tokens/SKILL.md) | Deploy and manage projects on Vercel using token-based authentication. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`vercel-optimize`](skills/vercel-optimize/SKILL.md) | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |
| [`workload-manager-basics`](skills/workload-manager-basics/SKILL.md) | Workload Manager validates enterprise workloads against Google Cloud best practices and recommendations. | [google/skills](https://github.com/google/skills) | Apache-2.0 |

### AI & ML (`ai-and-ml`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-ai-and-ml`](skills/pack-ai-and-ml/SKILL.md) | Model work from a paper to a served endpoint: architecture notes (Mamba, RWKV, diffusion, CLIP, BLIP-2), fine-tuning stacks (Axolotl, Llama-Factory,… | **pack** | mixed |
| [`academic-plotting`](skills/academic-plotting/SKILL.md) | Generates publication-quality figures for ML papers from research context. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ara-compiler`](skills/ara-compiler/SKILL.md) | Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete Agent-Native… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ara-research-manager`](skills/ara-research-manager/SKILL.md) | Records research provenance as a post-task epilogue, scanning conversation history at the end of a coding or research session to extract decisions,… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ara-rigor-reviewer`](skills/ara-rigor-reviewer/SKILL.md) | Performs ARA Seal Level 2 semantic epistemic review on Agent-Native Research Artifacts, scoring six dimensions (evidence relevance, falsifiability,… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`audiocraft-audio-generation`](skills/audiocraft-audio-generation/SKILL.md) | PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`autogpt-agents`](skills/autogpt-agents/SKILL.md) | Autonomous AI agent platform for building and deploying continuous agents. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`autoresearch`](skills/autoresearch/SKILL.md) | Orchestrates end-to-end autonomous AI research projects using a two-loop architecture. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`awq-quantization`](skills/awq-quantization/SKILL.md) | Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`axolotl`](skills/axolotl/SKILL.md) | Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`blip-2-vision-language`](skills/blip-2-vision-language/SKILL.md) | Vision-language pre-training framework bridging frozen image encoders and LLMs. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`brainstorming-research-ideas`](skills/brainstorming-research-ideas/SKILL.md) | Guides researchers through structured ideation frameworks to discover high-impact research directions. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`chroma`](skills/chroma/SKILL.md) | Open-source embedding database for AI applications. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`clip`](skills/clip/SKILL.md) | OpenAI's model connecting vision and language. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`constitutional-ai`](skills/constitutional-ai/SKILL.md) | Anthropic's method for training harmless AI through self-improvement. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`creative-thinking-for-research`](skills/creative-thinking-for-research/SKILL.md) | Applies cognitive science frameworks for creative thinking to CS and AI research ideation. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`crewai-multi-agent`](skills/crewai-multi-agent/SKILL.md) | Multi-agent orchestration framework for autonomous AI collaboration. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`deepspeed`](skills/deepspeed/SKILL.md) | Expert guidance for distributed training with DeepSpeed - ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8, 1-bit Adam, sparse attention | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`distributed-llm-pretraining-torchtitan`](skills/distributed-llm-pretraining-torchtitan/SKILL.md) | Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`dspy`](skills/dspy/SKILL.md) | Build complex AI systems with declarative programming, optimize prompts automatically, create modular RAG systems and agents with DSPy - Stanford… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`evaluating-code-models`](skills/evaluating-code-models/SKILL.md) | Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`evaluating-cosmos-policy`](skills/evaluating-cosmos-policy/SKILL.md) | Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`evaluating-llms-harness`](skills/evaluating-llms-harness/SKILL.md) | Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`evolving-ai-agents`](skills/evolving-ai-agents/SKILL.md) | Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`experiment-tracking-swanlab`](skills/experiment-tracking-swanlab/SKILL.md) | Provides guidance for experiment tracking with SwanLab. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`faiss`](skills/faiss/SKILL.md) | Facebook's library for efficient similarity search and clustering of dense vectors. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`fine-tuning-openvla-oft`](skills/fine-tuning-openvla-oft/SKILL.md) | Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`fine-tuning-serving-openpi`](skills/fine-tuning-serving-openpi/SKILL.md) | Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy inference across ALOHA,… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`fine-tuning-with-trl`](skills/fine-tuning-with-trl/SKILL.md) | Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization,… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`gguf-quantization`](skills/gguf-quantization/SKILL.md) | GGUF format and llama.cpp quantization for efficient CPU/GPU inference. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`gptq`](skills/gptq/SKILL.md) | Post-training 4-bit quantization for LLMs with minimal accuracy loss. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`grpo-rl-training`](skills/grpo-rl-training/SKILL.md) | Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`guidance`](skills/guidance/SKILL.md) | Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`hf-cli`](skills/hf-cli/SKILL.md) | Hugging Face Hub CLI (`hf`) for downloading, uploading, and managing models, datasets, spaces, buckets, repos, papers, jobs, and more on the Hugging… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-aws-context-discovery`](skills/hf-cloud-aws-context-discovery/SKILL.md) | Discover the user's local AWS context (active profile, region, account ID, caller identity) at the start of any AWS task. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-python-env-setup`](skills/hf-cloud-python-env-setup/SKILL.md) | Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto3. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-sagemaker-deployment-planner`](skills/hf-cloud-sagemaker-deployment-planner/SKILL.md) | Plan and coordinate the deployment of a model to Amazon SageMaker AI. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-sagemaker-iam-preflight`](skills/hf-cloud-sagemaker-iam-preflight/SKILL.md) | Ensure a usable SageMaker execution role exists before deploying or training. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-sagemaker-production-defaults`](skills/hf-cloud-sagemaker-production-defaults/SKILL.md) | Create a SageMaker endpoint (real-time, real-time scale-to-zero, or async) with autoscaling, CloudWatch alarms, and tagging enabled by default. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-cloud-serving-image-selection`](skills/hf-cloud-serving-image-selection/SKILL.md) | Pick the right serving container for a SageMaker model deployment and find its current image URI. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-mcp`](skills/hf-mcp/SKILL.md) | Use Hugging Face Hub via MCP server tools. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hf-mem`](skills/hf-mem/SKILL.md) | Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`hqq-quantization`](skills/hqq-quantization/SKILL.md) | Half-Quadratic Quantization for LLMs without calibration data. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`huggingface-accelerate`](skills/huggingface-accelerate/SKILL.md) | Simplest distributed training API. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`huggingface-best`](skills/huggingface-best/SKILL.md) | Finds the best models for a task by querying official HF benchmark leaderboards, enriching results with model size data, filtering for what fits on… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-community-evals`](skills/huggingface-community-evals/SKILL.md) | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-datasets`](skills/huggingface-datasets/SKILL.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-gradio`](skills/huggingface-gradio/SKILL.md) | Build Gradio web UIs and demos in Python. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-llm-trainer`](skills/huggingface-llm-trainer/SKILL.md) | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Face Jobs infrastructure. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-local-models`](skills/huggingface-local-models/SKILL.md) | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-lora-space-builder`](skills/huggingface-lora-space-builder/SKILL.md) | Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-paper-publisher`](skills/huggingface-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-papers`](skills/huggingface-papers/SKILL.md) | Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/datasets/spaces,… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-spaces`](skills/huggingface-spaces/SKILL.md) | Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated hardware, model loading,… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-tokenizers`](skills/huggingface-tokenizers/SKILL.md) | Fast tokenizers optimized for research and production. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`huggingface-tool-builder`](skills/huggingface-tool-builder/SKILL.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-trackio`](skills/huggingface-trackio/SKILL.md) | Track and visualize ML training experiments with Trackio. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-vision-trainer`](skills/huggingface-vision-trainer/SKILL.md) | Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm models — MobileNetV3,… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`huggingface-zerogpu`](skills/huggingface-zerogpu/SKILL.md) | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`implementing-llms-litgpt`](skills/implementing-llms-litgpt/SKILL.md) | Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`instructor`](skills/instructor/SKILL.md) | Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type safety, and… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`knowledge-distillation`](skills/knowledge-distillation/SKILL.md) | Compress large language models using knowledge distillation from teacher to student models. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`lambda-labs-gpu-cloud`](skills/lambda-labs-gpu-cloud/SKILL.md) | Reserved and on-demand GPU cloud instances for ML training and inference. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`langchain`](skills/langchain/SKILL.md) | Framework for building LLM-powered applications with agents, chains, and RAG. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`langsmith-observability`](skills/langsmith-observability/SKILL.md) | LLM observability platform for tracing, evaluation, and monitoring. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`llama-cpp`](skills/llama-cpp/SKILL.md) | Runs LLM inference on CPU, Apple Silicon, and consumer GPUs without NVIDIA hardware. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`llama-factory`](skills/llama-factory/SKILL.md) | Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`llamaguard`](skills/llamaguard/SKILL.md) | Meta's 7-8B specialized moderation model for LLM input/output filtering. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`llamaindex`](skills/llamaindex/SKILL.md) | Data framework for building LLM applications with RAG. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`llava`](skills/llava/SKILL.md) | Large Language and Vision Assistant. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`long-context`](skills/long-context/SKILL.md) | Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`mamba-architecture`](skills/mamba-architecture/SKILL.md) | State-space model with O(n) complexity vs Transformers' O(n²). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`miles-rl-training`](skills/miles-rl-training/SKILL.md) | Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ml-paper-writing`](skills/ml-paper-writing/SKILL.md) | Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ml-training-recipes`](skills/ml-training-recipes/SKILL.md) | Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery, spatial omics, genomics. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`mlflow`](skills/mlflow/SKILL.md) | Track ML experiments, manage model registry with versioning, deploy models to production, and reproduce experiments with MLflow - framework-agnostic… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`modal-serverless-gpu`](skills/modal-serverless-gpu/SKILL.md) | Serverless GPU cloud platform for running ML workloads. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`model-merging`](skills/model-merging/SKILL.md) | Merge multiple fine-tuned models using mergekit to combine capabilities without retraining. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`model-pruning`](skills/model-pruning/SKILL.md) | Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`moe-training`](skills/moe-training/SKILL.md) | Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`nanogpt`](skills/nanogpt/SKILL.md) | Educational GPT implementation in ~300 lines. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`nemo-curator`](skills/nemo-curator/SKILL.md) | GPU-accelerated data curation for LLM training. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`nemo-evaluator-sdk`](skills/nemo-evaluator-sdk/SKILL.md) | Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`nemo-guardrails`](skills/nemo-guardrails/SKILL.md) | NVIDIA's runtime safety framework for LLM applications. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`nnsight-remote-interpretability`](skills/nnsight-remote-interpretability/SKILL.md) | Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`openrlhf-training`](skills/openrlhf-training/SKILL.md) | High-performance RLHF framework with Ray+vLLM acceleration. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`optimizing-attention-flash`](skills/optimizing-attention-flash/SKILL.md) | Optimizes transformer attention with Flash Attention for 2-4x speedup and 10-20x memory reduction. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`outlines`](skills/outlines/SKILL.md) | Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`peft-fine-tuning`](skills/peft-fine-tuning/SKILL.md) | Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`phoenix-observability`](skills/phoenix-observability/SKILL.md) | Open-source AI observability platform for LLM tracing, evaluation, and monitoring. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`pinecone`](skills/pinecone/SKILL.md) | Managed vector database for production AI applications. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`presenting-conference-talks`](skills/presenting-conference-talks/SKILL.md) | Generates conference presentation slides (Beamer LaTeX PDF and editable PPTX) from a compiled paper with speaker notes and talk script. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`prompt-guard`](skills/prompt-guard/SKILL.md) | Meta's 86M prompt injection and jailbreak detector. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`pytorch-fsdp2`](skills/pytorch-fsdp2/SKILL.md) | Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed checkpointing. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`pytorch-lightning`](skills/pytorch-lightning/SKILL.md) | High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and minimal boilerplate. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`pyvene-interventions`](skills/pyvene-interventions/SKILL.md) | Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`qdrant-vector-search`](skills/qdrant-vector-search/SKILL.md) | High-performance vector similarity search engine for RAG and semantic search. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`quantizing-models-bitsandbytes`](skills/quantizing-models-bitsandbytes/SKILL.md) | Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ray-data`](skills/ray-data/SKILL.md) | Scalable data processing for ML workloads. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`ray-train`](skills/ray-train/SKILL.md) | Distributed training orchestration across clusters. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`rwkv-architecture`](skills/rwkv-architecture/SKILL.md) | RNN+Transformer hybrid with O(n) inference. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`segment-anything-model`](skills/segment-anything-model/SKILL.md) | Foundation model for image segmentation with zero-shot transfer. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`sentence-transformers`](skills/sentence-transformers/SKILL.md) | Framework for state-of-the-art sentence, text, and image embeddings. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`sentencepiece`](skills/sentencepiece/SKILL.md) | Language-independent tokenizer treating text as raw Unicode. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`serving-llms-vllm`](skills/serving-llms-vllm/SKILL.md) | Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`sglang`](skills/sglang/SKILL.md) | Fast structured generation and serving for LLMs with RadixAttention prefix caching. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`simpo-training`](skills/simpo-training/SKILL.md) | Simple Preference Optimization for LLM alignment. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`skypilot-multi-cloud-orchestration`](skills/skypilot-multi-cloud-orchestration/SKILL.md) | Multi-cloud orchestration for ML workloads with automatic cost optimization. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`slime-rl-training`](skills/slime-rl-training/SKILL.md) | Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`sparse-autoencoder-training`](skills/sparse-autoencoder-training/SKILL.md) | Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`speculative-decoding`](skills/speculative-decoding/SKILL.md) | Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`stable-diffusion-image-generation`](skills/stable-diffusion-image-generation/SKILL.md) | State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`systems-paper-writing`](skills/systems-paper-writing/SKILL.md) | Comprehensive guide for writing systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`tensorboard`](skills/tensorboard/SKILL.md) | Visualize training metrics, debug models with histograms, compare experiments, visualize model graphs, and profile performance with TensorBoard -… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`tensorrt-llm`](skills/tensorrt-llm/SKILL.md) | Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`torchforge-rl-training`](skills/torchforge-rl-training/SKILL.md) | Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`train-sentence-transformers`](skills/train-sentence-transformers/SKILL.md) | Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder, dense or static embedding model for retrieval, similarity,… | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`training-llms-megatron`](skills/training-llms-megatron/SKILL.md) | Trains large language models (2B-462B parameters) using NVIDIA Megatron-Core with advanced parallelism strategies. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`transformer-lens-interpretability`](skills/transformer-lens-interpretability/SKILL.md) | Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals via HookPoints and… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`transformers-js`](skills/transformers-js/SKILL.md) | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`trl-training`](skills/trl-training/SKILL.md) | Post-train LLMs with TRL (Transformers Reinforcement Learning) — SFT, DPO, GRPO, KTO, and reward-model training. | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 |
| [`unsloth`](skills/unsloth/SKILL.md) | Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`verl-rl-training`](skills/verl-rl-training/SKILL.md) | Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`weights-and-biases`](skills/weights-and-biases/SKILL.md) | Track ML experiments with automatic logging, visualize training in real-time, optimize hyperparameters with sweeps, and manage model registry with… | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |
| [`whisper`](skills/whisper/SKILL.md) | OpenAI's general-purpose speech recognition model. | [orchestra-research/AI-research-SKILLs](https://github.com/orchestra-research/AI-research-SKILLs) | MIT |

### Office documents (`office-docs`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-office-docs`](skills/pack-office-docs/SKILL.md) | Produce and edit real office files: Word documents with tracked changes and styles, PowerPoint decks built with PptxGenJS or edited XML-safely inside… | **pack** | mixed |
| [`docx`](skills/docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`frontend-slides`](skills/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`minimax-docx`](skills/minimax-docx/SKILL.md) | Create, edit, and format DOCX documents via CLI tools or direct C# scripts built on OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`minimax-pdf`](skills/minimax-pdf/SKILL.md) | Rule: when in doubt between CREATE and REFORMAT, ask whether the user has an existing document to start from. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`minimax-xlsx`](skills/minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`pdf`](skills/pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`pdf-conversion-router`](skills/pdf-conversion-router/SKILL.md) | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the best… | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`ppt-editing-skill`](skills/ppt-editing-skill/SKILL.md) | Edit existing PowerPoint files or templates with XML-safe workflows. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`ppt-orchestra-skill`](skills/ppt-orchestra-skill/SKILL.md) | Plan and orchestrate multi-slide PowerPoint creation from scratch. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`pptx`](skills/pptx/SKILL.md) | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`pptx-deck-creation`](skills/pptx-deck-creation/SKILL.md) | Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`pptx-generator`](skills/pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`slide-making-skill`](skills/slide-making-skill/SKILL.md) | Implement single-slide PowerPoint pages with PptxGenJS. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`spreadsheet-manual-build`](skills/spreadsheet-manual-build/SKILL.md) | Spreadsheet Manual Build: an empty Excel workbook or CSV from a confirmed field list, formatted and validated. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`xlsx`](skills/xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |

### Engineering workflow (`engineering-workflow`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-engineering-workflow`](skills/pack-engineering-workflow/SKILL.md) | How the work itself is run: turn a request into a spec and tickets, implement in thin verifiable slices, test-first, debug systematically, request… | **pack** | mixed |
| [`ask-matt`](skills/ask-matt/SKILL.md) | Ask which skill or flow fits your situation. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`brainstorming`](skills/brainstorming/SKILL.md) | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`chief-of-staff`](skills/chief-of-staff/SKILL.md) | Pursue a long-running goal in a single session by co-ordinating subagents. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`claude-handoff`](skills/claude-handoff/SKILL.md) | Hand the current conversation off to a fresh background agent that picks up the work immediately. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`code-review-and-quality`](skills/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`code-simplification`](skills/code-simplification/SKILL.md) | Simplifies code for clarity. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`codebase-design`](skills/codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`context-engineering`](skills/context-engineering/SKILL.md) | Optimizes agent context setup. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`debugging-and-error-recovery`](skills/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`deprecation-and-migration`](skills/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`diagnosing-bugs`](skills/diagnosing-bugs/SKILL.md) | Diagnosis loop for hard bugs and performance regressions. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`diagnosing-superpowers`](skills/diagnosing-superpowers/SKILL.md) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`documentation-and-adrs`](skills/documentation-and-adrs/SKILL.md) | Records decisions and documentation. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`domain-modeling`](skills/domain-modeling/SKILL.md) | Build and sharpen a project's domain model. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`executing-plans`](skills/executing-plans/SKILL.md) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`find-skills`](skills/find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or… | [vercel-labs/skills](https://github.com/vercel-labs/skills) | MIT |
| [`finishing-a-development-branch`](skills/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`git-workflow-and-versioning`](skills/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`grill-me`](skills/grill-me/SKILL.md) | A relentless interview to sharpen a plan or design. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`grill-with-docs`](skills/grill-with-docs/SKILL.md) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`grilling`](skills/grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`handoff`](skills/handoff/SKILL.md) | Compact the current conversation into a handoff document for another agent to pick up. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`idea-refine`](skills/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`implement`](skills/implement/SKILL.md) | Implement a piece of work based on a spec or set of tickets. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`implement-spec`](skills/implement-spec/SKILL.md) | Implement the result of /to-spec and /to-tickets in code. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`incremental-implementation`](skills/incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`interview-me`](skills/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`loop-me`](skills/loop-me/SKILL.md) | Grill me about specs for the workflows I want to build, within this workspace. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`migrate-to-shoehorn`](skills/migrate-to-shoehorn/SKILL.md) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`planning-and-task-breakdown`](skills/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`ponytail`](skills/ponytail/SKILL.md) | You are a lazy senior developer. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`ponytail-audit`](skills/ponytail-audit/SKILL.md) | Audit the whole repo like the senior developer who just inherited it and will be paged when it breaks. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`ponytail-debt`](skills/ponytail-debt/SKILL.md) | Every deliberate ponytail shortcut is marked with a shortcut: comment naming its ceiling and upgrade path (older code may say ponytail:). | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`ponytail-gain`](skills/ponytail-gain/SKILL.md) | Show ponytail measured impact as a scoreboard: less code, less cost, more speed, from the agentic benchmark averages. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`ponytail-help`](skills/ponytail-help/SKILL.md) | Display this reference card when invoked. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`ponytail-review`](skills/ponytail-review/SKILL.md) | Review a change like the senior developer who will be paged when it breaks. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| [`pr`](skills/pr/SKILL.md) | Use when writing a PR body. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`pr-labeling`](skills/pr-labeling/SKILL.md) | Classify a skills CLI pull request from its description and patch, while respecting existing labels. | [vercel-labs/skills](https://github.com/vercel-labs/skills) | MIT |
| [`prototype`](skills/prototype/SKILL.md) | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`receiving-code-review`](skills/receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`requesting-code-review`](skills/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`research`](skills/research/SKILL.md) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`retro`](skills/retro/SKILL.md) | Conduct a retrospective on a coding session. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`scaffold-exercises`](skills/scaffold-exercises/SKILL.md) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`setup-pre-commit`](skills/setup-pre-commit/SKILL.md) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`setup-ts-deep-modules`](skills/setup-ts-deep-modules/SKILL.md) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through… | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. | [anthropics/skills](https://github.com/anthropics/skills) | NOASSERTION |
| [`skill-optimizer`](skills/skill-optimizer/SKILL.md) | Optimizes AI skills for activation, clarity, and cross-model reliability. | [mcollina/skills](https://github.com/mcollina/skills) | MIT |
| [`source-driven-development`](skills/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`spec-driven-development`](skills/spec-driven-development/SKILL.md) | Creates specs before coding. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`subagent-driven-development`](skills/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`teach`](skills/teach/SKILL.md) | Teach the user a new skill or concept, within this workspace. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`to-questionnaire`](skills/to-questionnaire/SKILL.md) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`to-spec`](skills/to-spec/SKILL.md) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`to-tickets`](skills/to-tickets/SKILL.md) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured… | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`triage`](skills/triage/SKILL.md) | Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention. | [vercel-labs/skills](https://github.com/vercel-labs/skills) | MIT |
| [`using-agent-skills`](skills/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`using-git-worktrees`](skills/using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`using-superpowers`](skills/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying… | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`wait-what`](skills/wait-what/SKILL.md) | Stop. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`wizard`](skills/wizard/SKILL.md) | Generate an interactive bash wizard that walks a human through steps only they can perform. | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT |
| [`writing-plans`](skills/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`writing-skills`](skills/writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | [obra/superpowers](https://github.com/obra/superpowers) | MIT |

### Notes & knowledge (`notes-knowledge`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-notes-knowledge`](skills/pack-notes-knowledge/SKILL.md) | Work inside a Markdown knowledge base: Obsidian Flavored Markdown with wikilinks, callouts and properties, Bases views and formulas, JSON Canvas… | **pack** | mixed |
| [`bulletmind`](skills/bulletmind/SKILL.md) | Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`defuddle`](skills/defuddle/SKILL.md) | Extract clean Markdown from HTML pages with Defuddle CLI. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`json-canvas`](skills/json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`knap`](skills/knap/SKILL.md) | Render Markdown from templates and structured data using Knap CLI. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-bases`](skills/obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-cli`](skills/obsidian-cli/SKILL.md) | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-clipper-template-creator`](skills/obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`obsidian-markdown`](skills/obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`unpaid-intern`](skills/unpaid-intern/SKILL.md) | A free second brain for work in plain markdown files the user owns. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |

### Mobile apps (`mobile-apps`)

| Skill | Description | Upstream | Licence |
|---|---|---|---|
| [`pack-mobile-apps`](skills/pack-mobile-apps/SKILL.md) | Native and cross-platform mobile work: Android with Kotlin, Compose and Material 3, iOS application development, Flutter, React Native and Expo… | **pack** | mixed |
| [`android-native-dev`](skills/android-native-dev/SKILL.md) | Android native application development and UI design guide. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`animate-expo`](skills/animate-expo/SKILL.md) | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which… | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| [`developing-genkit-dart`](skills/developing-genkit-dart/SKILL.md) | Generates code and provides documentation for the Genkit Dart SDK. | [google/skills](https://github.com/google/skills) | Apache-2.0 |
| [`flutter-dev`](skills/flutter-dev/SKILL.md) | A practical guide for building cross-platform applications with Flutter 3 and Dart. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`frontend-architecture`](skills/frontend-architecture/SKILL.md) | A portable, framework-agnostic architecture style for any React or React Native frontend. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`frontend-observability`](skills/frontend-observability/SKILL.md) | A portable, framework-agnostic field-side observability pattern for React or React Native integrations. | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | MIT |
| [`ios-application-dev`](skills/ios-application-dev/SKILL.md) | A practical guide for building iOS applications using UIKit, SnapKit, and SwiftUI. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`kotlin-exposed-patterns`](skills/kotlin-exposed-patterns/SKILL.md) | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository… | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`kotlin-testing`](skills/kotlin-testing/SKILL.md) | Patrones de pruebas Kotlin con Kotest, MockK, pruebas de coroutines, pruebas basadas en propiedades y cobertura con Kover. | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`react-native-dev`](skills/react-native-dev/SKILL.md) | A practical guide for building production-ready React Native and Expo applications. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`vercel-react-native-skills`](skills/vercel-react-native-skills/SKILL.md) | Comprehensive best practices for React Native and Expo applications. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | NOASSERTION |

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
