---
name: sui-free-route-gateway
description: Every free model route is probed, policy-checked and scored before it can answer a prompt; every escalation is traced; paid credentials are not read at all unless the gate is opened — with fifteen invariants kept as data, each naming the module that enforces it and the test that proves it.
metadata:
  title: "Sui — a verification-first free-route AI gateway"
---

# Sui — a verification-first free-route AI gateway

A gateway that refuses to report success it has not measured. A green tick requires a real
model round-trip, and every failover is visible in the response, the ledger and the dashboard.

## When to use

- You are routing prompts across free or mixed-tier model providers and need the routing decision to be explainable.
- You must guarantee that paid credentials are never read, and that no prompt content reaches telemetry.
- You want failover that never degrades silently.

## Method

1. `npx sui` — one command finds the keys on the machine, finds your coding tools, writes a config, sends a real request through the gateway, prints the endpoint and starts serving.
2. Read the invariants before changing routing: `packages/core/src/invariants.js` holds fifteen, each with the module that enforces it and the test that proves it. `npm test` fails if an invariant loses either.
3. Keep the ones you can feel from outside: **I4** paid credentials are never read unless `paid_tiers.enabled` is true (checked before the environment is touched); **I6** zero silent degradation — every failover is in the response, the ledger and the dashboard; **I7** onboarding cannot report success without a real round-trip; **I11** no prompt content in telemetry, a salted hash and a length only; **I12** a provider marked `tos: avoid` is never auto-routed; **I13** the circuit breaker trips on 5xx and transport failures only, never on 401, 404 or 429.
4. Inspect a route's evidence in the dashboard — budget, routing pool, combos, prompt-free usage and recent turns.
5. Read `AUDIT.md` and `AUDIT-2026-11-15.md` before trusting a claim; `evals/` holds the evaluation material.

## Key files / entry points

- `packages/core/src/invariants.js` — the fifteen invariants as data.
- `packages/core/src/` — `config.js`, `errors.js`, `recipes.js`, `tenants.js`, `index.js`.
- `apps/cli/` — the `npx sui` onboarding path; `apps/gateway/` — the serving path.
- `recipes/`, `config/`, `evals/`, `test/` — routing recipes, configuration, evaluations and the test suite.
- `AUDIT.md`, `ROADMAP.md`, `TERMS.md` — the audit trail, the plan and the terms the provider policy is drawn from.

## Gotchas

- **A 429 is not a transport failure.** The breaker must not trip on 401, 404 or 429 — a rate limit is an answer, not an outage, and tripping on it turns a slow provider into a dead route.
- **"Free" is a claim to verify, not a tier to assume.** A provider marked `tos: avoid` must never be auto-routed, whatever its score.
- **Success needs a round-trip.** Onboarding that prints a green tick from configuration alone is the exact failure I7 exists to prevent.
- **Telemetry is a hash and a length.** Any debug logging that includes a prompt body breaks I11 and the test that guards it.
- **Paid keys must not be read at all** — not read-then-ignored, since a read is already a leak of intent in logs and in the environment.

## Source projects

- [sui](https://github.com/drsamonline/sui) — the gateway, its invariants, audits and evals.
