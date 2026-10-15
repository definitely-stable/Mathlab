"""RCP-001-E: scoped claim dependency impact and model-compatibility review.

This reports candidate re-review obligations, NOT mathematical contradictions,
theorem acceptance, or a claim that all HYP-105 PRs are registered.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from pathlib import Path

from research.rcp.claim_registry import RegistryError
from research.rcp.context_builder import read_snapshot
from research.rcp.context_delta import compare_snapshots


def demand(ok, error):
    if not ok:
        raise RegistryError(error)


def unique(records, field):
    values = {}
    for item in records:
        key = item.get(field)
        demand(isinstance(key, str) and key and key not in values,
               "duplicate or invalid " + field)
        values[key] = item
    return values


def proof_graph(snapshot):
    research = snapshot["research"]
    claims = unique(research["claims"], "id")
    model_ids = set(research["models"])
    children = {cid: set() for cid in claims}
    for cid, c in claims.items():
        ids = c.get("depends_on_claims")
        demand(isinstance(ids, list) and len(ids) == len(set(ids)),
               "duplicate or missing claim dependency")
        demand(all(p in claims and p != cid for p in ids),
               "missing claim dependency: " + cid)
        demand(set(c.get("model_ids", [])).issubset(model_ids),
               "unknown mathematical model: " + cid)
        for parent in ids:
            children[parent].add(cid)
    processing, done = set(), set()
    def visit(cid):
        if cid in processing:
            raise RegistryError("claim dependency cycle: " + cid)
        if cid in done:
            return
        processing.add(cid)
        for child in children[cid]:
            visit(child)
        processing.remove(cid)
        done.add(cid)
    for cid in sorted(claims):
        visit(cid)
    edges = [{"parent": p, "dependent": d}
             for p in sorted(children) for d in sorted(children[p])]
    return claims, children, edges


def descendants(children, cid):
    seen = set()
    queue = deque(sorted(children.get(cid, ())))
    while queue:
        n = queue.popleft()
        if n in seen:
            continue
        seen.add(n)
        queue.extend(sorted(children.get(n, ())))
    return sorted(seen)


def compatibility_review(snapshot):
    """Only highlight candidate scope gaps; never invent a contradiction."""
    claims, _, edges = proof_graph(snapshot)
    flags = []
    for edge in edges:
        parent, child = claims[edge["parent"]], claims[edge["dependent"]]
        missing = sorted(set(parent["model_ids"]) - set(child["model_ids"]))
        if missing:
            flags.append({
                "kind": "MODEL_SCOPE_BRIDGE_REVIEW",
                "parent": parent["id"], "dependent": child["id"],
                "models_in_parent_not_declared_in_dependent": missing,
                "decision": "UNREVIEWED_NOT_CONTRADICTION",
                "reason": "Dependency may use an independent deterministic "
                          "proof or a model-preserving reduction; inspect source.",
            })
        if parent["mode"] in {"ENSEMBLE_EXPECTATION", "CONDITIONAL_EXPECTATION"} and \
                child["mode"] in {"ALL_H_IDENTITY", "DETERMINISTIC_BOUND"}:
            flags.append({
                "kind": "EXPECTATION_TO_DETERMINISTIC_BRIDGE_REVIEW",
                "parent": parent["id"], "dependent": child["id"],
                "decision": "UNREVIEWED_NOT_INVALID",
                "reason": "The dependency link must not use averaging "
                          "as a pointwise proof without an explicit argument.",
            })
        p_h, c_h = parent["quantifiers"][0], child["quantifiers"][0]
        if p_h != c_h:
            flags.append({
                "kind": "DOMAIN_TRANSFER_REVIEW",
                "parent": parent["id"], "dependent": child["id"],
                "from": p_h["domain"], "to": c_h["domain"],
                "decision": "UNREVIEWED_NOT_INVALID",
                "reason": "Different h ranges need proof-level domain audit; "
                          "this text check cannot establish subset semantics.",
            })
    return sorted(flags, key=lambda e: (e["kind"], e["parent"], e["dependent"]))


def impact_report(snapshot, previous=None):
    claims, children, edges = proof_graph(snapshot)
    no_go = unique(snapshot["research"]["no_go"], "id")
    evidence = unique(snapshot["research"]["evidence"], "id")
    pr_to_claims = defaultdict(list)
    for cid, claim in claims.items():
        pr_to_claims[claim["source"]["pr"]].append(cid)
    for cid_list in pr_to_claims.values():
        cid_list.sort()
    warnings = compatibility_review(snapshot)
    source_head_observations = []
    for cid, c in claims.items():
        p = c["source_pr_current"]
        if p["state"] == "OPEN" and p["head"] != c["source"]["commit"]:
            source_head_observations.append({
                "claim": cid, "source_pr": c["source"]["pr"],
                "pinned_proof_commit": c["source"]["commit"],
                "observed_pr_head": p["head"],
                "meaning": "PINNED_PROOF_MAY_BE_HISTORICAL_NOT_INVALIDATED",
            })
        elif p["state"] == "NOT_IN_OPEN_INVENTORY":
            source_head_observations.append({
                "claim": cid, "source_pr": c["source"]["pr"],
                "pinned_proof_commit": c["source"]["commit"],
                "observed_pr_head": None,
                "meaning": "CLOSED_MERGED_OR_ABSENT_NOT_INFERABLE_FROM_OPEN_LIST",
            })
    seeds = defaultdict(set)
    changed_events = []
    if previous is not None:
        # Input snapshots must have already passed read_snapshot self-integrity.
        old_claims, old_children, _ = proof_graph(previous)
        delta = compare_snapshots(previous, snapshot)
        old_no_go = unique(previous["research"]["no_go"], "id")
        old_evidence = unique(previous["research"]["evidence"], "id")
        all_edges = {k: set(children.get(k, ())) | set(old_children.get(k, ()))
                     for k in set(children) | set(old_children)}
        for ev in delta["scientific_registry_events"]:
            typ, key = ev["kind"], ev["id"]
            affected = set()
            if typ.startswith("CLAIM_"):
                affected.add(key)
            elif typ.startswith("MODEL_DEFINITION_"):
                affected.update(cid for cid, c in claims.items()
                                if key in c["model_ids"])
                affected.update(cid for cid, c in old_claims.items()
                                if key in c["model_ids"])
            elif typ.startswith("EVIDENCE_"):
                affected.update(evidence.get(key, {}).get("claim_ids", []))
                affected.update(old_evidence.get(key, {}).get("claim_ids", []))
            elif typ.startswith("NO_GO_"):
                affected.update(no_go.get(key, {}).get("related_claim_ids", []))
                affected.update(old_no_go.get(key, {}).get("related_claim_ids", []))
            elif typ == "ESCROW_CONTENT_CHANGED":
                # Match stable escrow PRnnn alias to pinned evidence sources.
                folder = key.split("/")
                names = [x for x in folder if x.startswith("PR") and x[2:].isdigit()]
                if names:
                    pnum = int(names[0][2:])
                    affected.update(pr_to_claims.get(pnum, []))
                    affected.update(cid for cid, c in old_claims.items()
                                    if c["source"]["pr"] == pnum)
            for cid in affected:
                seeds[cid].add(typ)
            changed_events.append({
                "kind": typ, "id": key, "direct_claims": sorted(affected),
            })
    else:
        all_edges = children
        delta = None
    impacts = []
    for cid in sorted(seeds):
        downstream = descendants(all_edges, cid)
        impacts.append({
            "seed_claim": cid,
            "direct_reasons": sorted(seeds[cid]),
            "transitive_dependents": downstream,
            "review_scope": "PROOF_AND_ASSUMPTIONS_RECHECK_REQUIRED",
            "not_implied": "NOT_AUTOMATICALLY_REFUTED_OR_ACCEPTED",
        })
    affected_union = sorted({x["seed_claim"] for x in impacts} |
                            {n for x in impacts for n in x["transitive_dependents"]})
    return {
        "schema": "mathlab.rcp.impact.v1",
        "snapshot_sha256": snapshot["snapshot_sha256"],
        "previous_snapshot_sha256": previous["snapshot_sha256"] if previous else None,
        "acceptance": "CANDIDATE_REVIEW_NOT_MATHEMATICAL_CONTRADICTION",
        "registered_claim_count": len(claims),
        "open_pr_count": snapshot["inventory"]["open_pr_count"],
        "registered_source_pr_count": len(pr_to_claims),
        "coverage": "REGISTERED_CLAIMS_ONLY_NOT_ALL_OPEN_RESEARCH_PRS",
        "proof_edges": edges,
        "transitive_impact": impacts,
        "possibly_impacted_claim_ids": affected_union,
        "semantic_change_seeds": changed_events,
        "compatibility_review_flags": warnings,
        "source_head_observations": sorted(
            source_head_observations, key=lambda z: z["claim"]),
        "diagnosed_contradictions": "NONE_ESTABLISHED_AUTOMATICALLY",
        "observed_operational_events": (
            delta["operational_event_count"] if delta else None),
    }


def md(report):
    lines = [
        "# HYP-105 — RCP-001-E Proof Impact & Model Compatibility",
        "",
        "Snapshot: " + report["snapshot_sha256"],
        "**Coverage:** " + report["coverage"] +
        " — %d claims among %d open PRs (source PRs registered: %d)." %
        (report["registered_claim_count"], report["open_pr_count"],
         report["registered_source_pr_count"]),
        "**Status:** " + report["acceptance"] +
        "; no contradiction or universal theorem has been established.",
        "",
        "## Registered dependency DAG", "",
        "| Prior claim | Dependent claim |",
        "|---|---|",
    ]
    for e in report["proof_edges"]:
        lines.append("| " + e["parent"] + " | " + e["dependent"] + " |")
    lines.extend(["", "## Changes requiring transitive proof re-review"])
    if report["previous_snapshot_sha256"] is None:
        lines.extend(["", "Baseline audit only; no prior state supplied, "
                      "therefore no changed-proof status is fabricated."])
    elif not report["transitive_impact"]:
        lines.extend(["", "No registered scientific changes detected between "
                      "the selected snapshots. Operational PR updates may still "
                      "need inspection."])
    for x in report["transitive_impact"]:
        lines.extend(["", "### " + x["seed_claim"], "",
                      "Change: " + ", ".join(x["direct_reasons"]),
                      "Transitive dependents: " +
                      (", ".join(x["transitive_dependents"]) or "none"),
                      "Action: re-examine pinned proofs and assumptions; "
                      "this does not refute the claims."])
    lines.extend(["", "## Potential model/quantifier compatibility review"])
    if not report["compatibility_review_flags"]:
        lines.append("No metadata-level compatibility review flags.")
    for f in report["compatibility_review_flags"]:
        lines.append("- " + f["kind"] + ": " + f["parent"] +
                     " → " + f["dependent"] + " — " + f["reason"])
    lines.extend(["", "## Source PR vs pinned proof observations"])
    for x in report["source_head_observations"]:
        lines.append("- " + x["claim"] + ": PR #" + str(x["source_pr"]) +
                     " pinned=" + x["pinned_proof_commit"][:12] +
                     " current=" + str(x["observed_pr_head"])[:12] +
                     "; " + x["meaning"])
    lines.extend([
        "", "## Prohibitions", "",
        "A different model ID is a review trigger, not automatically a contradiction. "
        "The graph indexes only registered mathematical claim edges, not every "
        "statement implicit in unregistered research PRs. Source head drift is "
        "not proof invalidation; disappeared PR is not confirmed merged. "
        "No CI success, delta or dependency traversal certifies Root Branch A/B/C.",
        "",
    ])
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--snapshot", required=True, type=Path)
    ap.add_argument("--previous", type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args(argv)
    current = read_snapshot(args.snapshot)
    old = read_snapshot(args.previous) if args.previous else None
    data = impact_report(current, old)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "impact.json").write_text(
        json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) +
        "\n", encoding="utf-8")
    (args.output / "impact.md").write_text(md(data), encoding="utf-8")
    print("RCP-001-E: %d registered claims, %d dependency edges, %d review flags, "
          "%d impacted claims; no automatic theorem certification" %
          (data["registered_claim_count"], len(data["proof_edges"]),
           len(data["compatibility_review_flags"]),
           len(data["possibly_impacted_claim_ids"])))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as e:
        raise SystemExit("RCP-001-E INVALID: " + str(e)) from e
