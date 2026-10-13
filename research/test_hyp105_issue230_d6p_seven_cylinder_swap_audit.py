"""Independent real-ORIGINAL W32 seven-GF5 cylinder tests and swap falsifiers."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
import unittest

from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_census,
    cylinder_seven_class, exact_seven_cylinder_swap,
    original_W32_seven_cylinder_report, swapped_labels,
    _physical_dual, _is_six_cycle,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS
)
from hyp105_issue230_d6o_joint_ba_ca_covariance import (
    original_sixline_weights_BC, _moments_one_pair
)


SCHEMES=("lex","reverse","S68","S72")
PINNED_S={"lex":259,"reverse":169,"S68":68,"S72":72}


def independent_recount_for_swapped_g(model,u,v):
    """Independent legacy full original six-incidence GF5-positive classifier."""
    alternate=dict(model)
    alternate["right_labels"]=swapped_labels(model["right_labels"],u,v)
    return seven_census(alternate,independent_checks=False)


class SevenOriginalCylinderSwapTests(unittest.TestCase):
    def test_original_full_seven_class_and_GF5_weight_exact_all_maps(self):
        for scheme in SCHEMES:
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                compiled=compile_original_W32_cylinders(model)
                actual=cylinder_census(compiled,model["right_labels"])
                independent=seven_census(model,independent_checks=False)
                self.assertEqual(actual["S_seven"],PINNED_S[scheme])
                self.assertEqual(actual["seven_class_motif_counts"],
                                 independent["seven_class_motif_counts"])
                self.assertEqual(actual["GF5_seven_lower_numerator"],
                                 independent["GF5_seven_lower_numerator"])
                self.assertEqual(actual["number_original_left_candidates"],62370)
                self.assertLess(compiled["unique_position_aware_right_cylinders"],62370)
                self.assertEqual(compiled["left_original_sixset_counts"],
                                 {"A":51030,"B":10935,"C":405})
                self.assertEqual(len(compiled["by_original_line"]),15)

    def test_independent_complete_recount_after_real_original_right_swaps(self):
        for scheme in SCHEMES:
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            base=cylinder_census(compiled,model["right_labels"])
            for u,v in ((0,1),(0,7),(5,14),(13,14)):
                with self.subTest(scheme=scheme,original_lines=(u,v)):
                    delta=exact_seven_cylinder_swap(
                        compiled,model["right_labels"],u,v)
                    true=independent_recount_for_swapped_g(model,u,v)
                    self.assertEqual(
                        base["S_seven"]+delta["delta_S_seven"],
                        true["S_seven"])
                    self.assertEqual(
                        base["GF5_seven_lower_numerator"]+
                        delta["delta_GF5_selected_lower_numerator"],
                        true["GF5_seven_lower_numerator"])
                    for klass in R3_CERTIFIED_FLOORS:
                        self.assertEqual(
                            base["seven_class_motif_counts"][klass]+
                            delta["delta_by_seven_class"][klass],
                            true["seven_class_motif_counts"][klass])
                    self.assertLessEqual(
                        delta["touched_unique_cylinders"],
                        compiled["unique_position_aware_right_cylinders"])

    def test_all_105_original_line_swaps_each_true_W32_instance(self):
        report=original_W32_seven_cylinder_report()
        self.assertEqual(report["Branch_A"],"OPEN")
        self.assertEqual(report["Branch_B"],"OPEN")
        self.assertEqual(report["complete_W34_W38_seven_S"],
                         "UNKNOWN-NOT-CLAIMED")
        self.assertEqual(report["finite_W32_all_105_right_line_swaps_each"],
                         "EXACT-LOCAL-CYLINDER-DELTAS")
        self.assertEqual([x["scheme"] for x in report["records"]],
                         list(SCHEMES))
        for row in report["records"]:
            self.assertEqual(row["base"]["S_seven"],PINNED_S[row["scheme"]])
            self.assertEqual(
                row["number_improving_one_swaps"]+
                row["number_worsening_one_swaps"]+
                row["number_stable_one_swaps"],105)
            self.assertLessEqual(row["min_delta_S_seven"],0)
            self.assertGreaterEqual(row["max_delta_S_seven"],0)
            self.assertEqual(row["all_swaps_local_only"],True)

    def test_counterexample_right_line_support_alone_loses_D6_column_dual(self):
        """A/A aligned D6 can change while full right support stays identical.

        Deliberately synthetic incidence POSITION control (not real GQ).
        This is why a 6-line support-only mask cannot encode all seven.
        """
        cycle=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        left_dual=_physical_dual(tuple(range(6)),cycle)
        self.assertTrue(_is_six_cycle(left_dual))
        signature=("A",tuple(range(6)),left_dual,())
        self.assertEqual(cylinder_seven_class(signature,cycle),"D6")
        swapped=swapped_labels(cycle,0,1)
        self.assertNotEqual(cylinder_seven_class(signature,swapped),"D6")
        other_dual=_physical_dual(tuple(range(6)),swapped)
        self.assertTrue(_is_six_cycle(other_dual))
        other_signature=("A",tuple(range(6)),other_dual,())
        self.assertNotEqual(left_dual,other_dual)
        self.assertNotEqual(cylinder_seven_class(other_signature,cycle),"D6")
        self.assertEqual(cylinder_seven_class(other_signature,swapped),"D6")
        # Both right lines are present. Their transposition DOES change D6.
        self.assertIn(0,signature[1])
        self.assertIn(1,signature[1])

    def test_d6n_d6o_directional_BC_same_two_present_swap_invariant(self):
        for scheme in SCHEMES:
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            all_bc=original_sixline_weights_BC(model)
            row=_moments_one_pair(all_bc,model["right_labels"],model["a"])
            base=cylinder_census(compiled,model["right_labels"])
            self.assertEqual(base["seven_class_motif_counts"]["B-left/A-right"],
                             row["B"]["actual_fixed_g_directional_sixsets"])
            # C-left/A-right is only one orientation of aggregate C/A.
            actual_C=sum(m for signature,m in compiled["cylinders"].items()
                         if signature[0]=="C" and
                         cylinder_seven_class(
                             signature,model["right_labels"])=="C/A")
            self.assertEqual(actual_C,
                             row["C"]["actual_fixed_g_directional_sixsets"])
            self.assertGreaterEqual(
                base["seven_class_motif_counts"]["C/A"],actual_C)
            for sig in compiled["cylinders"]:
                if sig[0] in ("B","C") and len(set(sig[1]))==6:
                    u,v=sig[1][:2]
                    old=cylinder_seven_class(sig,model["right_labels"])
                    updated=cylinder_seven_class(
                        sig,swapped_labels(model["right_labels"],u,v))
                    expected=("B-left/A-right" if sig[0]=="B" else "C/A")
                    self.assertEqual(old==expected,updated==expected)

    def test_invalid_original_swap_line_ids_fail_closed(self):
        model=fixture(1,"lex")
        compiled=compile_original_W32_cylinders(model)
        for bad in ((0,0),(-1,2),(0,15),(15,14)):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                exact_seven_cylinder_swap(
                    compiled,model["right_labels"],*bad)
        self.assertEqual(
            sum(compiled["cylinders"].values()),62370)


if __name__=="__main__":
    unittest.main()
