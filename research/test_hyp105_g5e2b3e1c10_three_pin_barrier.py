"""C10: exact three-pin all-h method-barrier and real W32 falsifiers."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c10_three_pin_barrier import (
    three_pin_capacity_certificate,
    analytic_s_ge_64_three_pin_gate,
    all_h_three_pin_zero_barrier,
)
from hyp105_g5e2b3e1c9_two_pin_barrier import (
    two_pin_all_h_zero_barrier,
)
from hyp105_g5e2b3e1c8_fiber_rearrangement import frozen_fiber_rearrangement
from hyp105_g5e2b3e1c5_common_bijection import physical_occupied_target


class ThreePinC10Tests(unittest.TestCase):
    def test_exact_s16_s32_and_uniform_tail(self):
        a=analytic_s_ge_64_three_pin_gate()
        self.assertTrue(a["uniform_all_s_ge_64"])
        self.assertGreater(a["tail_positive_slack"],Fraction(1,2))
        for s in (16,32,64,128,256,512,1024):
            d=all_h_three_pin_zero_barrier(s)
            self.assertTrue(d["three_pin_zero_proved"])
            self.assertTrue(d["zero_for_every_D_with_cardinality_at_most_3"])
            self.assertEqual(len(d["classes"]),4)
            for cls in d["classes"]:
                self.assertGreater(cls["strict_zero_cell_slack"],0)
                self.assertLess(cls["support_plus_target_ratio"],1)
            old=two_pin_all_h_zero_barrier(s)
            self.assertTrue(old["proved_all_two_pin_fibers_zero"])

    def test_below_threshold_not_promoted(self):
        for s in (2,4,8):
            d=all_h_three_pin_zero_barrier(s)
            self.assertFalse(d["three_pin_zero_proved"])
            self.assertFalse(d["actual_zero_overlap_map_proved"])
            self.assertEqual(d["proof_scope"],"BELOW_PROVEN_THRESHOLD_NOT_DECIDED")

    def test_witness_cap_contains_one_fixed_third_right_line(self):
        # Independently enumerate a genuine W(3,2) incidence witness census:
        # source multiplicity of all R containing a candidate pinned triple
        # whose doubled point pair belongs to the pinned triple. The test
        # uses a more conservative source marginal (ALL motives with pins);
        # only the mathematically universal support bounds can constrain it.
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
        V=15
        cap=three_pin_capacity_certificate(2)
        for kind in ("lex","reverse-line"):
            src=source_weighted_BA_hypergraph(pair_labeled_symplectic(1,kind))
            self.assertEqual(len(src),3076)
            self.assertEqual(sum(src.values()),5000)
            for D in ((0,1,2),(0,3,7),(4,9,14)):
                for r in range(4):
                    n=sum(1 for R in src if len(R.intersection(D))==r)
                    self.assertLessEqual(n,cap["classes"][r]["source_nonpinned_concurrence_support_upper"]
                                             +cap["classes"][r]["source_pinned_witness_support_upper"])

    def test_full_physical_target_degree_exact(self):
        # Independent direct enumeration of the occupied K6 target 2factors.
        F=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,F)
        self.assertEqual(len(target),70)
        expected=three_pin_capacity_certificate(2)
        self.assertEqual(expected["physical_full_target_sixsets"],70)
        self.assertEqual(expected["physical_target_degree_one"],28)
        for idx in range(len(F)):
            self.assertEqual(sum(idx in R for R in target),28)

    def test_actual_W32_three_pins_can_be_reported_but_no_all_h_claim(self):
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
        from hyp105_g5e2b3e1c5_common_bijection import fixed_map_overlap
        F=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,F)
        model=pair_labeled_symplectic(1,"reverse-line")
        src=source_weighted_BA_hypergraph(model)
        lookup={e:i for i,e in enumerate(F)}
        pi=tuple(lookup[e] for e in model["right_labels"])
        actual=fixed_map_overlap(src,target,pi)
        self.assertEqual(actual,77)
        D=(0,1,2)
        for images in ((pi[0],pi[1],pi[2]),(0,1,2),(12,13,14)):
            lb=frozen_fiber_rearrangement(src,target,15,D,images)
            self.assertGreaterEqual(lb,0)
            if images==(pi[0],pi[1],pi[2]):
                self.assertLessEqual(lb,actual)
        self.assertFalse(all_h_three_pin_zero_barrier(2)["three_pin_zero_proved"])

    def test_bad_parameters_rejected(self):
        for bad in (0,1,3,5,12,True):
            with self.assertRaises(ValueError):
                three_pin_capacity_certificate(bad)


if __name__=="__main__":
    unittest.main()
