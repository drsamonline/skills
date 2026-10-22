---
name: Android WebView APK packaging
description: Wrap a static single-file web app into a dependency-free Android WebView APK (platform framework only, no AndroidX), signed with a shared debug key, built by Gradle in CI.
---

# Android WebView APK packaging

A drsamonline web app is shipped to Android by wrapping it in a minimal WebView. The `app-builder` kit's `apk/` project is deliberately tiny: one `Activity`, one `AndroidManifest.xml`, `compileSdk 34 / minSdk 24 / targetSdk 34`, and **no AndroidX** — only the platform framework. The app's HTML is copied into `app/src/main/assets/www/` and loaded from `file:///android_asset/www/index.html`, so it runs fully offline.

## When to use

- You have a static web app (single HTML file or a `docs/play/` folder) and want a sideloadable Android app.
- You want the smallest possible APK with no AndroidX/Jetpack dependencies and no runtime download.
- You want CI to build and attach the APK to a release automatically.

## Method

1. Use the `app-builder` kit's `apk/` Gradle project. Set `namespace`/`applicationId` to your own reverse-DNS id, keep `compileSdk = 34`, `minSdk = 24`, `targetSdk = 34`, Java/Kotlin target 17, and AGP 8.x.
2. Write a single `MainActivity` that extends `android.app.Activity` (not AppCompatActivity, to avoid AndroidX). In `onCreate`, build a `WebView`, enable `javaScriptEnabled`, `domStorageEnabled`, `allowFileAccess`, `allowContentAccess`, `useWideViewPort`, `loadWithOverviewMode`, and set `mediaPlaybackRequiresUserGesture = false`. Set a plain `WebViewClient`, then `loadUrl("file:///android_asset/www/index.html")` and `setContentView(webView)`.
3. Handle the hardware back button: in `onKeyDown`, if `KEYCODE_BACK` and `webView.canGoBack()`, call `goBack()` and consume the event; also override the deprecated `onBackPressed()` for pre-API-33 devices.
4. Copy the app's HTML into `app/src/main/assets/www/`. Keep it as the same single file (or folder) the browser build uses — one source, two wrappers.
5. Set the app label via `res/values/strings.xml`. Use a placeholder token (`APP_NAME_PLACEHOLDER`) and have CI `sed` it to the real name.
6. Declare only `android.permission.INTERNET` in the manifest (some wrapped apps fetch remote assets) and set `android:theme="@android:style/Theme.NoTitleBar"` and `configChanges` for orientation/screen-size so rotation does not restart the activity.
7. Sign with the kit's committed debug-grade keystore (`keystore/debug.keystore`, alias `androiddebugkey`, store/key password `android`) so successive builds install over each other during sideloading. `app/build.gradle.kts` reads `KEYSTORE_FILE`/`KEYSTORE_PASSWORD`/`KEY_ALIAS`/`KEY_PASSWORD` from the environment and falls back to the debug key — pass repository secrets to use your own key.
8. Build with Gradle in CI: set up JDK 17, `gradle/actions/setup-gradle` with Gradle 8.9, install `platforms;android-34` and `build-tools;34.0.0` via `sdkmanager`, write `local.properties` with `sdk.dir`, then run `gradle assembleRelease`. Collect `app/build/outputs/apk/release/app-release.apk`.

## Key files / entry points

- `apk/settings.gradle.kts`, `apk/build.gradle.kts`, `apk/gradle.properties` — project-level Gradle config (AGP + Kotlin plugin applied false).
- `apk/app/build.gradle.kts` — module config, `signingConfigs.release` reading the env vars.
- `apk/app/src/main/AndroidManifest.xml` — INTERNET permission, NoTitleBar theme, launcher intent-filter.
- `apk/app/src/main/java/.../MainActivity.kt` — the WebView wrapper.
- `apk/app/src/main/res/values/strings.xml` — `app_name` with the `APP_NAME_PLACEHOLDER` token.
- `apk/app/src/main/assets/www/` — where the app's HTML is staged by the workflow.
- `keystore/debug.keystore` — shared debug-grade signing key.

## Gotchas

- The committed key is **debug-grade and public** — it only exists so successive sideloaded builds can be installed over one another. It is **not** a Play Store key and provides no security. Never publish to Google Play with it.
- Do not pull in AndroidX/AppCompat unless you truly need it; staying on the platform framework keeps the APK small and the build dependency-light.
- `file:///android_asset/` is the only origin; relative paths in the HTML must resolve inside `assets/www/`. Absolute `/` paths break.
- The APK is debug-signed and the EXE is unsigned, so first-run warnings (Play Protect / SmartScreen) are expected — document them.
- A cold Android build downloads the SDK and Gradle; it is the slow half of a release (~2 runner-minutes total).
- Keep `APP_NAME` consistent between the EXE and APK jobs so both assets land on the same release with predictable names.

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — the shared `apk/` Gradle project and the reusable build workflow.
- [open-materia-medica](https://github.com/drsamonline/open-materia-medica) — also ships a hand-written `android/` Gradle project with a `sync-assets.sh` that copies the web edition into the app.

