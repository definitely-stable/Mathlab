"""HYP-105 #230 AA4-AA-SRC: nine genuine ORIGINAL GQ forest closure."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    CELL_NAMES,exact_W32_source_six_forest_universe,
)
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    two_uniform_complete_global_maps_full_seven_expectation,
)
from hyp105_issue230_d6aa4z_original_matching_moments import (
    all_h_two_new_selected_GF5_ensemble_sectors,
)
from hyp105_issue230_d6aa4aa_original_full_forest_closure import (
    TYPES,all_h_BB_disjoint_two_P2_source_capacity,
    exact_all_h_nine_source_forest_universes,
    full_seven_all_h_two_complete_global_uniform_expectation,
    independent_actual_true_GQ_two_P2_original_placement,
)

EXPECTED_W32={
    "A/A":1566360,"A/B":1666980,"B/A":1666980,
    "A/C":6225,"C/A":6225,"B/C":5220,"C/B":5220,
    "B/B-overlap":910080,"B/B-disjoint":707580,
}


class NineTrueOriginalSourceForestClosureTests(unittest.TestCase):
    def test_001_all_h_genuine_GQ_BB_disjoint_one_original_cross_or_common_neighbor(self):
        for h in range(1,19):
            s=1<<h
            z=all_h_BB_disjoint_two_P2_source_capacity(s)
            V,d,N=z["V"],z["d"],z["N_actual_original_incidence_IDs"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertEqual(d,s+1)
            self.assertEqual(N,V*d)
            n=z["three_exact_second_opposite_original_P2_types_per_first_root"]
            m=z["three_exact_residual_original_2matching_counts"]
            self.assertEqual(set(n),set(TYPES))
            self.assertEqual(set(m),set(TYPES))
            r=d-1
            self.assertEqual(
                n[TYPES[0]],(d-2)*comb(d-1,2)+2*r**3)
            self.assertEqual(
                n[TYPES[1]],2*r*r*comb(d-1,2)+(d-2)*r**3)
            self.assertEqual(
                n[TYPES[2]],(d-2)*r*r*comb(d-1,2))
            for tag,t,H in ((TYPES[0],1,0),(TYPES[1],0,1),(TYPES[2],0,0)):
                e=N-6*d+4+t
                answer=(comb(e,2)
                        -(2*V-6)*comb(d,2)
                        +(d-1)*(6*d-8-2*t)-H)
                self.assertEqual(m[tag],answer)
                self.assertEqual(z["three_source_type_geometry_details"][tag][
                    "original_remaining_incidence_edges"],e)
            self.assertEqual(
                z["source_original_B/B_disjoint_six_incidence_count"],
                V*comb(d,2)*sum(n[t]*m[t] for t in TYPES))
            self.assertTrue(z["all_h_true_GQ_unique_projection_and_girth8_PROVED"])
            self.assertTrue(z["original_source_only_NOT_physical_f_g_acceptance"])

    def test_002_TRUE_W32_full_8145060_original_six_ID_catalog_all_nine(self):
        independent=exact_W32_source_six_forest_universe(fixture(1,"lex"))
        self.assertEqual(independent["total_original_45_choose_6"],comb(45,6))
        self.assertEqual(independent["original_source_forest_universe"],EXPECTED_W32)
        actual=exact_all_h_nine_source_forest_universes(2)
        self.assertEqual(
            actual["all_nine_original_source_forest_cell_populations"],
            EXPECTED_W32)
        self.assertEqual(set(actual["all_nine_original_source_forest_cell_populations"]),
                         set(CELL_NAMES))
        self.assertEqual(actual["all_actual_original_six_Q_universe"],
                         comb(45,6))
        self.assertEqual(actual["all_nine_cells_total"],
                         sum(EXPECTED_W32.values()))
        self.assertTrue(actual["all_h_original_source_closed_catalog_PROVED"])
        self.assertTrue(actual["adversarial_GLOBAL_f_g_omega_s6_NOT_PROVED"])

    def test_003_TRUE_W32_exact_new_residual_source_2matching_golden(self):
        z=all_h_BB_disjoint_two_P2_source_capacity(2)
        self.assertEqual(z["genuine_original_LINE_centered_P2_roots"],45)
        self.assertEqual(
            z["three_exact_second_opposite_original_P2_types_per_first_root"],
            {TYPES[0]:17,TYPES[1]:16,TYPES[2]:4})
        self.assertEqual(
            z["three_exact_residual_original_2matching_counts"],
            {TYPES[0]:440,TYPES[1]:412,TYPES[2]:413})
        self.assertEqual(
            z["source_original_B/B_disjoint_six_incidence_count"],707580)

    def test_004_TRUE_W34_exact_all_h_source_BB_disjoint_finite_golden(self):
        z=all_h_BB_disjoint_two_P2_source_capacity(4)
        self.assertEqual(z["genuine_original_LINE_centered_P2_roots"],850)
        self.assertEqual(
            z["three_exact_second_opposite_original_P2_types_per_first_root"],
            {TYPES[0]:146,TYPES[1]:384,TYPES[2]:288})
        self.assertEqual(
            z["three_exact_residual_original_2matching_counts"],
            {TYPES[0]:78240,TYPES[1]:77848,TYPES[2]:77849})
        self.assertEqual(
            z["source_original_B/B_disjoint_six_incidence_count"],54176606400)
        all9=exact_all_h_nine_source_forest_universes(4)
        self.assertEqual(all9["all_nine_original_source_forest_cell_populations"][
            "B/B-disjoint"],54176606400)

    def test_005_independent_ACTUAL_GQ_W32_ALL_original_root_placement_types(self):
        # All 45 true original line-centered P2 roots; for each ALL 37
        # disjoint opposite point-centered actual original source P2.
        a=independent_actual_true_GQ_two_P2_original_placement(
            fixture(1,"S68"),sample_fixed_P2_roots=45,
            brute_force_first_roots=3)
        self.assertEqual(a["actual_original_line_centered_P2_roots_checked"],45)
        self.assertEqual(len(a["actual_original_root_rows"]),45)
        self.assertEqual(set(a["source_root_placement_witnesses_per_type"]),set(TYPES))
        for row in a["actual_original_root_rows"]:
            self.assertEqual(
                row["actual_opposite_SOURCE_P2_types"],
                {TYPES[0]:17,TYPES[1]:16,TYPES[2]:4})
        self.assertEqual(a["universal_BB_disjoint_source_count"],707580)
        self.assertTrue(a["strict_true_original_GQ_projection_validator"])

    def test_006_independent_ACTUAL_GQ_W34_point_line_source_root_oracle(self):
        z=independent_actual_true_GQ_two_P2_original_placement(
            fixture(2,"random"),sample_fixed_P2_roots=24,
            brute_force_first_roots=3)
        self.assertEqual(z["actual_original_line_centered_P2_roots_checked"],24)
        self.assertEqual(z["universal_BB_disjoint_source_count"],54176606400)
        expect={TYPES[0]:146,TYPES[1]:384,TYPES[2]:288}
        for row in z["actual_original_root_rows"]:
            self.assertEqual(row["actual_opposite_SOURCE_P2_types"],expect)
        self.assertEqual(len(z["source_root_placement_witnesses_per_type"]),3)

    def test_007_FULL_seven_GF5_all_h_exact_NEW_BB_disjoint_global_mean_W32(self):
        z=full_seven_all_h_two_complete_global_uniform_expectation(2)
        self.assertEqual(z["new_seventh_selected_BB_disjoint_mean"],
                         Fraction(6368220,1002001))
        self.assertEqual(z["previous_exact_six_selected_tags_mean"],
                         Fraction(3240036,20449))
        self.assertEqual(z["exact_full_seven_historical_GF5_selected_S_mean"],
                         Fraction(165129984,1002001))
        prior=two_uniform_complete_global_maps_full_seven_expectation(
            2,exact_W32_source_six_forest_universe(fixture(1,"lex"))[
                "original_source_forest_universe"])
        self.assertEqual(z["exact_all_seven_GF5_tag_means"],
                         prior["exact_tag_expectations"])
        self.assertEqual(z["exact_full_seven_historical_GF5_selected_S_mean"],
                         prior["exact_expected_seven_S"])
        self.assertEqual(
            z["exact_full_seven_selected_51palette_certified_numerator_mean"],
            prior["exact_expected_51palette_numerator"])
        self.assertTrue(z["root_HYP105_ISSUE230_OPEN"])
        self.assertTrue(z["both_maps_complete_uniform_global_NOT_adversarial_all_f_g"])

    def test_008_FULL_seven_GF5_all_h_exact_NEW_BB_disjoint_global_mean_W34(self):
        z=full_seven_all_h_two_complete_global_uniform_expectation(4)
        self.assertEqual(z["new_seventh_selected_BB_disjoint_mean"],
                         Fraction(121897364400,6661561))
        self.assertEqual(z["exact_full_seven_historical_GF5_selected_S_mean"],
                         Fraction(4960589766387600,12317226289))
        self.assertEqual(len(z["exact_all_seven_GF5_tag_means"]),7)
        self.assertGreater(
            z["exact_full_seven_selected_51palette_certified_numerator_mean"],0)

    def test_009_all_h_source_BB_disjoint_and_full_seven_GQ_asymptotic(self):
        # The leading powers are analytical consequences of integer
        # all-h polynomial formulas and without-replacement probabilities.
        for h in range(1,18):
            s=1<<h
            z=full_seven_all_h_two_complete_global_uniform_expectation(s)
            self.assertEqual(z["leading_original_BB_disjoint_source_over_s18"],
                             Fraction(1,8))
            self.assertEqual(z["leading_expected_BB_disjoint_over_s6"],18)
            self.assertEqual(z["leading_all_seven_GF5_selected_S_over_s6"],
                             Fraction(1070,3))
            self.assertTrue(z["both_maps_complete_uniform_global_NOT_adversarial_all_f_g"])
            self.assertFalse(z["ASET_PROVED"])
            if s>=2048:
                q=z["new_seventh_selected_BB_disjoint_mean"]/s**6
                self.assertLess(abs(q-18),Fraction(3,2))
                p=z["exact_full_seven_historical_GF5_selected_S_mean"]/s**6
                self.assertLess(abs(p-Fraction(1070,3)),Fraction(50))

    def test_010_invalid_ORIGINAL_source_GQ_fake_C6_and_noninjective_maps(self):
        base=fixture(1,"lex")
        fake={**base,"incidences":tuple(
            (p,l) for l in range(15) for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaises(ValueError):
            independent_actual_true_GQ_two_P2_original_placement(fake)
        bad={**base,"left_labels":tuple(
            [base["left_labels"][0]]*len(base["left_labels"]))}
        with self.assertRaises(ValueError):
            independent_actual_true_GQ_two_P2_original_placement(bad)
        for s in (0,1,3,5,6,True,2.0,-4):
            with self.assertRaises(ValueError):
                all_h_BB_disjoint_two_P2_source_capacity(s)
        self.assertNotEqual(
            all_h_BB_disjoint_two_P2_source_capacity(2)[
                "source_original_B/B_disjoint_six_incidence_count"],
            0)


if __name__=="__main__":
    unittest.main()
