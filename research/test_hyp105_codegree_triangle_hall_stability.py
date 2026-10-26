"""AA4-HALL2: exhaustive Hall-SDR two-common-neighbor triangle stability."""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import planted_original_k44
from hyp105_coherent_c6_codegree_trace import exact_bipartite_codegree_trace
from hyp105_codegree_triangle_hall_stability import (
    exact_double_codegree_triangle_stability,
    true_original_source_coherent_Hall_certificate,
)


def graph_from_mask(nleft,nright,mask):
    L=tuple((0,i) for i in range(nleft))
    R=tuple((1,j) for j in range(nright))
    adj={v:set() for v in L+R}
    for i,u in enumerate(L):
        for j,v in enumerate(R):
            if mask & (1<<(i*nright+j)):
                adj[u].add(v)
                adj[v].add(u)
    return adj


class TestCodegreeTriangleHallStability(unittest.TestCase):
    def test_sharp_K32_K33_K44_and_near_saturation(self):
        k32=graph_from_mask(3,2,(1<<6)-1)
        z=exact_double_codegree_triangle_stability(k32)
        self.assertEqual((
            z["double_codegree_triangle_count"],
            z["saturated_identical_two_right_witness_triangles"],
            z["triple_codegree_triangle_count"],
            z["direct_exact_C6_on_double_codegree_left_triples"],
            z["all_h_stable_C6_lower"],
            z["total_C6_independent_right_collision_trace"],
        ),(1,1,0,0,0,0))
        # A single extra physical right witness shared by only two left
        # hubs creates EXACTLY TWO genuine simple sixcycles.
        nearly=graph_from_mask(3,3,0)
        for u in ((0,0),(0,1),(0,2)):
            for v in ((1,0),(1,1)):
                nearly[u].add(v)
                nearly[v].add(u)
        right=(1,2)
        for u in ((0,0),(0,1)):
            nearly[u].add(right)
            nearly[right].add(u)
        z=exact_double_codegree_triangle_stability(nearly)
        self.assertEqual((
            z["double_codegree_triangle_count"],
            z["saturated_identical_two_right_witness_triangles"],
            z["productive_double_codegree_triangles"],
            z["triple_codegree_triangle_count"],
            z["direct_exact_C6_on_double_codegree_left_triples"],
            z["all_h_stable_C6_lower"],
        ),(1,0,1,0,2,2))
        z=exact_double_codegree_triangle_stability(
            graph_from_mask(3,3,(1<<9)-1))
        self.assertEqual((
            z["double_codegree_triangle_count"],
            z["triple_codegree_triangle_count"],
            z["direct_exact_C6_on_double_codegree_left_triples"],
            z["all_h_stable_C6_lower"],
        ),(1,1,6,6))
        z=exact_double_codegree_triangle_stability(
            graph_from_mask(4,4,(1<<16)-1))
        self.assertEqual((
            z["double_codegree_triangle_count"],
            z["saturated_identical_two_right_witness_triangles"],
            z["triple_codegree_triangle_count"],
            z["direct_exact_C6_on_double_codegree_left_triples"],
            z["all_h_stable_C6_lower"],
        ),(4,0,4,96,24))

    def test_all_512_simple_3_by_3_bipartite_graphs(self):
        n_saturated=n_productive=0
        for mask in range(1<<9):
            graph=graph_from_mask(3,3,mask)
            z=exact_double_codegree_triangle_stability(graph)
            c6=exact_bipartite_codegree_trace(graph,verify_by_dfs=True)[
                "exact_ordinary_C6"]
            self.assertLessEqual(z["all_h_stable_C6_lower"],c6)
            self.assertLessEqual(
                z["direct_exact_C6_on_double_codegree_left_triples"],c6)
            n_saturated+=z["saturated_identical_two_right_witness_triangles"]
            n_productive+=z["productive_double_codegree_triangles"]
        self.assertGreater(n_saturated,0)
        self.assertGreater(n_productive,0)

    def test_all_4096_simple_3_by_4_bipartite_graphs(self):
        # Includes many configurations with singleton pair witnesses,
        # strong K3,2 saturation and strong productive triangles.
        n_saturated=n_productive=n_strong=0
        for mask in range(1<<12):
            graph=graph_from_mask(3,4,mask)
            z=exact_double_codegree_triangle_stability(graph)
            c6=exact_bipartite_codegree_trace(graph,verify_by_dfs=True)[
                "exact_ordinary_C6"]
            self.assertLessEqual(
                z["direct_exact_C6_on_double_codegree_left_triples"],c6)
            self.assertLessEqual(z["all_h_stable_C6_lower"],c6)
            n_saturated+=z["saturated_identical_two_right_witness_triangles"]
            n_productive+=z["productive_double_codegree_triangles"]
            n_strong+=z["triple_codegree_triangle_count"]
        self.assertGreater(n_saturated,0)
        self.assertGreater(n_productive,0)
        self.assertGreater(n_strong,0)

    def test_real_original_W32_two_complete_fixed_injections(self):
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            z=true_original_source_coherent_Hall_certificate(
                1,model["left_labels"],model["right_labels"],Fraction(1,2))
            self.assertTrue(z["original_source_provenance_verified"])
            self.assertTrue(z["two_physical_coordinate_cuts_verified"])
            self.assertEqual(
                z["total_C6_independent_right_collision_trace"],
                z["original_source_GF5_accepted_D6"])
            self.assertLessEqual(
                z["all_h_stable_C6_lower"],
                z["original_source_GF5_accepted_D6"])
            self.assertFalse(z["all_h_root_sevenclass_Omega_s6_proved"])

    def test_true_original_W34_adversarial_complete_injection(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        z=true_original_source_coherent_Hall_certificate(
            2,cert["f"],cert["g"],Fraction(1))
        self.assertEqual(
            z["total_C6_independent_right_collision_trace"],
            z["original_source_GF5_accepted_D6"])
        self.assertLessEqual(
            z["all_h_stable_C6_lower"],
            z["original_source_GF5_accepted_D6"])

    def test_true_original_W34_protected_16_flags_and_96_accepted_D6(self):
        f,g,source_ids=planted_original_k44()
        z=true_original_source_coherent_Hall_certificate(
            2,f,g,Fraction(1,4),source_subset=source_ids)
        self.assertEqual(z["retained_true_original_source_IDs"],16)
        self.assertEqual(z["original_source_GF5_accepted_D6"],96)
        self.assertEqual(
            z["direct_exact_C6_on_double_codegree_left_triples"],96)
        self.assertEqual(z["all_h_stable_C6_lower"],24)
        self.assertTrue(z["original_source_provenance_verified"])

    def test_malformed_non_bipartite_rejection(self):
        u,v,w=(0,0),(0,1),(1,0)
        g={u:{v,w},v:{u,w},w:{u,v}}
        with self.assertRaises(ValueError):
            exact_double_codegree_triangle_stability(g)
        with self.assertRaises(ValueError):
            exact_double_codegree_triangle_stability({u:{v},v:set()})


if __name__=="__main__":
    unittest.main()
