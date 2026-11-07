#!/usr/bin/env bash
# 02_clone_all.sh <repos.tsv> <dest-dir> [owner] [parallel]
#
# Shallow-clone every repository in repos.tsv into <dest-dir>/<name>. Resumable: re-running
# skips anything already cloned, so a fleet that takes longer than one command timeout can be
# acquired in batches.
#
# Depth 1 with a single branch is deliberate — a full clone pulls history the audit never
# reads, and history is most of the bytes. Check free disk first (df -h): a hundred repos with
# vendored engines ran to 1.5 GB, and one Chromium-derived repo was 170 MB on its own.
set -uo pipefail

TSV="${1:?usage: $0 repos.tsv dest-dir [owner] [parallel]}"
DEST="${2:?usage: $0 repos.tsv dest-dir [owner] [parallel]}"
OWNER="${3:-$(git config --get user.name 2>/dev/null || echo drsamonline)}"
PAR="${4:-8}"

mkdir -p "$DEST"

do_one() {
  n="$1"
  d="$DEST/$n"
  if [ -d "$d/.git" ]; then echo "SKIP $n"; return; fi
  rm -rf "$d"
  if git clone --depth 1 --single-branch --quiet \
       "https://github.com/$OWNER/$n.git" "$d" 2>"/tmp/clone_err.$n"; then
    echo "OK $n"
  else
    echo "FAIL $n $(head -c 140 "/tmp/clone_err.$n" | tr '\n' ' ')"
  fi
}

export -f do_one
export DEST OWNER

cut -f1 "$TSV" | xargs -P "$PAR" -I{} bash -c 'do_one "$@"' _ {}

echo "--- cloned: $(find "$DEST" -maxdepth 1 -mindepth 1 -type d | wc -l)"
echo "--- re-run to retry any FAIL lines"
