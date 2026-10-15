"""RCP-001-B: deterministic machine/human claim index; never promote draft proofs."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from research.rcp.claim_registry import (
    REPO, RegistryError, read_registry, validate_registry, verify_pinned_sources
)

def render(root: Path) -> tuple[dict, str]:
    validation = validate_registry(root)
    _, claims = read_registry(root)
    claims.sort(key=lambda c: c["id"])
    index = {
        "schema": "mathlab.rcp.claim-index.v1",
        "program": "HYP-105",
        "root_issue": 230,
        "root_branch_status": "NOT_ESTABLISHED_BY_THESE_CLAIMS",
        "acceptance": "REGISTRY_METADATA_ONLY_NOT_PROOF",
        "claims": [{
            "id": c["id"], "mode": c["mode"],
            "mathematical_status": c["mathematical_status"],
            "review_status": c["review_status"],
            "novelty_status": c["novelty_status"],
            "quantifiers": c["quantifiers"],
            "depends_on_claims": c["depends_on_claims"],
            "source_pr": c["source"]["pr"],
            "source_commit": c["source"]["commit"],
            "proof_url": "https://github.com/" + REPO + "/blob/" +
                         c["source"]["commit"] + "/" + c["source"]["proof_path"],
            "statement": c["statement"],
            "limitations": c["limitations"],
        } for c in claims],
        "dependency_edges": sorted(
            [{"from": d, "to": c["id"]}
             for c in claims for d in c["depends_on_claims"]],
            key=lambda e: (e["from"], e["to"]),
        ),
        "validation": validation,
    }
    tick = chr(96)
    lines = [
        "# HYP-105 — pinned mathematical claim index",
        "",
        "**Metadata validation only. No mathematical peer review or theorem "
        "acceptance is implied by this index.**",
        "",
        "Root: [issue #230](https://github.com/" + REPO + "/issues/230) "
        "remains unresolved by the claims recorded here.",
        "",
        "| Claim ID | Logical mode | Status | Pinned source |",
        "|---|---|---|---|",
    ]
    for item in index["claims"]:
        id_ = item["id"]
        lines.append("| " + tick + id_ + tick + " | " + item["mode"] +
                     " | " + item["mathematical_status"] +
                     " | [PR #" + str(item["source_pr"]) + "](" +
                     item["proof_url"] + ") |")
    for item in index["claims"]:
        lines.extend([
            "",
            "## " + item["id"],
            "",
            item["statement"],
            "",
            "**Ordered quantifiers:** " + "; ".join(
                q["op"] + "(" + q["variable"] + ": " + q["domain"] + ")"
                for q in item["quantifiers"]),
            "",
            "**Claim dependencies:** " +
            (", ".join(item["depends_on_claims"]) or "none registered"),
            "",
            "**Cannot conclude:** " + " ".join(item["limitations"]),
            "",
            "**Pinned proof:** [" + item["source_commit"][:12] + "](" +
            item["proof_url"] + ")",
        ])
    return index, "\n".join(lines) + "\n"

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path,
                        default=Path("research/rcp/hyp105"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--verify-sources", action="store_true")
    args = parser.parse_args(argv)
    index, doc = render(args.registry)
    if args.verify_sources:
        index["sources_verified"] = len(verify_pinned_sources(args.registry))
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "claims.json").write_text(
        json.dumps(index, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output / "claims.md").write_text(doc, encoding="utf-8")
    print("RCP-001-B METADATA VALIDATED: %d claims, %d edges, %d unique sources%s" %
          (len(index["claims"]), len(index["dependency_edges"]),
           len({c["source_commit"] for c in index["claims"]}),
           "; source blobs verified" if args.verify_sources else
           "; source blobs NOT INSPECTED"))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        raise SystemExit("RCP-001-B INVALID: " + str(exc)) from exc
