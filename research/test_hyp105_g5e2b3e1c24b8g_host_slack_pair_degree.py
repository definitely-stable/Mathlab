"""Independent K4 full-global-injection falsifiers for C24-B8-G all-h bound."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import unittest

from hyp105_g5e2b3e1c24b8g_host_slack_pair_degree import (
    minimal_host_capacity, certified_pair_degree_lower,
    evaluate_global_projection,residual_separation_gate,
)


def weights(n):
    return {(i,j):Fraction(((7*i+11*j)%17)-8,3)
            for i,j in combinations(range(n),2)}


def brute_injection(a,n,coeff):
    edges=tuple(combinations(range(a),2))
    p=Fraction(4,a+1)
    return min(sum((v*(int(bool(set(mapping[i])&set(mapping[j])))-p)
                    for (i,j),v in coeff.items()),Fraction(0))
               for mapping in permutations(edges,n))


class HostSlackPairDegreeTests(unittest.TestCase):
    def test_all_global_k4_injections_signed_pair_lower(self):
        a=4
        for n in (4,5,6):
            coeff=weights(n)
            cert=certified_pair_degree_lower(coeff,a,n)
            exact=brute_injection(a,n,coeff)
            self.assertLessEqual(cert["certified_global_projection_lower"],exact)
            self.assertLessEqual(cert["unshifted_row_lower"],
                                 cert["certified_global_projection_lower"])
            self.assertTrue(cert["complete_piecewise_linear_dual_scan"])
            self.assertTrue(cert["no_claim_global_quadratic_assignment_optimality"])
            self.assertEqual(cert["host"]["unused_physical_edges"],6-n)
            self.assertEqual(cert["projected_pair_feature_count"],comb(n,2))
            first=tuple(combinations(range(a),2))[:n]
            evaluated=evaluate_global_projection(coeff,first,a)
            self.assertLessEqual(cert["certified_global_projection_lower"],
                                 evaluated["centered_projection"])
            self.assertEqual(sum(evaluated["occupied_row_degrees"]),
                             2*evaluated["occupied_adjacency_count"])

    def test_deleted_physical_edge_exact_adjacency_extrema(self):
        # Independent enumeration of deleted host subgraphs, not algebra from module.
        for a in (4,5,6):
            host=tuple(combinations(range(a),2))
            m=len(host)
            for q in range(min(a-2,m-4)+1):
                n=m-q
                par=minimal_host_capacity(a,n)
                observed=[]
                for omitted in combinations(host,q):
                    used=set(host)-set(omitted)
                    observed.append(sum(bool(set(e)&set(h))
                                        for e,h in combinations(used,2)))
                self.assertEqual(min(observed),
                                 par["occupied_adjacency_total_min"])
                self.assertEqual(max(observed),
                                 par["occupied_adjacency_total_max"])
                self.assertLessEqual(par["occupied_row_degree_min"],
                                     par["occupied_row_degree_max"])

    def test_global_adjacency_dual_recovers_sharp_unweighted_extrema(self):
        a=4
        for n in (4,5,6):
            par=minimal_host_capacity(a,n)
            for sign in (1,-1):
                coeff={pair:Fraction(sign)
                       for pair in combinations(range(n),2)}
                cert=certified_pair_degree_lower(coeff,a,n)
                p=Fraction(4,a+1)
                exact=(par["occupied_adjacency_total_min"] if sign==1
                       else -par["occupied_adjacency_total_max"])
                exact-=sign*p*comb(n,2)
                self.assertEqual(cert["certified_global_projection_lower"],exact)

    def test_fixed_breakpoint_budget_remains_certified_not_optimal(self):
        coeff=weights(5)
        narrow=certified_pair_degree_lower(coeff,4,5,
                                           max_exact_candidates=1)
        full=certified_pair_degree_lower(coeff,4,5)
        self.assertFalse(narrow["complete_piecewise_linear_dual_scan"])
        self.assertLessEqual(narrow["certified_global_projection_lower"],
                             full["certified_global_projection_lower"])
        self.assertLessEqual(narrow["certified_global_projection_lower"],
                             brute_injection(4,5,coeff))
        self.assertTrue(full["complete_piecewise_linear_dual_scan"])

    def test_residual_logic_falsifies_only_separated_bound(self):
        gate=residual_separation_gate(Fraction(870476,5005),
                                      Fraction(-558274,3003),
                                      Fraction(73373,8580))
        self.assertTrue(gate["separated_positive_gate_ruled_out_by_witness"])
        self.assertEqual(gate["required_projection_lower_improvement_strictly_more_than"],
                         Fraction(9817,2860))
        self.assertTrue(gate["not_a_minimum_S_or_residual_estimate"])

    def test_reject_noncanonical_and_nonminimal_hosts(self):
        with self.assertRaises(ValueError):
            minimal_host_capacity(6,14) # K6 is not minimal for 14
        with self.assertRaises(ValueError):
            minimal_host_capacity(5,11)
        with self.assertRaises(ValueError):
            minimal_host_capacity(4,3)
        with self.assertRaises(ValueError):
            certified_pair_degree_lower({},4,5)
        with self.assertRaises(ValueError):
            certified_pair_degree_lower(weights(5),4,5,max_exact_candidates=0)
        with self.assertRaises(ValueError):
            evaluate_global_projection(weights(5),((0,1),)*5,4)
        with self.assertRaises(ValueError):
            residual_separation_gate(0.25,0,0)


if __name__=="__main__":
    unittest.main()
