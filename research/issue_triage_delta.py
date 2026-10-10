"""Offline integrity of a dated issue-set delta; never calls GitHub or asserts live state."""
import json
import re
from issue_triage_snapshot import ROOT, SNAPSHOT, validate as validate_archive

DELTA = ROOT / "docs/research/ISSUE-TRIAGE-DELTA-2026-10-11.json"
REPORT = ROOT / "docs/research/ISSUE-TRIAGE-POSTSNAPSHOT-2026-10-11.md"
PLAN = ROOT / "docs/research/RESEARCH-MAINTENANCE-PLAN-2026-10-11.md"

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate_delta(data, archive):
    validate_archive(archive)
    required = {"schema", "date", "immutable_historical_snapshot", "historical_count",
                "source_query", "captured_open_issue_count", "captured_open_issue_ids",
                "added", "closed", "open_pr_count", "open_pr_ids",
                "scientific_root", "warning"}
    require(isinstance(data, dict) and set(data) == required, "delta schema mismatch")
    require(data["schema"] == "mathlab.issue-triage-delta.v1" and data["date"] == "2026-10-11",
            "invalid delta version/date")
    require(data["immutable_historical_snapshot"] == "ISSUE-TRIAGE-SNAPSHOT.json" and
            data["historical_count"] == archive["issue_count"] == 55,
            "historical snapshot mutated")
    require(data["source_query"] == "repo:definitely-stable/Mathlab is:issue is:open",
            "source must be GitHub open issues only")
    require("Dated" in data["warning"] and "no theorem proof" in data["warning"],
            "false live/theorem inference")
    ids = data["captured_open_issue_ids"]
    require(isinstance(ids, list) and all(type(n) is int and n > 0 for n in ids)
            and ids == sorted(set(ids)) and data["captured_open_issue_count"] == len(ids),
            "duplicate/missing captured open issue IDs")
    before = {i["number"] for i in archive["issues"]}
    now = set(ids)
    new, closed = data["added"], data["closed"]
    require(isinstance(new, list) and isinstance(closed, list), "bad delta groups")
    new_ids = []
    for issue in new:
        require(isinstance(issue, dict) and
                set(issue) == {"number", "title", "url", "category"},
                "bad new issue fields")
        number = issue["number"]
        require(type(number) is int and len(issue["title"]) >= 15 and
                issue["url"] == f"https://github.com/definitely-stable/Mathlab/issues/{number}",
                "invalid new issue identity")
        require(issue["category"] in {"EXTERNAL_TRACKER", "UCT-005", "OTHER"},
                "unknown new issue class")
        require((number == 289) == (issue["category"] == "EXTERNAL_TRACKER"),
                "external cross-repository tracker misclassified")
        new_ids.append(number)
    closed_ids = []
    for issue in closed:
        require(isinstance(issue, dict) and set(issue) == {"number", "title", "url"},
                "bad closed issue fields")
        number = issue["number"]
        require(type(number) is int and
                issue["url"] == f"https://github.com/definitely-stable/Mathlab/issues/{number}",
                "bad closed issue URL")
        closed_ids.append(number)
    require(new_ids == sorted(set(new_ids)) and set(new_ids) == now - before,
            "added issue set not conserved")
    require(closed_ids == sorted(set(closed_ids)) and set(closed_ids) == before - now,
            "closed issue set not conserved")
    require(len(before) + len(new_ids) - len(closed_ids) == len(now),
            "historical/current issue count conservation failed")
    require(data["scientific_root"] == {"issue": 105, "state": "OPEN_UNPROVED"} and
            105 in now, "false scientific root promotion")
    prs = data["open_pr_ids"]
    require(isinstance(prs, list) and all(type(n) is int and n > 0 for n in prs) and
            prs == sorted(set(prs)) and len(prs) == data["open_pr_count"],
            "duplicate/missing open PR IDs")

def audit():
    archive = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    data = json.loads(DELTA.read_text(encoding="utf-8"))
    validate_delta(data, archive)
    report = REPORT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    for issue in data["added"] + data["closed"]:
        require(f"#{issue['number']}" in report,
                f"report missing issue #{issue['number']}")
    for number in (256, 257, 263, 277, 290, 294, 296, 297):
        require(f"#{number}" in plan,
                f"plan missing dependency/owner #{number}")
    for term in ("exact-head", "post-merge", "GitHub-hosted", "OPEN_UNPROVED"):
        require(term in plan, f"plan missing acceptance firewall: {term}")
    require("OPEN_UNPROVED" in report, "report falsely omits root novelty boundary")

if __name__ == "__main__":
    audit()
    print("issue-triage-delta PASS: dated issue/PR sets and scope gates")
