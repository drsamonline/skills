# Indian law that actually applies to a software repository

Last reviewed: 09 November 2026. Every entry below names the instrument and its official home. Verify the current text and the version in force on the relevant date before relying on it.

Read this as a map of exposure, not a list of citations to sprinkle into a document. A repo typically engages three or four of these and none of the rest.

## 1. Copyright — the licence layer

**Copyright Act, 1957** (as amended, including by the Finance Act 2018 and the Copyright (Amendment) Rules 2021). Official text: India Code, <https://www.indiacode.gov.in/>.

- Computer programs are protected as literary works. The owner's exclusive rights, including the right to issue copies and to make adaptations, sit in s.14.
- Term: life of the author plus 60 years (s.22). This is why a "public domain" claim needs a death date, not a publication date.
- Moral rights (s.57) survive assignment — attribution and integrity cannot be licensed away. Any NOTICE file is partly a moral-rights artefact.
- No registration is required for protection to subsist; registration is evidentiary only. A missing © line does not mean a work is free to use.
- Consequence for a repo: the `LICENSE` file is the entire grant. Silence grants nothing. A custom "Other" licence that reads as a EULA grants nothing beyond its own words.

## 2. Information technology — the platform layer

**Information Technology Act, 2000** (as amended). Official text: India Code; rules and notifications via MeitY, <https://www.meity.gov.in/>.

- **s.43A** and the **Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011** ("SPDI Rules") still govern sensitive personal data until the DPDP regime fully displaces them. Rule 3 defines sensitive personal data or information to include **physical, physiological and mental health condition**, medical records and history, biometric information, financial information, and sexual orientation. A hospital or clinic system is squarely inside this definition.
- **s.79** gives intermediaries conditional safe harbour, lost if the intermediary fails due diligence or does not act on actual knowledge. Relevant only if the product hosts or transmits third-party content.
- **IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021** set the due-diligence conditions: published terms and privacy policy, a grievance officer resident in India, acknowledgement in 24 hours and resolution in 15 days, monthly compliance reporting, and takedown on a court order or government direction. A user-generated-content surface triggers these; a static offline tool does not.

## 3. Personal data — the DPDP layer

**Digital Personal Data Protection Act, 2023** (assent 11 August 2023) and the **Digital Personal Data Protection Rules, 2025** (notified 13 November 2025). Full substantive compliance timeline per the Rules: 13 May 2027. Detail in `dpdp-2023.md`.

Applies to digital personal data processed in India, and to processing outside India that relates to offering goods or services to individuals in India. Applies to a hospital system, an app with accounts, and any product that stores notes, photos, voice clips or health entries that identify a person — even on-device storage counts as processing.

Does not apply to data that is never digitised, to data made publicly available by the Data Principal themselves, or to the exempted categories in s.17.

## 4. Consumer-facing claims — the advertising layer

**Consumer Protection Act, 2019**, with the Consumer Protection (E-Commerce) Rules, 2020. Official text: Department of Consumer Affairs, <https://consumeraffairs.nic.in/>.

- A misleading advertisement includes one that falsely describes a product's usefulness, or conceals material information. Penalties for a manufacturer or endorser run to lakhs, with repeat-offence exposure in crores.
- Applies to a paid product, a paid app, or any claim in a store listing or README that a buyer could rely on — "compresses better than X", "clinically validated", "100% secure".

## 5. Health and homeopathic claims — the exposure most software teams miss

- **Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954** and Rules, 1955. Prohibits advertisements of remedies claiming to cure or treat the diseases listed in the Schedule, and any "magic remedy" claim. A remedy app that advertises therapeutic effect, not merely reproduces a classical text, engages this.
- **Drugs and Cosmetics Act, 1940** and Rules, 1945 — labelling and advertising of drugs, including homoeopathic medicines.
- **National Commission for Homoeopathy Act, 2020** and the Commission's professional-conduct and advertising expectations; the earlier Homoeopathy Central Council Act, 1973 framework it replaced. Official: <https://nch.org.in/>.
- Consequence: a repertory or materia medica reader is a *publishing* product and needs source attribution and a "reference only, not medical advice" statement. A symptom-checker that recommends a remedy is an *advertising and practice* product and needs a lawyer before it ships.

## 6. Commercial and corporate — only if you sell

**Companies Act, 2013** (Ministry of Corporate Affairs, <https://www.mca.gov.in/>) once the repo sits inside a company: registered name and address on the site, and the disclosures in the legal-notice footer. **Trade Marks Act, 1999** for the product name and logo — a name used in commerce without registration is still exposed to a passing-off claim.

## 7. Criminal-law vocabulary, for accuracy only

The **Bharatiya Nyaya Sanhita, 2023** replaced the Indian Penal Code; the **Bharatiya Nagarik Suraksha Sanhita, 2023** replaced the Code of Criminal Procedure; the **Bharatiya Sakshya Adhiniyam, 2023** replaced the Indian Evidence Act. Defamation is now BNS s.356. Cite the new instruments and the new section numbers, or cite both with the transition noted. Do not carry IPC numbers into a 2026 document without saying they are superseded.

## 8. What almost never applies

Patent law, competition law, securities law, FEMA, and the labour codes do not belong in a repository's legal file. If a document starts citing them, it is padding.

## Source discipline

Every proposition in a published document needs a pinpoint. Use `sources.md` for the registry of official publishers, and record the date you checked. A government homepage is not authority for a section number; the section text is.
