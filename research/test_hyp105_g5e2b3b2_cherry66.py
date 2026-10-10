"""HYP-105 B3.1-B2-A: independent GF5 and forest-model falsifiers."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_g5e2b3b2_cherry66 import (
    LEFT, RIGHT, SIGNS, census, signed_orbits,
    supports_for_edges, all_h_cherry66_expectation, _relabel_graph,
    _relabel_sign, left_automorphisms, falling,
)
from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
from hyp105_g5e2b3b1_critical_flows import exact_nowherezero_signed_flow
from hyp105_g5e2b1_energy import single_signed_trade_mitm
from hyp105_g5e2b3_forests import six_projection_coefficients


class Cherry66GF5Tests(unittest.TestCase):
    def test_explicit_unique_left_cherry_and_right_two_factors(self):
        self.assertEqual(Counter(LEFT)[(0,1)],2)
        self.assertEqual(len(set(LEFT)),5)
        self.assertEqual(len(RIGHT),70)
        self.assertEqual(len(SIGNS),10)
        for right in RIGHT:
            selected=supports_for_edges(LEFT,right)
            self.assertEqual(len(selected),6)
            self.assertTrue(all(len(s)==4 for s in selected))
            self.assertEqual(len({tuple(sorted(s)) for s in selected}),6)
            ldegs=Counter(x for edge in LEFT for x in edge)
            rdegs=Counter(x for edge in right for x in edge)
            self.assertEqual(sorted(ldegs.values()),[2]*6)
            self.assertEqual(sorted(rdegs.values()),[2]*6)

    def test_signed_orbit_mass_and_exact_flow_census(self):
        orbits=signed_orbits()
        self.assertEqual(len(orbits),66)
        self.assertEqual(sum(mass for _,mass in orbits),700)
        c=census()
        self.assertEqual(c["positive_signed_cases_fixed_left"],700)
        self.assertEqual(c["zero_signed_cases_fixed_left"],0)
        self.assertEqual(c["flow_min"],4560)
        self.assertEqual(c["flow_max"],6786)
        self.assertEqual(c["sum_weights_fixed_left"],3902064)
        self.assertEqual(c["sum_weights_all_three_left_C4"],11706192)
        self.assertFalse(c["full_R3_upper_proved"])

    def test_independent_integer_fourier_and_real_GF5_mitm(self):
        # Algorithmic independence: primary census is 2^12 spanning
        # subgraph inclusion/exclusion; 782-state dual characters and
        # 51^3-side full GF5 subset sums are different exact algorithms.
        orbits=signed_orbits()
        ranked=[]
        for ((right,mask),mass) in orbits:
            result=exact_nowherezero_signed_flow(LEFT,right,mask)
            ranked.append((result,right,mask))
        ranked.sort()
        for _,right,mask in (ranked[0],ranked[len(ranked)//2],ranked[-1]):
            supports=supports_for_edges(LEFT,right)
            signs=tuple(1 if mask&(1<<i) else -1 for i in range(6))
            exact=exact_nowherezero_signed_flow(LEFT,right,mask)
            dual=exact_dual_GF5_six_flow(supports,signs,dimension=12)
            self.assertEqual(exact,dual)
        value,right,mask=ranked[0]
        support=supports_for_edges(LEFT,right)
        plus=tuple(i for i in range(6) if mask&(1<<i))
        minus=tuple(i for i in range(6) if not mask&(1<<i))
        picked=tuple(support[i] for i in plus+minus)
        mitm=single_signed_trade_mitm(
            picked,(1,1,1,-1,-1,-1),12)
        self.assertEqual(mitm["weighted_flow_count"],value)

    def test_invariance_under_all_left_stabilizer_permutations(self):
        right,mask=signed_orbits()[0][0]
        n=exact_nowherezero_signed_flow(LEFT,right,mask)
        for perm in left_automorphisms():
            mapped=_relabel_graph(right,perm)
            mapped_sign=_relabel_sign(mask,perm)
            self.assertEqual(n,exact_nowherezero_signed_flow(
                LEFT,mapped,mapped_sign))

    def test_physical_left_mask_symmetry_and_projection_coefficient(self):
        # Two physical left coordinates are indistinguishable by column
        # incidence masks, which forces (a)_6/2, not (a)_6.
        s=supports_for_edges(LEFT,RIGHT[0])
        incidence=[tuple(i for i,coords in enumerate(s) if j in coords)
                   for j in range(6)]
        self.assertEqual(Counter(incidence)[(0,1)],2)
        p=six_projection_coefficients((2,1,1,1,1))
        self.assertIn((6,Fraction(3,2)),p)

    def test_all_h_exact_expectation_and_no_universal_upper(self):
        for s in (2,4,8,16):
            x=all_h_cherry66_expectation(s)
            self.assertGreater(x["count_lower"],0)
            self.assertLessEqual(x["count_lower"],x["count_upper"])
            self.assertGreater(x["expected_R3_lower"],0)
            self.assertLessEqual(x["expected_R3_lower"],x["expected_R3_upper"])
            self.assertFalse(x["uniform_fixed_label_U_lower"])
            self.assertFalse(x["strict_R3_upper_proved"])
        with self.assertRaises(ValueError):
            all_h_cherry66_expectation(3)
        with self.assertRaises(ValueError):
            falling(5,6)
        with self.assertRaises(ValueError):
            supports_for_edges(LEFT,((0,1),)*5)


if __name__=="__main__":
    unittest.main()
