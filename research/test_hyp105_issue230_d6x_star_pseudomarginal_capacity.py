"""HYP-105 D6-X independent exact local-star and global capacity falsifiers."""
import unittest
from collections import Counter
from fractions import Fraction
from math import comb
from itertools import combinations

from hyp105_issue230_d6x_star_pseudomarginal_capacity import (
    star_point_probability,right_injection_probability,
    typed_local_star_probability,enumerate_small_star,projective_oracle,
    lifted_column_occupancy_cut,genuine_original_sixset_star_zero,
    separator_only_dual_no_go,report,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_proof_audit import parameters


def direct_brute_two_site_star_probability(a,e,e_prime):
    numerator=denominator=0
    for center in range(a):
        neighbors=tuple(v for v in range(a) if v!=center)
        for n1 in neighbors:
            for n2 in neighbors:
                if n2==n1:
                    continue
                first=tuple(sorted((center,n1)))
                second=tuple(sorted((center,n2)))
                denominator+=1
                numerator+=(first==e and second==e_prime)
    return Fraction(numerator,denominator)


def independently_degree_is_bad(Q,labels):
    occurrences=Counter(coord for point,line in Q
                        for coord in labels[point])
    return (len(occurrences)!=6 or any(z!=2 for z in occurrences.values()))


class D6XProjectiveStarCapacityTests(unittest.TestCase):
    def test_exact_normalization_every_projective_subset_small_7_and_14(self):
        for a,n in ((7,4),(14,3)):
            z=projective_oracle(a,n)
            self.assertGreater(z["full_center_spoke_assignments"],1000)
            self.assertEqual(z["all_proper_subscopes_checked"],2**n-1)
            self.assertEqual(z["projective_consistency"],
                             "EXACT_RATIONAL_INDEPENDENT_ENUMERATION")
            # Two-site marginal for disjoint physical edges MUST vanish,
            # while intersecting edges have strictly positive probability.
            self.assertEqual(star_point_probability(a,((0,1),(2,3))),0)
            self.assertEqual(
                star_point_probability(a,((0,1),(0,2))),
                Fraction(1,a*(a-1)*(a-2)))

    def test_independent_two_site_center_spoke_enumeration_and_one_site(self):
        for a in (6,7,14):
            e,e_prime=(0,1),(0,2)
            joint=direct_brute_two_site_star_probability(a,e,e_prime)
            self.assertEqual(joint,
                             star_point_probability(a,(e,e_prime)))
            self.assertEqual(star_point_probability(a,(e,)),
                             Fraction(1,comb(a,2)))
            self.assertEqual(star_point_probability(a,((0,1),(0,1))),0)
            self.assertEqual(
                star_point_probability(a,((0,1),(1,2),(0,2))),0)
            self.assertEqual(
                star_point_probability(a,((0,1),(0,2),(0,3))),
                Fraction(1,a*(a-1)*(a-2)*(a-3)))

    def test_all_h_minimal_alphabet_lifted_column_capacity_violation(self):
        for h in range(1,9):
            z=lifted_column_occupancy_cut(2**h)
            a,V=z["a"],z["V"]
            self.assertEqual(z["V"],(2**h+1)*(2**(2*h)+1))
            self.assertGreaterEqual(comb(a,2),V)
            self.assertLess(comb(a-1,2),V)
            self.assertEqual(Fraction(z["point_edge_marginal"]),
                             Fraction(1,comb(a,2)))
            self.assertEqual(
                Fraction(z["unlifted_physical_column_expected_occupancy"]),
                Fraction(V,comb(a,2)))
            self.assertEqual(
                Fraction(z["conditional_other_original_point_occupancy"]),
                Fraction(V-1,2*(a-2)))
            self.assertLess(Fraction(z["lifted_capacity_slack"]),0)
            self.assertTrue(z["lifted_column_capacity_strictly_violated"])
        self.assertEqual(
            Fraction(lifted_column_occupancy_cut(4)[
                "conditional_other_original_point_occupancy"]),Fraction(7,2))

    def test_global_capacity_violation_by_direct_finite_count_s4(self):
        # No extrapolation: independent direct counting of all a*(a-1)*(a-2)
        # two-ORIGINAL-point star assignments at s=4, a=14.
        s=4
        p=parameters(s)
        a,V=p["a"],p["V"]
        e,e_prime=(0,1),(0,2)
        first=star_point_probability(a,(e,))
        joint=direct_brute_two_site_star_probability(a,e,e_prime)
        unconditional=V*first
        lifted=first-(V-1)*joint
        self.assertEqual((V,a),(85,14))
        self.assertLessEqual(unconditional,1)
        self.assertEqual(lifted,Fraction(-5,182))
        self.assertEqual((V-1)*joint/first,Fraction(7,2))

    def test_true_original_W34_W38_incidence_sixsets_star_all_zero(self):
        for power in (2,3):
            model=fixture(power,"lex")
            s=2**power
            E=tuple(tuple(e) for e in model["incidences"])
            by_point={}
            for p,l in E:
                by_point.setdefault(p,(p,l))
            self.assertGreaterEqual(len(by_point),6)
            Q1=tuple(by_point[i] for i in sorted(by_point)[:6])
            self.assertEqual(len({p for p,l in Q1}),6)
            Q2=tuple(E[:6])
            check=genuine_original_sixset_star_zero(s,E,[Q1,Q2])
            self.assertEqual(check["independent_original_sixsets_checked"],2)
            self.assertEqual(check["true_original_incidences_checked"],
                             len(E))
            for Q in (Q1,Q2):
                labels={p:(0,i+1) for i,p in
                        enumerate(dict.fromkeys(x for x,_ in Q))}
                self.assertTrue(independently_degree_is_bad(Q,labels))
            for item in check["rows"]:
                self.assertEqual(item["center_physical_degree"],6)
                self.assertTrue(item["local_left_injective"])

    def test_typed_local_marginals_and_fail_closed_inputs(self):
        a=14
        e0,e1=(0,1),(0,2)
        self.assertEqual(
            typed_local_star_probability(a,(e0,e1),((1,2),)),
            star_point_probability(a,(e0,e1))*
            right_injection_probability(a,((1,2),)))
        self.assertEqual(right_injection_probability(a,((0,1),(0,1))),0)
        self.assertEqual(typed_local_star_probability(a,(),()),1)
        self.assertEqual(star_point_probability(a,((1,3),(1,4))),
                         star_point_probability(a,((0,1),(0,2))))
        bad_inputs=((0,0),(3,1),(-1,3),(0,14))
        for bad in bad_inputs:
            with self.assertRaises(ValueError):
                star_point_probability(a,(bad,))
        with self.assertRaises(ValueError):
            star_point_probability(a,tuple((0,i) for i in range(1,a))+((0,1),))
        with self.assertRaises(ValueError):
            typed_local_star_probability(a,
                tuple((0,i) for i in range(1,a)),((1,2),))
        with self.assertRaises(ValueError):
            enumerate_small_star(14,4,max_states=1)
        with self.assertRaises(ValueError):
            genuine_original_sixset_star_zero(
                2,fixture(1,"lex")["incidences"],[])
        model=fixture(2,"lex")
        with self.assertRaises(ValueError):
            genuine_original_sixset_star_zero(4,model["incidences"],
                [tuple((84,84) for _ in range(6))])

    def test_all_h_separator_only_positive_dual_impossible_without_capacity(self):
        for h in range(2,7):
            x=separator_only_dual_no_go(2**h)
            a=parameters(2**h)["a"]
            self.assertEqual(x["max_certified_separator_region_rank"],a-1)
            self.assertGreaterEqual(a-1,12)
            self.assertEqual(x["every_original_Q_seven_GF5_expected_cost"],0)
            self.assertEqual(x["signed_overlap_messages_sum"],"0")
            self.assertEqual(
                sum(Fraction(v) for v in
                    x["signed_common_original_point_messages"]),0)
            self.assertEqual(
                x["positive_root_bound_by_this_separator_only_dual"],"IMPOSSIBLE")
            self.assertFalse(x["global_physical_column_lifts_in_model"])
            self.assertFalse(x["generic_Sherali_Adams_no_go"])
        with self.assertRaises(ValueError):
            separator_only_dual_no_go(2)

    def test_report_rejects_SA_claim_and_keeps_root_open(self):
        x=report()
        self.assertEqual(x["all_h_h_ge_2_scope_rank"],"a_minus_1")
        self.assertEqual(x["all_h_original_sixset_left_center_degree"],6)
        self.assertEqual(x["selected_nonnegative_GF5_numerator_local_expected"],0)
        self.assertEqual(x["capacity_failure_rank"],
             "TWO-FOR-LIFTED-GLOBAL-PHYSICAL-COLUMN-CONSTRAINT")
        self.assertEqual(x["first_order_global_capacity"],"SATISFIED")
        self.assertFalse(x["this_is_feasible_Sherali_Adams_for_global_assignment"])
        self.assertFalse(x["general_Sherali_Adams_no_go"])
        self.assertEqual(x["all_h_unanchored_separator_only_dual_positive"],"NO_GO")
        self.assertEqual(len(x["all_h_separator_only_no_go"]),5)
        self.assertFalse(x["global_original_root_PROVED_A"])
        self.assertFalse(x["infinite_correlated_counterexample_PROVED_B"])
        self.assertEqual((x["Branch_A"],x["Branch_B"]),("OPEN","OPEN"))


if __name__=="__main__":
    unittest.main()
