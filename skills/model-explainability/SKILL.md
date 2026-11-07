---
name: model-explainability
description: "Explain and audit machine-learning predictions with SHAP: choose the explainer and masker, compute and validate feature attributions, handle multi-output and multiclass explanations, and produce local or global visualisations. Use for feature importance, model auditing, subgroup and fairness analysis, or explaining an individual prediction."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Model explainability with SHAP"
  category: "ai-and-ml"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "shap"
---

# Model explainability with SHAP

SHAP answers 'why this prediction' with additive attributions, so the explanation is only as trustworthy as the additivity check. The order matters: fix the model, define the explanation target, choose the explainer deliberately, then pick the plot that answers the question rather than the plot that is convenient.

## When to use

- Feature attributions are needed for a fitted model, globally or for single rows.
- A model is being audited for fairness across cohorts or for reliance on a suspicious feature.
- A stakeholder asks why a specific prediction came out as it did.

## Method

1. Explain a fixed, evaluated model. SHAP is not a substitute for predictive validation — validate first.
2. Define the explanation target: which output, which unit (raw margin or probability), which population.
3. Select the explainer by model family and data size (tree explainers for tree ensembles, permutation or kernel for anything else, deep for neural nets), and the masker for the feature grouping you care about.
4. Compute a modern `Explanation` object and check additivity: the attributions plus the base value must reconstruct the model output. Never silence an additivity failure before checking input shape, preprocessing, model version, output space and row ordering.
5. For multiclass and multi-output, index with `values[..., class_index]` or slice the `Explanation`; the pre-0.45 `values[class_index]` pattern is wrong now.
6. Choose the plot from the question: global summary to locate important patterns, dependence scatter to inspect one, waterfall or force for one row, cohort plots for subgroups.
7. Do not select only visually dramatic rows — document the sampling rule for local explanations.
8. Report limitations with the result: correlation between features, off-manifold inputs, and the fact that attribution is not causation.
9. Never load untrusted pickle, joblib or explainer artefacts — deserialisation can execute code.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`shap`](references/shap/) | The SHAP operating method: explainer selection, additivity validation, multi-output handling, plot selection, limitations, troubleshooting. |

## Key files / entry points

- `references/shap/` — operating rules, explainer and masker selection, tree output semantics, visualisation guidance, troubleshooting order, reference map.
- `references/shap/scripts/` — bundled helper script.

## Gotchas

- Never infer units from a plot's colour or sign — decide margin vs probability explicitly.
- Tree probability-space explanations must be requested explicitly.
- `approximate=True` goes on the call, not the constructor.
- An additivity failure is a bug signal, not a warning to suppress.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `shap` — no licence file shipped with the source
