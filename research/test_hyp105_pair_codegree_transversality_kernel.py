"""HYP-105 #230 AA4-PTK: exact pair-list transversality kernel and certificate."""
import json
from itertools import product
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_pair_codegree_transversality_kernel import (
    pair_coordinate_collisions,
    exact_transverse_three_list_kernel,
    original_pair_codegree_transversality_profile,
)
from test_hyp105_triple_codegree_d6_compensation import (
    _coherent_k44_source_witness,
)


class TestPairCodegreeTransversalityKernel(unittest.TestCase):
    def test_exact_algebra_and_source_free_typed_set_falsifiers(self):
        A=((0,0),(1,1))
        B=((1,2),(2,3))
        C=((3,4),(4,5))
        z=exact_transverse_three_list_kernel(A,B,C,check_symmetry=True)
        self.assertEqual(z["raw_pair_codegree_product"],8)
        self.assertEqual(z["cross_pairs_AB_colliding"],1)
        self.assertEqual(z["cross_pairs_AB_valid"],3)
        self.assertEqual(z["exact_coordinate_transverse_triples"],6)
        self.assertEqual(z["exact_coordinate_collision_loss"],2)
        self.assertEqual(z["union_collision_lower"],6)
        self.assertEqual(z["certified_lower"],6)
        # Same physical corner in two different lists contributes to
        # both x and y collisions but must be subtracted ONCE.
        self.assertEqual(
            pair_coordinate_collisions(((1,2),),((1,2),)),1
        )
        self.assertEqual(
            exact_transverse_three_list_kernel(
                ((1,2),),((1,2),),((3,4),),
                check_symmetry=True)["exact_coordinate_transverse_triples"],0
        )
        # Huge raw product yet no transversal triple: the coordinates
        # coincide on one side, so no accepted original D6 certificate.
        row=tuple((0,j) for j in range(9))
        z=exact_transverse_three_list_kernel(
            row,row,row,check_symmetry=True
        )
        self.assertEqual(z["raw_pair_codegree_product"],9**3)
        self.assertEqual(z["exact_coordinate_transverse_triples"],0)
        self.assertEqual(z["certified_lower"],0)

    def test_sequential_bound_not_just_union_bound(self):
        # Three blocks on disjoint coordinates: every triple accepted.
        A=tuple((i,i) for i in range(4))
        B=tuple((10+i,10+i) for i in range(4))
        C=tuple((20+i,20+i) for i in range(5))
        z=exact_transverse_three_list_kernel(
            A,B,C,check_symmetry=True
        )
        self.assertEqual(z["exact_coordinate_transverse_triples"],80)
        self.assertEqual(z["union_collision_lower"],80)
        self.assertEqual(z["certified_lower"],80)
        # Independently enumerate selected sparse subsets with overlaps.
        for n in (3,4):
            grid=tuple(product(range(n),repeat=2))
            for stride_a,stride_b,stride_c in (
                (1,2,3),(2,3,4),(2,4,5),(3,4,6)):
                with self.subTest(n=n,strides=(stride_a,stride_b,stride_c)):
                    A=grid[::stride_a]
                    B=grid[::stride_b]
                    C=grid[::stride_c]
                    p=exact_transverse_three_list_kernel(
                        A,B,C,check_symmetry=True)
                    self.assertLessEqual(
                        p["union_collision_lower"],
                        p["exact_coordinate_transverse_triples"])
                    self.assertLessEqual(
                        p["sequential_degree_lower"],
                        p["exact_coordinate_transverse_triples"])

    def test_genuine_W32_original_D6_with_exact_loss_conservation(self):
        for scheme,expected in (("lex",15),("reverse-line",3)):
            model=pair_labeled_symplectic(1,scheme)
            p=original_pair_codegree_transversality_profile(
                1,model["left_labels"],model["right_labels"],
                verify_full=True)
            with self.subTest(scheme=scheme):
                self.assertEqual(p["accepted_original_D6"],expected)
                self.assertEqual(
                    p["exact_coordinate_transverse_triples"],2*expected)
                self.assertEqual(
                    p["raw_pair_codegree_product"],
                    p["exact_coordinate_transverse_triples"]+
                    p["exact_coordinate_collision_loss"])
                self.assertLessEqual(
                    p["certified_original_D6_lower_numerator"],
                    2*expected)
                self.assertTrue(p["independent_genuine_source_D6_checked"])
                self.assertFalse(p["all_h_sevenclass_Omega_s6_proved"])

    def test_genuine_W34_adversarial_D6_without_K33(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        p=original_pair_codegree_transversality_profile(
            2,cert["f"],cert["g"],verify_full=True)
        self.assertEqual(p["accepted_original_D6"],4972)
        self.assertEqual(p["exact_coordinate_transverse_triples"],9944)
        self.assertGreaterEqual(p["raw_pair_codegree_product"],9944)
        self.assertGreaterEqual(
            p["raw_pair_codegree_product"],
            p["exact_coordinate_collision_loss"])
        self.assertGreaterEqual(
            p["independent_small_triangle_cubic_checks"],16)
        self.assertLessEqual(p["certified_lower"],9944)

    def test_genuine_W34_coherent_K44_source_16flags(self):
        f,g=_coherent_k44_source_witness()
        p=original_pair_codegree_transversality_profile(
            2,f,g,verify_full=False)
        self.assertGreaterEqual(p["accepted_original_D6"],96)
        self.assertGreaterEqual(
            p["exact_coordinate_transverse_triples"],192)
        self.assertLessEqual(p["certified_lower"],
                             p["exact_coordinate_transverse_triples"])

    def test_independent_coordinate_permutations_are_invariant(self):
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        baseline=original_pair_codegree_transversality_profile(
            1,f,g,verify_full=False)
        ff=[tuple(sorted(((5*x+1)%6,(5*y+1)%6))) for x,y in f]
        gg=[tuple(sorted(((5*x+2)%6,(5*y+2)%6))) for x,y in g]
        rotated=original_pair_codegree_transversality_profile(
            1,ff,gg,verify_full=False)
        for key in (
            "raw_pair_codegree_product",
            "exact_coordinate_transverse_triples",
            "exact_coordinate_collision_loss",
            "union_collision_lower",
            "sequential_degree_lower",
            "certified_lower",
            "accepted_original_D6",
        ):
            self.assertEqual(baseline[key],rotated[key])

    def test_fail_closed_inputs(self):
        with self.assertRaises(ValueError):
            exact_transverse_three_list_kernel(
                ((1,2),(1,2)),((3,4),),((5,6),))
        with self.assertRaises(ValueError):
            pair_coordinate_collisions(((1,-1),),((3,4),))
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        with self.assertRaises(ValueError):
            original_pair_codegree_transversality_profile(3,f,g)
        with self.assertRaises(ValueError):
            original_pair_codegree_transversality_profile(1,f[:-1],g)
        g2=list(g)
        g2[0]=g2[1]
        with self.assertRaises(ValueError):
            original_pair_codegree_transversality_profile(1,f,g2)


if __name__ == "__main__":
    unittest.main()
