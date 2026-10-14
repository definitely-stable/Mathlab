"""Fail-closed exact finite injection matching-cover and source-cylinder tests."""
import unittest
from itertools import combinations

from hyp105_issue230_jpkc013_injection_compatibility import (
    exact_minimum_positive_profile_cover,
    coherent_original_injection_certificate,
    _bitwise_or,
)


class JPKC013Tests(unittest.TestCase):
    def test_independently_exhaustive_tiny_set_cover_vs_solver(self):
        examples=(
            ({(0,):1,(1,):2,(2,):4},3,3),
            ({(0,):3,(1,):6,(2,):5},3,2),
            ({(0,):7,(1,):1,(2,):3},3,1),
            ({(0,):3,(1,):6,(2,):12,(3,):9},4,2),
            ({(0,):3,(1,):5,(2,):9,(3,):6,(4,):10,(5,):12},4,2),
            ({(0,):3,(1,):12,(2,):16,(3,):4,(4,):8},5,3),
        )
        for masks,n,expected in examples:
            with self.subTest(n=n,masks=masks):
                cert=exact_minimum_positive_profile_cover(masks,n)
                self.assertEqual(cert["exact_optimum_cover_cardinality"],expected)
                self.assertEqual(cert["complete_covered_global_state_mask"],(1<<n)-1)
                self.assertTrue(cert["minimality_proved_over_ALL_positive_profile_masks"])
                for k in range(1,expected):
                    self.assertFalse(any(
                        _bitwise_or([masks[p] for p in group])==(1<<n)-1
                        for group in combinations(masks,k)))

    def test_invalid_partial_bitmasks_uncovered_states_and_exact_budgets(self):
        with self.assertRaisesRegex(ValueError,"no positive"):
            exact_minimum_positive_profile_cover({(1,):1},2)
        with self.assertRaisesRegex(ValueError,"mask"):
            exact_minimum_positive_profile_cover({(1,):8},3)
        with self.assertRaisesRegex(ValueError,"mask"):
            exact_minimum_positive_profile_cover({(1,):True},3)
        with self.assertRaisesRegex(ValueError,"budget"):
            exact_minimum_positive_profile_cover({(1,):1,(2,):2},2,
                                                 max_distinct_masks=1)
        with self.assertRaises(ValueError):
            exact_minimum_positive_profile_cover({(1,):1},25)
        with self.assertRaises(ValueError):
            exact_minimum_positive_profile_cover({},1)

    def test_actual_original_source_factor_cylinders_partial_states(self):
        for scheme in ("S68","S72"):
            with self.subTest(scheme=scheme):
                c=coherent_original_injection_certificate(scheme,states=3)
                self.assertFalse(c["complete_24_state_injection_fiber_exhausted"])
                self.assertEqual(c["globally_injective_states_examined"],3)
                self.assertEqual(c["J44_locality_checked_original_profile_state_pairs"],
                                 c["total_active_original_source_profiles"]*3)
                self.assertTrue(c["J44_original_factor_cylinder_locality_verified"])
                self.assertTrue(c["independent_GF5_seven_class_oracle_checked_for_every_state"])
                self.assertTrue(c["J45_exact_injection_no_simultaneous_zero_clause_certificate"])
                self.assertLessEqual(
                    c["J45_min_sum_of_cover_original_Q_on_one_global_map"],
                    c["full_seven_S_min_over_examined_maps"])
                self.assertEqual(c["full_original_right_factor_block"].__len__(),4)
                self.assertTrue(c["J45_minimal_positive_cover"][
                    "minimality_proved_over_ALL_positive_profile_masks"])

    def test_all_24_coherent_maps_original_GF5_and_positive_cover(self):
        for scheme,expected_gap in (("S68",57),("S72",68)):
            with self.subTest(scheme=scheme):
                c=coherent_original_injection_certificate(scheme)
                self.assertTrue(c["complete_24_state_injection_fiber_exhausted"])
                self.assertEqual(c["globally_injective_states_examined"],24)
                self.assertEqual(c["full_seven_S_min_over_examined_maps"],68)
                self.assertEqual(c["exact_source_profile_coherence_gap"],expected_gap)
                self.assertEqual(c["individual_original_source_profiles_positive_in_all_states"],
                                 {"S68":7,"S72":0}[scheme])
                cert=c["J45_minimal_positive_cover"]
                self.assertTrue(cert["minimality_proved_over_ALL_positive_profile_masks"])
                self.assertEqual(cert["complete_covered_global_state_mask"],(1<<24)-1)
                self.assertEqual(len(c["J45_positive_original_profile_cover_rows"]),
                                 cert["exact_optimum_cover_cardinality"])
                self.assertTrue(c["independent_GF5_seven_class_oracle_checked_for_every_state"])
                self.assertTrue(c["J44_all_h_cylinder_identity"])
                self.assertTrue(c["J45_all_h_conditional_injection_matching_cover_lemma"])
                for row in c["J45_positive_original_profile_cover_rows"]:
                    self.assertEqual(len(row["original_source_right_line_multiset"]),6)
                    self.assertTrue(row["genuine_source_profile_local_cylinder_verified"])
                    self.assertEqual(row["positive_state_bitmask"],sum(
                        (1<<i) for i,x in enumerate(
                            row["original_positive_sixsets_on_legal_states"]) if x>0))
                self.assertFalse(c["root_A_proved"])

    def test_reject_incomplete_or_unverified_fiber_as_universal(self):
        for bad in (0,-1,25,True):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    coherent_original_injection_certificate("S72",states=bad)
        with self.assertRaises(ValueError):
            coherent_original_injection_certificate("lex")
        with self.assertRaisesRegex(ValueError,"budget"):
            coherent_original_injection_certificate("S68",states=2,
                                                   max_positive_profiles=1)
        with self.assertRaises(ValueError):
            coherent_original_injection_certificate("S72",states=2,
                                                   max_distinct_masks=0)


if __name__=="__main__":
    unittest.main()
