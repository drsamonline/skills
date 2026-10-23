---
name: reusable-build-release-workflow
description: One GitHub Actions workflow per app repo builds the portable EXE and Android APK, publishes them to a fixed-tag release, and gives permanent /releases/latest/download/<asset> URLs.
metadata:
  title: "Shared build/release workflow with stable download URLs"
---

# Shared build/release workflow with stable download URLs

Every drsamonline app repo adds **one** workflow file and gets freshly-built binaries attached to a GitHub Release on each push. The `app-builder` kit publishes to a fixed tag (`app-latest`) that is deleted and recreated each run, so `.../releases/latest/download/<APP_NAME>-portable.exe` and `.../<APP_NAME>.apk` are permanent URLs the landing page can link to. The kit itself is checked out alongside the app repo, so the build logic lives in one place.

## When to use

- An app repo should ship download artefacts without duplicating build logic.
- Landing pages need a download link that always points at the newest build.
- You want Windows and Android artefacts produced from the same push.

## Method

1. Drop `examples/build-apps.yml` into the app repo as `.github/workflows/build-apps.yml`. Set two `env` values at the top: `APP_NAME` (names the assets) and `APP_SRC` (the folder holding `index.html`, usually `docs/play`). Keep `KIT_REPO: drsamonline/app-builder`.
2. Trigger on `push` to `main` and on `workflow_dispatch`; grant `permissions: contents: write` so the release job can create releases.
3. **exe job** (`windows-latest`): checkout the app repo (`path: app-repo`) and the kit (`repository: ${{ env.KIT_REPO }}`, `path: builder`); set up Python 3.12; install PyInstaller; `rm -rf builder/exe/app && mkdir -p builder/exe/app && cp -r app-repo/${APP_SRC}/. builder/exe/app/`; run `python builder/exe/build.py`; copy the EXE to `out/`; `upload-artifact`.
4. **apk job** (`ubuntu-latest`): same two checkouts; JDK 17 + Gradle 8.9; install Android SDK 34 build-tools; stage `${APP_SRC}` into `builder/apk/app/src/main/assets/www/`; `sed` the `APP_NAME_PLACEHOLDER`; write `local.properties`; `gradle assembleRelease`; copy the APK; `upload-artifact`.
5. **release job** (`needs: [exe, apk]`, `if: always()`): download both artifacts into `dist/`, then `gh release delete app-latest --repo ${{ github.repository }} --yes --cleanup-tag || true`, then `gh release create app-latest --title ... --notes ... dist/${APP_NAME}-portable.exe dist/${APP_NAME}.apk`.
6. Because the tag is recreated every run, the download URLs never change: `https://github.com/<owner>/<repo>/releases/latest/download/<APP_NAME>-portable.exe` and `.../<APP_NAME>.apk`. Point the landing page at those.
7. For a larger product (e.g. HMS), use the same idea with two tracks: a rolling `nightly` prerelease overwritten on every `main` push (one nightly, never accumulating) plus permanent `vX.Y.Z` releases on tags, with SHA-256 checksums and a `test` gate job that must pass first.

## Key files / entry points

- `examples/build-apps.yml` — the template a consuming repo copies to `.github/workflows/build-apps.yml`.
- `.github/workflows/refresh-hub.yml` / `.github/workflows/refresh.yml` — the sibling pattern for a scheduled, no-prose refresh.
- `HMS/.github/workflows/release.yml` — the tag-driven variant (test gate → dual-platform build → checksums → one release).

## Gotchas

- Deleting and recreating the release each run means `/releases/latest` always resolves to the newest build — but you must delete with `--cleanup-tag` or the tag lingers and the create fails.
- Use `if: always()` on the release job only when you want a partial release; otherwise a failed half leaves a release missing an asset.
- Each run costs ~2 GitHub-hosted runner-minutes (Windows + Linux); the Android build dominates.
- Do not put a build matrix in every app repo — keep the logic in the kit and reference it, so a fix lands everywhere at once.
- Set `APP_NAME` identically in both jobs or the release assets get mismatched names.

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — the reusable workflow and the stable-URL release strategy.
- [HMS](https://github.com/drsamonline/HMS) — a mature variant with a test gate, nightly + versioned releases and checksums.

