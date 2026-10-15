"""RCP-AA4R-CYC: independent provenance and exact-rational original D6 gates.

The arithmetic checks finite boundary values and source assumptions. They do
not replace the source paper's all-h proof or independent mathematical review.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, perm
from pathlib import Path
import unittest

from research.rcp.claim_registry import read_registry, validate_registry
from research.rcp.evidence_ledger import (
    validate_ledgers, verify_archives, load_ledgers, git_blob_sha, load_pins,
)
from research.rcp.structured_docs import read_formulas, render_all

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
SOURCE_SHA = "53af9d2f03ef4fec147b633558a0e7bb96aea070"
PREFIX = "research/rcp/hyp105/archive/PR480"
IDS = (
    "HYP105-AA4RCYC-D6-QUENCHED-IDENTITY",
    "HYP105-AA4RCYC-D6-QUENCHED-LOWER",
    "HYP105-AA4RCYC-D6-DUAL-QUENCHED-LOWER",
)


def exact_lower(s: int):
    assert s >= 8
    V = (s + 1) * (s * s + 1)
    a = 2
    while comb(a, 2) < V:
        a += 1
    K, m = comb(a, 2), comb(a, 2) - V
    occupied = Fraction(perm(a, 6), 12) - m * perm(a - 2, 4)
    lower = Fraction(perm(a, 6), perm(K, 6)) * occupied * perm(s + 1, 6)
    return a, K, m, occupied, lower


class OriginalD6ImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validation = validate_ledgers(REG)
        cls.models, claims = read_registry(REG)
        cls.claims = {c["id"]: c for c in claims}
        cls.evidence, cls.nogo = load_ledgers(REG)

    def test_001_original_source_immutability_and_sha256(self):
        blobs = verify_archives(REG, ROOT)
        self.assertEqual(len(blobs), len(load_pins(REG)))
        for path in ("proof.md", "oracle.py.txt", "independent_test.py.txt"):
            b = next(x for x in blobs if x["archive"] == PREFIX + "/" + path)
            self.assertEqual(b["source_commit"], SOURCE_SHA)
            self.assertEqual(b["git_blob_sha"],
                             git_blob_sha((ROOT / b["archive"]).read_bytes()))
            self.assertEqual(len(b["sha256"]), 64)

    def test_002_exact_legacy_source_byte_identifiers(self):
        expected = {
            "proof.md": "5f360465a324acd606e632142aa4795c559c0d9a",
            "oracle.py.txt": "ba0d47134dad74bfc8ff9acf7dea8556400c60af",
            "independent_test.py.txt": "582850332c7c1252e3d669e74980625527dbd0ee",
        }
        from hashlib import sha256
        for suffix, blob in expected.items():
            payload = (ROOT / PREFIX / suffix).read_bytes()
            self.assertEqual(git_blob_sha(payload), blob)
            self.assertEqual(sha256(payload).hexdigest(),
                             load_pins(REG)[PREFIX + "/" + suffix])

    def test_003_all_three_claims_have_frozen_exact_source(self):
        for id_ in IDS:
            c = self.claims[id_]
            self.assertEqual(c["source"]["commit"], SOURCE_SHA)
            self.assertEqual(c["source"]["pr"], 480)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "5f360465a324acd606e632142aa4795c559c0d9a")
            self.assertEqual(c["mathematical_status"], "DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"], "NOT_REVIEWED")
            self.assertEqual(c["root_impact"], "ROOT_BRANCHES_OPEN")

    def test_004_quantifier_order_fixed_f_random_one_global_g(self):
        for cid in IDS[:2]:
            c = self.claims[cid]
            self.assertEqual([q["op"] for q in c["quantifiers"]],
                             ["forall", "forall", "expectation"])
            self.assertEqual([q["variable"] for q in c["quantifiers"]],
                             ["h", "f", "g"])
            self.assertIn("COMPLETE", c["quantifiers"][-1]["domain"])
            self.assertEqual(c["mode"], "CONDITIONAL_EXPECTATION")

    def test_005_reverse_quantifiers_are_not_averaged_over_both(self):
        c = self.claims[IDS[2]]
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall", "forall", "expectation"])
        self.assertEqual([q["variable"] for q in c["quantifiers"]],
                         ["h", "g", "f"])
        self.assertEqual(c["depends_on_claims"], [IDS[1]])

    def test_006_original_aa4q_and_internal_dependency_dag(self):
        self.assertEqual(self.claims[IDS[0]]["depends_on_claims"],
                         ["HYP105-AA4Q-SEVEN-ORIGINAL-JOIN"])
        self.assertEqual(self.claims[IDS[1]]["depends_on_claims"], [IDS[0]])
        self.assertEqual(self.claims[IDS[2]]["depends_on_claims"], [IDS[1]])
        validate_registry(REG)

    def test_007_single_same_receipt_covers_three_results(self):
        e = next(x for x in self.evidence if x["id"] == "HYP105-EV-AA4RCYC")
        self.assertEqual(set(e["claim_ids"]), set(IDS))
        self.assertEqual(e["source"]["commit"], SOURCE_SHA)
        self.assertEqual(e["ci"]["status"], "NOT_ARCHIVED_AS_PROOF")
        self.assertEqual(e["reproduction"]["execution_status"],
                         "COMMAND_DOCUMENTED_NOT_EXECUTED_BY_RCP_C")

    def test_008_scoped_no_go_does_not_refute_seven_class_root(self):
        n = next(x for x in self.nogo if x["id"] ==
                 "HYP105-NG-AA4RCYC-QUENCHED-NOT-POINTWISE")
        self.assertEqual(set(n["related_claim_ids"]), set(IDS))
        self.assertEqual(n["kind"], "INVALID_INFERENCE")
        self.assertEqual(n["root_status"], "OPEN_WITH_FORMAL_BLOCKER")
        self.assertTrue(any("universal" in x.lower()
                            for x in n["does_not_refute"]))

    def test_009_minimal_alphabet_and_missing_edge_bound(self):
        for s in (8, 16, 32, 64, 128, 256, 512):
            a, K, m, C, lower = exact_lower(s)
            self.assertGreaterEqual(K, (s + 1) * (s*s + 1))
            self.assertLess(comb(a - 1, 2), (s + 1) * (s*s + 1))
            self.assertLessEqual(m, a - 2)
            self.assertGreater(C, 0)
            self.assertGreater(lower, 0)

    def test_010_exact_all_finite_boundaries_ge_one_eighth(self):
        for s in (8, 16, 32, 64, 128):
            with self.subTest(s=s):
                _, _, _, _, lower = exact_lower(s)
                self.assertGreaterEqual(lower, Fraction(s**6, 8))
                self.assertGreater(lower, Fraction(s**6, 2))

    def test_011_exact_asymptotic_regime_checks_not_a_proof(self):
        for s in (256, 512, 1024):
            _, _, _, _, lower = exact_lower(s)
            self.assertGreaterEqual(lower, Fraction(s**6, 8))
            self.assertLess(lower / s**6, Fraction(16, 3))
        # This is only a finite sanity check. The source proof provides the
        # uniform analytical argument for ALL h>=8.

    def test_012_exact_connected_C6_probability_W32(self):
        a, K = 6, 15
        self.assertEqual(Fraction(perm(a, 6), perm(K, 6)),
                         Fraction(1, 5005))
        self.assertEqual(perm(a, 6)//12, 60)
        self.assertEqual(perm(a - 2, 4), 24)

    def test_013_four_formula_ids_scoped_to_proof(self):
        formulas = read_formulas(REG, set(self.claims))
        picked = {f["id"]: f for f in formulas
                  if f["id"] in {"HYP105-F-010", "HYP105-F-011",
                                 "HYP105-F-012", "HYP105-F-013"}}
        self.assertEqual(len(picked), 4)
        self.assertIn("N_{", picked["HYP105-F-010"]["latex"])
        self.assertIn("1", picked["HYP105-F-012"]["latex"])
        self.assertEqual(picked["HYP105-F-013"]["claim_ids"], [IDS[2]])

    def test_014_generated_math_docs_expose_proof_and_expectation(self):
        docs = render_all(REG)
        for name in ("RESULTS.md", "FORMULAS.md", "PROOF-GRAPH.md",
                     "RESEARCH-MATRIX.md"):
            self.assertIn("HYP105-AA4RCYC", "\n".join(
                docs[k] for k in ("RESULTS.md", "PROOF-GRAPH.md")))
            self.assertTrue(docs[name])
        self.assertIn("\\mathbb E_g", docs["FORMULAS.md"])
        self.assertIn("min_(f,g)", docs["RESULTS.md"])

    def test_015_ledger_counts_without_arbitrary_upper_limit(self):
        self.assertGreaterEqual(self.validation["claim_count"], 12)
        self.assertGreaterEqual(self.validation["evidence_count"], 7)
        self.assertGreaterEqual(self.validation["archived_blob_count"], 26)
        self.assertGreaterEqual(self.validation["no_go_count"], 7)


if __name__ == "__main__":
    unittest.main()
