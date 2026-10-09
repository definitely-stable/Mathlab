"""Independent finite graph, GF5 histogram and all-h boundary tests for B3.1-B."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
import unittest

from hyp105_g5e2b3b1_critical_flows import (
    CYCLE, SIGNS, critical_supports, exact_nowherezero_signed_flow,
    two_factors,
)
from hyp105_g5e2b1_energy import single_signed_trade_mitm
from hyp105_g5e2b3b1b_five_six_flows import (
    DUAL_ORBITS, FIVE_PALETTE, _coordinate_character_factor,
    exact_dual_GF5_six_flow, five_graph_types, five_six_supports,
    five_six_complete_census, five_six_all_h_expected_obstruction,
)


def direct_character(values):
    return sum(
        __import__("math").prod(4 if v==candidate else -1 for v in values)
        for candidate in range(5)
    )


def brute_five_graph_count():
    count=0
    degtypes=Counter()
    for chosen in combinations(FIVE_PALETTE,6):
        degree=Counter(x for p in chosen for x in p)
        if len(degree)==5 and min(degree.values())>=2:
            count+=1
            degtypes[tuple(sorted(degree.values(),reverse=True))]+=1
    return count,degtypes


class GF5FiveSixClassificationTests(unittest.TestCase):
    def test_character_sum_direct_all_phase_partitions(self):
        for size in (1,2,3,4,5,6):
            values=tuple((i*i+2*i)%5 for i in range(size))
            self.assertEqual(_coordinate_character_factor(values),
                             direct_character(values))
            self.assertEqual(_coordinate_character_factor((0,)*size),
                             direct_character((0,)*size))
        with self.assertRaises(ValueError):
            _coordinate_character_factor(())

    def test_exact_dual_orbit_count_and_gauge(self):
        self.assertEqual(len(DUAL_ORBITS),782)
        self.assertEqual({weight for _,weight in DUAL_ORBITS},{1,4,-1})
        expanded=set()
        for representative,_ in DUAL_ORBITS:
            for multiplier in (1,2,3,4):
                expanded.add(tuple((x*multiplier)%5 for x in representative))
        self.assertEqual(len(expanded),5**5)
        self.assertTrue(all(t[0]==0 for t in expanded))

    def test_exact_dual_agrees_with_previous_independent_full_GF5(self):
        for right in (CYCLE,two_factors()[-1]):
            supports=critical_supports(CYCLE,right)
            for mask in (SIGNS[0],SIGNS[-1]):
                signs=tuple(1 if mask&(1<<i) else -1 for i in range(6))
                exact=exact_dual_GF5_six_flow(supports,signs,dimension=12)
                other=exact_nowherezero_signed_flow(CYCLE,right,mask)
                self.assertEqual(exact,other)

    def test_five_graphs_three_classes_have_exhaustive_sizes(self):
        graph_types=five_graph_types()
        self.assertEqual([x[1] for x in graph_types],[15,60,10])
        count,degree_patterns=brute_five_graph_count()
        self.assertEqual(count,85)
        self.assertEqual(degree_patterns,{
            (4,2,2,2,2):15,
            (3,3,2,2,2):70,
        })
        self.assertEqual(len(two_factors()),70)

    def test_mixed_5x6_full_GF5_independent_MITM_and_side_swap(self):
        for left,_ in five_graph_types():
            for right in (two_factors()[0],two_factors()[-1]):
                supports=five_six_supports(left,right)
                mask=SIGNS[0]
                signs=tuple(1 if mask&(1<<i) else -1 for i in range(6))
                dual=exact_dual_GF5_six_flow(supports,signs,dimension=11)
                independent=single_signed_trade_mitm(
                    supports,signs,11,max_side_assignments=51**3)
                self.assertEqual(dual,independent["weighted_flow_count"])
                self.assertGreater(dual,0)
                # Swap physical coordinate colors, no claim of equivariance
                # under arbitrary finite symplectic maps.
                transpose=tuple(tuple(
                    sorted((c+6 if c<5 else c-5) for c in row))
                    for row in supports)
                self.assertEqual(exact_dual_GF5_six_flow(
                    transpose,signs,dimension=11),dual)
                # Global sign reversal leaves coordinate balance invariant.
                self.assertEqual(exact_dual_GF5_six_flow(
                    supports,tuple(-x for x in signs),dimension=11),dual)
                col_perm=(1,2,3,4,5,0)
                self.assertEqual(exact_dual_GF5_six_flow(
                    tuple(supports[i] for i in col_perm),
                    tuple(signs[i] for i in col_perm),dimension=11),dual)

    def test_singleton_coordinate_is_rigorously_zero(self):
        left,_=five_graph_types()[0]
        supports=list(five_six_supports(left,two_factors()[0]))
        # First column: a new physical coordinate appears only once.
        prior=supports[0]
        supports[0]=tuple(sorted(tuple(prior[:-1])+(11,)))
        result=exact_dual_GF5_six_flow(
            supports,(1,-1,1,-1,1,-1),dimension=12)
        self.assertEqual(result,0)
        with self.assertRaises(ValueError):
            exact_dual_GF5_six_flow(supports,(1,1,1,-1,-1,-1),dimension=11)
        with self.assertRaises(ValueError):
            exact_dual_GF5_six_flow(supports,(1,1,1,1,-1,-1),dimension=12)
        with self.assertRaises(ValueError):
            exact_dual_GF5_six_flow((supports[0],)*6,
                                    (1,-1,1,-1,1,-1),dimension=12)

    def test_complete_all_2100_cases_and_true_positive_floor(self):
        result=five_six_complete_census()
        self.assertEqual(result["total_representative_signed_cases"],2100)
        self.assertEqual(result["positive_representative_signed_cases"],2100)
        self.assertEqual(result["zero_representative_signed_cases"],0)
        self.assertEqual(result["universal_per_event_GF5_flow_lower"],10950)
        self.assertEqual(result["per_matched_six_set_risk_numerator_lower"],
                         109500)
        self.assertEqual(
            [x["minimum_exact_GF5_flow"] for x in result["by_type"]],
            [14400,10950,11685])
        self.assertEqual(
            [x["maximum_exact_GF5_flow"] for x in result["by_type"]],
            [17955,12357,12405])
        self.assertFalse(result["complete_other_six_motifs"])
        self.assertFalse(result["all_h_R3_upper_proved"])

    def test_random_matching_class_exact_projection_probabilities(self):
        for s in (2,4,8,16):
            result=five_six_all_h_expected_obstruction(s)
            p5=Fraction(result["P5_exact"])
            p6=Fraction(result["P6_exact"])
            self.assertGreater(p5,0)
            self.assertGreater(p6,0)
            self.assertLessEqual(p5+p6,1)
            self.assertGreater(Fraction(result["random_E_U56_lower"]),0)
            self.assertGreater(
                Fraction(result["random_expected_R3_lower_from_U56"]),0)
            self.assertFalse(result["all_h_R3_upper_proved"])
            self.assertFalse(result["new_ASET_exponent_proved"])
        with self.assertRaises(ValueError):
            five_six_all_h_expected_obstruction(3)


if __name__=="__main__":
    unittest.main()
