"""D6-F exact exception-budget oracle tests for HYP-105 issue #230."""
import unittest

from hyp105_issue230_d6f_exception_budget_oracle import (
    exception_budget_for_capacity,
    exception_frontier,
    minimal_capacity_for_exception_budget,
    report,
)


class ExceptionBudgetOracleTests(unittest.TestCase):
    def test_synthetic_budget_is_exact_and_monotone(self):
        sources = {(0, 1, 2): 5, (2, 3, 4): 3}
        targets = {
            (0, 1, 2, 10, 11, 12): "D6",
            (2, 3, 4, 13, 14, 15): "B/B-overlap",
        }
        split = {
            "endpoint": {(0, 1, 2): 5, (2, 3, 4): 0},
            "internal": {(0, 1, 2): 0, (2, 3, 4): 3},
        }

        at_two = exception_budget_for_capacity(sources, targets, 2, split)
        at_three = exception_budget_for_capacity(sources, targets, 3, split)
        at_five = exception_budget_for_capacity(sources, targets, 5, split)

        self.assertEqual(at_two["minimal_exception_mass"], 4)
        self.assertEqual(at_three["minimal_exception_mass"], 2)
        self.assertEqual(at_five["minimal_exception_mass"], 0)
        self.assertEqual(at_three["max_chargeable_mass"], 6)
        self.assertEqual(at_three["exception_split_lower_hint"], {"endpoint": 0, "internal": 0})
        self.assertLessEqual(
            sum(at_three["exception_split_lower_hint"].values()),
            at_three["minimal_exception_mass"],
        )
        self.assertEqual(at_three["status"], "EXACT-EXCEPTION-BUDGET")
        self.assertEqual(at_five["status"], "ZERO-EXCEPTION-FEASIBLE")

        frontier = exception_frontier(sources, targets, [5, 2, 3], split)
        self.assertEqual([x["capacity_K"] for x in frontier["frontier"]], [2, 3, 5])
        self.assertEqual([x["minimal_exception_mass"] for x in frontier["frontier"]], [4, 2, 0])
        self.assertTrue(frontier["exception_mass_nonincreasing_in_K"])
        self.assertTrue(frontier["max_chargeable_mass_nondecreasing_in_K"])

        self.assertEqual(
            minimal_capacity_for_exception_budget(sources, targets, 0, split)["minimum_capacity_K"],
            5,
        )
        self.assertEqual(
            minimal_capacity_for_exception_budget(sources, targets, 2, split)["minimum_capacity_K"],
            3,
        )

    def test_unsupported_sources_become_irreducible_exception_mass(self):
        sources = {(0, 1, 2): 2, (8, 9, 10): 4}
        targets = {(0, 1, 2, 11, 12, 13): "D6"}
        budget = exception_budget_for_capacity(sources, targets, 99)
        self.assertEqual(budget["minimal_exception_mass"], 4)
        self.assertEqual(budget["status"], "EXACT-EXCEPTION-BUDGET")

        impossible = minimal_capacity_for_exception_budget(sources, targets, 0)
        self.assertEqual(impossible["status"], "NO-FINITE-K-MEETS-BUDGET")
        self.assertEqual(impossible["irreducible_exception_mass"], 4)

    def test_complete_w32_d6f_rows_are_pinned(self):
        data = report()
        self.assertEqual(data["slice"], "HYP105-ISSUE230-D6F-EXCEPTION-BUDGET-ORACLE")
        self.assertEqual(data["all_h_exception_mass_bound"], "OPEN")
        expected = {
            "lex": (942, 259, 4, 165),
            "reverse": (898, 169, 6, 53),
            "S68": (606, 68, 9, 62),
            "S72": (658, 72, 10, 10),
        }
        rows = data["W32_COMPLETE_positive_all_seven_exception_frontiers"]
        self.assertEqual(len(rows), 4)
        for row in rows:
            C, S, K, km1_exception = expected[row["scheme"]]
            self.assertEqual(row["C_blocked_oriented"], C)
            self.assertEqual(row["full_seven_positive_S"], S)
            self.assertEqual(row["D6D_exact_zero_exception_K"], K)
            self.assertEqual(row["zero_exception_capacity"]["minimum_capacity_K"], K)
            self.assertEqual(row["K_minus_one_budget"]["minimal_exception_mass"], km1_exception)
            self.assertEqual(row["K_minus_one_global_source_closed_excess"], km1_exception)
            self.assertTrue(row["frontier"]["exception_mass_nonincreasing_in_K"])
            self.assertTrue(row["frontier"]["max_chargeable_mass_nondecreasing_in_K"])


if __name__ == "__main__":
    unittest.main()
