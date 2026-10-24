---
name: free-tool-marketing
description: Plan and judge a free, genuinely useful tool as the way people find the paid work — engineering as marketing. Use when deciding whether to build a free tool, what it should do, and how it earns attention without ads or trackers.
metadata:
  title: "Free tools as marketing (engineering as marketing)"
---

# Free tools as marketing

Take something people pay for elsewhere and give a small, real version away — the free tool is how they find you, and the paid or supported work is what they buy. This is already the house model: the apps are free, and the system that builds them is the product.

## When to use

- Deciding whether to build a free tool, and what it should do.
- A free tool exists but attracts nobody — the honest question is whether it solves a real problem.
- Explaining the model ("why is it free?") to a reader or a buyer.

## Method

1. **Solve a real problem on its own.** The tool must be worth using even if the product it promotes did not exist. A tool that is only useful after buying something is an ad, and reads like one.
2. **Stay adjacent to the core.** The free tool should share the problem space with the work it leads to, so the step from tool to product is natural.
3. **Do one thing, and do it well.** Small, fast, no sign-up, no friction. Our tools are single-file and offline; a free tool that needs an account or a network contradicts everything else we ship.
4. **Judge it honestly.** Value to the reader × the number of readers it can reach, versus the cost to build and keep it working. If the second number is a guess, say so — do not dress a hunch as a forecast.
5. **Measure only what we can actually measure.** No trackers are shipped, so "conversions" and "attribution" are unavailable by design. What we can see honestly: repository traffic and clones (GitHub API), stars, and inbound issues. Report those; do not claim the ones we cannot see.
6. **Keep it maintained, or retire it.** A broken free tool is worse than no free tool; a stale one should be said to be stale, not quietly left to rot.

## Key files / entry points

- The tool itself — a single-file app, or a `docs/` page.
- The landing page that explains it (see `static-landing-page-seo`).
- The repository's traffic and stars (GitHub API) — the only honest signal we have.

## Gotchas

- **No trackers, ever.** Third-party analytics is ruled out by the privacy stance, so a plan that depends on conversion tracking does not fit here.
- **No invented numbers.** "AI-referred traffic converts 6-27× higher" is a sourced claim from a survey, not ours; cite it as theirs or leave it out.
- A free tool with a lead-capture gate is not free — decide deliberately whether the gate is worth the friction, and default to no gate.
- The tool must be free to *use*, not merely free to try.

## Source projects

- [All4ONE](https://github.com/drsamonline/All4ONE), [TTB](https://github.com/drsamonline/TTB), [bmi-bmr-tdee-macros-fluid-calculator](https://github.com/drsamonline/bmi-bmr-tdee-macros-fluid-calculator) — free, useful tools that already work this way.

*Adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), rewritten for this system.*
