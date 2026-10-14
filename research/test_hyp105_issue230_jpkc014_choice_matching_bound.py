"""Independent J50 original source-line injected-image minimum cost falsifiers."""
from itertools import permutations
import unittest

from hyp105_issue230_jpkc014_choice_matching_bound import (
    exact_injective_choice_star_lower,
)
from hyp105_issue230_jpkc014_source_factor_capacity import (
    single_factor_choice_certificate,
)


class OriginalFactorAssignmentBoundTests(unittest.TestCase):
    def test_exact_dp_vs_independent_permutation_minimum(self):
        images=((0,1),(0,2),(1,2))
        rows={
            1:{images[0]:1,images[1]:7,images[2]:7},
            2:{images[0]:1,images[1]:2,images[2]:9},
            3:{images[0]:1,images[1]:3,images[2]:4},
        }
        cert=exact_injective_choice_star_lower(rows,images)
        true_min=min(sum(rows[r][p[i]] for i,r in enumerate(sorted(rows)))
                     for p in permutations(images))
        self.assertEqual(cert["exact_injective_min_original_Q_lower"],true_min)
        self.assertEqual(cert["sum_of_independent_original_source_star_row_minima"],3)
        self.assertGreater(cert["strict_injection_assignment_gain"],0)
        self.assertTrue(cert["all_selected_original_source_images_distinct"])

    def test_disjoint_full_w32_original_true_Q_matching_bound(self):
        for scheme in ("S68","S72"):
            with self.subTest(scheme=scheme):
                x=single_factor_choice_certificate(scheme)
                m=x["J50_exact_injective_original_source_star_matching"]
                self.assertEqual(m["exact_injective_min_original_Q_lower"],8)
                self.assertEqual(m["sum_of_independent_original_source_star_row_minima"],7)
                self.assertEqual(m["strict_injection_assignment_gain"],1)
                self.assertEqual(
                    m["exact_injective_min_original_Q_lower"],
                    x["J48_finite_exact_min_selected_true_original_Q_by_state"])
                self.assertEqual(len(m["selected_original_line_to_physical_image"]),4)
                self.assertTrue(m["J50_all_h_conditional_injection_assignment_lemma"])
                self.assertFalse(m["unconditional_all_h_star_existence_proved"])

    def test_nonnegative_control_empty_star_set_is_not_a_false_theorem(self):
        images=((0,1),(2,3))
        c=exact_injective_choice_star_lower({},images)
        self.assertEqual(c["exact_injective_min_original_Q_lower"],0)
        self.assertEqual(c["strict_injection_assignment_gain"],0)
        self.assertTrue(c["all_selected_original_source_images_distinct"])

    def test_fail_closed_malformed_rows_and_injection_invalid(self):
        images=((0,1),(2,3))
        for bad in (
            {1:{images[0]:1}},
            {1:{images[0]:0,images[1]:1}},
            {1:{images[0]:1,images[1]:-1}},
            {1:{images[0]:1,images[1]:True}},
        ):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                exact_injective_choice_star_lower(bad,images)
        with self.assertRaises(ValueError):
            exact_injective_choice_star_lower({},(images[0],images[0]))
        with self.assertRaises(ValueError):
            exact_injective_choice_star_lower({},images,max_block=0)
        with self.assertRaises(ValueError):
            exact_injective_choice_star_lower({
                1:{images[0]:1,images[1]:1},
                2:{images[0]:1,images[1]:1},
                3:{images[0]:1,images[1]:1},
            },images)


if __name__=="__main__":
    unittest.main()
