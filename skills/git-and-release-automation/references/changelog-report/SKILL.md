---
name: changelog-report
description:
  A print-optimized HTML template + method for producing a weekly (or
  arbitrary-range) changelog report from GitHub activity. Reads merged PRs
  across the configured repositories for a resolved date window, filters to the
  configured product scope, writes user-facing entries (title, contributors,
  plain-English details), renders a branded PDF via WeasyPrint with embedded
  fonts, and delivers it to the configured channel. All instance specifics —
  org, repos, product filter, branding, timezone, window length, delivery
  channel, footer text — live in references/report-config.md.
---

# Changelog Report

A method + print-optimized HTML template for turning a window's merged GitHub
PRs into a readable, branded PDF changelog written for non-technical readers.
The report is the deliverable; the chat reply is a one-line pointer to it.

## When to use

Use this skill when generating a changelog report over a date window (the
default instance is a rolling 7-day week) that will be rendered as HTML and
then converted to PDF (via WeasyPrint or similar), and posted to a channel. The
HTML it produces is print-first: it is designed to look correct as a PDF, not
as a web page.

## One-time setup — read the config

`references/report-config.md` holds every instance-specific value: GitHub org
and tracked repos, product scope and filter rules, timezone, window length,
branding (name, title, eyebrow, logo, footer), and delivery (channel, timing,
empty-state behaviour). Read it before anything else. If it is empty or a
required field is still a `<placeholder>`, ask the user for these, in one
batch, and write the answers into the file before proceeding:

- GitHub org and the list of repos to track (and which repos to exclude)
- Product scope: the product name shown in the summary line, plus any filter
  rule for shared repos
- Timezone for resolving the window
- Window length and end date (e.g. rolling 7 days ending yesterday)
- Brand name, report title, eyebrow label, logo file, footer text
- Delivery channel, posting time, and what to post when the window is empty

Do not re-ask for values that are already present.

## How it works

1. Load the skill via `skill_view("changelog-report")` to get the `sandbox_dir`.
2. Read `references/report-config.md` for the org, repos, product scope,
   branding, timezone, window, and delivery settings.
3. Resolve the date window (see Resolve the date window).
4. Check the repo list for drift (see Repo discovery).
5. Collect merged PRs inside the window (see Collect merged PRs).
6. Read the template: `read_file("<sandbox_dir>/assets/changelog-template.html")`.
7. Read `assets/fonts.css` and replace the `{{FONTS}}` placeholder in the
   template's `<style>` block with its full contents. The fonts are embedded as
   base64 in that file — never link Google Fonts at render time.
8. Read the logo named in the config, default `assets/logo.svg`, and convert it
   to a data URI: `"data:image/svg+xml;base64," + base64_encode(svg_content)`.
9. Classify PRs into sections, write the entries.
10. Replace the remaining placeholders (`{{DATE}}`, `{{PERIOD}}`,
    `{{SUMMARY}}`, `{{SECTIONS}}`, `{{LOGO}}`, `{{TITLE}}`, `{{EYEBROW}}`,
    `{{FOOTER}}`) with actual content.
11. Write the filled HTML to a file, run the validator, then convert to PDF.
12. Deliver per the config, then append the run to `references/run-log.md`.

**Important:** the template, logo and fonts are in the `assets/` directory.
They are uploaded to the sandbox filesystem when `skill_view` runs, so
`read_file()` will find them on disk. Do NOT use a `templates/` path — that
directory is not uploaded to disk and will cause a "file not found" error.

## Resolve the date window

Resolve every date in the config's timezone, not the host's. The window is
derived from `references/run-log.md` first and from the calendar second:

- Empty log: window start = run date − configured length (7 days for the
  weekly instance), 00:00:00 local; window end = yesterday, 23:59:59 local.
- Non-empty log: window start = the day after the last logged window end, so
  consecutive runs tile exactly. If that span exceeds twice the configured
  length, keep the whole span and state it in the summary.
- Convert both bounds to UTC before querying GitHub, and each PR's `merged_at`
  back to local time before display.
