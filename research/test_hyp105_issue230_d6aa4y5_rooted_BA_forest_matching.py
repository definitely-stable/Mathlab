"""Independent original GQ B/A and A/B root-pair source forest matching tests."""
import random
import unittest
from itertools import product
from math import comb

from hyp105_issue230_d6aa4y5_rooted_BA_forest_matching import (
    original_four_source_injective_matching,
    original_BA_root_pair_universal_bounds,
    genuine_W32_rooted_BA_forest,
    _partitions,
)


def independent_direct_permanent(neighbors):
    return sum(len(set(x))==4 for x in product(*neighbors))


class OriginalBARootPairMatchingTests(unittest.TestCase):
    def test_001_four_source_partition_mobius_exact_15_partitions(self):
        self.assertEqual(len(list(_partitions(range(4)))),15)
        self.assertEqual(
            original_four_source_injective_matching(
                ({0,1,2,3},)*4),24)
        self.assertEqual(
            original_four_source_injective_matching(
                ({0,1,2},)*4),0)
        self.assertEqual(
            original_four_source_injective_matching(
                ({0,1,2},{3,4,5},{6,7,8},{9,10,11})),81)
        self.assertEqual(
            original_four_source_injective_matching(((),(),(),())),0)
        with self.assertRaises(ValueError):
            original_four_source_injective_matching(((0,),)*3)

    def test_002_independent_literal_random_finite_rook_sets(self):
        rng=random.Random(230505)
        for _ in range(400):
            sets=tuple(set(rng.sample(range(9),rng.randrange(0,6)))
                       for _ in range(4))
            self.assertEqual(
                original_four_source_injective_matching(sets),
                independent_direct_permanent(sets))

    def test_003_all_h_rooted_GQ_original_lower_bound_without_physical_A_claim(self):
        for h in range(1,17):
            s=1<<h
            row=original_BA_root_pair_universal_bounds(s)
            d=s+1
            self.assertEqual(row["max_true_original_B_A_source_forest_six_Q_per_root_flag_pair"],
                             3*comb(row["a"]-2,4)*d**4)
            self.assertGreaterEqual(row[
                "per_REALIZED_root_C4_pattern_distinct_opposite_A_source_lower"],0)
            self.assertLessEqual(row[
                "per_REALIZED_root_C4_pattern_distinct_opposite_A_source_lower"],d**4)
            self.assertTrue(row["all_h_exact_source_BA_A_B_forest_permanent_PROVED"])
            self.assertTrue(row["historical_GF5_opposite_physical_A_also_needed"])
            self.assertFalse(row["root_all_h_seven_S_omega_s6_PROVED"])
            self.assertEqual(row["positive_per_REALIZED_B_C4_for_s_ge_4"],s>=4)
        w32=original_BA_root_pair_universal_bounds(2)
        self.assertEqual((w32["d"],w32["a"]), (3,6))
        self.assertEqual(w32["physical_Ka_C4_candidates_per_prescribed_root_edge"],3)
        self.assertEqual(w32["max_true_original_B_A_source_forest_six_Q_per_root_flag_pair"],243)
        self.assertEqual(w32["per_REALIZED_root_C4_pattern_distinct_opposite_A_source_lower"],0)

    def test_004_all_45_real_original_W32_B_root_pair_flag_cohorts_and_GF5(self):
        x=genuine_W32_rooted_BA_forest("S68")
        self.assertEqual(x["scheme"],"S68")
        for tag in ("B-left/A-right","A-left/B-right"):
            row=x["per_historical_GF5_BA_tag"][tag]
            self.assertEqual(row["real_original_root_factors"],15)
            self.assertEqual(row["root_fixed_two_distinct_flag_pairs"],45)
            self.assertEqual(row["physical_B_candidate_original_six_IDs"],10935)
            self.assertTrue(row[
                "all_45_true_original_root_flag_pairs_independently_brute_checked"])
            self.assertTrue(row["all_10935_original_B_half_Q_checked"])
            self.assertEqual(row[
                "original_BA_rooted_51palette_historical_GF5_crosscheck"],"PASS")
            self.assertEqual(
                row["true_source_opposite_A_failures"]
                +row["true_source_BA_forest_opposite_physical_A_failures"]
                +row["historical_positive_GF5_accepted_BA_six_IDs"],10935)
            self.assertGreater(row["true_source_BA_forest_potential_six_IDs"],0)
            self.assertGreater(row["historical_positive_GF5_accepted_BA_six_IDs"],0)
        self.assertEqual(x["root_A"],"OPEN")

    def test_005_finite_separate_original_label_anchor(self):
        # Independently verify the opposite finite source labeling,
        # with the SAME original GQ incidence graph.
        z=genuine_W32_rooted_BA_forest("S72")
        self.assertEqual(z["scheme"],"S72")
        self.assertTrue(z["six_original_incidence_IDs_not_physical_pseudo_forests"])
        self.assertTrue(z["genuine_complete_GLOBAL_point_line_maps_not_independent_per_Q"])
        for key,row in z["per_historical_GF5_BA_tag"].items():
            self.assertEqual(row["root_fixed_two_distinct_flag_pairs"],45)
            self.assertEqual(row["original_BA_rooted_51palette_historical_GF5_crosscheck"],"PASS")


if __name__=="__main__":
    unittest.main()
