"""Independent exact GF5 and topology tests of E2-B3.1-A matching core."""
from itertools import permutations
import unittest

from hyp105_g5e2b3b1_critical_flows import (
    CYCLE, TRIANGLES, SIGNS, REPRESENTATIVES, _factor_type,
    _normalized_edges, _relabel_edges, _relabel_mask,
    _automorphisms, two_factors, critical_orbits,
    critical_supports, exact_nowherezero_signed_flow,
    critical_flow_census,
)
from hyp105_g5e2b1_energy import single_signed_trade_mitm
from hyp105_g5e1_motifs import topology_gate


def direct_full_GF5_event(left, right, mask):
    """Fully independent 51^3 GF5 vector-sum oracle, not flow IE."""
    supports = critical_supports(left, right)
    signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
    result = single_signed_trade_mitm(supports, signs, dimension=12)
    return result["weighted_flow_count"]


class CriticalSixFlowTests(unittest.TestCase):
    def test_2_factors_and_exact_automorphism_groups(self):
        factors = two_factors()
        self.assertEqual(len(factors), 70)
        self.assertEqual(sum(_factor_type(x) == (6,) for x in factors), 60)
        self.assertEqual(sum(_factor_type(x) == (3, 3) for x in factors), 10)
        self.assertEqual(len(_automorphisms(CYCLE)), 12)
        self.assertEqual(len(_automorphisms(TRIANGLES)), 72)
        self.assertEqual(len(SIGNS), 10)
        self.assertTrue(all(mask.bit_count() == 3 and mask & 1 for mask in SIGNS))

    def test_complete_orbit_conservation_and_sign_reversal(self):
        orbits = critical_orbits()
        self.assertEqual(sum(orbits.values()), 70 * 70 * 10)
        self.assertEqual(len(orbits), len(set(orbits)))
        self.assertTrue(all(weight > 0 for weight in orbits.values()))
        a = (1 << 0) | (1 << 2) | (1 << 4)
        for left, right in ((CYCLE, CYCLE), (CYCLE, TRIANGLES),
                            (TRIANGLES, TRIANGLES)):
            v = exact_nowherezero_signed_flow(left, right, a)
            self.assertEqual(v, exact_nowherezero_signed_flow(
                left, right, 63 ^ a))
            for p in (tuple(range(6)), (1, 2, 3, 4, 5, 0),
                      (5, 4, 3, 2, 1, 0), (1, 0, 2, 4, 3, 5)):
                moved = sum(1 << p[i] for i in range(6) if a & (1 << i))
                self.assertEqual(v, exact_nowherezero_signed_flow(
                    _relabel_edges(left, p), _relabel_edges(right, p),
                    moved))

    def test_independent_MITM_GF5_counts_and_topological_gate(self):
        masks = (SIGNS[0], SIGNS[-1])
        for left, right in ((CYCLE, CYCLE), (CYCLE, TRIANGLES),
                            (TRIANGLES, TRIANGLES)):
            for mask in masks:
                exact = exact_nowherezero_signed_flow(left, right, mask)
                direct = direct_full_GF5_event(left, right, mask)
                self.assertEqual(exact, direct, (left, right, mask))
                signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
                gate = topology_gate(critical_supports(left, right),
                                     signs, block_size=6)
                self.assertEqual(gate["singleton_coords"], ())
                self.assertTrue(gate["two_block_projection"][
                    "left_all_degrees_at_least_two"])
                self.assertTrue(gate["two_block_projection"][
                    "right_all_degrees_at_least_two"])
                if exact > 0:
                    self.assertTrue(gate["potential_nonzero_flow"])

    def test_full_finite_signed_core_scope(self):
        report = critical_flow_census()
        self.assertEqual(report["total_labeled_signed_cases"], 49000)
        self.assertEqual(report["left_right_2_factors"], 4900)
        self.assertEqual(sum(report["labeled_cases_by_kind_and_sign"].values()),
                         49000)
        self.assertEqual(sum(report["orbits_by_kind_and_sign"].values()),
                         report["colored_signed_isomorphism_orbits"])
        self.assertFalse(report["all_11663_leafless_forest_shapes_classified"])
        self.assertFalse(report["actual_W3s_event_multiplicities_bounded"])
        self.assertFalse(report["strict_R3_power_proved"])
        self.assertFalse(report["new_ASET_exponent_proved"])
        if report["positive_example"]:
            left, right, mask, count = report["positive_example"]
            self.assertGreater(count, 0)
            self.assertEqual(count, direct_full_GF5_event(left, right, mask))
        if report["zero_example"]:
            left, right, mask, count = report["zero_example"]
            self.assertEqual(count, 0)
            self.assertEqual(0, direct_full_GF5_event(left, right, mask))


if __name__ == "__main__":
    unittest.main()