- `{{DATE}}` = the window end date in `dd/mm/yyyy` (e.g. `01/11/2026`).
- `{{PERIOD}}` = the human-readable window: `26 Oct – 1 Nov 2026`. Use
  `29 Dec 2026 – 4 Jan 2027` across a year boundary. For a single-day window,
  write the long date instead: `Saturday, 16 August 2026`.

## Repo discovery

Before collecting, list the org's repositories and diff them against the
tracked list in the config. Report untracked additions in one line under the
summary (`New repos not yet tracked: x, y`) — do not silently add them, and do
not fail the run over it. Repos in the config that now return 404 are reported
the same way.

## Collect merged PRs

For each tracked repo:

- `GET /repos/{org}/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=100`,
  paginating until the oldest `updated_at` on a page is earlier than the window
  start.
- Keep only PRs where `merged_at` is not null and falls inside the window.
  Closed-but-unmerged PRs never appear.
- If a repo returns 404, skip it and note it — do not fail the whole report for
  one renamed or deleted repo.
- Deduplicate by PR id.
- Collapse cross-repo duplicates: the same change merged into several apps
  appears as several PRs with near-identical titles. Keep the earliest and list
  the other PR links on the same contributors line rather than repeating the
  entry.
- Drop `[bot]` authors from the contributor line unless the bot is the only
  author.
- If the window contains zero merged PRs across every tracked repo, stop here
  and follow the empty-state branch under Delivery — do not render a PDF.

## Classify and write entries

Sections, in this order, omitting any that end up empty:

- **New** (`changelog-section--new`) — `feature`, `feat`, `new`
- **Improved** (`changelog-section--improved`) — `enhancement`, `improvement`,
  `perf`
- **Fixed** (`changelog-section--fixed`) — `bug`, `fix`, `hotfix`
- **Removed** (`changelog-section--removed`) — anything a user can no longer
  do: deleted screens, retired features, dropped formats, breaking changes.
  Always describe the migration path if the PR provides one.
- **Under the hood** (`changelog-section--hood`) — `chore`, `refactor`, `ci`,
  `docs`, `test`, `deps`, build and release work

For unlabelled PRs, judge from the title and the changed files. Never invent a
capability: if a PR's purpose is unclear from title, body and diff, put it in
Under the hood and describe the maintenance work factually.

### Grouping long sections

When a section holds more than 12 entries, group it by repo — one
`changelog-group` block per repo, ordered by the repo's earliest merge in the
window, entries chronological inside each group. Below 12 entries, keep the
flat chronological list.

```html
<div class="changelog-group">
  <div class="changelog-group__heading">app-panchang</div>
  <div class="changelog-entry">…</div>
</div>
```

## Content format

The template expects these placeholders:

- `{{FONTS}}` — the full contents of `assets/fonts.css` (embedded woff2)
- `{{DATE}}` — the window end date in dd/mm/yyyy (e.g. `01/11/2026`)
- `{{PERIOD}}` — the window in long form (e.g. `26 Oct – 1 Nov 2026`)
- `{{TITLE}}` — the report title (e.g. `WHATS CHANGED`, `Platform`)
- `{{EYEBROW}}` — the small uppercase label above the title (e.g. `Updates`)
- `{{SUMMARY}}` — 1-line summary. For 1-5 PRs: "N PRs merged across M repos
  for <product>, <period> — #xxx, #yyy." For 6+ PRs: "N PRs merged across M
  repos for <product>, <period>." Omit the PR list once it would run past one
  line. If zero: "No changes for <product> in the last N days."
- `{{LOGO}}` — a base64 data URI of the logo SVG
- `{{FOOTER}}` — the footer text (from config)
- `{{SECTIONS}}` — HTML blocks for each section, structured as:

