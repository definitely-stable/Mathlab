"""AA4-CHUNKREF: independent all-h 2x tail and true ORIGINAL D6 check."""
from fractions import Fraction
from itertools import combinations,product
import json
from pathlib import Path
import unittest

from hyp105_balanced_chunk_source_referee import (
    exact_balanced_chunk,
    strengthened_tail_constants,
    independent_true_original_chunk,
)
from hyp105_branch_a_integrated_referee import (
    _root_theorem_constants_from_source_lemmas,
    _min_dyadic_at_least,
)
from hyp105_full_physical_degree_tail import (
    genuine_source,
    planted_original_k44,
    finite_tail_selector,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


def all_grid_edges(mask,p=3,q=4):
    vertices=tuple(range(p+q))
    graph={v:set() for v in vertices}
    for i,(u,v) in enumerate(product(range(p),range(p,p+q))):
        if mask&(1<<i):
            graph[u].add(v)
            graph[v].add(u)
    return graph


class TestAllHTrueOriginalChunkReferee(unittest.TestCase):
    def test_exhaustive_4096_labeled_bipartite_3x4_and_every_R_subset(self):
        # NO ORIGINAL geometry here; pure graph pigeonhole is independently
        # valid for all 4096 graphs and all 7 nonempty heavy left subsets.
        for mask in range(1<<12):
            graph=all_grid_edges(mask)
            for pop in range(1,1<<3):
                R={u for u in range(3) if pop>>u&1}
                z=exact_balanced_chunk(
                    graph,set(range(3)),set(range(3,7)),R)
                E=z["E_original_distinct_heavy_to_opposite_edges"]
                r=len(R)
                self.assertEqual(z["heavy_left_size_r"],r)
                self.assertLessEqual(z["number_actual_chunks"]*r,2*7)
                self.assertGreaterEqual(z["winner_actual_edges"]*2*7,E*r)
                self.assertGreaterEqual(
                    z["winner_actual_edges"]*4*7,
                    E*z["winner_actual_vertices"])
                self.assertLessEqual(z["winner_actual_vertices"],2*r)
                self.assertTrue(z["no_cloning_of_original_physical_vertices"])

    def test_sharper_all_h_exact_symbolic_source_tail_and_root_threshold(self):
        for C,c,eps in (
            (Fraction(1),Fraction(1),Fraction(1,8)),
            (Fraction(5,3),Fraction(2,17),Fraction(1,8)),
            (Fraction(1,1024),Fraction(1,97),Fraction(1,9)),
            (Fraction(17,7),Fraction(4,25),Fraction(1,3)),
            (Fraction(2**12),Fraction(1,2**12),Fraction(1,8)),
        ):
            with self.subTest(C=C,c=c,epsilon=eps):
                z=strengthened_tail_constants(C,c,eps)
                self.assertEqual(
                    2*z["new_T_threshold"],z["old_T_threshold"])
                self.assertEqual(z["new_T_threshold"],
                                 Fraction(2**40)*C**3/eps**6)
                self.assertEqual(
                    z["new_original_D6_lower_unchanged"],
                    c*eps**12/2**72)
                if eps==Fraction(1,8):
                    self.assertEqual(
                        z["new_T_threshold"],Fraction(2**58)*C**3)
                    self.assertEqual(
                        z["old_T_threshold"],Fraction(2**59)*C**3)
                    oldT=max(1,-(-z["old_T_threshold"].numerator//
                                  z["old_T_threshold"].denominator))
                    newT=max(1,-(-z["new_T_threshold"].numerator//
                                  z["new_T_threshold"].denominator))
                    self.assertLessEqual(newT,oldT)
                    old=_root_theorem_constants_from_source_lemmas(oldT)
                    new=_root_theorem_constants_from_source_lemmas(newT)
                    self.assertLessEqual(new["s0_integer"],old["s0_integer"])
                    ho,_=_min_dyadic_at_least(old["s0_integer"])
                    hn,_=_min_dyadic_at_least(new["s0_integer"])
                    self.assertLessEqual(hn,ho)

    def test_real_original_W32_lex_and_four_global_reassignments(self):
        model=pair_labeled_symplectic(1,"lex")
        f=tuple(model["left_labels"]);base=tuple(model["right_labels"])
        for shift in (0,1,3,7,11):
            right=tuple(base[(i+shift)%len(base)] for i in range(len(base)))
            for T in (Fraction(1,4),Fraction(1)):
                with self.subTest(shift=shift,T=T):
                    z=independent_true_original_chunk(1,f,right,T)
                    self.assertNotIn("empty_source_tail",z)
                    self.assertTrue(z["selected_both_original_diagonals"])
                    self.assertEqual(
                        z["actual_selected_physical_C6"],
                        z["actual_selected_ORIGINAL_D6_unique_sixsets"])
                    self.assertEqual(
                        z["actual_balanced_F_e"],
                        z["balanced_chunk"]["winner_actual_edges"])
                    self.assertLessEqual(
                        z["actual_balanced_F_C6"],
                        z["actual_selected_physical_C6"])
                    self.assertGreaterEqual(
                        z["original_full_heavy_physical_edges"],0)
                    self.assertGreaterEqual(
                        z["after_second_typed_cut"]*4,
                        z["original_independent_flag_count"])

    def test_real_original_W34_full_sparse_reassigned_g_and_planted_C6(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,fixture["f"])),tuple(map(tuple,fixture["g"]))
        _,V,flags=genuine_source(2)
        cases=[
            ("full",f,g,None,Fraction(1)),
            ("permuted",f,tuple(g[(i+17)%V] for i in range(V)),
             None,Fraction(2)),
            ("sparse-true-heavy",f,g,None,Fraction(1,2)),
        ]
        for name,left,right,core,T in cases:
            with self.subTest(name=name,T=T):
                z=independent_true_original_chunk(2,left,right,T,core)
                self.assertNotIn("empty_source_tail",z)
                self.assertTrue(z["real_original_W3_source_not_all_h_proof"])
                self.assertEqual(
                    z["actual_selected_physical_C6"],
                    z["actual_selected_ORIGINAL_D6_unique_sixsets"])
                self.assertGreaterEqual(
                    z["balanced_chunk"]["E_original_distinct_heavy_to_opposite_edges"],
                    z["heavy_original_source_witnesses_side"])
        left,right,ids=planted_original_k44()
        planted=independent_true_original_chunk(
            2,left,right,Fraction(1,4),source_subset=ids)
        old=finite_tail_selector(
            2,left,right,Fraction(1,4),source_subset=ids)
        self.assertEqual(
            planted["actual_selected_ORIGINAL_D6_unique_sixsets"],96)
        self.assertEqual(
            planted["actual_selected_ORIGINAL_D6_unique_sixsets"],
            old["accepted_original_D6"])
        self.assertGreater(planted["actual_balanced_F_v"],0)
        self.assertGreater(planted["actual_balanced_F_e"],0)

    def test_invalid_physical_bipartitions_ineffective_source_and_threshold(self):
        graph=all_grid_edges((1<<12)-1)
        for args in [
            (graph,{0,1},{1,3,4,5,6},{0}),
            (graph,{0,1,2},{3,4,5,6},set()),
            (graph,{0,1,2},{3,4,5,6},{4}),
        ]:
            with self.assertRaises(ValueError):
                exact_balanced_chunk(*args)
        with self.assertRaises(ValueError):
            exact_balanced_chunk({0:{1},1:set()}, {0},{1},{0})
        with self.assertRaises(ValueError):
            exact_balanced_chunk(graph,{0,1,2},{3,4,5,6},{0},physical_n=6)
        for triple in ((0,1,Fraction(1,8)),(1,0,Fraction(1,8)),
                       (1,1,0),(1,1,-1),("abc",1,1)):
            with self.assertRaises(ValueError):
                strengthened_tail_constants(*triple)
        model=pair_labeled_symplectic(1,"lex")
        with self.assertRaises(ValueError):
            independent_true_original_chunk(
                1,model["left_labels"],model["right_labels"],0)
        with self.assertRaises(ValueError):
            independent_true_original_chunk(
                1,model["left_labels"][:-1],model["right_labels"],1)
        with self.assertRaises(ValueError):
            independent_true_original_chunk(
                3,model["left_labels"],model["right_labels"],1)
        with self.assertRaises(ValueError):
            independent_true_original_chunk(
                1,model["left_labels"],model["right_labels"],
                Fraction(1,4),source_subset=(0,0))

    def test_machine_readable_original_sixcycle_chunk_certificate(self):
        z=strengthened_tail_constants(Fraction(1),Fraction(1),Fraction(1,8))
        print("HYP105_AA4_CHUNKREF_CERTIFICATE="+json.dumps({
            "graph_theorem_C_c_are_hypothetical_not_authoritative":True,
            "new_T_threshold_at_epsilon_eighth":str(z["new_T_threshold"]),
            "old_T_threshold_at_epsilon_eighth":str(z["old_T_threshold"]),
            "new_T_allh":"2^40*C_graph^3*epsilon^-6",
            "old_T_allh":"2^41*C_graph^3*epsilon^-6",
            "original_D6_sextic_lower_unchanged":"c_graph*epsilon^12/2^72",
            "source_heavy_degree_sum":"sum_v deg_full(v)=4N<=8s4",
            "original_C6_to_six_distinct_flag_ID_injection":True,
            "all_4096_graphs_and_all_nonempty_R_subsets":True,
            "source_true_W32_W34_including_planted_K44":True,
            "root_Branch_A_external_peer_review_pending":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
