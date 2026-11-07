# The four analyses

Each analysis has a test that separates a real relationship from a coincidence. Apply the test; if a
candidate fails it, drop it. A short list of true claims is worth more than a long list of plausible
ones.

---

## Analysis 1 — Improvement pairs

> **Question:** which app should take an existing capability from which other app?
> **Test:** the receiving app has a *visible gap* that the donor already fills, and the gap is
> user-facing rather than aesthetic.

This is the cheapest gain available, because nothing new has to be designed. The capability exists, is
tested, and has a home. Your job is to notice the pairing.

**What makes a good pair:**

- The donor's capability is *load-bearing* in the donor — it is not a side feature. A crypto
  implementation that protects real secrets is a better donor than a demo.
- The receiving app has a gap that its own README apologises for, or that its roadmap names, or that
  a user would hit in the first ten minutes.
- The transfer does not require the receiver to adopt the donor's whole architecture. A library, a
  module or a data format transfers cleanly; a framework does not.
- The direction is not always the obvious one. The app with the *worse* product can have the *better*
  implementation of one component, and that is exactly the transfer worth making.

**How to find them.** For each cluster from step 7, list every member. For each member, ask: does it
implement this capability, and how well? The best implementation is the donor; every other member is a
receiver. Then ask the harder question — is there a member that *needs* the capability and does not
have it at all? Those pairs are usually worth more than the "upgrade the worse copy" pairs, because
they create a new ability rather than a better one.

**What to write per pair:** donor, receiver, the specific thing that moves (name the function, the
format, the algorithm — not "the crypto"), why it matters to a user, and an effort estimate. Effort
means the work to bring it across and prove it, not to design it.

**The trap:** recommending that everything be centralised. Sometimes the duplication is correct — two
apps with genuinely different constraints should have two implementations. Say so when it is true, and
explain what makes them different.

---

## Analysis 2 — Suites

> **Question:** which apps belong together without merging?
> **Test:** would one user, on one day, want all of it in one place?

A suite is not a merger. The apps stay separate; they gain a shared identity, a shared spine and one
way in. The distinguishing feature of a suite is that its members share a *model* — a patient, a book, a
document, a tool — not merely a technology.

**What a suite needs to be real:**

1. **A shared spine.** One data model, one identifier scheme, one export format, or one runtime. Without
   this it is a category, not a suite.
2. **A shared front door.** One page, one installer, one bookshelf, one catalogue. If the user has to
   know six repo names, it is not a suite.
3. **A single day's use.** The test above. A clinic suite passes because a practitioner registers,
   takes a case, prescribes and bills in one morning.
4. **A reason the members stay separate.** If they should merge, that is Analysis 3.

**Naming the spine is the work.** "They all use the same kit" is not a spine — it is a technology
choice. "They all address the same patient record" is a spine. When you propose a suite, state the
spine in one sentence, and state which repository currently owns it or whether it must be created.

**Ordering suites.** Rank by value ÷ risk. The best suite to build first usually has: the highest-value
content, the lowest integration risk (everything already offline and self-contained), and a spine that
can be frozen quickly. The suite with the biggest commercial case often has a server in it, and the
server is the risk — do that one second, using the model the first one forced you to settle.

**The trap:** grouping by technology instead of by user. "All the single-file HTML apps" is a
deployment property, not a suite. Nine games on one engine is a refactor, not a product.

---

## Analysis 3 — Merges

> **Question:** which two or more apps should become one better thing?
> **Test:** does the combined product answer a question neither could answer alone?

A suite shares a spine. A merge creates a new subject. The test is deliberately strict: if the combined
product merely does both things side by side, it is a bundle, not a merge.

**What makes a merge real:**

- **A new question becomes answerable.** "Who says this remedy relates to that one, in what words, and
  does anyone disagree?" needs a provenance model plus a relationship graph plus a differential list.
  No one of the three can answer it.
- **A workflow completes.** Capture → dedupe → strip → attach → compare is a workflow; any two of those
  steps is a feature.
- **A constraint becomes satisfiable.** Two halves that each fail a requirement alone (a record that
  is portable but unencrypted, and an encryption tool with no records) satisfy it together.

**What to write per merge:** the new name, the components, the product in two sentences, why the merge
is *necessary* rather than convenient, and which files or modules carry each half. That last item is
what turns a proposal into a plan.

**The trap:** merging because the pieces are adjacent in the file tree. Proximity is not synergy. Also
beware the merge that creates a product with two unclear owners of one data model — that is a suite
with extra steps.

---

## Analysis 4 — New products

> **Question:** what does this collection make unusually cheap to build?
> **Test:** is the expensive component already written, tested and proven?

A fleet's most valuable property is not what it ships but what it makes *cheap*. When the corpus, the
cryptography, the packaging pipeline, the search index and the offline runtime all exist, a new product
built from them costs a fraction of what it would cost from scratch — and that is the argument that
justifies building it.

**How to find them.** List the components that are expensive to build and already done: a licensed
corpus, a correct cryptographic implementation, a cross-platform packaging pipeline, a proven scoring
engine, a search index over a large body of text, a physical-machine emulator with a parity proof. Then
ask what user-facing product those components unlock that does not exist.

**Specify each idea properly.** A one-line idea is worthless in an audit. Each specification needs:

- **The gap** — the user and the situation, in two sentences.
- **The parts** — which existing repositories supply which component.
- **What it does** — the product, concretely, in the user's words.
- **The data model** — the entities and their relationships. This is the part that reveals whether the
  idea is real.
- **The constraints it must respect** — the estate's own house rules (offline, no accounts, no
  telemetry, single-file where possible, printable, licence separation). Naming these is what makes
  the idea buildable by *this* author rather than by anyone.
- **Effort** — an honest estimate for one experienced developer with AI assistance.
- **The principal risk** — one risk, the real one, not a list.

**Rank them.** The best ideas in a fleet audit usually have three properties: the hard part is already
built, the buyer is obvious, and the product can ship without a server.

**The trap:** inventing products the collection does not actually support. If the expensive component is
not already written, you are writing a startup idea, not an audit finding. Say which it is.

---

## Ranking and presenting

Whatever the analysis, end with an ordering and a "do nothing here" list. A reader who is given forty
recommendations will do none of them.

A useful ordering rule:

1. **Free and compounding** — make the record honest, freeze the shared model, fix the distribution.
   These cost days and make everything after them cheaper.
2. **High value, low risk** — the suite whose components are all offline and self-contained.
3. **High value, real risk** — the one with a server or clinical responsibility. Do it second, with the
   model the previous phase forced you to settle.
4. **Cheap and satisfying** — the small merges and packs. Schedule them for a week when you need
   something that finishes.
5. **Deliberately last** — the big refactor of finished work. Name it and set it aside explicitly,
   because otherwise it will sit in the backlog looking urgent.

---

## Recording the decisions

The four analyses end as data, not only as prose. Write `decisions.json` — schema in
`decisions-schema.json` — one object per recommendation: which analysis it came from, its name, the
repositories involved, what moves, why it matters, the effort, the principal risk, and its rank in the
value ÷ effort ordering.

The report argues from that file, the workbook's Decisions sheet lists it, and a re-run of the audit
diffs against it. A recommendation that cannot be written as one of those objects is not yet a finding —
it is a feeling about the code.
