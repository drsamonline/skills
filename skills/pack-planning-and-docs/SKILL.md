---
name: pack-planning-and-docs
description: Write the plan down and publish the documentation: repository planning documents (SPEC, ROADMAP, TASKS) for AI-assisted work, Wayfinder's SPEC/MAP/ANSWERS for foggy destinations, Hugo sites, and mdBook books or KDP manuscripts. Use when a task needs a durable plan or a documentation site.
license: MIT
metadata:
  title: "Planning and docs pack — plan it, then publish it"
  origin: "ChrisTitusTech/titstack"
  license: "MIT"
  upstream-commit: "b9b7fb03bd347e4b514c5a6ccff397dbc909b65c"
  members: "ai-project-manager, wayfinder, hugo, mdbook"
---

# Planning and docs pack — plan it, then publish it

A pack of 4 related skills from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack), merged into one document so the whole workflow is in front of you at once. Each member is also kept as its own skill in this repository, and every member's support files are preserved here under `references/<member>/`, `scripts/<member>/` and `assets/<member>/`.

## When to use

- AI-assisted development needs planning documents, phase checkpoints and validation evidence.
- The destination is unclear and needs SPEC/MAP/ANSWERS before any implementation.
- A Hugo site needs content, template, taxonomy, asset or deployment work.
- A documentation book or a KDP manuscript is built with mdBook.

## Which member to follow

| Situation | Skill |
|---|---|
| Keep SPEC/ROADMAP/TASKS current | `ai-project-manager` |
| The destination is foggy | wayfinder — explicit invocation only |
| A Hugo site | `hugo` |
| A book or a KDP manuscript | `mdbook` |
| Review the resulting code | not here — use the code quality pack |

## Method

Pick the member for the situation in the table above, then follow that member's own workflow below. Do not run all of them: each member is written to stand alone, and running a review loop for a one-line edit is the failure mode this pack is meant to prevent.

## AI project manager — planning documents

*Member skill: `ai-project-manager` — Create and maintain repository planning documents, phased implementation plans, approval checkpoints, task status, and validation evidence for AI-assisted development work.*

### Workflow

1. Inspect repository instructions, current changes, and the active branch.
2. Identify which planning documents are relevant to the task. Locate each
   relevant `SPEC.md`, `ROADMAP.md`, or `TASKS.md` at the repository root first,
   then under `docs/`. If both locations contain a relevant document, read both
   and surface conflicts.
3. Determine missing requirements, unresolved decisions, dependencies, risks,
   and implementation impact.
4. Match planning detail to the task. Create only requested or useful planning
   artifacts, map work to acceptance criteria, and define applicable validation
   and rollback. Pause points come from the user or a real unresolved decision.
5. Present the plan and stop when the user requested planning only or reserved
   implementation approval.
6. Once implementation is authorized, execute one reviewable phase at a time.
7. Validate the phase, inspect the diff, summarize evidence, and update task
   status only after the exit criteria pass.
8. Hand completed implementation to a pull-request readiness workflow when the
   user asks to prepare, review, publish, or merge the change.

### Diagnostics

```bash
git status --short
git branch --show-current
rg --files -g 'AGENTS.md' -g 'AGENTS.override.md' -g 'SPEC.md' -g 'ROADMAP.md' -g 'TASKS.md'
```

Read every applicable `AGENTS.md` and each planning document relevant to the
task. Do not assume that planning files live under `docs/`.

If the user asks to create missing planning files, adapt the templates under
`assets/ai-project-manager/project-docs/` to the repository. Remove irrelevant sections instead of
leaving placeholders or inventing requirements.

### Safety Rules

- Never rewrite project requirements unless asked.
- Mark work complete only when required validation passes. Record skipped
  required checks as blockers, not as substitutes for acceptance evidence.
- Never ignore conflicts between SPEC, ROADMAP, TASKS, and code.
- Never cross a user approval or plan-only checkpoint.
- Never treat an agent's implementation report as validation evidence.
- Keep project-specific knowledge in project docs, not reusable skills.
- Prefer small reviewable phases over broad plans.

### Validation

- Plan maps to documented requirements.
- Each task has clear scope and acceptance criteria.
- Automated and manual validation are defined before implementation.
- Completed work updates task status when appropriate.
- The final diff contains only the intended phase.
- Final summary lists changed files, checks run, skipped checks, and residual risk.

## Wayfinder — SPEC, MAP and ANSWERS

