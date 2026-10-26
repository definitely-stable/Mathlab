"""AA4-RC6: independent physical 6-cycles vs original GF5 D6 joins."""
import json
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3b2_coincident_cycles import exact_coincident_c6
from hyp105_physical_rainbow_c6 import (
    build_original_physical_graph, exact_rainbow_c6_finite,
)
from hyp105_b1_symplectic import symplectic_gq
from hyp105_weighted_variance_transfer import witness_maps


class TestPhysicalRainbowC6(unittest.TestCase):
    def test_w32_two_schemes_match_existing_independent_D6_join(self):
        for scheme,triangles,total,D6,xonly,yonly in (
                ("lex",20,730,15,78,87),
                ("reverse-line",25,485,3,44,50)):
            with self.subTest(scheme=scheme):
                m = pair_labeled_symplectic(1,scheme)
                c = exact_rainbow_c6_finite(
                    1,m["left_labels"],m["right_labels"]
                )
                prior = exact_coincident_c6(m,witness_limit=0)
                self.assertEqual(c["D6_original_sixsets"],D6)
                self.assertEqual(
                    c["D6_original_sixsets"],
                    prior["exact_coincident_C6_factor_matchings_D"],
                )
                self.assertEqual(c["physical_triangles"],triangles)
                self.assertEqual(c["physical_simple_C6"],total)
                self.assertEqual(c["nonrainbow_coordinate_defect"],total-D6)
                self.assertEqual(c["x_distinct_physical_C6"],xonly)
                self.assertEqual(c["y_distinct_physical_C6"],yonly)
                self.assertTrue(c["GF5_source_classifier_checked"])
                self.assertFalse(c["universal_D6_Omega_s6_proved"])

    def test_true_w34_adversarial_source_sixsets_reconstructed_uniquely(self):
        cert = json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        c = exact_rainbow_c6_finite(2,cert["f"],cert["g"])
        self.assertEqual((c["V"],c["a"],c["original_source_flags"],
                          c["physical_undirected_edges"]),(85,14,425,850))
        self.assertEqual((c["physical_triangles"],c["physical_simple_C6"],
                          c["D6_original_sixsets"],
                          c["nonrainbow_coordinate_defect"],
                          c["x_distinct_physical_C6"],
                          c["y_distinct_physical_C6"]),
                         (87,30306,4972,25334,12700,13193))
        self.assertEqual(c["exact_12D6_squarefree_physical_closed_walks"],
                         12*4972)
        # Exact all-cycle finite partition, not an extrapolated floor.
        self.assertEqual(c["x_only_repeat_C6"]+
                         c["y_only_repeat_C6"]+
                         c["both_repeat_C6"],25334)

    def test_independent_physical_coordinate_relabeling_invariance(self):
        m = pair_labeled_symplectic(1,"reverse-line")
        left,right = m["left_labels"],m["right_labels"]
        original = exact_rainbow_c6_finite(1,left,right)
        left2 = [tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in left]
        right2 = [tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in right]
        permuted = exact_rainbow_c6_finite(1,left2,right2)
        self.assertEqual(permuted,original)

    def test_true_original_flags_build_simple_loopless_physical_graph(self):
        _,_,_,flags = symplectic_gq(1)
        f,g = witness_maps(41)
        adjacency,arc_flag = build_original_physical_graph(2,f,g,flags)
        self.assertEqual(len(arc_flag),4*45)
        self.assertEqual(sum(map(len,adjacency.values())),4*45)
        self.assertEqual(set(arc_flag.values()),set(range(45)))
        for (v,w),source_id in arc_flag.items():
            self.assertEqual(arc_flag[w,v],source_id)
            self.assertIn(w,adjacency[v])
            self.assertNotEqual(v,w)

    def test_incomplete_injective_flags_or_power_fail_closed(self):
        f,g = witness_maps(41)
        _,_,_,flags = symplectic_gq(1)
        with self.assertRaises(ValueError):
            exact_rainbow_c6_finite(3,f,g)
        with self.assertRaises(ValueError):
            exact_rainbow_c6_finite(1,f[:-1],g)
        wrong=list(f)
        wrong[0]=wrong[1]
        with self.assertRaises(ValueError):
            exact_rainbow_c6_finite(1,wrong,g)
        with self.assertRaises(ValueError):
            build_original_physical_graph(2,f,g,flags[:-1])


if __name__=="__main__":
    unittest.main()
