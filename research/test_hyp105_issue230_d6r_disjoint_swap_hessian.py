"""Independent exact all-seven ORIGINAL disjoint right transposition Hessian controls.

No source classifier used as the direct full recount: original frozen
seven_census is an independent incidence-level GF5-family oracle.
Targeted 2-exchange results are NOT global minima or all 2-swaps.
"""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_issue230_d6r_disjoint_swap_hessian import (
    exact_disjoint_right_swap_hessian,
)
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_census,
    exact_seven_cylinder_swap, swapped_labels,
    SEVEN_CLASSES,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)
from hyp105_issue230_projection import fixture


def direct_independent_full_original_recount(model, swaps):
    """Pass full globally injective g to legacy original-incidence classifier."""
    new=dict(model)
    right=tuple(model["right_labels"])
    for u,v in swaps:
        right=swapped_labels(right,u,v)
    new["right_labels"]=right
    return seven_census(new,independent_checks=False)


def direct_hessian_of_class_totals(q0,q1,q2,q12):
    return {
        k:(q12["seven_class_motif_counts"][k]
            -q1["seven_class_motif_counts"][k]
            -q2["seven_class_motif_counts"][k]
            +q0["seven_class_motif_counts"][k])
        for k in SEVEN_CLASSES
    }


class ExactDisjointSwapHessianTests(unittest.TestCase):
    def test_true_W32_independent_full_seven_GF5_double_recounts(self):
        for scheme in ("lex","S68","S72"):
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            original=direct_independent_full_original_recount(model,())
            for first,second in (((0,1),(2,3)),((2,11),(4,13))):
                with self.subTest(scheme=scheme,swaps=(first,second)):
                    first_m=exact_seven_cylinder_swap(
                        compiled,model["right_labels"],*first)
                    second_m=exact_seven_cylinder_swap(
                        compiled,model["right_labels"],*second)
                    h=exact_disjoint_right_swap_hessian(
                        compiled,model["right_labels"],first,second,
                        first_m,second_m)
                    one=direct_independent_full_original_recount(
                        model,(first,))
                    two=direct_independent_full_original_recount(
                        model,(second,))
                    both=direct_independent_full_original_recount(
                        model,(first,second))
                    independent=direct_hessian_of_class_totals(
                        original,one,two,both)
                    self.assertEqual(h["Hessian_by_all_seven_positive_classes"],
                                     independent)
                    self.assertEqual(h["Hessian_S"],
                                     sum(independent.values()))
                    self.assertEqual(
                        h["Hessian_GF5_selected_lower_numerator"],
                        sum(independent[k]*R3_CERTIFIED_FLOORS[k]
                            for k in SEVEN_CLASSES))
                    self.assertEqual(
                        h["two_disjoint_swaps_delta_S"],
                        both["S_seven"]-original["S_seven"])
                    self.assertEqual(
                        h["two_disjoint_swaps_delta_GF5_selected_lower_numerator"],
                        both["GF5_seven_lower_numerator"]-
                        original["GF5_seven_lower_numerator"])
                    self.assertEqual(
                        h["two_disjoint_swaps_delta_by_seven_class"],
                        {k:both["seven_class_motif_counts"][k]-
                           original["seven_class_motif_counts"][k]
                         for k in SEVEN_CLASSES})
                    self.assertLessEqual(
                        abs(h["Hessian_S"]),
                        h["deterministic_absolute_Hessian_S_upper"])

    def test_exact_doubly_touched_original_cylinder_intersection(self):
        model=fixture(1,"S68")
        compiled=compile_original_W32_cylinders(model)
        x=(0,1);y=(2,3)
        row=exact_disjoint_right_swap_hessian(
            compiled,model["right_labels"],x,y)
        direct=[sig for sig in compiled["cylinders"]
                if any(p in sig[1] for p in x)
                and any(q in sig[1] for q in y)]
        self.assertEqual(row["joint_boundary_unique_original_cylinders"],
                         len(direct))
        self.assertEqual(
            row["joint_boundary_original_sixsets_weight"],
            sum(compiled["cylinders"][sig] for sig in direct))
        self.assertLessEqual(
            abs(row["Hessian_GF5_selected_lower_numerator"]),
            row["deterministic_absolute_Hessian_GF5_upper"])
        self.assertTrue(
            row["genuine_complete_right_injection_preserved"])

    def test_marginal_composition_and_disjoint_commutation(self):
        model=fixture(1,"reverse")
        compiled=compile_original_W32_cylinders(model)
        first=(0,7);second=(4,13)
        a=exact_seven_cylinder_swap(
            compiled,model["right_labels"],*first)
        b=exact_seven_cylinder_swap(
            compiled,model["right_labels"],*second)
        h=exact_disjoint_right_swap_hessian(
            compiled,model["right_labels"],first,second,a,b)
        self.assertEqual(
            h["two_disjoint_swaps_delta_S"],
            a["delta_S_seven"]+b["delta_S_seven"]+h["Hessian_S"])
        self.assertEqual(
            h["two_disjoint_swaps_delta_GF5_selected_lower_numerator"],
            a["delta_GF5_selected_lower_numerator"]+
            b["delta_GF5_selected_lower_numerator"]+
            h["Hessian_GF5_selected_lower_numerator"])
        self.assertEqual(
            swapped_labels(swapped_labels(model["right_labels"],*first),
                           *second),
            swapped_labels(swapped_labels(model["right_labels"],*second),
                           *first))

    def test_real_W32_strict_one_swap_minimum_not_presumed_two_swap_minimum(self):
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            # The accepted previous D6-P independently scanned 105
            # singleton moves; do not repeat 105 per test invocation.
            self.assertIn(cylinder_census(compiled,model["right_labels"])[
                "S_seven"],(68,72))
            for first,second in (((0,1),(2,3)),((8,9),(10,11))):
                h=exact_disjoint_right_swap_hessian(
                    compiled,model["right_labels"],first,second)
                self.assertFalse(h["root_all_h_lower_proved"])
                self.assertEqual(
                    h["negative_Hessian_needed_to_escape_two_strict_single_swaps"],
                    (h["two_disjoint_swaps_delta_S"]<0 and
                     h["singleton_delta_S_first"]>0 and
                     h["singleton_delta_S_second"]>0))
                self.assertLessEqual(
                    abs(h["Hessian_S"]),
                    2*h["joint_boundary_original_sixsets_weight"])

    def test_fail_closed_on_overlap_invalid_original_factor_and_cache(self):
        model=fixture(1,"lex")
        compiled=compile_original_W32_cylinders(model)
        g=model["right_labels"]
        for first,second in (
            ((0,1),(1,2)),((0,1),(0,1)),((0,15),(2,3)),
            ((0,1),(2,2)),((-1,1),(2,3)),
        ):
            with self.subTest(first=first,second=second):
                with self.assertRaises(ValueError):
                    exact_disjoint_right_swap_hessian(
                        compiled,g,first,second)
        wrong=exact_seven_cylinder_swap(compiled,g,0,1)
        with self.assertRaises(ValueError):
            exact_disjoint_right_swap_hessian(
                compiled,g,(0,2),(3,4),marginal_first=wrong)

    def test_explicit_all_h_sign_and_GF5_curvature_bounds(self):
        """General binary event extremum: second discrete difference <=2."""
        for values in combinations((0,1,2,3),4):
            pass
        for a in (0,1):
            for b in (0,1):
                for c in (0,1):
                    for d in (0,1):
                        h=a-b-c+d
                        self.assertLessEqual(abs(h),2)
                        self.assertLessEqual(abs(h*51750),2*51750)
        # The bound requires disjoint original transpositions. For
        # overlapping ones, intersection-only support can be incorrect.
        self.assertEqual(
            sorted(R3_CERTIFIED_FLOORS),
            sorted(SEVEN_CLASSES))


if __name__=="__main__":
    unittest.main()
