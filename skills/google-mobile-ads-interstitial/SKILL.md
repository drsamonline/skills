---
name: google-mobile-ads-interstitial
description: Interstitial ads show full-page ads for users on mobile apps. Interstitial ads are designed to be placed between content and are best placed at natural app transition points.
license: Apache-2.0
metadata:
  title: "google mobile ads interstitial"
  origin: "google/skills"
  upstream-path: "skills/ads/google-mobile-ads-interstitial/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# Google Mobile Ads SDK - Interstitial Ads

Interstitial ads show full-page ads for users on mobile apps. Interstitial ads
are designed to be placed between content and are best placed at natural app
transition points.

## Workflow

1.  **Determine the user's platform**: Identify if the project is Android,
    iOS, or Unity. If unclear, ask before proceeding.

2.  **Read the platform guide** for implementation details:
    -   Android: `references/android-interstitial.md`
    -   iOS: `references/ios-interstitial.md`
    -   Unity: `references/unity-interstitial.md`

3.  **Follow these steps in order**:
    -   [ ] Load the ad
    -   [ ] Register for ad event callbacks
    -   [ ] Show the ad
    -   [ ] Verify the implementation

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/ads/google-mobile-ads-interstitial/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
