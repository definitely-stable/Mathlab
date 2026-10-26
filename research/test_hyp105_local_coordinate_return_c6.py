"""AA4-LCR: exact W(3,2)/W(3,4) local physical coordinate defects."""
import json
from pathlib import Path
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_local_coordinate_return_c6 import (
    canonical_return_signature, original_coordinate_return_census,
)
from hyp105_weighted_variance_transfer import witness_maps


class TestLocalCoordinateReturnC6(unittest.TestCase):
    def test_original_real_w32_both_complete_k6_schemes(self):
        baselines=(
            ("lex", (730,15,715,634,81,468,404,308,345,677,38)),
            ("reverse-line", (485,3,482,422,60,266,297,237,214,451,31)),
        )
        names=(
            "simple_C6","D6_rainbow","defect_C6",
            "two_step_return_defect","pure_three_step_return_defect",
            "x_two_step_defect","y_two_step_defect",
            "x_three_step_defect","y_three_step_defect",
            "six_distinct_source_flags_defect",
            "repeated_source_flag_defect",
        )
        for scheme,expected in baselines:
            with self.subTest(scheme=scheme):
                old=pair_labeled_symplectic(1,scheme)
                c=original_coordinate_return_census(
                    1,old["left_labels"],old["right_labels"],
                    check_independent=True
                )
                self.assertEqual(tuple(c[name] for name in names),expected)
                self.assertEqual(sum(c["return_signature_counts"].values()),
                                 expected[0])
                self.assertFalse(c["root_all_seven_lower_proved"])

    def test_genuine_w34_source_id_distinct_defect_falsifier(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        c=original_coordinate_return_census(
            2,cert["f"],cert["g"],check_independent=True
        )
        self.assertEqual((
            c["simple_C6"],c["D6_rainbow"],c["defect_C6"],
            c["two_step_return_defect"],c["pure_three_step_return_defect"],
            c["x_two_step_defect"],c["y_two_step_defect"],
            c["x_three_step_defect"],c["y_three_step_defect"],
            c["six_distinct_source_flags_defect"],
            c["repeated_source_flag_defect"],
        ),(30306,4972,25334,20869,4465,12987,12531,5620,5620,
           25182,152))
        self.assertGreater(c["six_distinct_source_flags_defect"],
                           99*c["defect_C6"]//100)
        self.assertEqual(c["return_signature_counts"]["0,0,0,0"],4972)
        self.assertEqual(c["return_signature_counts"]["1,0,0,0"],4695)
        self.assertEqual(c["return_signature_counts"]["0,0,1,0"],4395)

    def test_local_returns_are_intrinsically_coordinate_separated(self):
        # A legitimate simple hexagon can have an x-backtrack and a
        # different y-backtrack, but not both at the SAME position.
        cycle=((0,0),(1,1),(0,2),(2,3),(3,2),(2,1))
        bx,tx,by,ty=canonical_return_signature(cycle)
        self.assertGreaterEqual(bx,1)
        self.assertGreaterEqual(by,1)
        self.assertEqual((bx>0 or by>0 or tx>0 or ty>0),True)
        with self.assertRaises(ValueError):
            canonical_return_signature(cycle[:-1])
        with self.assertRaises(ValueError):
            canonical_return_signature(cycle[:5]+(cycle[0],))
        with self.assertRaises(ValueError):
            canonical_return_signature(
                ((0,0),(0,1),(2,2),(3,3),(4,4),(5,5))
            )

    def test_original_mapping_validation_fail_closed(self):
        f,g=witness_maps(41)
        with self.assertRaises(ValueError):
            original_coordinate_return_census(3,f,g)
        with self.assertRaises(ValueError):
            original_coordinate_return_census(1,f[:-1],g)
        bad=list(g);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            original_coordinate_return_census(1,f,bad)

    def test_independent_physical_coordinate_permutations(self):
        m=pair_labeled_symplectic(1,"reverse-line")
        f,g=m["left_labels"],m["right_labels"]
        base=original_coordinate_return_census(1,f,g,check_independent=False)
        f2=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        g2=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        other=original_coordinate_return_census(1,f2,g2,
                                                 check_independent=False)
        self.assertEqual(other,base)


if __name__=="__main__":
    unittest.main()
