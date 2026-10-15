"""Independent finite falsifiers for AA4-AJ: true original GQ, not fake C6s."""
import unittest
from itertools import combinations

from hyp105_issue230_d6aa4aj_connected_22_hall import (
    edge, sites, two_bridge_pairings, original_connected_22_cohort,
    independent_original_connected_22, complete_22_capacity,
    certified_two_bridge_prehall_floor,
)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32, full_original_W32_sector_certificate,
    classify_physical_A_twofactor,
)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors,
)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    pinned_twofactor_completions,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    transform_model, symplectic_transvection_source,
)


class ConnectedOriginalTwoBridge(unittest.TestCase):
    def test_01_exact_complete_K6_K7_K8_third_of_C6(self):
        pins = ((0, 1), (2, 3))
        for a in (6, 7, 8):
            Hs = list(pinned_twofactor_completions(*pins, a))
            expected = complete_22_capacity(a)
            C6 = [H for H in Hs if classify_physical_A_twofactor(
                H, pins) == "connected_C6"]
            self.assertEqual(len(C6), expected["all_disjoint_pinned_connected_C6"])
            exact22 = []
            for H in C6:
                P = set(pins[0] + pins[1])
                other = set(v for e in H for v in e) - P
                rem = set(H) - set(pins)
                if len(other) == 2 and all(
                    len(set(e) & P) == 1 and len(set(e) & other) == 1
                    for e in rem
                ):
                    exact22.append(H)
            self.assertEqual(len(exact22), expected["both_bridges"])
            self.assertEqual(3 * len(exact22), len(C6))

    def test_02_ordered_sites_and_diagonal_exclusion_for_physical_holes(self):
        for a in (6, 7, 8):
            e0, e1 = (0, 1), (2, 3)
            pairings = two_bridge_pairings(e0, e1)
            self.assertEqual(len(pairings), 2)
            for holes in (set(), {edge(1, 4)},
                          {edge(1, 4), edge(2, 5)},
                          {edge(1, 4), edge(2, 5), edge(0, 6)}):
                inv = {e: i for i, e in enumerate(combinations(range(a), 2))
                       if e not in holes}
                bad = set(e0 + e1)
                patterns = []
                for L, R in pairings:
                    Y, Z = sites(a, inv, L, bad), sites(a, inv, R, bad)
                    predicted = len(Y) * len(Z) - len(set(Y) & set(Z))
                    literal = 0
                    for y in Y:
                        for z in Z:
                            if y != z:
                                literal += 1
                                patterns.append(frozenset((
                                    e0, e1, edge(L[0], y), edge(L[1], y),
                                    edge(R[0], z), edge(R[1], z)
                                )))
                    self.assertEqual(predicted, literal)
                self.assertEqual(len(patterns), len(set(patterns)))
                self.assertTrue(all(classify_physical_A_twofactor(
                    H, (e0, e1)) == "connected_C6" for H in patterns))

    def test_03_true_original_W32_all_135_cohorts_two_orientations(self):
        m = zero_split_original_W32()
        for side in (0, 1):
            total = occupied = cohorts = disjoint = 0
            for root in range(15):
                four_list = occupied_root_C4_source_factors(
                    m, side=side, root=root)
                self.assertEqual(len(four_list), 3)
                for k in range(3):
                    for four in four_list:
                        z = original_connected_22_cohort(
                            m, side=side, root=root, pair_offset=k,
                            four=four, independent=True)
                        cohorts += 1
                        disjoint += z["pinned_physical_edges_disjoint"]
                        total += z["accepted_original_GF5_connected_22_Q"]
                        occupied += z["occupied_connected_22_physical_C6"]
            self.assertEqual(cohorts, 135)
            self.assertGreater(disjoint, 0)
            full = full_original_W32_sector_certificate(m, side=side)
            self.assertLessEqual(total, full[
                "original_GF5_A_accepted_by_sector"]["connected_C6"])
            self.assertLessEqual(occupied, full[
                "occupied_opposite_A_physical_H_by_sector"]["connected_C6"])
            self.assertGreater(occupied, 0)

    def test_04_true_original_lex_and_S68_independent_cycle_oracle(self):
        for scheme in ("lex", "S68", "S72"):
            m = fixture(1, scheme)
            for side in (0, 1):
                for root in (0, 1, 2):
                    four = occupied_root_C4_source_factors(
                        m, side=side, root=root)[0]
                    for offset in (0, 1, 2):
                        z = original_connected_22_cohort(
                            m, side=side, root=root, pair_offset=offset,
                            four=four, independent=False)
                        oracle = independent_original_connected_22(
                            m, side=side, root=root, pair_offset=offset,
                            four=four)
                        self.assertEqual(z[
                            "accepted_original_GF5_connected_22_Q"],
                            oracle["accepted_Q"])
                        self.assertEqual(z[
                            "occupied_connected_22_physical_C6"],
                            len(oracle["occupied_H"]))

    def test_05_genuine_original_W34_nonsurjective_full_global(self):
        m = fixture(2, "lex")
        self.assertEqual(m["s"], 4)
        for side in (0, 1):
            for root in (0, 1):
                all_C4 = occupied_root_C4_source_factors(
                    m, side=side, root=root)
                self.assertGreater(len(all_C4), 0)
                for four in all_C4[:2]:
                    z = original_connected_22_cohort(
                        m, side=side, root=root, pair_offset=0, four=four,
                        independent=True)
                    self.assertEqual(sum(r["accepted_original_GF5_Q"]
                                         for r in z["bridge_rows"]),
                                     z["accepted_original_GF5_connected_22_Q"])

    def test_06_source_automorphism_and_separate_physical_renaming(self):
        m = zero_split_original_W32()
        p, l = symplectic_transvection_source(m, 1)
        x = transform_model(
            m, point_sources=p, line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i + 2) % 6 for i in range(6)))
        def totals(model, side):
            accepted = occupied = 0
            for root in range(15):
                for k in range(3):
                    for four in occupied_root_C4_source_factors(
                            model, side=side, root=root):
                        z = original_connected_22_cohort(
                            model, side=side, root=root, pair_offset=k,
                            four=four, independent=False)
                        accepted += z["accepted_original_GF5_connected_22_Q"]
                        occupied += z["occupied_connected_22_physical_C6"]
            return accepted, occupied
        for side in (0, 1):
            self.assertEqual(totals(m, side), totals(x, side))

    def test_07_all_h_closed_integer_floor_and_explicit_no_Hall(self):
        for h in range(1, 40):
            s = 1 << h
            z = certified_two_bridge_prehall_floor(s)
            self.assertTrue(z["accepted_original_Hall_positive_lower_NOT_PROVED"])
            if h >= 4:
                self.assertTrue(z["s14_over_128_physical_proved_for_all_global_maps"])
                self.assertGreaterEqual(
                    128 * z["connected_22_indexed_preHall_lower"], s**14)
            else:
                self.assertFalse(z["s14_over_128_physical_proved_for_all_global_maps"])

    def test_08_reject_invalid_inputs_and_adjacent_pins(self):
        for s in (0, 3, 6, 12, 16.0, True):
            with self.assertRaises(ValueError):
                certified_two_bridge_prehall_floor(s)
        for a in (5, 6.0, True):
            with self.assertRaises(ValueError):
                complete_22_capacity(a)
        self.assertEqual(two_bridge_pairings((0, 1), (1, 2)), ())
        m = zero_split_original_W32()
        for invalid in (2, -1, True):
            with self.assertRaises(ValueError):
                original_connected_22_cohort(
                    m, side=invalid, root=0, pair_offset=0,
                    four=(1, 2, 3, 4))
        with self.assertRaises(ValueError):
            original_connected_22_cohort(
                m, side=0, root=0, pair_offset=0, four=(0, 1, 2, 3))


if __name__ == "__main__":
    unittest.main()
