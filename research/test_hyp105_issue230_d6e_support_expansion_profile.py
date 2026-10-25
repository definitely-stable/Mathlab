"""D6-E source-closed Hall support-expansion profile tests."""
import unittest
from collections import Counter

from hyp105_issue230_d6e_support_expansion_profile import (
    source_closed_support_profile,
    factored_cut_profile,
    finite_w32_support_expansion_report,
)


class SupportExpansionProfileTests(unittest.TestCase):
    def test_synthetic_source_closed_split_profile(self):
        sources = Counter({(0, 1, 2): 2, (1, 2, 3): 3, (7, 8, 9): 4})
        targets = {
            (0, 1, 2, 10, 11, 12): "D6",
            (3, 4, 5, 6, 13, 14): "B/B-overlap",
        }
        split = {
            "endpoint": Counter({(0, 1, 2): 1, (1, 2, 3): 3}),
            "internal": Counter({(0, 1, 2): 1, (7, 8, 9): 4}),
        }

        prof = source_closed_support_profile(
            sources, targets, {0, 1, 2, 3}, split, candidate_K=2
        )
        self.assertEqual(prof["source_closed_oriented_demand"], 5)
        self.assertEqual(prof["split_source_demand"], {"endpoint": 4, "internal": 1})
        self.assertEqual(prof["eligible_positive_original_sixsets_B"], 2)
        self.assertEqual(prof["minimal_K_required_by_this_F"], 3)
        self.assertEqual(prof["excess_over_candidate_K"], 1)
        self.assertTrue(prof["source_closed_uses_active_union_denominator"])

        bad = source_closed_support_profile(sources, targets, {7, 8, 9}, split, candidate_K=9)
        self.assertEqual(bad["source_closed_oriented_demand"], 4)
        self.assertEqual(bad["eligible_positive_original_sixsets_B"], 0)
        self.assertTrue(bad["denominator_zero_with_positive_demand"])
        self.assertEqual(bad["excess_over_candidate_K"], 4)

    def test_synthetic_factored_cut_profile_refines_to_source_closed_F(self):
        sources = Counter({(0, 1, 2): 2, (1, 2, 3): 3})
        targets = {
            (0, 1, 2, 10, 11, 12): "D6",
            (3, 4, 5, 6, 13, 14): "B/B-overlap",
        }
        split = {
            "endpoint": Counter({(0, 1, 2): 2}),
            "internal": Counter({(1, 2, 3): 3}),
        }
        obstruction = factored_cut_profile(sources, targets, 2, split)
        self.assertEqual(obstruction["status"], "EXACT-HALL-OBSTRUCTION")
        self.assertEqual(obstruction["residual_cut_strict_deficit"], 1)
        self.assertEqual(obstruction["source_closed_profile"]["minimal_K_required_by_this_F"], 3)
        self.assertEqual(obstruction["source_closed_profile"]["split_source_demand"],
                         {"endpoint": 2, "internal": 3})

        feasible = factored_cut_profile(sources, targets, 3, split)
        self.assertEqual(feasible["status"], "COMPLETE-HALL-FEASIBLE")
        self.assertEqual(feasible["value"], 5)

    def test_true_W32_complete_all_seven_D6E_profiles_are_global_floor_only(self):
        data = finite_w32_support_expansion_report()
        self.assertEqual(data["slice"], "HYP105-ISSUE230-D6E-SOURCE-SUPPORT-EXPANSION-PROFILE")
        expected = {"lex": (942, 259, 4), "reverse": (898, 169, 6),
                    "S68": (606, 68, 9), "S72": (658, 72, 10)}
        rows = data["W32_COMPLETE_positive_all_seven_source_closed_profiles"]
        self.assertEqual(set(expected), {row["scheme"] for row in rows})
        for row in rows:
            C, S, K = expected[row["scheme"]]
            self.assertEqual((row["C_blocked_oriented"], row["full_seven_positive_S"],
                              row["D6D_exact_optimal_K"]), (C, S, K))
            self.assertEqual(row["E_endpoint_bad"] + row["I_internal_only"], C)
            self.assertEqual(row["global_source_closed_profile"]["source_closed_oriented_demand"], C)
            self.assertEqual(row["global_source_closed_profile"]["eligible_positive_original_sixsets_B"], S)
            self.assertEqual(row["global_source_closed_profile"]["minimal_K_required_by_this_F"], K)
            self.assertEqual(row["global_source_closed_profile"]["split_source_demand"],
                             {"endpoint": row["E_endpoint_bad"], "internal": row["I_internal_only"]})
            self.assertEqual(row["K_profile"]["status"], "COMPLETE-HALL-FEASIBLE")
            self.assertEqual(row["K_minus_one_profile"]["status"], "EXACT-HALL-OBSTRUCTION")
            self.assertGreater(row["K_minus_one_profile"]["source_closed_profile"]["excess_over_candidate_K"], 0)
        self.assertEqual(data["all_h_uniform_support_expansion_bound"], "OPEN")


if __name__ == "__main__":
    unittest.main()
