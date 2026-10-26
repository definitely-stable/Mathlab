"""AA4-COMP exact true-original W(3,2)/W(3,4) wedge completion kernel."""
import json
from fractions import Fraction
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_local_return_completion_kernel import (
    returning_wedge_completion_kernel,
    independent_four_path_dfs,
    original_wedge_completion_profile,
)


class TestLocalReturnCompletionKernel(unittest.TestCase):
    def test_single_sixcycle_and_strict_vertex_exclusion(self):
        # Six distinct actual physical corners, first-coordinate
        # return a[0] == c[0], all physical arcs change BOTH axes.
        a,b,c,d,e,f = (
            (0,0), (1,1), (0,2), (2,3), (3,4), (4,5)
        )
        vertices=(a,b,c,d,e,f)
        graph={v:set() for v in vertices}
        for i,v in enumerate(vertices):
            nxt=vertices[(i+1)%6]
            graph[v].add(nxt)
            graph[nxt].add(v)
        self.assertEqual(returning_wedge_completion_kernel(graph,a,b,c),1)
        self.assertEqual(independent_four_path_dfs(graph,a,b,c),1)
        self.assertEqual(returning_wedge_completion_kernel(graph,c,b,a),1)
        graph[d].remove(e)
        graph[e].remove(d)
        self.assertEqual(returning_wedge_completion_kernel(graph,a,b,c),0)
        self.assertEqual(independent_four_path_dfs(graph,a,b,c),0)
        with self.assertRaises(ValueError):
            returning_wedge_completion_kernel(graph,a,b,d)
        with self.assertRaises(ValueError):
            returning_wedge_completion_kernel(graph,a,b,a)

    def test_true_original_w32_lex_and_reverse_labelings(self):
        cases=(
            ("lex",(64,52,586,493,28,26,7956,6717,64,51)),
            ("reverse-line",(42,52,352,372,28,16,4166,3208,42,51)),
        )
        keys=("J_x","J_y","W2_x","W2_y",
              "max_completion_x","max_completion_y",
              "sum_squared_completion_x","sum_squared_completion_y",
              "nonzero_completion_wedges_x",
              "nonzero_completion_wedges_y")
        for scheme,expected in cases:
            with self.subTest(scheme=scheme):
                model=pair_labeled_symplectic(1,scheme)
                result=original_wedge_completion_profile(
                    1,model["left_labels"],model["right_labels"],
                    verify_independent_c6=True)
                self.assertEqual(tuple(result[key] for key in keys),
                                 expected)
                self.assertEqual(
                    Fraction(result["mean_completion_x"]),
                    Fraction(result["W2_x"],result["J_x"]))
                self.assertEqual(
                    Fraction(result["mean_completion_y"]),
                    Fraction(result["W2_y"],result["J_y"]))
                self.assertGreaterEqual(
                    result["independent_sample_checks"]["x"],expected[0])
                self.assertGreaterEqual(
                    result["independent_sample_checks"]["y"],expected[1])
                self.assertTrue(result["all_h_kernel_identity_proved"])
                self.assertFalse(result["all_h_average_O_s_completion_proved"])

    def test_true_w34_full_original_symplectic_adversarial_map(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        result=original_wedge_completion_profile(
            2,cert["f"],cert["g"],verify_independent_c6=True)
        self.assertEqual((
            result["J_x"],result["J_y"],
            result["W2_x"],result["W2_y"],
            result["max_completion_x"],result["max_completion_y"],
            result["sum_squared_completion_x"],
            result["sum_squared_completion_y"],
            result["nonzero_completion_wedges_x"],
            result["nonzero_completion_wedges_y"],
        ),(624,602,15438,14756,71,86,484084,459984,624,602))
        self.assertEqual(
            Fraction(result["mean_completion_x"]),Fraction(2573,104))
        self.assertEqual(
            Fraction(result["mean_completion_y"]),Fraction(7378,301))
        self.assertGreaterEqual(result["independent_sample_checks"]["x"],12)
        self.assertGreaterEqual(result["independent_sample_checks"]["y"],12)
        for axis in ("x","y"):
            witness=result["maximizer_"+axis]
            self.assertEqual(len(witness["three_physical_corners"]),3)
            self.assertEqual(len(set(witness["two_genuine_source_flag_ids"])),2)
            self.assertEqual(len(witness["two_original_source_flags"]),2)
        self.assertFalse(result["all_h_uniform_O_s_completion_proved"])
        self.assertFalse(result["root_sevenclass_proved"])

    def test_coordinate_relabeling_invariant_profile(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        f,g=model["left_labels"],model["right_labels"]
        base=original_wedge_completion_profile(
            1,f,g,verify_independent_c6=False)
        f2=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        g2=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        shifted=original_wedge_completion_profile(
            1,f2,g2,verify_independent_c6=False)
        for key in (
            "J_x","J_y","W2_x","W2_y",
            "max_completion_x","max_completion_y",
            "sum_squared_completion_x",
            "sum_squared_completion_y",
            "mean_completion_x","mean_completion_y"
        ):
            self.assertEqual(shifted[key],base[key])

    def test_invalid_finite_source_maps_fail_closed(self):
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        with self.assertRaises(ValueError):
            original_wedge_completion_profile(3,f,g)
        with self.assertRaises(ValueError):
            original_wedge_completion_profile(1,f[:-1],g)
        bad=list(f);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            original_wedge_completion_profile(1,bad,g)


if __name__ == "__main__":
    unittest.main()
