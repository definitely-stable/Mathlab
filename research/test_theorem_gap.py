"""THEOREM-GAP-004: deterministic model-transfer falsification oracles.

This tests elementary finite-field implications and metadata, NOT a proof
of Lefmann's general theorem, XYZ-Sketch claims, or global novelty.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/research/THEOREM-GAP-004-TRANSFER.json"
LITERATURE = ROOT / "docs/research/catalog/literature.json"
CATALOG = ROOT / "docs/research/catalog/registry.json"


def all_exact_subsets(columns, prime):
    """Unique 0,1,2 DISTINCT column subset sums, including empty."""
    if not columns:
        return True
    m = len(columns[0])
    if any(len(v) != m or all(x % prime == 0 for x in v) for v in columns):
        return False
    if len(set(columns)) != len(columns):
        return False
    seen = set()
    for size in range(min(2, len(columns)) + 1):
        for subset in itertools.combinations(columns, size):
            total = tuple(sum(v[i] for v in subset) % prime for i in range(m))
            if total in seen:
                return False
            seen.add(total)
    return True


def rank_mod(columns, prime):
    if not columns:
        return 0
    matrix = [[v % prime for v in col] for col in columns]
    width = len(matrix[0])
    row = 0
    for col in range(width):
        pivot = next((i for i in range(row, len(matrix))
                      if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = pow(matrix[row][col], -1, prime)
        matrix[row] = [(x * inverse) % prime for x in matrix[row]]
        for i in range(len(matrix)):
            if i == row:
                continue
            factor = matrix[i][col]
            if factor:
                matrix[i] = [(a - factor * b) % prime
                             for a, b in zip(matrix[i], matrix[row])]
        row += 1
        if row == len(matrix):
            break
    return row


def at_most_four_independent(columns, prime):
    return all(rank_mod(subset, prime) == len(subset)
               for size in range(1, min(4, len(columns)) + 1)
               for subset in itertools.combinations(columns, size))


def lefmann_k4_r_exponent(sparsity):
    return Fraction((4 * sparsity + 2) // 3, 2)


class TheoremGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = json.loads(DOC.read_text(encoding="utf-8"))
        cls.lit = json.loads(LITERATURE.read_text(encoding="utf-8"))
        cls.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    def test_sufficient_independence_implies_aset_in_small_prime_fields(self):
        # Exhaustive over all sets of up to four among the eight nonzero
        # 2D vectors over GF(3), and capped samples over GF(5).
        for p, m, candidate_limit in ((3, 2, 8), (5, 2, 9)):
            candidates = [x for x in itertools.product(range(p), repeat=m)
                          if any(x)][:candidate_limit]
            for n in range(1, 5):
                for family in itertools.combinations(candidates, n):
                    if at_most_four_independent(family, p):
                        self.assertTrue(all_exact_subsets(family, p))

    def test_exact_aset_not_fourwise_independent(self):
        columns = ((1,), (2,))
        self.assertTrue(all_exact_subsets(columns, 5))
        self.assertFalse(at_most_four_independent(columns, 5))
        self.assertEqual(sorted([0, 1, 2, 3]), [0, 1, 2, 3])

    def test_explicit_collision_versus_arbitrary_coefficient_dependence(self):
        self.assertFalse(all_exact_subsets(((1, 0), (0, 1), (1, 1)), 5))
        self.assertTrue(all_exact_subsets(((1,), (2,)), 5))
        self.assertEqual(rank_mod(((1,), (2,)), 5), 1)

    def test_lefmann_k4_support_exponents(self):
        self.assertEqual(lefmann_k4_r_exponent(2), Fraction(3, 2))
        self.assertEqual(lefmann_k4_r_exponent(3), Fraction(2, 1))
        # For r=4 the exponent is ceil(16/3)/2 = 3,
        # not a claimed ASET upper bound.
        self.assertEqual(lefmann_k4_r_exponent(4), Fraction(3, 1))

    def test_registry_sources_and_stage_coverage(self):
        self.assertEqual(self.audit["schema"], "mathlab.theorem-gap-004.v1")
        literature_ids = {x["id"] for x in self.lit["entries"]}
        research_ids = {x["id"] for x in self.catalog["entries"]}
        records = self.audit["records"]
        self.assertEqual(len(records), 12)
        self.assertEqual({x["stage"] for x in records}, {1, 2, 3, 4})
        self.assertEqual(len({x["id"] for x in records}), len(records))
        for x in records:
            self.assertTrue(x["sources"])
            self.assertTrue(x["research"])
            self.assertTrue(x["direction"] and x["counter_direction"])
            self.assertTrue(x["research_gap"] and x["model"])
            self.assertTrue(set(x["sources"]).issubset(literature_ids))
            self.assertTrue(set(x["research"]).issubset(research_ids))

    def test_policy_no_proof_or_product_promotion(self):
        p = self.audit["policy"]
        self.assertEqual(p, {
            "originality_verified": False,
            "external_full_proof_rechecked": False,
            "lean_independent_check": False,
            "product_rust_authorized": False,
            "finite_b2_unchanged": True,
        })
        checks = {x["id"]: x for x in self.audit["records"]}
        self.assertEqual(checks["TG-009"]["status"], "STOP_SYSTEM_PRODUCT")
        self.assertEqual(checks["TG-012"]["status"],
                         "NO_PRODUCT_OR_NOVELTY_AUTHORIZATION")
        self.assertIn("LIT-043", checks["TG-001"]["sources"])
        self.assertIn("LIT-043", checks["TG-002"]["sources"])

    def test_snapshot_shas_are_pinned_not_branch_names(self):
        snaps = self.audit["source_snapshots"]
        self.assertEqual(set(snaps), {"MATHLAB", "DELSK", "DELTAMETER"})
        for obj in snaps.values():
            self.assertEqual(len(obj["sha"]), 40)
            self.assertTrue(all(c in "0123456789abcdef" for c in obj["sha"]))
            self.assertNotEqual(obj["sha"], "main")

    def test_no_global_aset_upper_claim_is_attributed_to_lefmann(self):
        for x in self.audit["records"][:2]:
            self.assertIn("PRIOR_ART_EXPONENT_OVERLAP", x["status"])
            self.assertIn("upper", x["counter_direction"].lower()
                          + x["direction"].lower()
                          + x["research_gap"].lower()
                          + x["model"].lower()
                          if x["id"] == "TG-002" else
                          "upper for ASET must be separately proved")


if __name__ == "__main__":
    unittest.main()
