---
name: pico-automation-engine
description: 114 rules, four risk tiers, universal undo, slot dialogue, replay from snapshots and a trigger DSL on the Python standard library alone — with an optional model that is only ever allowed to propose a command string, never run one. Deleting the model pack loses no capability, only phrasing convenience.
metadata:
  title: "pico — a personal automation engine on the standard library"
---

# pico — a personal automation engine on the standard library

The rule engine is the spine; the model is a plug-in translator. Every claim about safety is
enforced in the core resolver and proved by a numbered test, not by a prompt.

## When to use

- You are automating a personal machine and cannot accept a network call, an account or a telemetry stream.
- A destructive command needs a risk gate, a consent window and a universal undo rather than a warning message.
- You want an optional language model in the loop but the model must not be able to execute anything.

## Method

1. Run one-shot: `python3 pico.py tasks`, `python3 pico.py spend 250 food`, `python3 pico.py emi 500000 8.5 240`; or open the console with `python3 pico.py --ui` (serves on `127.0.0.1:8765`).
2. Resolve a sentence to a rule through `pico/ladder.py` — 114 rules, four risk tiers and slot dialogue; use `dry <cmd>` to see which tier resolved a command, its risk tier and what it would touch.
3. Respect the gate: a send or delete is intercepted and state is held for 120 s pending consent; a `write`-tier command *proposed by the model* is gated like a send, while the same command typed by hand runs.
4. Register an inverse for every mutation so `undo` can replay handlers in reverse; replay from a snapshot to reproduce a state.
5. Keep privacy domains in `never_send` — it is checked in the **core** resolver before any translator is called.
6. If a model is used at all, it lives in `packs/llm.py`, returns a string, and the core matches it against `RULES` before anything runs. Delete the pack and the system stays complete.
7. Guard the packs: import and call are both wrapped, so one bad pack prints a failure and continues, and the REPL never dies.
8. Test with the suite in `tests/` (the README badge records the current count).

## Key files / entry points

- `pico.py` — the entry point (`tasks`, `spend`, `emi`, `--ui`, `dry`, `undo`).
- `pico/ladder.py` — rules, risk tiers, slot dialogue.
- `pico/cmd_*.py` — the command families (tasks, files, money, time, quarantine, repair, doctor, web).
- `packs/` — the capability packs (`llm.py` is the only one that talks to a model).
- `budget.json`, `templates/`, `web/` — state, scaffolding and the browser console.
- `docs/COMMANDS.md`, `docs/ARCHITECTURE.md`, `docs/ANDROID.md` — the reference and the port notes.

## Gotchas

- **The model is a translator, not an actor.** It returns a string; nothing it says runs until a rule matches it. A no-match is a rejection with a stated reason, which is how a hallucination cannot invent an action.
- **A hand-typed write and a model-proposed write are not treated alike.** The gate applies to the proposed one; that asymmetry is deliberate.
- **Undo is only as good as the inverse.** A handler that mutates without registering an inverse is unrecoverable — check the handler, not the undo command.
- **The console is loopback-only.** File and network commands need the local engine; the Pages demo runs the resolver and the arithmetic in the browser and nothing else.
- **Zero dependencies is a constraint, not an accident.** The engine is stdlib-only so it runs where `pip install` does not.

## Source projects

- [pico](https://github.com/drsamonline/pico) — the engine, its rule ladder, packs, docs and tests.
