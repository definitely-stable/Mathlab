"""Independent all-N selector sixth-moment Young constant and 47/8 tests.

Exact analytical invariant:
  tr A6 <= 12 C6 + 6 Delta tr A4
         <= 24 C6 + 72 m Delta^2.
Use finite COMPLETE enumeration of all 512 bipartite graphs K_{3,3}
as an independent algebraic falsifier; never as substitute for GQ
source incidence. Also test TRUE ORIGINAL W32/W34 paired-coordinate
priority selectors with two physical colors and source provenance.
Test formal T/K caps without assuming external graph SS6 constants.
"""
from fractions import Fraction
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_original_selector_symbolic_ledger import (
    independent_tighter_original_selector_moment_ledger,
    exact_selected_original_bipartite_trace6_lemma,
    canonical_original_selector_symbolic_ledger,
)


def independent_simple_bipartite_3x3_spectral_envelope():
    edges=list((x,y) for x in range(3) for y in range(3,6))
    assert len(edges)==9
    completed=0
    for mask in range(1<<9):
        adj={i:set() for i in range(6)}
        m=0
        for j,(x,y) in enumerate(edges):
            if (mask>>j)&1:
                adj[x].add(y);adj[y].add(x)
                m+=1
        Delta=max(map(len,adj.values()))
        A2={}
        A3={}
        for u in adj:
            row={}
            for v in adj[u]:
                for w in adj[v]:
                    row[w]=row.get(w,0)+1
            A2[u]=row
        for u in adj:
            row={}
            for v,n in A2[u].items():
                for w in adj[v]:
                    row[w]=row.get(w,0)+n
            A3[u]=row
        tr4=sum(n*n for row in A2.values() for n in row.values())
        tr6=sum(n*n for row in A3.values() for n in row.values())
        # Direct rooted oriented SIMPLE sixcycles /12. Not using
        # the same count algorithm as the production physical owner
        # DFS: each ordinary physical cycle has 6*2 root/direction choices.
        n_oriented=sum(
            all(w[(i+1)%6] in adj[w[i]] for i in range(6))
            for w in permutations(range(6)))
        if n_oriented%12:
            raise AssertionError("not simple bipartite oriented C6 count")
        C6=n_oriented//12
        if (tr6>12*C6+6*Delta*tr4
            or tr6>24*C6+72*m*Delta**2
            or tr6>24*C6+144*m*Delta**2):
            raise AssertionError(
                ("independent ALL 512 simple K3,3 bipartite graphs "
                 "falsify proposed analytical selector sixth moment",mask))
        completed+=1
    return completed


class OriginalSelectorIndependentAllNAnalyticLedger(unittest.TestCase):
    def test_all_512_independently_constructed_small_bipartite_graphs(self):
        self.assertEqual(
            independent_simple_bipartite_3x3_spectral_envelope(),512)

    def test_actual_genuine_original_W32_W34_6_source_selector_graphs(self):
        for power,scheme,seed in (
            (1,"lex",0),(1,"lex",1),(1,"reverse-line",0),
            (1,"reverse-line",3),(2,"lex",0),(2,"reverse-line",1)):
            with self.subTest(power=power,scheme=scheme,seed=seed):
                z=exact_selected_original_bipartite_trace6_lemma(
                    power,scheme,seed)
                self.assertTrue(z["actual_trace6_le_24C6_plus_72mDelta2"])
                self.assertTrue(z["actual_trace6_le_12C6_plus_6Delta_trace4"])
                self.assertTrue(z["all_selected_source_physical_edges_bichromatic"])
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertLessEqual(z["selected_source_physical_trace_A6"],
                    24*z["selected_source_physical_C6"]+
                    72*z["selected_source_physical_edges"]*
                    z["selected_source_physical_max_degree"]**2)

    def test_exact_independent_original_K_T_analytic_constants(self):
        for K,T in ((0,1),(2,3),(8,10),(64,2**65),
                    (64,2**65*7**3)):
            with self.subTest(K=K,T=T):
                v=independent_tighter_original_selector_moment_ledger(K,T)
                self.assertEqual(
                    int(v["original_L6_tighter_24plus288T2"]),
                    24+288*T*T)
                self.assertEqual(
                    int(v["original_parent_L6_24plus576T2"]),
                    24+576*T*T)
                self.assertEqual(
                    int(v["exact_original_sigma2_inverse"]),
                    64*(K+1)**2)
                self.assertEqual(
                    int(v["exact_original_sigma3_inverse"]),
                    64*27*(K+1)**3)
                self.assertLessEqual(
                    int(v["original_L4_tighter_SAFE_integer_envelope"]),
                    int(v["original_L4_parent_SAFE_integer_envelope"]))
                self.assertLessEqual(
                    int(v["original_internal_I47over8_tighter_SAFE_integer_envelope"]),
                    int(v["original_internal_I47over8_parent_SAFE_integer_envelope"]))
                self.assertEqual(
                    Fraction(v["original_mixed_source_B_exponent"]),
                    Fraction(23,4))
                self.assertEqual(
                    Fraction(v["original_internal_blocking_exponent"]),
                    Fraction(47,8))
                self.assertEqual(
                    Fraction(v["strict_gap_to_six"]),Fraction(1,8))
                self.assertTrue(v["allh_prior_graph_CHUNK_supersaturation_requires_external_acceptance"])
                self.assertTrue(v["this_is_NOT_new_allh_geometric_Branch_A_proof"])

    def test_formal_graph_constants_are_NOT_independently_accepted(self):
        for params in ((-1,1),(0,0),(2,-1),(0,1.0),
                       (False,2),(True,3)):
            with self.assertRaises(ValueError):
                independent_tighter_original_selector_moment_ledger(*params)

    def test_actual_complete_ledger_scopes_no_new_root_proof(self):
        z=canonical_original_selector_symbolic_ledger()
        self.assertEqual(z["schema"],
                         "mathlab.hyp105.original-selector-analytic-47over8-checks.v1")
        self.assertEqual(len(z["formal_parameter_pairs"]),4)
        self.assertEqual(len(z["true_original_bipartite_source_graph_cases"]),6)
        self.assertTrue(z["no_new_allh_geometric_proof_claimed"])
        self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")


if __name__=="__main__":
    unittest.main()
