"""AA4-LCR-W: independent source-pencil vs physical-corner wedges."""
import json
from pathlib import Path
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_source_pencil_wedges import original_source_pencil_wedges
from hyp105_weighted_variance_transfer import witness_maps


class TestOriginalSourcePencilWedges(unittest.TestCase):
    def test_true_w32_two_full_labelings_and_both_independent_methods(self):
        _,_,_,flags=symplectic_gq(1)
        for scheme,expected in (
            ("lex",(64,52,90,3,3)),
            ("reverse-line",(42,52,90,2,3)),
        ):
            with self.subTest(scheme=scheme):
                m=pair_labeled_symplectic(1,scheme)
                result=original_source_pencil_wedges(
                    2,m["left_labels"],m["right_labels"],flags
                )
                self.assertEqual((
                    result["Jx_point_pencil_two_edge_wedges"],
                    result["Jy_line_pencil_two_edge_wedges"],
                    result["individual_axis_upper_V_s_s_plus_1"],
                    result["maximum_source_point_pencil_symbol_degree"],
                    result["maximum_source_line_pencil_symbol_degree"],
                ),expected)
                self.assertEqual(
                    result["Jx_direct_physical"],expected[0])
                self.assertEqual(
                    result["Jy_direct_physical"],expected[1])
                self.assertTrue(result["all_h_wedge_upper_O_s5_proved"])
                self.assertFalse(result["C6_completion_average_bound_proved"])

    def test_true_w34_existing_global_injection_original_source_pencils(self):
        _,_,_,flags=symplectic_gq(2)
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        result=original_source_pencil_wedges(4,cert["f"],cert["g"],flags)
        self.assertEqual((
            result["Jx_point_pencil_two_edge_wedges"],
            result["Jy_line_pencil_two_edge_wedges"],
            result["individual_axis_upper_V_s_s_plus_1"],
            result["maximum_source_point_pencil_symbol_degree"],
            result["maximum_source_line_pencil_symbol_degree"],
        ),(624,602,1700,5,5))
        self.assertEqual(result["Jx_direct_physical"],624)
        self.assertEqual(result["Jy_direct_physical"],602)

    def test_independent_coordinate_permutations_preserve_original_wedges(self):
        _,_,_,flags=symplectic_gq(1)
        f,g=witness_maps(41)
        first=original_source_pencil_wedges(2,f,g,flags)
        f2=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        g2=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        second=original_source_pencil_wedges(2,f2,g2,flags)
        self.assertEqual(first,second)

    def test_invalid_source_or_injection_fail_closed(self):
        _,_,_,flags=symplectic_gq(1)
        f,g=witness_maps(41)
        with self.assertRaises(ValueError):
            original_source_pencil_wedges(3,f,g,flags)
        with self.assertRaises(ValueError):
            original_source_pencil_wedges(2,f[:-1],g,flags)
        with self.assertRaises(ValueError):
            original_source_pencil_wedges(2,f,g,flags[:-1])
        bad=list(g)
        bad[0]=bad[1]
        with self.assertRaises(ValueError):
            original_source_pencil_wedges(2,f,bad,flags)


if __name__=="__main__":
    unittest.main()
