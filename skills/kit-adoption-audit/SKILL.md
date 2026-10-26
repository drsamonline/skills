---
name: kit-adoption-audit
description: Measure which apps actually consume each shared kit and which hand-roll the same capability, from repository trees and blob SHAs alone, before proposing a kit create, update or retire.
metadata:
  title: "Kit adoption audit"
---

# Kit adoption audit

A shared kit only pays for itself if apps call it. The question this audit
answers is measurable and cheap: for every kit, which repos carry it, which call
it, and which implement the same thing themselves. The answer decides whether a
kit should be created, updated, adopted — or retired.

## When to use

- A weekly or periodic pass over a multi-repo estate, before writing retrofit PRs.
- A kit looks unused and you need to know whether it is dead or merely unknown.
- You are about to create a kit and want to prove the duplication is real first.

## Method

1. List the repos and each one's default branch; fetch every repo's **recursive
   tree** in one call per repo. The tree carries each blob's SHA, which is the
   content hash — that is what makes duplication measurable.
2. For every kit repo, note the name of its main file (`web-kit.js`,
   `repertory-kit.js`, …). A vendored copy keeps that filename.
3. For every app repo, record which `*-kit.js` files it contains. **Presence is
   adoption**; a kit's name in prose, in a tool list or inside a base64 blob is
   not.
4. Group blobs by SHA inside each repo to find one file stored twice, and across
   repos to find the same file shipped by several. Two `app.html` files with the
   same SHA are one artefact, not two.
5. For every kit with no adopter, grep the apps that clearly need that capability
   for the giveaway signal — a `requestAnimationFrame` loop, an
   `AES-GCM` import, a `crc32` table, an SM-2 interval — and read the hit before
   believing it.
6. Write down three lists: adopted kits, zero-adopter kits, and apps that
   duplicate a kit. That is the whole output, and it is enough to order the work.

## Key files

- The tree dumps — the evidence; keep them, because a claim about duplication is
  only as good as the tree it came from.
- Each kit's main `.js` — the filename the audit searches for.
- `forge/PROGRESS.log` — the estate's own running record of retrofits, kit
  proposals and known gaps; read it before proposing anything, so the audit
  agrees with what has already been decided.

## Gotchas

- **Present is not the same as used.** Three repos vendor `web-kit.js` and never
  call it, so the retrofit target is the call site, not the file.
- A regex over a minified page matches base64 by accident: "interval" appears
  inside a PNG data URI. Read the surrounding code every time.
- The `docs/play/` mirror makes one file look like two, and the mirror is a
  build output — its presence is not duplication to be removed, it is a
  convention to be understood.
- Adoption can be **unsafe even when it is possible**: `web-kit`'s storage
  writes under a fixed `loom:` prefix, so swapping an app onto it orphans the
  keys a user has already saved. That is a kit gap, not an app fault.
- Do not count a kit's own demo page as an adopter, and do not count the kit
  repo itself.

## Source projects

- [skills](https://github.com/drsamonline/skills) — the knowledge base that records this method.
- [web-kit](https://github.com/drsamonline/web-kit) — the most-adopted kit, and the one whose storage namespace blocks three retrofits.
- [forge](https://github.com/drsamonline/forge) — the run log that records each retrofit and kit proposal.
- [repertory-kit](https://github.com/drsamonline/repertory-kit) and [srs-kit](https://github.com/drsamonline/srs-kit) — two kits with no adopter while the apps that need them hand-roll the maths.
