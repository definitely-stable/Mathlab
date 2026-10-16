"""AA4-V independent second-moment algebra + genuine ORIGINAL W32 regressions."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4v_full_conditional_second_moment import (
    exact_D6_full_family_second_moment,
    true_original_W32_subfamily_exact_moment,
)
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    exact_two_D6_gluing_kernel, _actual_original_Q_line_cycle,
)
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


C0 = (0, 1, 2, 3, 4, 5)
C_DISJOINT = (6, 7, 8, 9, 10, 11)
C_R2_OK = (0, 6, 3, 7, 8, 9)
C_R2_IMPOSSIBLE = (0, 2, 6, 7, 8, 9)
C_R6_BAD = (0, 1, 2, 3, 5, 4)
P = Fraction(1, 5005)


def as_fraction(record, field):
    return Fraction(record[field])


class OriginalQuenchedD6FullSecondMomentTests(unittest.TestCase):
    def test_one_event_exact_bernoulli_not_fake_independence(self):
        z = exact_D6_full_family_second_moment(2, [C0])
        self.assertEqual(as_fraction(z, "E_D6"), P)
        self.assertEqual(as_fraction(z, "E_D6_squared"), P)
        self.assertEqual(as_fraction(z, "Var_D6"), P*(1-P))
        self.assertEqual(sum(z["ordered_pair_overlap_counts"].values()), 1)

    def test_two_distinct_original_Q_same_source_line_cycle_count_multiplicity(self):
        # Two different true Q may impose the SAME cyclic physical-line event.
        z = exact_D6_full_family_second_moment(2, [C0, C0])
        self.assertEqual(z["N_original_Q_events"], 2)
        self.assertEqual(z["N_distinct_source_line_cycle_events"], 1)
        self.assertEqual(as_fraction(z, "E_D6_squared"), 4*P)
        self.assertEqual(as_fraction(z, "Var_D6"), 4*P*(1-P))
        self.assertEqual(as_fraction(z, "Paley_Zygmund_P_D6_positive_lower"), P)

    def test_incompatible_same_six_line_factors_negative_pair_covariance(self):
        z = exact_D6_full_family_second_moment(2, [C0, C_R6_BAD])
        self.assertEqual(as_fraction(z, "E_D6_squared"), 2*P)
        self.assertEqual(as_fraction(z, "Var_D6"), 2*P-4*P*P)
        self.assertEqual(z["zero_joint_ordered_event_pairs"], 2)
        self.assertEqual(z["ordered_pair_overlap_counts"][6], 4)

    def test_general_two_event_formula_and_known_disjoint_control(self):
        for second in (C_DISJOINT, C_R2_OK, C_R2_IMPOSSIBLE):
            z = exact_D6_full_family_second_moment(2, [C0, second])
            exact_joint = Fraction(exact_two_D6_gluing_kernel(
                2, C0, second)["joint_probability_one_complete_GLOBAL_g"])
            self.assertEqual(as_fraction(z, "E_D6_squared"), 2*P+2*exact_joint)
            self.assertEqual(as_fraction(z, "Var_D6"),
                             2*P+2*exact_joint-4*P*P)
            self.assertEqual(sum(z["ordered_pair_overlap_counts"].values()), 4)

    def test_three_event_ordered_pairs_symmetry_and_full_covariance(self):
        cycles = [C0, C_R2_OK, C_R2_IMPOSSIBLE]
        z = exact_D6_full_family_second_moment(2, cycles)
        independent_direct = sum(
            (Fraction(exact_two_D6_gluing_kernel(
                2, left, right)["joint_probability_one_complete_GLOBAL_g"])
             for left in cycles for right in cycles), Fraction())
        self.assertEqual(as_fraction(z, "E_D6_squared"), independent_direct)
        self.assertEqual(as_fraction(z, "E_D6"), 3*P)
        self.assertEqual(sum(z["ordered_pair_overlap_counts"].values()), 9)
        for shuffled in ((cycles[2], cycles[0], cycles[1]),
                         (cycles[1], cycles[2], cycles[0])):
            self.assertEqual(
                as_fraction(exact_D6_full_family_second_moment(2, shuffled),
                            "E_D6_squared"), independent_direct)

    def test_dihedral_representations_are_same_event_not_spurious_two_types(self):
        second = tuple(C0[(2-i) % 6] for i in range(6))
        z = exact_D6_full_family_second_moment(2, [C0, second])
        self.assertEqual(z["N_distinct_source_line_cycle_events"], 1)
        self.assertEqual(as_fraction(z, "E_D6_squared"), 4*P)

    def test_empty_bad_models_fail_closed_and_big_h_recover_bernoulli(self):
        z = exact_D6_full_family_second_moment(2, [])
        self.assertEqual(z["E_D6_squared"], "0")
        with self.assertRaises(ValueError):
            exact_D6_full_family_second_moment(2, [C0, (0, 0, 1, 2, 3, 4)])
        with self.assertRaises(ValueError):
            exact_D6_full_family_second_moment(3, [C0])
        for s in (4, 8, 128, 4096):
            z = exact_D6_full_family_second_moment(s, [C0])
            p = as_fraction(z, "single_event_probability")
            self.assertEqual(as_fraction(z, "Var_D6"), p*(1-p))

    def test_true_original_W32_two_distinct_schemes_exact_finite_subfamily(self):
        for scheme in ("S68", "S72"):
            z = true_original_W32_subfamily_exact_moment(scheme, count=8)
            self.assertEqual(z["N_original_Q_events"], 8)
            self.assertEqual(z["full_W32_left_C6_candidate_count_from_parent"], 21186)
            self.assertEqual(z["subfamily_Q_count_not_full_W32"], 8)
            self.assertEqual(as_fraction(z, "E_D6"), 8*P)
            self.assertGreaterEqual(as_fraction(z, "Var_D6"), 0)
            self.assertLessEqual(
                as_fraction(z, "Paley_Zygmund_P_D6_positive_lower"), 1)
            self.assertEqual(sum(z["ordered_pair_overlap_counts"].values()), 64)
            model, original_rows = genuine_W32_fixed_f_original_connected_left_Q(scheme)
            self.assertEqual(len(original_rows), 21186)
            for q in z["actual_original_six_incidence_IDs"]:
                self.assertEqual(len(set(q)), 6)
                cycle = _actual_original_Q_line_cycle(model, q)
                self.assertEqual(len(set(cycle)), 6)
                # The *source incidence IDs*, not synthetic coordinate edges.
                inc = model["incidences"]
                self.assertEqual(len({inc[i][0] for i in q}), 6)
                self.assertEqual(len({inc[i][1] for i in q}), 6)

    def test_source_event_not_sufficient_for_fixed_adversarial_right_map(self):
        model, original_rows = genuine_W32_fixed_f_original_connected_left_Q("S68")
        q = next(iter(original_rows))
        # Actual deterministic g may reject this genuine D6-eligible Q.
        tag = classify_seven_prechecked(q, model["left_labels"],
                                        model["right_labels"], model["incidences"])
        self.assertIn(tag, (None, "D6"))
        z = exact_D6_full_family_second_moment(
            2, [_actual_original_Q_line_cycle(model, q)])
        self.assertGreater(as_fraction(z, "E_D6"), 0)
        self.assertFalse(z["global_minimax_six_motif_PROVED"])

    def test_probability_second_moment_cauchy_independent_direct_bound(self):
        for events in ([C0], [C0]*3, [C0, C_R6_BAD],
                       [C0, C_DISJOINT], [C0, C_R2_OK, C_R2_IMPOSSIBLE]):
            z = exact_D6_full_family_second_moment(2, events)
            mu = as_fraction(z, "E_D6")
            m2 = as_fraction(z, "E_D6_squared")
            self.assertEqual(as_fraction(z, "Paley_Zygmund_P_D6_positive_lower"),
                             mu*mu/m2)
            self.assertGreaterEqual(m2, mu*mu)


if __name__ == "__main__":
    unittest.main()
