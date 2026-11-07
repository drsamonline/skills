# Manus Modifications to Upstream HyperFrames Skills

This document records every change Manus made to upstream HyperFrames skill materials when packaging them as the `html-video-production` Manus skill. It is maintained for Apache License 2.0 §4(b): modified files carry prominent `[MANUS OVERRIDE]` notices, and this ledger identifies the source, scope, and reason for every localized modification.

## Provenance

| Field | Value |
| --- | --- |
| Upstream project | [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) |
| Upstream license | Apache License 2.0 (preserved verbatim in `../UPSTREAM_LICENSE_APACHE-2.0.txt`) |
| Previous pinned upstream commit | `c811a2750a2f9a242b764959e7509217f9943511` |
| Pinned upstream release tag | `v0.7.64` |
| **Pinned upstream commit** | `11cd61d1e3ab945f40991c9ee18e9598b3dfaccd` |
| Pinned commit date | 2026-07-18 |
| Sync date | 2026-07-20 |
| Packaging model | Full coverage. All 19 upstream skills under `skills/` are redistributed under `references/`, flattened one level so each resides directly at `references/<skill-name>/`. |

### Bundled upstream skills (19/19)

| Category | Skills |
| --- | --- |
| Domain and router skills | `hyperframes`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use` |
| Workflow skills | `product-launch-video`, `faceless-explainer`, `pr-to-video`, `motion-graphics`, `embedded-captions`, `talking-head-recut`, `music-to-video`, `slideshow`, `general-video`, `remotion-to-hyperframes` |
| Source adapter | `figma` |

### Structural upstream changes in this sync

| Upstream change | Manus packaging action |
| --- | --- |
| Added `skills/figma/` | Bundled as `references/figma/`, routed as a source adapter, and patched so credentials are never requested in chat or through insecure instructions. |
| Added `skills/hyperframes-keyframes/` | Bundled as `references/hyperframes-keyframes/` and added to the root domain-skill router. |
| Removed `skills/hyperframes-media/` | Removed from the package; its media engine is now consolidated under `references/media-use/audio/`. All media references in Manus overrides were updated to the new paths. |
| Removed `skills/website-to-video/` | Removed from the package. Website tours/showcases now route to `product-launch-video`, as described by upstream. |

## Why these changes exist

Upstream documentation includes safe composition, animation, rendering, and workflow logic as well as paths that can authenticate to or charge paid cloud services. In Manus, all generative media follows the **Three-Tier Priority Model** in [`media-generation.md`](media-generation.md):

1. **Tier 1 (default):** Manus-native `generate_speech`, `generate_music`, and `generate_image`, bridged into HyperFrames by hand-writing `audio_meta.json` and `.media/manifest.jsonl`.
2. **Tier 2 (permitted fallback):** local, free, offline `hyperframes transcribe`, `hyperframes remove-background`, bundled Pixabay SFX, and `hyperframes tts` (Kokoro) as a last-resort voice.
3. **Tier 3 (hard prohibited):** `npx hyperframes init`, `npx hyperframes skills update`, `hyperframes lambda *`, and paid HeyGen/ElevenLabs branches.

The changes are intentionally **destructive at each unsafe instruction**. A banner alone is not enough: step-by-step reading must not reach a sign-in gate, provider choice, auto-puller, paid cloud-render command, or a command that invokes an upstream media orchestrator.

## Modified files and changes

### 1. Manus-authored package files

| Path | Change |
| --- | --- |
| `SKILL.md` | Rebuilt the Manus router. The Fidelity Gate (Route A / Route B / Route C) remains at the top. The router removes obsolete `hyperframes-media` and `website-to-video` entries; adds `figma` and `hyperframes-keyframes`; routes website tours to `product-launch-video`; and restates the localization contract. |
| `_manus-overrides/media-generation.md` | Updated the canonical media contract for the upstream `media-use/audio/` layout. It explicitly forbids all upstream `audio.mjs` and `resolve.mjs` paths, preserves the `audio_meta.json` and `.media/manifest.jsonl` bridge schemas, and lists `skills update` alongside `init` as an auto-puller prohibition. |
| `_manus-overrides/modifications.md` | This provenance and modification ledger. |
| `assets/sfx/` | Refreshed from upstream `media-use/audio/assets/sfx/` as the one canonical 19-file Pixabay SFX set. |

### 2. Standard banner on every bundled `SKILL.md`

A prominent `[MANUS OVERRIDE]` banner is prepended above the original YAML frontmatter in every one of these 19 files:

`embedded-captions`, `faceless-explainer`, `figma`, `general-video`, `hyperframes`, `hyperframes-animation`, `hyperframes-cli`, `hyperframes-core`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-registry`, `media-use`, `motion-graphics`, `music-to-video`, `pr-to-video`, `product-launch-video`, `remotion-to-hyperframes`, `slideshow`, and `talking-head-recut`.

