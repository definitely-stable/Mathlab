"""AA4-CM independent true original W34/W38 negative named D6 covariance."""
import unittest
from fractions import Fraction
from collections import Counter

from hyp105_issue230_d6aa4cm_negative_original_named_pair_covariance import (
    exact_original_negative_named_dual_choice,
    true_original_negative_D6_pair_fixture,
    full_original_fiber_check_negative_named_vs_entire,
    _right_physical_edges_for_dual,
    EXPECTED_NAMED_NEGATIVE_COV,N_STATES,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    ORBIT,FAMILIES,complete_overlapping_global_f,_cov,GRAPH_CASES,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    _six_position_dual_cycle,W_D,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)


def independent_literal_original_named_Q_D6(Q,inc,f,g):
    """Direct independent source incidence-position graph matcher.

    No call to historical tagger, spectral graph, histogram score, or
    right-cycle choice. The original Q must be six real unique flags
    and EACH projection has six physical coordinates degree two.
    """
    if len(set(Q))!=6 or len(Q)!=6:
        return False
    if len(set(inc[j][0] for j in Q))!=6 or len(set(inc[j][1] for j in Q))!=6:
        return False
    ds=[]
    for side,mapping in ((0,f),(1,g)):
        coordinate={}
        for k,j in enumerate(Q):
            for v in mapping[inc[j][side]]:
                coordinate.setdefault(v,[]).append(k)
        if len(coordinate)!=6 or any(len(a)!=2 for a in coordinate.values()):
            return False
        dual=frozenset(frozenset(x) for x in coordinate.values())
        if len(dual)!=6:return False
        # independently DFS on the SIX immutable original flag slots
        adj=[set() for i in range(6)]
        for e in dual:
            a,b=tuple(e)
            adj[a].add(b);adj[b].add(a)
        if any(len(x)!=2 for x in adj):
            return False
        visited=set();stack=[0]
        while stack:
            a=stack.pop()
            if a in visited:continue
            visited.add(a);stack.extend(adj[a]-visited)
        if len(visited)!=6:return False
        ds.append(dual)
    return ds[0]==ds[1]


