"""RCP-AA4T: independent scoped provenance, integer/rational and review-boundary tests.

These metadata/finite-arithmetic oracles do not independently prove the
source author's infinite all-h analytical argument.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from math import comb, perm
from pathlib import Path
import unittest

from research.rcp.claim_registry import validate_registry, read_registry
from research.rcp.evidence_ledger import (
    validate_ledgers, verify_archives, load_ledgers, load_pins, git_blob_sha,
)
from research.rcp.structured_docs import read_formulas, render_all

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
COMMIT = "c51448b4e47b17737285ef8e6b7ea09991a8c289"
PREFIX = "research/rcp/hyp105/archive/PR484/"
TENSOR = "HYP105-AA4T-POSITIONAL-D6-TENSOR"
IDENTITY = "HYP105-AA4T-QUENCHED-TENSOR-IDENTITY"
LOWER = "HYP105-AA4T-ALLH-QUENCHED-D6-LOWER"
DUAL = "HYP105-AA4T-ALLH-DUAL-QUENCHED-LOWER"
W32 = "HYP105-AA4T-W32-POSITIVE-MEAN-ZERO-D6"
CLAIMS = (TENSOR, IDENTITY, LOWER, DUAL, W32)


def exact_certificate(s):
    assert s >= 2 and (s & (s - 1)) == 0
    V = (s+1)*(s*s+1)
    a = 6
    while comb(a, 2) < V:
        a += 1
    K = comb(a, 2)
    m = K - V
    d = s + 1
    occupied = perm(a, 6)//12 - m*perm(a-2, 4)
    matching = perm(d, 6) if d >= 6 else 1
    probability = Fraction(perm(a, 6), perm(K, 6))
    return {"s":s, "a":a, "K":K, "V":V, "m":m,
            "occupied":occupied, "matching":matching,
            "probability":probability,
            "expected_lower":probability*occupied*matching}


class PositionalD6ImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validation = validate_ledgers(REG)
        _, entries = read_registry(REG)
        cls.by_id = {x["id"]: x for x in entries}
        cls.evidence, cls.nogos = load_ledgers(REG)

    def test_01_pinned_original_three_git_blobs_and_sha256(self):
        expected = {
            "proof.md": "7d19b0f32e6fa8d7d57f324c826c0b84d1ce9780",
            "oracle.py.txt": "03661875ce183dc75ccfd392e89dbf70badce15c",
            "independent_test.py.txt": "6af233091497a2095f2615f227aaa57dde3f2f7c",
        }
        pins=load_pins(REG)
        scanned={r["archive"]:r for r in verify_archives(REG, ROOT)}
        self.assertEqual(set(scanned),set(pins))
        for name, blob in expected.items():
            with self.subTest(archive=name):
                path=PREFIX+name
                payload=(ROOT/path).read_bytes()
                self.assertEqual(git_blob_sha(payload),blob)
                self.assertEqual(sha256(payload).hexdigest(),pins[path])
                self.assertEqual(scanned[path]["source_commit"],COMMIT)

    def test_02_five_claims_all_source_pinned_and_not_promoted(self):
        for name in CLAIMS:
            c=self.by_id[name]
            self.assertEqual(c["source"]["pr"],484)
            self.assertEqual(c["source"]["commit"],COMMIT)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "7d19b0f32e6fa8d7d57f324c826c0b84d1ce9780")
            self.assertEqual(c["mathematical_status"],"DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"],"NOT_REVIEWED")
            self.assertEqual(c["novelty_status"],"NOT_ASSESSED")
            self.assertEqual(c["root_impact"],"ROOT_BRANCHES_OPEN")

    def test_03_positional_identity_is_deterministic_every_f_g(self):
        c=self.by_id[TENSOR]
        self.assertEqual(c["mode"],"ALL_H_IDENTITY")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall","forall"])
        self.assertIn("60 labelled",c["statement"])
        self.assertIn("SAME original",c["quantifiers"][1]["domain"])

    def test_04_one_complete_global_random_map_quantifiers(self):
        for name in (IDENTITY,LOWER):
            c=self.by_id[name]
            self.assertEqual(c["mode"],"CONDITIONAL_EXPECTATION")
            self.assertEqual([q["op"] for q in c["quantifiers"]],
                             ["forall","forall","expectation"])
            self.assertEqual([q["variable"] for q in c["quantifiers"]],
                             ["h","f","g"])
            self.assertIn("ONE",c["quantifiers"][-1]["domain"].upper() if
                          "one" in c["quantifiers"][-1]["domain"] else
                          c["quantifiers"][-1]["domain"])

    def test_05_duality_reverses_only_fixed_and_random_types(self):
        c=self.by_id[DUAL]
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall","forall","expectation"])
        self.assertEqual([q["variable"] for q in c["quantifiers"]],
                         ["h","g","f"])

    def test_06_finite_w32_is_not_a_global_counterfamily(self):
        c=self.by_id[W32]
        self.assertEqual(c["mode"],"LOCAL_CONSTRUCTION")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall","exists","finite_witness"])
        self.assertIn("h=1",c["quantifiers"][0]["domain"])
        self.assertIn("all-h",c["limitations"][-1].lower())

    def test_07_exact_dependency_graph_and_all_claims_evidenced(self):
        self.assertEqual(self.by_id[TENSOR]["depends_on_claims"],
                         ["HYP105-AA4Q-SEVEN-ORIGINAL-JOIN"])
        self.assertEqual(self.by_id[IDENTITY]["depends_on_claims"],[TENSOR])
        self.assertIn(IDENTITY,self.by_id[LOWER]["depends_on_claims"])
        self.assertEqual(self.by_id[DUAL]["depends_on_claims"],[LOWER])
        receipt=next(x for x in self.evidence if x["id"]=="HYP105-EV-AA4T")
        self.assertEqual(set(receipt["claim_ids"]),set(CLAIMS))
        self.assertEqual(receipt["ci"]["status"],"NOT_ARCHIVED_AS_PROOF")
        self.assertEqual(receipt["reproduction"]["execution_status"],
                         "COMMAND_DOCUMENTED_NOT_EXECUTED_BY_RCP_C")
        validate_registry(REG)

    def test_08_60_unoriented_connected_position_cycles(self):
        self.assertEqual(perm(6,6)//12,60)
        self.assertEqual(exact_certificate(2)["occupied"],60)
        self.assertEqual(exact_certificate(4)["occupied"],108900)

    def test_09_small_real_gq_hall_boundary_not_false_factorial_zero(self):
        for s in (2,4):
            v=exact_certificate(s)
            self.assertEqual(v["matching"],1)
            self.assertLess(s+1,6)
            self.assertGreater(v["expected_lower"],0)
        self.assertEqual(exact_certificate(2)["probability"],Fraction(1,5005))

    def test_10_exact_rational_all_h_finite_sanity_inequality(self):
        for h in range(1,13):
            s=1<<h
            z=exact_certificate(s)
            with self.subTest(s=s):
                self.assertGreaterEqual(z["m"],0)
                self.assertLessEqual(z["m"],z["a"]-2)
                self.assertGreater(z["occupied"],0)
                self.assertGreaterEqual(z["expected_lower"],Fraction(s**6,98304))
                self.assertLess(comb(z["a"]-1,2),z["V"])

    def test_11_relative_constants_do_not_downgrade_existing_stronger_bound(self):
        self.assertLess(Fraction(1,98304),Fraction(1,8))
        self.assertIn("s^6/8",self.by_id[LOWER]["statement"])
        self.assertIn("h=1,2",self.by_id[LOWER]["statement"])
        self.assertIn("s>=8",self.by_id[LOWER]["statement"])

    def test_12_exact_finite_true_w32_mean_and_realized_zero(self):
        self.assertEqual(Fraction(21186,5005),Fraction(1926,455))
        self.assertGreater(Fraction(1926,455),0)
        s=self.by_id[W32]["statement"]
        self.assertIn("D6(f,g)=0",s)
        self.assertIn("68 and 72",s)
        self.assertIn("21186",s)

    def test_13_scoped_negative_knowledge_is_not_root_counterexample(self):
        n=next(x for x in self.nogos if x["id"] ==
               "HYP105-NG-AA4T-POSITIVE-TENSOR-MARGINAL-NOT-POINTWISE")
        self.assertEqual(n["kind"],"INVALID_INFERENCE")
        self.assertEqual(n["root_status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertIn(W32,n["related_claim_ids"])
        self.assertTrue(any("TOTAL seven" in x for x in n["does_not_refute"]))

    def test_14_five_formulas_and_real_dependency_docs(self):
        f={v["id"]:v for v in read_formulas(REG,set(self.by_id))}
        for i in range(17,22):
            self.assertIn("HYP105-F-%03d"%i,f)
        self.assertIn("A_g(H,Q)",f["HYP105-F-017"]["latex"])
        self.assertIn("98304",f["HYP105-F-019"]["latex"])
        docs=render_all(REG)
        self.assertIn(TENSOR,docs["RESULTS.md"])
        self.assertIn(W32,docs["RESEARCH-MATRIX.md"])
        self.assertIn("HYP105-F-021",docs["FORMULAS.md"])
        self.assertIn(IDENTITY,docs["PROOF-GRAPH.md"])

    def test_15_full_incremental_ledgers_no_global_count_cap(self):
        self.assertGreaterEqual(self.validation["claim_count"],19)
        self.assertGreaterEqual(self.validation["evidence_count"],9)
        self.assertGreaterEqual(self.validation["no_go_count"],9)
        self.assertGreaterEqual(self.validation["archived_blob_count"],29)


if __name__ == "__main__":
    unittest.main()
