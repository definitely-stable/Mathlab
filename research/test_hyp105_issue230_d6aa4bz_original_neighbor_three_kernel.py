"""AA4-BZ rigorous original six-packet right-2factor 3-neighbor and kernel."""

import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    CUBE6_INDEPENDENT_HIGH_PASS,original_six_packet_source_line_A,
)
from hyp105_issue230_d6aa4bz_original_neighbor_three_kernel import (
    CUBE6_NEIGHBOR_THREE_HIGH_PASS,
    CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING,
    CUBE6_RADIAL_KERNEL,exact_sixcube_neighbor_three_kernel_certificate,
    assert_radial_relaxation,original_Q_sixcube_physical_neighbor_three,
    original_W32_f_only_all_seven_neighbor_three_envelope,
    original_W32_all64_true_center_neighbor_three,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import high_degree_boolean_kernel
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def independent_count_allowed_physical_neighbors_of_base_six_edges(base,all_edges):
    """K6 direct distinct-edge completion, no source or parent helpers.

    For each of six chosen base edges, collect ALL nine globally unused
    pair edges which make the other five fixed base edges plus this
    substituted edge physically 2regular. Then find MAXIMUM matching
    of replacement edges to distinct packet indices by augmenting
    paths. Distinct replacements enforce ORIGINAL global injection.
    """
    occupied=set(base)
    free=tuple(e for e in all_edges if e not in occupied)
    eligible=[]
    for old in base:
        survivors=tuple(e for e in base if e!=old)
        feasible=[]
        for added in free:
            degree=Counter(u for e in survivors+(added,) for u in e)
            if len(degree)==6 and all(n==2 for n in degree.values()):
                feasible.append(added)
        eligible.append(feasible)
    right_owner={}
    def augment(i,seen):
        for edge in eligible[i]:
            if edge in seen:continue
            seen.add(edge)
            if edge not in right_owner or augment(right_owner[edge],seen):
                right_owner[edge]=i
                return True
        return False
    return sum(augment(i,set()) for i in range(6))


class BZTrueOriginalPhysicalNeighborThree(unittest.TestCase):
    def test_01_all_h_exact_rational_6cube_kernel_dual(self):
        z=exact_sixcube_neighbor_three_kernel_certificate()
        self.assertEqual(z["radial_degree_ge4_Walsh_kernel"],CUBE6_RADIAL_KERNEL)
        self.assertEqual(z["signed_highpass_numerator_upper"],Fraction(139,2))
        self.assertEqual(z["signed_highpass_numerator_lower"],Fraction(-264,5))
        self.assertEqual(z["true_original_sixcube_eta_upper"],Fraction(139,128))
        self.assertEqual(CUBE6_INDEPENDENT_HIGH_PASS,Fraction(45,32))
        self.assertEqual(CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING,
                         Fraction(41,128))
        self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        p=(Fraction(1),Fraction(0),Fraction(1,4),Fraction(3,4),
           Fraction(0),Fraction(0),Fraction(1))
        assert_radial_relaxation(p)
        lower=(0,Fraction(1,2),0,0,Fraction(3,5),Fraction(2,5),0)
        assert_radial_relaxation(lower)
        def score(q):
            return sum(comb(6,j)*CUBE6_RADIAL_KERNEL[j]*q[j]
                       for j in range(7))
        self.assertEqual(score(p),Fraction(139,2))
        self.assertEqual(score(lower),Fraction(-264,5))
        self.assertLess(CUBE6_NEIGHBOR_THREE_HIGH_PASS,
                        CUBE6_INDEPENDENT_HIGH_PASS)
        self.assertFalse(z["eta_upper_NOT_sharp_realizability"]==False)

    def test_02_original_W32_sixpacket_each_true_Q_all64_neighbor_sparsity(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            Qs=tuple(Q for Q,_ in selected_left_six(model)
                     if original_six_packet_source_line_A(Q,inc,PACKETS,V))
            self.assertEqual(len(Qs),351 if scheme=="lex" else 301)
            max_neighbors=0;nonempty=0
            maps=tuple(apply_disjoint_factor_swaps(
                g,PACKETS,tuple(i for i in range(6) if x>>i&1))
                for x in range(64))
            for Q in Qs:
                a=original_Q_sixcube_physical_neighbor_three(model,Q,PACKETS)
                b=a["physical_2factor_global_right_map_indicator"]
                if any(b):nonempty+=1
                max_neighbors=max(max_neighbors,a["max_accepted_neighbors_in_sixcube"])
                self.assertLessEqual(max_neighbors,3)
                self.assertTrue(a["six_true_original_LINE_source_packets_distinct"])
                for x in range(64):
                    true_historical=classify_seven_prechecked(Q,f,maps[x],inc)
                    self.assertLessEqual(int(true_historical is not None),b[x])
                    self.assertLessEqual(sum(b[x^(1<<i)] for i in range(6)),3)
            print("AA4BZ_W32",scheme,"original_Q",len(Qs),
                  "physical_active_Q",nonempty,
                  "max_true_physical_neighbors",max_neighbors,flush=True)

    def test_03_independent_COMPLETE_K6_distinct_replacement_matching(self):
        """Exhaust all 5,005 distinct SIX-edge base subsets of K6.

        For every base, build all feasible one-edge replacement pairs
        independently, then a maximum matching across six original
        source packet indices ensures replacements are mutually
        distinct. This is a separate finite physical oracle, NOT
        the all-h mathematical proof or an artificial large W3.
        """
        edges=tuple(combinations(range(6),2))
        hist=Counter()
        for base in combinations(edges,6):
            m=independent_count_allowed_physical_neighbors_of_base_six_edges(
                base,edges)
            hist[m]+=1
            self.assertLessEqual(m,3)
        self.assertEqual(sum(hist.values()),5005)
        self.assertEqual(hist,Counter({0:2665,1:1260,2:720,3:360}))
        self.assertEqual(max(hist),3)

    def test_04_original_W32_all_seven_f_only_center_strict_improvement(self):
        expected={
            "lex":{
                "mass":4690929,
                "saving":Fraction(192328089,128),
                "error":Fraction(64996597819,128),
                "center":11225795},
            "S72":{
                "mass":3731790,
                "saving":Fraction(76501695,64),
                "error":Fraction(31102815453,64),
                "center":3283610},
        }
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            env=original_W32_f_only_all_seven_neighbor_three_envelope(
                model,PACKETS)
            self.assertEqual(
                env["weighted_six_source_packet_original_Q_mass"],
                expected[scheme]["mass"])
            self.assertEqual(env["strict_saving"],expected[scheme]["saving"])
            self.assertEqual(
                env["new_original_f_only_ALL_SEVEN_error_upper"],
                expected[scheme]["error"])
            self.assertGreater(env["strict_saving"],0)
            self.assertLess(env["new_original_f_only_ALL_SEVEN_error_upper"],
                            env["parent_all_seven_f_only_E"])
            alternate=dict(model,right_labels=tuple(reversed(model["right_labels"])))
            changed=original_W32_f_only_all_seven_neighbor_three_envelope(
                alternate,PACKETS)
            self.assertEqual(env["new_original_f_only_ALL_SEVEN_error_upper"],
                             changed["new_original_f_only_ALL_SEVEN_error_upper"])
            center=original_W32_all64_true_center_neighbor_three(model,PACKETS)
            self.assertEqual(center["original_seven_GF5_unchanged_center"],
                             expected[scheme]["center"])
            self.assertEqual(center["new_f_only_ALL_SEVEN_kernel_E"],
                             expected[scheme]["error"])
            self.assertEqual(center["original_center_certified_nonnegative_lower"],0)
            self.assertEqual(center["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            print("AA4BZ_FQUENCH",scheme,
                  "old",env["parent_all_seven_f_only_E"],
                  "new",env["new_original_f_only_ALL_SEVEN_error_upper"],
                  "reduction",env["strict_saving"],flush=True)

    def test_05_adversarial_original_fails_closed(self):
        for bad in (
            (Fraction(0),)*6,
            (Fraction(0),)*6+(Fraction(2),),
            (Fraction(1),)*7,
            (Fraction(-1),)*7,
        ):
            with self.assertRaises(ValueError):
                assert_radial_relaxation(bad)
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        Q=next(Q for Q,_ in selected_left_six(model)
               if original_six_packet_source_line_A(Q,inc,PACKETS,V))
        for bad in (PACKETS[:5],
                    ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10))):
            with self.assertRaises(ValueError):
                original_Q_sixcube_physical_neighbor_three(model,Q,bad)
        with self.assertRaises(ValueError):
            original_Q_sixcube_physical_neighbor_three(
                dict(model,right_labels=((0,1),)*15),Q,PACKETS)
        with self.assertRaises(ValueError):
            original_W32_f_only_all_seven_neighbor_three_envelope(
                fixture(2,"lex"),PACKETS)

    def test_06_abstract_parent_extremizer_falsified_by_new_neighborhood(self):
        """Original parent #599 negative MAXIMIZER cannot be physical."""
        K=high_degree_boolean_kernel(6)
        parent_extremizer=frozenset(x for x in range(64)
                                   if x.bit_count() in (1,4))
        self.assertEqual(sum(K[x] for x in parent_extremizer),-90)
        self.assertTrue(all(x^(1<<i) not in parent_extremizer
                            for x in parent_extremizer for i in range(6)))
        self.assertEqual(sum(x in parent_extremizer for x in
                             (1,2,4,8,16,32)),6)
        self.assertGreater(6,3)
        # Parent 'sharp over all abstract independent sets' IS TRUE,
        # but its sharp witness violates TRUE physical degree2 local
        # neighborhood constraints. Not a new W3 counterfamily.

if __name__=="__main__":
    unittest.main()