```html
<section class="changelog-section changelog-section--fixed">
  <h2 class="changelog-section__heading">Fixed</h2>
  <div class="changelog-entry">
    <h3 class="changelog-entry__title">Translated replies no longer disappear from chat</h3>
    <div class="changelog-entry__contributors"><span class="changelog-entry__date">15 Aug</span><strong>by</strong> sohilmomin <a href="https://github.com/drsamonline/app-panchang/pull/955">#955</a></div>
    <p class="changelog-entry__text">Translated replies in Indian languages were silently disappearing from chat — on web from the second message onward, on mobile from the very first. The text now streams correctly on every turn and survives a page reload, on both web and mobile.</p>
  </div>
</section>
```

### Escaping — mandatory

Every value interpolated into the HTML is escaped before insertion: `&` → `&amp;`,
`<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`. Strip markdown emphasis, backticks,
issue references and HTML tags from PR titles and bodies before they become
prose. A PR title containing `<` or `&` must never reach the template raw.

### Entry structure

Each entry has three parts:
1. **Title** (`changelog-entry__title`) — a one-line title from the user's
   job-to-be-done perspective. What problem did this solve or what capability
   did it add? Written in plain English, not technical.
2. **Contributors** (`changelog-entry__contributors`) — starts with the merge
   date in bold (`changelog-entry__date` span, format `dd Mon` e.g. `15 Aug`),
   then the GitHub usernames of who shipped the change prefixed with `by`,
   followed by the PR number as a clickable link. Use the PR author's
   `user.login` field and `pr['html_url']` for the link. Format: `15 Aug · by
   sohilmomin #955` where `#955` is an `<a>` tag linking to the PR URL. For a
   collapsed cross-repo change, add the other links to the same line. If
   multiple people contributed: `15 Aug · by sohilmomin #955, ananya-r #951`.
   **Entries within each section must be sorted chronologically by
   `merged_at` — oldest first.**
3. **Details** (`changelog-entry__text`) — the plain-English explanation of what
   changed and why it matters. **Keep to 2-3 sentences maximum.** No jargon, no
   class names, no file paths.

### Section CSS modifiers

Use these class modifiers on the `changelog-section` element. Note: these only
color the section heading text, not the entry boxes (entries have no colored
background):
- `changelog-section--new` — green accent (new features)
- `changelog-section--improved` — teal accent (improvements)
- `changelog-section--fixed` — rose accent (bug fixes)
- `changelog-section--removed` — violet accent (removals, breaking changes)
- `changelog-section--hood` — grey accent (under the hood)

## Template structure

The template uses these critical print CSS techniques:

### Embedded fonts, no network at render time
```css
@font-face {
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 400;
  font-display: block;
  src: url(data:font/woff2;base64,…) format('woff2');
}
```
Three Plus Jakarta Sans faces (400, 700, 800) are embedded as base64 data URIs
from `assets/fonts.css`, subset to Latin plus the typographic marks the report
uses. There is no `<link>` to Google Fonts: a render host without that network
access would fall back to a system font silently, changing every measurement in
the PDF. Monospace text (eyebrow, contributors) uses a system mono stack.
The logo wordmark is outlined as paths, so it does not depend on the font at
all.

### Page setup with margin box footer
```css
@page {
  size: A4;
  margin: 20mm 18mm 25mm 18mm;

  @bottom-center {
    content: "{{FOOTER}}";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    color: #6b7280;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    color: #6b7280;
  }
}
```
The footer lives in the `@bottom-center` margin box — it appears on every page
but never collides with body content.

### Vertical timeline layout (border-left, not pseudo-element)
```css
.timeline {
  border-left: 2px solid #d1d5db;
  padding-left: 26px;
}
```
The timeline uses a `border-left` on the `.timeline` container, NOT a
`position: absolute` pseudo-element. This is critical: in WeasyPrint's paged
media model, borders on block elements repeat across page breaks, while
absolutely-positioned pseudo-elements only render on the first page. The
vertical grey line must continue on every page.

Each entry has a solid dark grey dot (`#374151`) positioned on the line.
Section headings have NO dots next to them — only entries do.

### Entry-level page break protection
```css
.changelog-entry {
  break-inside: avoid;
  page-break-inside: avoid;
}
```
Each changelog entry (title + contributors + details) is treated as an atomic
block. WeasyPrint will move the whole block to the next page rather than
splitting it mid-sentence.

