"""RCP-AA4U: independent source-forest provenance, finite arithmetic and quantifier tests.

This checks pinned original evidence and simple mathematical identities. The
original 8,145,060-set research census is preserved, not rerun in this import.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import unittest

from research.rcp.claim_registry import read_registry, validate_registry
from research.rcp.evidence_ledger import load_ledgers, validate_ledgers, verify_archives, git_blob_sha, load_pins
from research.rcp.structured_docs import read_formulas, render_all
from research.test_rcp_aa4q_import import w32_true_source_incidence

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
PR = 486
SOURCE = "f49dcef044e8a4f1bb17f080ffa11c7b365a077a"
PREFIX = "research/rcp/hyp105/archive/PR486/"
IDS = (
    "HYP105-AA4U-NINE-ORIGINAL-FOREST",
    "HYP105-AA4U-FOREST-FRECHET-LOWER",
    "HYP105-AA4U-W32-NINE-FOREST-CENSUS",
    "HYP105-AA4U-W32-ZERO-MARGINAL-POSITIVE-JOINT",
)
N = {
    "A/A":1566360, "A/B":1666980, "B/A":1666980,
    "A/C":6225, "C/A":6225, "B/C":5220, "C/B":5220,
    "B/B-overlap":910080, "B/B-disjoint":707580,
}
S68 = {"A/A":263,"A/B":21,"B/A":44,"A/C":0,"C/A":0,
       "B/C":0,"C/B":0,"B/B-overlap":2,"B/B-disjoint":1}
S72 = {"A/A":286,"A/B":31,"B/A":36,"A/C":0,"C/A":2,
       "B/C":0,"C/B":0,"B/B-overlap":1,"B/B-disjoint":2}


class ForestImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validation = validate_ledgers(REG)
        _, claims = read_registry(REG)
        cls.claims = {c["id"]:c for c in claims}
        cls.evidence, cls.nogos = load_ledgers(REG)

    def test_01_source_git_blobs_and_independent_sha256(self):
        expected = {
            "proof.md":"364f95d0dfd94d693d0152abf571a1312532ba14",
            "oracle.py.txt":"9eb84d4b7798ee5e7b524977257b3f53cb034d95",
            "independent_test.py.txt":"e53c9c77bf378eef354e6ac383761f7e022cf6fd",
        }
        records = {r["archive"]:r for r in verify_archives(REG, ROOT)}
        pins = load_pins(REG)
        for suffix, blob in expected.items():
            path = PREFIX + suffix
            payload = (ROOT/path).read_bytes()
            self.assertEqual(git_blob_sha(payload),blob)
            self.assertEqual(records[path]["source_commit"],SOURCE)
            self.assertEqual(sha256(payload).hexdigest(),pins[path])

    def test_02_four_distinct_scopes_and_unreviewed_origins(self):
        for key in IDS:
            c = self.claims[key]
            self.assertEqual(c["source"]["pr"],PR)
            self.assertEqual(c["source"]["commit"],SOURCE)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "364f95d0dfd94d693d0152abf571a1312532ba14")
            self.assertEqual(c["mathematical_status"],"DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"],"NOT_REVIEWED")
            self.assertEqual(c["root_impact"],"ROOT_BRANCHES_OPEN")

    def test_03_universal_quantifiers_are_not_averages(self):
        for key in IDS[:2]:
            c = self.claims[key]
            self.assertEqual([x["op"] for x in c["quantifiers"]],
                             ["forall","forall"])
            self.assertEqual(c["quantifiers"][0]["variable"],"h")
            self.assertIn("h>=1",c["quantifiers"][0]["domain"])
            self.assertNotIn("expectation",[x["op"] for x in c["quantifiers"]])

    def test_04_finite_only_claim_must_pin_exact_h(self):
        self.assertEqual(self.claims[IDS[2]]["quantifiers"][0]["domain"].split(";")[0],
                         "integer h=1, s=2^h=2")
        self.assertEqual([x["op"] for x in self.claims[IDS[3]]["quantifiers"]],
                         ["forall","exists","finite_witness"])
        self.assertIn("NOT",self.claims[IDS[3]]["limitations"][1].upper())

    def test_05_canonical_dependency_graph(self):
        self.assertIn("HYP105-AA4Q-CC-GIRTH-OBSTRUCTION",
                      self.claims[IDS[0]]["depends_on_claims"])
        self.assertIn("HYP105-AA4T-POSITIONAL-D6-TENSOR",
                      self.claims[IDS[1]]["depends_on_claims"])
        self.assertIn(IDS[2],self.claims[IDS[3]]["depends_on_claims"])
        validate_registry(REG)

    def test_06_genuine_W32_GQ_flags_have_no_source_6_cycles(self):
        edges = w32_true_source_incidence()
        self.assertEqual(len(edges),45)
        # Any source C/C would require a 3-point/3-line 6-cycle.
        for pts in combinations(range(1,16),3):
            for lids in combinations(range(15),3):
                q = [(p,l) for p in pts for l in lids if (p,l) in edges]
                self.assertFalse(len(q)==6 and all(sum(u==p for u,_ in q)==2
                         for p in pts) and all(sum(v==l for _,v in q)==2
                         for l in lids))

    def test_07_finite_original_source_grid_exact_arithmetic(self):
        self.assertEqual(comb(45,6),8145060)
        self.assertEqual(sum(N.values()),6540870)
        self.assertEqual(comb(45,6)-sum(N.values()),1604190)
        self.assertEqual(len(N),9)
        self.assertEqual(N["A/B"],N["B/A"])
        self.assertEqual(N["A/C"],N["C/A"])
        self.assertEqual(N["B/C"],N["C/B"])

    def test_08_finite_source_A_B_C_marginals_not_physical(self):
        A=comb(15,6)*3**6
        B=15*comb(14,4)*comb(3,2)*3**4
        C=comb(15,3)*comb(3,2)**3
        self.assertEqual((A,B,C),(3648645,3648645,12285))
        self.assertGreater(A,51030)
        self.assertGreater(B,10935)
        self.assertGreater(C,405)

    def test_09_nine_joint_cells_and_historical_AA_veto(self):
        self.assertEqual(sum(S68.values()),331)
        self.assertEqual(sum(S72.values()),358)
        self.assertEqual(sum(v for k,v in S68.items() if k!="A/A"),68)
        self.assertEqual(sum(v for k,v in S72.items() if k!="A/A"),72)
        self.assertEqual(sum(S68.values())-S68["A/A"],68)
        self.assertEqual(sum(S72.values())-S72["A/A"],72)

    def test_10_frechet_relaxation_is_not_realizability(self):
        universe=set(range(100))
        left=set(range(20))
        right=set(range(20,40))
        right_better=set(range(0,20))
        floor=max(0,len(left)+len(right)-len(universe))
        self.assertEqual(floor,0)
        self.assertEqual(len(left & right),0)
        self.assertEqual(len(left & right_better),20)
        self.assertEqual(sum(max(0,2*40-v) for v in N.values()),0)

    def test_11_source_receipt_and_no_go_dont_promote_theorem(self):
        e=next(x for x in self.evidence if x["id"]=="HYP105-EV-AA4U")
        self.assertEqual(set(e["claim_ids"]),set(IDS))
        self.assertEqual(e["ci"]["status"],"NOT_ARCHIVED_AS_PROOF")
        n=next(x for x in self.nogos if x["id"]==
               "HYP105-NG-AA4U-NINE-FOREST-MARGINAL-NOT-MINIMAX")
        self.assertEqual(n["kind"],"INVALID_INFERENCE")
        self.assertEqual(n["root_status"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_12_five_formulas_and_five_documents(self):
        formulas={f["id"]:f for f in read_formulas(REG,set(self.claims))}
        for n in range(22,27):
            self.assertIn(f"HYP105-F-{n:03}",formulas)
        docs=render_all(REG)
        self.assertEqual(len(docs),5)
        for key in ("RESULTS.md","FORMULAS.md","PROOF-GRAPH.md","RESEARCH-MATRIX.md","PROTOCOLS.md"):
            self.assertIn("HYP-105",docs[key])
        self.assertIn("HYP105-AA4U",docs["RESULTS.md"])
        self.assertIn("HYP105-NG-AA4U",docs["RESEARCH-MATRIX.md"])

    def test_13_incremental_ledger_not_capped(self):
        self.assertGreaterEqual(self.validation["claim_count"],23)
        self.assertGreaterEqual(self.validation["evidence_count"],10)
        self.assertGreaterEqual(self.validation["archived_blob_count"],32)
        self.assertGreaterEqual(self.validation["no_go_count"],10)


if __name__=="__main__":
    unittest.main()
