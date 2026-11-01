"""AA4-SELROOT: independent original selector/sixwalk joint root gate."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_original_selector_sixwalk_joint_root_gate import (
    EPSILON,CORE_BUDGET,HEAVY_BETA,K,
    _pow2_root_upper,_original_budget,
    selector_moment_root_gate,exact_root_ablation_grid,
    exact_small_priority_and_cut_falsifier,
)
from hyp105_dense_global_exact_dyadic_closure_referee import integrated_dense_closure
from hyp105_selector_positive_correlation import (
    improved_path_selector_sigma,
    genuine_original_path_selector_probabilities,
)
from hyp105_full_physical_degree_tail import genuine_source


def real_maps(power,step,shift=0):
    _,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    palette=tuple(combinations(range(a),2))[:V]
    return palette,tuple(palette[(step*i+shift)%V] for i in range(V))


class OriginalSelectorSixwalkJointRoot(unittest.TestCase):
    def test_exact_fractional_radicals_are_rigorous_uppers_without_float(self):
        for den in (2,8):
            for h in range(6,260):
                q=_pow2_root_upper(h,den)
                self.assertGreaterEqual(q**den*(2**h),1)
                self.assertLess(q**den*(2**h),(Fraction(4097,4096))**den)
            self.assertEqual(_pow2_root_upper(den*3,den),Fraction(1,8))

    def test_genuine_source_budget_and_input_provenance_all_dyadic(self):
        self.assertEqual(HEAVY_BETA,Fraction(15966845,6735233024))
        self.assertLess(EPSILON,CORE_BUDGET)
        self.assertGreater(HEAVY_BETA,EPSILON**2/128)
        for h in range(6,30):
            s=2**h
            b=_original_budget(s)
            self.assertEqual(b["N"],(s+1)**2*(s*s+1))
            self.assertEqual(b["V"],(s+1)*(s*s+1))
            self.assertGreaterEqual(b["exact_core_budget"],CORE_BUDGET)
            self.assertEqual(b["epsilon"],EPSILON)

    def test_exact_original_selector_star_priority_and_typed_cut(self):
        r=exact_small_priority_and_cut_falsifier()
        self.assertEqual(r["original_source_priority_orders_enumerated"],24)
        self.assertEqual(r["independent_typed_two_cut_assignments_enumerated"],256)
        self.assertEqual(r["joint_priority_local_minimum_probability"],Fraction(1,4))
        self.assertEqual(r["joint_two_cut_probability"],Fraction(1,64))
        self.assertEqual(r["whole_proper_three_path_exact_survival"],Fraction(1,256))
        self.assertGreater(r["whole_proper_three_path_exact_survival"],
                           r["selector_r3_uniform_degree_one_floor"])
        self.assertFalse(r.get("pair_path_independence_assumed",False))

    def test_genuine_W32_W34_prior_independent_original_single_path_marginals(self):
        expected=improved_path_selector_sigma(K)
        self.assertEqual(expected["new_sigma2"],Fraction(1,16*(K+1)**2))
        self.assertEqual(expected["new_sigma3"],Fraction(1,64*(K+1)**3))
        for power,step in ((1,7),(2,19)):
            f,g=real_maps(power,step,3)
            for r in (2,3):
                z=genuine_original_path_selector_probabilities(
                    power,f,g,r=r,max_paths=8)
                self.assertGreater(z["paths_checked"],0)
                self.assertEqual(z["r"],r)
                for path in z["original_proper_path_certificates"]:
                    self.assertGreaterEqual(
                        path["whole_source_flag_path_exact_survival_probability"],
                        path["all_h_uniform_sigma_floor"])
                    self.assertEqual(
                        path["both_typed_coordinate_cut_probability"],
                        Fraction(1,4**r))

    def test_matched_four_profiles_every_model_exact_and_monotone(self):
        for C,c in ((1,1),(Fraction(1,2),Fraction(3,5)),
                    (Fraction(7,9),Fraction(2,11)),
                    (Fraction(13,4),Fraction(1,19))):
            with self.subTest(C=C,c=c):
                grid=exact_root_ablation_grid(C,c)
                z=grid["four_matched_runs"]
                base=z["baseline_702"]
                sel=z["selector_only_679"]
                mom=z["sixwalk_only_703"]
                both=z["joint_679_703"]
                for k,v in z.items():
                    self.assertEqual(v["T"],base["T"])
                    self.assertEqual(v["delta"],base["delta"])
                    self.assertEqual(v["original_mixed_internal_multiplier"],15)
                    self.assertEqual(v["K"],64)
                    self.assertEqual(v["epsilon"],EPSILON)
                    self.assertEqual(v["beta"],HEAVY_BETA)
                    self.assertGreaterEqual(
                        v["joint_certified_dyadic_h"],6)
                    self.assertLessEqual(
                        v["joint_loss_upper"],Fraction(1,4))
                    self.assertEqual(
                        sum(v["three_independent_relative_losses_exact_rational_upper"]),
                        v["joint_loss_upper"])
                    self.assertLessEqual(
                        v["joint_certified_dyadic_h"],
                        v["separate_sufficient_dyadic_h"])
                    self.assertTrue(v["external_constants_numerically_UNKNOWN"])
                    self.assertTrue(v["no_path_pair_independence_used"])
                    self.assertTrue(v["mathematically_all_h_greater_orders_by_true_monotone_losses"])
                self.assertEqual(base["selector_sigma2_inverse"],64*65**2)
                self.assertEqual(base["selector_sigma3_inverse"],64*27*65**3)
                self.assertEqual(sel["selector_sigma2_inverse"],16*65**2)
                self.assertEqual(sel["selector_sigma3_inverse"],64*65**3)
                self.assertEqual(mom["sixwalk_L6_coefficient"],288)
                self.assertEqual(base["sixwalk_L6_coefficient"],576)
                self.assertEqual(both["sixwalk_L6_coefficient"],288)
                self.assertLessEqual(both["joint_certified_dyadic_h"],
                                     min(sel["joint_certified_dyadic_h"],
                                         mom["joint_certified_dyadic_h"]))
                self.assertLessEqual(sel["joint_certified_dyadic_h"],
                                     base["joint_certified_dyadic_h"])
                self.assertLessEqual(mom["joint_certified_dyadic_h"],
                                     base["joint_certified_dyadic_h"])
                # Independent existing #702 ROOT calculator uses a coarser
                # radical upper (1/256 vs 1/4096), not identical rounding;
                # both are valid and should agree within a dyadic level.
                old=integrated_dense_closure(C,c)
                self.assertEqual(base["T"],old["original_heavy_tail_T"])
                self.assertEqual(base["delta"],old["root_delta"])
                self.assertEqual(base["L6"],old["conservative_L6"])
                self.assertEqual(base["L4_integer_upper"],
                                 old["ceil_fourth_moment_L4"])
                self.assertEqual(base["B0_integer_upper"],
                                 old["mixed_blocker_B0_conservative_integer"])
                self.assertLessEqual(
                    abs(base["joint_certified_dyadic_h"]-
                        old["dyadic_h0_combined_exact_rational"]),1)

    def test_only_hypothetical_graph_Cc_one_and_sample_print_from_ci(self):
        z=exact_root_ablation_grid(1,1)
        self.assertEqual(z["same_original_heavy_T"],39352331442479)
        self.assertTrue(z["no_genuine_numeric_C_graph_c_graph_claim"])
        self.assertGreaterEqual(z["gain_in_dyadic_h"],0)
        for name,v in z["four_matched_runs"].items():
            print(f"HYPOTHETICAL_C_graph=c_graph=1 / {name}: "
                  f"T={v['T']} h_joint={v['joint_certified_dyadic_h']} "
                  f"h_separate={v['separate_sufficient_dyadic_h']} "
                  f"loss_fraction={str(v['joint_loss_upper'])[:48]}")
            self.assertGreater(v["root_original_sextic_lower_coefficient"],0)
        self.assertEqual(z["four_matched_runs"]["baseline_702"][
            "selector_sigma2_inverse"],64*65**2)

    def test_two_path_negative_color_covariance_not_assumed_positive(self):
        # Actual local binary color-CSP witness from #695; standalone
        # full enumeration, not a fake original W(3,s).
        # Paths individually use left edges {(0,1),(1,2)}
        # versus {(1,2),(0,2)}, each is a three-vertex path.
        # Union is triangle -> impossible to two-color it.
        left1=((0,1),(1,2))
        left2=((1,2),(0,2))
        count1=count2=joint=0
        for mask in range(8):
            b=lambda i:(mask>>i)&1
            p=all(b(x)!=b(y) for x,y in left1)
            q=all(b(x)!=b(y) for x,y in left2)
            count1+=p;count2+=q;joint+=p and q
        self.assertEqual(count1,2)
        self.assertEqual(count2,2)
        self.assertEqual(joint,0)
        self.assertEqual(Fraction(joint,8)-
            Fraction(count1*count2,8*8),Fraction(-1,16))

    def test_fail_closed_bad_inputs(self):
        for C,c in ((0,1),(-1,1),(True,1),(1,False),
                    ("1",1),(1.0,1),(1,Fraction(0))):
            with self.assertRaises(ValueError):
                exact_root_ablation_grid(C,c)
        for selector,moment in ((None,False),(1,False),(False,"true")):
            with self.assertRaises(ValueError):
                selector_moment_root_gate(1,1,
                    improved_selector=selector,sharper_sixwalk=moment)
        for h,d in ((-1,2),(2,4),(3,0),(3,True),(3.0,8)):
            with self.assertRaises(ValueError):
                _pow2_root_upper(h,d)
        for s in (0,63,65,True,64.0,96):
            with self.assertRaises(ValueError):
                _original_budget(s)


if __name__=="__main__":
    unittest.main()