*Member skill: `wayfinder` — Create or maintain SPEC.md, MAP.md, and ANSWERS.md for large or unclear work. Invoke only with /wayfinder or $wayfinder; do not use for ordinary planning or implementation.*

Turn a foggy destination into three durable local planning files. Stay in
planning mode: investigate and decide, but do not implement the destination
unless the user separately authorizes implementation.

### Files

Create or maintain these files in the repository root unless the user names a
different planning directory:

- `SPEC.md` is the current agreed destination: goals, scope, requirements,
  constraints, and success criteria.
- `MAP.md` is the live route: unresolved questions, dependencies, the current
  frontier, fog that is not precise enough to ask yet, and completed decisions.
- `ANSWERS.md` is the decision record: the answer, rationale, evidence, and
  consequences for each resolved question.

Use the templates under `assets/wayfinder/templates/` as structural starting points.
Adapt them to the project, replace all example content, and remove all
instructional comments from the created planning files.

Keep each fact in one canonical place:

- Put settled requirements and boundaries in `SPEC.md`.
- Put unresolved questions and their status in `MAP.md`.
- Put decision history and supporting detail in `ANSWERS.md`.
- Let `MAP.md` link to completed entries in `ANSWERS.md` instead of repeating
  their detail.

### Workflow

1. Read applicable `AGENTS.md` files, inspect existing changes, and locate any
   existing `SPEC.md`, `MAP.md`, and `ANSWERS.md`. Preserve useful content and
   unrelated user edits; never blindly replace an existing planning file.
2. Identify the invocation mode:
   - **Chart** when the user brings a new idea or the three files do not exist.
   - **Advance** when the files exist and the user wants to continue planning.
   - **Refresh** when new evidence changes the destination, scope, or route.
3. Name the destination before mapping the route. Ask focused questions until
   the intended outcome and stopping point are clear. Do not invent missing
   requirements.
4. Explore breadth-first. Capture precise unanswered decisions as named
   questions in `MAP.md`; capture hazy but in-scope areas under `Fog` until they
   can be phrased as questions. Put work beyond the destination in the
   `Out of scope` section of `SPEC.md`.
5. Give each question a stable `Q-###` identifier, a descriptive name, and any
   dependency on another question. Use names in narration; identifiers exist
   only for stable links and editing.
6. Resolve one coherent question at a time unless the user has already supplied
   a set of inseparable answers. Use repository evidence or current primary
   sources when the answer depends on facts. Record uncertainty explicitly.
7. When a question is resolved:
   - Add its full decision record to `ANSWERS.md`.
   - Update `SPEC.md` with any newly settled requirement or boundary.
   - Move the question from `Frontier` or `Blocked` to `Completed` in `MAP.md`
     and link its name to the answer entry.
   - Add newly exposed questions, update dependencies, and promote any fog that
     has become precise.
8. Stop when the requested planning pass is complete. Summarize the destination,
   decisions recorded, remaining frontier, and any user input needed next.

### Mapping Rules

- A question belongs in `Frontier` when it is precise, unresolved, and has no
  unresolved dependency.
- A question belongs in `Blocked` when another named question must be answered
  first.
- An area belongs in `Fog` when it is in scope but cannot yet be stated as a
  precise question.
- A resolved question belongs in `Completed` and has exactly one detailed entry
  in `ANSWERS.md`.
- Phrase questions as decisions or investigations, not implementation tasks.
  The route is complete when nothing material remains to decide before work can
  be planned or implemented.
- If the whole route is already clear and fits in one session, say that a
  wayfinder map adds little value, still create or update the requested files,
  and keep `MAP.md` concise.

### Validation

Before finishing a planning pass, verify that:

- all three files exist in the same planning directory;
- `SPEC.md` describes a bounded destination with testable success criteria;
- every unresolved precise question appears once in `MAP.md` with a valid
  status and dependency;
- every completed map item links to one unique answer entry;
- settled facts do not remain in the frontier or fog;
- no required decision was silently guessed; and
- no implementation work was performed under planning-only authorization.

