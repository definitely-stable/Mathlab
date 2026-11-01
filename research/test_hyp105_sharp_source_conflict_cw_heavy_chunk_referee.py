"""AA4-CWSHARP — independently falsify source conflicts, CW and real chunks."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_sharp_source_conflict_cw_heavy_chunk_referee import (
    minimum_original_alphabet,true_original_source_book_symbolic,
    exact_source_selector_bridge,_independent_conflict_census,
    _min_degree_constructive_cw,_conditional_typed_cut,
    independent_true_source_heavy_cw_referee,
)
from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44


def labels(power,shift=0):
    _,V,_=genuine_source(power)
    a=minimum_original_alphabet(V)
    base=tuple(combinations(range(a),2))[:V]
    return base,tuple(base[(19*i+shift)%V] for i in range(V))


class OriginalSourceSharpCaroWei(unittest.TestCase):
    def test_exact_dyadic_original_Cs_six_fifths_and_alphabet_envelope(self):
        for h in range(6,26):
            s=2**h
            r=true_original_source_book_symbolic(s)
            self.assertEqual(r["a_minimal"],minimum_original_alphabet(r["V"]))
            self.assertLess(comb(r["a_minimal"]-1,2),r["V"])
            self.assertGreaterEqual(comb(r["a_minimal"],2),r["V"])
            self.assertLessEqual(r["Cs_over_s4"],Fraction(6,5))
            self.assertLess(r["uniform_rho_analytic"],Fraction(6,5))
            self.assertEqual(r["Cs_exact"],(s*s+1)*(s*s+r["a_minimal"]-2))
            self.assertEqual(r["main_n2N_actual_original_paired_physical_edges"],
                             2*(s+1)**2*(s*s+1))
        self.assertLess(true_original_source_book_symbolic(64)["Cs_over_s4"],
                        Fraction(6,5))

    def test_exact_new_beta_heavy_threshold_and_D6_all_rational_eps(self):
        epslist=(Fraction(1,8),Fraction(1,4),Fraction(1787,4096),
                 Fraction(13,32),Fraction(1),Fraction(2),Fraction(4))
        for eps in epslist:
            for C,c in ((1,1),(Fraction(7,9),Fraction(3,11)),
                        (Fraction(17,2),Fraction(2,19))):
                with self.subTest(eps=eps,C=C,c=c):
                    r=exact_source_selector_bridge(eps,C,c)
                    old=eps*eps/128
                    expected=5*eps*eps/(384+40*eps)
                    self.assertEqual(r["old_beta"],old)
                    self.assertEqual(r["new_beta"],expected)
                    self.assertEqual(r["new_to_old_source_retention_factor"],
                                     Fraction(640,384+40*eps))
                    self.assertGreaterEqual(r["new_beta"],old)
                    self.assertEqual(r["new_symbolic_T_threshold"],
                                     2**19*Fraction(C)**3/expected**3)
                    self.assertEqual(r["new_original_D6_coefficient"],
                                     Fraction(c)*(expected/32)**6)
                    self.assertLessEqual(r["new_T_over_old_T"],1)
                    self.assertGreaterEqual(r["new_D6_over_old_D6"],1)
                    self.assertTrue(r["graph_constants_are_hypothetical_not_published_values"])

    def test_new_selector_uses_Cs_bound_not_old_3_halves(self):
        eps=Fraction(1787,4096)
        result=exact_source_selector_bridge(eps,1,1)
        self.assertGreater(result["new_to_old_source_retention_factor"],
                           Fraction(3,2))
        self.assertLess(result["new_T_over_old_T"],Fraction(1,4))
        self.assertGreater(result["new_D6_over_old_D6"],Fraction(16))
        self.assertEqual(result["original_uniform_book_rho"],Fraction(6,5))

    def test_every_1024_five_vertex_graphs_caro_wei_constructive_with_edge_major(self):
        pts=tuple(range(5))
        pairs=tuple(combinations(pts,2))
        for mask in range(1<<10):
            conflict={u:set() for u in pts}
            for j,(u,v) in enumerate(pairs):
                if mask>>j&1:
                    conflict[u].add(v);conflict[v].add(u)
            selected,cw=_min_degree_constructive_cw(conflict)
            self.assertGreaterEqual(len(selected),cw)
            self.assertEqual(cw,sum((Fraction(1,len(ns)+1)
                                     for ns in conflict.values()),Fraction()))
            self.assertFalse(any(v in conflict[u] for u,v in combinations(selected,2)))

    def test_all_4096_three_by_four_binary_cuts_exact_half(self):
        # Each of 12 possible original physical pair-label edges may occur
        # or not, with distinct flag IDs and independent source point IDs.
        edges=tuple((x,y) for x in range(3) for y in range(3,7))
        labels0=tuple(edges)
        flags=tuple((i,i) for i in range(12))
        for mask in range(4096):
            ids=tuple(i for i in range(12) if mask>>i&1)
            kept,col=_conditional_typed_cut(ids,flags,labels0,0,7)
            self.assertGreaterEqual(2*len(kept),len(ids))
            self.assertEqual(tuple(i for i in ids if col[edges[i][0]]!=col[edges[i][1]]),kept)

    def test_true_original_W32_independent_full_conflict_book_and_heavy_witnesses(self):
        s,V,flags=genuine_source(1)
        for k in (0,1,3,7,11):
            f,g=labels(1,k)
            conflict,point,line=_independent_conflict_census(range(len(flags)),flags,f,g)
            self.assertEqual(sum(map(len,conflict.values()))//2,point+line)
            C=(s*s+1)*(s*s+minimum_original_alphabet(V)-2)
            self.assertLessEqual(max(point,line),C)
            for T in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(10)):
                z=independent_true_source_heavy_cw_referee(1,f,g,T)
                self.assertEqual(z["original_full_physical_edges"],2*len(flags))
                self.assertGreaterEqual(z["independent_original_source_flags"],
                                        z["actual_source_Caro_Wei_sum"])
                self.assertGreaterEqual(4*z["selected_original_source_flags_after_two_cuts"],
                                        z["independent_original_source_flags"])
                self.assertEqual(z["retained_original_owners_both_physical_diagonals"],
                                 2*z["selected_original_source_flags_after_two_cuts"])
                self.assertEqual(z["actual_original_heavy_witnesses_retained"],
                                 z["selected_original_source_flags_after_two_cuts"])
                chunk=z["no_cloned_physical_chunk"]
                if chunk is not None:
                    self.assertGreaterEqual(
                        2*minimum_original_alphabet(V)**2*chunk["winner_edges"],
                        chunk["full_R_to_Y_edges"]*chunk["heavy_R"])

    def test_true_original_W34_correlated_maps_full_and_sparse_tails(self):
        _,V,flags=genuine_source(2)
        for shift,T in ((0,Fraction(1,4)),(5,Fraction(1,2)),
                        (17,Fraction(1))):
            f,g=labels(2,shift)
            z=independent_true_source_heavy_cw_referee(2,f,g,T)
            self.assertEqual(z["original_full_flags"],len(flags))
            self.assertEqual(z["original_full_physical_edges"],2*len(flags))
            self.assertGreaterEqual(z["independent_original_source_flags"],
                                    z["strong_original_conflict_CW_lower"])
            self.assertGreaterEqual(z["strong_original_conflict_CW_lower"],
                                    z["symbolic_source_Cs_CW_lower"])
            self.assertGreaterEqual(
                z["chosen_side_original_heavy_witnesses"]*2,
                z["selected_original_source_flags_after_two_cuts"])

    def test_true_original_W34_planted_original_K44_and_empty_tail(self):
        f,g,ids=planted_original_k44()
        z=independent_true_source_heavy_cw_referee(2,f,g,Fraction(1,4))
        self.assertEqual(z["original_full_physical_edges"],2*z["original_full_flags"])
        self.assertTrue(z["not_an_all_h_numeric_W32_W34_proof"])
        zempty=independent_true_source_heavy_cw_referee(2,f,g,999)
        self.assertEqual(zempty["full_original_heavy_vertices"],0)
        self.assertEqual(zempty["selected_original_source_flags_after_two_cuts"],0)
        self.assertIsNone(zempty["no_cloned_physical_chunk"])

    def test_invalid_dyadic_trial_constants_and_original_injections_fail_closed(self):
        for s in (0,32,63,65,96,-64,64.0,True):
            with self.assertRaises(ValueError):
                true_original_source_book_symbolic(s)
        for epsilon,C,c in ((0,1,1),(-1,1,1),(5,1,1),
                            (Fraction(1,8),0,1),(Fraction(1,8),1,0),
                            (0.1,1,1),(Fraction(1,8),True,1)):
            with self.assertRaises(ValueError):
                exact_source_selector_bridge(epsilon,C,c)
        f,g=labels(1)
        for power,ff,gg,T in ((0,f,g,1),(3,f,g,1),(1,f[:-1],g,1),
                              (1,(f[0],)*len(f),g,1),(1,f,g,0),
                              (1,f,g,True)):
            with self.assertRaises(ValueError):
                independent_true_source_heavy_cw_referee(power,ff,gg,T)


if __name__=="__main__":
    unittest.main()
