#!/usr/bin/env python3
"""Fail-closed metadata consistency checks for Mathlab active research.

This is NOT a theorem prover, a live GitHub issue/CI auditor, or a
cryptographic/security proof. Existing scientific documents remain authoritative.
Only Python's standard library is needed by the GitHub-hosted Research workflow.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/research/RESEARCH-STATUS-REGISTRY.json"
SCHEMA = ROOT / "docs/research/RESEARCH-STATUS-REGISTRY.schema.json"
DASHBOARD = ROOT / "docs/research/RESEARCH-STATUS.md"
TREE = ROOT / "docs/research/UCT-005-THEOREM-TREE.json"
F1 = ROOT / "docs/research/UCT-005-G3-B2-D1B0-F1-MODEL.json"
G4 = ROOT / "docs/research/UCT-005-G4-TYPED-BRIDGES.json"
KNOWN = ROOT / "docs/research/KNOWN-AND-STOPPED-RESEARCH.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
ID = re.compile(r"^[A-Z0-9-]+$")
CI_RUN = re.compile(r"^https://github.com/definitely-stable/Mathlab/actions/runs/[0-9]+$")
ROOT_FIELDS = frozenset({
    "schema", "as_of", "baseline_main_sha", "authority", "root_id",
    "programs", "dependencies", "typed_edges",
})
PROGRAM_FIELDS = frozenset({
    "id", "owner_issue", "parent", "scientific_status", "workflow_status",
    "proof_grade", "novelty_status", "source_audit_grade", "model_id",
    "artifact_paths", "evidence", "last_verified_sha", "ci",
    "next_falsifier", "reopen_rule",
})
EDGE_STATUSES = {
    "REDUCTION_REQUIRED": "UNPROVED",
    "UPPER_CONSTRUCTION_PENDING": "UNVERIFIED",
    "APPLICATION_ONLY": "NO_THEOREM_TRANSFER",
    "MODEL_COMPARISON_ONLY": "NO_THEOREM_TRANSFER",
    "COUNTERMODEL": "FALSE_TRANSFER",
    "PROOF_INGREDIENT": "CLASSICAL_RESTRICTED",
}


def _require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError(reason)


def _json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def _enum(schema: dict, field: str) -> set[str]:
    return set(schema["$defs"]["program"]["properties"][field]["enum"])


def _safe_file(relative: str, root: Path) -> None:
    _require(isinstance(relative, str), "artifact path must be a string")
    path = PurePosixPath(relative)
    _require(not path.is_absolute() and ".." not in path.parts
             and path.parts and path.parts[0] in {"docs", "research", "lean", "preprints"}
             and not relative.startswith("./") and "\\" not in relative,
             f"unsafe artifact path: {relative}")
    _require((root / relative).is_file(), f"missing evidence/artifact: {relative}")


def _acyclic(vertices: set[str], edges: list[tuple[str, str]], label: str) -> None:
    adjacency = {node: [] for node in vertices}
    for src, dst in edges:
        _require(src in vertices and dst in vertices, f"{label}: dangling endpoint")
        _require(src != dst, f"{label}: self-loop at {src}")
        adjacency[src].append(dst)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            raise ValueError(f"{label}: directed cycle at {node}")
        if node in visited:
            return
        visiting.add(node)
        for next_node in adjacency[node]:
            visit(next_node)
        visiting.remove(node)
        visited.add(node)

    for node in sorted(vertices):
        visit(node)


def validate_registry(data: dict, root: Path = ROOT) -> None:
    """Validate local metadata and typed dependencies, not mathematical truth."""
    schema = _json(root / "docs/research/RESEARCH-STATUS-REGISTRY.schema.json")
    _require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
             "JSON Schema version drift")
    _require(isinstance(data, dict) and set(data) == ROOT_FIELDS,
             "registry root keys mismatch")
    _require(data["schema"] == schema["properties"]["schema"]["const"],
             "registry schema mismatch")
    _require(isinstance(data["as_of"], str), "invalid review date")
    try:
        date.fromisoformat(data["as_of"])
    except ValueError as exc:
        raise ValueError("invalid review date") from exc
    _require(isinstance(data["baseline_main_sha"], str)
             and SHA.fullmatch(data["baseline_main_sha"]) is not None,
             "invalid baseline SHA")
    _require(isinstance(data["authority"], str)
             and "not establish proof" in data["authority"].lower(),
             "authority must disclaim proof")
    _require(data["root_id"] == "UCT-005-ROOT", "wrong central research root")
    programs = data["programs"]
    _require(isinstance(programs, list) and programs, "no programs")
    ids: set[str] = set()
    by_id: dict[str, dict] = {}
    for record in programs:
        _require(isinstance(record, dict) and set(record) == PROGRAM_FIELDS,
                 "program field set mismatch")
        key = record["id"]
        _require(isinstance(key, str) and ID.fullmatch(key) is not None,
                 f"invalid program id: {key}")
        _require(key not in ids, f"duplicate program id: {key}")
        ids.add(key)
        by_id[key] = record
        _require(type(record["owner_issue"]) is int and record["owner_issue"] > 0,
                 f"{key}: invalid GitHub issue number")
        for field in ("scientific_status", "workflow_status", "proof_grade",
                      "novelty_status", "source_audit_grade"):
            _require(record[field] in _enum(schema, field),
                     f"{key}: invalid {field}")
        _require(record["model_id"] is None or
                 isinstance(record["model_id"], str) and len(record["model_id"]) >= 3,
                 f"{key}: invalid model id")
        for field in ("artifact_paths", "evidence"):
            values = record[field]
            _require(isinstance(values, list) and bool(values)
                     and len(set(values)) == len(values),
                     f"{key}: empty/duplicate {field}")
            for relative in values:
                _safe_file(relative, root)
        _require(isinstance(record["last_verified_sha"], str)
                 and SHA.fullmatch(record["last_verified_sha"]) is not None,
                 f"{key}: invalid last verified SHA")
        for field in ("next_falsifier", "reopen_rule"):
            _require(isinstance(record[field], str) and len(record[field]) >= 20,
                     f"{key}: missing {field}")
        ci = record["ci"]
        _require(isinstance(ci, dict) and set(ci) == {"status", "head_sha", "run_url"},
                 f"{key}: invalid CI fields")
        _require(ci["status"] in {"NOT_CHECKED", "SUCCESS", "FAILURE"},
                 f"{key}: invalid CI status")
        if ci["status"] == "NOT_CHECKED":
            _require(ci["head_sha"] is None and ci["run_url"] is None,
                     f"{key}: unchecked CI must not imply a run")
        else:
            _require(isinstance(ci["head_sha"], str)
                     and SHA.fullmatch(ci["head_sha"]) is not None
                     and ci["head_sha"] == record["last_verified_sha"],
                     f"{key}: CI result must match exact reviewed SHA")
            _require(isinstance(ci["run_url"], str)
                     and CI_RUN.fullmatch(ci["run_url"]) is not None,
                     f"{key}: CI result needs exact run URL")
        if record["proof_grade"] == "FORMAL_CHECKED":
            _require(any(path.startswith("lean/") for path in record["evidence"]),
                     f"{key}: formal proof needs Lean evidence")
        if record["scientific_status"] == "OPEN_UNPROVED":
            _require(record["proof_grade"] != "FORMAL_CHECKED",
                     f"{key}: open root cannot claim a formal proof")
    _require(data["root_id"] in ids, "root id is missing")
    _require(by_id["UCT-005-ROOT"]["scientific_status"] == "OPEN_UNPROVED"
             and by_id["UCT-005-ROOT"]["proof_grade"] == "NONE"
             and by_id["UCT-005-ROOT"]["owner_issue"] == 105,
             "UCT-005 root novelty/proof promotion is forbidden")
    _require("UCT-005-F1" in ids and "UCT-005-G4" in ids,
             "required F1/G4 programs missing")
    _require(by_id["UCT-005-F1"]["owner_issue"] == 223
             and by_id["UCT-005-F1"]["scientific_status"] == "OPEN_UNPROVED",
             "F1 owner or scientific status drift")
    _require(by_id["UCT-005-G4"]["owner_issue"] == 234
             and by_id["UCT-005-G4"]["scientific_status"] == "CLASSICAL_RESTRICTED",
             "G4 is an atlas, not a new root theorem")
    parents: list[tuple[str, str]] = []
    for record in programs:
        parent = record["parent"]
        if parent is not None:
            _require(isinstance(parent, str), "parent must be an ID or null")
            parents.append((record["id"], parent))
    _acyclic(ids, parents, "organizational parent")
    dependencies = data["dependencies"]
    _require(isinstance(dependencies, list), "dependencies must be a list")
    dependency_pairs: list[tuple[str, str]] = []
    for dep in dependencies:
        _require(isinstance(dep, dict) and set(dep) == {"from", "to"},
                 "dependency fields mismatch")
        pair = (dep["from"], dep["to"])
        _require(pair not in dependency_pairs, "duplicate dependency")
        dependency_pairs.append(pair)
    _acyclic(ids, dependency_pairs, "logical prerequisites")
    edges = data["typed_edges"]
    _require(isinstance(edges, list), "typed_edges must be a list")
    edge_ids: set[tuple[str, str, str]] = set()
    for edge in edges:
        _require(isinstance(edge, dict)
                 and set(edge) == {"source", "target", "kind", "status", "evidence"},
                 "typed edge fields mismatch")
        src, dst, kind = edge["source"], edge["target"], edge["kind"]
        _require(src in ids and dst in ids and src != dst, "dangling/self typed edge")
        _require(kind in EDGE_STATUSES and edge["status"] == EDGE_STATUSES[kind],
                 "unproved transfer promoted or invalid edge kind")
        identity = (src, dst, kind)
        _require(identity not in edge_ids, "duplicate typed edge")
        edge_ids.add(identity)
        _safe_file(edge["evidence"], root)
    tree = _json(root / "docs/research/UCT-005-THEOREM-TREE.json")
    model = _json(root / "docs/research/UCT-005-G3-B2-D1B0-F1-MODEL.json")
    atlas = _json(root / "docs/research/UCT-005-G4-TYPED-BRIDGES.json")
    known = _json(root / "docs/research/KNOWN-AND-STOPPED-RESEARCH.json")
    _require(tree["root"] == "UCT005" and tree["root_novelty"] == "OPEN_UNPROVED",
             "canonical theorem-tree root differs")
    _require(next(x["status"] for x in tree["nodes"] if x["id"] == "UCT005")
             == "OPEN_UNPROVED", "theorem-tree node falsely promoted")
    _require(model["schema"] == "mathlab.uct005.d1b0.f1.v1"
             and model["root_novelty"] == "OPEN_UNPROVED"
             and model["parent_issue"] == 223, "F1 model drift")
    _require(by_id["UCT-005-F1"]["model_id"] == model["schema"],
             "F1 model ID mismatch")
    for key, issue, parent, scientific in (
        ("UCT-005-COW", 244, "UCT-005-F1", "MODEL_ONLY"),
        ("UCT-005-PIN-BITMAP", 252, "UCT-005-F1", "MODEL_ONLY"),
        ("UCT-005-ALLOCATOR", 254, "UCT-005-COW", "MODEL_ONLY"),
        ("UCT-005-PIN-TRUST", 255, "UCT-005-F1", "OPEN_UNPROVED"),
    ):
        _require(key in by_id and by_id[key]["model_id"] == model["schema"],
                 f"{key}: incompatible or absent F1 model")
        _require(by_id[key]["owner_issue"] == issue
                 and by_id[key]["parent"] == parent
                 and by_id[key]["scientific_status"] == scientific,
                 f"{key}: owner, parent or scientific status drift")
    _require(atlas["status"] == "EVIDENCE_TYPED_ATLAS_NOT_ROOT_THEOREM"
             and atlas["owner_issue"] == 234 and atlas["root_issue"] == 105,
             "G4 atlas scope drift")
    _require(known["schema"] == "mathlab.known-and-stopped-research.v1",
             "known-work registry missing")
    _require(len({x["id"] for x in known["entries"]}) == len(known["entries"]),
             "duplicate known-work record")


def render_dashboard(data: dict) -> str:
    lines = [
        "# Mathlab active research — checked metadata snapshot",
        "",
        "This page is generated by `python research/research_status_registry.py --write`.",
        "It is NOT live GitHub issue/PR/CI status and NOT a mathematical proof.",
        f"Review date: `{data['as_of']}`. Main baseline: `{data['baseline_main_sha']}`.",
        "",
        "| Program | Scientific status | Proof grade | Workflow snapshot | Owner issue |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in data["programs"]:
        issue = item["owner_issue"]
        lines.append(
            f"| `{item['id']}` | `{item['scientific_status']}` | "
            f"`{item['proof_grade']}` | `{item['workflow_status']}` | "
            f"[#{issue}](https://github.com/definitely-stable/Mathlab/issues/{issue}) |"
        )
    lines.extend([
        "",
        "The canonical scientific authority remains "
        "[UCT-005 theorem tree](UCT-005-THEOREM-TREE.json), "
        "[F1 model](UCT-005-G3-B2-D1B0-F1-MODEL.json), "
        "[G4 typed bridges](UCT-005-G4-TYPED-BRIDGES.json), and "
        "[known/stopped register](KNOWN-AND-STOPPED-RESEARCH.json).",
        "Existing [live navigation](../STATUS-LIVE.md) provides GitHub-hosted "
        "CI/PR links; no exact-head CI success is inferred here.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="regenerate status dashboard after validation")
    parser.add_argument("--check", action="store_true",
                        help="validate registry and require generated dashboard to match")
    args = parser.parse_args()
    data = _json(REGISTRY)
    try:
        validate_registry(data)
        expected = render_dashboard(data)
        if args.write:
            DASHBOARD.write_text(expected, encoding="utf-8")
        else:
            _require(DASHBOARD.is_file()
                     and DASHBOARD.read_text(encoding="utf-8") == expected,
                     "generated status dashboard drift; run --write")
    except (ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"research-status FAIL: {exc}\n")
    print(f"research-status PASS: {len(data['programs'])} programs, "
          f"{len(data['dependencies'])} prerequisite edges, "
          f"{len(data['typed_edges'])} non-implication typed edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
