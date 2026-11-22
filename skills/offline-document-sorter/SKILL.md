---
name: offline-document-sorter
description: Build an ultra-light semantic file sorter as one Rust binary: drop a file or a folder and it lands somewhere you can predict, with a log entry that explains why — local embeddings, no service, no telemetry, and a stated size/RAM/startup budget.
metadata:
  title: "Sorta"
---

# Sorta — an offline document sorter with a budget

An ultra-light, offline-first semantic document sorter: one binary, no service, no telemetry, no
cloud. Drop a file on it (or point it at a folder) and it lands in a folder you can predict, with a
log entry that explains why. Rust 2021, Windows and Linux, targets under 20 MB / 40 MB idle /
300 ms cold start — measured at 1.2 MB and 915 KB.

## When to use

- Files arrive faster than anyone will file them, and the destination should be predictable rather than clever.
- The material is private, so classification has to run locally with no network.
- A tool has to be *light* — a stated budget, measured, not a vague claim of "fast".

## Method

1. Write the **budget** down before the code: binary size, idle RAM, cold start. It is the design constraint that keeps an ML feature from becoming a service.
2. Classify with **local embeddings**, not an LLM call — the difference is a dependency and a data flow, not a quality level.
3. Make the destination predictable: a small, named folder set with a documented rule per folder, so the user can correct it once and be right afterwards.
4. Log the **reason** for every move ("matched: invoice vocabulary"), because a sorter you cannot audit gets turned off.
5. Ship as one static binary with no C/C++ runtime linked; that is what makes "drop it on any machine" true.
6. Cloud is strictly opt-in and off by default.

## Key files / entry points

- The classifier (local embeddings) and the folder rules.
- The move log — the audit trail.
- The release build (size and dependency checks).

## Gotchas

- A sorter that moves files irreversibly will be distrusted the first time it is wrong; keep a dry-run and an undo log.
- Embedding models are large; a 1.2 MB binary means the model is either tiny, quantised or optional — say which.
- Predictability beats accuracy: a user can fix a rule, but cannot fix a mystery.

## Source projects

- [Sorta](https://github.com/drsamonline/Sorta)
