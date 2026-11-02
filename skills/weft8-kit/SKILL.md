---
name: weft8-kit
description: An auditable, step-limited rule engine on the Weft-8 8-bit machine: a rule is an assembly program with a contract — inputs in the ports, one verdict byte out — so a decision can be read, bounded and reviewed.
metadata:
  title: "Weft-8 kit — a rule engine small enough to sign off"
---

# Weft-8 kit — a rule engine small enough to sign off

A rule is a **Weft-8 program with a contract**: the caller puts inputs in the ports (`IN0 0xD0`, `IN1 0xD1`, `IN2 0xD2`, `IN3 0xD3`, each 0–255), the rule writes one byte to the verdict port, and everything else is the machine's business. The point is not nostalgia — it is that a rule you can read in full, on a machine with a step limit, is a rule you can approve.

## When to use

- A decision has to be explainable to someone who will not read the host language.
- You want a rule that provably terminates, because the machine is step-limited.
- You need five worked rules to copy the shape from.

## Method

1. Load `docs/play/weft8.js` (the machine) and `docs/play/rules.js` (the rule set) before your own code; both are plain scripts on a global.
2. Write each rule as assembly with a header stating its ports and its verdict encoding — the contract is documentation that the harness can check.
3. Keep inputs inside 0–255; the ports are bytes, and a rule that assumes a wider value is a rule that will be wrong.
4. Cap execution with the machine's step limit and treat "ran out of steps" as a distinct verdict from "false", so a bug is visible.
5. Test the engine with `node test-node.js` and the page with `node tests/page-smoke.js` (`npm test` runs both).

## Key files / entry points

- `docs/play/weft8.js` — the machine; `docs/play/rules.js` — the example rules.
- `docs/play/index.html` — the demo.
- `test-node.js`, `tests/page-smoke.js` — the two test levels.

## Gotchas

- One byte per port means a rule cannot see a number above 255 — split or scale before the port, never inside the rule.
- A rule with no step limit can loop forever; the limit is the guarantee, not an optimisation.
- The verdict port is one byte: every outcome you care about needs a distinct value, or the caller cannot tell them apart.
- Reading assembly is only an advantage if the rule is short; a 200-line rule is the same black box in a harder language.

## Source projects

- [weft8-kit](https://github.com/drsamonline/weft8-kit) — the rule contract, the port map and the five example rules.
