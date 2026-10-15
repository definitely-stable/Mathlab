"""RCP-001-E: reproducible committed Markdown mathematical research registers.

Source of truth is pinned claim/model/formula/evidence/no-go JSON and original proofs.
The rendered Markdown is navigation, not mathematical acceptance.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
from research.rcp.claim_registry import (
    REPO, RegistryError, read_registry, validate_registry, parse_json, nonblank
)
from research.rcp.evidence_ledger import validate_ledgers, load_ledgers
from research.rcp.proof_impact import proof_graph, compatibility_review

FORMULA_SCHEMA = "mathlab.rcp.formula-catalog.v1"
DOC_PATH = Path("docs/research/hyp105/registry")
FILENAMES = ("RESULTS.md", "FORMULAS.md", "PROOF-GRAPH.md",
             "PROTOCOLS.md", "RESEARCH-MATRIX.md")


def read_formulas(root, ids):
    data = parse_json(root / "formulas.json")
    if not isinstance(data, dict) or data.get("schema") != FORMULA_SCHEMA or \
            data.get("program") != "HYP-105" or data.get("root_issue") != 230:
        raise RegistryError("invalid formula catalog")
    values = data.get("formulas")
    if not isinstance(values, list) or not values:
        raise RegistryError("empty formula catalog")
    seen = set()
    for f in values:
        fid = f.get("id") if isinstance(f, dict) else None
        if not isinstance(fid, str) or not re.fullmatch(r"HYP105-F-[0-9]+", fid) or fid in seen:
            raise RegistryError("duplicate/invalid formula id")
        seen.add(fid)
        linked = f.get("claim_ids")
        if not isinstance(linked, list) or not linked or \
                len(set(linked)) != len(linked) or any(i not in ids for i in linked):
            raise RegistryError(fid + " missing or unknown scoped claim")
        for fld in ("title", "latex", "scope", "not_implies"):
            if not nonblank(f.get(fld)):
                raise RegistryError(fid + " missing " + fld)
        if len(f["latex"]) > 3000 or "\n"+chr(96)*3 in f["latex"] or \
                "\\begin{document}" in f["latex"]:
            raise RegistryError(fid + " unsafe/overlong mathematical expression")
    return sorted(values, key=lambda x: x["id"])


def link(c):
    source = c["source"]
    url = "https://github.com/" + REPO + "/blob/" + \
          source["commit"] + "/" + source["proof_path"]
    return "[PR #" + str(source["pr"]) + " @ " + source["commit"][:12] + "](" + url + ")"


def ordered_quantifiers(c):
    return " ; ".join(q["op"] + " " + q["variable"] +
                      " (" + q["domain"] + ")" for q in c["quantifiers"])


def header():
    return [
        "> Generated from pinned research registries; do not edit by hand.",
        "> DOCUMENTED_IN_DRAFT is not independently reviewed/proven mathematics.",
        "> HYP-105 issue [#230](https://github.com/" + REPO +
        "/issues/230) remains unresolved by these registered results.",
        "> GitHub PR HEAD and CI are live data; none are hardcoded here.",
        "",
    ]


def render_all(root):
    root = Path(root)
    validate_registry(root)
    validate_ledgers(root)
    models, claims = read_registry(root)
    claims.sort(key=lambda c: c["id"])
    cby = {c["id"]: c for c in claims}
    evidence, no_go = load_ledgers(root)
    formulas = read_formulas(root, set(cby))
    evidence.sort(key=lambda x: x["id"])
    no_go.sort(key=lambda x: x["id"])

    r = ["# HYP-105 — Registered Research Results", ""] + header() + [
        "## Coverage and acceptance", "",
        "The table indexes **%d specific results** from **%d research PRs**. "
        "It does not claim to catalog all open HYP-105 research PRs." %
        (len(claims), len({c["source"]["pr"] for c in claims})),
        "",
        "| Stable claim | Scope / logical mode | Mathematical status | Pinned proof |",
        "|---|---|---|---|",
    ]
    for c in claims:
        r.append("| " + c["id"] + " | " + c["mode"] + " | " +
                 c["mathematical_status"] + " | " + link(c) + " |")
    r.extend(["", "## Mathematical statements (registered subset)"])
    for c in claims:
        r.extend(["", "### " + c["id"] + " — " + c["title"], "",
                  "**Claim:** " + c["statement"], "",
                  "**Ordered quantifiers:** " + ordered_quantifiers(c), "",
                  "**Model IDs:** " + ", ".join(c["model_ids"]), "",
                  "**Claim dependencies:** " +
                  (", ".join(c["depends_on_claims"]) or "none registered"), "",
                  "**Proof provenance:** " + link(c), "",
                  "**Review:** " + c["review_status"] +
                  "; novelty: " + c["novelty_status"], "",
                  "**Does not imply:** " + " ".join(c["limitations"]), ""])
    r.extend(["", "## Sources and remaining obligations", "",
              "The proof is the pinned original source, not this index. "
              "Branch A/B/C requires separate uniform or counterfamily proof.", ""])

    f = ["# HYP-105 — Formula Catalog", ""] + header() + [
        "Formula excerpts retain their original scoped quantifiers. "
        "Do not remove an expectation operator or silently generalize.",
        "",
    ]
    for x in formulas:
        parents = [cby[i] for i in x["claim_ids"]]
        f.extend(["## " + x["id"] + " — " + x["title"], "",
                  "\\[", x["latex"], "\\]", "",
                  "**Applies under:** " + x["scope"], "",
                  "**Cannot conclude:** " + x["not_implies"], "",
                  "**Linked claim:** " + ", ".join(x["claim_ids"]), "",
                  "**Pinned source:** " + "; ".join(link(c) for c in parents), ""])
    f.extend(["## Formula review protocol", "",
              "Verify original six-incidence constraints, alphabet, all-h "
              "range, global injection semantics, and quantifier order "
              "against the cited proof commit. CI does not mechanically "
              "check the algebra.", ""])

    refs = [{"id": c["id"], "depends_on_claims": c["depends_on_claims"],
             "model_ids": c["model_ids"], "quantifiers": c["quantifiers"],
             "mode": c["mode"]} for c in claims]
    synthetic = {"research": {"claims": refs, "models": models}}
    _, _, edges = proof_graph(synthetic)
    flags = compatibility_review(synthetic)
    g = ["# HYP-105 — Proof Dependency Graph", ""] + header() + [
        "Only explicitly registered edges are included. An unregistered "
        "historical proof can remain an essential external dependency.", "",
        "| Prerequisite claim | Dependent claim |",
        "|---|---|",
    ]
    for e in edges:
        g.append("| " + e["parent"] + " | " + e["dependent"] + " |")
    g.extend(["", "## Explicit external proof inputs"])
    for c in claims:
        g.extend(["", "### " + c["id"], ""])
        for ext in c["external_dependencies"]:
            g.append("- " + ext)
    g.extend(["", "## Scope-review flags (not proven contradictions)", ""])
    if not flags:
        g.append("No metadata-level scope-review flags.")
    for z in flags:
        g.append("- **" + z["kind"] + "**: " + z["parent"] + " -> " +
                 z["dependent"] + ". " + z["reason"])
    g.extend(["", "A model difference is not itself a contradiction. "
              "Review the original proof or record a valid reduction.", ""])

    m = ["# HYP-105 — Research Matrix", ""] + header() + [
        "| Result | Quantifier mode | Evidence receipt | Applicable models | Main caution |",
        "|---|---|---|---|---|",
    ]
    by_claim = {c["id"]: [] for c in claims}
    for e in evidence:
        for cid in e["claim_ids"]:
            by_claim[cid].append(e["id"])
    for c in claims:
        m.append("| " + c["id"] + " | " + c["mode"] + " | " +
                 ", ".join(sorted(by_claim[c["id"]])) + " | " +
                 ", ".join(c["model_ids"]) + " | " +
                 c["limitations"][0].replace("|", "\\|") + " |")
    m.extend(["", "## Negative knowledge and exact reopening condition", "",
              "| No-go ID | Rejected inference | Revisit only if |",
              "|---|---|---|"])
    for n in no_go:
        m.append("| " + n["id"] + " | " +
                 n["rejected_inference"].replace("|", "\\|") + " | " +
                 n["reopen_only_if"].replace("|", "\\|") + " |")
    m.extend(["", "## Coverage warning", "",
              "This matrix covers the registered pilot results, not the "
              "entire HYP-105 research corpus.", ""])

    p = ["# HYP-105 — Research Protocols & Acceptance Gates", ""] + header() + [
        "## Mathematical and operational sources", "",
        "| Layer | Source of truth | Acceptance boundary |",
        "|---|---|---|",
        "| Original mathematics | Root #230 and commit-pinned proof documents | Separate mathematical review |",
        "| Claims | research/rcp/hyp105/claims/*.json | Metadata-valid only |",
        "| Formulas | research/rcp/hyp105/formulas.json and cited proof | Not mechanically algebra-verified |",
        "| Evidence | research/rcp/hyp105/evidence and archive/ | Git blob SHA and SHA-256 |",
        "| No-go | research/rcp/hyp105/no_go | Scoped inference blockers only |",
        "| Live state | GitHub PRs, issues and SHA checks | Non-atomic observation |",
        "| Impact | research/rcp/proof_impact.py | Review candidates, not contradictions |",
        "", "## Reproduce and validate", "",
        "```bash",
        "python -m unittest research.test_rcp_proof_impact -v",
        "python -m research.rcp.structured_docs --check",
        "python -m research.rcp.evidence_ledger --output /tmp/hyp105-evidence",
        "GITHUB_TOKEN=... python -m research.rcp.context_builder --output /tmp/hyp105-live --check-claim-prs",
        "python -m research.rcp.proof_impact --snapshot /tmp/hyp105-live/snapshot.json --output /tmp/hyp105-impact",
        "```",
        "", "## Update process", "",
        "1. Update the pinned mathematical claim and evidence only after "
        "auditing exact source provenance; green CI does not promote the claim.",
        "2. Record formulas with full scope, model, quantifiers and non-implications.",
        "3. Maintain precise no-go scope and reopening conditions.",
        "4. Regenerate these Markdown files using "
        "`python -m research.rcp.structured_docs --write`; CI checks "
        "`--check` to prevent drift.",
        "5. Compare snapshots and review changed proofs and all downstream claims.",
        "6. Integrate infrastructure PRs from ancestor to descendant only "
        "after review; no automated merge.",
        "", "## Hard boundaries", "",
        "No averaging-to-adversarial-minimum inference, local-to-global "
        "transfer, W32-to-all-h promotion, or conflation of CI and proofs.",
        "No cap on claim count, PR count or stack depth.", "",
    ]
    result = [r, f, g, p, m]
    return dict(zip(FILENAMES, ("\n".join(v) + "\n" for v in result)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--registry", type=Path,
                    default=Path("research/rcp/hyp105"))
    ap.add_argument("--destination", type=Path, default=DOC_PATH)
    action = ap.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    docs = render_all(args.registry)
    if args.write:
        args.destination.mkdir(parents=True, exist_ok=True)
        for name, content in docs.items():
            (args.destination / name).write_text(content, encoding="utf-8")
    else:
        for name, expected in docs.items():
            path = args.destination / name
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                raise RegistryError("stale structured Markdown register: " + str(path))
    print("RCP-001-E structured Markdown %s: %d files" %
          ("WRITTEN" if args.write else "VERIFIED", len(docs)))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as err:
        raise SystemExit("RCP-001-E INVALID: " + str(err)) from err
