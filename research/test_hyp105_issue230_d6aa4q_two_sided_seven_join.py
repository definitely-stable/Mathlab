"""D6-AA4-Q independent true ORIGINAL GQ two-sided seven-GF5 join tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model,
    exact_ONE_side_original_projection_index,
    exact_two_sided_original_seven_join,
    all_h_source_girth_and_side_count_identity,
    independent_joint_classify,
)


class AllSevenTwoSidedOriginalJoinTests(unittest.TestCase):
    def test_001_independent_both_half_full_original_W32_62370_candidates(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            for side in (0,1):
                z=exact_ONE_side_original_projection_index(m,side)
                self.assertEqual(z["original_sixset_count"],62370)
                self.assertEqual(z["candidate_class_marginals"],
                                 {"A":51030,"B":10935,"C":405})
                self.assertEqual(len(z["candidate_sixset_map"]),62370)
                self.assertEqual(len(set(z["candidate_sixset_map"])),62370)
                for Q,tag in list(z["candidate_sixset_map"].items())[:50]:
                    self.assertEqual(len(Q),6)
                    self.assertEqual(len(set(Q)),6)
                    mult=tuple(sorted(Counter(m["incidences"][i][side]
                                                   for i in Q).values(),reverse=True))
                    self.assertEqual(mult,{"A":(1,)*6,
                                            "B":(2,1,1,1,1),
                                            "C":(2,2,2)}[tag])

    def test_002_true_original_all_7_historical_GF5_classes_match_independent_join(self):
        known={"lex":259,"reverse":169,"S68":68,"S72":72}
        for scheme,S in known.items():
            m=fixture(1,scheme)
            z=exact_two_sided_original_seven_join(m,collect=True)
            legacy=seven_census(m,independent_checks=False,witness_sets=True)
            self.assertEqual(z["accepted_seven_GF5_original_S"],S)
            self.assertEqual(z["accepted_seven_GF5_original_Q_by_tag"],
                             legacy["seven_class_motif_counts"])
            self.assertEqual(z["selected_GF5_51palette_certified_numerator"],
                             legacy["GF5_seven_lower_numerator"])
            self.assertEqual(z["selected_ORIGINAL_Q_tags"],legacy["sets"])
            self.assertEqual(z["forbidden_original_GQ_C_C_sixsets"],0)
            self.assertEqual(z["physical_A_A_genuine_D6_only"],
                             legacy["seven_class_motif_counts"]["D6"])
            self.assertEqual(sum(z["physical_projection_source_3x3_joint_matrix"].values()),
                             z["exact_source_original_Q_double_projection_intersection"])
            self.assertEqual(z["physical_A_A_nonD6_rejected"]+
                             z["physical_A_A_genuine_D6_only"],
                             z["physical_A_A_joint_candidates"])
            self.assertTrue(z["same_global_complete_f_g_both_side_join"])
            self.assertTrue(z["retains_true_six_ORIGINAL_incidence_IDs"])
            self.assertFalse(z["S_full_root_all_h_omega_s6_PROVED"])

    def test_003_3by3_true_original_joint_structural_no_C_C_all_h(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            z=exact_two_sided_original_seven_join(m)
            a=z["physical_projection_source_3x3_joint_matrix"]
            self.assertEqual(len(a),9)
            self.assertEqual(a["C/C"],0)
            self.assertTrue(z["all_h_no_C_C_original_GQ_incidence_girth_six_PROVED"])
            self.assertGreaterEqual(a["A/A"],z["physical_A_A_genuine_D6_only"])
            self.assertGreaterEqual(a["B/A"],z["accepted_seven_GF5_original_Q_by_tag"]["B-left/A-right"])
            self.assertGreaterEqual(a["A/B"],z["accepted_seven_GF5_original_Q_by_tag"]["A-left/B-right"])
            self.assertGreater(z["candidate_P_total"],z["accepted_seven_GF5_original_S"])
            self.assertGreater(z["candidate_L_total"],z["accepted_seven_GF5_original_S"])

    def test_004_real_original_W32_FULL_global_random_both_type_injections(self):
        rng=random.Random(2300473)
        edges=list(combinations(range(6),2))
        m=fixture(1,"lex")
        for _ in range(5):
            rng.shuffle(edges);left=tuple(edges)
            rng.shuffle(edges);right=tuple(edges)
            current={**m,"left_labels":left,"right_labels":right}
            z=exact_two_sided_original_seven_join(current)
            old=seven_census(current,independent_checks=False)
            self.assertEqual(z["accepted_seven_GF5_original_S"],old["S_seven"])
            self.assertEqual(z["selected_GF5_51palette_certified_numerator"],
                             old["GF5_seven_lower_numerator"])
            self.assertEqual(z["physical_projection_source_3x3_joint_matrix"]["C/C"],0)

    def test_005_true_original_S72_literal_BA_adversarial_minimizer_still_all7(self):
        m=fixture(1,"S72")
        point_labels=((1,3),(3,5),(1,4),(0,2),(1,2),
                      (0,3),(2,3),(2,5),(4,5),(0,5),
                      (3,4),(1,5),(0,4),(0,1),(2,4))
        alternate={**m,"left_labels":point_labels}
        base=exact_two_sided_original_seven_join(m)
        alt=exact_two_sided_original_seven_join(alternate)
        self.assertEqual(base["accepted_seven_GF5_original_S"],72)
        self.assertEqual(alt["accepted_seven_GF5_original_S"],102)
        self.assertEqual(base["exact_independent_half_marginal_counts"],
                         alt["exact_independent_half_marginal_counts"])
        self.assertEqual(base["candidate_P_total"],62370)
        self.assertEqual(alt["candidate_L_total"],62370)
        self.assertNotEqual(base["accepted_seven_GF5_original_Q_by_tag"],
                            alt["accepted_seven_GF5_original_Q_by_tag"])
        self.assertEqual(alt["independent_historical_62370_original_Q_oracle"],"PASS")

    def test_006_all_h_source_degree_and_no_C_C_symbolic_identity(self):
        for h in range(1,12):
            s=1<<h
            V=(s+1)*(s*s+1)
            a=6
            while a*(a-1)//2<V:
                a+=1
            params=all_h_source_girth_and_side_count_identity(
                s,a,70,45,15)
            d=s+1
            self.assertEqual(params["A_original_sixset_candidates"],70*d**6)
            self.assertEqual(params["B_original_sixset_candidates"],45*
                             (d*(d-1)//2)*d**4)
            self.assertEqual(params["C_original_sixset_candidates"],15*
                             (d*(d-1)//2)**3)
            self.assertTrue(params["C_C_source_congruence_impossible_for_true_GQ"])
            self.assertFalse(params["any_all_h_joint_positive_lower_derived_from_half_marginals"])
        self.assertEqual(
            all_h_source_girth_and_side_count_identity(2,6,70,45,15)[
               "A_original_sixset_candidates"],51030)
        self.assertEqual(
            all_h_source_girth_and_side_count_identity(2,6,70,45,15)[
               "B_original_sixset_candidates"],10935)
        self.assertEqual(
            all_h_source_girth_and_side_count_identity(2,6,70,45,15)[
               "C_original_sixset_candidates"],405)

    def test_007_fail_closed_improper_model_and_source_half(self):
        m=fixture(1,"S68")
        for side in (-1,2,True):
            with self.assertRaises(ValueError):
                exact_ONE_side_original_projection_index(m,side)
        with self.assertRaises(ValueError):
            exact_two_sided_original_seven_join({**m,"left_labels":
                   tuple(m["left_labels"][:-1])+tuple(m["left_labels"][:1])})
        with self.assertRaises(ValueError):
            exact_two_sided_original_seven_join({**m,"right_labels":
                   tuple(m["right_labels"][:-1])+tuple(m["right_labels"][:1])})
        with self.assertRaises(ValueError):
            strict_true_W32_model({**m,"incidences":tuple(m["incidences"])[:-1]})
        with self.assertRaises(ValueError):
            all_h_source_girth_and_side_count_identity(3,6,1,1,1)
        with self.assertRaises(ValueError):
            all_h_source_girth_and_side_count_identity(4,6,1,1,1)


if __name__=="__main__":
    unittest.main()
