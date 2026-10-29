---
name: google-mobile-ads-validate
description: Validate a project's Google Mobile Ads (GMA) SDK integration either as a complete audit or for specific requested checks.
license: Apache-2.0
metadata:
  title: "google mobile ads validate"
  origin: "google/skills"
  upstream-path: "skills/ads/google-mobile-ads-validate/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# Validate Google Mobile Ads SDK Integration

Validate a project's Google Mobile Ads (GMA) SDK integration either as a
complete audit or for specific requested checks.

-   **Full Audit**: If the user requests a general validation or full audit,
    evaluate all checklist items.
-   **Specific Checks**: If the user asks to validate only a specific area
    (e.g., ad preloading), evaluate only the relevant check(s) without running
    the entire checklist.

## Scoring Rules

For each check, apply one of the following statuses:

-   **Pass**: None of the Warning, Fail, or N/A criteria are met.
-   **Warning**, **Fail**, or **N/A**: The conditions described under each
    respective status are met.

## Validation Checklist

Read the reference guide for each check to be performed:

-   No test application ID is in the project, format correct:
    `references/application-id.md`
-   No test ad units are in the project, format correct:
    `references/ad-units.md`
-   Implemented all Google SKAdNetwork IDs:
    `references/google-skadnetwork-ids.md`
-   Mediation adapter compatibility:
    `references/mediation-adapter-compatibility.md`
-   Ad preloading validation checks: `references/ad-preloading.md`

## Final Output

Generate a Markdown report following the format below. **ONLY** include the
findings for items that were actually checked.

| Check | Status | Findings | Next Steps |
| :--- | :---: | :--- | :--- |
| No test application ID is in the project, format correct | {{status_1}} | {{findings_1}} | {{next_steps_1}} |
| No test ad units are in the project, format correct | {{status_2}} | {{findings_2}} | {{next_steps_2}} |
| Implemented all Google SKAdNetwork IDs | {{status_3}} | {{findings_3}} | {{next_steps_3}} |
| Mediation adapter compatibility | {{status_4}} | {{findings_4}} | {{next_steps_4}} |
| Ad preloading validation checks | {{status_5}} | {{findings_5}} | {{next_steps_5}} |

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/ads/google-mobile-ads-validate/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
