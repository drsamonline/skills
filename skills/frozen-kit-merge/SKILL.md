---
name: frozen-kit-merge
description: Merge one library into another without breaking anyone who vendors it: move the code, keep a frozen shim repository that still resolves, repoint the docs at the new path, and say plainly in the README that it is no longer maintained.
metadata:
  title: "motion-kit"
---

# motion-kit — folding a kit into another, and leaving a readable shim

On 2026-11-12 motion-kit was folded into tokens-kit as version 2.0.0, reached as `T.motion.*`. The
repository was not deleted and the code was not left to rot: it became a **frozen shim** that still
resolves for anything vendoring it, with a README that says so in the first line.

## When to use

- Two libraries are meaningless apart (a token set without its motion is half a design system) and consumers want both.
- Other repositories vendor the old one by path, so deleting it breaks them silently.
- You cannot create the repository the merge really wants, so the survivor has to carry both halves under its old name.

## Method

1. Move the code into the survivor and release it as a **major** (`tokens-kit` 2.0.0), exposing the old surface at a namespaced path (`T.motion.*`).
2. Keep the old repository readable: same files, same exports, so a vendored copy still resolves.
3. Rewrite the old README in the first line: *this kit is no longer maintained on its own*, where it went, and **why** — the reason is what stops someone re-splitting it next month.
4. Add an old-to-new table (`Motion.ease` → `Tokens.motion.ease`) so migration is mechanical.
5. Freeze the code at the last pre-merge version and say so, rather than leaving it half-edited.
6. When a later pass wants to add a feature "to motion-kit", that is the signal the merge worked: put the feature in the survivor, or in the kit that actually owns the concept.

## Key files / entry points

- `README.md` — the notice, the reason and the old-to-new table.
- The frozen exports that keep vendored copies resolving.

## Gotchas

- A shim that diverges from the survivor is worse than a deletion: two behaviours, one name, no owner.
- "Merged" is not "deprecated": consumers need the new path in the same breath as the notice, or the notice is just bad news.
- The merge's real cost is documentation, not code — the old-to-new table is the deliverable.

## Source projects

- [motion-kit](https://github.com/drsamonline/motion-kit)
