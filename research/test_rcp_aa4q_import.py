"""RCP-COV-AA4Q: independent scientific *scope* and genuine W32 GQ checks.

Checks source/meta integrity + the girth-8 combinatorial implication.
These tests do NOT certify the historical GF5 seven-class classifier or
an all-(f,g) positive lower bound.
"""
from __future__ import annotations

from itertools import combinations
from pathlib import Path
import json
import unittest

from research.rcp.claim_registry import read_registry, validate_registry
from research.rcp.evidence_ledger import validate_ledgers, verify_archives
from research.rcp.structured_docs import read_formulas

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "research/rcp/hyp105"
Q_SOURCE = "a51ce5aeb7883dcd029b9275ce44eaca9a60370f"
JOIN_ID = "HYP105-AA4Q-SEVEN-ORIGINAL-JOIN"
CC_ID = "HYP105-AA4Q-CC-GIRTH-OBSTRUCTION"


def w32_true_source_incidence():
    """Build genuine symplectic W(3,2), independently of the original PR oracle."""
    def symp(a, b):
        return ((a >> 0 & 1) * (b >> 2 & 1) ^
                (a >> 2 & 1) * (b >> 0 & 1) ^
                (a >> 1 & 1) * (b >> 3 & 1) ^
                (a >> 3 & 1) * (b >> 1 & 1)) & 1
    lines = {tuple(sorted((u, v, u ^ v))) for u in range(1, 16)
             for v in range(u+1, 16) if symp(u, v) == 0}
    rows = tuple(sorted(lines))
    assert len(rows) == 15 and all(len(line) == 3 for line in rows)
    return {(p, lid) for lid, line in enumerate(rows) for p in line}


def cc_sixset_cyclic_witness(edges):
    """Every simple six-edge degree-2 bipartite 3+3 graph is a source C6."""
    points = {p for p, _ in edges}
    lines = {q for _, q in edges}
    return (len(edges) == 6 and len(set(edges)) == 6 and
            len(points) == len(lines) == 3 and
            all(sum(u == p for u, _ in edges) == 2 for p in points) and
            all(sum(v == q for _, v in edges) == 2 for q in lines))


