---
name: ima-dai-sdk
description: Use the IMA DAI SDK to load HLS or DASH streams into the app for:
license: Apache-2.0
metadata:
  title: "ima dai sdk"
  origin: "google/skills"
  upstream-path: "skills/ads/ima-dai-sdk/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# IMA DAI SDK

Use the IMA DAI SDK to load HLS or DASH streams into the app for:

*   **Livestream events** configured in Google Ad Manager.
*   **Video on demand (VOD)** content ingested into Google Ad Manager.

## Prerequisites

Review the platform-specific integration guides for the target platforms:

*   **Web/HTML5/ReactJs/NodeJs/Angular:** Read
    [StreamManager guide](references/web-StreamManager-guide.md) for loading
    stream URL from Google full-service DAI into `<video>` element.

*   **ChromeCast:** Read
    [StreamManager guide](references/cast-StreamManager-guide.md) for
    integrating the IMA DAI SDK into a ChromeCast Web Receiver.

*   **Android:** Read
    [ImaServerSideAdInsertionMediaSource guide](references/android-ImaServerSideAdInsertionMediaSource-guide.md)
    for integrating Media3 Exoplayer IMA extension.

*   **iOS/tvOS:** Read
    [IMAStreamRequest guide](references/ios-IMAStreamRequest-guide.md) for
    playing streams with `AVPlayer`.

*   **Roku:** Read [StreamManager guide](references/roku-StreamManager-guide.md)
    for implementing DAI on Roku SceneGraph.

## Quick start (general workflow)

1.  Import the SDK
2.  Initialize the SDK
3.  Add stream event listeners
4.  Set up timed metadata forwarding
5.  Make a stream request
6.  Clean up SDK resources when the stream fails or the user leaves the stream.

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/ads/ima-dai-sdk/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