This workflow is a simplified local-file adaptation of Matt Pocock's
[Wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
concept.

## Hugo static sites

*Member skill: `hugo` — Build, edit, validate, and troubleshoot Hugo sites, including content, templates, assets, taxonomies, redirects, output formats, and deployment configuration.*

Use this skill for Hugo static-site work: content changes, template/layout edits, taxonomy and menu updates, asset pipeline changes, data files, shortcodes, render hooks, redirects, and deployment validation.

### First Pass

Read repository instructions and inspect existing changes first. Choose the
remaining context by task; a content correction does not require a full site
or deployment inventory:

- Read repository instructions such as `AGENTS.md`, `.codex/config.toml`, and relevant README files.
- Identify the Hugo config file: `hugo.toml`, `config.toml`, `hugo.yaml`, `config.yaml`, `hugo.json`, or a `config/` directory.
- For content edits, read the target page, nearby content, and the archetype or template defining its required fields.
- For template, asset, or data work, inspect the affected theme, module, or local directories: `themes/`, `layouts/`, `assets/hugo/`, `static/`, `data/`, `archetypes/`, `i18n/`.
- For build or deployment changes, inspect the relevant scripts and configuration: `package.json`, `go.mod`, `.github/workflows/`, `netlify.toml`, `vercel.json`, `wrangler.*`, Cloudflare Pages docs, or Makefile.
- Run or inspect `hugo version` when validation depends on version-specific behavior.
- Inspect `git status --short` and preserve unrelated user changes.

### Common Commands

Use the repository's existing scripts when present. Otherwise prefer:

```bash
hugo server
hugo server --buildDrafts --buildFuture
hugo --gc --minify
hugo --printPathWarnings --printUnusedTemplates
```

Use `--source`, `--config`, `--environment`, or `--destination` only when the repository structure requires them.

### Content Work

- Use existing archetypes and nearby content as the model for new pages or posts.
- Preserve explicit `url`, `slug`, `aliases`, and redirect behavior unless the task is specifically about URL changes.
- Keep front matter format consistent with the file or project: TOML, YAML, or JSON.
- Preserve taxonomy spelling and casing used by existing content.
- For posts, verify required fields such as `title`, `date`, `draft`, `description`, `summary`, `image`, `categories`, `tags`, `author`, or custom params by checking templates and archetypes.
- Use `<!--more-->` only when existing list templates or content conventions rely on manual summaries.
- Avoid broad rewrites of historical content unless requested.

### Template Work

- Prefer existing partials, base templates, render hooks, shortcodes, and CSS patterns over one-off markup.
- Identify template lookup rules before moving or renaming files. Section/type-specific templates can be intentional.
- Treat these as high-impact files because they often affect many pages: `baseof.html`, head/meta partials, navigation/header/footer partials, list/single templates, RSS templates, sitemap templates, search index templates, and structured-data partials.
- Preserve SEO and sharing behavior: canonical URLs, Open Graph, Twitter cards, JSON-LD, RSS, sitemap, and robots output.
- Preserve accessibility affordances such as semantic headings, skip links, focus states, useful alt text, labels, and keyboard-accessible controls.
- For shortcodes, keep positional/named parameter compatibility unless a breaking change is requested.

### Assets And Data

- Understand the asset boundary:
  - `assets/hugo/` is processed by Hugo Pipes.
  - `static/` is copied directly to the published site.
  - `public/` is generated output and is usually not source.
- For SCSS, JS, fonts, and images, follow the existing pipeline rather than adding a new package manager or bundler.
- For image processing, check config and template use of `.Resources`, `resources.Get`, `Fit`, `Fill`, `Resize`, WebP, and fingerprinting before changing paths.
- For `data/` files, keep JSON/YAML/TOML valid and preserve the shape consumed by templates.
- Do not commit secrets, API keys, private tokens, or generated credentials in data files, templates, scripts, or build logs.

### Hugo Modules And Themes

- If the site uses Hugo Modules, inspect `go.mod`, `go.sum`, and module imports in config before editing theme files.
- If the site uses a theme under `themes/`, prefer overriding templates in the project `layouts/` directory unless the task requires changing the theme source.
- If the site vendors a theme or has no external theme, treat local templates and assets as first-party source.

### Multilingual Sites

When `languages`, `defaultContentLanguage`, `i18n/`, or language-specific content directories are present:

- Preserve translation keys and language-specific URL rules.
- Check whether menus, params, taxonomies, and permalinks are language-specific.
- Validate at least one representative page per affected language when practical.

### Deployment

Match validation to the deployment target:

- Cloudflare Pages commonly runs `hugo` or a project script and publishes `public/`.
- Netlify may use `netlify.toml`, environment variables, and a pinned Hugo version.
- GitHub Pages may deploy through Actions and may require base URL or artifact settings.
- Vercel or custom hosts may wrap Hugo in package scripts.

Do not change deployment commands, publish directories, Hugo versions, or environment assumptions without checking the existing deployment config.

### Validation

For most changes, run:

```bash
hugo --gc --minify
```

For content scheduled in the future or drafts:

```bash
hugo server --buildDrafts --buildFuture
```

For high-impact template or URL changes, also inspect representative generated pages or run a local server and check:

- Home page.
- A single content page.
- A list page.
- A taxonomy page.
- Search or JSON output if present.
- RSS or sitemap if touched.
- A page using any changed shortcode/render hook.

If the complete build fails because of a confirmed pre-existing problem outside
the requested change, do not weaken or hide that failure. Use the narrowest
legitimate Hugo option or environment that still renders the affected content,
inspect the generated output, and report the focused validation separately from
the unresolved full-build blocker. Never describe focused validation as a
successful complete build.

Report validation commands run, failures, skipped checks, and residual risks.

## mdBook books and KDP manuscripts

*Member skill: `mdbook` — Create, edit, validate, and publish mdBook projects or mdBook-based KDP manuscripts. Use for book.toml, SUMMARY.md, themes, preprocessors, CI, and manuscript conversion.*

Use mdBook as the source workflow for documentation books and KDP manuscripts.

### Workflow

1. Read repository instructions and the affected chapter or configuration.
   Inspect `book.toml` for source/build settings, `SUMMARY.md` for chapter or
   navigation changes, and preprocessors, theme, or deployment configuration
   only when they affect the task.
2. Determine whether the task concerns ordinary mdBook output, custom tooling,
   deployment, or a KDP manuscript, then read only the matching references.
3. Preserve the existing chapter hierarchy, URLs, output contracts, and pinned
   mdBook version unless the task requires changing them.
4. Make the smallest source or configuration change and use valid TOML and
   mdBook Markdown.
5. Build the requested outputs and inspect representative rendered pages or
   publication artifacts rather than relying only on command success.
6. Report exact validation, skipped checks, and remaining publication or
   deployment risks.

### Reference routing

- For KDP ebook or print work, read [references/mdbook/kdp.md](references/mdbook/kdp.md).
- For installation and project creation, read
  [references/mdbook/installation.md](references/mdbook/installation.md) and
  [references/mdbook/creating-a-book.md](references/mdbook/creating-a-book.md).
- For CLI behavior, read [references/mdbook/cli.md](references/mdbook/cli.md).
- For chapter structure, read
  [references/mdbook/summary-format.md](references/mdbook/summary-format.md).
- For Markdown, includes, playgrounds, or hidden lines, read
  [references/mdbook/markdown.md](references/mdbook/markdown.md) and
  [references/mdbook/mdbook-specific.md](references/mdbook/mdbook-specific.md).
- For `book.toml`, preprocessors, renderers, search, or environment variables,
  read [references/mdbook/configuration.md](references/mdbook/configuration.md).
- For themes, MathJax, CI, or developer APIs, read only the corresponding file:
  [theme](references/mdbook/theme.md), [MathJax](references/mdbook/mathjax.md),
  [CI](references/mdbook/continuous-integration.md), or
  [developer APIs](references/mdbook/for-developers.md).

The generated references are snapshots of the official mdBook guide. Check the
version metadata in `references/mdbook/.wiki-version` against the project or current
official documentation when behavior may have changed.

### Reference maintenance

Run `scripts/mdbook/generate-references.sh` from this skill directory to refresh the
bundled upstream references. The script rewrites relative documentation links
to versioned official URLs so the flattened reference files remain navigable.

### Validation

- `mdbook build` succeeds for the intended configuration.
- `mdbook test` passes when the book contains testable Rust examples.
- The table of contents, internal links, images, search, and changed theme
  behavior work in representative rendered output.
- CI or hosted output is checked when deployment behavior changed.
- KDP deliverables pass the format-specific checks in `references/mdbook/kdp.md`.

## Gotchas

- The members disagree on one thing on purpose: `dwm-titus-debug` and `linux-sysadmin` inspect before they change, while the change skills act. Keep that split — diagnosis is read-only unless the user asks for a fix.
- `wayfinder` is explicit-invocation only in the upstream setup. Loading this pack is not an instruction to run it.
- `code-review` never replaces a review the repository requires; `autofix` fixes findings and does not push or reply without authorisation.

## Source projects

All members come from [ChrisTitusTech/titstack](https://github.com/ChrisTitusTech/titstack) at commit `b9b7fb0` (MIT, © 2026 titstack contributors): `ai-project-manager`, `wayfinder`, `hugo`, `mdbook`.
