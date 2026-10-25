"""D6-AA4-L exact true ORIGINAL GF5 charged-moment and isolated flag tests."""
import random
import unittest
from fractions import Fraction
from itertools import combinations
from math import factorial

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4i_original_spectral_coordinate import geometry
from hyp105_issue230_d6aa4k_projection_aware_charge import true_original_projection_charge
from hyp105_issue230_d6aa4l_charge_energy_obstruction import (
    separated_original_flag_count_theorem, genuine_original_W38_zero_charge_positive_D6,
    threshold_average_charge,original_pair_energy,_select_six_original_separated_flags,
    _true_source_geometry_incidence_lists,
)


class OriginalSourcePairEnergyTests(unittest.TestCase):
    def test_001_all_h_s16_onward_six_fully_original_source_separated_flag_count(self):
        for h in range(4,12):
            s=2**h
            r=separated_original_flag_count_theorem(s)
            self.assertEqual(r["s"],s)
            self.assertEqual(r["V"],(s+1)*(s*s+1))
            self.assertEqual(r["original_closed_collinear_source_neighborhood"],1+s*(s+1))
            self.assertEqual(len(r["conservative_valid_next_original_flag_counts"]),6)
            self.assertGreater(min(r["conservative_valid_next_original_flag_counts"]),0)
            p=1
            for n in r["conservative_valid_next_original_flag_counts"]:p*=n
            self.assertEqual(p,r["guaranteed_distinct_ordered_six_original_flags"])
            self.assertEqual(r["guaranteed_distinct_unordered_six_flag_sets"],
                             (p+factorial(6)-1)//factorial(6))
            self.assertTrue(r["all_six_source_points_pairwise_NONCOLLINEAR"])
            self.assertTrue(r["all_six_source_lines_pairwise_NONCONCURRENT"])
            self.assertFalse(r["seven_GF5_all_h_total_charge_bound_NOT_proved"] is False)
        for bad in (0,2,4,8,17,True,-16):
            with self.assertRaises(ValueError):
                separated_original_flag_count_theorem(bad)

    def test_002_true_original_W38_both_type_zero_charge_single_positive_GF5_D6(self):
        w=genuine_original_W38_zero_charge_positive_D6()
        self.assertEqual((w["s"],w["V"],w["true_original_incidence_count"]),
                         (8,585,5265))
        self.assertTrue(w["complete_GLOBAL_point_and_line_injections_verified"])
        self.assertEqual(w["genuine_historical_GF5_class"],"D6")
        self.assertEqual(w["certified_selected_GF5_Q_numerator"],5643)
        self.assertEqual(w["actual_physically_disjoint_point_pairs_in_Q"],9)
        self.assertEqual(w["actual_physically_disjoint_line_pairs_in_Q"],9)
        self.assertEqual(w["actual_ELIGIBLE_source_collinear_point_pairs_in_Q"],0)
        self.assertEqual(w["actual_ELIGIBLE_source_concurrent_line_pairs_in_Q"],0)
        self.assertTrue(w["positive_original_GF5_Q_with_zero_joint_charge_PROVED"])
        self.assertTrue(w["entire_real_W38_positive_sixset_census_NOT_executed"])
        self.assertTrue(w["does_not_construct_global_I_zero_family"])
        self.assertEqual(len(set(w["chosen_original_six_incidence_IDs"])),6)
        self.assertEqual(len(set(w["chosen_original_six_source_points"])),6)
        self.assertEqual(len(set(w["chosen_original_six_source_lines"])),6)

    def test_003_independent_real_original_W38_no_collinear_or_concurrent_flags(self):
        model=fixture(3,"lex")
        flags,seed=_select_six_original_separated_flags(model)
        inc,AP,AL=_true_source_geometry_incidence_lists(model)
        self.assertEqual(len(flags),6)
        self.assertLess(seed,64)
        self.assertTrue(all(x in inc for x in flags))
        for (p,l),(q,r) in combinations(flags,2):
            self.assertNotEqual(p,q)
            self.assertNotEqual(l,r)
            self.assertNotIn(q,AP[p])
            self.assertNotIn(r,AL[l])

    def test_004_finite_threshold_quantile_exact_degree_certificates(self):
        ds=(0,0,1,2,3,9,11)
        for threshold in (1,2,4,8,16,32):
            r=threshold_average_charge(ds,threshold)
            self.assertEqual(r["original_source_pair_count"],len(ds))
            self.assertEqual(r["total_actual_charge"],sum(ds))
            expected=sum(x>=threshold for x in ds)
            self.assertEqual(r["pairs_with_at_least_threshold_positive_Q"],expected)
            self.assertEqual(r["fraction_pairs_above_threshold"],
                             str(Fraction(expected,len(ds))))
            self.assertEqual(r["valid_S_lower_from_actual_threshold"],
                             -(-expected*threshold//9))
            self.assertTrue(r["global_large_s_positive_fraction_hypothesis_NOT_proved"])
        for bad in (0,-1,True,3.14):
            with self.assertRaises(ValueError):
                threshold_average_charge((1,2),bad)
        with self.assertRaises(ValueError):
            threshold_average_charge((),1)
        with self.assertRaises(ValueError):
            threshold_average_charge((1,-1),1)
        with self.assertRaises(ValueError):
            threshold_average_charge((True,3),1)

    def test_005_actual_ORIGINAL_W32_four_pinned_GF5_models_both_side_Gram(self):
        for scheme,expected in (("lex",259),("reverse",169),
                                ("S68",68),("S72",72)):
            m=fixture(1,scheme)
            g=geometry(2,m["incidences"])
            c=seven_census(m,independent_checks=False,witness_sets=True)
            self.assertEqual(c["S_seven"],expected)
            energy=[]
            for typ in ("P","L"):
                r=original_pair_energy(g,m,c["sets"],typ)
                self.assertEqual(r["actual_accepted_original_seven_GF5_Q"],expected)
                self.assertTrue(r["gram_energy_identity_independent_verified"])
                self.assertTrue(r["cauchy_energy_inequality_verified"])
                self.assertEqual(r["full_original_pair_major_audit"],"PASS")
                self.assertGreaterEqual(r["true_source_eligible_pairs"],9)
                self.assertLessEqual(r["true_total_pair_Q_charge"],9*expected)
                self.assertEqual(r["source_pair_positive_Q_degree_second_moment"],
                                 r["independent_ORIGINAL_Q_major_Gram"])
                for k,threshold in r["threshold_certificates"].items():
                    self.assertEqual(int(k),threshold["threshold"])
                    self.assertEqual(threshold["original_source_pair_count"],
                                     r["true_source_eligible_pairs"])
                energy.append(r["true_total_pair_Q_charge"])
            charge=true_original_projection_charge(g,m,c["sets"])
            self.assertEqual(tuple(energy),(charge["source_P_charge"],
                                             charge["source_L_charge"]))

    def test_006_random_real_W32_full_point_line_injections_GF5_Gram(self):
        m=fixture(1,"lex")
        g=geometry(2,m["incidences"])
        edges=list(combinations(range(6),2))
        rng=random.Random(2300444)
        for _ in range(5):
            rng.shuffle(edges);left=tuple(edges)
            rng.shuffle(edges);right=tuple(edges)
            current={**m,"left_labels":left,"right_labels":right}
            c=seven_census(current,independent_checks=False,witness_sets=True)
            for typ in ("P","L"):
                r=original_pair_energy(g,current,c["sets"],typ)
                self.assertEqual(r["actual_accepted_original_seven_GF5_Q"],
                                 c["S_seven"])
                self.assertEqual(r["full_original_pair_major_audit"],"PASS")
                self.assertGreaterEqual(r["source_pair_positive_Q_degree_second_moment"],0)

    def test_007_illegal_original_pair_Q_inputs_fail_closed(self):
        m=fixture(1,"S68")
        g=geometry(2,m["incidences"])
        with self.assertRaises(ValueError):
            original_pair_energy(g,m,{},"X")
        with self.assertRaises(ValueError):
            original_pair_energy(g,m,{(0,1,2,3,4,45):"D6"},"P")
        with self.assertRaises(ValueError):
            original_pair_energy(g,m,{(0,1,2,3,4,5):"FAKE"},"P")

    def test_008_S72_genuine_zero_degree_original_line_pair_remains_visible(self):
        m=fixture(1,"S72")
        g=geometry(2,m["incidences"])
        c=seven_census(m,independent_checks=False,witness_sets=True)
        r=original_pair_energy(g,m,c["sets"],"L")
        self.assertGreaterEqual(r["exact_zero_charge_source_pair_count"],1)
        self.assertEqual(r["minimum_eligible_pair_positive_Q_degree"],0)
        self.assertGreaterEqual(r["true_source_eligible_pairs"],20)


if __name__=="__main__":
    unittest.main()
