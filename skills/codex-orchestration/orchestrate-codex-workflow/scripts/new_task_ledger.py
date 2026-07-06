#!/usr/bin/env python3
"""Generate a Markdown task ledger from a frozen plan."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


ACTION_SECTIONS = {
    "key changes",
    "implementation",
    "implementation changes",
    "test plan",
    "verification",
    "quality gates",
}


def read_plan(path: str | None) -> tuple[str, str]:
    if not path or path == "-":
        return "stdin", sys.stdin.read()
    plan_path = Path(path)
    return str(plan_path), plan_path.read_text(encoding="utf-8")


def first_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if match:
            return strip_markdown(match.group(1))
    return fallback


def strip_markdown(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.strip()


def extract_items(text: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    current_section = "Plan"

    for raw_line in text.splitlines():
        heading = re.match(r"^\s{0,3}#{2,4}\s+(.+?)\s*$", raw_line)
        if heading:
            current_section = strip_markdown(heading.group(1))
            continue

        bullet = re.match(r"^\s*(?:[-*]|\d+[.)])\s+(?:\[[ xX-]\]\s*)?(.+?)\s*$", raw_line)
        if not bullet:
            continue

        item = strip_markdown(bullet.group(1))
        if not item or item.lower() in {"none", "n/a"}:
            continue

        section_key = current_section.lower()
        if section_key in {"summary", "assumptions"}:
            continue

        if section_key not in ACTION_SECTIONS and len(items) >= 12:
            continue

        items.append((current_section, item))

    return items


def build_ledger(title: str, source: str, items: list[tuple[str, str]]) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not items:
        items = [
            ("Planning", "Confirm the frozen spec and success criteria."),
            ("Implementation", "Implement the smallest safe change that satisfies the spec."),
            ("Verification", "Run the planned quality gates and collect evidence."),
            ("Report", "Summarize changes, verification, blockers, and residual risk."),
        ]

    lines = [
        f"# Task Ledger: {title}",
        "",
        f"Generated: {now}",
        f"Source: {source}",
        "",
        "## Operating Rules",
        "",
        "- Keep this ledger aligned with the frozen spec.",
        "- Update task state as work progresses.",
        "- Do not expand scope without updating the spec first.",
        "- Keep verification evidence attached to the task that proved it.",
        "",
        "## Tasks",
        "",
    ]

    for index, (section, item) in enumerate(items, start=1):
        lines.append(f"- [ ] T{index:02d} [{section}] {item}")

    lines.extend(
        [
            "",
            "## Final Gates",
            "",
            "- [ ] V01 Run required lint/typecheck/test/build gates.",
            "- [ ] V02 Complete required browser, API, or runtime smoke checks.",
            "- [ ] V03 Review diff for dead code, unused files, and scope drift.",
            "- [ ] V04 Produce final report with verified and unverified items.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", nargs="?", help="Frozen plan Markdown file, or '-' for stdin")
    parser.add_argument("-o", "--output", help="Write the ledger to this path")
    parser.add_argument("--title", help="Override the ledger title")
    args = parser.parse_args()

    source, text = read_plan(args.plan)
    title = args.title or first_title(text, "Frozen Plan")
    ledger = build_ledger(title, source, extract_items(text))

    if args.output:
        Path(args.output).write_text(ledger, encoding="utf-8")
    else:
        print(ledger)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
