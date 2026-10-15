"""Independent true ORIGINAL W32 fixed-f full D6 second-moment regressions."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations
from math import comb,perm

from hyp105_issue230_d6aa4vcyc_full_moment import (
    normalize_original_LINE_C6,
    actual_original_line_C6_multiplicities,
    exact_13327_relative_original_LINE_gluing_weight_table,
    _encode_partial_source_LINE_gluing,
    _engine_payload,
    direct_grouped_true_original_D6_for_one_complete_g,
    FULL_ORIGINAL_ORDERED_PAIRS,TRUE_ORIGINAL_Q,PHYSICAL_K6_DENOMINATOR,
)
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    exact_two_D6_gluing_kernel,
    canonical_two_source_C6_gluing,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


class ExactTrueOriginalD6FullSecondMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table,cls.meta=exact_13327_relative_original_LINE_gluing_weight_table()

    def test_001_exact_13327_relative_source_line_gluing_diagrams(self):
        self.assertEqual(sum(x>=0 for x in self.table),13327)
        self.assertEqual(len(self.table),7**6)
        self.assertEqual(self.meta[
            "number_valid_original_LINE_relative_partial_gluing_diagrams"],13327)
        self.assertEqual(self.meta["nonisomorphic_original_LINE_C6_pair_gluing_types"],125)
        self.assertEqual(self.meta["relative_partial_source_LINE_gluings_by_shared_factor_count"],
                         {r:comb(6,r)*perm(6,r) for r in range(7)})
        self.assertEqual(PHYSICAL_K6_DENOMINATOR,217945728000)
        self.assertEqual(FULL_ORIGINAL_ORDERED_PAIRS,448846596)

    def test_002_independent_ORIGINAL_line_C6_dihedral_normalization(self):
        C=(10,2,14,7,3,5)
        expected=normalize_original_LINE_C6(C)
        self.assertEqual(expected[0],2)
        for direction in (1,-1):
            for off in range(6):
                rotated=tuple(C[(off+direction*j)%6] for j in range(6))
                self.assertEqual(normalize_original_LINE_C6(rotated),expected)
        with self.assertRaises(ValueError):
            normalize_original_LINE_C6((0,0,1,2,3,4))
        with self.assertRaises(ValueError):
            normalize_original_LINE_C6((0,1,2))

    def test_003_source_LINE_gluing_lookup_vs_independent_all_h_kernel(self):
        cases=((6,6,6,6,6,6),(0,6,3,6,6,6),
               (0,2,6,6,6,6),(0,1,2,3,4,5),
               (0,1,2,3,5,4),(0,6,6,6,6,6))
        for indices in cases:
            key=_encode_partial_source_LINE_gluing(indices)
            gluing=tuple(indices[j] if indices[j]!=6 else 6+
                         sum(indices[k]==6 for k in range(j))
                         for j in range(6))
            original=exact_two_D6_gluing_kernel(2,tuple(range(6)),gluing)
            probability=Fraction(self.table[key],PHYSICAL_K6_DENOMINATOR)
            self.assertEqual(probability,Fraction(
                original["joint_probability_one_complete_GLOBAL_g"]))
        # Strict zero and positive with SAME original two shared LINE factors.
        self.assertEqual(self.table[_encode_partial_source_LINE_gluing((0,2,6,6,6,6))],0)
        self.assertGreater(self.table[_encode_partial_source_LINE_gluing((0,6,3,6,6,6))],0)

    def test_004_complete_TRUE_original_W32_line_cycle_C6_event_multiplicities(self):
        for name in ("S68","S72"):
            model,rows,count,anchor,anchor_event=actual_original_line_C6_multiplicities(name)
            self.assertEqual(len(rows),TRUE_ORIGINAL_Q)
            self.assertEqual(sum(count.values()),TRUE_ORIGINAL_Q)
            self.assertEqual(len(count),17811)
            self.assertIn(anchor_event,count)
            self.assertTrue(all(len(x)==6 and len(set(x))==6 and multiplicity>=1
                                for x,multiplicity in count.items()))
            self.assertEqual(model["s"],2)
            payload=_engine_payload(count,anchor_event,self.table)
            head=payload.splitlines()
            self.assertEqual(len(head),1+len(count)+7**6)
            n,index=map(int,head[0].split())
            self.assertEqual(n,len(count))
            self.assertTrue(0<=index<len(count))

    def test_005_independent_complete_g_historical_original_D6_event_equality(self):
        for scheme in ("S68","S72"):
            model,rows,count,anchor,anchor_event=actual_original_line_C6_multiplicities(scheme)
            for other in ("S68","S72"):
                g=fixture(1,other)["right_labels"]
                direct=direct_grouped_true_original_D6_for_one_complete_g(count,g)
                reference=seven_census({**model,"right_labels":tuple(g)},
                                       independent_checks=False)
                self.assertEqual(direct,reference["seven_class_motif_counts"]["D6"])
            with self.assertRaises(ValueError):
                direct_grouped_true_original_D6_for_one_complete_g(count,
                    tuple(model["right_labels"][:-1])+tuple(model["right_labels"][:1]))


if __name__=="__main__":
    unittest.main()
