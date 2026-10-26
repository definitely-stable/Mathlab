"""AA4-C6TRACE: independent exact codegree correction and genuine source tests."""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import planted_original_k44
from hyp105_coherent_c6_codegree_trace import (
    exact_bipartite_codegree_trace,
    independent_simple_C6_DFS,
    source_selected_codegree_certificate,
)


def graph_from_edges(edges,vertices=()):
    g={v:set() for v in vertices}
    for a,b in edges:
        g.setdefault(a,set()).add(b)
        g.setdefault(b,set()).add(a)
    return g


class TestCoherentC6CodegreeTrace(unittest.TestCase):
    def test_empty_forest_and_proper_bipartite_examples(self):
        empty=exact_bipartite_codegree_trace({},verify_by_dfs=True)
        self.assertEqual(empty["exact_ordinary_C6"],0)
        star=graph_from_edges([((0,0),(1,i)) for i in range(3)])
        z=exact_bipartite_codegree_trace(star,verify_by_dfs=True)
        self.assertEqual(z["exact_ordinary_C6"],0)
        self.assertEqual(z["trace_K_cubed_div_six"],0)
        K33=graph_from_edges(
            [((0,i),(1,j)) for i in range(3) for j in range(3)]
        )
        z=exact_bipartite_codegree_trace(K33,verify_by_dfs=True)
        self.assertEqual((z["trace_K_cubed_div_six"],
                          z["exact_right_collision_correction"],
                          z["exact_ordinary_C6"]), (27,21,6))
        K44=graph_from_edges(
            [((0,i),(1,j)) for i in range(4) for j in range(4)]
        )
        z=exact_bipartite_codegree_trace(K44,verify_by_dfs=True)
        self.assertEqual(z["exact_ordinary_C6"],96)

    def test_all_512_bipartite_3_by_3_graphs(self):
        L=tuple((0,i) for i in range(3))
        R=tuple((1,i) for i in range(3))
        choices=tuple((a,b) for a in L for b in R)
        for mask in range(1<<len(choices)):
            edges=(edge for i,edge in enumerate(choices) if mask>>i&1)
            g=graph_from_edges(edges,vertices=L+R)
            z=exact_bipartite_codegree_trace(g,verify_by_dfs=True)
            self.assertGreaterEqual(z["trace_K_cubed_div_six"],
                                    z["exact_right_collision_correction"])
            self.assertEqual(z["independent_C6_DFS"],
                             z["exact_ordinary_C6"])
            if mask==(1<<len(choices))-1:
                self.assertEqual(z["exact_ordinary_C6"],6)

    def test_real_source_W32_W34_GQ_Levi_is_density_only_no_go(self):
        for power in (1,2):
            s=1<<power
            _,points,lines,flags=symplectic_gq(power)
            g=graph_from_edges(
                (((0,p),(1,l)) for p,l in flags),
                vertices=tuple((0,p) for p in range(len(points)))+
                         tuple((1,l) for l in range(len(lines)))
            )
            z=exact_bipartite_codegree_trace(g,verify_by_dfs=True)
            self.assertEqual(z["edges"],(s+1)*(s+1)*(s*s+1))
            self.assertEqual(z["exact_ordinary_C6"],0)
            self.assertEqual(
                z["trace_K_cubed_div_six"],
                z["exact_right_collision_correction"]
            )
            self.assertGreater(z["trace_K_cubed_div_six"],0)
            # These Levi graphs are NOT asserted to be feasible physical
            # subgraphs under the source-paired coordinate model.

    def test_actual_original_W32_W34_full_maps_and_two_cuts(self):
        checked=0
        for power in (1,2):
            for scheme in ("lex","reverse-line"):
                m=pair_labeled_symplectic(power,scheme)
                for threshold in (Fraction(1,2),Fraction(2)):
                    with self.subTest(power=power,scheme=scheme,T=threshold):
                        z=source_selected_codegree_certificate(
                            power,m["left_labels"],m["right_labels"],
                            threshold)
                        self.assertEqual(
                            z["exact_ordinary_C6"],
                            z["prior_accepted_original_D6"])
                        self.assertTrue(z["both_original_diagonals_retained"])
                        self.assertTrue(z["genuine_original_GF5_D6_checked"])
                        self.assertFalse(
                            z["all_h_universal_seven_class_Omega_s6_proved"])
                        checked+=1
        self.assertEqual(checked,8)

    def test_W34_actual_original_adversarial_full_map(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        z=source_selected_codegree_certificate(
            2,cert["f"],cert["g"],Fraction(1))
        self.assertEqual(z["exact_ordinary_C6"],
                         z["prior_accepted_original_D6"])
        self.assertTrue(z["genuine_original_GF5_D6_checked"])

    def test_real_W34_protected_four_by_four_original_96_D6(self):
        f,g,ids=planted_original_k44()
        z=source_selected_codegree_certificate(
            2,f,g,Fraction(1,4),source_subset=ids)
        self.assertEqual(z["complete_original_source_ID_count"],16)
        self.assertEqual(z["exact_ordinary_C6"],96)
        self.assertEqual(z["prior_accepted_original_D6"],96)
        self.assertEqual(z["independent_C6_DFS"],96)

    def test_reject_nonsimple_nonbipartite_malformed_edges(self):
        u,v,w=(0,0),(0,1),(1,0)
        with self.assertRaises(ValueError):
            exact_bipartite_codegree_trace({u:{v},v:set()})
        with self.assertRaises(ValueError):
            exact_bipartite_codegree_trace({u:{u}})
        with self.assertRaises(ValueError):
            exact_bipartite_codegree_trace(
                graph_from_edges(((u,v),(v,w),(w,u))))
        with self.assertRaises(ValueError):
            exact_bipartite_codegree_trace({"bad":set()})


if __name__=="__main__":
    unittest.main()