The banner makes `_manus-overrides/media-generation.md` controlling; skips upstream auth/preflight and provider-choice paths; prohibits upstream `audio.mjs` / `resolve.mjs`, `init`, `skills update`, and `lambda`; and names the Manus-native ledger substitute.

### 3. Auto-puller and scaffold replacements

Every Markdown instruction that invokes or recommends `npx hyperframes skills update` or `npx hyperframes init` is replaced with a `[MANUS OVERRIDE]` manual-scaffold instruction: create the directory, run `npm init -y`, install with `npm install hyperframes`, and author the composition locally. This includes top-level workflow preambles and CLI reference material, including `references/hyperframes-cli/SKILL.md`, `references/hyperframes-cli/references/init-and-scaffold.md`, `references/hyperframes/references/skill-lifecycle.md`, and every affected workflow document.

### 4. CLI and paid cloud-render replacements

| Path | Change |
| --- | --- |
| `references/hyperframes-cli/SKILL.md` | Replaces the scaffold line with the manual scaffold recipe and replaces the Lambda render option with an explicit `[MANUS OVERRIDE]` local `render --docker --strict` alternative. |
| `references/hyperframes-cli/references/lambda.md` | Replaces the executable Lambda workflow with the local-render alternative. |
| `references/hyperframes-cli/references/cloud.md` and `references/hyperframes-cli/references/cloudrun.md` | Adds an explicit localization notice that paid/authenticated cloud-render paths are not a Manus default and must not be selected by these skill instructions. |

### 5. Media engine, resolver, auth-gate, and provider-choice replacements

| Scope | Change |
| --- | --- |
| `references/media-use/SKILL.md` | Replaces HeyGen setup, auth preflight, provider defaults, and executable resolver/audio-engine commands with a Manus-native generation and ledger-writing directive. Safe local schema, asset-operation, and provenance material remains available as reference. |
| `references/media-use/audio/references/bgm.md`, `tts.md`, `tts-to-captions.md`, `requirements.md`, `sfx.md`, and related audio guidance | Replaces auth gates, `STOP`/wait language, API-key/provider-choice instructions, and paid-provider defaults with the Tier-1 native path and Tier-2 fallback note. Schema/reference details are retained only beneath an explicit override. |
| `references/media-use/references/operations.md` and other media-use Markdown instructions containing `resolve.mjs` | Adds an inline `[MANUS OVERRIDE]` immediately above each resolver command. The original command remains directly below as schema reference, but is non-executable under Manus. |
| `references/faceless-explainer/SKILL.md`, `references/pr-to-video/SKILL.md`, and `references/product-launch-video/SKILL.md` | Adds an inline `[MANUS OVERRIDE]` immediately above every workflow-local `scripts/audio.mjs` command; the original command remains as the schema reference. Replaces the upstream auth-status preflight and sign-in/offline decision branch with the native-media directive. |
| `references/general-video/SKILL.md`, `references/music-to-video/SKILL.md`, and `references/motion-graphics/SKILL.md` | Replaces upstream authenticated-provider / media-source paths with the native-media directive and removes auto-puller execution. |
| All other Markdown files containing an executable `audio.mjs` or `resolve.mjs` media command | Receive the same immediately preceding `[MANUS OVERRIDE]` marker. Commands remain as non-executable schema references only. |

