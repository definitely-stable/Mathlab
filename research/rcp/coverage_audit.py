"""RCP-COV-001: coverage audit for all open HYP-105 research PRs.

Find unregistered research PRs without inventing scientific acceptance,
merges, formulas, or an arbitrary cap on PR/claim/branch count.
Source: sealed live/replayed RCP-D snapshot. Standard library only.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re

from research.rcp.claim_registry import RegistryError, REPO
from research.rcp.context_builder import read_snapshot

RCP_RESEARCH = re.compile(r"(?:\bHYP[\s-]?105\b|(?:^|[^\d])#230\b)", re.I)
SCOPE_TAGS = (
    ("ALL_H", re.compile(r"\ball[- ]h\b", re.I)),
    ("ORIGINAL", re.compile(r"\boriginal\b", re.I)),
    ("GF5", re.compile(r"(?:GF[\s(]*5|seven[\s-]*class)", re.I)),
    ("QUENCHED", re.compile(r"\bquenched\b|\bevery.fixed\b", re.I)),
    ("NO_GO", re.compile(r"\bno[- ]go\b|\bcounterexample\b", re.I)),
    ("JOINT", re.compile(r"\bjoin\b|\bcoupling\b|\bintersection\b", re.I)),
)


def demand(value, message):
    if not value:
        raise RegistryError(message)


def build_coverage(snapshot):
    inv, research = snapshot["inventory"], snapshot["research"]
    demand(inv.get("repo") == REPO and
           inv.get("complete_open_pr_pagination") is True and
           inv.get("open_pr_count") == len(inv["open_prs"]),
           "coverage requires complete open-PR inventory")
    claims = research.get("claims")
    receipts = research.get("evidence")
    demand(isinstance(claims, list) and isinstance(receipts, list),
           "snapshot needs claim and evidence ledgers")

    by_pr = defaultdict(list)
    by_claim = {}
    for c in claims:
        cid, src = c.get("id"), c.get("source", {})
        pr = src.get("pr")
        demand(isinstance(cid, str) and cid not in by_claim and
               type(pr) is int and pr >= 1, "invalid registered claim reference")
        by_claim[cid] = c
        by_pr[pr].append(cid)

    linked_evidence = set()
    for e in receipts:
        ids = e.get("claim_ids")
        demand(isinstance(ids, list) and
               all(cid in by_claim for cid in ids),
               "evidence claims must be registered")
        linked_evidence.update(ids)
    missing_evidence = sorted(set(by_claim) - linked_evidence)
    # Missing evidence in a future schema is NOT implicitly proof accepted.
    demand(not missing_evidence,
           "registered claims without evidence receipts: " +
           ", ".join(missing_evidence))
    for refs in by_pr.values():
        refs.sort()

    all_open = inv["open_prs"]
    numbers = [p["number"] for p in all_open]
    demand(len(numbers) == len(set(numbers)),
           "duplicate open PR identity in coverage input")
    open_by_num = {p["number"]: p for p in all_open}
    research_prs = [p for p in all_open if p["focus"]]
    queue = []
    covered = []
    for p in research_prs:
        registered = p["number"] in by_pr
        # Keywords are DISCOVERY metadata only, not verified mathematical scope.
        tags = [tag for tag, pattern in SCOPE_TAGS
                if pattern.search(p["title"])]
        row = {
            "pr": p["number"],
            "url": p["url"],
            "title": p["title"],
            "head_sha": p["head_sha"],
            "base_sha": p["base_sha"],
            "base_ref": p["base_ref"],
            "updated_at": p["updated_at"],
            "discovery_tags_unverified": tags,
            "registered_claim_ids": by_pr.get(p["number"], []),
            "source_status": "OPEN_IN_NON_ATOMIC_INVENTORY",
            "proof_status": "NOT_INSPECTED_BY_COVERAGE_AUDIT",
            "ci_status": p["checks"]["status"],
        }
        (covered if registered else queue).append(row)

    # Prefer recently updated entries with strong search signals as a
    # triage aid, not as an epistemic/novelty rank.
    queue.sort(key=lambda x: (x["updated_at"] or "",
                              len(x["discovery_tags_unverified"]),
                              x["pr"]), reverse=True)
    covered.sort(key=lambda x: x["pr"])
    absent = [{
        "pr": pr, "claim_ids": by_pr[pr],
        "status": "NOT_IN_OPEN_PR_INVENTORY",
        "merge_status": "UNVERIFIED_DO_NOT_INFER_MERGED",
    } for pr in sorted(by_pr) if pr not in open_by_num]
    active_registered = sorted(set(by_pr) & {p["number"] for p in research_prs})
    demand(len(covered) + len(queue) == len(research_prs),
           "coverage partition does not reconstruct tagged PR total")
    return {
        "schema": "mathlab.rcp.coverage.v1",
        "snapshot_sha256": snapshot["snapshot_sha256"],
        "observed_at_utc": snapshot["observed_at_utc"],
        "program": "HYP-105",
        "tracking_issue": 474,
        "mathematical_root_issue": 230,
        "root_issue_github_state": snapshot["issues"]["root"]["state"],
        "mathematical_root_acceptance":
            "NOT_INFERRED_FROM_GITHUB_STATE_OR_CI",
        "observation": "NON_ATOMIC_GITHUB_API_SNAPSHOT",
        "provenance": "OPEN_PR_TITLE_AND_PINNED_REGISTRY_METADATA_ONLY",
        "open_pr_count": inv["open_pr_count"],
        "open_hyp105_pr_count": len(research_prs),
        "registered_claim_count": len(by_claim),
        "registered_source_pr_count": len(by_pr),
        "registered_open_hyp105_source_pr_count": len(active_registered),
        "unregistered_open_hyp105_pr_count": len(queue),
        "registered_source_prs_absent_from_open_inventory": absent,
        "coverage_queue": queue,
        "registered_open_research_prs": covered,
        "coverage_is_exhaustive": False,
        "coverage_explanation": (
            "All *open* PRs with matching discovery metadata were scanned, "
            "but titles/body tags can omit research and many scientific "
            "results remain unregistered. This is NOT a mathematical census."
        ),
        "next_procedure": (
            "Inspect each original proof and quantifiers independently; "
            "add exact source-commit claim; archive proof/oracle/test bytes; "
            "pin Git blob SHA and SHA256; add scoped formulas/no-go when "
            "applicable; regenerate five structured Markdown registers; "
            "run CI. Do not promote draft mathematics."
        ),
    }


def markdown(data):
    lines = [
        "# HYP-105 — Research Coverage and Backfill Queue", "",
        "**Discovery metadata only:** title tags and current open-PR "
        "observation are not proof review or scientific acceptance.",
        "**Observation:** " + data["observed_at_utc"] +
        " (non-atomic, exact source commit references only).",
        "**Root issue #" + str(data["mathematical_root_issue"]) +
        ":** GitHub " + data["root_issue_github_state"] +
        " — mathematical Branch A/B/C status NOT inferred.",
        "**Coverage:** %d registered claims from %d source PRs, "
        "%d registered source PRs currently open; "
        "%d open tagged research PRs lack registered claims." %
        (data["registered_claim_count"],
         data["registered_source_pr_count"],
         data["registered_open_hyp105_source_pr_count"],
         data["unregistered_open_hyp105_pr_count"]),
        "",
        "The list is a triage queue, not a priority claim about novelty or "
        "a mathematical theorem. Exact scope and proof must be read before "
        "creating claim/evidence receipts.",
        "", "## Unregistered open research PRs", "",
        "| PR | Last GitHub update (UTC) | Discovery tags (unverified) | Title |",
        "|---|---|---|---|",
    ]
    for item in data["coverage_queue"]:
        lines.append("| [#" + str(item["pr"]) + "](" + item["url"] +
                     ") | " + (item["updated_at"] or "UNKNOWN") +
                     " | " + ", ".join(item["discovery_tags_unverified"]) +
                     " | " + item["title"].replace("|", "\\|").replace("\n", " ") +
                     " |")
    lines.extend(["", "## Registered sources not in open-PR inventory", "",
                  "**Absence does not establish a merge.**"])
    for missing in data["registered_source_prs_absent_from_open_inventory"]:
        lines.append("- PR #" + str(missing["pr"]) + ": " +
                     ", ".join(missing["claim_ids"]) +
                     "; merge state UNVERIFIED.")
    if not data["registered_source_prs_absent_from_open_inventory"]:
        lines.append("None in this observation.")
    lines.extend(["", "## Safe backfill protocol", "",
                  "Inspect the primary proof, ordered quantifiers, "
                  "physical/original incidence model and independently "
                  "pinned source SHA. Only then add a machine-readable "
                  "claim and an archive receipt. Rebuild results, formulas, "
                  "proof graph, protocols and research matrix. Do not infer "
                  "universal minimax or automatically close scientific #230.", ""])
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--snapshot", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args(argv)
    result = build_coverage(read_snapshot(args.snapshot))
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "coverage.json").write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) +
        "\n", encoding="utf-8")
    (args.output / "coverage.md").write_text(markdown(result),
                                            encoding="utf-8")
    print("RCP-COV-001: %d registered claims; %d/%d open tagged PRs "
          "await scoped research import; no automatic theorem inference" %
          (result["registered_claim_count"],
           result["unregistered_open_hyp105_pr_count"],
           result["open_hyp105_pr_count"]))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        raise SystemExit("RCP-COV-001 INVALID: " + str(exc)) from exc
