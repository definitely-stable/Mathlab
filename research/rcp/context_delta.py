"""RCP-001-D semantic delta between two self-integrity-checked snapshots.

Separate GitHub observation changes from mathematical-claim semantics.
A missing open PR is NOT evidence of merge; CI is never proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research.rcp.claim_registry import RegistryError


def event(kind, identity, before=None, after=None, **extra):
    x = {"kind": kind, "id": identity, "before": before, "after": after}
    x.update(extra)
    return x


def _map(items, key):
    values = {x[key]: x for x in items}
    if len(values) != len(items):
        raise RegistryError("duplicate identity in snapshot: " + key)
    return values


def _diff_items(old_list, new_list, *, key, label, fields=None,
                withdrawn="REMOVED_FROM_REGISTRY"):
    before = _map(old_list, key)
    after = _map(new_list, key)
    changes = []
    for i in sorted(before.keys() | after.keys()):
        if i not in before:
            changes.append(event(label + "_ADDED", i,
                                 after=after[i]))
        elif i not in after:
            changes.append(event(label + "_" + withdrawn, i,
                                 before=before[i],
                                 warning="Absence alone is not a refutation or retraction"))
        elif fields:
            for f in fields:
                if before[i].get(f) != after[i].get(f):
                    changes.append(event(label + "_" + f.upper() + "_CHANGED", i,
                                         before=before[i].get(f),
                                         after=after[i].get(f)))
        elif before[i].get("fingerprint") != after[i].get("fingerprint"):
            changes.append(event(label + "_CONTENT_CHANGED", i,
                                 before=before[i].get("fingerprint"),
                                 after=after[i].get("fingerprint")))
    return changes


def compare_snapshots(old, new):
    if old.get("schema") != "mathlab.rcp.snapshot.v1" or new.get(
            "schema") != "mathlab.rcp.snapshot.v1":
        raise RegistryError("cannot delta different snapshot schemas")
    if old.get("program") != new.get("program") or old.get("root_issue") != \
            new.get("root_issue") or old.get("tracking_issue") != \
            new.get("tracking_issue"):
        raise RegistryError("cross-program or cross-issue snapshot comparison rejected")
    operations = []
    science = []
    if old["inventory"]["main_head"] != new["inventory"]["main_head"]:
        operations.append(event("MAIN_HEAD_CHANGED", "main",
                                old["inventory"]["main_head"],
                                new["inventory"]["main_head"]))
    for name in ("root", "operations"):
        a, b = old["issues"][name], new["issues"][name]
        if a["state"] != b["state"]:
            operations.append(event("ISSUE_STATE_CHANGED", str(a["number"]),
                                    a["state"], b["state"],
                                    warning="Issue closure does not prove root mathematics"))
        elif a.get("updated_at") != b.get("updated_at"):
            operations.append(event("ISSUE_ACTIVITY_UPDATED", str(a["number"]),
                                    a.get("updated_at"), b.get("updated_at"),
                                    warning="Issue update is not a mathematical assertion"))
    old_pr = _map(old["inventory"]["open_prs"], "number")
    new_pr = _map(new["inventory"]["open_prs"], "number")
    for n in sorted(set(old_pr) | set(new_pr)):
        x, y = old_pr.get(n), new_pr.get(n)
        if x is None:
            operations.append(event("PR_ADDED_TO_OPEN_INVENTORY", str(n), after={
                "head": y["head_sha"], "base_ref": y["base_ref"]}))
        elif y is None:
            operations.append(event("PR_NO_LONGER_IN_OPEN_INVENTORY", str(n),
                                    before={"head": x["head_sha"],
                                            "base_ref": x["base_ref"]},
                                    warning="Closure, merge, branch deletion or scan race unverified"))
        else:
            for f in ("head_sha", "base_sha", "base_ref", "parent_pr",
                      "base_relation", "draft", "title"):
                if x.get(f) != y.get(f):
                    operations.append(event("PR_" + f.upper() + "_CHANGED",
                                            str(n), x.get(f), y.get(f)))
            before = x.get("checks", {"status": "NOT_INSPECTED"})
            after = y.get("checks", {"status": "NOT_INSPECTED"})
            if x["head_sha"] == y["head_sha"] and before != after:
                operations.append(event("CI_OBSERVATION_CHANGED", str(n),
                                        before, after,
                                        warning="Check-runs only on same exact SHA; not theorem proof"))
            elif x["head_sha"] != y["head_sha"]:
                operations.append(event("CI_NEW_HEAD_REQUIRES_RECHECK", str(n),
                                        before, after,
                                        warning="Old SHA checks do not apply to updated HEAD"))
    def diagnostics(snapshot):
        return {json.dumps(d, sort_keys=True, separators=(",", ":"))
                for d in snapshot["inventory"]["diagnostics"]}
    for d in sorted(diagnostics(new) - diagnostics(old)):
        operations.append(event("PR_DIAGNOSTIC_APPEARED", d, after=json.loads(d)))
    for d in sorted(diagnostics(old) - diagnostics(new)):
        operations.append(event("PR_DIAGNOSTIC_DISAPPEARED", d, before=json.loads(d)))
    a, b = old["research"], new["research"]
    old_claim = _map(a["claims"], "id")
    new_claim = _map(b["claims"], "id")
    for cid in sorted(set(old_claim) | set(new_claim)):
        x, y = old_claim.get(cid), new_claim.get(cid)
        if x is None:
            science.append(event("CLAIM_ADDED", cid, after=y,
                                 warning="New registry entry is not proof acceptance"))
        elif y is None:
            science.append(event("CLAIM_REMOVED", cid, before=x,
                                 warning="Missing entry is not mathematical refutation"))
        elif x["fingerprint"] != y["fingerprint"]:
            changed = [name for name in
                       ("statement", "mode", "quantifiers", "mathematical_status",
                        "review_status", "novelty_status", "root_impact",
                        "depends_on_claims", "model_ids", "limitations", "source")
                       if x.get(name) != y.get(name)]
            science.append(event("CLAIM_SEMANTICS_CHANGED", cid,
                                 before=x["fingerprint"], after=y["fingerprint"],
                                 changed_fields=changed,
                                 warning="Review exact new proof; status not automatically accepted"))
    for family, key in (("evidence", "EVIDENCE"), ("no_go", "NO_GO")):
        science.extend(_diff_items(a[family], b[family], key="id", label=key))
    for m in set(a["models"]) | set(b["models"]):
        if a["models"].get(m) != b["models"].get(m):
            science.append(event("MODEL_DEFINITION_CHANGED", m,
                                 before=a["models"].get(m),
                                 after=b["models"].get(m),
                                 warning="Model change can alter claim applicability"))
    old_escrow = _map(a["escrow"], "archive")
    new_escrow = _map(b["escrow"], "archive")
    for path in sorted(set(old_escrow) | set(new_escrow)):
        x, y = old_escrow.get(path), new_escrow.get(path)
        if x != y:
            science.append(event("ESCROW_CONTENT_CHANGED", path,
                                 before=x, after=y,
                                 warning="Immutable evidence bytes need independent review"))
    # No timestamp-only "new theorem" events.
    operations.sort(key=lambda e: (e["kind"], e["id"]))
    science.sort(key=lambda e: (e["kind"], e["id"]))
    return {
        "schema": "mathlab.rcp.delta.v1",
        "base_snapshot_sha256": old["snapshot_sha256"],
        "new_snapshot_sha256": new["snapshot_sha256"],
        "base_observed_at_utc": old["observed_at_utc"],
        "new_observed_at_utc": new["observed_at_utc"],
        "acceptance": "OBSERVATION_AND_REGISTRY_DELTA_NOT_MATHEMATICAL_PROOF",
        "operational_events": operations,
        "scientific_registry_events": science,
        "operational_event_count": len(operations),
        "scientific_registry_event_count": len(science),
    }


def format_delta(result):
    lines = [
        "# RCP-001-D — research state delta",
        "",
        "From snapshot: " + result["base_snapshot_sha256"],
        "To snapshot: " + result["new_snapshot_sha256"],
        "Observations: " + result["base_observed_at_utc"] + " -> " +
        result["new_observed_at_utc"],
        "",
        "**Differences in GitHub state or the research registry are not mathematical proofs.**",
        "A disappeared open PR is not automatically merged. New HEAD invalidates old CI assertions.",
        "",
        "## GitHub operational changes (%d)" %
        result["operational_event_count"],
    ]
    for e in result["operational_events"]:
        lines.append("- " + e["kind"] + " / " + str(e["id"]) +
                     ": " + json.dumps({"before": e["before"], "after": e["after"]},
                                       ensure_ascii=False, sort_keys=True))
    lines.extend(["", "## Scientific registry changes (%d)" %
                  result["scientific_registry_event_count"]])
    for e in result["scientific_registry_events"]:
        name = e["kind"] + " / " + str(e["id"])
        fields = e.get("changed_fields")
        if fields:
            name += " (fields: " + ", ".join(fields) + ")"
        lines.append("- " + name)
    lines.extend(["", "Scientific claim status must be separately reviewed and cannot "
                  "be inferred from PR changes, Git object fingerprints, or CI.", ""])
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", required=True, type=Path)
    parser.add_argument("--after", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    from research.rcp.context_builder import read_snapshot
    before, after = read_snapshot(args.before), read_snapshot(args.after)
    changes = compare_snapshots(before, after)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "delta.json").write_text(
        json.dumps(changes, indent=2, sort_keys=True,
                   ensure_ascii=False) + "\n", encoding="utf-8")
    (args.output / "delta.md").write_text(
        format_delta(changes), encoding="utf-8")
    print("RCP-001-D DELTA: operational=%d scientific=%d" %
          (changes["operational_event_count"],
           changes["scientific_registry_event_count"]))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        raise SystemExit("RCP-001-D INVALID: " + str(exc)) from exc
