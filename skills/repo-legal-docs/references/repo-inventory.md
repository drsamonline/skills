# The drsamonline fleet — legal posture and what each repo needs

Snapshot taken 09 November 2026 via the GitHub API: **114 repositories, 105 public, 9 private.**

Licence spread across the 105 public repositories: **96 "Other", 8 MIT, 1 with no licence file at all** (UniRep). Languages: JavaScript 49, Python 30, HTML 12, TypeScript 3, Rust 3, C++ 2, PowerShell 2. Account-wide, six repositories report no licence — UniRep plus the five private `dumps-*` backup repos.

Read the two headline facts together. Ninety-six repos report as "Other" because most carry PolyForm Noncommercial 1.0.0 or a bespoke EULA — both invisible to GitHub's detector and to every dependency scanner downstream. UniRep carries no licence at all, which means all rights reserved and no permission to use. That is a bigger problem than a missing privacy policy, and it is fixed in one commit.

Legal files that exist today, measured across all 105 public repositories: `LICENSE` in 105, `SECURITY.md` in 13, `NOTICE`/`THIRD-PARTY.md` in 9, `CONTRIBUTING.md` in 22, a code of conduct in 12, `PRIVACY.md` in 2 (kitbox and one other), `TERMS.md` in **none**, a disclaimer in **none**.

## Triage — five tiers

### Tier 0 — no licence at all (fix first, today)

One public repository, **UniRep**, plus the five private `dumps-*` backups. Without a `LICENSE` the default is all rights reserved: nobody may copy, fork or use them, including the people the README invites. Pick MIT for reusable kits, PolyForm Noncommercial for the standalone apps, and an EULA for anything sold. For the backup repos a one-line `LicenseRef-Private` note is enough.

Run the audit to list them: `python scripts/audit_legal_docs.py --gh-user drsamonline`.

### Tier 1 — offline tool, no personal data (lightest set)

The bulk of the fleet: kitbox, TTB, base-bench, app-poets-studio, offline-pdf-toolkit, app-image-toolkit, eon-commando, weft8-*, game-kit, ui-kit, web-kit and the other `*-kit` libraries.

Needs: `LICENSE` (present), `SECURITY.md`, and a short factual `PRIVACY.md` on the kitbox model — "collects nothing, here is what localStorage holds, here is how to erase it". That model document is already written and is the template to copy.

### Tier 2 — offline app that stores user content on the device

seance (sealed notes), today-card, musicgen, lumen, srs-kit consumers, accent-oracle (four seconds of speech), app-clip-loom.

Needs Tier 1 plus a "what is stored, where, and how to erase it" section, and — for accent-oracle specifically — an explicit statement that audio is processed on device and not retained, because a voice clip is biometric-adjacent personal data and the user will assume the worst.

### Tier 3 — third-party API or AI in the product

ai-bridge (web-chat models in the editor), smartnote-scheduler (classification), mnemosyne-companion, anything calling a hosted model.

Needs Tier 2 plus `TERMS.md`, a data-flow disclosure naming the provider category and what is transmitted, the provider's retention position, and an AI-output disclaimer. ai-bridge is the sharpest case: it carries prompts and possibly credentials to a third-party web chat, so the privacy document is the product's trust surface.

### Tier 4 — health records and clinical workflow (highest exposure)

**HMS** — a LAN-based hospital management system for homeopathic hospitals, holding identified patient records, prescriptions and case histories. This is a Data Fiduciary under the DPDP Act 2023, sensitive personal data under the SPDI Rules 2011, and an SDF candidate. It has a `SECURITY.md` and a carefully drafted proprietary EULA; what it lacks is the privacy notice, retention and erasure schedule, breach procedure, and processor list.

**case-kit**, **app-encrypted-case-log** — practitioner case records. Encryption at rest is a safeguard, not an exemption: the DPDP obligations attach to the data, not to the storage.

Needs: DPDP-grade privacy notice with all nine Rule 3 elements, retention and erasure schedule per record class, breach notification procedure, processor inventory, role-based access described plainly, and a `DISCLAIMER.md`.

### Tier 5 — health content and classical texts (publishing exposure)

app-organon-reader (Organon 6th ed., Boericke 1922 translation), repertory-reader (17 repertories, 271,421 rubrics), boericke-repertory, open-materia-medica, Repertorium-Publicum, UniRep, remedy-relationship-explorer, app-thermals, homoeopathic-materia-medica-repertory-json, MATERIA-MEDICA-BUILDER, drsamonline profile.

Needs Tier 1 plus: a `NOTICE` attributing every classical source by author, translator, edition, year and publisher; a public-domain basis statement; and a medical `DISCLAIMER.md` that says the app reproduces published reference material and does not diagnose, prescribe or treat.

**whispering-body-first-aid** and **gentle-pediatrics-companion** sit above this tier. First-aid guidance that a user may follow in an emergency, and anything concerning children's health, are the two places where a wrong output causes physical harm. Both need a lawyer's review, an explicit emergency-services instruction, and in-app placement of the warning — not a file in the repo.

## Cross-cutting gaps

1. **"Other" licences are invisible.** Add SPDX identifiers to `package.json`, `pyproject.toml`, `Cargo.toml`, and a plain-English one-liner at the top of each `LICENSE`.
2. **Attribution debt.** The public-domain medical corpus is the fleet's biggest unrecorded obligation. A single `NOTICE` per content repo settles it.
3. **No `TERMS.md` anywhere.** Fine for offline tools; not fine for ai-bridge, HMS, or anything sold.
4. **Inbound contribution terms.** Where `CONTRIBUTING.md` exists, check whether it states a DCO, CLA or inbound=outbound rule.
5. **Private repos.** Nine private repositories (forge, knowledge, dumps-4 and others) hold internal material; they still need a licence line and, if they contain customer or patient data, a retention rule.

## Suggested order of work

1. The six unlicensed repos — one commit each.
2. `PRIVACY.md` + `SECURITY.md` across Tier 1, from the kitbox model.
3. `NOTICE` + medical disclaimer across Tier 5.
4. HMS privacy notice, retention schedule and breach procedure.
5. `TERMS.md` for ai-bridge and HMS.
6. Lawyer review for Tier 4 and the two paediatric/first-aid repos.
