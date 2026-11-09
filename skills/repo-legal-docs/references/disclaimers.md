# Disclaimers: health, homeopathy, AI and consumer claims

A disclaimer is not a magic phrase that removes liability. It is an accurate statement of what the software does not do, placed where a user will actually read it. An inaccurate disclaimer is worse than none: it is evidence you knew the risk existed.

## 1. Medical and health disclaimers

### What the statement must establish

1. The software is **not** a medical device, and not a substitute for examination by a registered practitioner.
2. The content is **reference material** — a reproduction or organisation of published sources — not diagnosis, prescription or treatment.
3. No doctor–patient relationship arises from use.
4. Emergencies require emergency services, named for the jurisdiction (in India, 108 or the local emergency number).
5. Who is responsible for clinical decisions: the treating practitioner, always.

### What it must not do

- Claim a therapeutic benefit ("helps you find the right remedy") — that converts a reference tool into an advertising claim under the Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954.
- Name diseases it "treats" or "cures". The Schedule to that Act lists conditions that may not be advertised as curable at all.
- Disclaim liability for negligence. A blanket "no liability whatsoever" is unenforceable in India and signals bad faith; limit liability to a stated amount instead.

### Homeopathic content specifically

Reproducing a repertory, materia medica or provings is publishing. The obligations are accuracy, attribution and non-endorsement: quote the source, name the edition and translator, and state that a remedy suggested by a repertory is a hypothesis for a practitioner to test, not a prescription. Symptom-checker features that output a remedy sit on the far side of that line and need a lawyer's sign-off before release.

### Where the disclaimer lives

Not only in `DISCLAIMER.md`. In-app, on first run, in the README above the fold, and on any screen that displays a remedy, potency or prescription-like output. A file nobody opens does not discharge the duty to warn.

## 2. AI-generated output

Where the product calls a model, or ships one:

- State that output is machine-generated, may be wrong, and must be verified before reliance — with a specific example of the failure mode (a fabricated citation, a wrong dose, a stale date).
- State which provider receives the prompt, what is sent, and whether it is retained for training, per the provider's own terms. That disclosure is a DPDP notice element, not a nicety.
- Do not present generated text as professional advice. For a legal or medical product this is the single highest-risk sentence in the repository.
- Label synthetic media where the product creates images, audio or video — MeitY's advisory framework expects identifiable synthetic content, and the IT Rules 2021 due-diligence duties apply to a platform that hosts it.
- Never put a model's output behind a claim of accuracy, certification or clinical validation you cannot document.

## 3. Consumer-facing claims

Every superlative in a README, store listing or landing page is a representation:

| Claim | Risk |
| --- | --- |
| "100% secure", "unhackable", "military-grade encryption" | Misleading advertisement; also invites a security researcher's rebuttal |
| "Faster than <named competitor>" | Must be measured, dated and reproducible, or it is denigration |
| "Clinically proven", "doctor-recommended" | Requires the study and the endorsement, in writing |
| "GDPR/DPDP compliant" | A legal conclusion; state the behaviour instead |
| "Free" with a paid tier | Must disclose the tier in the same breath |

Under the Consumer Protection Act, 2019 a misleading advertisement includes one that conceals material information — so a README that omits that data is uploaded to a third party is itself the problem.

## 4. Liability limitation that survives scrutiny

A workable structure for an Indian-facing product:

1. Software provided "as is", without warranties of merchantability, fitness for a particular purpose or non-infringement, to the extent permitted by law.
2. No warranty that operation will be uninterrupted or error-free.
3. Limitation of aggregate liability to the amount the user paid in the preceding twelve months, or a stated figure for free software.
4. Carve-outs that cannot be excluded by law — death or personal injury caused by negligence, fraud, and any liability that Indian law does not permit to be limited. Saying so explicitly is what makes the rest of the clause credible.
5. Indemnity only where the user's misuse caused the loss.

## 5. The honesty test

Before publishing any disclaimer, answer: if a user relied on this software and was harmed, would this document be an honest account of what the software was for? If not, the problem is the claim, not the wording.
