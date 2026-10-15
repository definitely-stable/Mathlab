"""Independent tests for HYP-105 #230 D6-AA4-X-CYC exact deterministic frontier."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4q_two_sided_seven_join import _K6_2factors
from hyp105_issue230_d6aa4xcyc_seven_joint_swap_frontier import (
    ExactRightLineSwapFrontier, packed_physical_edge,
    original_line_swap_support, DEGREE_TWO_PACKED,
    dual_original_W32_model, exhaustive_bilateral_210_original_source_swaps,
    independent_bilateral_witness_historical,
)


class OriginalSevenSwapFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = ExactRightLineSwapFrontier(fixture(1, "S68"))

    def test_001_packed_two_regular_sixcoordinate_oracle(self):
        all_phys = set(combinations(range(6), 2))
        self.assertEqual(len(_K6_2factors()), 70)
        for pattern in _K6_2factors():
            packed = sum(packed_physical_edge(e) for e in pattern)
            self.assertEqual(packed, DEGREE_TWO_PACKED)
            manual = Counter(c for e in pattern for c in e)
            self.assertEqual(manual, Counter({c: 2 for c in range(6)}))
        bad = ((0, 1), (0, 2), (0, 3),
               (1, 4), (2, 5), (3, 4))
        self.assertEqual(len(set(bad)), 6)
        self.assertTrue(set(bad) <= all_phys)
        self.assertNotEqual(sum(packed_physical_edge(e) for e in bad),
                            DEGREE_TWO_PACKED)
        for invalid in ((2, 1), (0, 0), (0, 6), (True, 1)):
            with self.assertRaises(ValueError):
                packed_physical_edge(invalid)

    def test_002_real_original_S68_baseline_historical(self):
        o = self.oracle
        self.assertEqual(len(o.rows), 62370)
        self.assertEqual(o.base["S_seven"], 68)
        self.assertEqual(o.base["D6"], 0)
        self.assertEqual(o.base["non_AA"], 68)
        self.assertEqual(o.base["selected_GF5_51palette_certified_numerator"],
                         3112510)
        independent = o.legacy_join_recount(historical=True)
        for field in independent:
            self.assertEqual(o.base[field], independent[field])

    def test_003_all_h_sparse_support_rule_on_actual_original_Q(self):
        o = self.oracle
        for u, v in ((0, 1), (0, 14), (7, 9)):
            affected = o.support[u] | o.support[v]
            for i in (0, 1, 37, 450, 2000, len(o.rows)-1):
                row = o.rows[i]
                actual = original_line_swap_support(
                    row.original_Q, o.incidences, u, v)
                self.assertEqual(i in affected, actual)
            new_g = list(o.base_g)
            new_g[u], new_g[v] = new_g[v], new_g[u]
            swapped_packed = list(o.base_packed)
            swapped_packed[u], swapped_packed[v] = (
                swapped_packed[v], swapped_packed[u])
            unaffected = next(i for i in range(len(o.rows)) if i not in affected)
            self.assertEqual(o.base_tags[unaffected],
                             o._tag(o.rows[unaffected], new_g, swapped_packed))
        with self.assertRaises(ValueError):
            original_line_swap_support((0, 0, 1, 2, 3, 4),
                                       o.incidences, 0, 1)

    def test_004_real_original_synchronous_sparse_vs_complete(self):
        o = self.oracle
        for swap in ((0, 1), (0, 14), (13, 14)):
            sparse = o.swap(*swap)
            all_rows = o.full_recount(swap)
            for field in ("S_seven", "D6", "non_AA",
                          "true_original_seven_classes",
                          "selected_GF5_51palette_certified_numerator"):
                self.assertEqual(sparse[field], all_rows[field])
            self.assertEqual(sparse["S_seven"],
                             sparse["non_AA"]+sparse["D6"])
            self.assertTrue(sparse["affected_original_left_Q"] < 62370)

    def test_005_real_original_independent_historical_swapped_GF5(self):
        for scheme, swaps in (
            ("S68", ((0, 14), (7, 9))),
            ("S72", ((0, 1),)),
        ):
            o = self.oracle if scheme == "S68" else ExactRightLineSwapFrontier(
                fixture(1, scheme))
            for swap in swaps:
                a = o.swap(*swap)
                b = o.legacy_join_recount(swap, historical=True)
                for field in b:
                    self.assertEqual(a[field], b[field])

    def test_006_exhaustive_105_and_nondominance(self):
        x = self.oracle.exhaustive_105_neighbor_frontier()
        self.assertEqual(x["neighbors_checked"], 105)
        self.assertEqual(x["complete_global_line_bijections_compared"], 106)
        self.assertGreaterEqual(x["D6_zero_labelings_in_exact_neighborhood"], 1)
        self.assertEqual(
            x["D6_zero_labelings_in_exact_neighborhood"]
            + x["D6_positive_labelings_in_exact_neighborhood"], 106)
        self.assertLessEqual(x["min_S_witness"]["S_seven"], 68)
        self.assertLessEqual(
            x["min_D6_zero_nonAA_witness"]["non_AA"], 68)
        frontier = {(a["D6"], a["non_AA"]) for a in x["pareto_frontier"]}
        self.assertEqual(len(frontier), len(x["pareto_frontier"]))
        for d, n in frontier:
            self.assertFalse(any(
                a <= d and b <= n and (a < d or b < n)
                for a, b in frontier))
        self.assertFalse(x["all_h_adversarial_seven_class_obstruction_PROVED"])
        self.assertFalse(x["all_h_counterexample_family_PROVED"])

    def test_007_invalid_swaps_and_original_bijections_rejected(self):
        o = self.oracle
        for wrong in ((0, 0), (-1, 1), (1, 15), (4, 3), (True, 2)):
            with self.assertRaises(ValueError):
                o.swap(*wrong)
        m = fixture(1, "S68")
        duplicate = tuple(m["right_labels"][:-1]) + (m["right_labels"][0],)
        with self.assertRaises(ValueError):
            ExactRightLineSwapFrontier({**m, "right_labels": duplicate})

    def test_008_true_original_point_line_dual_baseline_and_one_swaps(self):
        m = fixture(1, "S68")
        dual = ExactRightLineSwapFrontier(dual_original_W32_model(m))
        self.assertEqual(dual.base["S_seven"], 68)
        self.assertEqual(dual.base["D6"], 0)
        self.assertEqual(dual.base["true_original_seven_classes"]["B-left/A-right"], 21)
        self.assertEqual(dual.base["true_original_seven_classes"]["A-left/B-right"], 44)
        for source_swap in ((0, 1), (0, 14)):
            changed = dual.swap(*source_swap)
            actual = {**m, "left_labels": tuple(
                m["left_labels"][v] if i == u else
                m["left_labels"][u] if i == v else m["left_labels"][i]
                for i in range(15)
                for u, v in (source_swap,))}
            history = ExactRightLineSwapFrontier(actual).base
            self.assertEqual(changed["S_seven"], history["S_seven"])
            self.assertEqual(changed["D6"], history["D6"])
            self.assertEqual(changed["selected_GF5_51palette_certified_numerator"],
                             history["selected_GF5_51palette_certified_numerator"])

    def test_009_exact_bilateral_210_original_one_side_swaps(self):
        m = fixture(1, "S68")
        both = exhaustive_bilateral_210_original_source_swaps(m)
        self.assertEqual(both["source_POINT_swaps"], 105)
        self.assertEqual(both["source_LINE_swaps"], 105)
        self.assertEqual(both["complete_global_map_pairs_in_neighborhood"], 211)
        self.assertEqual(
            both["D6_zero_label_pairs"] + both["D6_positive_label_pairs"], 211)
        self.assertLessEqual(both["minimum_S_witness"]["S_seven"], 68)
        self.assertTrue(both["every_single_one_side_swap_exhausted"])
        self.assertFalse(both["simultaneous_two_side_swaps_exhausted"])
        self.assertFalse(both["all_h_min_f_g_seven_S_lower_PROVED"])
        for key in ("minimum_S_witness", "minimum_D6_zero_witness",
                    "minimum_weighted_51palette_numerator_witness"):
            witness = both[key]
            self.assertTrue(independent_bilateral_witness_historical(m, witness))



if __name__ == "__main__":
    unittest.main()
