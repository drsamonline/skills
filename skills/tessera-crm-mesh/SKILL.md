---
name: tessera-crm-mesh
description: Every system a team already runs becomes a node; the mesh presents one customer view across them, routes work to whichever node should handle it, and writes every action in every system to a single hash-chained ledger — with a native node that is the system of record when there is no CRM at all. Under development: published to be inspected, not adopted.
metadata:
  title: "TESSERA — the mosaic layer above every CRM"
---

# TESSERA — the mosaic layer above every CRM

A layer that sits above the systems a team already runs instead of replacing them. Each connected
system becomes a node; the mesh presents one customer view, routes work, and writes every action
to one hash-chained ledger. A native CRM is one node in that mesh, not the product.

## When to use

- You are designing a system that must reconcile records across several systems of record without a migration.
- You need an auditable answer to "which system did this field come from, and by which rule?".
- You are reading this repository for its method, not to deploy it: the README opens with a status block saying it is not finished and not released.

## Method

1. Start with the constraint that shapes the architecture: one founder and a five-thousand-person organisation run the same code paths.
2. Choose a mode. **As a layer**: point it at the CRMs a team already runs — every field shows which system it came from and the rule that chose it, and nothing is merged without a rule being recorded. **As the CRM**: `python3 -m tessera.demo --standalone` starts it with no external system, and the native node is the system of record.
3. Read `CLAIMS.md` before believing anything: it lists every public claim beside the command that checks it, and the status block states how many are unverified.
4. Use `CONFORMANCE.md` for the connector checks (four connectors, sixteen checks, generated) and `docs/audit/defect-register.md` for the audit trail.
5. Treat every action as a ledger entry: the hash chain is what makes the reconciliation tamper-evident.
6. Run the gates in `scripts/` — docs freshness, links, claims, conformance, DDL, smoke — before any change is called done.

## Key files / entry points

- `tessera/` — the reference core: `canonical.py`, `conflict.py`, `compliance.py`, `automation.py`, `archive.py`, `checkpoint.py`, `access.py`, `api.py`, `cli.py`, `bulk.py`, `bench.py`.
- `CLAIMS.md` — every public claim and the command that checks it.
- `CONFORMANCE.md` — the generated connector conformance matrix.
- `docs/index.md` — the document map; `docs/16-acceptance-criteria.md`, `docs/48-standalone.md` — what standalone means and what it still is not.
- `DEVELOPMENT.md` — the gate to leave the under-development state.
- `tests/` — 37 test modules; the README badge records the current passing count.

## Gotchas

- **It is not finished, and the repository says so.** Published so the work can be inspected, not adopted; version numbers are build numbers and every release is flagged pre-release.
- **The claims list is the honest surface.** Some claims are unverified and several deliverables are partial; quoting the README without `CLAIMS.md` overstates the system.
- **Adoption is additive or it is a migration.** The moment a connector needs data moved rather than read, the premise ("the first result arrives before anything is migrated") is gone.
- **Two modes, one code path.** A change that only works in standalone is a change that breaks the layer mode.
- **`tessera-app` is the companion surface, not the engine.** Keep the console's assumptions out of the core.

## Source projects

- [tessera](https://github.com/drsamonline/tessera) — the reference core, the claims register, the conformance matrix and the audit trail.
- [tessera-app](https://github.com/drsamonline/tessera-app) — the console that sits on it.
