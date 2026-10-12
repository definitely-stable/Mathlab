"""Independent exact prefix-injection conditional-expectation and B/A tests."""
from fractions import Fraction
from itertools import combinations,permutations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph,random_injection_expectation,
)
from hyp105_g5e2b3e1k3g2k_conditional_injection import (
    SixSourceConditionalExpectation,_W32_oracle,hosted_W32_pair,
)


def independent_bruteforce(oracle,prefix):
    k=len(prefix)
    remaining=tuple(i for i in range(oracle.K) if i not in prefix)
    targets=set(oracle.target_masks)
    total=0
    n=0
    for suffix in permutations(remaining,oracle.V-k):
        assignment=tuple(prefix)+suffix
        score=0
        for R,w in oracle.weights:
            T=sum(1<<assignment[i] for i in range(oracle.V)
                  if R & (1<<i))
            score+=w*(T in targets)
        total+=score
        n+=1
    return Fraction(total,n)


class K3G2KConditionalInjectionTests(unittest.TestCase):
    def test_synthetic_all_prefixes_equal_independent_bruteforce(self):
        weights={
            frozenset(range(6)):2,
            frozenset(range(1,7)):3,
            frozenset((0,1,2,4,5,6)):1
        }
        targets=(frozenset(range(6)),
                 frozenset(range(1,7)),
                 frozenset((0,1,2,3,5,6)))
        oracle=SixSourceConditionalExpectation(7,7,weights,targets)
        for prefix in ((),(0,),(1,),(0,4),(5,2,6),
                       (6,5,4,3,2,1),(0,1,2,3,4,5,6)):
            with self.subTest(prefix=prefix):
                self.assertEqual(
                    oracle.expectation(prefix),
                    independent_bruteforce(oracle,prefix))
        for mode in ("maximize","minimize"):
            result=oracle.construct(mode)
            self.assertEqual(len(set(result["pair_ids"])),7)
            self.assertEqual(
                result["actual_overlap"],oracle.full_overlap(result["pair_ids"]))
            self.assertEqual(result["trajectory"][-1]["conditional_after"],
                             [result["actual_overlap"],1])
        mx=oracle.construct("maximize")["actual_overlap"]
        mn=oracle.construct("minimize")["actual_overlap"]
        self.assertLessEqual(mn,oracle.uniform_expectation())
        self.assertLessEqual(oracle.uniform_expectation(),mx)

    def test_outside_source_used_labels_are_forbidden(self):
        # Source sixset R excludes original endpoint 0. Mapping endpoint 0
        # to physical 0 forbids a target containing physical 0.
        weights={frozenset((1,2,3,4,5,6)):1}
        targets=[frozenset((0,1,2,3,4,5))]
        oracle=SixSourceConditionalExpectation(7,7,weights,targets)
        self.assertEqual(oracle.uniform_expectation(),Fraction(1,7))
        self.assertEqual(oracle.expectation((0,)),0)
        self.assertEqual(oracle.expectation((6,)),1)
        self.assertEqual(oracle.expectation((0,3)),0)

    def test_complete_genuine_W32_weighted_BA_and_full_B0(self):
        model=gq_pair_model(1,"lex")
        weights,physical,targets,oracle=_W32_oracle(model)
        self.assertEqual(len(physical),15)
        self.assertEqual(len(targets),70)
        self.assertEqual(
            oracle.uniform_expectation(),
            random_injection_expectation(weights,a=6,original_vertices=15))
        self.assertEqual(sum(weights.values()),
                         sum(w for _,w in oracle.weights))
        cert=hosted_W32_pair(left_variant="lex")
        mean=Fraction(*cert["random_mean"])
        upper=cert["results"]["maximize"]
        lower=cert["results"]["minimize"]
        self.assertGreaterEqual(upper["actual_overlap"],mean)
        self.assertLessEqual(lower["actual_overlap"],mean)
        for row in (upper,lower):
            self.assertEqual(row["actual_overlap"],
                             row["actual_BA_full_B0_independent"])
            self.assertEqual(row["physical_label_capacity"],15)
            self.assertEqual(row["source_vertices"],15)
            self.assertEqual(len(row["pair_ids"]),15)
            self.assertEqual(len(set(row["pair_ids"])),15)
            self.assertGreaterEqual(
                row["seven_GF5_risk_floor_numerator"],
                row["BA_GF5_risk_floor_numerator"])
            self.assertFalse(row["all_f_g_positive_lower_bound_proved"])

    def test_fail_closed_inputs_and_injective_completion(self):
        for args in ((5,6,{},[]),(7,6,{},[]),
                     (True,7,{},[]),(7,True,{},[])):
            with self.assertRaises(ValueError):
                SixSourceConditionalExpectation(*args)
        with self.assertRaises(ValueError):
            SixSourceConditionalExpectation(7,7,
                {frozenset((0,1,2,3,4,8)):1},[])
        with self.assertRaises(ValueError):
            SixSourceConditionalExpectation(7,7,
                {frozenset(range(6)):-1},[])
        with self.assertRaises(ValueError):
            SixSourceConditionalExpectation(7,7,{},
                [frozenset((0,1,2,3,4,8))])
        oracle=SixSourceConditionalExpectation(7,7,{},[])
        for prefix in ((0,0),(8,),(-1,),(0,True),tuple(range(8))):
            with self.assertRaises(ValueError):
                oracle.expectation(prefix)
        for mode in ("unrestricted","max","MIN"):
            with self.assertRaises(ValueError):
                oracle.construct(mode)
        with self.assertRaises(ValueError):
            hosted_W32_pair(left_variant="unknown")


if __name__=="__main__":
    unittest.main()
