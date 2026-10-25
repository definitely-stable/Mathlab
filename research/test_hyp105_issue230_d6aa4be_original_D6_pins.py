"""AA4-BE exact original six-incidence D6 adversarial pinned map oracles."""
import unittest
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4be_original_D6_pins import (
    falling, original_D6_sixflag_pinned_envelope,
    original_W32_true_source_candidate_and_physical_cycle_census,
)


def brute_cycle_count_on_vertices(vertices,occupied):
    """Independent K_a physical cycle recognizer using rooted 6-vertex tuples."""
    count=0
    for z in permutations(vertices,6):
        if z[0]!=min(z) or z[1]>z[-1]:
            continue
        if all(tuple(sorted((z[i],z[(i+1)%6]))) in occupied for i in range(6)):
            count+=1
    return count


def independent_physical_cycle_completion_six_edge_oracle():
    """One fixed physical C6 on six coords; six complete source-line images.

    Directly check the historical D6 physical pair-position alignment:
    all six mapped pair edges form the same 6-cycle adjacency as the
    pinned six original point physical edges, not merely any cycle.
    """
    e=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
    def connected_rainbow(physical):
        if len(set(physical))!=6:
            return False
        shared=[]
        for i in range(6):
            ab=set(physical[i]) & set(physical[(i+1)%6])
            if len(ab)!=1:
                return False
            shared.append(next(iter(ab)))
        return len(set(shared))==6
    good=sum(connected_rainbow(z) for z in permutations(e))
    return good, len(list(permutations(e)))


class AA4BESixTrueOriginalGF5D6PinnedTest(unittest.TestCase):
    def test_01_all_h_exact_rational_D6_six_original_flag_extension(self):
        for h in tuple(range(5,35))+(40,48,64,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//16):
                x=original_D6_sixflag_pinned_envelope(s,k)
                self.assertEqual(x["allowed_arbitrary_original_LINE_pin_count"],V//16)
                self.assertGreaterEqual(
                    x["one_global_conditional_original_sixID_D6_expected_count_lower"],s**6)
                self.assertGreaterEqual(
                    x["one_global_conditional_original_sixID_D6_expected_count_lower"],
                    Fraction(27,25)*(s+1)**6)
                self.assertGreaterEqual(
                    x["right_physical_C6_avoiding_all_pinned_pair_edge_images_floor"],
                    x["K_a_full_physical_C6"]/2)
                self.assertGreaterEqual(
                    x["original_point_C6_sixflag_candidates_avoiding_all_pinned_line_IDs_floor"],
                    x["K_a_full_physical_C6"]*(s+1)**6/2)
                self.assertTrue(
                    x["some_complete_legal_extension_selected_original_D6_ge_s6"])
                self.assertTrue(
                    x["every_given_full_original_g_has_positive_D6_NOT_PROVED"])
                self.assertTrue(
                    x["seven_GF5_sum_for_EACH_complete_f_g_NOT_PROVED"])
                self.assertEqual(x["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_true_original_W32_all_four_global_typed_supports_and_pins(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            V=len(m["right_labels"])
            left={tuple(sorted(e)) for e in m["left_labels"]}
            right={tuple(sorted(e)) for e in m["right_labels"]}
            self.assertEqual(len(left),V)
            self.assertEqual(len(right),V)
            for k in (0,1,2):
                pins={i:m["right_labels"][(i+3)%V] for i in range(k)}
                c=original_W32_true_source_candidate_and_physical_cycle_census(m,pins)
                self.assertEqual(c["k"],k)
                self.assertLessEqual(c["original_sixflag_candidates_avoiding_pinned_lines"],
                                     c["original_pointC6_six_distinct_lineID_source_Q_count"])
                self.assertLessEqual(c["right_C6_cycles_avoiding_pinned_physical_edges"],
                                     c["point_C6_count"])
                self.assertGreaterEqual(
                    c["exact_ONE_complete_original_LINE_permutation_conditional_D6_mean"],0)
                if k==0:
                    self.assertEqual(c["point_C6_count"],60)
                    self.assertEqual(c["original_pointC6_six_distinct_lineID_source_Q_count"],
                                     21186 if scheme.startswith("S") else 18716)
                    self.assertEqual(c["right_C6_cycles_avoiding_pinned_physical_edges"],60)
                    self.assertEqual(c[
                        "exact_ONE_complete_original_LINE_permutation_conditional_D6_mean"],
                        Fraction(c["original_pointC6_six_distinct_lineID_source_Q_count"]*720,
                                 falling(V,6)))
            print("AA4BE_W32",scheme,c["original_pointC6_six_distinct_lineID_source_Q_count"],
                  c["right_C6_cycles_avoiding_pinned_physical_edges"])

    def test_03_independent_K6_sixcycle_rainbow_original_flag_positions(self):
        good,total=independent_physical_cycle_completion_six_edge_oracle()
        self.assertEqual(total,720)
        self.assertEqual(good,12)
        E={tuple(sorted(x)) for x in combinations(range(6),2)}
        self.assertEqual(brute_cycle_count_on_vertices(range(6),E),60)
        for k in (0,1,2,3):
            removed={tuple(sorted(x)) for x in list(E)[:k]}
            whole=brute_cycle_count_on_vertices(range(6),E-removed)
            self.assertGreaterEqual(whole,60-24*k)
            self.assertLessEqual(whole,60)

    def test_04_one_original_LINE_factor_source_influence_exact_girth_scope(self):
        for scheme in ("lex","S68"):
            m=fixture(1,scheme)
            inc=set(map(tuple,m["incidences"]))
            self.assertEqual(len(inc),45)
            for p in range(15):
                n={l for x,l in inc if x==p}
                self.assertEqual(len(n),3)
            for l in range(15):
                n={p for p,x in inc if x==l}
                self.assertEqual(len(n),3)
            # Any two TRUE ORIGINAL distinct point factors share
            # at most ONE original line factor: exact GQ girth >=8.
            for x,y in combinations(range(15),2):
                common=({l for p,l in inc if p==x} &
                        {l for p,l in inc if p==y})
                self.assertLessEqual(len(common),1)

    def test_05_invalid_original_pins_and_unproved_domain_fail_closed(self):
        for s in (0,2,4,8,16,24,33,48,True,Fraction(32,1)):
            with self.assertRaises(ValueError):
                original_D6_sixflag_pinned_envelope(s,0)
        V=(32+1)*(32**2+1)
        for k in (-1,V//16+1,V,Fraction(1,2),True):
            with self.assertRaises(ValueError):
                original_D6_sixflag_pinned_envelope(32,k)
        m=fixture(1,"lex")
        for bad in ({-1:m["right_labels"][0]}, {0:(6,7)},
                    {0:m["right_labels"][1],1:m["right_labels"][1]},
                    {15:m["right_labels"][0]}):
            with self.assertRaises(ValueError):
                original_W32_true_source_candidate_and_physical_cycle_census(m,bad)
        with self.assertRaises(ValueError):
            falling(5,6)

if __name__=="__main__":
    unittest.main()
