"""C18 independent combinatorial adversaries against pure-local L_poly."""
import unittest
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c18_zero_star_barrier import (
    all_h_occupied_star_gate, minimal_physical_coordinates,
    star_destroying_left_assignment, exact_sixset_left_projection_invalid,
    genuine_W32_C18_report,
)


class C18AllHZeroStarBarrierTests(unittest.TestCase):
    def test_exact_gq_2_power_minimal_a_degree_gate(self):
        for s in (2, 4, 8, 16, 32, 64):
            x = all_h_occupied_star_gate(s)
            v, a = x["occupied_pair_edges"], x["minimal_physical_coordinates"]
            self.assertLess(comb(a - 1, 2), v)
            self.assertLessEqual(v, comb(a, 2))
            self.assertGreater(v, 2*a)
            self.assertGreaterEqual(
                x["certified_minimum_max_star_degree"], 5)
            self.assertEqual(
                x["C17_no_left_pin_pure_local_S_lower_exactly"], 0)
            self.assertEqual(
                x["C17_no_left_pin_pure_local_GF5_numerator_lower_exactly"], 0)

    def test_all_six_original_left_multiplicity_patterns_kill_same_star(self):
        pairs = tuple(combinations(range(6), 2))
        for k in range(1, 7):
            original = tuple(range(k))
            f, center = star_destroying_left_assignment(pairs, original)
            # Pattern 6-k+1,1,...,1; real six incidence IDs remain distinct.
            p_ids = [0] * (7-k) + list(range(1, k))
            six = tuple((p, j) for j, p in enumerate(p_ids))
            killed, degree = exact_sixset_left_projection_invalid(six, f)
            self.assertTrue(killed)
            self.assertEqual(degree, 6 if k <= 5 else 5)
            self.assertEqual(len(f), k)
            self.assertEqual(len(set(f.values())), k)
            self.assertTrue(any(center in e for e in f.values()))

    def test_adversarial_incomplete_physical_edge_F_still_has_star(self):
        # True GF4 V=85, minimal a=14: ANY six missing K14 edges
        # leave 85 occupied edges, which must have a degree>=5 star.
        a = minimal_physical_coordinates(85)
        self.assertEqual(a, 14)
        full = list(combinations(range(a), 2))
        for removed in (full[:6], full[-6:], full[::15][:6]):
            missing = set(removed)
            occupied = tuple(e for e in full if e not in missing)
            self.assertEqual(len(occupied), 85)
            for k in (1, 3, 5, 6):
                chosen, _ = star_destroying_left_assignment(
                    occupied, tuple(range(k)))
                incidences = tuple(
                    (p, j) for j, p in enumerate(
                        [0]*(7-k)+list(range(1, k))))
                self.assertTrue(
                    exact_sixset_left_projection_invalid(
                        incidences, chosen)[0])

    def test_independent_real_w32_A_B_C_source_shapes(self):
        x = genuine_W32_C18_report()
        self.assertEqual(set(x["independent_original_W32_motif_controls"]),
                         {"A", "B", "C"})
        for row in x["independent_original_W32_motif_controls"].values():
            self.assertGreaterEqual(row["left_coordinate_degree"], 5)

    def test_wrong_scope_and_small_target_fail_closed(self):
        for s in (0, 1, 3, 6, True):
            with self.assertRaises(ValueError):
                all_h_occupied_star_gate(s)
        with self.assertRaises(ValueError):
            star_destroying_left_assignment(((0, 1), (0, 2)), (0, 1))
        with self.assertRaises(ValueError):
            star_destroying_left_assignment(
                tuple(combinations(range(6), 2)), (0, 0))
        with self.assertRaises(ValueError):
            exact_sixset_left_projection_invalid(
                tuple((0, i) for i in range(5)), {0: (0, 1)})


if __name__ == "__main__":
    unittest.main()
