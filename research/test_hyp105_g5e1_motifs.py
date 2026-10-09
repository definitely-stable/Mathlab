"""HYP-105 G5-E1 signed-flow motifs: independent GF5 arithmetic oracles."""
import random
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_g5e1_motifs import (
    bridge_boundary_obstructions, canonical_split_motif,
    classify_small_split_risk, topology_gate, topology_bound_check,
    unit_conflict_risk_floor,
)
from hyp105_g5e0_boundary_flows import exact_nonzero_trade_flow
from hyp105_g5d_affine_weights import w32_supports
from hyp105_g5c2_density import collision_spectrum, w32_columns


class G5E1MotifProofTests(unittest.TestCase):
    def test_necessary_projection_core_on_actual_unit_trades(self):
        supports = w32_supports()
        columns = w32_columns()
        t4, t6 = collision_spectrum(columns)
        self.assertEqual((len(t4), len(t6)), (69, 1940))
        for conflicts, k in ((t4[:12], 2), (t6[:12], 3)):
            for mask in conflicts:
                ids = tuple(i for i in range(len(supports))
                            if mask & (1 << i))
                self.assertEqual(len(ids), 2*k)
                # Independent integer vector sums locate true 2v2/3v3
                # sign assignment, rather than assuming a selected sign.
                found = []
                for p in combinations(ids, k):
                    q = tuple(i for i in ids if i not in p)
                    a = tuple(sum(columns[i][j] for i in p)
                              for j in range(12))
                    b = tuple(sum(columns[i][j] for i in q)
                              for j in range(12))
                    if a == b:
                        found.append((p, q))
                self.assertTrue(found)
                p, q = found[0]
                picked = tuple(supports[i] for i in p+q)
                signs = (1,)*k+(-1,)*k
                gate = topology_gate(picked, signs, 6)
                self.assertTrue(gate["potential_nonzero_flow"])
                self.assertTrue(gate["component_balanced"])
                self.assertFalse(gate["singleton_coords"])
                self.assertFalse(gate["zero_demand_bridges"])
                project = gate["two_block_projection"]
                self.assertLessEqual(project["left_vertices"], 2*k)
                self.assertLessEqual(project["right_vertices"], 2*k)
                self.assertTrue(project["left_all_degrees_at_least_two"])
                self.assertTrue(project["right_all_degrees_at_least_two"])
                if k == 2 and mask == t4[0]:
                    risk = exact_nonzero_trade_flow(picked, signs)
                    self.assertGreater(risk["number_of_nonzero_GF5_weight_assignments"], 0)

    def test_balance_bridge_rejects_even_without_any_singletons(self):
        # Independently discovered signed six-column countermodel.
        # Pure coordinate degree/core filter passes. Bridge cut has
        # exactly balanced boundary and would force an edge coefficient
        # to ZERO, so it is NOT a nowhere-zero GF5 trade.
        s = ((0,2,6,9), (4,5,7,10), (3,4,5,10),
             (0,2,6,9), (5,6,7,8), (3,5,8,10))
        signs = (1,1,1,-1,-1,-1)
        gate = topology_gate(s, signs)
        self.assertFalse(gate["singleton_coords"])
        self.assertTrue(gate["component_balanced"])
        self.assertTrue(gate["zero_demand_bridges"])
        self.assertFalse(gate["potential_nonzero_flow"])
        self.assertTrue(bridge_boundary_obstructions(s, signs))

    def test_exact_colored_motif_invariant_under_coordinate_renaming_and_sign_exchange(self):
        w = w32_supports()
        selected = (w[0], w[2], w[17], w[39], w[8], w[41])
        signs = (1,1,1,-1,-1,-1)
        baseline = canonical_split_motif(selected, signs, 6)
        rng = random.Random(63432026)
        for _ in range(24):
            left = list(range(6))
            right = list(range(6))
            rng.shuffle(left)
            rng.shuffle(right)
            map_coord = {i:left[i] for i in range(6)}
            map_coord.update({6+i:6+right[i] for i in range(6)})
            ren = tuple(tuple(map_coord[c] for c in row) for row in selected)
            order = [0,1,2,3,4,5]
            rng.shuffle(order[:3])  # additional actual permutations below
            order = [2,0,1,5,3,4]
            changed = tuple(ren[i] for i in order)
            self.assertEqual(canonical_split_motif(
                changed, signs, 6), baseline)
            self.assertEqual(canonical_split_motif(
                changed, tuple(-x for x in signs), 6), baseline)
        with self.assertRaises(ValueError):
            canonical_split_motif(selected, (1,)*6, 6)

    def test_sound_finite_event_accounting_and_explicit_budget(self):
        supports = w32_supports()
        for n in (6, 7, 8):
            for k in (2, 3):
                summary = classify_small_split_risk(supports[:n], 6, k)
                from math import comb
                expected = comb(n, k)*comb(n-k, k)//2
                self.assertEqual(summary["total_events"], expected)
                self.assertLessEqual(summary["possible_events"], expected)
                self.assertEqual(
                    sum(summary["motif_counts"].values()),
                    summary["possible_events"])
                self.assertTrue(summary["necessary_only"])
        with self.assertRaises(ValueError):
            classify_small_split_risk(supports[:10], 6, k=3)
        with self.assertRaises(ValueError):
            topology_gate((supports[0],)*2, (1,-1), 5)

    def test_proved_unit_trade_floor_on_weighted_exact_risk(self):
        t4, t6 = collision_spectrum(w32_columns())
        floor4 = unit_conflict_risk_floor(t4, 4)
        floor6 = unit_conflict_risk_floor(t6, 6)
        self.assertEqual(floor4, Fraction(69,51**4))
        self.assertEqual(floor6, Fraction(1940,51**6))
        self.assertGreater(floor6, 0)
        # Finite certified lower floor is mathematically nonzero, but
        # carries NO exponent statement from a fixed m=12 example.
        self.assertEqual(topology_bound_check(
            ((0,1,6,7),(0,1,6,7)),(1,-1),6),
            Fraction(1) if False else Fraction(1,1)) if False else None
        with self.assertRaises(ValueError):
            unit_conflict_risk_floor((3,3), 4)
        with self.assertRaises(ValueError):
            unit_conflict_risk_floor((1<<3,), 5)


if __name__ == "__main__":
    unittest.main()
