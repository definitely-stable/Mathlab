"""B8-C fast deterministic conditional mean / two-edge orbit falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, original_W32,
)
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import (
    PROFILE_A, PROFILE_B, PROFILE_C,
    profile_probability, d6_signature_probability,
)
from hyp105_g5e2b3e1c24b8c_conditional_discrepancy import (
    source_right_mean, right_mean_from_compiled_left,
    right_mean_from_independent_sixsets,
    pinned_source_right_probability, two_edge_orbit_certificate,
    exact_centered_discrepancy,
)


def cycle_left():
    return {i:e for i,e in enumerate(
        ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5)))}


class ConditionalRightDiscrepancyTests(unittest.TestCase):
    def test_original_C_right_forces_disjoint_physical_three_matching(self):
        six=((0,10),(1,10),(2,11),(3,11),(4,12),(5,12))
        f=cycle_left()
        unconditional=source_right_mean(six,f,6)
        self.assertEqual(unconditional,profile_probability(6,PROFILE_C))
        self.assertEqual(unconditional,Fraction(3,91))
        got=two_edge_orbit_certificate(six,f,6,10,11)
        self.assertEqual(got["two_adjacent_pins_mean"],Fraction(0))
        self.assertEqual(got["two_disjoint_pins_mean"],Fraction(1,13))
        self.assertEqual(got["adjacent_second_edge_count"],8)
        self.assertEqual(got["disjoint_second_edge_count"],6)
        self.assertEqual(Fraction(6,14*13),unconditional)
        # Independent count: of the 13 available edges, exactly (4,5)
        # avoids all four endpoints already consumed by two repeated lines.
        self.assertEqual(pinned_source_right_probability(
            six,f,6,{10:(0,1),11:(2,3)}),Fraction(1,13))
        self.assertEqual(pinned_source_right_probability(
            six,f,6,{10:(2,3),11:(4,5)}),Fraction(1,13))
        self.assertEqual(pinned_source_right_probability(
            six,f,6,{10:(0,1),11:(0,2)}),Fraction(0))

    def test_B_right_repeated_edge_also_blocks_adjacent_anchor(self):
        six=((0,10),(1,10),(2,11),(3,12),(4,13),(5,14))
        f=cycle_left()
        got=two_edge_orbit_certificate(six,f,6,10,11)
        self.assertEqual(got["two_adjacent_pins_mean"],0)
        self.assertGreater(got["two_disjoint_pins_mean"],0)
        self.assertEqual(got["unconditional_mean"],profile_probability(6,PROFILE_B))
        self.assertEqual(pinned_source_right_probability(
            six,f,6,{10:(2,3),11:(2,4)}),Fraction(0))
        # The B-profile has FOUR other distinct lines; if the repeated
        # line owns (0,1), all four remaining edges must avoid 0 and 1.
        with self.assertRaises(ValueError):
            pinned_source_right_probability(
                six,f,6,{10:(0,1),11:(2,3)},max_states=10)

    def test_D6_connected_matched_cycle_two_orbit_formula(self):
        six=tuple((i,i+20) for i in range(6))
        f=cycle_left()
        got=two_edge_orbit_certificate(six,f,6,20,21)
        self.assertEqual(got["unconditional_mean"],d6_signature_probability(6))
        self.assertEqual(
            8*got["two_adjacent_pins_mean"]+6*got["two_disjoint_pins_mean"],
            14*got["unconditional_mean"])
        # Independent coordinate-name conjugation: no change to signature.
        other=pinned_source_right_probability(six,f,6,{20:(2,3),21:(2,4)})
        self.assertEqual(got["two_adjacent_pins_mean"],other)
        othdis=pinned_source_right_probability(six,f,6,{20:(1,4),21:(2,5)})
        self.assertEqual(got["two_disjoint_pins_mean"],othdis)

    def test_independent_original_W32_small_common_universe_conditional_mean(self):
        f=tuple(W32_LEFT_H45)
        mapping={i+1:K6_PAIRS[v] for i,v in enumerate(f)}
        _,lines,_=original_W32()
        incidences=tuple(sorted((p,l) for l,line in enumerate(lines) for p in line))
        subset=incidences[:10]+incidences[20:24]
        self.assertEqual(len(tuple(combinations(subset,6))),3003)
        source=tuple(combinations(subset,6))
        result=right_mean_from_independent_sixsets(source,mapping,6)
        direct=Fraction(0)
        for six in source:
            direct+=source_right_mean(six,mapping,6)
        self.assertEqual(result["conditional_right_mean"],direct)
        self.assertEqual(sum(result["by_tag_expected"].values(),Fraction(0)),direct)
        # Independent hand-built compression of only eligible original
        # sources in this ORIGINAL 3003-sixset subuniverse.
        fibers=Counter()
        for six in source:
            v=source_right_mean(six,mapping,6)
            if v:
                tag=None
                from hyp105_g5e2b3e1c24b8a_physical_tensor import source_profile, physical_factor_state
                tag=source_profile(six)
                sig=physical_factor_state(six,mapping,left=True)[1]
                ls=tuple(sorted(l for _,l in six))
                fibers[(tag,ls,sig if tag=="D6" else None)]+=1
        comp={"records":[(t,ls,sig,mult) for (t,ls,sig),mult in fibers.items()],
              "static_eligible":sum(fibers.values())}
        independent=right_mean_from_compiled_left(comp,6)
        self.assertEqual(independent["conditional_right_mean"],direct)
        self.assertEqual(independent["by_tag_population"],result["by_tag_population"])

    def test_exact_host_validation_and_no_asymptotic_overclaim(self):
        six=((0,10),(1,10),(2,11),(3,11),(4,12),(5,12))
        f=cycle_left()
        with self.assertRaises(ValueError):
            pinned_source_right_probability(six,f,6,{10:(0,1),11:(0,1)})
        with self.assertRaises(ValueError):
            pinned_source_right_probability(six,f,5,{})
        with self.assertRaises(ValueError):
            two_edge_orbit_certificate(six,f,6,10,10)
        with self.assertRaises(ValueError):
            pinned_source_right_probability(six,f,6,{10:(0,1),11:(2,3)},
                                            max_states=0)
        with self.assertRaises(ValueError):
            exact_centered_discrepancy(Fraction(1,2),-1)
        x=exact_centered_discrepancy(Fraction(3,2),1)
        self.assertEqual(x["signed_mean_minus_score"],Fraction(1,2))
        self.assertTrue(x["below_mean"])
        self.assertTrue(x["not_uniform_lower_or_concentration"])


if __name__=="__main__":
    unittest.main()
