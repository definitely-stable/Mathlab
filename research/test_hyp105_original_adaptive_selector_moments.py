"""True original HYP-105 adaptive path-selector exact moment referee.

Independent end-to-end tests require:
- original W(3,2), W(3,4) full source incidence geometry;
- full separate globally injected fixed physical f,g, correlated allowed;
- actual ORIGINAL flag conflict priorities and BOTH physical color cuts;
- explicit EXACT small finite priority and coloring probability controls;
- actual physical fourth/sixth moments and weighted Jensen bounds;
- selected C6 injection to a historical actual original SIX-ID D6 motif.
These are falsifiers, not a finite proof of all dyadic orders.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations,product
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import (
    conflict_graph as reference_original_source_conflict_graph,
    physical as independent_original_physical_builder,
    verify_selected as reference_selector_source_cycle_checker,
)
from hyp105_original_adaptive_selector_moments import (
    _actual_gq,_true_original_source_conflict,
    _true_original_physical,_priority_color_selector_source_graph,
    _true_original_sixcycle_selector_audit,
    _paths_and_moments_for_r,adaptive_true_original_selector_certificate,
    selected_original_D6_witness,
)


class OriginalAdaptivePhysicalSelectorMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models={(h,scheme):pair_labeled_symplectic(h,scheme)
                    for h in (1,2)
                    for scheme in ("lex","reverse-line")}

    def test_one_specific_original_path_first_r_priority_and_color_probability_exact(self):
        for r,b in ((2,2),(2,5),(2,8),(3,3),(3,6),(3,8)):
            with self.subTest(r=r,b=b):
                if b>8:continue
                count=0
                total=0
                S=set(range(r))
                for permutation in permutations(range(b)):
                    total+=1
                    count+=set(permutation[:r])==S
                self.assertEqual(total,comb(b,r)*count)
                self.assertEqual(Fraction(count,total),Fraction(1,comb(b,r)))
                self.assertGreaterEqual(
                    Fraction(1,4**r*comb(b,r)),
                    Fraction(1,4**r*b**r))
        for r in (2,3):
            good=0;total=0
            for left in product((0,1),repeat=r+1):
                for right in product((0,1),repeat=r+1):
                    total+=1
                    good+=all(left[i]!=left[i+1] and
                              right[i]!=right[i+1] for i in range(r))
            self.assertEqual(Fraction(good,total),Fraction(1,4**r))

    def test_genuine_original_conflict_graph_and_paired_physical_DIAGONAL_provenance(self):
        for h,scheme,core_rule in (
            (1,"lex",lambda i:i%3!=0),
            (1,"reverse-line",lambda i:True),
            (2,"lex",lambda i:i%4==0),
            (2,"reverse-line",lambda i:i%7 in (0,2))):
            with self.subTest(h=h,scheme=scheme):
                m=self.models[h,scheme]
                flags=m["incidences"];f=m["left_labels"];g=m["right_labels"]
                C=tuple(i for i in range(len(flags)) if core_rule(i))
                exact=_true_original_source_conflict(flags,f,g,C)
                old,_,_=reference_original_source_conflict_graph(C,flags,f,g)
                self.assertEqual(
                    {i:set(v) for i,v in exact.items()},
                    {i:set(old.get(i,())) for i in C})
                adj,owner=_true_original_physical(flags,f,g,C)
                old_adj,old_owner=independent_original_physical_builder(C,flags,f,g)
                self.assertEqual(
                    {u:set(v) for u,v in adj.items()},
                    {u:set(v) for u,v in old_adj.items()})
                self.assertEqual(owner,old_owner)
                self.assertEqual(len(owner),2*len(C))
                self.assertTrue(all(len(x)!=0 for x in adj.values()))

    def test_real_W32_W34_exact_adaptive_2_3_moment_is_stronger_than_uniform(self):
        for h,scheme,core_rule in (
            (1,"lex",lambda i:True),
            (1,"reverse-line",lambda i:i%3!=0),
            (2,"lex",lambda i:i%4 in (0,1)),
            (2,"reverse-line",lambda i:i%5 in (1,3))):
            with self.subTest(h=h,scheme=scheme):
                m=self.models[h,scheme]
                Z=tuple(i for i in range(len(m["incidences"])) if i%29==0)
                C=tuple(i for i in range(len(m["incidences"]))
                        if core_rule(i) and i not in Z)
                z=adaptive_true_original_selector_certificate(
                    h,m["left_labels"],m["right_labels"],C,Z)
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertTrue(z["all_N_weighted_Jensen_original_selector_proof"])
                self.assertEqual(z["physical_core_edges"],2*len(C))
                self.assertEqual(z["deleted_original_source_IDs"],list(Z))
                self.assertEqual(z["retained_original_source_flags"],len(C))
                self.assertFalse(z["new_root_allh_Branch_A_proved_here"])
                self.assertEqual(z["real_original_trace_A4"],
                                 z["r2"]["physical_original_full_core_trace_A_to_2r"])
                self.assertEqual(z["real_original_trace_A6"],
                                 z["r3"]["physical_original_full_core_trace_A_to_2r"])
                for r in ("r2","r3"):
                    u=z[r]
                    adaptive=Fraction(
                        u["original_adaptive_weighted_endpoint_Frobenius_square"])
                    uniform=Fraction(
                        u["uniform_sigma_squared_times_exact_original_proper_endpoint_Frobenius_square"])
                    moment=u["physical_original_full_core_trace_A_to_2r"]
                    self.assertGreaterEqual(adaptive,uniform)
                    self.assertLessEqual(adaptive,moment)
                    self.assertGreater(u[
                        "directed_proper_original_physical_r_paths"],0)
                    self.assertGreaterEqual(
                        u["original_source_union_closed_conflict_neighborhood_max_b"],
                        u["original_source_union_closed_conflict_neighborhood_min_b"])
                    self.assertEqual(
                        sum(u["original_source_neighborhood_size_histogram"].values()),
                        u["directed_proper_original_physical_r_paths"])

    def test_actual_source_W32_constructed_positive_D6_SURVIVES_priority_and_both_cuts(self):
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                w=selected_original_D6_witness(1,scheme)
                self.assertTrue(w["selector_C6_source_injective"])
                self.assertTrue(w["source_priority_and_bichromatic_both_halves_FORCED_D6"])
                self.assertGreaterEqual(w["selected_physical_simple_C6"],1)
                self.assertIn(w["planted_original_six_flag_IDs"],
                              w["actual_original_flag_IDs_D6"])

    def test_genuine_original_deterministic_random_priority_color_selector_C6_injection(self):
        for h,scheme,nseed in ((1,"lex",5),(1,"reverse-line",5),
                               (2,"lex",2)):
            with self.subTest(h=h,scheme=scheme):
                m=self.models[h,scheme]
                n=len(m["incidences"])
                C=tuple(i for i in range(n) if h==1 or i%5==0)
                a=6 if h==1 else 14
                for seed in range(nseed):
                    pri=tuple(sorted(C,key=lambda i:((i*47+seed*11)%(n+17),i)))
                    left=tuple((j*13+seed+j//3)%2 for j in range(a))
                    right=tuple((j*7+2*seed+j//2)%2 for j in range(a))
                    result=_true_original_sixcycle_selector_audit(
                        h,m["left_labels"],m["right_labels"],C,pri,left,right)
                    self.assertEqual(
                        result["selected_physical_simple_C6"],
                        result["source_original_D6_sixsets_from_physical_C6"])
                    self.assertTrue(result["all_selected_C6_coordinate_proper"])
                    self.assertTrue(result["selector_C6_source_injective"])
                    physical,owner,kept=_priority_color_selector_source_graph(
                        m["incidences"],m["left_labels"],m["right_labels"],C,
                        pri,left,right)
                    # Independent historical owner/typed-flag no-row/col
                    # condition source gate, not relied on for our proof.
                    prior_adj,prior_owner,stats=reference_selector_source_cycle_checker(
                        kept,m["incidences"],m["left_labels"],
                        m["right_labels"],left,right)
                    self.assertEqual(
                        {u:set(v) for u,v in physical.items()},
                        {u:set(v) for u,v in prior_adj.items()})
                    self.assertEqual(owner,prior_owner)
                    self.assertEqual(stats["ordinary_C6"],
                                     result["selected_physical_simple_C6"])

    def test_illegal_source_flags_noninjective_labels_core_Z_fail_closed(self):
        m=self.models[1,"lex"]
        f,g=m["left_labels"],m["right_labels"]
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(1,f,g,(0,1,2),(2,))
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(1,f,g,(0,0,1),())
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(1,f,g,(0,1),(45,))
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(1,f,g,(0,1),(True,))
        bad=list(f);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(1,bad,g,(0,1),())
        with self.assertRaises(ValueError):
            adaptive_true_original_selector_certificate(3,f,g,(0,1),())
        with self.assertRaises(ValueError):
            _priority_color_selector_source_graph(
                m["incidences"],f,g,(0,1),(0,0),(0,)*6,(1,)*6)


if __name__=="__main__":
    unittest.main()
