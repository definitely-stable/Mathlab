"""AA4-SPW: genuine source GQ spectral star-pencil wedge cap and falsifiers."""
import json
from pathlib import Path
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_source_spectral_pencil_wedges import (
    original_line_collinearity_polynomial, original_spectral_pencil_cap,
)


class TestSourceSpectralPencilWedges(unittest.TestCase):
    def test_source_line_collinearity_integer_polynomial_both_GQ_fields(self):
        for power in (1,2):
            s=1<<power
            _,points,lines,flags=symplectic_gq(power)
            certificate=original_line_collinearity_polynomial(s,flags)
            self.assertEqual(certificate["V"],len(points))
            self.assertEqual(certificate["V"],len(lines))
            self.assertEqual(certificate["source_line_collinearity_degree"],
                             s*(s+1))
            self.assertEqual(certificate["nontrivial_positive_eigenvalue"],
                             s-1)
            self.assertEqual(certificate["nontrivial_negative_eigenvalue"],
                             -(s+1))
            self.assertTrue(
                certificate["integer_collinearity_polynomial_checked"])

    def test_original_W32_lex_and_reverse_exact_integer_spectral_caps(self):
        _,_,_,flags=symplectic_gq(1)
        for scheme,jx,jy in (("lex",64,52),("reverse-line",42,52)):
            with self.subTest(scheme=scheme):
                m=pair_labeled_symplectic(1,scheme)
                result=original_spectral_pencil_cap(
                    2,m["left_labels"],m["right_labels"],flags
                )
                self.assertEqual((
                    result["J_x"],result["J_y"],
                    result["original_point_coordinate_degree_square_sum"],
                    result["original_line_coordinate_degree_square_sum"],
                    result["x_spectral_bound_numerator"],
                    result["y_spectral_bound_numerator"],
                    result["spectral_bound_denominator"],
                    result["universal_each_axis_integer_bound"],
                    result["previous_each_axis_pencil_bound"],
                ),(jx,jy,150,150,1200,1200,15,80,90))
                self.assertEqual(
                    (result["independent_original_collinear_pair_x"],
                     result["independent_original_collinear_pair_y"]),
                    (jx,jy))
                self.assertTrue(result["all_h_O_s4_pencil_wedge_upper_proved"])
                self.assertFalse(result["all_h_average_O_s2_completion_proved"])

    def test_original_W34_adversarial_exact_integer_spectral_caps(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        _,_,_,flags=symplectic_gq(2)
        result=original_spectral_pencil_cap(
            4,cert["f"],cert["g"],flags
        )
        self.assertEqual((
            result["J_x"],result["J_y"],
            result["original_point_coordinate_degree_square_sum"],
            result["original_line_coordinate_degree_square_sum"],
            result["x_spectral_bound_numerator"],
            result["y_spectral_bound_numerator"],
            result["spectral_bound_denominator"],
            result["universal_each_axis_integer_bound"],
            result["previous_each_axis_pencil_bound"],
        ),(624,602,2090,2076,78642,78880,85,952,1700))
        self.assertEqual(
            (result["independent_original_collinear_pair_x"],
             result["independent_original_collinear_pair_y"]),
            (624,602))
        self.assertLess(result["x_spectral_bound_numerator"],
                        624*1700)
        self.assertLess(result["y_spectral_bound_numerator"],
                        602*1700)
        self.assertFalse(result["root_sevenclass_proved"])

    def test_physical_coordinate_permutation_invariance_of_spectral_data(self):
        _,_,_,flags=symplectic_gq(1)
        model=pair_labeled_symplectic(1,"reverse-line")
        f,g=model["left_labels"],model["right_labels"]
        before=original_spectral_pencil_cap(2,f,g,flags)
        ff=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        gg=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        after=original_spectral_pencil_cap(2,ff,gg,flags)
        for field in ("J_x","J_y",
                      "original_point_coordinate_degree_square_sum",
                      "original_line_coordinate_degree_square_sum",
                      "x_spectral_bound_numerator",
                      "y_spectral_bound_numerator",
                      "universal_each_axis_integer_bound"):
            self.assertEqual(before[field],after[field])

    def test_reject_non_gq_regular_switch_and_illegal_maps(self):
        _,_,_,flags=symplectic_gq(1)
        original=set(flags)
        # A two-edge switch retains EVERY original vertex degree 3,
        # but breaks GQ collinearity. Do not accept an arbitrary
        # regular substitute as the genuine symplectic geometry.
        change=None
        for p,l in flags:
            if change is not None:
                break
            for q,m in flags:
                if p!=q and l!=m and (p,m) not in original and (
                        q,l) not in original:
                    change=(p,l,q,m)
                    break
        self.assertIsNotNone(change)
        p,l,q,m=change
        altered=set(original)
        altered.remove((p,l))
        altered.remove((q,m))
        altered.add((p,m))
        altered.add((q,l))
        with self.assertRaises(AssertionError):
            original_line_collinearity_polynomial(2,tuple(sorted(altered)))
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        with self.assertRaises(ValueError):
            original_spectral_pencil_cap(3,f,g,flags)
        with self.assertRaises(ValueError):
            original_spectral_pencil_cap(2,f[:-1],g,flags)
        with self.assertRaises(ValueError):
            original_spectral_pencil_cap(2,f,g,flags[:-1])


if __name__=="__main__":
    unittest.main()
