---
name: public-domain-library
description: Run a public-domain library where every title is cleared for both India and the United States, each record says on what basis, one book is one card across PDF/EPUB/text, and the storage is split across repositories because Pages caps a site at 1 GB.
metadata:
  title: "Corpus Extendum"
---

# Corpus Extendum — the public domain, properly shelved

A free library of out-of-copyright books: 79 titles, 12 categories, one shelf that grows by itself.
Read in the page as PDF, EPUB or plain text; download anything; keep it forever. The claim is not
generosity — the copyright has expired — and the app is built to make that claim auditable.

## When to use

- A corpus has to be shipped with a **licence claim per item**, not one blanket statement.
- The same work exists in several formats and must not appear three times.
- The content outgrows the hosting: Pages caps a site at 1 GB, so the books need somewhere else to live.

## Method

1. Gate every title on the **stricter of the two jurisdictions** it must be legal in (here India and the United States), and store *why* on the record — the basis, not just a boolean.
2. Dedupe before fetching: one title that exists as PDF, EPUB and text is one card with format chips. A second copy is refused at ingest, not merged later.
3. Keep reading position per book in the browser only; the shelf opens on *Continue reading* because that is the only state worth remembering.
4. Split storage from the site: the app repository holds code and records, and a **vault repository** holds the bytes (`corpus-extendum-vault-01`, ten books, PDF + EPUB + text + records, built to reach 2.5 GB). The app links out; it does not inline.
5. Open every format in the page — PDF, EPUB, text — with no plugin and no new tab.

## Key files / entry points

- `corpus-extendum` — the shelf, the records and the reader.
- `corpus-extendum-vault-01` — the book storage repository, deliberately not a website.
- `docs/assets/shelf.png` — the shelf view.

## Gotchas

- **A public-domain claim is per country.** A title free in the US may still be in copyright in India; the stricter test is the gate, and the record has to say which one applied.
- The vault is a repository, not a Pages site, *on purpose*: publishing it as a site hits the 1 GB cap and the failure looks like a broken library rather than a hosting limit.
- Format chips on one card are a data model decision — three entries that look identical to a reader are a search result nobody trusts.

## Source projects

- [corpus-extendum](https://github.com/drsamonline/corpus-extendum)
- [corpus-extendum-vault-01](https://github.com/drsamonline/corpus-extendum-vault-01)
