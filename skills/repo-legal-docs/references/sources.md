# Official source registry

Policy: **official only**. A document cites the publisher's own instrument, or it cites nothing. Discovery tools are for finding the document, never for proving what it says.

Registry assembled from the source registry in `mihirkavi/indian-law-official-sources` (policy `official_only`, reviewed 2026-10-10) and the India authoritative-sources guide in `rohasnagpal/legal-ai-skills` (reviewed 24 September 2026). Re-check each before relying on it.

## Primary legislation and gazette

| Source | Publisher | Use | URL |
| --- | --- | --- | --- |
| India Code | Legislative Department | Central Acts, subordinate legislation, consolidated text | <https://indiacode.gov.in/> |
| eGazette of India | Department of Publication | Notifications, commencement, amendments, rules | <https://egazette.gov.in/> |

`indiacode.nic.in` redirects to `indiacode.gov.in`; treat the old host as legacy.

## Courts

| Source | Use | URL |
| --- | --- | --- |
| Supreme Court of India | Judgments, orders, rules, case information | <https://www.sci.gov.in/> |
| Supreme Court Reports search | Reported authorities by citation, case, statute | <https://scr.sci.gov.in/scrsearch/> |
| eCourts Services | Case status and orders for participating courts | <https://services.ecourts.gov.in/> |
| The relevant High Court's own site | Territorial and subject-matter jurisdiction | varies |

## Regulators and ministries

| Body | Covers | URL |
| --- | --- | --- |
| MeitY | IT Act rules, IT Rules 2021, DPDP administration | <https://www.meity.gov.in/> |
| Ministry of Corporate Affairs | Companies Act, LLP, registered-office disclosures | <https://www.mca.gov.in/> |
| Department of Consumer Affairs | Consumer Protection Act, e-commerce rules, misleading ads | <https://consumeraffairs.nic.in/> |
| Central Drugs Standard Control Organisation | Drugs and Cosmetics Act and Rules | <https://cdsco.gov.in/> |
| National Commission for Homoeopathy | Homoeopathy education and practice regulation | <https://nch.org.in/> |
| Reserve Bank of India | Payments, if the product takes money | <https://www.rbi.org.in/> |

## Discovery, never authority

**Indian Kanoon** (<https://indiankanoon.org/>) is useful for full-text search and for locating a judgment. It is a private database: cite it to find the case, then cite the court's own copy. The same applies to commercial databases, court-data aggregators, law-firm blogs and AI answers.

Explicitly excluded as authority by the registry above: Indian Kanoon as a substitute for the judgment, private court-data APIs, and blogs. Search snippets are leads.

## Verification record

When you cite, record: instrument, provision, version in force on the relevant date, the exact URL used, and the date checked. A failed search is not evidence that a provision does not exist.

## Open corpora used to build this skill

These are secondary and were used for structure and cross-checking, not as the authority:

- `mihirkavi/indian-law-official-sources` — official-source registry, retrieval discipline, evidence-ledger pattern.
- `rohasnagpal/legal-ai-skills` — India jurisdiction operating rules, authoritative-source ordering, 232 practice skills.
- `lawve-ai/awesome-legal-skills` — the `dpdpa` skill (Act and Rules reference, last verified 2026-07-03).
- `sheevu/indian-law-training-dataset-2026` — statute and judgment corpora, reasoning structure.
- `civictech-India/Indian-Law-Penal-Code-Json`, `raivivek/open-bns` — structured statute text for section lookup.
- `judicialmind/legal-skills`, `shashionline/indian-law-plugin` — skill packaging patterns.
- `jeannesulzer/international-criminal-tribunals-skills` — irrelevant to Indian repo work; excluded.
