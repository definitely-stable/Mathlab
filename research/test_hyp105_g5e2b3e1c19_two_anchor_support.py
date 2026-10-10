"""C19 exact all-h two-coordinate-cover and original W32 shared-block tests."""
import unittest
from itertools import combinations

from hyp105_g5e2b3e1c19_two_anchor_support import (
    all_h_double_star_gate,
    occupied_two_anchor_witness,
    certified_all_h_occupied_double_star,
    two_anchor_kills_original_sixset,
    genuine_W32_C19_report,
)


class C19TwoAnchorBlockBarrierTests(unittest.TestCase):
    def test_exact_integer_symbolic_all_h_double_star_gate(self):
        for s in (2, 4, 8, 16, 32, 64, 128):
            result = all_h_double_star_gate(s)
            v, a = (result["occupied_physical_pair_edges"],
                    result["physical_coordinate_count"])
            self.assertGreaterEqual(
                result["certified_shared_original_left_block_capacity"], 9)
            self.assertGreater(
                result["certified_shared_original_left_block_capacity"], 6)
            self.assertLess(
                result["certified_shared_original_left_block_capacity"], v)
            self.assertLess(result["missing_physical_pair_edges"], a-1)
            if s == 2:
                self.assertEqual(
                    result["certified_shared_original_left_block_capacity"], 9)
            else:
                self.assertEqual(
                    result["certified_shared_original_left_block_capacity"], 2*a-5)

    def test_gf2_real_K6_all_nine_edges_touched_by_two_anchors(self):
        edges = tuple(combinations(range(6), 2))
        r = certified_all_h_occupied_double_star(2, edges)
        self.assertEqual(r["occupied_double_star_size"], 9)
        self.assertEqual(len(r["physical_pair_edges_for_named_left_support"]), 9)
        self.assertEqual(r["two_physical_coordinates"], (0,1))
        self.assertEqual(
            len({tuple(edge) for edge in
                 r["physical_pair_edges_for_named_left_support"]}), 9)

    def test_gf4_adversarial_missing_edge_images_all_have_23_cover(self):
        full = tuple(combinations(range(14), 2))
        self.assertEqual(len(full), 91)
        removed_cases = (
            full[:6],
            full[-6:],
            tuple((0, x) for x in range(1,7)),
            tuple((0,1), (2,3), (4,5), (6,7), (8,9), (10,11)),
        )
        for removed in removed_cases:
            subset = tuple(e for e in full if e not in set(removed))
            self.assertEqual(len(subset), 85)
            r = certified_all_h_occupied_double_star(4, subset)
            self.assertGreaterEqual(r["occupied_double_star_size"], 23)
            cover = r["two_physical_coordinates"]
            for k in (1, 6, 9, 23):
                f = dict(zip(range(k),
                             r["physical_pair_edges_for_named_left_support"][:k]))
                six = tuple((i % k, i) for i in range(6))
                result = two_anchor_kills_original_sixset(six, f, cover)
                self.assertTrue(
                    result["cannot_be_a_six_coordinate_left_two_factor"])
                self.assertGreaterEqual(result["total_two_anchor_degree"], 6)

    def test_shared_left_block_not_just_single_motif_W32_oracle(self):
        report = genuine_W32_C19_report()
        self.assertGreater(
            report["pre_relabel_true_left_2factor_witnesses_inside_support"], 0)
        self.assertEqual(
            report["post_relabel_true_left_2factor_witnesses_inside_support"], 0)
        self.assertEqual(report["occupied_double_star_edges"], 9)
        self.assertEqual(
            report["real_original_incidence_degree_falsifier"][
                "cannot_be_a_six_coordinate_left_two_factor"], True)

    def test_covered_support_9_is_bounded_not_all_15_original_points(self):
        edges = tuple(combinations(range(6), 2))
        with self.assertRaises(ValueError):
            occupied_two_anchor_witness(edges, 6, need=10)
        with self.assertRaises(ValueError):
            certified_all_h_occupied_double_star(4, edges)

    def test_invalid_input_and_fake_local_assignments_fail_closed(self):
        for s in (True, 1, 3, 6):
            with self.assertRaises(ValueError):
                all_h_double_star_gate(s)
        edges = tuple(combinations(range(6), 2))
        for case in ((edges + (edges[0],), 6),
                     (((0,1), (1,0)), 6),
                     (((0,7), (1,2)), 6)):
            with self.assertRaises(ValueError):
                occupied_two_anchor_witness(*case)
        with self.assertRaises(ValueError):
            occupied_two_anchor_witness(edges, 6, need=0)
        with self.assertRaises(ValueError):
            two_anchor_kills_original_sixset(
                ((0,0),) * 6, {0:(0,1)}, (0,1))
        with self.assertRaises(ValueError):
            two_anchor_kills_original_sixset(
                tuple((0, i) for i in range(6)), {0:(2,3)}, (0,1))


if __name__ == "__main__":
    unittest.main()
