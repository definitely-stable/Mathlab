"""C24-B1 exact three-way right-C correction and independent original W32."""
from itertools import combinations
import unittest
from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, W32_right_C_source, right_C_pair_weights,
    exact_star_collision_upper,
)
from hyp105_g5e2b3e1c24b_three_collision import (
    W32_LEFT_H45, W32_RIGHT_H45_ZERO,
    right_C_source_with_left_f, independent_left_first_source,
    exact_collision_decomposition, pasch_pair_tensor_limitation,
    original_W32_B1_report,
)


class C24B1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = right_C_source_with_left_f(W32_LEFT_H45)

    def test_left_source_H45_two_independent_full_enumerations(self):
        n, oracle = independent_left_first_source(W32_LEFT_H45)
        self.assertEqual(n, 62370)
        self.assertEqual(oracle, self.source)
        self.assertEqual((sum(self.source.values()), len(self.source)), (45, 40))

    def test_exact_collision_zero_right_witness(self):
        x = exact_collision_decomposition(self.source, W32_RIGHT_H45_ZERO, K6_PAIRS)
        self.assertEqual(x["H_C"], 45)
        self.assertEqual(x["accepted_right_C"], 0)
        self.assertEqual(sum(x["conflict_multiplicity_histogram"].values()), 45)
        W = right_C_pair_weights(self.source, 15)
        self.assertEqual(x["first_order_star_conflicts"],
                         exact_star_collision_upper(W, W32_RIGHT_H45_ZERO, K6_PAIRS))
        self.assertEqual(x["first_order_star_conflicts"], 45 + x["total_correction"])
        self.assertEqual(sum(sum(row) for row in W) // 2, 135)
        self.assertEqual(max(map(max, W)), 5)

    def test_105_global_right_swaps_exact_third_order_identity(self):
        base = list(W32_RIGHT_H45_ZERO)
        W = right_C_pair_weights(self.source, 15)
        for i, j in combinations(range(15), 2):
            p = base.copy()
            p[i], p[j] = p[j], p[i]
            d = exact_collision_decomposition(self.source, p, K6_PAIRS)
            self.assertEqual(d["first_order_star_conflicts"],
                             exact_star_collision_upper(W, p, K6_PAIRS))
            self.assertGreaterEqual(d["accepted_right_C"], 45 - d["first_order_star_conflicts"])

    def test_preserve_existing_lex_92_right_C_source(self):
        src = W32_right_C_source()
        self.assertEqual(src, right_C_source_with_left_f(range(15)))
        self.assertEqual(sum(src.values()), 92)

    def test_paschtwo_same_W_but_different_accepted_C(self):
        info = pasch_pair_tensor_limitation()
        self.assertEqual((info["Pasch_A_accepted"], info["Pasch_B_accepted"]), (0, 1))
        self.assertTrue(info["same_pair_tensor"])
        self.assertNotEqual(*info["different_triple_corrections"])

    def test_invalid_original_label_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            right_C_source_with_left_f((1,) * 15)
        with self.assertRaises(ValueError):
            independent_left_first_source(tuple(range(14)))
        with self.assertRaises(ValueError):
            exact_collision_decomposition({(1, 1, 2): 1}, tuple(range(15)), K6_PAIRS)
        with self.assertRaises(ValueError):
            exact_collision_decomposition({(0, 1, 2): -1}, tuple(range(15)), K6_PAIRS)

    def test_exact_report(self):
        x = original_W32_B1_report()
        self.assertEqual((x["right_C_original_source_H"],
                          x["nonzero_original_right_triples"]), (45, 40))
        self.assertTrue(x["no_total_seven_or_asymptotic_counterexample"])


if __name__ == "__main__":
    unittest.main()
