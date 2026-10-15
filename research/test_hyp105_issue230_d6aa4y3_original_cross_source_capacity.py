"""Independent genuine-original GQ mixed point-line source star tests."""
import unittest

from hyp105_issue230_d6aa4y3_original_cross_source_capacity import (
    original_two_source_one_fixed_flag_upper,
    original_crossed_source_point_line_upper,
    original_two_plus_two_actual_GQ_harm_upper,
    genuine_W32_cross_star_oracle,
    report,
)
from hyp105_issue230_d6aa4y3_original_source_star_capacity import (
    original_single_factor_pattern_capacity,
    original_two_factors_union_capacity,
)


class GenuineOriginalCrossedSourceTests(unittest.TestCase):
    def test_001_real_W32_two_marked_point_factors_one_fixed_actual_flag(self):
        x=original_two_source_one_fixed_flag_upper(2,"adjacent")
        y=original_two_source_one_fixed_flag_upper(2,"disjoint")
        # These physical half-Q bounds distinguish marked source q's
        # repeated-root B role from its once-used C4 role conservatively.
        self.assertEqual(x["true_original_two_source_fixed_other_flag_upper"],
                         {"A":1701,"B":486,"C":0})
        self.assertEqual(y["true_original_two_source_fixed_other_flag_upper"],
                         {"A":3402,"B":972,"C":18})
        self.assertEqual(x[
            "all_h_true_original_two_distinct_source_factor_physical_upper"],2187)
        self.assertEqual(y[
            "all_h_true_original_two_distinct_source_factor_physical_upper"],4392)

    def test_002_genuine_original_cross_point_line_fixed_star_bounds(self):
        no=original_crossed_source_point_line_upper(2,False)
        yes=original_crossed_source_point_line_upper(2,True)
        self.assertEqual(no["original_crossed_source_point_line_half_Q_upper"],13176)
        self.assertEqual(yes["original_crossed_source_point_line_half_Q_upper"],17100)
        direct=original_crossed_source_point_line_upper(
            2,True,("adjacent","disjoint"))
        self.assertEqual(
            direct["original_crossed_source_point_line_half_Q_upper"],
            8316+2187+4392)
        self.assertLess(direct["original_crossed_source_point_line_half_Q_upper"],
                        yes["original_crossed_source_point_line_half_Q_upper"])
        with self.assertRaises(ValueError):
            original_crossed_source_point_line_upper(2,1)
        with self.assertRaises(ValueError):
            original_crossed_source_point_line_upper(2,False,("adjacent",))

    def test_003_full_original_GQ_no_four_cross_incidences(self):
        for m in range(4):
            x=original_two_plus_two_actual_GQ_harm_upper(
                2,m,"adjacent","disjoint")
            self.assertEqual(x["actual_original_marked_point_line_incidence_count"],m)
            self.assertTrue(x["true_GQ_girth_eight_excludes_four_point_line_cross_incidences"])
            self.assertTrue(x["not_worse_than_prior_all_h_two_source_star_upper"])
            self.assertLessEqual(
                x["harmful_shared_original_seven_GF5_mode_upper"],
                x["previous_only_same_typed_side_mode_upper"])
            self.assertFalse(x["all_h_original_full_seven_S_Omega_s6_PROVED"])
        with self.assertRaises(ValueError):
            original_two_plus_two_actual_GQ_harm_upper(
                2,4,"adjacent","disjoint")
        with self.assertRaises(ValueError):
            original_two_plus_two_actual_GQ_harm_upper(
                2,True,"adjacent","disjoint")

    def test_004_all_h_cross_star_reduces_exponent_without_root_claim(self):
        z=report()
        self.assertTrue(z["all_h_genuine_GQ_two_by_two_source_incidence_girth_four_forbidden"])
        self.assertTrue(z["all_h_exact_source_cross_star_anchored_true_flag_bound"])
        self.assertTrue(z["all_h_harmful_GF5_mode_capacity_improves_to_O_s11"])
        self.assertEqual(z["root_A"],"OPEN")
        self.assertEqual(z["root_B"],"OPEN")
        for record in z["orders"]:
            self.assertGreater(record["worst_cap_all_actual_original_2point_by_2line_layouts"],0)
            self.assertGreater(record["best_cap_no_true_original_cross_source_incidence"],0)
            self.assertLessEqual(
                record["best_cap_no_true_original_cross_source_incidence"],
                record["worst_cap_all_actual_original_2point_by_2line_layouts"])
        for s in (4,8,16,32):
            old=original_two_factors_union_capacity(s,"adjacent")[
                "two_source_factor_original_union_upper"]*2
            actual=original_two_plus_two_actual_GQ_harm_upper(
                s,3,"adjacent","adjacent")
            self.assertLess(actual["harmful_shared_original_seven_GF5_mode_upper"],
                            old)

    def test_005_true_original_W32_225_source_cross_stars_per_typed_side(self):
        for scheme in ("S68","S72"):
            z=genuine_W32_cross_star_oracle(scheme)
            self.assertEqual(z["true_original_s"],2)
            self.assertTrue(z["full_11025_real_original_2point_x_2line_source_layouts_checked"])
            source=z["true_original_GQ_2by2_marked_source_incidence_class_counts"]
            self.assertEqual(sum(source.values()),11025)
            self.assertEqual(source.get(4,0),0)
            for side in ("point","line"):
                row=z["per_typed_side"][side]
                self.assertEqual(row["actual_source_OPPOSITE_source_cross_stars_checked"],225)
                self.assertTrue(row["all_225_real_original_source_cross_caps_PASS"])
                self.assertGreater(row[
                    "max_real_original_six_ID_Q_for_incident_point_line_stars"],0)
                self.assertGreater(row[
                    "max_real_original_six_ID_Q_for_nonincident_point_line_stars"],0)

    def test_006_genuine_all_h_exact_one_flag_vs_two_source_injection(self):
        for h in range(1,13):
            s=1<<h
            star=original_single_factor_pattern_capacity(s)
            for relation in ("adjacent","disjoint"):
                fixed=original_two_source_one_fixed_flag_upper(s,relation)
                self.assertGreater(fixed[
                    "all_h_true_original_two_distinct_source_factor_physical_upper"],0)
                self.assertLessEqual(
                    fixed["all_h_true_original_two_distinct_source_factor_physical_upper"],
                    star["per_actual_original_incidence_upper"])
                for n in range(4):
                    x=original_two_plus_two_actual_GQ_harm_upper(
                        s,n,relation,relation)
                    self.assertGreater(x["harmful_shared_original_seven_GF5_mode_upper"],0)


if __name__=="__main__":
    unittest.main()
