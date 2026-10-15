"""RCP-001-D: live, scope-safe HYP-105 L0/L1/L2 research context.

Compose RCP-A GitHub inventory, RCP-B mathematical claims and RCP-C evidence.
An API observation is non-atomic; CI successes are never theorem acceptance.
Only Python standard library. No automatic changes to GitHub.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
from typing import Any

from research.rcp.github_inventory import GitHubAPI, InventoryError, build_inventory
from research.rcp.claim_registry import (
    REPO, RegistryError, read_registry, parse_json, validate_registry
)
from research.rcp.evidence_ledger import (
    load_ledgers, validate_ledgers, verify_archives
)

SCHEMA = "mathlab.rcp.snapshot.v1"


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def require(value: bool, why: str) -> None:
    if not value:
        raise RegistryError(why)


def issue_view(raw: dict, expected: int) -> dict:
    require(isinstance(raw, dict) and raw.get("number") == expected,
            "invalid issue payload for #" + str(expected))
    require(raw.get("state") in ("open", "closed"),
            "invalid issue state for #" + str(expected))
    url = raw.get("html_url")
    require(isinstance(url, str) and url.startswith(
        "https://github.com/" + REPO + "/issues/" + str(expected)),
        "invalid issue URL #" + str(expected))
    return {
        "number": expected,
        "state": raw["state"].upper(),
        "url": url,
        "updated_at": raw.get("updated_at"),
        "title": raw.get("title") or "",
    }


def repo_checkout_sha() -> str | None:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL,
            timeout=5, text=True,
        ).strip()
        return sha if len(sha) == 40 and all(c in "0123456789abcdef" for c in sha) else None
    except (OSError, subprocess.SubprocessError):
        return None


def capture_github(api: GitHubAPI, checked: set[int],
                   claim_prs: set[int], at: str) -> tuple[dict, dict]:
    # GitHub is mutable. Keep a provenance envelope; NEVER claim atomicity.
    start_main = api.main_head()
    pulls = api.open_pulls()
    active = {p["number"] for p in pulls}
    require(not (checked - active),
            "explicitly requested CI for a PR that is not open")
    selected = checked | (claim_prs & active)
    inventory = build_inventory(REPO, pulls, start_main, at,
                                api=api, check_prs=selected)
    def get_issue(n: int) -> dict:
        value, _ = api.get(
            "https://api.github.com/repos/" + REPO + "/issues/" + str(n)
        )
        return issue_view(value, n)
    issues = {"root": get_issue(230), "operations": get_issue(474)}
    # Check the root baseline again. This cannot ensure a global atomic
    # snapshot but catches a common race, instead of silently pinning stale main.
    if api.main_head() != start_main:
        raise InventoryError("main moved during live context collection")
    return inventory, issues


def build_snapshot(root: Path, repo_root: Path, inventory: dict,
                   issues: dict, *, origin: str,
                   checkout: str | None = None) -> dict:
    require(origin in ("LIVE_GITHUB", "REPLAYED_INPUT"),
            "unknown observation source")
    require(inventory.get("schema") == "mathlab.rcp.inventory.v1" and
            inventory.get("repo") == REPO and
            inventory.get("complete_open_pr_pagination") is True and
            inventory.get("consistency") == "NON_ATOMIC_GITHUB_API_OBSERVATION",
            "incomplete or wrong-repository inventory")
    require(inventory.get("open_pr_count") == len(inventory.get("open_prs", [])),
            "inventory claims a false PR count")
    require(isinstance(issues, dict) and
            all(issues.get(k, {}).get("state") in ("OPEN", "CLOSED")
                for k in ("root", "operations")),
            "unverified root or operations issue state")
    require(all(issues[k].get("number") == n for k, n in
                (("root", 230), ("operations", 474))),
            "issue number mismatch")
    validate_registry(root)
    receipt_validation = validate_ledgers(root)
    escrow_files = verify_archives(root, repo_root)
    models, claims = read_registry(root)
    evidence, no_go = load_ledgers(root)
    claims.sort(key=lambda c: c["id"])
    evidence.sort(key=lambda e: e["id"])
    no_go.sort(key=lambda n: n["id"])
    c_ids = {c["id"] for c in claims}
    evidence_by_claim: dict[str, list[str]] = {id_: [] for id_ in c_ids}
    no_go_by_claim: dict[str, list[str]] = {id_: [] for id_ in c_ids}
    for e in evidence:
        for cid in e["claim_ids"]:
            evidence_by_claim[cid].append(e["id"])
    for n in no_go:
        for cid in n["related_claim_ids"]:
            no_go_by_claim[cid].append(n["id"])

    known_prs = {p["number"]: p for p in inventory["open_prs"]}
    summary = []
    for c in claims:
        source = c["source"]
        p = known_prs.get(source["pr"])
        # A source SHA pinned to an older commit is still valid provenance:
        # it is NEVER treated as current branch HEAD if the PR advances.
        summary.append({
            "id": c["id"], "title": c["title"], "statement": c["statement"],
            "mode": c["mode"], "quantifiers": c["quantifiers"],
            "mathematical_status": c["mathematical_status"],
            "review_status": c["review_status"],
            "novelty_status": c["novelty_status"],
            "root_impact": c["root_impact"],
            "limitations": c["limitations"],
            "model_ids": c["model_ids"],
            "depends_on_claims": c["depends_on_claims"],
            "evidence_ids": sorted(evidence_by_claim[c["id"]]),
            "no_go_ids": sorted(no_go_by_claim[c["id"]]),
            "source": source,
            "proof_url": "https://github.com/" + REPO + "/blob/" +
                         source["commit"] + "/" + source["proof_path"],
            "source_pr_current": {
                "state": "OPEN" if p else "NOT_IN_OPEN_INVENTORY",
                "head": p["head_sha"] if p else None,
                "base": p["base_ref"] if p else None,
                "checks": p["checks"] if p else {"status": "NOT_INSPECTED"},
            },
            "fingerprint": digest(c),
        })
    records = {
        "models": models,
        "claims": summary,
        "evidence": [{"id": e["id"], "claim_ids": sorted(e["claim_ids"]),
                      "source": e["source"], "artifacts": e["artifacts"],
                      "limitations": e["limitations"],
                      "fingerprint": digest(e)} for e in evidence],
        "no_go": [{
            "id": n["id"], "kind": n["kind"],
            "related_claim_ids": n["related_claim_ids"],
            "evidence_ids": n["evidence_ids"],
            "rejected_inference": n["rejected_inference"],
            "witness_scope": n["witness_scope"],
            "does_not_refute": n["does_not_refute"],
            "reopen_only_if": n["reopen_only_if"],
            "fingerprint": digest(n)
        } for n in no_go],
        "escrow": escrow_files,
        "validation": receipt_validation,
    }
    payload = {
        "schema": SCHEMA,
        "program": "HYP-105",
        "root_issue": 230,
        "tracking_issue": 474,
        "observed_at_utc": inventory["as_of_utc"],
        "observation": {
            "mode": origin,
            "atomicity": "NON_ATOMIC_GITHUB_API_OBSERVATION",
            "checked_issues": [230, 474],
            "root_mathematical_acceptance":
                "NOT_INFERABLE_FROM_ISSUE_STATE_OR_CI",
            "registry_checkout_commit": checkout,
            "snapshot_integrity": "UNSIGNED_SHA256_SELF_CHECK_NOT_SIGNATURE",
        },
        "issues": issues,
        "inventory": inventory,
        "research": records,
    }
    return seal_snapshot(payload)


def seal_snapshot(payload: dict) -> dict:
    data = dict(payload)
    data.pop("snapshot_sha256", None)
    data["snapshot_sha256"] = digest(data)
    return data


def read_snapshot(path: Path) -> dict:
    obj = parse_json(path)
    require(isinstance(obj, dict) and obj.get("schema") == SCHEMA,
            "unsupported snapshot schema")
    claimed = obj.get("snapshot_sha256")
    require(isinstance(claimed, str) and claimed == digest({
        k: v for k, v in obj.items() if k != "snapshot_sha256"}),
        "snapshot content digest mismatch; not an authenticated signature")
    require(obj.get("program") == "HYP-105" and
            obj.get("root_issue") == 230 and obj.get("tracking_issue") == 474,
            "snapshot belongs to a different research program")
    inv = obj.get("inventory")
    require(isinstance(inv, dict) and
            inv.get("schema") == "mathlab.rcp.inventory.v1" and
            inv.get("repo") == REPO and
            inv.get("complete_open_pr_pagination") is True and
            inv.get("open_pr_count") == len(inv.get("open_prs", [])),
            "invalid snapshot inventory")
    require(isinstance(obj.get("issues"), dict) and
            all(obj["issues"].get(k, {}).get("state") in ("OPEN", "CLOSED")
                for k in ("root", "operations")),
            "snapshot contains no verified issue states")
    require(obj.get("observation", {}).get("atomicity") ==
            "NON_ATOMIC_GITHUB_API_OBSERVATION",
            "snapshot falsely claims an atomic GitHub scan")
    research = obj.get("research")
    require(isinstance(research, dict) and
            all(isinstance(research.get(k), list)
                for k in ("claims", "evidence", "no_go", "escrow")),
            "incomplete scientific registry in snapshot")
    return obj


def _fmt_status(pr: dict) -> str:
    value = pr["checks"]
    return value.get("status", "NOT_INSPECTED")


def format_levels(snapshot: dict) -> dict[str, str]:
    """L0 short situational scan; L1 full frontier; L2 durable evidence map."""
    s = snapshot
    inv, research, issues = s["inventory"], s["research"], s["issues"]
    claims, no_gos = research["claims"], research["no_go"]
    by_pr = {p["number"]: p for p in inv["open_prs"]}
    observed = s["observed_at_utc"]
    root = issues["root"]
    l0 = [
        "# HYP-105 — L0 / current research state",
        "",
        "**Observed GitHub:** " + observed + ". Non-atomic API observation.",
        "**Root:** [#230](" + root["url"] + ") GitHub " + root["state"] +
        "; mathematical Branch A/B/C: **NOT ESTABLISHED BY THIS REGISTRY**.",
        "**Operations:** [#474](" + issues["operations"]["url"] + ") GitHub " +
        issues["operations"]["state"] + ".",
        "**main SHA:** " + inv["main_head"] + ".",
        "**Open PRs:** %d overall; %d direct HYP-105; depth max %d." %
        (inv["open_pr_count"], inv["hyp105_direct_count"],
         inv["max_stack_depth"]),
        "**Scientific claims:** %d documented; evidence %d; scoped no-go %d." %
        (len(claims), len(research["evidence"]), len(no_gos)),
        "**Integrity diagnostics:** %d (see L1; not automatically branch failures)." %
        len(inv["diagnostics"]),
        "",
        "CI is reported **only for exact observed HEADs when explicitly inspected**; "
        "NOT_INSPECTED is not PASS. Green CI cannot certify mathematical truth.",
        "",
        "## Registered proof sources (not necessarily current PR HEAD)",
    ]
    for c in claims:
        ps = c["source_pr_current"]
        l0.append("- " + c["id"] + ": [PR #" + str(c["source"]["pr"]) +
                  "](https://github.com/" + REPO + "/pull/" +
                  str(c["source"]["pr"]) + "), " + c["mode"] +
                  ", " + c["mathematical_status"] +
                  ", PR=" + ps["state"] +
                  ", checked CI=" + ps["checks"]["status"])
    l0.extend([
        "",
        "## Outstanding formal boundaries (not settled by archived results)",
    ])
    for n in no_gos:
        l0.append("- " + n["id"] + ": " + n["rejected_inference"])
    l0.extend(["", "Next: inspect L1 quantifiers and claim proof lineage, "
               "then L2 byte-pinned evidence before advancing a theorem.",
               ""])

    l1 = [
        "# HYP-105 — L1 / mathematical proof frontier",
        "",
        "Snapshot: " + s["snapshot_sha256"] + ". Observed: " + observed,
        "Root scientific acceptance is NOT inferred from issue closure or CI.",
        "",
        "## Scoped mathematical results",
    ]
    for c in claims:
        l1.extend([
            "", "### " + c["id"] + " (" + c["mode"] + ")",
            "",
            c["statement"], "",
            "**Ordered quantifiers:** " + "; ".join(
                q["op"] + " " + q["variable"] + " in " + q["domain"]
                for q in c["quantifiers"]),
            "**Proof:** [" + c["source"]["commit"][:12] + "](" + c["proof_url"] + ")"
            " (pinned, not automatically current PR HEAD)",
            "**Status:** " + c["mathematical_status"] +
            " / review " + c["review_status"] +
            " / novelty " + c["novelty_status"],
            "**Depends on:** " + (", ".join(c["depends_on_claims"]) or
                                  "no registered claims"),
            "**Evidence IDs:** " + ", ".join(c["evidence_ids"]),
            "**Does not imply:** " + " ".join(c["limitations"]),
        ])
    l1.extend(["", "## Known scoped no-go paths"])
    for n in no_gos:
        l1.extend(["", "- **" + n["id"] + "**: " + n["rejected_inference"] +
                   " Scope: " + n["witness_scope"] +
                   " Not refuted: " + "; ".join(n["does_not_refute"])])
    l1.extend(["", "## Open PR ancestry and observed exact-HEAD CI",
               "", "| PR | Parent/base | HEAD | CI | Title |",
               "|---|---|---|---|---|"])
    for p in inv["open_prs"]:
        if not p["focus"]:
            continue
        parent = ("#" + str(p["parent_pr"])) if p["parent_pr"] else p["base_relation"]
        l1.append("| [#" + str(p["number"]) + "](" + p["url"] + ") | " +
                  parent + " | " + p["head_sha"][:12] +
                  " | " + _fmt_status(p) +
                  " | " + p["title"].replace("|", "\\|").replace("\n", " ") + " |")
    l1.extend(["", "## Structural warnings"])
    if not inv["diagnostics"]:
        l1.append("No detected structural mismatches.")
    for d in inv["diagnostics"]:
        l1.append("- " + json.dumps(d, ensure_ascii=False, sort_keys=True))
    l1.append("")

    l2 = [
        "# HYP-105 — L2 / full provenance and reproducible receipts",
        "",
        "Snapshot SHA-256 (self-integrity, NOT cryptographic authenticity): " +
        s["snapshot_sha256"],
        "Source status: " + s["observation"]["mode"] +
        "; registry checkout " + str(s["observation"]["registry_checkout_commit"]),
        "Root #230 GitHub state: " + root["state"] +
        "; root mathematical result NOT independently certified.",
        "",
        "## Exact Git-blobs with SHA-256",
        "",
        "| Archived Git path | Source pinned commit | SHA256 |",
        "|---|---|---|",
    ]
    for a in research["escrow"]:
        l2.append("| " + a["archive"] + " | " +
                  a["source_commit"] + " | " + a["sha256"] + " |")
    l2.extend(["", "## Evidence receipts"])
    for ev in research["evidence"]:
        src = ev["source"]
        link = ("https://github.com/" + REPO + "/blob/" +
                src["commit"] + "/" + src["proof_path"])
        l2.extend([
            "", "### " + ev["id"], "",
            "Claims: " + ", ".join(ev["claim_ids"]),
            "Pinned original proof: [" + src["commit"] + "](" + link + ")",
            "Original source blob: " + src["proof_blob_sha"],
            "Oracle/test and fixture entries: " + "; ".join(
                a["role"] + ":" + a["path"] + " @ " + a["git_blob_sha"]
                for a in ev["artifacts"]),
            "Limitations: " + " ".join(ev["limitations"]),
        ])
    l2.extend([
        "", "## No-go revival criteria", "",
    ])
    for n in no_gos:
        l2.extend(["### " + n["id"], "",
                   "Rejected: " + n["rejected_inference"],
                   "Reopen only if: " + n["reopen_only_if"],
                   "Does not refute: " + "; ".join(n["does_not_refute"]),
                   ""])
    return {"L0.md": "\n".join(l0) + "\n",
            "L1.md": "\n".join(l1) + "\n",
            "L2.md": "\n".join(l2) + "\n"}


def write_context(snapshot: dict, dest: Path) -> None:
    # Render first: no empty output on formatter failure.
    level_files = format_levels(snapshot)
    dest.mkdir(parents=True, exist_ok=True)
    for name, text in level_files.items():
        (dest / name).write_text(text, encoding="utf-8")
    (dest / "snapshot.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def run(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--registry", type=Path,
                        default=Path("research/rcp/hyp105"))
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--check-pr", type=int, action="append", default=[])
    parser.add_argument("--check-claim-prs", action="store_true",
                        help="inspect exact HEAD checks for currently open source PRs")
    parser.add_argument("--previous", type=Path,
                        help="compare with previously sealed snapshot.json")
    parser.add_argument("--snapshot-in", type=Path,
                        help="offline replay/render a prior verified snapshot")
    args = parser.parse_args(argv)
    if args.snapshot_in:
        require(not args.check_pr and not args.check_claim_prs,
                "cannot inspect live checks while replaying an old snapshot")
        snap = read_snapshot(args.snapshot_in)
    else:
        validate_ledgers(args.registry)
        _, claims = read_registry(args.registry)
        api = GitHubAPI(REPO)
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        inv, issues = capture_github(
            api, set(args.check_pr),
            {c["source"]["pr"] for c in claims} if args.check_claim_prs else
            set(), now)
        snap = build_snapshot(args.registry, args.repo_root, inv, issues,
                              origin="LIVE_GITHUB", checkout=repo_checkout_sha())
    if args.previous:
        from research.rcp.context_delta import compare_snapshots, format_delta
        old = read_snapshot(args.previous)
        changes = compare_snapshots(old, snap)
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "delta.json").write_text(
            json.dumps(changes, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8")
        (args.output / "delta.md").write_text(format_delta(changes),
                                             encoding="utf-8")
    write_context(snap, args.output)
    print("RCP-001-D snapshot " + snap["snapshot_sha256"][:16] +
          " root=" + snap["issues"]["root"]["state"] +
          " openPR=" + str(snap["inventory"]["open_pr_count"]) +
          " claims=" + str(len(snap["research"]["claims"])) +
          " escrow=" + str(len(snap["research"]["escrow"])) +
          "; CI CHECKS != MATHEMATICAL PROOF")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except (RegistryError, InventoryError) as e:
        raise SystemExit("RCP-001-D FAIL CLOSED: " + str(e)) from e
