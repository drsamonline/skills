# Audit legal documentation across a repo or a fleet
#
#   python audit_legal_docs.py --path /path/to/repo
#   python audit_legal_docs.py --gh-user drsamonline --json audit.json
#
# Reports which legal files exist, guesses the licence family, and flags
# evidence of network calls, analytics, on-device storage, health fields and
# bundled third-party assets. Read-only: it never writes to the repo.

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter

LEGAL_FILES = {
    "license": [r"^licen[cs]e(\.(md|txt))?$", r"^copying$"],
    "privacy": [r"^privacy(\.(md|txt))?$"],
    "terms": [r"^terms(\.(md|txt))?$", r"^tos(\.(md|txt))?$"],
    "security": [r"^security(\.md)?$"],
    "disclaimer": [r"^disclaimer(\.(md|txt))?$", r"^medical-disclaimer(\.md)?$"],
    "notice": [r"^notice(\.(md|txt))?$", r"^third[-_]party(\.(md|txt))?$"],
    "contributing": [r"^contributing(\.md)?$"],
    "code_of_conduct": [r"^code[-_]of[-_]conduct(\.md)?$"],
}

LICENCE_SIGNATURES = [
    ("MIT", r"Permission is hereby granted, free of charge"),
    ("Apache-2.0", r"Apache License\s*,?\s*Version 2\.0"),
    ("GPL-3.0", r"GNU GENERAL PUBLIC LICENSE\s*Version 3"),
    ("GPL-2.0", r"GNU GENERAL PUBLIC LICENSE\s*Version 2"),
    ("AGPL-3.0", r"GNU AFFERO GENERAL PUBLIC LICENSE"),
    ("LGPL", r"GNU LESSER GENERAL PUBLIC LICENSE"),
    ("MPL-2.0", r"Mozilla Public License Version 2\.0"),
    ("BSL-1.0", r"Boost Software License"),
    ("Unlicense", r"This is free and unencumbered software released into the public domain"),
    ("CC0-1.0", r"CC0 1\.0 Universal"),
    ("CC-BY-4.0", r"Creative Commons Attribution 4\.0"),
    ("PolyForm-Noncommercial-1.0.0", r"PolyForm Noncommercial License 1\.0\.0"),
    ("PolyForm-Shield-1.0.0", r"PolyForm Shield License 1\.0\.0"),
    ("PolyForm-Small-Business-1.0.0", r"PolyForm Small Business License 1\.0\.0"),
    ("OFL-1.1", r"SIL OPEN FONT LICENSE"),
]

# Signals: (name, regex, what it means for the documents)
SIGNALS = [
    ("network_call", r"\b(fetch\s*\(|XMLHttpRequest|axios\.|requests\.(get|post)|urllib\.request|https?://(?!www\.w3\.org))", "code can reach the network"),
    ("analytics", r"\b(gtag|googletagmanager|google-analytics|posthog|mixpanel|amplitude|plausible|umami|sentry|bugsnag|firebase\.analytics)", "analytics or crash reporting"),
    ("on_device_storage", r"\b(localStorage|sessionStorage|indexedDB|AsyncStorage|sqlite3?|leveldb|SharedPreferences)", "stores data on the device"),
    ("health_fields", r"\b(patient|diagnosis|prescription|remedy|potency|rubric|case_?history|medical_record|dob|blood_group)", "health or patient data"),
    ("ai_provider", r"\b(openai|anthropic|gemini|groq|huggingface|cohere|mistral|ollama|llama)", "calls a model provider"),
    ("payments", r"\b(razorpay|stripe|paypal|instamojo|payu|cashfree)\b", "takes payment"),
    ("auth", r"\b(jwt|oauth|session_id|password_hash|bcrypt|argon2)\b", "has accounts or credentials"),
    ("telemetry_upload", r"\b(upload|telemetry|beacon|sendBeacon)\b", "may transmit user data"),
]

TEXT_EXT = {
    ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".html", ".htm", ".css",
    ".rs", ".c", ".h", ".cpp", ".cs", ".go", ".java", ".kt", ".dart", ".php", ".rb",
    ".sh", ".ps1", ".bat", ".json", ".toml", ".yaml", ".yml", ".md", ".sql", ".swift",
}
SKIP_DIRS = {".git", "node_modules", "dist", "build", "target", ".venv", "venv",
             "__pycache__", ".next", "vendor", "site-packages", ".idea", ".vscode"}
MAX_BYTES = 400_000


def guess_licence(text: str) -> str:
    for name, pattern in LICENCE_SIGNATURES:
        if re.search(pattern, text, re.I):
            return name
    if re.search(r"END[- ]USER[- ]LICEN[CS]E|PROPRIETARY SOFTWARE LICEN[CS]E|All rights reserved", text, re.I):
        return "LicenseRef-Proprietary (EULA)"
    return "unrecognised"


def match_legal(name: str) -> str | None:
    low = name.lower()
    for kind, patterns in LEGAL_FILES.items():
        for p in patterns:
            if re.match(p, low):
                return kind
    return None