class AA4QImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, claims = read_registry(REG)
        cls.registry = {c["id"]: c for c in claims}

    def test_01_exact_two_scoped_claims_with_source(self):
        self.assertIn(JOIN_ID, self.registry)
        self.assertIn(CC_ID, self.registry)
        for key in (JOIN_ID, CC_ID):
            c = self.registry[key]
            self.assertEqual(c["source"]["commit"], Q_SOURCE)
            self.assertEqual(c["source"]["pr"], 476)
            self.assertEqual(c["source"]["proof_blob_sha"],
                             "2618aab8a4e57ee6b71eb2746c65bc9757984828")
            self.assertEqual(c["mode"], "ALL_H_IDENTITY")
            self.assertEqual(c["mathematical_status"], "DOCUMENTED_IN_DRAFT")
            self.assertEqual(c["review_status"], "NOT_REVIEWED")
            self.assertEqual(c["root_impact"], "ROOT_BRANCHES_OPEN")

    def test_02_joint_two_map_quantifiers_not_random_independent_q(self):
        for key in (JOIN_ID, CC_ID):
            c = self.registry[key]
            self.assertEqual([q["op"] for q in c["quantifiers"]],
                             ["forall", "forall"])
            self.assertIn("s=2^h", c["quantifiers"][0]["domain"])
            self.assertIn("reused across all six-incidence sets",
                          c["quantifiers"][1]["domain"])

    def test_03_dependency_cc_in_seven_join(self):
        self.assertIn(CC_ID, self.registry[JOIN_ID]["depends_on_claims"])
        self.assertFalse(self.registry[CC_ID]["depends_on_claims"])
        validate_registry(REG)

    def test_04_exact_original_archive_has_three_bytes_pins(self):
        result = verify_archives(REG, ROOT)
        entries = [x for x in result if "archive/PR476/" in x["archive"]]
        self.assertEqual(len(entries), 3)
        self.assertTrue(all(x["source_commit"] == Q_SOURCE for x in entries))
        self.assertEqual({x["git_blob_sha"] for x in entries},
                         {"2618aab8a4e57ee6b71eb2746c65bc9757984828",
                          "1dbdd1172a0776e53cac42a2655268d84b85fcbc",
                          "c85c97a070e814294f7d24484aa9a0237804ea13"})
        validate_ledgers(REG)

    def test_05_two_separately_scoped_latex_formulas(self):
        values = read_formulas(REG, set(self.registry))
        formulas = {x["id"]: x for x in values}
        self.assertGreaterEqual(len(formulas), 9)
        self.assertTrue(all(fid in formulas for fid in
                            ("HYP105-F-008", "HYP105-F-009")))
        self.assertEqual(formulas["HYP105-F-008"]["claim_ids"], [JOIN_ID])
        self.assertEqual(formulas["HYP105-F-009"]["claim_ids"], [CC_ID])
        self.assertIn("cap", formulas["HYP105-F-008"]["latex"])
        self.assertIn("varnothing", formulas["HYP105-F-009"]["latex"])

    def test_06_genuine_symplectic_w32_has_15_points_lines_and_45_flags(self):
        edges = w32_true_source_incidence()
        self.assertEqual(len(edges), 45)
        self.assertEqual(len({p for p, _ in edges}), 15)
        self.assertEqual(len({q for _, q in edges}), 15)
        self.assertTrue(all(sum(p == x for x, _ in edges) == 3
                            for p in range(1, 16)))
        self.assertTrue(all(sum(q0 == q for _, q0 in edges) == 3
                            for q in range(15)))

    def test_07_no_genuine_original_w32_source_cc(self):
        edges = w32_true_source_incidence()
        points = sorted({p for p, _ in edges})
        lines = sorted({q for _, q in edges})
        # 455 * 455 genuine 3x3 induced incidence matrices, no fake physical Q.
        for pts in combinations(points, 3):
            for lids in combinations(lines, 3):
                src = [(p, q) for p in pts for q in lids if (p, q) in edges]
                self.assertFalse(cc_sixset_cyclic_witness(src))

    def test_08_abstract_cc_forces_a_six_cycle_not_theorem_about_physical_labels(self):
        cycle = [(0,0),(1,0),(1,1),(2,1),(2,2),(0,2)]
        self.assertTrue(cc_sixset_cyclic_witness(cycle))
        self.assertFalse(cc_sixset_cyclic_witness(cycle[:-1]))

    def test_09_set_join_formula_is_not_marginal_product(self):
        # Independent set oracle: original IDs, *not* abstract column orbits.
        original = set(range(40))
        hp = {0,1,2,3,4,5,6,7}
        hl = {4,5,6,7,8,9}
        joint = hp & hl
        aa = {4,5}
        d6 = {4}
        positive = (joint - aa) | d6
        self.assertEqual(len(positive), len(joint)-len(aa)+len(d6))
        self.assertNotEqual(len(positive), len(hp)*len(hl))
        self.assertTrue(aa <= joint and d6 <= aa and positive <= original)

    def test_10_marginals_are_not_joint_information(self):
        hp = {1, 2, 3, 4}
        hl0, hl1 = {5, 6, 7, 8}, {1, 2, 3, 4}
        self.assertEqual(len(hl0), len(hl1))
        self.assertNotEqual(len(hp & hl0), len(hp & hl1))

    def test_11_zero_joint_possible_from_equal_nonzero_marginals(self):
        hp, hl = {1,2,3}, {4,5,6}
        self.assertTrue(hp and hl)
        self.assertFalse(hp & hl)

    def test_12_positive_ensemble_mean_does_not_imply_fixed_pair_positive(self):
        xs = [0, 12, 5, 2]
        self.assertGreater(sum(xs)/len(xs), 0)
        self.assertEqual(min(xs), 0)


if __name__ == "__main__":
    unittest.main()
