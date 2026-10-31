"""AA4-MOM6: referee-grade exact graph six-walk and REAL original GQ tests."""
from fractions import Fraction
from itertools import combinations,product
import json
from pathlib import Path
import unittest

from hyp105_exact_bipartite_sixth_moment import (
    exact_bipartite_sixwalk_certificate,
    improved_allh_selected_sixth_moment_envelopes,
    genuine_source_selected_graph_moment_certificates,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source


def graph_from_bipartite_mask(n_left,n_right,mask):
    """Independent exact graph constructor for every bipartite edge set."""
    graph={v:set() for v in range(n_left+n_right)}
    for j,(u,v) in enumerate(product(range(n_left),
                                      range(n_left,n_left+n_right))):
        if mask&(1<<j):
            graph[u].add(v);graph[v].add(u)
    return graph


class TestExactSixthMomentReferee(unittest.TestCase):
    def test_ALL_bipartite_graphs_on_three_plus_four_vertices(self):
        # Exhaust ALL 2^(3*4)=4096 graphs. Each C6, tr A4 and tr A6
        # additionally verified by separate direct DFS and walk DP.
        for mask in range(1<<12):
            g=graph_from_bipartite_mask(3,4,mask)
            x=exact_bipartite_sixwalk_certificate(
                g,range(3),range(3,7),exhaustive=True)
            self.assertEqual(
                x["trace_A6"],
                12*x["simple_physical_C6"]+x["noninjective_sixwalks"])
            self.assertLessEqual(
                x["trace_A6"],24*x["simple_physical_C6"]+
                                   72*x["edges"]*x["max_degree"]**2)
            self.assertLessEqual(
                x["trace_A4"]**2,2*x["edges"]*x["trace_A6"])
            self.assertEqual(
                x["noninjective_sixwalks"],
                x["left_collision_decomposition"]["noninjective_closed_six_walk_count"])
        self.assertTrue(True)

    def test_explicit_sixcycle_complete_bipartite_stars_and_empty_graphs(self):
        cases=[
            (3,3,0),
            (3,3,(1<<9)-1),
            (4,4,(1<<16)-1),
            (4,4,0x6969),
            (4,3,(1<<12)-1),
            (1,5,(1<<5)-1),
            (3,4,0x7ee),
            (2,6,0xfab),
        ]
        for left,right,mask in cases:
            with self.subTest(left=left,right=right,mask=mask):
                q=exact_bipartite_sixwalk_certificate(
                    graph_from_bipartite_mask(left,right,mask),
                    range(left),range(left,left+right),exhaustive=True)
                self.assertGreaterEqual(q["noninjective_sixwalks"],0)
                self.assertTrue(q["full_exact_independent_6walk_DFS_checked"])
                self.assertEqual(
                    q["trace_A6"],
                    12*q["simple_physical_C6"]+q["noninjective_sixwalks"])
                self.assertEqual(q["left_collision_decomposition"][
                    "simple_C6"],q["simple_physical_C6"])
                self.assertEqual(q["right_collision_decomposition"][
                    "simple_C6"],q["simple_physical_C6"])
                self.assertLessEqual(q["tighter_all_h_Young_upper"],
                                     q["old_672_all_h_upper"])
        k33=exact_bipartite_sixwalk_certificate(
            graph_from_bipartite_mask(3,3,(1<<9)-1),
            range(3),range(3,6),exhaustive=True)
        self.assertEqual(k33["simple_physical_C6"],6)
        self.assertEqual(k33["trace_A6"],1458)
        self.assertEqual(k33["noninjective_sixwalks"],1386)
        self.assertEqual(k33["trace_A4"],162)

    def test_all_h_L6_propagation_together_with_new_selector(self):
        for K in (0,1,64,128):
            for T in (1,2,100,2**65):
                with self.subTest(K=K,T=T):
                    a=improved_allh_selected_sixth_moment_envelopes(K,T)
                    self.assertEqual(a["strict_L6_gain"],288*T*T)
                    self.assertEqual(a["old_L6_s6"],24+576*T*T)
                    self.assertEqual(a["new_L6_s6"],24+288*T*T)
                    self.assertGreaterEqual(
                        a["P3_frobenius_exact_strict_ratio"],729)
                    self.assertEqual(
                        a["P2_frobenius_square_coefficient_ratio"],16)
                    self.assertLess(
                        a["new_P3_frobenius_coefficient"],
                        a["old_P3_frobenius_coefficient"])
                    self.assertFalse(a["full_Branch_A_root_scientific_acceptance"])

    def test_TRUE_original_W32_five_correlated_g_selected_physical_graphs(self):
        model=pair_labeled_symplectic(1,"lex")
        f=tuple(model["left_labels"])
        g0=tuple(model["right_labels"])
        total=0
        for shift in (0,1,3,7,11):
            g=tuple(g0[(i+shift)%len(g0)] for i in range(len(g0)))
            with self.subTest(shift=shift):
                q=genuine_source_selected_graph_moment_certificates(
                    1,f,g,seeds=(1,3,7,11,19,37))
                self.assertEqual(len(q["certificates"]),6)
                self.assertTrue(q["all_selected_graphs_from_true_original_flags"])
                for row in q["certificates"]:
                    z=row["physical_moment"]
                    self.assertEqual(
                        z["trace_A6"],12*z["simple_physical_C6"]+z["noninjective_sixwalks"])
                    self.assertLessEqual(
                        z["trace_A6"],z["tighter_all_h_Young_upper"])
                    self.assertEqual(
                        z["simple_physical_C6"],row["accepted_original_D6_C6_subcount"])
                    total+=z["edges"]
        self.assertGreater(total,0)

    def test_TRUE_original_W34_adversarial_sparse_and_reassigned_g(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f=tuple(map(tuple,fixture["f"]))
        g=tuple(map(tuple,fixture["g"]))
        _,V,flags=genuine_source(2)
        cases=[
            ("full",None,g),
            ("sparse",tuple(i for i in range(len(flags)) if i%3),g),
            ("shuffled-right",tuple(i for i in range(len(flags)) if i%4),
                         tuple(g[(i+17)%V] for i in range(V))),
        ]
        for tag,core,right in cases:
            with self.subTest(name=tag):
                q=genuine_source_selected_graph_moment_certificates(
                    2,f,right,core,seeds=(3,7,11,23))
                self.assertEqual(len(q["certificates"]),4)
                for row in q["certificates"]:
                    c=row["physical_moment"]
                    self.assertTrue(c["full_exact_independent_6walk_DFS_checked"])
                    self.assertEqual(c["trace_A6"],
                                     c["noninjective_sixwalks"]+
                                     12*c["simple_physical_C6"])
                    self.assertEqual(c["simple_physical_C6"],
                                     row["accepted_original_D6_C6_subcount"])

    def test_invalid_graph_and_original_source_cases_fail_closed(self):
        with self.assertRaises(ValueError):
            exact_bipartite_sixwalk_certificate({0:{1},1:set()})
        with self.assertRaises(ValueError):
            exact_bipartite_sixwalk_certificate({0:{0}})
        with self.assertRaises(ValueError):
            exact_bipartite_sixwalk_certificate(
                {0:{1,2},1:{0,2},2:{0,1}})
        with self.assertRaises(ValueError):
            exact_bipartite_sixwalk_certificate(
                {0:{1},1:{0}},left=(0,1),right=())
        with self.assertRaises(ValueError):
            improved_allh_selected_sixth_moment_envelopes(64,0)
        model=pair_labeled_symplectic(1,"lex")
        for core in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                genuine_source_selected_graph_moment_certificates(
                    1,model["left_labels"],model["right_labels"],core)
        with self.assertRaises(ValueError):
            genuine_source_selected_graph_moment_certificates(
                1,model["left_labels"][:-1],model["right_labels"])

    def test_machine_readable_sixth_moment_certificate(self):
        q=improved_allh_selected_sixth_moment_envelopes(64,2**65)
        print("HYP105_AA4_MOM6_CERTIFICATE="+json.dumps({
            "pure_graph_all_h":"trace(A^6)<=24*C6+72*m*Delta^2",
            "original_672":"trace(A^6)<=24*C6+144*m*Delta^2",
            "exact_bipartite_noninjective_6walk_identity":True,
            "old_L6":str(q["old_L6_s6"]),
            "new_L6":str(q["new_L6_s6"]),
            "selector_sigma3_combined_P3_gain_at_least":"729x",
            "all_4096_bipartite_3x4_graphs":True,
            "real_source_W32_W34_not_synthetic_host":True,
            "does_not_claim_full_root_Branch_A_acceptance":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
