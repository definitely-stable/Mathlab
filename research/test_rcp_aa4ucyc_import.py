"""Independent RCP-AA4UCYC provenance and scope tests.

Tests immutable original Git blob bytes and exact finite rational identities.
They do not reprove the underlying all-h cycle-coloring classification nor
rerun the archived original 21,186-sixset oracle.
"""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from math import comb, perm
from pathlib import Path
import unittest

from research.rcp.claim_registry import read_registry, validate_registry
from research.rcp.evidence_ledger import (
    validate_ledgers, verify_archives, load_ledgers, load_pins, git_blob_sha
)
from research.rcp.structured_docs import read_formulas, render_all

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
PREFIX = "research/rcp/hyp105/archive/PR487/"
SOURCE = "1502844a49cea1631206b2b68144c65f879fc4c0"
KERNEL = "HYP105-AA4UCYC-SHARED-LINE-D6-KERNEL"
ROW = "HYP105-AA4UCYC-W32-ANCHORED-ROW"
NOGO = "HYP105-NG-AA4UCYC-OVERLAP-SIZE-INSUFFICIENT"

class OriginalLineGluingImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v = validate_ledgers(REG)
        cls.models, claims = read_registry(REG)
        cls.claims = {x["id"]: x for x in claims}
        cls.receipts, cls.nogos = load_ledgers(REG)

    def test_01_byte_exact_all_three_sources_and_independent_sha256(self):
        blobs = {x["archive"]:x for x in verify_archives(REG, ROOT)}
        pins = load_pins(REG)
        expected = {
            "proof.md":"ccb294cb90b50a58a5751c087b2e75f33f16bf4b",
            "oracle.py.txt":"ef0d82fc09c88f1c7465e85d2fc67792d185c24d",
            "independent_test.py.txt":"a27a82787550ab7c1bceb4c63d0146dd8ddf391b",
        }
        for end,blob in expected.items():
            p=PREFIX+end
            content=(ROOT/p).read_bytes()
            self.assertEqual(git_blob_sha(content),blob)
            self.assertEqual(sha256(content).hexdigest(),pins[p])
            self.assertEqual(blobs[p]["git_blob_sha"],blob)
            self.assertEqual(blobs[p]["source_commit"],SOURCE)
        self.assertEqual(len(blobs),len(pins))

    def test_02_source_full_SHA_and_draft_no_false_review(self):
        for cid in (KERNEL,ROW):
            c=self.claims[cid]
            self.assertEqual(c["source"]["commit"],SOURCE)
            self.assertEqual(c["source"]["pr"],487)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "ccb294cb90b50a58a5751c087b2e75f33f16bf4b")
            self.assertEqual(c["mathematical_status"],"DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"],"NOT_REVIEWED")
            self.assertEqual(c["root_impact"],"ROOT_BRANCHES_OPEN")

    def test_03_exact_kernel_requires_true_Q_and_one_uniform_g(self):
        c=self.claims[KERNEL]
        self.assertEqual(c["mode"],"CONDITIONAL_EXPECTATION")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall","forall","forall","expectation"])
        self.assertEqual([q["variable"] for q in c["quantifiers"]],
                         ["h","f","Q0,Q1","g"])
        self.assertIn("ONE",c["quantifiers"][-1]["domain"])
        self.assertIn("12-r",c["statement"])
        self.assertIn("tau",c["statement"])

    def test_04_finite_row_is_not_all_h_second_moment(self):
        c=self.claims[ROW]
        self.assertEqual(c["mode"],"LOCAL_CONSTRUCTION")
        self.assertEqual([q["op"] for q in c["quantifiers"]],
                         ["forall","exists","finite_witness"])
        self.assertEqual(c["quantifiers"][0]["variable"],"h")
        self.assertIn("h=1",c["quantifiers"][0]["domain"])
        self.assertTrue(any("not the full" in z.lower()
                            for z in c["limitations"]))

    def test_05_registered_dependency_dag_avoids_unregistered_485(self):
        self.assertEqual(self.claims[KERNEL]["depends_on_claims"],
                         ["HYP105-AA4Q-SEVEN-ORIGINAL-JOIN"])
        self.assertEqual(self.claims[ROW]["depends_on_claims"],[KERNEL])
        self.assertTrue(any("485" in z for z in
                            self.claims[KERNEL]["external_dependencies"]))

    def test_06_single_receipt_and_proper_source_reproduction(self):
        e=next(x for x in self.receipts if x["id"]=="HYP105-EV-AA4UCYC")
        self.assertEqual(set(e["claim_ids"]),{KERNEL,ROW})
        self.assertEqual(e["source"]["commit"],SOURCE)
        self.assertEqual(e["ci"]["status"],"NOT_ARCHIVED_AS_PROOF")
        self.assertEqual(e["reproduction"]["execution_status"],
                         "COMMAND_DOCUMENTED_NOT_EXECUTED_BY_RCP_C")

    def test_07_no_go_only_rejects_overlap_cardinality_reduction(self):
        n=next(x for x in self.nogos if x["id"]==NOGO)
        self.assertEqual(n["kind"],"INVALID_INFERENCE")
        self.assertEqual(set(n["related_claim_ids"]),{KERNEL,ROW})
        self.assertTrue(any("full" in z.lower()
                            for z in n["does_not_refute"]))
        self.assertEqual(n["root_status"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_08_original_w32_row_partition_is_exact(self):
        self.assertEqual(6192+14994,21186)
        self.assertLess(112,21186)

    def test_09_exact_conditional_ratio_of_anchored_row(self):
        p=Fraction(perm(6,6),perm(15,6))
        self.assertEqual(p,Fraction(1,5005))
        row=Fraction(19457,10810800)
        self.assertEqual(row/p,Fraction(19457,2160))
        self.assertNotEqual(row,Fraction(1926,455))  # unlike unconditional mean

    def test_10_same_r_two_types_do_not_define_one_probability(self):
        c=self.claims[KERNEL]
        self.assertIn("identical",c["statement"].lower())
        self.assertIn("tau",c["statement"])
        self.assertTrue(any("cardinality" in z.lower()
                            for z in c["limitations"]))

    def test_11_three_formulas_keep_parent_proof_and_rational_row(self):
        fs={x["id"]:x for x in read_formulas(REG,set(self.claims))}
        for fid in ("HYP105-F-027","HYP105-F-028","HYP105-F-029"):
            self.assertIn(fid,fs)
            self.assertTrue(fs[fid]["not_implies"])
        self.assertEqual(fs["HYP105-F-027"]["claim_ids"],[KERNEL])
        self.assertEqual(fs["HYP105-F-029"]["claim_ids"],[ROW])
        self.assertIn("c_{\\tau,k}",fs["HYP105-F-027"]["latex"])
        self.assertIn("19457",fs["HYP105-F-029"]["latex"])

    def test_12_generated_document_matrix_not_proof_certificate(self):
        docs=render_all(REG)
        self.assertIn(KERNEL,docs["RESULTS.md"])
        self.assertIn(ROW,docs["RESULTS.md"])
        self.assertIn("HYP105-F-029",docs["FORMULAS.md"])
        self.assertIn(NOGO,docs["RESEARCH-MATRIX.md"])
        self.assertIn(KERNEL,docs["PROOF-GRAPH.md"])
        self.assertIn("NOT_REVIEWED",docs["RESULTS.md"])

    def test_13_fails_closed_metadata_schema_no_fixed_cap(self):
        val=validate_registry(REG)
        self.assertGreaterEqual(val["claims"],25)
        self.assertGreaterEqual(self.v["archived_blob_count"],35)
        self.assertGreaterEqual(self.v["evidence_count"],11)
        self.assertGreaterEqual(self.v["no_go_count"],11)

if __name__ == "__main__":
    unittest.main()
