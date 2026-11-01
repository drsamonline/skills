#!/usr/bin/env bash
# Screenshot a repo's landing page and app with headless Chromium.
#
#   scripts/shot.sh /path/to/repo            # -> docs/assets/landing-desktop.png ...
#   scripts/shot.sh /path/to/repo app        # -> docs/assets/app-desktop.png ...
#
# Writes a desktop (1280 wide) and a phone (430 wide) shot. Look at them before committing.
set -euo pipefail

REPO="${1:?usage: shot.sh <repo-path> [landing|app] [out-name]}"
KIND="${2:-landing}"
NAME="${3:-$KIND}"
ROOT="$(cd "$REPO" && pwd)"

if [ "$KIND" = "app" ]; then PAGE="$ROOT/docs/play/index.html"; else PAGE="$ROOT/docs/index.html"; fi
[ -f "$PAGE" ] || { echo "no page at $PAGE"; exit 1; }

mkdir -p "$ROOT/docs/assets"
CHROME="$(command -v chromium || command -v chromium-browser || command -v google-chrome)"

shot () { # size, outfile, height
  "$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --window-size="$1,$3" --screenshot="$2" "file://$PAGE" >/dev/null 2>&1
  echo "wrote $2 ($(stat -c%s "$2") bytes)"
}

shot 1280 1600 "$ROOT/docs/assets/${NAME}-desktop.png"
shot 430  860  "$ROOT/docs/assets/${NAME}-mobile.png"
