"""RCP-AA4S: independently check scoped original root-Fréchet provenance.

Exact finite integer arithmetic is a boundary check, not an independent
machine proof of all h or proof-review acceptance of scientific PR #479.
"""
from __future__ import annotations

from hashlib import sha256
from math import comb, prod
from pathlib import Path
import unittest

from research.rcp.claim_registry import validate_registry, read_registry
from research.rcp.evidence_ledger import (
    load_ledgers, validate_ledgers, verify_archives, git_blob_sha, load_pins,
)
from research.rcp.structured_docs import read_formulas, render_all

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
SRC = "357b3d201e14713668fbd045b450ffd279610081"
PREFIX = "research/rcp/hyp105/archive/PR479/"
A = "HYP105-AA4S-ROOT-FRECHET-ZERO"
B = "HYP105-AA4S-W32-POSITIVE-JOINT-ZERO-MARGINAL"


def root_envelope(s: int):
    assert s >= 2 and s & (s-1) == 0
    d, V = s + 1, (s+1)*(s*s+1)
    a = 2
    while comb(a, 2) < V:
        a += 1
    M = comb(d, 2) * prod(d*(V-3-2*j) for j in range(4)) // 24
    BP = 3 * comb(a-2, 4) * comb(d, 2) * d**4
    AG = 70 * comb(a, 6) * d**6
    return {"s": s, "a": a, "M": M, "B": BP, "A": AG,
            "gap": M-BP-AG}


class RootMarginalImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validation = validate_ledgers(REG)
        cls.models, entries = read_registry(REG)
        cls.claims = {c["id"]: c for c in entries}
        cls.receipts, cls.nogos = load_ledgers(REG)

    def test_01_original_three_blobs_byte_exact_sha1_and_sha256(self):
        escrows = verify_archives(REG, ROOT)
        by_path = {b["archive"]: b for b in escrows}
        pins = load_pins(REG)
        expected = {
            "proof.md": "2f6794f64b95e77368dc4dabcf8a4410f5f8b66f",
            "oracle.py.txt": "e3d67f69c3faff4e12d8537697eb89ce4cfeaffc",
            "independent_test.py.txt": "728262c792a66f54ebff9428e10a18ee292b2c60",
        }
        for suffix, blob in expected.items():
            name = PREFIX+suffix
            payload = (ROOT/name).read_bytes()
            self.assertEqual(git_blob_sha(payload), blob)
            self.assertEqual(by_path[name]["source_commit"], SRC)
            self.assertEqual(sha256(payload).hexdigest(), pins[name])
        self.assertEqual(len(escrows), len(pins))

    def test_02_original_commit_provenance_and_no_promotion(self):
        for cid in (A, B):
            c = self.claims[cid]
            self.assertEqual(c["source"]["pr"], 479)
            self.assertEqual(c["source"]["commit"], SRC)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "2f6794f64b95e77368dc4dabcf8a4410f5f8b66f")
            self.assertEqual(c["mathematical_status"], "DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"], "NOT_REVIEWED")
            self.assertEqual(c["root_impact"], "ROOT_BRANCHES_OPEN")

    def test_03_all_h_for_all_f_g_and_every_real_original_root(self):
        c = self.claims[A]
        self.assertEqual(c["mode"], "DETERMINISTIC_BOUND")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall", "forall", "forall"])
        self.assertEqual([q["variable"] for q in c["quantifiers"]],
                         ["h", "f,g", "p"])
        self.assertIn("original", c["statement"].lower())
        self.assertIn("Fréchet", c["statement"])
        self.assertIn("zero", " ".join(c["limitations"]).lower())

    def test_04_finite_witness_cannot_be_promoted_to_all_h_counterfamily(self):
        c = self.claims[B]
        self.assertEqual(c["mode"], "LOCAL_CONSTRUCTION")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall", "exists", "finite_witness"])
        self.assertIn("FINITE", c["quantifiers"][0]["domain"])
        self.assertTrue(any("not a counterfamily" in x.lower()
                            for x in c["limitations"]))

    def test_05_dependencies_and_exact_scoped_evidence_receipt(self):
        self.assertEqual(self.claims[A]["depends_on_claims"],
                         ["HYP105-AA4Q-SEVEN-ORIGINAL-JOIN"])
        self.assertEqual(self.claims[B]["depends_on_claims"], [A])
        receipt = next(e for e in self.receipts if e["id"]=="HYP105-EV-AA4S")
        self.assertEqual(receipt["source"]["commit"], SRC)
        self.assertEqual(set(receipt["claim_ids"]), {A,B})
        self.assertEqual(receipt["ci"]["status"], "NOT_ARCHIVED_AS_PROOF")

    def test_06_no_go_does_not_reject_positive_real_joint(self):
        n = next(x for x in self.nogos if x["id"] ==
                 "HYP105-NG-AA4S-ROOT-MARGINAL-FRECHET-ZERO")
        self.assertEqual(n["kind"], "INVALID_INFERENCE")
        self.assertEqual(set(n["related_claim_ids"]), {A,B})
        self.assertIn("=0", n["mathematical_basis"])
        self.assertTrue(any("positive" in x.lower()
                            for x in n["does_not_refute"]))

    def test_07_exact_small_h_source_root_marginal_envelopes(self):
        expected = {
            2: (6, 58320, 729, 51030, 6561),
            4: (14, 10127000000, 9281250, 3284531250, 6833187500),
            8: (35, 1106019023454720, 28995420960,
                60382964149200, 1045607063884560),
            16: (94, 171499941395314497920, 95215212860040,
                 1375724937609359610, 170124121242492278270),
        }
        for s, row in expected.items():
            with self.subTest(s=s):
                d = root_envelope(s)
                self.assertEqual((d["a"],d["M"],d["B"],d["A"],d["gap"]), row)
                self.assertGreater(d["gap"], 0)

    def test_08_other_finite_powers_have_strict_nonnegative_gap(self):
        for h in range(1,12):
            d = root_envelope(1<<h)
            self.assertGreater(d["gap"], 0)
            self.assertGreater(d["M"], d["B"]+d["A"])

    def test_09_lower_is_not_exact_U_p_at_true_W32(self):
        d = root_envelope(2)
        self.assertEqual(d["M"], 58320)
        self.assertLess(d["M"], 111132)
        self.assertEqual(self.claims[B]["statement"].count("111132"), 1)
        self.assertIn("44", self.claims[B]["statement"])
        self.assertIn("36", self.claims[B]["statement"])
        # This checks precise registration; it is not a replay of the
        # original W32 oracle in a different codebase.

    def test_10_three_indexed_formulas_with_scoped_nonimplications(self):
        formula = read_formulas(REG, set(self.claims))
        f = {x["id"]:x for x in formula}
        for name in ("HYP105-F-014", "HYP105-F-015", "HYP105-F-016"):
            self.assertIn(name,f)
            self.assertTrue(f[name]["not_implies"])
        self.assertIn("M_p", f["HYP105-F-014"]["latex"])
        self.assertIn("\\max", f["HYP105-F-015"]["latex"])

    def test_11_derived_markdown_preserves_math_sources(self):
        docs=render_all(REG)
        self.assertIn(A, docs["RESULTS.md"])
        self.assertIn(B, docs["RESULTS.md"])
        self.assertIn("HYP105-F-015", docs["FORMULAS.md"])
        self.assertIn("HYP105-NG-AA4S", docs["RESEARCH-MATRIX.md"])
        self.assertIn("HYP105-AA4Q-SEVEN-ORIGINAL-JOIN",
                      docs["PROOF-GRAPH.md"])

    def test_12_ledger_is_incremental_unbounded(self):
        self.assertGreaterEqual(self.validation["claim_count"], 14)
        self.assertGreaterEqual(self.validation["archived_blob_count"], 29)
        self.assertGreaterEqual(self.validation["evidence_count"], 9)
        self.assertGreaterEqual(self.validation["no_go_count"], 9)
        validate_registry(REG)


if __name__ == "__main__":
    unittest.main()
