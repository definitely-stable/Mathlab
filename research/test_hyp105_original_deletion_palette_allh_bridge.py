"""Independent normalized all-h deletion-to-GF5 bridge constants tests.

The NEW production symbolic derivation imports NOTHING from Draft #674.
These tests compare formal exact rational variables against the separately
written parent #674 calculator and then check every 51-palette exponent.
Formal (C,c)=(1,1) is NOT asserted to be a valid real Simonovits
balanced-C6 supersaturation constant pair.
"""
from fractions import Fraction
import unittest

from hyp105_original_deletion_palette_allh_bridge import (
    independent_UDEL_packing_and_exact_GF5_probability_bridge as bridge)
from hyp105_original_ten_sign_exclusive import Q_TEN
from hyp105_unconditional_original_deletion import exact_unconditional_constants


class IndependentAllhOriginalSourceConstantBridge(unittest.TestCase):
    def test_three_formal_pairs_match_independent_parent_674_exact_quantities(self):
        for C,c in ((1,Fraction(1)),(2,Fraction(1,5)),
                    (5,Fraction(1,17)),(13,Fraction(1,101))):
            with self.subTest(C=C,c=str(c)):
                x=bridge(C,c,assume_unreviewed_parent_674=True)
                old=exact_unconditional_constants(C,c)
                self.assertEqual(int(x["heavy_degree_cap_T"]),
                                 old["heavy_degree_cap_T"])
                self.assertEqual(int(x["original_selector_sigma2_inverse"]),
                                 old["selected_sigma2_inverse"])
                self.assertEqual(int(x["original_selector_sigma3_inverse"]),
                                 old["selected_sigma3_inverse"])
                self.assertEqual(int(x["original_physical_sixth_walk_L6"]),
                                 old["selected_graph_sixth_walk_envelope_L6"])
                self.assertEqual(int(x["original_proper_path_M3_squared"]),
                                 old["endpoint_proper_third_path_Frobenius_bound_squared_M3"])
                self.assertEqual(Fraction(x["parent_674_original_deletion_rho"]),
                                 old["allowed_original_flag_deletion_density_rho"])
                self.assertEqual(Fraction(x["parent_674_original_sevenmotif_delta"]),
                                 old["accepted_sixset_all_map_floor_delta"])
                self.assertEqual(int(x["parent_674_symbolic_s0"]),
                                 old["sufficient_s0_integer"])
                self.assertFalse(x["graph_SS6_actual_constants_VERIFIED"])
                self.assertTrue(x["allh_requires_parent_674_qualified_mathematical_review"])
                self.assertFalse(x["allh_NEW_geometric_obstruction_proved_here"])
                self.assertEqual(x["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_exact_rho_packing_and_sharp_q10_exponential_rates(self):
        x=bridge(3,Fraction(1,9),assume_unreviewed_parent_674=True)
        rho=Fraction(x["parent_674_original_deletion_rho"])
        self.assertLessEqual(rho,Fraction(1,32))
        self.assertEqual(Fraction(x["full_ten_sign_UNION_GF5_original_probability_q10"]),
                         Q_TEN)
        clean=Fraction(x["allh_random_clean_exponential_rate_q10rho_over_6"])
        dist=Fraction(x["allh_random_recolor_distance_min_coeff_q10rho_over_12"])
        lower=Fraction(x["allh_recolor_lower_tail_exponential_rate_q10rho_over_48"])
        self.assertEqual(clean,Q_TEN*rho/6)
        self.assertEqual(dist,clean/2)
        self.assertEqual(lower,clean/8)
        self.assertGreater(Q_TEN,10*Fraction(5175,51**6))
        self.assertGreater(clean,0)

    def test_no_external_math_claim_without_assumption_or_real_Cc(self):
        for pair in ((0,Fraction(1)),(1,Fraction(0)),(1,Fraction(2)),
                     (1,Fraction(-1,7))):
            with self.assertRaises(ValueError):
                bridge(*pair,assume_unreviewed_parent_674=True)
        with self.assertRaises(ValueError):
            bridge(1,Fraction(1),assume_unreviewed_parent_674=False)
        with self.assertRaises(ValueError):
            bridge(1,Fraction(1))  # no silent promotion
        with self.assertRaises(ValueError):
            bridge(3.0,Fraction(1),assume_unreviewed_parent_674=True)


if __name__=="__main__":
    unittest.main()