### Section-level break control
```css
.changelog-section {
  break-inside: auto;
}
.changelog-section__heading {
  break-after: avoid;
}
```
Sections can span pages (they may contain many entries), but a section heading
will never be orphaned at the bottom of a page — it always stays with its first
entry. The same `break-after: avoid` applies to repo group headings.

## Assets

All assets are in the `assets/` directory and are uploaded to the sandbox
filesystem by `skill_view`:

- `assets/changelog-template.html` — the print-optimized HTML template, with a
  `{{FONTS}}` placeholder inside its `<style>` block
- `assets/fonts.css` — three base64 woff2 `@font-face` blocks to splice into
  `{{FONTS}}`
- `assets/logo.svg` — the MATNEO wordmark (constellation mark + outlined
  "MATNEO"). Replace the file, or point the config at another logo, only when
  the brand changes.
- `assets/validate_changelog.py` — pre-flight checker, run before PDF
  conversion

## Validate, then convert

Run the validator on the filled HTML before rendering. It exits non-zero and
lists every failure: unfilled placeholders, unknown section modifiers, entries
missing a title / merge date / PR link / details, details over three sentences,
summary count disagreeing with the rendered entries, empty sections, and
literal `org/repo`, `contributor` or `example.com` strings.

```bash
python <sandbox_dir>/assets/validate_changelog.py /path/to/changelog.html
```

Only then convert:

```python
from weasyprint import HTML
HTML('/path/to/changelog.html').write_pdf('/path/to/changelog.pdf')
```

WeasyPrint is the recommended converter because it has full support for
`@page` margin boxes, `break-inside: avoid`, `border-left` page-break
repetition, embedded fonts and CSS Paged Media — the features this template
relies on. Give it the HTML file's path, not a string, so relative resources
resolve.

## Delivery

- **Non-empty window:** upload the PDF to the configured channel with the
  `{{SUMMARY}}` line as the message text, followed by one line of per-section
  counts (`New 2 · Improved 1 · Fixed 14 · Removed 1`). Name the file
  `changelog-<window end, YYYY-MM-DD>.pdf`. The PDF is the deliverable; the chat
  reply is one line pointing at it.
- **Empty window:** post the configured all-clear line (e.g. "No changes this
  week — nothing merged across the tracked repos.") and attach nothing. Do not
  render an empty PDF.
- **Partial failures:** if some repos 404'd or a section had no entries, say so
  in one short line under the summary. Never pad a section with filler entries.
- **After a successful delivery,** append the run block to
  `references/run-log.md`. On a failed delivery, append nothing.
- **Timing and cadence** belong to the agent's schedule, not to this skill. The
  window comes from the run log, so a late or manual run still produces a
  correct, non-overlapping window.

## Quality checks before delivery

- The validator passes
- The header shows the window (`{{PERIOD}}`), not a single date, for any
  multi-day window
- The summary line states the PR count, repo count, product and period, and
  matches the entries actually rendered
- No sentence is split across two pages (each entry is atomic)
- The footer appears at the bottom of each page, not in the content area
- Section and repo-group headings are not orphaned at the bottom of a page
- Page numbers appear in the bottom-right corner
- The logo appears in the top-right of the header, and its letterforms match
  the wordmark (outlined paths, not a substituted font)
- Body text renders in Plus Jakarta Sans, not a fallback — check the PDF's
  embedded font list if the render host is unfamiliar
- Each entry has a title, a contributors line with merge date + username + PR
  link (#xxx), and details (2-3 sentences)
- Entries within each section are sorted chronologically (oldest merge first)
- Sections over 12 entries are grouped by repo
- No empty section is rendered
- The layout is a vertical grey timeline with solid dark grey dots on entries
  only — section headings (Fixed, Improved, etc.) have NO circles next to them
- The vertical grey timeline line continues on every page (not just page 1)
- The run has been appended to `references/run-log.md`
