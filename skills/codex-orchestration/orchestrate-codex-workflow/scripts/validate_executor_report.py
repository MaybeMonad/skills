#!/usr/bin/env python3
"""Validate that an executor report contains minimum integration evidence."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SECTION_ALIASES = {
    "summary": ("summary",),
    "changed_files": ("changed files", "files changed", "touched files"),
    "verification": ("verification", "tests", "validation"),
    "blockers": ("blockers", "blocker", "risks", "residual risk"),
}

PATH_RE = re.compile(r"(`?[\w./@+-]+/[\w./@+-]+`?|`?[\w.@+-]+\.[A-Za-z0-9]{1,8}`?)")
EVIDENCE_RE = re.compile(
    r"\b(pass(?:ed)?|fail(?:ed)?|not run|blocked|skipped|error|bun|npm|pnpm|yarn|pytest|cargo|go test|swift|xcodebuild|curl|playwright|browser)\b",
    re.IGNORECASE,
)


def read_report(path: str) -> tuple[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    if path.endswith(".json"):
        try:
            return text, json.loads(text)
        except json.JSONDecodeError:
            return text, None
    return text, None


def markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "_root"
    sections[current] = []

    for line in text.splitlines():
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1).strip().lower()
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)

    return {key: "\n".join(value).strip() for key, value in sections.items()}


def get_section(sections: dict[str, str], canonical: str) -> str | None:
    aliases = SECTION_ALIASES[canonical]
    for heading, body in sections.items():
        normalized = re.sub(r"[^a-z0-9 ]+", "", heading.lower()).strip()
        if normalized in aliases:
            return body
    return None


def validate_json(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["JSON report must be an object."]

    summary = data.get("summary")
    changed_files = data.get("changed_files") or data.get("changedFiles")
    verification = data.get("verification")
    blockers = data.get("blockers") if "blockers" in data else data.get("residual_risk")

    if not isinstance(summary, str) or len(summary.strip()) < 20:
        errors.append("Missing useful summary.")
    if not isinstance(changed_files, list):
        errors.append("changed_files must be a list, even when empty.")
    if not verification:
        errors.append("Missing verification evidence.")
    if blockers is None:
        errors.append("Missing blockers or residual_risk field.")
    return errors


def validate_markdown(text: str) -> list[str]:
    errors: list[str] = []
    sections = markdown_sections(text)

    summary = get_section(sections, "summary")
    changed_files = get_section(sections, "changed_files")
    verification = get_section(sections, "verification")
    blockers = get_section(sections, "blockers")

    if not summary or len(summary) < 20:
        errors.append("Missing useful ## Summary section.")

    if not changed_files:
        errors.append("Missing ## Changed Files section.")
    elif "none" not in changed_files.lower() and not PATH_RE.search(changed_files):
        errors.append("Changed Files must list at least one path or explicitly say None.")

    if not verification:
        errors.append("Missing ## Verification section.")
    elif not EVIDENCE_RE.search(verification) and "```" not in verification:
        errors.append("Verification must include command/check evidence or an explicit not-run/blocker result.")

    if blockers is None:
        errors.append("Missing ## Blockers or ## Residual Risk section.")

    if re.search(r"\b(TODO|TBD)\b", text):
        errors.append("Report still contains TODO/TBD placeholders.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", help="Executor report file in Markdown or JSON")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable validation output")
    args = parser.parse_args()

    text, data = read_report(args.report)
    errors = validate_json(data) if data is not None else validate_markdown(text)

    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    elif errors:
        print("Executor report validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("OK: executor report passes basic validation.")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
