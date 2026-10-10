#!/usr/bin/env python3
"""Validate a dated GitHub issue inventory; never infer live issue/CI state."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "docs/research/ISSUE-TRIAGE-SNAPSHOT.json"
DASHBOARD = ROOT / "docs/research/ISSUE-TRIAGE-ALL-OPEN.md"
PLAN = ROOT / "docs/research/RESEARCH-MAINTENANCE-PLAN-2026-10-10.md"
SHA = re.compile(r"^[0-9a-f]{40}$")
ROOT_KEYS = {"schema", "as_of", "source", "reviewed_main_sha", "scope",
             "issue_count", "issues"}
ISSUE_KEYS = {"number", "title", "url", "state_at_snapshot", "family",
              "triage_action", "parent_issue", "acceptance_gate"}
ACTIONS = {"KEEP_ACTIVE", "UPDATE", "CHECK_PR_CI", "REVIEW_CLOSE_AFTER_GATES",
           "LEGACY_LINK", "AUDIT_SOURCE"}
FAMILIES = {"UCT-005", "UCT-LEGACY", "HYP-105", "INDEX-001", "DAG-ALG",
            "TKG-001", "LITERATURE", "LENT-001", "TOM",
            "HYP-FOUNDATION", "HYP-101"}
BT = chr(96)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def family_for(title: str) -> str:
    if title.startswith("UCT-005"):
        return "UCT-005"
    if re.match(r"^UCT-00[1-4]", title):
        return "UCT-LEGACY"
    if title.startswith("HYP-105"):
        return "HYP-105"
    if title.startswith("INDEX-001"):
        return "INDEX-001"
    if title.startswith("DAG-002"):
        return "DAG-ALG"
    if title.startswith("TKG-001"):
        return "TKG-001"
    if title.startswith(("IMPORT-", "SOURCE-", "RESEARCH-LITERATURE")):
        return "LITERATURE"
    if title.startswith("LENT-001"):
        return "LENT-001"
    if title.startswith("TOM-"):
        return "TOM"
    if title.startswith(("HYP-001", "HYP-002")):
        return "HYP-FOUNDATION"
    if title.startswith("HYP-101"):
        return "HYP-101"
    raise ValueError(f"unclassified issue title: {title}")


def validate(data: dict) -> None:
    require(isinstance(data, dict) and set(data) == ROOT_KEYS,
            "snapshot root keys changed")
    require(data["schema"] == "mathlab.issue-triage-snapshot.v1",
            "unsupported snapshot schema")
    try:
        date.fromisoformat(data["as_of"])
    except (TypeError, ValueError) as exc:
        raise ValueError("invalid snapshot date") from exc
    require(isinstance(data["source"], str)
            and "is:issue is:open" in data["source"],
            "source query must identify open issues only")
    require(isinstance(data["reviewed_main_sha"], str)
            and SHA.fullmatch(data["reviewed_main_sha"]) is not None,
            "invalid reviewed main SHA")
    require(isinstance(data["scope"], str)
            and "not actual issue state" in data["scope"],
            "scope must disclaim live state")
    items = data["issues"]
    require(isinstance(items, list) and items, "empty issue inventory")
    require(type(data["issue_count"]) is int and data["issue_count"] == len(items),
            "issue count does not match inventory")
    require(data["issue_count"] == 55 and data["as_of"] == "2026-10-10",
            "frozen 2026-10-10 search snapshot changed without review")
    numbers: list[int] = []
    by_number: dict[int, dict] = {}
    for item in items:
        require(isinstance(item, dict) and set(item) == ISSUE_KEYS,
                "issue fields changed")
        number = item["number"]
        require(type(number) is int and number > 0,
                "invalid issue number")
        require(number not in by_number, f"duplicate issue #{number}")
        by_number[number] = item
        numbers.append(number)
        require(isinstance(item["title"], str)
                and len(item["title"]) >= 12
                and "\n" not in item["title"]
                and "|" not in item["title"],
                f"invalid issue title #{number}")
        require(item["url"] == f"https://github.com/definitely-stable/Mathlab/issues/{number}",
                f"incorrect issue URL #{number}")
        require(item["state_at_snapshot"] == "OPEN",
                f"not-open-at-snapshot issue #{number}")
        require(item["family"] in FAMILIES
                and item["family"] == family_for(item["title"]),
                f"misclassified family #{number}")
        require(item["triage_action"] in ACTIONS,
                f"invalid triage action #{number}")
        require(isinstance(item["acceptance_gate"], str)
                and len(item["acceptance_gate"]) >= 30
                and "\n" not in item["acceptance_gate"]
                and "|" not in item["acceptance_gate"],
                f"missing/faulty acceptance gate #{number}")
    require(numbers == sorted(numbers), "issue inventory must be numerically sorted")
    for number, item in by_number.items():
        parent = item["parent_issue"]
        if parent is None:
            continue
        require(type(parent) is int and parent in by_number and parent != number,
                f"missing/self parent for issue #{number}")
    visited: set[int] = set()
    active: set[int] = set()

    def visit(number: int) -> None:
        if number in active:
            raise ValueError(f"issue parent cycle at #{number}")
        if number in visited:
            return
        active.add(number)
        parent = by_number[number]["parent_issue"]
        if parent is not None:
            visit(parent)
        active.remove(number)
        visited.add(number)

    for number in numbers:
        visit(number)
    for number, family in ((105, "UCT-005"), (223, "UCT-005"),
                           (234, "UCT-005"), (252, "UCT-005"),
                           (230, "HYP-105"), (183, "INDEX-001"),
                           (195, "TKG-001")):
        require(number in by_number and by_number[number]["family"] == family,
                f"mandatory root/owner issue #{number} missing")
    require(by_number[105]["parent_issue"] is None
            and "OPEN_UNPROVED" in by_number[105]["acceptance_gate"],
            "central root proof status must remain unproved")
    require(by_number[223]["parent_issue"] == 105
            and by_number[234]["parent_issue"] == 105,
            "F1/G4 must have same scientific root, separate owners")
    require("merged" in by_number[252]["acceptance_gate"].lower()
            and "open" in by_number[244]["acceptance_gate"].lower(),
            "historical PR #253/#248 checkpoints drift")


def render(data: dict) -> str:
    counts = Counter(x["family"] for x in data["issues"])
    lines = [
        "# Mathlab open issues — dated snapshot, not live status",
        "",
        "Generated by python research/issue_triage_snapshot.py --write.",
        "**No live GitHub verification, automatic issue closure, or theorem proof.**",
        f"Snapshot: {BT}{data['as_of']}{BT}; reviewed main {BT}{data['reviewed_main_sha']}{BT}.",
        f"Open issues returned by the snapshot query: **{data['issue_count']}**.",
        "",
        "## Coverage by track",
        "",
        "| Track | Open at snapshot |",
        "| --- | ---: |",
    ]
    for family in sorted(counts):
        lines.append(f"| {BT}{family}{BT} | {counts[family]} |")
    lines.extend([
        "",
        "## All issues and proposed next action",
        "",
        "| Issue | Track | Triage recommendation | Parent |",
        "| --- | --- | --- | --- |",
    ])
    for item in data["issues"]:
        number = item["number"]
        parent = f"#{item['parent_issue']}" if item["parent_issue"] is not None else "—"
        lines.append(f"| [#{number}]({item['url']}) — {item['title']} | "
                     f"{BT}{item['family']}{BT} | {BT}{item['triage_action']}{BT} | {parent} |")
    lines.extend([
        "",
        "Recommendations are not GitHub labels, closure decisions or claims of "
        "novelty. Exact acceptance conditions for each issue are in "
        "[the JSON snapshot](ISSUE-TRIAGE-SNAPSHOT.json); "
        "reviewed priority clusters are in "
        "[the dated triage report](ISSUE-TRIAGE-2026-10-10.md).",
        "",
    ])
    return "\n".join(lines)


def validate_plan(data: dict, content: str) -> None:
    """Check that the dated 20-task backlog is ranked and references real issues."""
    rows = [line for line in content.splitlines()
            if re.match(r"^\| [0-9]+ \| P[0-3] \|", line)]
    require(len(rows) == 20, "expected exactly 20 ranked execution tasks")
    pattern = re.compile(
        r"^\| ([0-9]+) \| (P[0-3]) \| (.*?) \| ([1-5])×([1-5])=([0-9]+)"
        r" \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")
    known = {item["number"] for item in data["issues"]}
    previous_phase = -1
    previous_score = 100
    for expected_rank, row in enumerate(rows, 1):
        match = pattern.fullmatch(row)
        require(match is not None, f"malformed backlog row {expected_rank}")
        rank, phase, task, impact, tractability, score, effort, deps, exit_gate = match.groups()
        require(int(rank) == expected_rank, "backlog ranks must be 1..20")
        phase_number = int(phase[1])
        require(phase_number >= previous_phase, "backlog phase order is wrong")
        actual_score = int(impact) * int(tractability)
        require(actual_score == int(score), "incorrect impact-times-tractability score")
        if phase_number == previous_phase:
            require(actual_score <= previous_score, "backlog must be sorted within phase")
        previous_phase, previous_score = phase_number, actual_score
        require(len(task) >= 30 and len(effort) >= 3
                and len(deps) >= 5 and len(exit_gate) >= 30,
                "missing task effort, dependency or acceptance gate")
        links = re.findall(
            r"https://github.com/definitely-stable/Mathlab/(issues|pull)/([0-9]+)",
            task)
        require(bool(links), "backlog task needs a GitHub issue or PR link")
        for kind, number in links:
            if kind == "issues":
                require(int(number) in known, f"backlog refers to absent issue #{number}")
    require("rollback" in content.lower() and "OPEN_UNPROVED" in content,
            "backlog must state rollback and unproved root boundary")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="regenerate markdown after validating the JSON snapshot")
    parser.add_argument("--check", action="store_true",
                        help="validate JSON and require exact generated markdown")
    args = parser.parse_args()
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    try:
        validate(data)
        validate_plan(data, PLAN.read_text(encoding="utf-8"))
        expected = render(data)
        if args.write:
            DASHBOARD.write_text(expected, encoding="utf-8")
        else:
            require(DASHBOARD.is_file()
                    and DASHBOARD.read_text(encoding="utf-8") == expected,
                    "generated issue inventory stale; run --write")
    except (ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"issue-triage FAIL: {exc}\n")
    print(f"issue-triage PASS: {data['issue_count']} open issues in dated snapshot")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