### 6. Figma credential localization

`references/figma/SKILL.md` is newly bundled and receives the standard banner plus a destructive replacement of its personal-token preflight. The patch prohibits asking users to paste a Figma token or exporting a token through chat. It directs agents to use an already securely configured connector/session or a user-provided export, and to report a missing approved access path rather than inventing or soliciting credentials. Its Figma-specific `skills update` instruction is also replaced by the manual-scaffold rule.

### 7. Trimmed non-instructional bloat

The rebuild removes, from `references/` only:

- Demo images: `*.png`, `*.jpg`, `*.jpeg`, `*.webp`, `*.gif`, and `*.avif`.
- Demo videos: `*.mp4`, `*.webm`, and `*.mov`.
- Bundled web fonts: `*.woff2`, `*.woff`, `*.ttf`, and `*.otf`, plus generated `fonts.css`.
- Vendored `gsap*.min.js` copies.
- Duplicate `sfx/*.mp3` files (the canonical package-root `assets/sfx/` remains).

All instructional Markdown, JSON schemas, scripts, and non-duplicative textual resources are retained. Upstream scripts are preserved unmodified as schema/reference material; only documentation is patched to prohibit their unsafe execution.

### 8. Verified upstream-relative link repair

`references/hyperframes-creative/references/house-style.md` contained thirteen links whose relative prefixes did not resolve after the upstream skills tree was flattened: three typography references, one motion-principles reference, and nine palette references. Each target was verified to exist in the upstream tree, then the links were corrected respectively to `typography.md`, `motion-principles.md`, and `../palettes/<name>.md`. No instructional content was altered.

## Re-syncing with future upstream releases

1. Compare **only** upstream `skills/` against the pinned commit and a stable release tag.
2. If the skill set changes structurally, back up the installed package and rebuild all `references/` from upstream; flatten `skills/<name>/` to `references/<name>/`.
3. Reapply every patch class above and update the root router, media contract, canonical SFX source, and this ledger.
4. Validate the skill package, size, internal relative links, and guard results. The following commands must return only explicitly `[MANUS OVERRIDE]`-annotated lines:

```bash
grep -rn 'STOP and wait\|STOP for the user' /home/ubuntu/skills/html-video-production/references
grep -rniE 'which (voice|tts|music) provider|ask the user which' /home/ubuntu/skills/html-video-production/references
grep -rn 'hyperframes init' /home/ubuntu/skills/html-video-production/references
```

## Per-file Sync Audit

This appendix is generated during the sync. It records every documentation file that received a Manus-localization change in addition to the category descriptions above.

### Standard banners

