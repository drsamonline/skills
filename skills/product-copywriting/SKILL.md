---
name: product-copywriting
description: Write honest product copy for a landing page, a README or a store listing — a headline, a value line, a CTA — that reads like a person wrote it and a competitor could not. Use when writing or fixing copy for an app page, a store entry or a README, or when a draft "sounds like AI".
metadata:
  title: "Product copywriting"
---

# Product copywriting

Copy that says what the thing does, in the reader's words, and claims nothing it cannot prove. The house stance is anti-hype: a product page is a description, not a pitch, and a claim that cannot be proven is decoration.

## When to use

- Writing or fixing the headline, value line, feature list or CTA of a landing page or a store entry.
- A README's opening paragraph must explain an app to someone who has never seen it.
- A draft "sounds like AI" — the reveal, the triplet list, the trailing clause.

## Method

1. **Diagnose first, and say which.** (a) A blank brief or generic company-speak — build the argument from facts, with latitude on angle but never on facts; (b) a real draft with a point of view — keep its argument and vocabulary, fix only the buried lead, the vague line and the AI tells; (c) a point edit — change only what was asked. Most bad copy comes from over-writing a draft that was already good.
2. **Lead with the reader's problem, not the feature.** "Itching worse at night" is the symptom; "symptom severity tracking" is the feature. Name the symptom.
3. **Run every line through the three-question gate.** Can the reader picture it? Can it be proven true or false? Could a competitor write this exact sentence? A line that fails the third is cut.
4. **Be specific.** "551 portable Windows tools in one .exe" beats "a powerful toolkit" — numbers, names and real limits.
5. **One idea per section.** If a paragraph needs an "and", it is two paragraphs.
6. **Claims must be supportable.** If you cannot point to the file, test or number behind a claim, do not make it — write the smaller true claim instead.
7. **Cut the AI tells.** No "it's not X, it's Y" reveal; no "no X, no Y, no Z" triplet; no sentence trailing into a clause that restates itself; no "in today's fast-paced world". Read it aloud — if it sounds like a brochure, rewrite it.
8. **The CTA says what happens.** "Open the app", "Download for Windows", "Read the source" — not "Get started" or "Learn more".

## Key files / entry points

- `docs/index.html` — the landing-page copy (hero, features, FAQ).
- `README.md` — the repository's opening paragraph and feature list.
- `docs/data/products.json` — the store entry (name, one-line description, long description).

## Gotchas

- **Never invent a price, a buy link, a rating or a customer.** Buy links come from the owner; claims about buyers we do not have are forbidden.
- The house voice is plain and specific, in Indian English where it fits ("centre", "₹") — not US marketing register.
- A landing page already carries a good SEO head (see `static-landing-page-seo`); the copy sits inside it, so do not rewrite the head.
- If a line feels strong, it is usually the one that most needs its proof.

## Source projects

- [open-materia-medica](https://github.com/drsamonline/open-materia-medica), [neon-runner](https://github.com/drsamonline/neon-runner), [Matneo](https://github.com/drsamonline/Matneo) — the copy these rules were read back from.

*Adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), rewritten for this system.*
