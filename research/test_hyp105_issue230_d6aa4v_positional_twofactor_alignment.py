"""HYP-105 AA4-V: all-h six-column positional C6 mismatch, genuine W32 tests."""
import random
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import _K6_2factors
from hyp105_issue230_d6aa4v_positional_twofactor_alignment import (
    ALL_TYPES, EXPECTED_ROW_COUNTS,
    physical_twofactor_kind, independent_all_70_positional_twofactors,
    all_h_positional_twofactor_overlap_theorem,
    genuine_W32_same_original_Q_positional_alignment,
)


class TrueOriginalPositionalTwofactorAlignmentTests(unittest.TestCase):
    def test_001_all_h_exact_70x70_twofactor_overlap_kernel_and_quantifiers(self):
        for h in range(1,13):
            result=all_h_positional_twofactor_overlap_theorem(1<<h)
            self.assertEqual(result["full_70_by_70_ordered_positional_factor_pairs"],4900)
            self.assertEqual(result["num_connected_C6_positional_factors"],60)
            self.assertEqual(result["num_disconnected_2C3_positional_factors"],10)
            self.assertEqual(
                {k:{int(r):n for r,n in x.items()}
                 for k,x in result["row_distribution_by_first_type"].items()},
                EXPECTED_ROW_COUNTS)
            self.assertEqual(result["distinct_connected_C6_common_original_position_adjacencies_max"],4)
            self.assertTrue(result["no_five_edge_connected_cycle_mismatch_ALL_H"])
            self.assertTrue(result["equal_disconnected_2C3_must_NOT_count_as_D6"])
            self.assertFalse(result["uniform_positive_minimum_s6_PROVED"])
            self.assertEqual(
                sum(sum(v.values()) for v in result["ordered_pair_overlap_counts"].values()),
                4900)

    def test_002_independently_check_physical_K6_twofactor_70_and_C6_no_five_overlap(self):
        F=independent_all_70_positional_twofactors()
        from_repo={frozenset(p) for p in _K6_2factors()}
        self.assertEqual({f for f,_ in F},from_repo)
        self.assertEqual(Counter(kind for _,kind in F),{"C":60,"T":10})
        for x,kx in F:
            for y,ky in F:
                r=len(x&y)
                if kx==ky=="C" and x!=y:
                    self.assertLessEqual(r,4)
                if r==6:
                    self.assertEqual(x,y)
                    self.assertEqual(kx,ky)
                self.assertNotEqual(r,5)

    def test_003_full_original_four_coherent_global_K6_maps_reconcile_GF5(self):
        expectedS={"S68":68,"S72":72,"lex":259,"reverse":169}
        expectedAA={"S68":263,"S72":286,"lex":364,"reverse":309}
        expectedD={"S68":0,"S72":0,"lex":15,"reverse":3}
        for name in expectedS:
            x=genuine_W32_same_original_Q_positional_alignment(fixture(1,name))
            self.assertEqual(x["actual_A_A_original_sixset_count"],expectedAA[name])
            self.assertEqual(x["actual_A_A_genuine_connected_D6"],expectedD[name])
            self.assertEqual(x["real_full_selected_original_seven_S"],expectedS[name])
            self.assertEqual(
                x["same_original_Q_two_sided_joint"],
                expectedS[name]+expectedAA[name]-expectedD[name])
            self.assertEqual(
                x["actual_non_A_A_accepted_seven"],
                expectedS[name]-expectedD[name])
            self.assertEqual(
                sum(x["AA_physical_dual_type_and_positional_overlap_histogram"].values()),
                expectedAA[name])
            self.assertEqual(
                x["CC_overlap_histogram"]["6"],expectedD[name])
            self.assertLessEqual(
                x["deterministic_all_h_D6_lower_by_CC_adjacency_threshold"],
                expectedD[name])
            self.assertLessEqual(
                x["deterministic_all_h_S_lower_using_exact_nonAA_and_CC_threshold"],
                expectedS[name])
            self.assertEqual(x["independent_full_seven_history"],"PASS")
            self.assertFalse(x["certifies_uniform_all_h_root_omega_s6"])

    def test_004_zero_D6_true_S68_S72_must_not_deduce_from_near_alignment(self):
        for name in ("S68","S72"):
            x=genuine_W32_same_original_Q_positional_alignment(
                fixture(1,name),check_history=False)
            self.assertEqual(x["actual_A_A_genuine_connected_D6"],0)
            self.assertEqual(x["deterministic_all_h_D6_lower_by_CC_adjacency_threshold"],0)
            self.assertLessEqual(
                x["actual_A_A_two_connected_C6_common_adjacency_sum"],
                4*x["actual_A_A_two_connected_C6_count"])
            self.assertEqual(
                x["exact_D6_from_E_minus_4M_plus_surplus_numerator"],0)
            self.assertEqual(x["actual_A_A_rejected"],x["actual_A_A_original_sixset_count"])

    def test_005_independent_seeded_random_complete_globally_injective_maps(self):
        rng=random.Random(23000431)
        edges=list(combinations(range(6),2))
        base=fixture(1,"lex")
        for _ in range(4):
            f=edges[:];g=edges[:]
            rng.shuffle(f);rng.shuffle(g)
            model={**base,"left_labels":tuple(f),"right_labels":tuple(g)}
            actual=genuine_W32_same_original_Q_positional_alignment(
                model,check_history=True)
            old=seven_census(model,independent_checks=False)
            self.assertEqual(actual["real_full_selected_original_seven_S"],
                             old["S_seven"])
            self.assertEqual(actual["original_51palette_weighted_selected_seven"],
                             old["GF5_seven_lower_numerator"])
            self.assertEqual(actual["actual_A_A_genuine_connected_D6"],
                             old["seven_class_motif_counts"]["D6"])

    def test_006_true_original_point_line_duality_preserves_D6_and_S(self):
        x=fixture(1,"reverse")
        reversed_source={**x,
                         "incidences":tuple((ell,p) for p,ell in x["incidences"]),
                         "left_labels":x["right_labels"],
                         "right_labels":x["left_labels"]}
        a=genuine_W32_same_original_Q_positional_alignment(x,check_history=False)
        b=genuine_W32_same_original_Q_positional_alignment(reversed_source,
                                                            check_history=False)
        self.assertEqual(a["real_full_selected_original_seven_S"],
                         b["real_full_selected_original_seven_S"])
        self.assertEqual(a["actual_A_A_genuine_connected_D6"],
                         b["actual_A_A_genuine_connected_D6"])
        self.assertEqual(a["actual_A_A_two_connected_C6_count"],
                         b["actual_A_A_two_connected_C6_count"])
        self.assertEqual(a["actual_A_A_two_connected_C6_common_adjacency_sum"],
                         b["actual_A_A_two_connected_C6_common_adjacency_sum"])
        self.assertEqual(
            a["AA_physical_dual_type_and_positional_overlap_histogram"]["C/T:r2"],
            b["AA_physical_dual_type_and_positional_overlap_histogram"]["T/C:r2"])

    def test_007_reject_fake_GQ_with_source_6cycle_and_noninjective_map(self):
        base=fixture(1,"lex")
        fake={**base,"incidences":tuple((p,ell) for ell in range(15)
                                      for p in (ell,(ell+1)%15,(ell+3)%15))}
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            genuine_W32_same_original_Q_positional_alignment(fake)
        bad=list(base["right_labels"]);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            genuine_W32_same_original_Q_positional_alignment(
                {**base,"right_labels":tuple(bad)})

    def test_008_a_equal_disconnected_2triangle_is_NOT_a_D6_witness(self):
        F=independent_all_70_positional_twofactors()
        disconnected=[edge for edge,kind in F if kind=="T"]
        self.assertEqual(len(disconnected),10)
        for h in disconnected:
            self.assertEqual(physical_twofactor_kind(tuple(h)),"T")
            self.assertEqual(len(h&h),6)
        with self.assertRaises(AssertionError):
            physical_twofactor_kind(((0,1),(1,0),(2,3),(3,4),(4,5),(5,2)))
        with self.assertRaises(AssertionError):
            physical_twofactor_kind(((0,1),(1,2),(2,0),(3,4),(4,5),(5,6)))


if __name__=="__main__":
    unittest.main()