class AA4CMOriginalNegativeCovariance(unittest.TestCase):
    def test_01_exact_96_global_cycle_pair_selection_and_abstract_negative_named_covariance(self):
        d=exact_original_negative_named_dual_choice()
        self.assertEqual(d["right_dual_orientation_pairs_examined"],24*24)
        self.assertEqual(d["right_dual_pairs_with_strictly_negative_named_covariance"],528)
        self.assertEqual(d["each_true_original_D6_named_Q_positive_states"],4)
        self.assertEqual(d["both_TRUE_original_Q_D6_coaccepted_states"],0)
        self.assertEqual(d["named_historical_weighted_GF5_covariance"],
                         Fraction(-W_D*W_D,576))
        self.assertEqual(d["weighted_named_mean_each"],Fraction(W_D,24))
        ca,cb=d["original_f_A_labeled_right_cycle"],d["original_f_B_labeled_right_cycle"]
        eA=_right_physical_edges_for_dual(ca,range(6))
        eB=_right_physical_edges_for_dual(cb,range(6,12))
        self.assertEqual(_six_position_dual_cycle(eA),ca)
        self.assertEqual(_six_position_dual_cycle(eB),cb)
        self.assertFalse(set(eA)&set(eB))
        print("AA4CM_ABSTRACT_COMBINATORIAL_ORBIT_NEGATIVE",
              "orientations",d["right_dual_orientation_pairs_examined"],
              "strict_negative",d["right_dual_pairs_with_strictly_negative_named_covariance"],
              "cov",str(d["named_historical_weighted_GF5_covariance"]),flush=True)

    def _real_Q_falsifier(self,h):
        z=true_original_negative_D6_pair_fixture(h)
        s,V,a,inc,f,g,_,_=_original_source(z["actual_original_model"])
        QA=z["QA_six_true_original_incidence_IDs"]
        QB=z["QB_six_true_original_incidence_IDs"]
        pts=z["eight_REAL_original_POINT_source_ids"]
        self.assertEqual(z["true_original_common_POINT_factor_ids"],4)
        self.assertEqual(z["true_original_common_incidence_flag_ids"],0)
        self.assertEqual(len(set(QA)|set(QB)),12)
        self.assertEqual(len(set(z["twelve_distinct_REAL_original_LINE_source_ids"])),12)
        # Point IDs 0..3 shared, but original line IDs at those
        # points differ; flags are therefore completely disjoint.
        for fam,Q in (("A",QA),("B",QB)):
            self.assertEqual(set(inc[j][0] for j in Q),
                             set(pts[i] for i in FAMILIES[fam]))
            self.assertEqual(len(set(inc[j][1] for j in Q)),6)
        self.assertEqual(len(set(f)),V)
        self.assertEqual(len(set(g)),V)
        rawA=[];rawB=[]
        for st in ORBIT:
            changed=complete_overlapping_global_f(f,pts,st)
            tags=[]
            for Q in (QA,QB):
                independent=independent_literal_original_named_Q_D6(Q,inc,changed,g)
                historical=classify_seven_all_a_original_Q(Q,changed,g,inc)=="D6"
                self.assertEqual(independent,historical)
                tags.append(int(independent))
            rawA.append(tags[0]);rawB.append(tags[1])
        self.assertEqual(sum(rawA),4)
        self.assertEqual(sum(rawB),4)
        self.assertEqual(sum(x*y for x,y in zip(rawA,rawB)),0)
        self.assertEqual(_cov(tuple(W_D*x for x in rawA),
                              tuple(W_D*y for y in rawB)),
                         EXPECTED_NAMED_NEGATIVE_COV)
        self.assertTrue(z["physical_RIGHT_image_coordinates_disjoint"])
        self.assertTrue(z["one_fixed_complete_original_LINE_g"])
        print("AA4CM_TRUE_ORIGINAL_NEGATIVE_NAMED_D6",
              "s",s,"V",V,"flags",len(inc),
              "source_Q_12",len(set(QA)|set(QB)),
              "positive_A_B",(sum(rawA),sum(rawB)),
              "simultaneous",0,
              "cov",str(EXPECTED_NAMED_NEGATIVE_COV),flush=True)

    def test_02_real_original_W34_s4_negative_historical_D6_named_covariance(self):
        self._real_Q_falsifier(2)

    def test_03_real_original_W38_s8_negative_historical_D6_named_covariance(self):
        self._real_Q_falsifier(3)

    def test_04_entire_real_original_pointA_fiber_cannot_inherit_named_sign_without_check(self):
        for h in (2,3):
            z=full_original_fiber_check_negative_named_vs_entire(h)
            self.assertEqual(z["named"]["named_GF5_historical_weighted_covariance"],
                             EXPECTED_NAMED_NEGATIVE_COV)
            self.assertEqual(z["named"]["all_96_genuine_original_global_states_classified"],96)
            self.assertTrue(z["full_global_seven_GQ_S_NOT_computed"])
            self.assertTrue(z["independently_directly_historical_sevenclass_96map_full_Q_referee"])
            # Strict NEGATIVE full true-original A/A-source-family
            # cross-covariance on real W34; ZERO on real W38.
            # The negative NAMED Q covariance persists on BOTH.
            self.assertEqual(z["entire_source_POINT_A_fiber_covariance"],
                             Fraction(-10614483,32) if h==2 else Fraction(0))
            self.assertEqual((
                z["entire_source_POINT_A_fiber_right_eligible_Q_A"],
                z["entire_source_POINT_A_fiber_right_eligible_Q_B"]),
                (4,12) if h==2 else (7,55))
            self.assertGreaterEqual(
                z["entire_source_POINT_A_fiber_right_eligible_Q_A"],1)
            self.assertGreaterEqual(
                z["entire_source_POINT_A_fiber_right_eligible_Q_B"],1)
            print("AA4CM_ENTIRE_ORIGINAL_POINT_A_FIBER_CHECK",
                  "s",z["named"]["s"],
                  "named_negative",str(EXPECTED_NAMED_NEGATIVE_COV),
                  "whole_fiber_covariance",str(
                      z["entire_source_POINT_A_fiber_covariance"]),
                  "right_Q_A_B",(
                    z["entire_source_POINT_A_fiber_right_eligible_Q_A"],
                    z["entire_source_POINT_A_fiber_right_eligible_Q_B"]),flush=True)

    def test_05_malformed_input_failclosed_and_W32_not_claimed(self):
        with self.assertRaises(ValueError):
            true_original_negative_D6_pair_fixture(1)
        with self.assertRaises(ValueError):
            true_original_negative_D6_pair_fixture(4)
        with self.assertRaises(ValueError):
            true_original_negative_D6_pair_fixture(True)
        d=exact_original_negative_named_dual_choice()
        with self.assertRaises(ValueError):
            _right_physical_edges_for_dual(d["original_f_A_labeled_right_cycle"],
                                           (0,0,1,2,3,4))
        with self.assertRaises(ValueError):
            _right_physical_edges_for_dual(d["original_f_A_labeled_right_cycle"],
                                           range(5))
        with self.assertRaises(ValueError):
            _right_physical_edges_for_dual(frozenset((frozenset((0,1)),)),
                                           range(6))


if __name__=="__main__":
    unittest.main()
