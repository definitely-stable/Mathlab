"""D6-W independent exact dual, marginal hierarchy and true ORIGINAL W32."""
import unittest
from fractions import Fraction
from itertools import permutations, product
from collections import Counter

from hyp105_issue230_d6w_overlap_separator_marginal_dual import (
    verified_separator_reparam_dual,check_local_marginal_consistency,
    saturated_triple_anchor_certificate,frozen_true_original_W32_report,
    _separator_domain,
)
from hyp105_issue230_d6t_assignment_dual_certificate import (
    complete_true_original_W32_three_factor_tables,
    local_factor_objective,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def parity(p):
    return sum(p[i]>p[j] for i in range(len(p))
               for j in range(i+1,len(p)))%2


def independent_sixstate_exact_min(factors):
    return min(sum(f["costs"][((),tuple(p[t] for t in f["R"]))]
                   for f in factors)
               for p in permutations(range(3)))


def parity_factors():
    all_perm=list(permutations(range(3)))
    return [{"L":(),"R":(0,1,2),
             "costs":{((),p):int(parity(p)==flag) for p in all_perm}}
            for flag in (0,1)]


class D6WSeparatorMarginalTests(unittest.TestCase):
    def test_exact_one_site_pseudomarginals_fail_pair_test_parity(self):
        factors=parity_factors()
        dists=[]
        for flag in (0,1):
            # Local zero-cost support chooses parity OPPOSITE to flag.
            dists.append({row:Fraction(1,3) if cost==0 else Fraction(0)
                          for row,cost in factors[flag]["costs"].items()})
        one=check_local_marginal_consistency(
            factors,0,0,3,3,dists,rank=1)
        two=check_local_marginal_consistency(
            factors,0,0,3,3,dists,rank=2)
        self.assertTrue(one["consistent"])
        self.assertEqual(one["objective_expectation"],"0")
        self.assertFalse(two["consistent"])
        self.assertEqual(independent_sixstate_exact_min(factors),1)
        # Independent, all-six permutations: uniform distribution is 2-wise consistent.
        uniform=[{row:Fraction(1,6) for row in f["costs"]} for f in factors]
        self.assertTrue(check_local_marginal_consistency(
            factors,0,0,3,3,uniform,rank=2)["consistent"])

    def test_exact_separator_dual_closes_parity_gap(self):
        f=parity_factors()
        dual,msg,aug=saturated_triple_anchor_certificate(f)
        self.assertEqual(dual["exact_integer_lower"],1)
        self.assertEqual(dual["exact_six_permutation_primal_min"],1)
        self.assertEqual(dual["shifted_factor_minima"],[0,0,1])
        self.assertEqual(dual["separator_rank"],2)
        self.assertTrue(dual["all_separators_cancel_identically"])
        self.assertEqual(len(msg),4)
        self.assertFalse(dual["general_rank_two_Sherali_Adams_exactness_claim"])

    def test_mixed_typed_point_line_overlap_transfer(self):
        # Two factors depend jointly on SAME ORIGINAL point and line site.
        # Opposite costs sum to one under every globally injective pair.
        a={"L":(0,),"R":(0,),
           "costs":{((l,),(r,)):int(l==r)
                    for l,r in product(range(2),repeat=2)}}
        b={"L":(0,),"R":(0,),
           "costs":{((l,),(r,)):int(l!=r)
                    for l,r in product(range(2),repeat=2)}}
        S=(("L",0),("R",0))
        vals={(l,r):int(l==r) for l,r in product(range(2),repeat=2)}
        dual=verified_separator_reparam_dual([a,b],1,2,1,2,[
            {"factor":0,"separator":S,
             "values":{row:-cost for row,cost in vals.items()}},
            {"factor":1,"separator":S,"values":vals},
        ])
        self.assertEqual(dual["exact_integer_lower"],1)
        self.assertEqual(dual["shifted_factor_minima"],[0,1])
        self.assertEqual(dual["separator_rank"],2)

    def test_fail_closed_on_malformed_dual_and_probabilities(self):
        factors=parity_factors()
        _,messages,aug=saturated_triple_anchor_certificate(factors)
        def solve(msg):
            return verified_separator_reparam_dual(
                aug,0,0,3,3,msg,max_separator_size=2)
        self.assertEqual(solve(messages)["exact_integer_lower"],1)
        with self.assertRaisesRegex(ValueError,"cancellation"):
            solve(messages[:-1])
        malformed=[dict(m) for m in messages]
        malformed[0]["values"]=dict(malformed[0]["values"])
        malformed[0]["values"].pop(next(iter(malformed[0]["values"])))
        with self.assertRaises(ValueError):
            solve(malformed)
        malformed=[dict(m) for m in messages]
        malformed[0]["values"]=dict(malformed[0]["values"])
        k=next(iter(malformed[0]["values"]))
        malformed[0]["values"][k]=True
        with self.assertRaises(ValueError):
            solve(malformed)
        malformed=[dict(m) for m in messages]
        malformed[0]["separator"]=(("R",0),("R",1),("R",2))
        with self.assertRaises(ValueError):
            solve(malformed)
        malformed=[dict(m) for m in messages]
        malformed[0]["separator"]=(("L",0),)
        with self.assertRaises(ValueError):
            solve(malformed)
        malformed=[dict(m) for m in messages]
        malformed[0]["separator"]=(("R",1),("R",0))
        with self.assertRaises(ValueError):
            solve(malformed)
        malformed=[dict(m) for m in messages]
        malformed[0]["separator"]=(("R",0),("R",0))
        with self.assertRaises(ValueError):
            solve(malformed)
        altered=[{**f,"costs":dict(f["costs"])} for f in factors]
        altered[0]["costs"].pop(next(iter(altered[0]["costs"])))
        with self.assertRaises(ValueError):
            verified_separator_reparam_dual(altered,0,0,3,3,[])
        with self.assertRaises(ValueError):
            check_local_marginal_consistency(factors,0,0,3,3,
                                             [{},{}],rank=1)

    def test_source_ORIGINAL_W32_exact_global_cost_conservation(self):
        # Inspect the exact cost identity at EACH true complete permutation,
        # not merely the min. All three ORIGINAL line IDs are retained at source.
        for scheme,T in (("S68",(3,11,12)),("S72",(1,7,9))):
            model=fixture(1,scheme)
            triple,labels,image,compiled,S,Y=(
                complete_true_original_W32_three_factor_tables(model,T))
            self.assertEqual(compiled["original_left_sixsets"],62370)
            for fs in (S,Y):
                indexed=[{**f,"R":tuple(triple.index(t) for t in f["R"])}
                         for f in fs]
                dual,messages,aug=saturated_triple_anchor_certificate(indexed)
                for p in permutations(range(3)):
                    source=local_factor_objective(fs,triple,p)
                    original=sum(f["costs"][((),tuple(p[t] for t in f["R"]))]
                                 for f in indexed)
                    self.assertEqual(source,original)
                    shifted=0
                    for index,f in enumerate(aug):
                        row=((),tuple(p[t] for t in f["R"]))
                        value=f["costs"][row]
                        for msg in messages:
                            if msg["factor"]!=index:
                                continue
                            arg=tuple(p[orig] for side,orig in msg["separator"])
                            value+=msg["values"][arg]
                        shifted+=value
                    self.assertEqual(shifted,source)
                    self.assertGreaterEqual(shifted,dual["exact_integer_lower"])
                self.assertEqual(dual["exact_integer_lower"],
                                 independent_sixstate_exact_min(indexed))

    def test_original_W32_rank_two_bounds_strictly_improve_D6V_S72(self):
        rows=frozen_true_original_W32_report()
        self.assertEqual(len(rows),2)
        for row in rows:
            self.assertEqual(row["true_original_left_sixsets"],62370)
            self.assertEqual(row["right_permutations_exhaustive"],6)
            for d in row["objectives"].values():
                self.assertEqual(d["global_conditional_exact_primal"],
                                 d["verified_pair_separator_integer_dual"])
                self.assertEqual(d["separator_rank"],2)
                self.assertTrue(d["zero_cost_full_three_site_anchor_explicit"])
                self.assertTrue(d["globally_injective_source_left_and_right"])
                self.assertTrue(d["frozen_left_and_other_twelve_right_originals"])
        vals={
            ("S68","S_seven"):(68,68),
            ("S72","S_seven"):(68,67),
            ("S68","GF5_selected_numerator"):(3112510,3112510),
            ("S72","GF5_selected_numerator"):(3104080,3056200),
        }
        for r in rows:
            for name,z in r["objectives"].items():
                exact,old=vals[r["scheme"],name]
                self.assertEqual(z["verified_pair_separator_integer_dual"],exact)
                self.assertEqual(z["D6V_max_three_factor_cluster_lower"],old)
                self.assertEqual(z["gap_closed_beyond_D6V"],exact-old)


if __name__=="__main__":
    unittest.main()
