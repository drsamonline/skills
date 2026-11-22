---
name: small-schema-locked-language-models
description: Harvest a training corpus from your own repositories, train a tiny transformer, export int8 and ship it beside the app — one file per stage, standard library only, no network, no API key, and the model output locked to a schema.
metadata:
  title: "lm-kit"
---

# lm-kit — small, schema-locked models for a fleet

Small, schema-locked language models for the fleet. Harvest the corpus from the repositories, train a
tiny transformer, export int8, ship it beside the app: one file per stage, standard library only, no
network, no API key.

## When to use

- The task is narrow enough that a small model beats an API call: classification, extraction, a fixed reply shape.
- The data cannot leave the machine, or the app must work with no network at all.
- You want the pipeline to be auditable: corpus → train → quantise → ship, one script each.

## Method

1. **Harvest** the corpus from your own repositories (code, docs, commit messages) so the model speaks the project's vocabulary.
2. Fix the **schema** the model must emit before training; the constraint is the product, and a schema-locked model is far easier to trust than a chatty one.
3. Train a small transformer in the standard library — slow but dependency-free, and the point is a pipeline you can read.
4. Quantise to int8 and export one file per stage, so each step can be re-run and diffed.
5. Ship the model beside the app; never fetch it at runtime.

## Key files / entry points

- The harvest script (corpus from repositories).
- The trainer and the schema definition.
- The int8 export.

## Gotchas

- A model trained on the fleet's own docs will happily reproduce private text — filter before training, not after shipping.
- Standard-library training is a demonstration of the pipeline, not a fast path; say which it is.
- Status honesty: the README says "pipeline built, models not trained", which is the difference between a plan and a claim.

## Source projects

- [lm-kit](https://github.com/drsamonline/lm-kit)