def scan_local(root: str) -> dict:
    found, signals, files = {}, Counter(), 0
    licence_text = ""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".git")]
        depth = dirpath[len(root):].count(os.sep)
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            if depth == 0:
                kind = match_legal(fn)
                if kind:
                    found.setdefault(kind, fn)
                    if kind == "license":
                        try:
                            licence_text = open(path, "r", errors="ignore").read()[:20000]
                        except OSError:
                            pass
            ext = os.path.splitext(fn)[1].lower()
            if ext not in TEXT_EXT:
                continue
            try:
                if os.path.getsize(path) > MAX_BYTES:
                    continue
                body = open(path, "r", errors="ignore").read()
            except OSError:
                continue
            files += 1
            for name, pattern, _ in SIGNALS:
                if re.search(pattern, body, re.I):
                    signals[name] += 1
    return {
        "target": root,
        "legal_files": found,
        "licence": guess_licence(licence_text) if licence_text else "none",
        "signals": dict(signals),
        "files_scanned": files,
    }


def gh_api(path: str):
    try:
        out = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return None
        return json.loads(out.stdout)
    except (subprocess.SubprocessError, json.JSONDecodeError):
        return None


def scan_github(user: str, limit: int) -> list[dict]:
    repos, page = [], 1
    while len(repos) < limit:
        batch = gh_api(f"users/{user}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    if not repos:
        print(f"could not list repositories for {user}", file=sys.stderr)
        return []
    results = []
    for repo in repos[:limit]:
        contents = gh_api(f"repos/{user}/{repo['name']}/contents") or []
        names = [c.get("name", "") for c in contents if isinstance(c, dict)]
        found = {}
        for n in names:
            kind = match_legal(n)
            if kind:
                found.setdefault(kind, n)
        licence = (repo.get("license") or {}).get("key") or "none"
        results.append({
            "target": repo["name"],
            "legal_files": found,
            "licence": licence,
            "github_licence_label": (repo.get("license") or {}).get("name") or "none",
            "visibility": repo.get("visibility", ""),
            "language": (repo.get("language") or "-"),
            "description": repo.get("description") or "",
        })
    return results


def required_docs(row: dict) -> list[str]:
    """Documents this repo profile needs, per SKILL.md Step 2."""
    need = ["LICENSE", "SECURITY.md"]
    text = (row.get("description") or "").lower()
    signals = row.get("signals", {})
    health = bool(signals.get("health_fields")) or any(
        k in text for k in ("homeopath", "homoeopath", "remedy", "repertor", "materia", "patient", "hospital", "clinic", "medical"))
    if signals.get("network_call") or signals.get("on_device_storage") or health:
        need.append("PRIVACY.md")
    if signals.get("ai_provider") or signals.get("payments") or signals.get("auth"):
        need.append("TERMS.md")
    if health:
        need.append("DISCLAIMER.md")
        need.append("NOTICE (source attribution)")
    return need


DOC_KIND = {
    "LICENSE": "license",
    "SECURITY.md": "security",
    "PRIVACY.md": "privacy",
    "TERMS.md": "terms",
    "DISCLAIMER.md": "disclaimer",
    "NOTICE (source attribution)": "notice",
}


def missing_docs(row: dict) -> list[str]:
    """Required documents not present, keyed off the kinds the scanner matched."""
    have = set(row.get("legal_files", {}))
    return [d for d in required_docs(row) if DOC_KIND.get(d, d) not in have]


def render(rows: list[dict]) -> str:
    lines = ["| repo | licence | legal files present | missing (suggested) |", "| --- | --- | --- | --- |"]
    for r in rows:
        present = ", ".join(sorted(r["legal_files"].values())) or "—"
        missing = missing_docs(r)
        lines.append(f"| {r['target']} | {r['licence']} | {present} | {', '.join(missing) or '—'} |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit legal documentation in a repo or across a GitHub user's fleet.")
    ap.add_argument("--path", help="local repository path to scan")
    ap.add_argument("--gh-user", help="GitHub login to audit across repositories")
    ap.add_argument("--limit", type=int, default=100, help="max repositories in fleet mode")
    ap.add_argument("--json", help="write full results to this JSON file")
    args = ap.parse_args()

    if not args.path and not args.gh_user:
        ap.error("give --path or --gh-user")

    if args.path:
        row = scan_local(os.path.abspath(args.path))
        print(f"# Audit — {row['target']}\n")
        print(f"Licence detected: **{row['licence']}**")
        print(f"Files scanned: {row['files_scanned']}\n")
        print("## Legal files\n")
        if row["legal_files"]:
            for kind, name in sorted(row["legal_files"].items()):
                print(f"- {kind}: `{name}`")
        else:
            print("- none")
        print("\n## Signals\n")
        if row["signals"]:
            for name, count in sorted(row["signals"].items(), key=lambda kv: -kv[1]):
                meaning = next(m for n, _, m in SIGNALS if n == name)
                print(f"- **{name}** ({count} files) — {meaning}")
        else:
            print("- no network, storage, health or payment signals found")
        print("\n## Documents this profile needs\n")
        for d in required_docs(row):
            print(f"- {d}")
        rows = [row]
    else:
        rows = scan_github(args.gh_user, args.limit)
        if not rows:
            return 1
        print(f"# Fleet audit — {args.gh_user} ({len(rows)} repositories)\n")
        counts = Counter(r["licence"] for r in rows)
        print("Licence spread: " + ", ".join(f"{k} {v}" for k, v in counts.most_common()) + "\n")
        print("_Classification here uses repository metadata only. Run with `--path` on a clone to detect network calls, on-device storage and health fields._\n")
        no_licence = [r["target"] for r in rows if r["licence"] in ("none", "noassertion")]
        if no_licence:
            print("No licence (all rights reserved — nobody may use these): " + ", ".join(no_licence) + "\n")
        print(render(rows))

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(rows, fh, indent=2)
        print(f"\nFull results written to {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
