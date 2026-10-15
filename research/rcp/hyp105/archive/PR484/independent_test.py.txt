"""AA4-T independent all-h quenched ORIGINAL D6 tensor and true-W32 tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)
from hyp105_issue230_d6aa4t_quenched_aligned_d6 import (
    falling, all_h_fixed_point_map_quenched_d6_certificate,
    connected_dual_or_none, direct_original_W32_point_source_connected_A_tensor,
    W32_point_first_60_position_D6_tensor,
)


class AlignedOriginalPositionalQuenchedD6Tests(unittest.TestCase):
    def test_001_all_h_exact_integer_constant_no_finite_asymptotic_fit(self):
        for h in range(1,15):
            s=1<<h
            z=all_h_fixed_point_map_quenched_d6_certificate(s)
            expectation=Fraction(
                z["every_f_quenched_D6_expectation_lower_num"],
                z["every_f_quenched_D6_expectation_lower_den"])
            self.assertGreaterEqual(expectation,Fraction(s**6,98304))
            self.assertTrue(z["all_h_every_f_conditional_EXPECTATION_omega_s6_PROVED"])
            self.assertFalse(z["all_h_min_over_both_maps_positive_PROVED"])
            self.assertEqual(z["missing_physical_edges"],z["K"]-z["V"])
            self.assertLessEqual(z["missing_physical_edges"],z["a"]-2)
            self.assertEqual(
                z["physical_occupied_C6_floor"],
                z["physical_complete_Ka_distinct_C6"]-
                z["missing_physical_edges"]*
                z["physical_missing_edge_destroyed_C6_cap"])
            if s>=8:
                self.assertEqual(z["uniform_all_h_proof_mode"],
                                 "analytic_uniform_s_ge_8")

    def test_002_true_small_orders_hall_exact_occupied_cycle_constants(self):
        s2=all_h_fixed_point_map_quenched_d6_certificate(2)
        self.assertEqual((s2["a"],s2["K"],s2["missing_physical_edges"],
                          s2["physical_occupied_C6_floor"]),
                         (6,15,0,60))
        self.assertEqual(
            Fraction(s2["right_g_uniform_connected_matching_probability_num"],
                     s2["right_g_uniform_connected_matching_probability_den"]),
            Fraction(1,5005))
        s4=all_h_fixed_point_map_quenched_d6_certificate(4)
        self.assertEqual((s4["a"],s4["K"],s4["missing_physical_edges"],
                          s4["physical_occupied_C6_floor"]),
                         (14,91,6,108900))
        self.assertEqual(s4["true_original_distinct_line_assignments_per_C6_floor"],1)

    def test_003_K6_exact_column_C6_coord_match_is_720_distinct(self):
        # Six ORIGINAL flags with fixed connected column dual:
        # position i carries physical (coord i, coord i+1 mod 6).
        H=tuple(sorted(tuple(sorted((i,(i+1)%6))) for i in range(6)))
        position_edges={}
        for col in range(6):
            position_edges[col]=tuple(i for i,(u,v) in enumerate(H)
                                       if col in (u,v))
        self.assertTrue(all(len(x)==2 for x in position_edges.values()))
        possibilities=set()
        for perm in permutations(range(6)):
            assignment=tuple(tuple(sorted(perm[e] for e in position_edges[i]))
                             for i in range(6))
            self.assertEqual(len(set(assignment)),6)
            possibilities.add(assignment)
        self.assertEqual(len(possibilities),720)
        self.assertEqual(Fraction(len(possibilities),falling(15,6)),
                         Fraction(1,5005))

    def test_004_true_W32_direct_vs_independent_source_major_all_schemes(self):
        for scheme,d6 in (("S68",0),("S72",0),("lex",15),("reverse",3)):
            model=fixture(1,scheme)
            out=W32_point_first_60_position_D6_tensor(model)
            self.assertEqual(out["D6_matched_exact_two_sided_original_count"],d6)
            self.assertEqual(out["physical_full_K6_connected_C6_count"],60)
            if scheme in ("S68","S72"):
                # Two genuine globally injected maps show actual D6=0
                # despite the exact strictly positive conditional mean.
                self.assertEqual(out["T_f_connected_60_position_C6_tensor_total"],21186)
                self.assertEqual(
                    Fraction(out["uniform_complete_right_global_injection_D6_expectation_num"],
                             out["uniform_complete_right_global_injection_D6_expectation_den"]),
                    Fraction(1926,455))
            self.assertGreaterEqual(out["T_f_connected_60_position_C6_tensor_total"],
                                    60)
            self.assertGreaterEqual(out["occupied_positional_H_fibres"],1)
            self.assertLessEqual(out["occupied_positional_H_fibres"],60)
            self.assertEqual(
                Fraction(out["uniform_complete_right_global_injection_D6_expectation_num"],
                         out["uniform_complete_right_global_injection_D6_expectation_den"]),
                Fraction(out["T_f_connected_60_position_C6_tensor_total"],5005))
            self.assertEqual(out["independent_original_W32_full_seven_oracles"],"PASS")
            self.assertFalse(out["all_h_deterministic_min_over_f_g_PROVED"])

    def test_005_genuine_global_both_type_random_permutations(self):
        rng=random.Random(23000409)
        edges=list(combinations(range(6),2))
        m=fixture(1,"lex")
        for _ in range(4):
            rng.shuffle(edges);f=tuple(edges)
            rng.shuffle(edges);g=tuple(edges)
            case={**m,"left_labels":f,"right_labels":g}
            out=W32_point_first_60_position_D6_tensor(case,
                                                       check_independent=False)
            legacy=seven_census(case,independent_checks=False)
            self.assertEqual(out["D6_matched_exact_two_sided_original_count"],
                             legacy["seven_class_motif_counts"]["D6"])
            self.assertGreater(out["T_f_connected_60_position_C6_tensor_total"],0)
            self.assertFalse(out["all_h_deterministic_min_over_f_g_PROVED"])

    def test_006_right_uniform_expectation_depends_only_on_fixed_true_f(self):
        left=fixture(1,"S68")
        base=direct_original_W32_point_source_connected_A_tensor(left)[0]
        right_scheme=fixture(1,"reverse")["right_labels"]
        case={**left,"right_labels":right_scheme}
        z=W32_point_first_60_position_D6_tensor(case,check_independent=False)
        self.assertEqual(z["T_f_connected_60_position_C6_tensor_total"],
                         len(base))
        self.assertEqual(
            Fraction(z["uniform_complete_right_global_injection_D6_expectation_num"],
                     z["uniform_complete_right_global_injection_D6_expectation_den"]),
            Fraction(len(base),5005))
        self.assertTrue(z["all_h_conditional_every_f_positive_EXPECTATION"])

    def test_007_reject_fake_source_GQ_or_noninjective_point_labels(self):
        model=fixture(1,"lex")
        inc=tuple((p,ell) for ell in range(15)
                  for p in (ell,(ell+1)%15,(ell+3)%15))
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            direct_original_W32_point_source_connected_A_tensor(
                {**model,"incidences":inc})
        labels=list(model["left_labels"])
        labels[0]=labels[1]
        with self.assertRaises(ValueError):
            W32_point_first_60_position_D6_tensor(
                {**model,"left_labels":tuple(labels)})

    def test_008_point_line_true_source_duality_and_fibre_balance(self):
        model=fixture(1,"reverse")
        original=W32_point_first_60_position_D6_tensor(model,
                                                       check_independent=False)
        # Swap typed ORIGINAL point/line factors and the full typed images.
        # The W32 source incidence graph is symmetric under duality.
        swapped={**model,
                 "incidences":tuple((l,p) for p,l in model["incidences"]),
                 "left_labels":model["right_labels"],
                 "right_labels":model["left_labels"]}
        dual=W32_point_first_60_position_D6_tensor(swapped,
                                                   check_independent=False)
        self.assertEqual(
            original["D6_matched_exact_two_sided_original_count"],
            dual["D6_matched_exact_two_sided_original_count"])
        self.assertGreater(dual["T_f_connected_60_position_C6_tensor_total"],0)


if __name__=="__main__":
    unittest.main()
