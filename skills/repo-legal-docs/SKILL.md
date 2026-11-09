---
name: repo-legal-docs
description: Write and audit the legal documentation a repository needs — LICENSE and third-party notices, PRIVACY policy, TERMS of use, medical and AI disclaimers, SECURITY policy, EULA — grounded in Indian law (Copyright Act 1957, IT Act 2000 with IT Rules 2021, DPDP Act 2023 with DPDP Rules 2025, Consumer Protection Act 2019, Drugs and Magic Remedies Act 1954). Use for "legal docs for my repo", "what licence should I use", "write a privacy policy", "terms of service", "DPDP compliance", "add a disclaimer", "attribution for public-domain sources", "NOTICE file", "EULA", or a compliance audit across a whole repository fleet.
metadata:
  title: "Repo legal docs — the paperwork a repository owes its users"
---

# Repo legal docs

A repository's legal surface is a small, fixed set of files. Most repositories have one of them and need five. This skill produces the set, sized to what the code actually does, in the owner's own voice, with every statutory reference traceable to an official source.

It produces review-ready drafts and a list of what a qualified Indian advocate must settle before publication. It is not legal advice and never presents itself as such.

## When to use

- A repo is about to be published, sold, or handed to a clinic, and nobody has written the privacy policy, terms or disclaimer.
- A licence question comes up: which one, what SPDX id, why GitHub says "Other", whether a relicence is valid.
- A health, homeopathic, AI or consumer-facing product makes a claim that needs bounding.
- An audit is wanted across a whole account rather than one repo.
- A public-domain text, font, dataset or dependency is bundled and the attribution has not been written down.

## Method

### 1. Classify the repository — before writing a word

Five axes decide the document set. Answer them from the code, not the README.

1. **Distribution** — source only, binary, hosted service, browser extension, mobile app, or a single HTML file.
2. **Data touch** — none / on-device only / to your server / to a third party (AI provider, payment, analytics).
3. **Data sensitivity** — ordinary, or health, biometric, financial, children's.
4. **Domain claim** — does it assert medical, legal, financial or safety authority, or emit AI output someone might act on.
5. **Commerciality** — free, donation-supported, paid, or a paid service with free clients.

### 2. Audit before drafting

Facts, not impressions:

```bash
python3 scripts/audit_legal_docs.py --path /path/to/repo
python3 scripts/audit_legal_docs.py --gh-user <login> --json audit.json
```

It reports which legal files exist, guesses the licence family, and flags network calls, analytics, on-device storage, health fields, AI providers, payments and auth. Those flags drive step 3. Never write "we collect nothing" without the network-call result in hand.

### 3. Pick the document set

| Repo profile | Documents |
| --- | --- |
| Offline tool, nothing leaves the device | `LICENSE`, `SECURITY.md`, short factual `PRIVACY.md`, `NOTICE` if third-party content is bundled |
| Offline app storing user content on device | above, plus "what is stored, where, how to erase it" |
| Calls a third-party API (AI, maps, sync) | above, plus data-flow disclosure naming the recipient category, plus `TERMS.md` |
| Hosted service or accounts | `PRIVACY.md` with the DPDP notice elements, `TERMS.md`, `SECURITY.md`, grievance contact |
| Holds health records | all of the above, plus a DPDP-grade notice, retention and erasure schedule, breach procedure, `DISCLAIMER.md` |
| Health, remedy or clinical content | all of the above, plus the medical disclaimer and source attribution for every quoted classical text |
| AI feature in a shipped product | AI-output disclaimer, synthetic-content labelling, provider data-flow disclosure |

Draft from `assets/templates/`. Fill every placeholder; delete every section that does not apply. A shorter true document beats a longer template.

### 4. Draft under four rules

- **Official sources only.** India Code, eGazette, the regulator's own site, the court's own site. Never a blog, a firm's summary or an AI answer as authority.
- **Cite section and rule numbers, with the date checked.** "DPDP Act 2023, s.8(6); DPDP Rules 2025, r.6; checked 09 Nov 2026." "As per Indian law" is not a citation.
- **Never invent a section, case, form or penalty figure.** If it cannot be verified, write the obligation plainly and flag it.
- **Describe the code as shipped.** Every factual sentence in a privacy or security document is a claim about a commit. If the code changes, the document changes in the same commit.

### 5. Close the loop

For each document, report the facts it asserts, the evidence for each, the statutory basis, and the open questions for a lawyer. Where an answer depends on an unverified fact — does the SDK phone home, does the provider retain prompts — say so rather than assuming.

Escalate where the repo holds identified patients' health data, is sold commercially, publishes therapeutic claims, or runs a public service with accounts.

## Key files

- `references/indian-law-map.md` — the statutes that bite a software repo, with official links.
- `references/dpdp-2023.md` — DPDP Act and Rules: notice elements, security, breach, children, health data, the 13 May 2027 timeline.
- `references/licensing.md` — licence choice, SPDX, PolyForm, EULA structure, attribution, public-domain texts.
- `references/disclaimers.md` — medical, homeopathic, AI and consumer-claim wording.
- `references/drafting-standards.md` — required elements per document, house style, review gates.
- `references/sources.md` — official source registry, and what never to cite.
- `references/repo-inventory.md` — the drsamonline fleet triaged into six tiers, with what each repo needs.
- `assets/templates/` — PRIVACY, TERMS, SECURITY, DISCLAIMER-medical, NOTICE, EULA, CONTRIBUTING, LEGAL-INDEX.
- `scripts/audit_legal_docs.py` — the scanner, dependency-free, read-only.

## Gotchas

- **GitHub reports PolyForm and bespoke EULAs as "Other".** So does every dependency scanner downstream, which blocks adoption in corporate and government settings. One plain-English line at the top of `LICENSE` plus an SPDX identifier in the manifest fixes the impression; the licence itself is fine.
- **A disclaimer in a file nobody opens discharges nothing.** It belongs in-app, on first run, in the README above the fold, and on any screen that shows a remedy, a dose or a prescription-like output.
- **"DPDP compliant" is a conclusion, not a sentence.** State the behaviour; let counsel conclude. The same applies to "GDPR compliant", "100% secure" and "clinically proven".
- **Relicensing needs a supersession clause.** Name the earlier grant, the effective date, and the fact that copies made under it stay under it. Without that, an MIT-to-EULA switch is a dispute waiting.
- **Public domain needs a death date, not a publication date.** Life plus 60 under s.22 of the Copyright Act. And a 1922 text copied from a 2019 website may carry that site's transcription rights.
- **A retention period the code does not implement is a false statement**, not an aspiration.
- **Health data is sensitive personal data under the SPDI Rules 2011 as well as personal data under the DPDP Act.** Encryption at rest is a safeguard, not an exemption.

## Source projects

Distilled from the public Indian-law corpora, not from a drsamonline repo: `mihirkavi/indian-law-official-sources` (official-source registry and evidence discipline), `rohasnagpal/legal-ai-skills` (India jurisdiction rules), `lawve-ai/awesome-legal-skills` (the DPDPA reference), `sheevu/indian-law-training-dataset-2026`, `civictech-India/Indian-Law-Penal-Code-Json`, `raivivek/open-bns`, `shashionline/indian-law-plugin`, `judicialmind/legal-skills`.

Applied to the drsamonline fleet in `references/repo-inventory.md`; the audit that produced it is in the `knowledge` repo.
