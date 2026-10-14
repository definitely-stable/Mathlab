"""AA4-D independent source partition and exact mixed global injection tests."""
import unittest
from collections import Counter
from itertools import combinations
from math import factorial

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4c_edit_transversal import (
    genuine_original_positive_hypergraph, incidence_cover_bits,
    survivor_certificate)
from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
    finite_source_support_partition,block_legal_completions,
    coherent_mixed_transversal_census)
from hyp105_g5e2b3e1b0_seven_signature import seven_census


class GlobalTwoTypeW32FiberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        model=fixture(1,"S68")
        source=genuine_original_positive_hypergraph(model)
        cls.model=model
        cls.source=source
        cls.bits,cls.weights,cls.allmask=incidence_cover_bits(source["records"])
        cls.partition=finite_source_support_partition(
            cls.bits,cls.weights,cls.allmask)

    def test_all_27405_typed_four_source_sets_partition_exhaustive(self):
        p=self.partition
        self.assertEqual(p["source_blocks_checked"],27405)
        self.assertEqual(p["number_transversal_blocks"],53)
        self.assertEqual(p["nontransversal_blocks"],27405-53)
        self.assertEqual(sum(p["all_blocks_by_number_original_point_factors"].values()),27405)
        self.assertEqual(
            {k:p["all_blocks_by_number_original_point_factors"][k] for k in range(5)},
            {k:__import__("math").comb(15,k)*__import__("math").comb(15,4-k)
             for k in range(5)})
        self.assertGreaterEqual(p["minimum_unchanged_old_S_on_nontransversal_blocks"],1)
        self.assertTrue(all(len(b)==4 and len(set(b))==4 for b in
                            p["transversal_original_factor_blocks"]))
        for b in p["transversal_original_factor_blocks"]:
            s,y,_=survivor_certificate(self.bits,self.weights,self.allmask,b)
            self.assertEqual((s,y),(0,0))
        # A nontransversal definitely retains exact ORIGINAL old positives.
        example=p["example_nontransversal_worst_support"]
        self.assertGreater(
            survivor_certificate(self.bits,self.weights,self.allmask,example)[0],0)

    def test_genuine_two_type_w32_block_completions_exhaustive(self):
        L=tuple(self.model["left_labels"])
        R=tuple(self.model["right_labels"])
        # Unlike the previous one-sided AA4B, include BOTH typed injections.
        examples=[]
        blocks=self.partition["transversal_original_factor_blocks"]
        for point_count in (0,1,2,3,4):
            found=next((b for b in blocks if sum(i<15 for i in b)==point_count),None)
            if found is not None:
                examples.append(found)
        self.assertTrue(examples)
        for b in examples:
            nP=sum(i<15 for i in b)
            completions=tuple(block_legal_completions(L,R,b))
            self.assertEqual(len(completions),
                             factorial(nP)*factorial(4-nP))
            self.assertEqual(completions[0],(L,R))
            self.assertEqual(len(set(completions)),len(completions))
            for A,B in completions:
                self.assertEqual(set(A),set(L))
                self.assertEqual(set(B),set(R))
                self.assertEqual(len(set(A)),15)
                self.assertEqual(len(set(B)),15)
                self.assertTrue(all(A[i]==L[i] for i in range(15) if i not in b))
                self.assertTrue(all(B[i]==R[i] for i in range(15) if i+15 not in b))
        with self.assertRaises(ValueError):
            tuple(block_legal_completions(L,R,(0,0,15,16)))
        with self.assertRaises(ValueError):
            tuple(block_legal_completions(L,R,(0,1,2,30)))

    def test_genuine_mixed_true_original_exact_census_and_source_ledger(self):
        blocks=self.partition["transversal_original_factor_blocks"]
        block=next(b for b in blocks if sum(i<15 for i in b)==2)
        full=coherent_mixed_transversal_census(self.model,(block,),expected_blocks=1)
        self.assertEqual(full["original_source_transversal_blocks"],1)
        self.assertEqual(full["globally_injective_two_typed_completions_checked"],4)
        self.assertEqual(sum(c["zero_S_completions"] for c in full["all_block_minima"]),full["zero_S_completions"])
        self.assertEqual(full["baseline"],(68,3112510))
        self.assertGreaterEqual(full["minimum_S_in_all_transversal_fibers"],0)
        self.assertEqual(len(full["independent_full_original_classification_checks"]),2)
        self.assertEqual(sum(v["completions"] for v in full["by_point_factor_split"].values()),4)
        independent=seven_census(self.model,independent_checks=False)
        self.assertEqual(independent["S_seven"],68)
        self.assertEqual(independent["GF5_seven_lower_numerator"],3112510)

    def test_fail_closed_source_budget(self):
        with self.assertRaises(ValueError):
            finite_source_support_partition((),(),0)
        with self.assertRaises(AssertionError):
            coherent_mixed_transversal_census(self.model,(),expected_blocks=1)
        with self.assertRaises(ValueError):
            tuple(block_legal_completions(self.model["left_labels"],self.model["right_labels"],(0,)))


if __name__=="__main__":
    unittest.main()
