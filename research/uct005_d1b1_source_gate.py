#!/usr/bin/env python3
"""UCT-005 D1-B1: audited source identities and strict GF2 interval-reduction barrier.

This certifies only a small *query-interface* algebraic fact, not a dynamic
cell-probe lower bound, authenticated security proof or source theorem transfer.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/research/UCT-005-G3-B2-D1B1-TRANSFER-MATRIX.json"
CATALOG = ROOT / "docs/research/catalog/literature.json"
F1 = ROOT / "docs/research/UCT-005-G3-B2-D1B0-F1-MODEL.json"
IDS = frozenset({68, 111, 112, 119, 156, 157, 158, 159, 199, 200,
                 349, 350, 351, 352, 353, 354, 355, 356, 358, 359})
ALLOWED = {"CLASSICAL_SUBTASK_ONLY", "REDUCTION_REQUIRED",
           "SECURITY_NONTRANSFER", "CONDITIONAL_UPPER", "METHOD_ONLY"}


def validate_matrix() -> dict:
    doc = json.loads(MATRIX.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    f1 = json.loads(F1.read_text(encoding="utf-8"))
    if doc["schema"] != "mathlab.uct005.d1b1.transfer-matrix.v1":
        raise ValueError("unrecognized D1-B1 source matrix")
    if doc["root_novelty"] != f1["root_novelty"] != "OPEN_UNPROVED":
        raise ValueError("false theorem promotion")
    if not doc["no_source_full_proof_rederived"]:
        raise ValueError("source proof verification falsely implied")
    actual = {x["id"] for x in doc["entries"]}
    expected = {f"LIT-{i:03d}" for i in IDS}
    if actual != expected or len(doc["entries"]) != len(expected):
        raise ValueError("canonical source cohort mismatch")
    indexed = {e["id"]: e for e in catalog["entries"]}
    for row in doc["entries"]:
        baseline = indexed[row["id"]]
        for field in ("identity", "title", "primary_url"):
            if row[field] != baseline[field]:
                raise ValueError(f"{row['id']} mismatched canonical {field}")
        if row["transfer"] not in ALLOWED:
            raise ValueError("unqualified source-to-F1 transfer")
        if row["proof_verified"] or not row["barrier"] or not row["missing_proof"]:
            raise ValueError("unsupported mathematical claim")
        if row["source_evidence"] not in {
                "ABSTRACT_ONLY", "ABSTRACT_PLUS_SECONDARY_THEOREM",
                "THEOREM_STATEMENT_PRIMARY", "PRIMARY_FULLTEXT_SCOPE_CHECKED"}:
            raise ValueError("unknown primary audit level")
    if not {"LIT-112", "LIT-119", "LIT-159"} <= set(
            doc["primary_theorem_statement_checked"]):
        raise ValueError("missing theorem-statement-level inspections")
    by_id = {e["id"]: e for e in doc["entries"]}
    if by_id["LIT-119"]["transfer"] != "REDUCTION_REQUIRED":
        raise ValueError("Multiphase confusion")
    if "proof-binding" not in by_id["LIT-159"]["barrier"]:
        raise ValueError("Tas-Boneh proof-binding assumption was dropped")
    if by_id["LIT-359"]["transfer"] != "METHOD_ONLY":
        raise ValueError("static CSP wrongly promoted to dynamic F1")
    return doc


def interval_run_decomposition(mask: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Minimum number of original-coordinate half-open parity interval XORs.

    Each interval introduces <=2 boundary flips, while mask with r maximal
    nonzero runs has exactly 2r boundary flips (padded by zero at both ends).
    Thus >=r intervals; the maximal-run decomposition achieves r. No coding,
    dimension blow-up, cross-epoch preprocessing or adaptive multiquery allowed.
    """
    if not mask or any(v not in (0, 1) for v in mask):
        raise ValueError("expected a nonempty GF2 mask")
    starts = []
    for i, value in enumerate(mask):
        if value and (i == 0 or not mask[i-1]):
            starts.append(i)
        if value and (i + 1 == len(mask) or not mask[i+1]):
            starts[-1] = (starts[-1], i + 1)
    return tuple(starts)


def query_mask_from_intervals(n: int, intervals: tuple[tuple[int, int], ...]):
    out = [0] * n
    for lo, hi in intervals:
        if not 0 <= lo < hi <= n:
            raise ValueError("invalid interval")
        for i in range(lo, hi):
            out[i] ^= 1
    return tuple(out)


def original_coordinate_interface_gap(n: int) -> dict:
    if n < 3:
        raise ValueError("n>=3 required for strict nonzero-mask count gap")
    arbitrary_nonzero_masks = (1 << n) - 1
    contiguous_interval_masks = n * (n+1) // 2
    assert arbitrary_nonzero_masks > contiguous_interval_masks
    hard = tuple(int(i % 2 == 0) for i in range(n))
    k = len(interval_run_decomposition(hard))
    return {
        "n": n, "arbitrary_nonzero_GF2_query_masks": arbitrary_nonzero_masks,
        "single_contiguous_interval_masks": contiguous_interval_masks,
        "alternating_mask_min_original_coordinate_intervals": k,
        "scope": "same-coordinate XOR of independent interval queries only",
        "cannot_rule_out": "clever encodings, reductions changing n, or other data structures",
        "root": "OPEN_UNPROVED",
    }


def report() -> dict:
    d = validate_matrix()
    return {
        "status": "PARTIAL_THEOREM_STATEMENT_AUDIT_NO_FULL_SOURCE_PROOFS",
        "transfer_counts": dict(Counter(e["transfer"] for e in d["entries"])),
        "interface_counterexample": original_coordinate_interface_gap(9),
        "root": d["root_novelty"],
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
