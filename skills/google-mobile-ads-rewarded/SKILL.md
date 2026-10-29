---
name: google-mobile-ads-rewarded
description: Rewarded ads reward users with in-app items for interacting with full-screen ads. Rewarded ads are served after a user explicitly opts in to view a rewarded ad.
license: Apache-2.0
metadata:
  title: "google mobile ads rewarded"
  origin: "google/skills"
  upstream-path: "skills/ads/google-mobile-ads-rewarded/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# Google Mobile Ads SDK - Rewarded Ads

Rewarded ads reward users with in-app items for interacting with full-screen
ads. Rewarded ads are served after a user explicitly opts in to view a rewarded
ad.

## Workflow

1.  **Determine the user's platform**: Identify if the project is Android,
    iOS, or Unity. If unclear, ask before proceeding.

2.  **Read the platform guide** for implementation details:
    -   Android: `references/android-rewarded.md`
    -   iOS: `references/ios-rewarded.md`
    -   Unity: `references/unity-rewarded.md`

3.  **Follow these steps in order**:
    -   [ ] Load the ad
    -   [ ] Register for ad event callbacks
    -   [ ] Add a UI element to view the ad for a reward
    -   [ ] Show the ad
    -   [ ] Verify the implementation

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/ads/google-mobile-ads-rewarded/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
