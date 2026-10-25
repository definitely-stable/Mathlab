"""Regression test suite for W(3,2) adversarial search and 1-swap neighborhood audit."""
import unittest

from hyp105_issue230_proof_audit import F0, G68, G72
from hyp105_w32_adversarial_search import (
    W32BitmaskEvaluator,
    run_full_1swap_neighborhood_audit,
    run_randomized_adversarial_search,
)


class W32AdversarialSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evaluator = W32BitmaskEvaluator(F0)

    def test_01_canonical_ground_truths(self):
        """Verify baseline ground truth values for S68 and S72."""
        s68 = self.evaluator.evaluate_all(G68)
        self.assertEqual(s68["D6"], 0)
        self.assertEqual(s68["BA"], 44)
        self.assertEqual(s68["AB"], 21)
        self.assertEqual(s68["core"], 65)
        self.assertEqual(s68["total_S"], 68)

        s72 = self.evaluator.evaluate_all(G72)
        self.assertEqual(s72["D6"], 0)
        self.assertEqual(s72["BA"], 36)
        self.assertEqual(s72["AB"], 31)
        self.assertEqual(s72["core"], 67)
        self.assertEqual(s72["total_S"], 72)

    def test_02_s68_is_strict_local_minimum(self):
        """Verify that all 105 single-transposition neighbors of S68 have higher core and S."""
        audit = run_full_1swap_neighborhood_audit(self.evaluator, G68, "S68")
        self.assertTrue(audit["is_strict_local_min_core"])
        self.assertTrue(audit["is_strict_local_min_S"])
        self.assertGreaterEqual(audit["min_neighbor_core"], 67)
        self.assertGreaterEqual(audit["min_neighbor_S"], 75)
        self.assertEqual(len(audit["strictly_better_neighbors"]), 0)

    def test_03_randomized_descent_preserves_positive_floor(self):
        """Verify that randomized descent finds a strictly positive core sum floor."""
        search = run_randomized_adversarial_search(
            self.evaluator, num_starts=5, steps_per_start=15, seed=999
        )
        self.assertFalse(search["simultaneous_zero_found"])
        self.assertGreaterEqual(search["global_min_core"], 65)
        self.assertGreaterEqual(search["global_min_S"], 68)


if __name__ == "__main__":
    unittest.main()
