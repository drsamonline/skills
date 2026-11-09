# Drafting standards — required elements, house style, review gates

## Document header

Every legal document opens with the same four lines. No exceptions, because a document without a date cannot be relied on.

```
Version: 1.0
Effective: 09 November 2026
Owner: <name>, <contact>
Changes: <one line, or "initial version">
```

## Required elements by document

### PRIVACY.md

- What is collected, per category, in plain words. "Nothing" is a valid and strong answer when true.
- Where it is stored (device, your server, a named provider) and for how long.
- Who it is shared with, by category, naming providers where a user would care.
- How to erase it — the exact control, not "contact us".
- What leaves the device, stated as a verifiable claim ("no network request is made; check your browser's network panel").
- Rights and grievance contact, if the DPDP Act applies.
- Children's data position if the product could be used by under-18s.
- Change process: what happens when the policy changes.

### TERMS.md

- What the service is and is not.
- Eligibility and account rules, if any.
- Acceptable use, listed concretely.
- Payment, refunds, cancellation if paid.
- IP: who owns what, and the licence the user gets.
- Disclaimers and liability limitation, by reference.
- Termination, governing law, forum, and a real contact.

### SECURITY.md

- Supported versions.
- Private reporting channel — an address or a private advisory, never "open a public issue".
- What to include in a report.
- Acknowledgement and fix timelines you can actually meet.
- Scope: what is in scope, and an explicit statement that testing must not damage others' data.

### DISCLAIMER.md

See `disclaimers.md`. Must be domain-specific: a health product's disclaimer is not a legal product's.

### NOTICE / THIRD-PARTY.md

One block per component, with licence, copyright holder, source and modifications. See `licensing.md`.

### CONTRIBUTING.md (legal section)

Inbound grant: DCO, CLA or inbound=outbound. Say which, and link it.

## House style

- Short sentences. One idea each. Active voice.
- Concrete over abstract: "writes to this browser's localStorage under the `tooly:` prefix" beats "may store certain information locally".
- Second person for obligations, first person for commitments.
- No defined-term maze. If a term needs defining, define it once inline.
- Tables for anything enumerable; prose for anything explanatory.
- Never "hereby", "hereinafter", "whereas", "notwithstanding". These signal a template, not a thought.
- Numbers as digits, dates as `09 November 2026`, money with the currency symbol and, where useful, lakh/crore.
- State the date a fact was checked when the fact can change.

## Facts must be checkable

Every factual sentence in a privacy or security document is a claim about the code at a commit. Before publishing, run the audit script and confirm each claim against its output. If the code later adds a network call, the policy changes in the same commit — and where possible a CI check enforces it.

## Review gates

| Gate | Question | Blocking? |
| --- | --- | --- |
| Facts | Is every claim about data flow verified against the code? | Yes |
| Citations | Does every statutory reference name the section/rule and the date checked? | Yes |
| Claims | Any superlative, compliance assertion or therapeutic claim left unqualified? | Yes |
| Completeness | Does the document set match the repo profile in `SKILL.md` Step 2? | Yes |
| Consistency | Do `LICENSE`, `NOTICE`, `TERMS.md` and the dependency list agree? | Yes |
| Plain language | Would a non-lawyer understand every obligation? | No, but fix it |
| Professional review | Required for patient health data, commercial sale, therapeutic claims, or accounts on a public service | Escalate |

## What never goes in a published document

- A section number you have not read in the official text.
- A case citation you cannot open.
- A penalty figure that is not in the Schedule or the section.
- A promise of certification, registration or government approval.
- A retention period the code does not implement.
- A statement that a named third party "does not retain data" without their current terms in hand.
- Any claim of being a lawyer or giving legal advice.
