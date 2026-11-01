"""Independent R5 all-four-position original cubic versus physical CORE tests."""
from collections import Counter
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source, planted_original_k44
from hyp105_original_four_blocker_cubic_referee import (
    minimal_alphabet, _source, original_flag_triple_cubic,
    evaluate_original_cubic, independent_physical_core_histogram,
    audit_original_four_blocker_cubic,
)
from hyp105_four_internal_blocker_weighted_referee import four_blocker_referee


def complete_maps(power, shift=0, point_multiplier=1):
    _,v,_=genuine_source(power)
    a=minimal_alphabet(v)
    labels=tuple(combinations(range(a),2))[:v]
    return (tuple(labels[(point_multiplier*i)%v] for i in range(v)),
            tuple(labels[(19*i+shift)%v] for i in range(v)))


class ActualOriginalFourBlockerCubic(unittest.TestCase):
    def test_universal_cubic_property_genuine_W32_full_core_and_128_subcores(self):
        _,v,flags=genuine_source(1)
        f,g=complete_maps(1,0)
        polynomial=original_flag_triple_cubic(1,f,g)
        self.assertEqual(polynomial["full_incidence_count"],45)
        self.assertEqual(polynomial["paired_edges_in_universe"],90)
        self.assertTrue(polynomial["coefficients"])
        self.assertTrue(all(len(support)==3 for (support,_,_) in polynomial["coefficients"]))
        full=evaluate_original_cubic(polynomial,range(len(flags)))
        actual=independent_physical_core_histogram(1,f,g,range(len(flags)))
        self.assertEqual(full,actual["histogram"])
        self.assertGreater(sum(full.values()),0)
        # Exact 7-dimensional original-ID retention cube (NOT random samples).
        selected=tuple(range(7))
        for mask in range(1<<len(selected)):
            core=tuple(i for j,i in enumerate(selected) if (mask>>j)&1)
            expected=evaluate_original_cubic(polynomial,core)
            independent=independent_physical_core_histogram(1,f,g,core)
            self.assertEqual(expected, independent["histogram"],msg="core="+str(core))
            for good in (False,True):
                self.assertLessEqual(
                    sum(z for (gg,mm),z in expected.items() if gg==good and mm),
                    sum(z for (gg,mm),z in full.items() if gg==good and mm))

    def test_actual_W32_multiple_full_correlated_injections_and_original_four_positions(self):
        _,v,flags=genuine_source(1)
        nonempty=0
        blocked=0
        for shift in (0,3,7):
            f,g=complete_maps(1,shift)
            audit=audit_original_four_blocker_cubic(1,f,g,range(len(flags)),
                                                   range(len(flags)))
            nonempty+=audit["projected_endgood"]
            blocked+=audit["endgood_blocked_union"]
            self.assertEqual(audit["physical_paired_edges"],90)
            self.assertTrue(audit["exact_cubic_for_this_core"])
            self.assertLessEqual(audit["endgood_blocked_union"],
                                 sum(audit["four_position_counts"]))
            historical=four_blocker_referee(1,f,g)
            direct=independent_physical_core_histogram(1,f,g,range(len(flags)))
            self.assertEqual(
                sum(direct["position_counts"][gg,j] for gg in (False,True) for j in range(4)),
                sum(historical["proper_blocked_by_position"]))
            self.assertEqual(
                sum(direct["histogram"].values()),
                historical["proper_paths_with_decoded_nonincident_ends"])
        self.assertGreater(nonempty,0)
        self.assertGreater(blocked,0)

    def test_full_anchor_outside_core_real_w32_no_erroneous_anchor_deletion(self):
        f,g=complete_maps(1,3)
        polynomial=original_flag_triple_cubic(1,f,g)
        witness=None
        for key,(path,owners,anchors) in polynomial["witnesses"].items():
            support,good,mask=key
            if good and any(i not in support for i in anchors):
                witness=(support,good,mask,anchors)
                break
        self.assertIsNotNone(witness,"actual FULL anchor outside three selected owners needed")
        support,good,mask,anchors=witness
        self.assertTrue(any(i not in support for i in anchors))
        expected=evaluate_original_cubic(polynomial,support)
        physical=independent_physical_core_histogram(1,f,g,support)
        self.assertEqual(expected,physical["histogram"])
        self.assertGreaterEqual(expected[True,mask],1)
        self.assertGreater(physical["outside_core_anchors"][True,mask],0)

    def test_true_W34_real_original_sixteen_flag_k44_and_independently_sourced_cores(self):
        f,g,ids=planted_original_k44()
        polynomial=original_flag_triple_cubic(2,f,g,ids)
        self.assertEqual(polynomial["paired_edges_in_universe"],32)
        subsets=(ids,(),ids[:8],ids[8:],ids[::2],ids[1::2],
                 tuple(i for j,i in enumerate(ids) if j%3==0))
        for core in subsets:
            with self.subTest(n=len(core)):
                expected=evaluate_original_cubic(polynomial,core)
                observed=independent_physical_core_histogram(2,f,g,core)
                self.assertEqual(expected,observed["histogram"])
                self.assertEqual(observed["paired_physical_edges"],2*len(core))
        audit=audit_original_four_blocker_cubic(2,f,g,ids,ids)
        self.assertTrue(audit["full_source_projections_independently_recomputed"])

    def test_reversal_involution_and_no_core_requirement_for_anchors(self):
        f,g=complete_maps(1,1)
        polynomial=original_flag_triple_cubic(1,f,g)
        full=evaluate_original_cubic(polynomial,polynomial["universe"])
        # The source triple mask transforms 0<->1, 2<->3 on path reversal.
        def reverse_mask(m):
            return ((m&1)<<1)|((m&2)>>1)|((m&4)<<1)|((m&8)>>1)
        for good in (False,True):
            for mask in range(16):
                self.assertEqual(full[good,mask],full[good,reverse_mask(mask)])
            for j,k in ((0,1),(2,3)):
                lhs=sum(n for (gg,mask),n in full.items() if gg==good and mask&(1<<j))
                rhs=sum(n for (gg,mask),n in full.items() if gg==good and mask&(1<<k))
                self.assertEqual(lhs,rhs)

    def test_fail_closed_source_corruption_and_empty_core(self):
        f,g=complete_maps(1)
        empty=original_flag_triple_cubic(1,f,g,())
        self.assertEqual(empty["coefficients"],Counter())
        self.assertEqual(independent_physical_core_histogram(1,f,g,())["histogram"],
                         Counter())
        self.assertRaises(ValueError,original_flag_triple_cubic,3,f,g)
        self.assertRaises(ValueError,original_flag_triple_cubic,1,f[:-1],g)
        self.assertRaises(ValueError,original_flag_triple_cubic,1,(f[0],)*len(f),g)
        self.assertRaises(ValueError,original_flag_triple_cubic,1,f,g,(0,0))
        self.assertRaises(ValueError,original_flag_triple_cubic,1,f,g,(True,))
        self.assertRaises(ValueError,evaluate_original_cubic,empty,(0,))
        self.assertRaises(ValueError,minimal_alphabet,0)


if __name__=="__main__":
    unittest.main()