| File | Change |
| --- | --- |
| `references/embedded-captions/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/faceless-explainer/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/figma/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/general-video/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-animation/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-cli/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-core/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-creative/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-keyframes/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/hyperframes-registry/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/media-use/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/motion-graphics/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/music-to-video/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/pr-to-video/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/product-launch-video/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/remotion-to-hyperframes/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/slideshow/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |
| `references/talking-head-recut/SKILL.md` | Top-of-file `[MANUS OVERRIDE]` banner |

### Inline media-command markers

| File | Markers inserted |
| --- | ---: |
| `references/faceless-explainer/SKILL.md` | 3 |
| `references/media-use/SKILL.md` | 20 |
| `references/motion-graphics/SKILL.md` | 1 |
| `references/motion-graphics/phases/source/guide.md` | 1 |
| `references/pr-to-video/SKILL.md` | 3 |
| `references/product-launch-video/SKILL.md` | 3 |

### Destructive risk-line replacements

| File | Lines replaced with a Manus override |
| --- | ---: |
| `references/embedded-captions/SKILL.md` | 4 |
| `references/embedded-captions/references/anti-patterns.md` | 1 |
| `references/embedded-captions/references/bespoke-vs-presets.md` | 1 |
| `references/embedded-captions/references/failure-modes.md` | 1 |
| `references/faceless-explainer/SKILL.md` | 9 |
| `references/faceless-explainer/references/story-design.md` | 1 |
| `references/figma/SKILL.md` | 1 |
| `references/general-video/SKILL.md` | 4 |
| `references/hyperframes-animation/techniques.md` | 1 |
| `references/hyperframes-cli/SKILL.md` | 6 |
| `references/hyperframes-cli/references/cloud.md` | 11 |
| `references/hyperframes-cli/references/cloudrun.md` | 1 |
| `references/hyperframes-cli/references/init-and-scaffold.md` | 7 |
| `references/hyperframes-cli/references/lambda.md` | 1 |
| `references/hyperframes-core/references/brief-contract.md` | 1 |
| `references/hyperframes-core/references/brief-format.md` | 1 |
| `references/hyperframes-core/references/production-loop.md` | 1 |
| `references/hyperframes-core/references/script-format.md` | 2 |
| `references/hyperframes-core/references/subagent-dispatch.md` | 1 |
| `references/hyperframes-core/references/tailwind.md` | 2 |
| `references/hyperframes-creative/references/typography.md` | 2 |
| `references/hyperframes-registry/SKILL.md` | 3 |
| `references/hyperframes-registry/references/contributing.md` | 1 |
| `references/hyperframes-registry/references/discovery.md` | 1 |
| `references/hyperframes-registry/references/install-locations.md` | 3 |
| `references/hyperframes-registry/references/templates.md` | 2 |
| `references/hyperframes/SKILL.md` | 2 |
| `references/hyperframes/references/capability-menu.md` | 3 |
| `references/hyperframes/references/skill-lifecycle.md` | 5 |
| `references/media-use/SKILL.md` | 17 |
| `references/media-use/audio/references/captions/authoring.md` | 1 |
| `references/media-use/audio/references/captions/transcript-handling.md` | 1 |
| `references/media-use/audio/references/tts-to-captions.md` | 1 |
| `references/media-use/luts/README.md` | 2 |
| `references/media-use/references/operations.md` | 29 |
| `references/media-use/references/telemetry-dashboard.md` | 1 |
| `references/motion-graphics/SKILL.md` | 3 |
| `references/music-to-video/SKILL.md` | 4 |
| `references/pr-to-video/SKILL.md` | 9 |
| `references/pr-to-video/references/story-design.md` | 2 |
| `references/product-launch-video/SKILL.md` | 9 |
| `references/product-launch-video/references/story-design.md` | 2 |
| `references/remotion-to-hyperframes/SKILL.md` | 6 |
| `references/remotion-to-hyperframes/assets/test-corpus/tier-4-escape-hatch/README.md` | 2 |
| `references/remotion-to-hyperframes/references/api-map.md` | 5 |
| `references/remotion-to-hyperframes/references/escape-hatch.md` | 7 |
| `references/remotion-to-hyperframes/references/limitations.md` | 2 |
| `references/remotion-to-hyperframes/references/lottie.md` | 2 |
| `references/remotion-to-hyperframes/references/media.md` | 2 |
| `references/remotion-to-hyperframes/references/transitions.md` | 1 |
| `references/slideshow/SKILL.md` | 1 |
| `references/slideshow/references/standalone-harness.md` | 1 |
| `references/talking-head-recut/SKILL.md` | 3 |

### Verified link repairs

| File | Links repaired |
| --- | ---: |
| `references/hyperframes-creative/references/house-style.md` | 13 |

**Trimmed non-instructional files:** 146. **Canonical SFX retained:** 19.

### Post-install guard cleanup

The final `hyperframes init` guard found two non-executable legacy references in bundled scripts. Both were retained as behavior-preserving comments and rewritten with an explicit `[MANUS OVERRIDE]` notice:

| File | Change |
| --- | --- |
| `references/embedded-captions/scripts/render-and-composite.sh` | Replaced the legacy auto-puller phrase in an asset-linking comment with an explicit override notice; no shell behavior changed. |
| `references/embedded-captions/scripts/transcribe.cjs` | Replaced the legacy auto-puller phrase in a transcript-schema comment with an explicit override notice; no JavaScript behavior changed. |

