"""D6-G local Hall-excess envelope tests for HYP-105 issue #230."""
import unittest

from hyp105_issue230_d6g_local_excess_envelope import (
    local_excess_for_capacity,
    local_excess_frontier,
    report,
)


class LocalExcessEnvelopeTests(unittest.TestCase):
    def test_synthetic_detects_local_excess_beyond_global_deficit(self):
        sources = {(0, 1, 2): 3, (0, 3, 4): 3}
        targets = {
            (0, 1, 2, 3, 4, 5): "D6",
            (6, 7, 8, 9, 10, 11): "B/B-overlap",
        }
        row = local_excess_for_capacity(sources, targets, 2)
        self.assertEqual(row["source_total_C"], 6)
        self.assertEqual(row["recipient_count_S"], 2)
        self.assertEqual(row["global_capacity_deficit"], 2)
        self.assertEqual(row["exact_exception_mass"], 4)
        self.assertEqual(row["local_Hall_excess_over_global_deficit"], 2)
        self.assertEqual(row["status"], "LOCAL-HALL-EXCESS")

    def test_synthetic_unsupported_source_is_local_excess_when_global_capacity_suffices(self):
        sources = {(0, 1, 2): 2, (8, 9, 10): 4}
        targets = {(0, 1, 2, 11, 12, 13): "D6"}
        row = local_excess_for_capacity(sources, targets, 99)
        self.assertEqual(row["global_capacity_deficit"], 0)
        self.assertEqual(row["exact_exception_mass"], 4)
        self.assertEqual(row["local_Hall_excess_over_global_deficit"], 4)
        self.assertTrue(row["unsupported_sources_can_contribute_to_local_excess"])

    def test_frontier_is_nonnegative_and_capacity_sorted(self):
        sources = {(0, 1, 2): 5, (2, 3, 4): 3}
        targets = {
            (0, 1, 2, 10, 11, 12): "D6",
            (2, 3, 4, 13, 14, 15): "B/B-overlap",
        }
        frontier = local_excess_frontier(sources, targets, [4, 2, 3])
        self.assertEqual([row["capacity_K"] for row in frontier["frontier"]], [2, 3, 4])
        self.assertTrue(frontier["local_excess_always_nonnegative"])
        self.assertTrue(frontier["exception_minus_global_deficit_verified"])
        self.assertEqual(frontier["max_local_Hall_excess_over_frontier"], 0)

    def test_complete_w32_k_minus_one_rows_have_no_local_excess(self):
        data = report()
        self.assertEqual(data["slice"], "HYP105-ISSUE230-D6G-LOCAL-HALL-EXCESS-ENVELOPE")
        self.assertEqual(data["all_h_local_excess_bound"], "OPEN")
        expected = {
            "lex": (942, 259, 4, 165),
            "reverse": (898, 169, 6, 53),
            "S68": (606, 68, 9, 62),
            "S72": (658, 72, 10, 10),
        }
        rows = data["W32_COMPLETE_positive_all_seven_local_excess_envelopes"]
        self.assertEqual(len(rows), 4)
        for row in rows:
            C, S, K, km1_deficit = expected[row["scheme"]]
            self.assertEqual(row["C_blocked_oriented"], C)
            self.assertEqual(row["full_seven_positive_S"], S)
            self.assertEqual(row["D6D_exact_zero_exception_K"], K)
            km1 = row["K_minus_one_local_excess"]
            self.assertEqual(km1["global_capacity_deficit"], km1_deficit)
            self.assertEqual(km1["exact_exception_mass"], km1_deficit)
            self.assertEqual(km1["local_Hall_excess_over_global_deficit"], 0)
            self.assertTrue(row["frontier"]["local_excess_always_nonnegative"])


if __name__ == "__main__":
    unittest.main()
