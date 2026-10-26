"""AA4-PC3: full original D6 using triangle of PAIR physical codegrees."""
import json
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_pair_codegree_triangle_d6 import exact_pair_codegree_triangle_d6
from test_hyp105_triple_codegree_d6_compensation import (
    _coherent_k44_source_witness,
)


class TestPairCodegreeTriangleD6(unittest.TestCase):
    def test_original_W32_two_schemes_exact_twofold_cycle_count(self):
        for scheme,total,sector in (
                ("lex",15,6),
                ("reverse-line",3,0)):
            with self.subTest(scheme=scheme):
                model=pair_labeled_symplectic(1,scheme)
                r=exact_pair_codegree_triangle_d6(
                    1,model["left_labels"],model["right_labels"],
                    verify_historical_gf5=True,verify_existing_C6_oracle=True)
                self.assertEqual(r["oriented_pair_codegree_witness_triples"],
                                 2*total)
                self.assertEqual(r["accepted_original_D6"],total)
                self.assertEqual(
                    r["accepted_original_D6_from_complete_K33"],sector)
                self.assertEqual(r["non_K33_accepted_original_D6"],
                                 total-sector)

    def test_W34_adversarial_without_ANY_coordinate_transverse_K33(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        r=exact_pair_codegree_triangle_d6(
            2,cert["f"],cert["g"],verify_historical_gf5=True,
            verify_existing_C6_oracle=True)
        self.assertEqual(r["accepted_original_D6"],4972)
        self.assertEqual(r["oriented_pair_codegree_witness_triples"],9944)
        self.assertEqual(r["accepted_original_D6_from_complete_K33"],0)
        self.assertEqual(r["non_K33_accepted_original_D6"],4972)
        self.assertGreater(r["candidate_hub_triangles"],0)
        self.assertFalse(r["root_Omega_s6_proved"])

    def test_source_W34_true_K44_coherent_gives_complete_K33s(self):
        f,g=_coherent_k44_source_witness()
        r=exact_pair_codegree_triangle_d6(
            2,f,g,verify_historical_gf5=True,
            verify_existing_C6_oracle=False)
        self.assertGreaterEqual(
            r["accepted_original_D6_from_complete_K33"],96)
        self.assertGreaterEqual(r["accepted_original_D6"],96)
        self.assertEqual(
            r["oriented_pair_codegree_witness_triples"],
            2*r["accepted_original_D6"])
        self.assertGreaterEqual(
            r["accepted_original_D6"],
            r["accepted_original_D6_from_complete_K33"])

    def test_true_W32_independent_coordinate_renaming(self):
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        before=exact_pair_codegree_triangle_d6(
            1,f,g,verify_existing_C6_oracle=False)
        f2=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        g2=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        after=exact_pair_codegree_triangle_d6(
            1,f2,g2,verify_existing_C6_oracle=False)
        for key in ("accepted_original_D6",
                    "accepted_original_D6_from_complete_K33",
                    "oriented_pair_codegree_witness_triples",
                    "non_K33_accepted_original_D6"):
            self.assertEqual(before[key],after[key])

    def test_full_original_injection_required(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        with self.assertRaises(ValueError):
            exact_pair_codegree_triangle_d6(3,f,g)
        with self.assertRaises(ValueError):
            exact_pair_codegree_triangle_d6(1,f[:-1],g)
        bad=list(g);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            exact_pair_codegree_triangle_d6(1,f,bad)


if __name__=="__main__":
    unittest.main()
