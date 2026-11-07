---
name: sox-audit-support
description: "Support SOX 404 compliance: control testing methodology, scoping, sample selection, testing workpapers, evidence standards, and deficiency classification. Use when preparing or reviewing internal-control testing, selecting audit samples, documenting control effectiveness, or classifying a deficiency as a deficiency, significant deficiency or material weakness."
license: "per source — see references/*/LICENSE"
metadata:
  title: "SOX 404 audit support"
  category: "security-audit"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "audit-support"
---

# SOX 404 audit support

A compliance method, not legal advice. Its value is that every conclusion is traceable: the account is in scope for a stated reason, the sample was selected by a stated method, the evidence covers the whole period of reliance, and the deficiency classification follows the stated criteria rather than impression.

## When to use

- A control must be tested for design or operating effectiveness.
- Samples must be selected and justified for a control test.
- A testing workpaper must be produced or reviewed.
- A control deficiency must be classified and aggregated.

## Method

1. Scope first: identify significant accounts and disclosures, then the relevant assertions for each account type, then the controls that address them. An account in scope without a stated reason is unauditable.
2. Separate design effectiveness (is the control capable of preventing or detecting the misstatement) from operating effectiveness (did it actually operate across the period).
3. Choose the sample method deliberately — random, targeted, haphazard or systematic — and state why; avoid unconscious bias (top of the list, round numbers, the same vendor every time).
4. Size the sample against the control's frequency and the reliance intended, and cover the full period of reliance.
5. Test with evidence that stands alone: documents, system reports, three-way matches. Verbal confirmation alone must be corroborated.
6. Document in the workpaper: control description, risk addressed, population, sample, method, evidence obtained, exceptions, conclusion, tester and date.
7. Classify each exception against the criteria, then aggregate deficiencies that affect the same account or assertion before concluding — individually minor issues can combine into a material weakness.
8. Write remediation with an owner, an action and a date, and state whether compensating controls exist.
9. State plainly that this supports the audit process and is not legal or attestation advice; a qualified auditor signs the conclusion.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`audit-support`](references/audit-support/) | The SOX 404 testing methodology: scoping, sampling, workpaper standards, evidence rules, deficiency classification and remediation. |

## Key files / entry points

- `references/audit-support/` — scoping, assertions by account type, design vs operating effectiveness, sampling approaches and sizes, workpaper and evidence standards, deficiency classification and remediation.

## Gotchas

- A sample that misses part of the period cannot support reliance.
- Evidence that is a screenshot of a screenshot is not evidence of operation.
- Aggregation is where individually minor deficiencies become material.
- A control that operated but was not designed to catch the risk is a design deficiency, whatever the test result.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `audit-support` — no licence file shipped with the source
