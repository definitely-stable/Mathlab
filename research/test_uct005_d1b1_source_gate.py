"""Independent D1-B1 source-index guards and original-coordinate query masks."""
import itertools
import unittest

from uct005_d1b1_source_gate import (
    IDS, interval_run_decomposition, original_coordinate_interface_gap,
    query_mask_from_intervals, validate_matrix,
)


class D1B1Tests(unittest.TestCase):
    def test_canonical_metadata_and_differentiated_primary_evidence(self):
        m = validate_matrix()
        self.assertEqual(m["root_novelty"], "OPEN_UNPROVED")
        self.assertEqual(m["source_count"], 20)
        self.assertEqual(len(m["entries"]), len(IDS))
        rows = {row["id"]: row for row in m["entries"]}
        self.assertEqual(rows["LIT-112"]["source_evidence"], "THEOREM_STATEMENT_PRIMARY")
        self.assertEqual(rows["LIT-119"]["transfer"], "REDUCTION_REQUIRED")
        self.assertEqual(rows["LIT-359"]["transfer"], "METHOD_ONLY")
        self.assertTrue(all(not row["proof_verified"] for row in m["entries"]))
        self.assertEqual(rows["LIT-354"]["transfer"], "CONDITIONAL_UPPER")
        self.assertIn("proof-binding", rows["LIT-159"]["barrier"])

    def test_minimum_interval_xor_count_all_masks_n1_to_9(self):
        for n in range(1, 10):
            all_intervals = [(i, j) for i in range(n)
                             for j in range(i+1, n+1)]
            for mask in itertools.product((0, 1), repeat=n):
                runs = interval_run_decomposition(mask)
                self.assertEqual(query_mask_from_intervals(n, runs), mask)
                expected = sum(mask[i] and (i == 0 or not mask[i-1])
                               for i in range(n))
                self.assertEqual(len(runs), expected)
                if expected > 1:
                    self.assertNotIn(mask, (
                        query_mask_from_intervals(n, (interval,))
                        for interval in all_intervals
                    ))

    def test_independent_boundary_flip_lower_certificate(self):
        for n in range(1, 10):
            for mask in itertools.product((0, 1), repeat=n):
                boundaries = (0,) + mask + (0,)
                changes = sum(boundaries[i] ^ boundaries[i+1]
                              for i in range(n+1))
                self.assertEqual(changes, 2 * len(interval_run_decomposition(mask)))

    def test_every_mask_parity_is_xor_of_its_runs(self):
        for n in range(1, 7):
            for mask in itertools.product((0, 1), repeat=n):
                runs = interval_run_decomposition(mask)
                for state in itertools.product((0, 1), repeat=n):
                    independent = sum(a & b for a, b in zip(mask, state)) % 2
                    by_queries = 0
                    for lo, hi in runs:
                        by_queries ^= sum(state[lo:hi]) % 2
                    self.assertEqual(by_queries, independent)

    def test_count_gap_is_not_a_dynamic_lower_bound(self):
        for n in range(3, 14):
            d = original_coordinate_interface_gap(n)
            self.assertGreater(d["arbitrary_nonzero_GF2_query_masks"],
                               d["single_contiguous_interval_masks"])
            self.assertEqual(d["root"], "OPEN_UNPROVED")
            self.assertIn("encodings", d["cannot_rule_out"])
        with self.assertRaises(ValueError):
            original_coordinate_interface_gap(2)
        with self.assertRaises(ValueError):
            interval_run_decomposition(())
        with self.assertRaises(ValueError):
            interval_run_decomposition((1, 2))
        with self.assertRaises(ValueError):
            query_mask_from_intervals(4, ((2, 5),))


if __name__ == "__main__":
    unittest.main()
