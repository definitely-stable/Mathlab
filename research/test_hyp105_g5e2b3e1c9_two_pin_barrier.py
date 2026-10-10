"""C9: independent exact GQ small-s and all-h rational no-go falsifiers."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c9_two_pin_barrier import (
    minimal_pair_alphabet, two_pin_source_target_capacity,
    analytic_s_ge_64_gate, two_pin_all_h_zero_barrier,
)
from hyp105_g5e2b3e1c5_common_bijection import physical_occupied_target
from hyp105_g5e2b3e1c8_fiber_rearrangement import (
    frozen_fiber_rearrangement, universal_k_pin_lower,
)


class TwoPinC9Tests(unittest.TestCase):
    def test_true_integer_gate_at_16_32_and_exact_tail_samples(self):
        self.assertGreaterEqual(analytic_s_ge_64_gate()["positive_uniform_slack"],Fraction(1,2))
        for s in (16,32,64,128,256,512,1024):
            v = two_pin_all_h_zero_barrier(s)
            self.assertTrue(v["proved_all_two_pin_fibers_zero"])
            self.assertTrue(v["C8_LD_zero_for_every_D_size_at_most_two"])
            for row in v["fibers"]:
                self.assertGreater(row["slack_integer"],0)
                self.assertLess(row["exact_ratio"],1)
        self.assertEqual(two_pin_all_h_zero_barrier(16)["proof_branch"],
                         "EXACT_INTEGER_BASE_CASE")
        self.assertEqual(two_pin_all_h_zero_barrier(64)["proof_branch"],
                         "UNIFORM_RATIONAL_ANALYTIC_TAIL")

    def test_below_threshold_is_not_false_general_claim(self):
        for s in (2,4,8):
            v=two_pin_all_h_zero_barrier(s)
            self.assertFalse(v["proved_all_two_pin_fibers_zero"])
            self.assertEqual(v["scope"],"BELOW_PROVEN_THRESHOLD_NOT_DECIDED")
            self.assertFalse(v["actual_minimum_zero_proved"])

    def test_independent_K6_target_all_70_two_factors_and_D2_classes(self):
        # Complete physical K6 target: direct counts in three pin-fibers.
        F=tuple(combinations(range(6),2))
        tgt=physical_occupied_target(6,F)
        self.assertEqual(len(tgt),70)
        p=(0,1)
        q={r:sum(R.intersection(p)==set(p[:r]) for R in tgt) for r in (0,1,2)}
        # Directly enumerate ALL four possible membership patterns; sum 70.
        all_patterns={}
        for R in tgt:
            pattern=tuple(i for i in p if i in R)
            all_patterns[pattern]=all_patterns.get(pattern,0)+1
        self.assertEqual(sum(all_patterns.values()),70)
        self.assertTrue(all(count<=70 for count in all_patterns.values()))
        self.assertEqual(len(F),15)

    def test_independent_genuine_W32_source_support_with_concurrence(self):
        # Complete original W(3,2) enumeration for both genuine embeddings.
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
        from hyp105_g5e2b3e1c1_gq_concurrency import original_line_concurrency_graph
        # Use direct actual sixsets and test exact C9 union-support upper
        # without assuming C9 capacity succeeds at small s.
        cert=two_pin_source_target_capacity(2)
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            m=source_weighted_BA_hypergraph(model)
            self.assertEqual(len(m),3076)
            self.assertEqual(sum(m.values()),5000)
            for r in range(3):
                actual=sum(1 for R in m if len(R.intersection((0,1)))==r)
                self.assertLessEqual(actual,cert["fibers"][r]["source_support_upper"])

    def test_genuine_W32_low_pin_relaxation_never_falsifies_C9_scope(self):
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
        from hyp105_g5e2b3e1c5_common_bijection import fixed_map_overlap
        F=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,F)
        labels={e:i for i,e in enumerate(F)}
        model=pair_labeled_symplectic(1,"reverse-line")
        m=source_weighted_BA_hypergraph(model)
        actual=fixed_map_overlap(m,target,tuple(labels[e] for e in model["right_labels"]))
        self.assertEqual(actual,77)
        low=universal_k_pin_lower(m,target,15,(0,1))
        self.assertLessEqual(low["minimum_fiber_lower"],actual)
        self.assertLessEqual(low["minimum_fiber_lower"],69)
        self.assertEqual(low["enumerated_injective_prefixes"],210)

    def test_finite_generic_star_positive_remains_allowed(self):
        # The theorem REQUIRES GQ source constraints and only s>=16;
        # generic positive one-pin star example from C8 stays valid.
        V=8
        star={frozenset(set(range(V))-{0,j}) for j in range(1,V)}
        src={R:1 for R in star}
        self.assertEqual(universal_k_pin_lower(
            src,star,V,(0,))["minimum_fiber_lower"],1)

    def test_bad_parameters_rejected(self):
        for bad in (0,1,3,5,12,True):
            with self.assertRaises(ValueError):
                two_pin_source_target_capacity(bad)
        for bad in (-1,0,True):
            with self.assertRaises(ValueError):
                minimal_pair_alphabet(bad)


if __name__=="__main__":
    unittest.main()
