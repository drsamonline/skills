#!/usr/bin/env bash
# 01_enumerate.sh <owner> [extra-owners...]
#
# List every repository an account can reach, one TSV line each:
#   name <TAB> language <TAB> sizeKB <TAB> updated <TAB> description
#
# Requires the GitHub CLI, authenticated (`gh auth status`). If a second connector is
# available (a GitHub App, an org membership), run this again for each and reconcile the
# lists by name — a repo visible through one path and not another is a permissions story
# worth knowing before you draw conclusions.
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <owner> [owner2 ...]" >&2
  exit 1
fi

for owner in "$@"; do
  gh repo list "$owner" --limit 500 \
     --json name,primaryLanguage,diskUsage,updatedAt,description \
     -q '.[] | [.name, (.primaryLanguage.name // "none"), (.diskUsage|tostring), .updatedAt, (.description // "")] | @tsv'
done

# Sanity checks worth doing by hand after this runs:
#   - the line count against the account's own repo count (a round number like 25/30/100
#     usually means a pagination cap, not a small fleet);
#   - organisations the account belongs to:  gh api user/orgs -q '.[].login'
#   - any repo whose description is empty (it will need a manual look during classification).
