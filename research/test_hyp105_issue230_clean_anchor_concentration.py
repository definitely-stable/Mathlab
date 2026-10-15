"""EICE-003-K: exact ORIGINAL GQ dirty-source collinear pencil identities."""
from fractions import Fraction
import random
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_projection import fixture
from hyp105_issue230_anchor_filtered_codegrees import (
    exact_original_anchor_middle_census, STAGES,
)
from hyp105_issue230_clean_anchor_concentration import (
    clean_anchor_all_h_bound, exact_global_original_clean_anchors,
    exact_middle_dirty_pullback, finite_global_clean_vs_source_report, report,
)


class TrueOriginalCleanAnchorConcentrationTests(unittest.TestCase):
    def test_K1_exact_all_h_minimal_pair_universe_and_clean_asymptotic(self):
        for s in (2,4,8,16,64,1024,65536,2**20):
            b=clean_anchor_all_h_bound(s)
            a,V=b["a"],b["V"]
            self.assertGreaterEqual(a*(a-1)//2,V)
            self.assertLess((a-1)*(a-2)//2,V)
            self.assertEqual(b["N"],(s+1)**2*(s*s+1))
            self.assertEqual(b["true_original_nonincident_endpoint_pairs"],
                             V*s*s*(s+1))
            self.assertEqual(b["left_dirty_absolute_upper"],
                             2*s*(a-2)*V)
            self.assertEqual(b["right_dirty_absolute_upper"],
                             2*s*(a-2)*V)
            self.assertFalse(b["uniform_five_source_four_anchor_clean_lower_proved"])
            self.assertFalse(b["universal_o_s4_middle_clean_capacity_proved"])
        for s in (2**16,2**18,2**20):
            self.assertLess(Fraction(
                clean_anchor_all_h_bound(s)[
                    "uniform_nonincident_original_dirty_probability_upper"]),
                Fraction(1,10))
        with self.assertRaisesRegex(ValueError,"s=2"):
            clean_anchor_all_h_bound(3)

    def test_K1_independent_original_point_and_line_pencil_exact_W32_W34(self):
        for h,schemes in ((1,("lex","reverse","S68","S72")),
                          (2,("lex","random"))):
            for scheme in schemes:
                with self.subTest(h=h,scheme=scheme):
                    model=fixture(h,scheme)
                    data=exact_global_original_clean_anchors(model)
                    bound=clean_anchor_all_h_bound(data["s"])
                    N=data["true_original_nonincident_endpoint_pairs"]
                    self.assertEqual(N,data["original_anchor_end_clean_pairs"]+
                                       data["original_anchor_end_dirty_pairs"])
                    self.assertEqual(data["K1_exact_left_dirty_from_point_pencils"],
                        data["original_anchor_dirty_LEFT_only"]+
                        data["original_anchor_dirty_BOTH"])
                    self.assertEqual(data["K1_exact_right_dirty_from_line_pencils"],
                        data["original_anchor_dirty_RIGHT_only"]+
                        data["original_anchor_dirty_BOTH"])
                    self.assertEqual(data["K1_exact_left_dirty_from_point_pencils"],
                        2*data["s"]*data[
                            "K1_original_collinear_overlap_unordered_point_pairs"])
                    self.assertEqual(data["K1_exact_right_dirty_from_line_pencils"],
                        2*data["s"]*data[
                            "K1_original_intersecting_overlap_unordered_line_pairs"])
                    self.assertLessEqual(
                        data["original_anchor_end_dirty_pairs"],
                        bound["union_dirty_absolute_upper"])
                    self.assertEqual(Fraction(
                        data["original_uniform_conditional_end_clean_fraction"]),
                        Fraction(data["original_anchor_end_clean_pairs"],N))
                    self.assertTrue(data["all_h_uniform_clean_convergence_proved"])
                    self.assertFalse(data[
                        "uniform_five_source_template_clean_convergence_proved"])

    def test_K1_adversarial_globally_injected_true_original_pair_permutations(self):
        seed_model=fixture(1,"lex")
        for seed in range(6):
            with self.subTest(seed=seed):
                model=dict(seed_model)
                model["left_labels"]=list(seed_model["left_labels"])
                model["right_labels"]=list(seed_model["right_labels"])
                random.Random(540_230+seed).shuffle(model["left_labels"])
                random.Random(541_230+seed).shuffle(model["right_labels"])
                global_clean=exact_global_original_clean_anchors(model)
                self.assertEqual(
                    len(global_clean["original_pair_dirty_set"]),
                    global_clean["original_anchor_end_dirty_pairs"])
                self.assertEqual(
                    global_clean["original_anchor_dirty_LEFT_only"]+
                    global_clean["original_anchor_dirty_RIGHT_only"]+
                    global_clean["original_anchor_dirty_BOTH"],
                    global_clean["original_anchor_end_dirty_pairs"])

    def test_K3_independent_actual_original_five_source_pullbacks(self):
        for h,scheme,middles in (
            (1,"lex",(0,10,44)),
            (1,"S68",(0,20)),
            (2,"lex",(0,10,26,45,126,206,424)),
            (2,"random",(0,10,26,45,126,206,424)),
        ):
            with self.subTest(h=h,scheme=scheme):
                model=fixture(h,scheme)
                ctx=EndpointEnergy(model)
                dirty=exact_global_original_clean_anchors(model)[
                    "original_pair_dirty_set"]
                for e in middles:
                    pulled=exact_middle_dirty_pullback(model,e)
                    earlier=exact_original_anchor_middle_census(ctx,e)[
                        "cumulative_all_four_corner_source_counts"]
                    self.assertEqual(pulled[
                        "true_five_source_physical_templates"],earlier[0])
                    self.assertEqual(pulled[
                        "all_four_original_nonincident_source_templates"],earlier[2])
                    self.assertEqual(pulled[
                        "all_four_original_end_clean_source_templates"],earlier[3])
                    self.assertEqual(pulled[
                        "nonincident_source_templates_with_at_least_one_dirty_anchor"],
                        earlier[2]-earlier[3])
                    self.assertLessEqual(
                        pulled["true_dirty_original_endpoint_pair_distinct_count"],
                        len(dirty))
                    self.assertLessEqual(
                        pulled["K3_union_lower_N_minus_C"],
                        pulled["true_dirty_original_endpoint_pair_corner_occurrences"])
                    self.assertLessEqual(
                        pulled["true_dirty_original_endpoint_pair_corner_occurrences"],
                        pulled["K3_union_upper_four_N_minus_C"])
                    self.assertTrue(pulled[
                        "K3_exact_true_source_dirty_pullback_verified"])
                    self.assertFalse(pulled[
                        "uniform_o_s4_clean_capacity_proved"])

    def test_K2_true_uniform_global_clean_NOT_the_physical_quadruple_law(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            data=finite_global_clean_vs_source_report(
                m,pullback_middle_ids=(0,10,26))
            global_clean=data["true_original_global_clean_anchor_census"]
            self.assertEqual(data["true_original_physical_five_source_cascade"][
                STAGES[3]],6421 if scheme=="lex" else 7968)
            self.assertEqual(data["true_original_physical_five_source_cascade"][
                STAGES[2]],127831 if scheme=="lex" else 94876)
            self.assertEqual(Fraction(data[
                "physically_conditioned_ALL_FOUR_anchor_clean_fraction_of_nonincident"]),
                Fraction(6421,127831) if scheme=="lex"
                else Fraction(7968,94876))
            self.assertTrue(data[
                "global_uniform_source_pairs_NOT_equal_to_physical_quadruple_law"])
            self.assertFalse(data["all_h_four_anchor_clean_capacity_upper_proved"])
            self.assertNotEqual(Fraction(global_clean[
                "original_uniform_conditional_end_clean_fraction"]),
                Fraction(data[
                "physically_conditioned_ALL_FOUR_anchor_clean_fraction_of_nonincident"]))

    def test_fail_closed_source_model_middle_and_budget(self):
        model=fixture(1,"lex")
        with self.assertRaisesRegex(ValueError,"nonnegative TRUE"):
            exact_middle_dirty_pullback(model,0,max_templates=-1)
        with self.assertRaisesRegex(ValueError,"true original middle"):
            exact_middle_dirty_pullback(model,-1)
        from hyp105_issue230_quadrant_matching_capacity import exact_local_middle_capacity
        ctx=EndpointEnergy(model)
        nonzero=next(e for e in range(ctx.N) if
            exact_local_middle_capacity(ctx,e)[
                "unique_x_y_coordinate_disjoint_five_source_templates"]>0)
        with self.assertRaisesRegex(ValueError,"template enumeration budget"):
            exact_middle_dirty_pullback(model,nonzero,max_templates=0)
        corrupt=dict(model)
        corrupt["left_labels"]=list(model["left_labels"])
        corrupt["left_labels"][0]=corrupt["left_labels"][1]
        with self.assertRaisesRegex(ValueError,"global injective"):
            exact_global_original_clean_anchors(corrupt)

    def test_report_research_only_no_false_root_or_GF5_sixset(self):
        r=report()
        self.assertEqual(r["status"],"RESTRICTED_THEOREM_K")
        self.assertEqual(r["root_A"],"OPEN")
        self.assertEqual(len(r["maps"]),6)
        self.assertTrue(all(not x["root_Branch_A_proved"] for x in r["maps"]))
        self.assertTrue(all(not x[
            "true_original_global_clean_anchor_census"][
            "uniform_five_source_template_clean_convergence_proved"]
            for x in r["maps"]))


if __name__=="__main__":
    unittest.main()
