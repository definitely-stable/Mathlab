r"""Independent adversarial ORIGINAL-ID Z heavy tail and actual SS6 test gates.

Genuine symplectic W32/W34 source maps only for complete true original
finite fuzz; synthetic ordinary K3,4 only algebraic independent
pigeonhole falsification. The theorem itself is all finite dyadic s,
and its conditional published SS6 constants are NEVER invented.
"""
from fractions import Fraction
from itertools import combinations,product
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import physical as independent_source_owner
from hyp105_balanced_chunk_source_referee import exact_balanced_chunk
from hyp105_ordinary_c6_ss6_hypothesis_spectral_bridge import exact_c6_gate

from hyp105_original_deletion_adaptive_heavy_tail import (
    _complete_true_original,_owned_physical,_true_source_conflict,
    _caro_wei_original_independent,_two_cut_conditional,
    _local_balanced_no_clone,_real_original_selector_adaptive_heavy,
    exact_allh_robust_source_tail_constants,
    canonical_original_deleted_adaptive_heavy_report,
)


class OriginalSourceDeletionAdaptiveHeavyTail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models={(h,scheme):pair_labeled_symplectic(h,scheme)
                    for h in (1,2) for scheme in ("lex","reverse-line")}

    def test_exact_original_adversarial_deletion_measures_FULL_Q_not_retrimmed(self):
        for h,scheme,T,Z in (
            (1,"lex",Fraction(1,2),(0,)),
            (1,"reverse-line",Fraction(3,4),(1,13,33)),
            (2,"lex",Fraction(1),(0,10,100,200)),
            (2,"reverse-line",Fraction(5,4),(0,25,26,33,34))):
            with self.subTest(h=h,scheme=scheme):
                m=self.models[h,scheme]
                z=_real_original_selector_adaptive_heavy(
                    h,m["left_labels"],m["right_labels"],Z,T)
                self.assertFalse(z.get("empty_tail",False))
                self.assertTrue(z["original_both_real_diagonals_per_selected_ID"])
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertFalse(z["root_allh_Branch_A_proved_here"])
                self.assertTrue(z["unknown_published_C_graph_c_graph_NOT_guessed"])
                self.assertEqual(z["deleted_original_flag_IDs"],list(Z))
                self.assertLessEqual(z["actual_original_heavy_edges_removed_by_Z"],
                                     2*len(Z))
                self.assertEqual(
                    z["original_tail_edges_remaining_after_Z"],
                    z["full_original_tail_edges"]-
                    z["actual_original_heavy_edges_removed_by_Z"])
                I=z["retained_heavy_original_flag_IDs"]
                L=len(I);e=z["original_heavy_conflict_edges_actual"]
                self.assertGreaterEqual(
                    4*z["original_both_typed_cuts_selected_count"]*(L+2*e),L*L)
                self.assertGreaterEqual(
                    z["actual_original_heavy_witnesses_on_chosen_side"]*2,
                    z["original_both_typed_cuts_selected_count"])
                n=z["full_original_physical_vertices"]
                q=z["full_original_QT_vertices"]
                floor=Fraction(L**6,2**16*n**3*q*(L+2*e)**3)
                self.assertEqual(
                    Fraction(z["exact_external_C_graph_CUBED_sufficient_data_threshold"]),
                    floor)
                w=z["actual_uncloned_balanced_chunk"]
                E=w["winner_ordinary_subgraph_edges"]
                v=w["winner_ordinary_subgraph_vertices"]
                self.assertGreaterEqual(Fraction(E**3,v**4),floor)
                self.assertLessEqual(v,2*q)
                self.assertTrue(z["source_c6_injects_original_positive_D6_after_Z"])
                self.assertEqual(
                    len(z["true_original_D6_six_flag_IDs_selected"]),
                    z["actual_physical_selected_C6"])
                for ids in z["true_original_D6_six_flag_IDs_selected"]:
                    self.assertEqual(len(set(ids)),6)
                    self.assertTrue(set(ids).isdisjoint(Z))

    def test_independent_genuine_full_original_physical_provenance_and_conflicts(self):
        for h,scheme in ((1,"lex"),(1,"reverse-line"),
                         (2,"lex"),(2,"reverse-line")):
            m=self.models[h,scheme]
            s,V,a,flags,f,g,Z,T=_complete_true_original(
                h,m["left_labels"],m["right_labels"],(0,),Fraction(1))
            ids=tuple(range(len(flags)))
            adj,owner=_owned_physical(flags,f,g,ids)
            otheradj,otherowner=independent_source_owner(ids,flags,f,g)
            self.assertEqual(owner,otherowner)
            self.assertEqual({v:set(ns) for v,ns in adj.items()},
                             {v:set(ns) for v,ns in otheradj.items()})
            self.assertEqual(len(owner),2*len(ids))
            I=tuple(i for i in range(len(ids)) if i%4==0)
            J=_true_source_conflict(flags,f,g,I)
            independent,weight=_caro_wei_original_independent(J)
            for u,v in combinations(independent,2):
                self.assertNotIn(v,J[u])
            self.assertGreaterEqual(len(independent),weight)
            first,lc=_two_cut_conditional(flags,f,independent,0,a)
            second,rc=_two_cut_conditional(flags,g,first,1,a)
            self.assertGreaterEqual(2*len(first),len(independent))
            self.assertGreaterEqual(2*len(second),len(first))
            self.assertEqual(len(lc),a)
            self.assertEqual(len(rc),a)

    def test_independent_EXHAUSTIVE_all_4096_K3x4_graph_heavy_R_chunks(self):
        # Abstract graph algebra only, no GQ source stand-in.
        for mask in range(1<<12):
            full={i:set() for i in range(7)}
            for k,(u,v) in enumerate(product(range(3),range(3,7))):
                if mask&(1<<k):
                    full[u].add(v);full[v].add(u)
            for Rmask in range(1,8):
                R={u for u in range(3) if (Rmask>>u)&1}
                Y=set(range(3,7))
                z=_local_balanced_no_clone(full,R,Y,7)
                w=exact_balanced_chunk(full,set(range(3)),Y,R,physical_n=7)
                self.assertGreaterEqual(
                    z["winner_ordinary_subgraph_edges"]*2*7,
                    z["edges_between_heavyR_and_Y"]*len(R))
                self.assertGreaterEqual(
                    z["winner_ordinary_subgraph_edges"],w["winner_actual_edges"])
                self.assertLessEqual(
                    z["winner_ordinary_subgraph_vertices"],2*len(R))
                self.assertLessEqual(
                    z["physical_nonclone_original_chunk_count"]*len(R),14)

    def test_actual_original_winner_is_SIMPLE_GRAPH_for_external_theorem(self):
        for h,scheme,T,Z in (
            (1,"lex",Fraction(1,2),(0,)),
            (2,"lex",Fraction(1),(0,10,100,200))):
            m=self.models[h,scheme]
            z=_real_original_selector_adaptive_heavy(
                h,m["left_labels"],m["right_labels"],Z,T)
            w=z["actual_uncloned_balanced_chunk"]
            R={tuple(x) for x in w["winner_original_physical_vertices"]}
            A={x:set() for x in R}
            for v,u in w["winner_actual_physical_edges"]:
                v=tuple(v);u=tuple(u)
                A[v].add(u);A[u].add(v)
            C={tuple(v) for v in w["winner_original_physical_vertices"]
               if v[0]!=next(iter(A))[0]}
            # Determine bipartition from true physical first-coordinate
            # binary cut using edges, never from synthetic source copies.
            if A and any(A.values()):
                root=next(v for v in A if A[v])
                left=set();right=set()
                side={root:0};work=[root]
                for v in work:
                    for u in A[v]:
                        if u not in side:
                            side[u]=1-side[v];work.append(u)
                        else:self.assertNotEqual(side[u],side[v])
                # Zero-edge isolates may choose either bipartition.
                for v in A:
                    side.setdefault(v,0)
                left={v for v in A if side[v]==0}
                right=set(A)-left
                out=exact_c6_gate(A,left,right)
                self.assertEqual(out["simple_C6_unrooted_unoriented"],
                                 z["actual_winner_uncloned_physical_C6"])
            self.assertEqual(len(w["winner_actual_physical_edges"]),
                             sum(map(len,A.values()))//2)

    def test_exact_formal_root_new_2to64_and_old_2to65_C3(self):
        for C,c,eps in (
            (Fraction(1),Fraction(1),Fraction(1,16)),
            (Fraction(7,3),Fraction(2,101),Fraction(1,16)),
            (Fraction(4),Fraction(1,5),Fraction(1,32))):
            with self.subTest(C=C,c=c,eps=eps):
                z=exact_allh_robust_source_tail_constants(C,c,eps)
                self.assertEqual(
                    Fraction(z["improved_684_AND_adversarial_original_deletion_T"]),
                    Fraction(2**40)*C**3/eps**6)
                self.assertEqual(
                    Fraction(z["old_659_heavy_threshold_T"]),
                    2*Fraction(z["improved_684_AND_adversarial_original_deletion_T"]))
                self.assertEqual(
                    Fraction(z["original_D6_after_ANY_deletion_lower_multiplier_of_sixpower"]),
                    c*eps**12/2**72)
                self.assertEqual(
                    Fraction(z["root_674_NEW_T_for_same_full_tail_deletion_hypothesis"]),
                    2**64*C**3)
                self.assertEqual(
                    Fraction(z["root_674_old_T_for_full_tail_eighth_original_deletion_at_most_1over32"]),
                    2**65*C**3)
                self.assertFalse(
                    z["actual_published_graph_constants_numerical_values_VERIFIED"])
                self.assertFalse(z["new_root_allh_geometric_Branch_A_proved"])
        for args in ((0,1,1),(1,0,1),(1,1,0),(1,-1,1)):
            with self.assertRaises(ValueError):
                exact_allh_robust_source_tail_constants(*args)

    def test_reject_duplicated_original_source_ID_or_noninjected_maps(self):
        m=self.models[1,"lex"];f,g=m["left_labels"],m["right_labels"]
        for Z in ((0,0),(45,),(-1,),(True,)):
            with self.assertRaises(ValueError):
                _real_original_selector_adaptive_heavy(
                    1,f,g,Z,Fraction(1))
        for T in (Fraction(0),Fraction(-1,2)):
            with self.assertRaises(ValueError):
                _real_original_selector_adaptive_heavy(1,f,g,(0,),T)
        ff=list(f);ff[1]=ff[0]
        with self.assertRaises(ValueError):
            _real_original_selector_adaptive_heavy(1,ff,g,(0,),Fraction(1))
        with self.assertRaises(ValueError):
            _real_original_selector_adaptive_heavy(3,f,g,(0,),Fraction(1))


if __name__=="__main__":
    unittest.main()
