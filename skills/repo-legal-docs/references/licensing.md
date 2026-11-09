# Licensing, attribution and public-domain content

## 1. Choose the licence by intent, not by fashion

| You want | Use | SPDX | Note |
| --- | --- | --- | --- |
| Anyone may use it, keep the notice | MIT | `MIT` | Shortest, most compatible, no patent grant |
| Anyone may use it, with an express patent grant | Apache-2.0 | `Apache-2.0` | Requires NOTICE propagation and states changes |
| Copyleft on distributed derivatives | GPL-3.0 | `GPL-3.0-only` | Derivative distributed binaries must ship source |
| Copyleft even over a network | AGPL-3.0 | `AGPL-3.0-only` | Hosted use counts as distribution; kills most commercial adoption |
| Free for personal use, paid for business | PolyForm Noncommercial 1.0.0 | `PolyForm-Noncommercial-1.0.0` | **Not OSI-approved.** GitHub reports it as "Other" |
| Free to use, you keep all other rights | A bespoke EULA | `LicenseRef-Proprietary` | Must be drafted, not templated |
| Public domain dedication | CC0-1.0 or Unlicense | `CC0-1.0` | CC0 is not recommended for patents; fine for docs and data |

Two rules that prevent most licence defects:

- **One grant, one file.** `LICENSE` at the repository root. Do not stack MIT and a bespoke EULA in the same repo without an explicit supersession clause naming the earlier grant, the effective date, and the fact that copies made under the earlier grant stay under it.
- **SPDX in the header.** A `SPDX-License-Identifier:` line in each source file makes the licence machine-readable. For a non-standard licence use `LicenseRef-<name>` and define it in `LICENSES/`.

## 2. The "Other" problem in this fleet

GitHub's licence detector reports a repository as **Other** when the file is PolyForm, a bespoke EULA, or any text it does not recognise. That has three consequences worth stating in the repo:

- Automated dependency scanners treat it as unknown, which blocks downstream adoption in corporate and government settings.
- The repository looks unlicensed to a casual reader even when it is carefully licensed.
- Nothing is inferred by silence: an unlicensed repository is all-rights-reserved, so the file must exist.

Mitigation, in order of preference: add an SPDX identifier in `package.json` / `pyproject.toml` / `Cargo.toml`; add a one-line plain-English summary at the top of `LICENSE` ("Free for personal and non-commercial use. Commercial use requires a written licence."); add a `LICENSES/` directory and a `NOTICE` describing the grant.

## 3. Proprietary EULA — what it must contain

For a closed-source binary or a source-available product:

1. Parties, effective date, and the software's definition — source, object code, installers, updates, schemas, UI, docs.
2. Grant, precisely bounded: personal, non-exclusive, non-transferable, revocable, for a named purpose.
3. Prohibitions: redistribution, sublicensing, reverse engineering (except where law permits), removing notices, commercial use.
4. Third-party components and their licences, by reference to `THIRD-PARTY.md`.
5. Data handling, by reference to `PRIVACY.md` — never restate it, always link.
6. Warranty disclaimer and limitation of liability, in the form Indian courts accept (see `drafting-standards.md`).
7. Term, termination, and what survives.
8. Governing law and forum — a real city and court, not "the courts of India".
9. Supersession clause if an earlier open licence applied.
10. Acceptance mechanism for a binary: a click, a checkbox at install, or an explicit first-run screen. A EULA nobody can accept is not agreed.

## 4. Third-party notices

`NOTICE` or `THIRD-PARTY.md` is a list, not a paragraph. One block per component:

```
<Component> <version> — <SPDX licence>
Copyright <year> <holder>
Source: <url>
Modifications: <none | described>
Licence text: <path or url>
```

Aggregate the licences that require it (Apache-2.0, BSD, MIT, OFL fonts, CC-BY data). Do not invent a component's version; read it from the lockfile.

## 5. Public-domain and classical texts

Homeopathic and legal-source apps in this fleet reproduce classical works. Three separate questions, and they have different answers:

- **Is the original text in the public domain in India?** Life of the author plus 60 years. Boericke's 1922 English translation of the *Organon* is free of copyright; the underlying Hahnemann text even more so. Kent's *Repertory* (1916) likewise. A modern annotated edition is a new copyright in its editorial matter — check what you actually copied.
- **Is the specific file you bundled free?** A scan, a transcription and a typeset edition each carry their own rights. Copying a 1922 text from a 2019 website may copy that site's transcription.
- **Is attribution still required?** Not by copyright once expired, but always by accuracy and by the reader's trust. State edition, translator, publisher and year for every quoted passage — and never silently modernise or "correct" a classical text.

A workable `NOTICE` entry for classical content: title, author, translator, edition, year, publisher of the edition relied on, the source file used, and a line stating the basis for the public-domain conclusion.

## 6. Inbound contributions

Pick one and say so in `CONTRIBUTING.md`:

- **DCO** — the contributor certifies origin with a `Signed-off-by` line. Lightest.
- **CLA** — the contributor grants a licence (often broader, allowing relicensing). Needed if you may change the outbound licence later, or dual-license.
- **Inbound=outbound** — contributions arrive under the repo's own licence. Simplest, and it forecloses relicensing.

Without one of these, an outside contribution is licensed to you only as narrowly as its author intended, and the repo's outbound licence is a promise you may not be able to keep.
