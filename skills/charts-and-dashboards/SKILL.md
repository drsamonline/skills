---
name: charts-and-dashboards
description: "Turn data into a chart that explains it and a dashboard that can be read: statistical plots in Seaborn and self-contained interactive HTML dashboards with KPI cards, filters and Chart.js. Use for distributions, relationships, categorical comparisons, regression displays, heatmaps, executive overviews, monitoring snapshots, or a shareable one-file report."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Charts and dashboards"
  category: "data-and-schema"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "build-dashboard, seaborn"
---

# Charts and dashboards

Two halves of the same job. **Static** plots answer a statistical question and must be honest about aggregation, uncertainty and missing data. **Interactive** dashboards answer a decision question and must stay one openable file. Both fail the same way: the chart is chosen before the question is stated.

## When to use

- A distribution, relationship, categorical comparison, regression or correlation matrix must be plotted.
- An executive overview, KPI snapshot or team monitoring page is wanted as one browser-openable file.
- Query results must become a shareable report with filters.

## Method

1. State the question the chart answers, and the decision it feeds. Then choose the chart; the plot type follows the question, not the data frame.
2. Prepare the data first: long-form with meaningful column names, explicit dtypes, documented handling of missing values. Aggregate before plotting, not in the reader's head.
3. For statistical plots, declare the estimator, the uncertainty interval and the aggregation level explicitly. Inspect the support of bounded or discrete measurements before choosing a KDE or violin — a Gaussian kernel can imply impossible negative values, so clip or cut the tails.
4. Use the objects interface for multi-panel figures rather than hand-built subplot grids, and keep one palette per figure with a reason for the colour mapping.
5. For a dashboard, aggregate in the query and embed the aggregated rows — never 50,000 raw rows for the browser to sum.
6. Lay the dashboard out by decision, not by chart: KPI cards first, then the one chart that explains movement, then the breakdown table.
7. Wire filters so a change updates only the changed elements and re-renders with animation disabled; keep the DOM stable.
8. Keep the dashboard self-contained (inline CSS/JS, one file, no CDN at read time) and set `break-inside: avoid` on chart containers so printing does not split them.
9. Label units, sources and the time window on the page itself; a number without a window is not a metric.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`build-dashboard`](references/build-dashboard/) | Self-contained interactive HTML dashboards: KPI cards, Chart.js charts, filters, aggregation, print handling. |
| [`seaborn`](references/seaborn/) | Statistical visualisation in Seaborn: function and objects interfaces, data shape, plot families, uncertainty, current API changes. |

## Key files / entry points

- `references/seaborn/` — the statistical plotting reference: interfaces, long vs wide data, plot families, palettes, current 0.13 API notes, weighting and uncertainty.
- `references/build-dashboard/` — the dashboard build: base template, KPI card pattern, Chart.js integration, filter logic, aggregation guidance.

## Gotchas

- KDE on bounded data implies values outside the support unless you cut the tails.
- Bootstrap weights must be finite, non-negative and sum positive within each group or the estimate is undefined.
- Rebuilding the whole DOM on every filter change makes the dashboard feel broken.
- A pie or doughnut with eight slices is a table with extra steps.
- `Chart.update('none')` for filter-driven updates; the animated update fights the user.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `build-dashboard` — no licence file shipped with the source
- `seaborn` — no licence file shipped with the source
