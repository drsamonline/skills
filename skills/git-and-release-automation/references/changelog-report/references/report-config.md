# Report configuration

This file holds the instance-specific settings for the changelog report. The
build interview fills it in once; every later run reads it. Replace every
`<placeholder>` below with the user's answers.

## GitHub source

- **Organization:** `drsamonline` — the GitHub org whose repos you track.
- **Repositories:** the 45 user-facing product repos to track. Every merged PR
  in these repos is relevant — no product filtering is needed.

  Clinical / homeopathy apps:
  - `drsamonline/open-materia-medica` — all PRs relevant
  - `drsamonline/boericke-repertory` — all PRs relevant
  - `drsamonline/kent-repertory-explorer` — all PRs relevant
  - `drsamonline/remedy-relationship-explorer` — all PRs relevant
  - `drsamonline/skin-case-tracker` — all PRs relevant
  - `drsamonline/app-encrypted-case-log` — all PRs relevant
  - `drsamonline/gentle-pediatrics-companion` — all PRs relevant
  - `drsamonline/whispering-body-first-aid` — all PRs relevant
  - `drsamonline/unstoppable-mind-companion` — all PRs relevant
  - `drsamonline/mnemosyne-companion` — all PRs relevant
  - `drsamonline/the-symphony-companion` — all PRs relevant
  - `drsamonline/app-panchang` — all PRs relevant
  - `drsamonline/today-card` — all PRs relevant
  - `drsamonline/seance` — all PRs relevant
  - `drsamonline/OMM` — all PRs relevant

  Tools and productivity apps:
  - `drsamonline/SmartNotes` — all PRs relevant
  - `drsamonline/TTB` — all PRs relevant
  - `drsamonline/lexora` — all PRs relevant
  - `drsamonline/helioprism` — all PRs relevant
  - `drsamonline/offline-pdf-toolkit` — all PRs relevant
  - `drsamonline/read-live-transform-app` — all PRs relevant
  - `drsamonline/blinkcode-ai` — all PRs relevant
  - `drsamonline/BLINKTRANSFER` — all PRs relevant
  - `drsamonline/smartbill-app` — all PRs relevant
  - `drsamonline/base-bench` — all PRs relevant
  - `drsamonline/bmi-bmr-tdee-macros-fluid-calculator` — all PRs relevant
  - `drsamonline/All4ONE` — all PRs relevant
  - `drsamonline/CLDR` — all PRs relevant
  - `drsamonline/NEO` — all PRs relevant
  - `drsamonline/The_Browser` — all PRs relevant
  - `drsamonline/ULTIMATE-WINDOWS-OPTIMIZER` — all PRs relevant
  - `drsamonline/HMS` — all PRs relevant
  - `drsamonline/Matneo` — all PRs relevant
  - `drsamonline/lockhtml` — all PRs relevant
  - `drsamonline/app-poets-studio` — all PRs relevant
  - `drsamonline/ambient-sound-studio` — all PRs relevant
  - `drsamonline/conqueror-os` — all PRs relevant

  Games:
  - `drsamonline/neon-runner` — all PRs relevant
  - `drsamonline/retro-strike` — all PRs relevant
  - `drsamonline/dance-fight` — all PRs relevant
  - `drsamonline/aethelgard-games` — all PRs relevant
  - `drsamonline/neon-games` — all PRs relevant
  - `drsamonline/Scrap-and-Gun` — all PRs relevant
  - `drsamonline/idle-city-ages-of-growth` — all PRs relevant
  - `drsamonline/neon-velocity` — all PRs relevant

  Do NOT track the internal kits (`web-kit`, `ui-kit`, `crypto-kit`,
  `audio-kit`, `art-kit`, `ml-kit`, `game-kit`, `case-kit`, `book-kit`,
  `search-kit`, `srs-kit`, `lan-kit`, `astro-kit`, `optical-kit`, `frame-kit`,
  `compress-kit`, `export-kit`, `repertory-kit`, `profile-kit`), the engines
  (`neon-engine`, `saga-vn-engine`, `aethelgard-rpg-engine`), or the
  infrastructure repos (`forge`, `registry`, `dashboard`, `skills`, `backup`,
  `dumps`, `knowledge`, `app-builder`, `app-companion-forge`,
  `drsamonline`, `drsamonline.github.io`, `homoeopathic-materia-medica-repertory-json`).
  If the user explicitly asks to add one, add it here first.

## Product scope

- **Product name:** `drsamonline (the whole fleet)` — the name shown in the
  summary line and the empty-state message.
- **Filter rules (if any):** all PRs relevant — no filtering needed. Every
  tracked repo is a single-product app, so every merged PR in it belongs in
  the report.

## Date resolution

- **Timezone:** `Asia/Kolkata` — the timezone to resolve relative dates in.
  "Today" and "yesterday" are resolved in this timezone; GitHub timestamps are
  UTC and converted for display.

## Branding

- **Company / brand:** `MATNEO`
- **Report title:** `WHATS CHANGED` — shown as the H1 in the header.
- **Eyebrow:** `Updates` — the small uppercase label above the title.
- **Logo:** `assets/logo.svg` — the MATNEO wordmark (constellation mark +
  "MATNEO" in Plus Jakarta Sans ExtraBold), taken from the MATNEO app's own
  brand mark. Embedded as base64 in the PDF.
- **Footer text:** `UPDATES FROM REPOS` — shown at the bottom of every page.

## Schedule & delivery

- **Frequency:** Weekly — a rolling 7-day window ending yesterday (today minus
  7 through yesterday), resolved in Asia/Kolkata.
- **Delivery:** Slack — channel `#CHANGELOG`.
- **Time:** 18:00 IST (end of day).
- **Empty state:** if the window has no merged PRs at all, post a one-line
  all-clear to `#CHANGELOG` (e.g. "No changes this week — nothing merged
  across the 45 tracked repos.") with **no PDF attached**.
