"""Independent exact nonzero GF5 flow counts and coefficient brute force."""
from itertools import product
from fractions import Fraction
import unittest

from hyp105_g5e0_boundary_flows import exact_nonzero_trade_flow
from hyp105_g5d_affine_weights import checksum_pattern_palette
from hyp105_g5d_trade_rank import signed_trade_rank_report


class G5E0BoundaryFlowTests(unittest.TestCase):
    def test_exact_two_column_nonzero_flow_equals_51_bruteforce(self):
        s=(0,1,2,3)
        report=exact_nonzero_trade_flow((s,s),(1,-1))
        self.assertEqual(report["number_of_nonzero_GF5_weight_assignments"],51)
        self.assertEqual(report["exact_probability"],Fraction(1,51))
        patterns=checksum_pattern_palette()
        brute=sum(x==y for x in patterns for y in patterns)
        self.assertEqual(brute,report["number_of_nonzero_GF5_weight_assignments"])
        self.assertLessEqual(report["exact_probability"], report["rank_upper"])

    def test_singleton_and_unbalanced_zero_flow(self):
        s=(0,1,2,3)
        self.assertEqual(exact_nonzero_trade_flow(
            (s,(0,1,4,5)),(1,-1))[
                "number_of_nonzero_GF5_weight_assignments"], 0)
        self.assertEqual(exact_nonzero_trade_flow(
            (s,(4,5,6,7)),(1,-1))[
                "number_of_nonzero_GF5_weight_assignments"], 0)
        self.assertEqual(exact_nonzero_trade_flow(
            (s,s),(1,1))[
                "number_of_nonzero_GF5_weight_assignments"], 0)

    def test_disconnected_balanced_components_product_factorization(self):
        a=(0,1,2,3)
        b=(4,5,6,7)
        r=exact_nonzero_trade_flow((a,a,b,b),(1,-1,1,-1))
        self.assertEqual(r["number_of_nonzero_GF5_weight_assignments"],51**2)
        self.assertEqual(r["exact_probability"],Fraction(1,51**2))
        self.assertEqual(r["components"],2)
        self.assertEqual(r["edge_variables"],16)

    def test_actual_w32_unit_trade_has_positive_weighted_flow_count(self):
        supports=((2,3,6,7),(0,5,8,9),(0,2,6,8),(3,5,7,9))
        signs=(1,1,-1,-1)
        report=exact_nonzero_trade_flow(supports,signs)
        self.assertGreaterEqual(
            report["number_of_nonzero_GF5_weight_assignments"],1)
        self.assertLessEqual(report["exact_probability"],report["rank_upper"])
        self.assertEqual(report["t"],4)

    def test_bad_model_and_expensive_queries_rejected(self):
        s=(0,1,2,3)
        with self.assertRaises(ValueError):
            exact_nonzero_trade_flow((s,s),(1,-1),max_edges=7)
        with self.assertRaises(ValueError):
            exact_nonzero_trade_flow((s,),(2,))
        with self.assertRaises(ValueError):
            exact_nonzero_trade_flow((s,)*6,(1,-1,1,-1,1,-1))


if __name__ == "__main__":
    unittest.main()
