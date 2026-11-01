"""AA4-GQSPECTRAL: true-original W32/W34 combinatorial spectrum and book."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_original_gq_incidence_spectral_kernel_referee import (
    minimum_alphabet,allh_original_GQ_spectrum_parameters,
    genuine_original_dual_spectral_book_referee,
)


def genuine_maps(h,step=1,shift=0):
    _,V,_=genuine_source(h)
    a=minimum_alphabet(V)
    palette=tuple(combinations(range(a),2))
    if len(palette)<V:raise AssertionError("source alphabet too small")
    return (
        tuple(palette[:V]),
        tuple(palette[(step*i+shift)%V] for i in range(V)),
    )


class OriginalSymplecticGQSpectrumKernel(unittest.TestCase):
    def test_all_h_closed_form_srg_incidence_spectrum_multiplicities(self):
        for h in range(1,29):
            s=2**h
            z=allh_original_GQ_spectrum_parameters(s)
            V=z["V"]
            self.assertEqual(z["flags"],(s+1)*V)
            self.assertEqual(z["collinearity_degree"],s*(s+1))
            self.assertEqual(z["collinearity_lambda"],s-1)
            self.assertEqual(z["collinearity_mu"],s+1)
            self.assertEqual(z["incidence_BBt_nonzero_eigenvalues"],
                             ((s+1)**2,2*s))
            self.assertEqual(z["incidence_BBt_multiplicities"],
                             (1,s*(s+1)**2//2,s*(s*s+1)//2))
            self.assertEqual(z["kernel_dimension"],s*(s*s+1)//2)
            self.assertEqual(sum(z["incidence_BBt_multiplicities"]),V)
            self.assertTrue(z["source_spectral_positive_semidefinite"])

    def test_W32_exact_full_spectrum_pencils_dual_and_kernel_slack(self):
        s,V,flags=genuine_source(1)
        self.assertEqual((s,V,len(flags)),(2,15,45))
        for step,shift in ((1,0),(1,3),(2,1),(7,4)):
            f,g=genuine_maps(1,step,shift)
            z=genuine_original_dual_spectral_book_referee(1,f,g)
            self.assertTrue(z["true_original_GQ_srg_axioms_independently_verified"])
            self.assertEqual(z["original_full_flag_ID_count"],45)
            self.assertEqual(z["minimal_alphabet_a"],6)
            for key in ("right_g_line_factor_point_pencil_book",
                        "left_f_point_factor_line_pencil_book"):
                m=z[key]
                self.assertEqual(m["missing_legal_pair_labels"],0)
                self.assertEqual(m["unused_pair_star_defect"],0)
                self.assertEqual(m["original_full_book_actual_M"],
                                 m["original_full_book_pair_major_M"])
                self.assertEqual(m["Cs_minus_actual_M_exact"],
                                 2*m["spectral_kernel_mass"])
                self.assertGreaterEqual(m["spectral_kernel_mass"],0)
                self.assertEqual(m["original_full_book_actual_M"]
                                 +m["Cs_minus_actual_M_exact"],
                                 m["algebraic_Cs"])
                self.assertTrue(
                    m["all_source_projectors_are_exact_original_kernel_projections"])

    def test_W34_exact_missing_six_pair_labels_strict_positive_gap(self):
        s,V,flags=genuine_source(2)
        self.assertEqual((s,V,len(flags)),(4,85,425))
        for step,shift in ((1,0),(1,11),(19,7),(21,13)):
            f,g=genuine_maps(2,step,shift)
            z=genuine_original_dual_spectral_book_referee(2,f,g)
            self.assertEqual(z["minimal_alphabet_a"],14)
            self.assertEqual(z["source_incidence_spectrum"]["kernel_dimension"],34)
            for key in ("right_g_line_factor_point_pencil_book",
                        "left_f_point_factor_line_pencil_book"):
                m=z[key]
                self.assertEqual(m["missing_legal_pair_labels"],6)
                self.assertGreater(m["unused_pair_star_defect"],0)
                self.assertGreater(m["Cs_minus_actual_M_exact"],Fraction(42,5))
                self.assertEqual(m["universal_unused_pairs_extra_gap"],
                                 Fraction(42,5))
                self.assertEqual(m["algebraic_Cs"],476)
                self.assertLessEqual(m["original_full_book_actual_M"],467)
                self.assertEqual(m["original_full_book_actual_M"],
                                 m["original_full_book_pair_major_M"])
                self.assertEqual(m["Cs_minus_actual_M_exact"],
                                 m["Cs_minus_actual_spectral_identity"])
                self.assertGreaterEqual(m["spectral_kernel_mass"],0)
                self.assertTrue(m["strict_extra_gap_if_missing"])

    def test_W32_W34_original_CORE_subsets_versus_FULL_source_books(self):
        for h in (1,2):
            s,V,flags=genuine_source(h)
            for step,shift in ((1,0),(19,3)):
                f,g=genuine_maps(h,step,shift)
                for core in ((),
                             tuple(i for i in range(len(flags)) if i%2),
                             tuple(i for i in range(len(flags)) if i%7==0)):
                    z=genuine_original_dual_spectral_book_referee(
                        h,f,g,core)
                    self.assertEqual(z["original_CORE_flag_ID_count"],len(core))
                    m_f=z["restricted_original_source_pencil_conflicts_Mf"]
                    m_g=z["restricted_original_source_pencil_conflicts_Mg"]
                    self.assertLessEqual(m_f,
                        z["left_f_point_factor_line_pencil_book"]["original_full_book_actual_M"])
                    self.assertLessEqual(m_g,
                        z["right_g_line_factor_point_pencil_book"]["original_full_book_actual_M"])
                    self.assertEqual(
                        z["restricted_original_SOURCE_conflict_edges"],m_f+m_g)
                    if not core:
                        self.assertEqual((m_f,m_g),(0,0))

    def test_original_book_slack_deficiency_is_exact_rational_both_sides(self):
        f,g=genuine_maps(2,19,1)
        z=genuine_original_dual_spectral_book_referee(2,f,g)
        for key in ("right_g_line_factor_point_pencil_book",
                    "left_f_point_factor_line_pencil_book"):
            b=z[key]
            s,V,a=z["s"],z["V"],z["minimal_alphabet_a"]
            ksq=b["label_star_squares"]
            self.assertEqual(b["unused_pair_star_defect"],
                             2*V*(a-1)-ksq)
            self.assertEqual(b["spectral_base_before_kernel"],
                             Fraction((s-1)*V)
                              +Fraction(s*s+1,2*V)*ksq)
            self.assertEqual(b["spectral_base_before_kernel"]
                             -s*b["spectral_kernel_mass"],
                             b["original_full_book_actual_M"])
            gap=(Fraction(s*s+1,2*V)*b["unused_pair_star_defect"]
                 +s*b["spectral_kernel_mass"])
            self.assertEqual(gap,b["Cs_minus_actual_M_exact"])

    def test_fail_closed_invalid_original_maps_core_and_nondyadic(self):
        for s in (0,1,3,6,64.0,True,-2):
            with self.assertRaises(ValueError):
                allh_original_GQ_spectrum_parameters(s)
        for V in (0,1.1,True,-3):
            with self.assertRaises(ValueError):
                minimum_alphabet(V)
        f,g=genuine_maps(1)
        _,_,flags=genuine_source(1)
        for h,ff,gg,core in (
            (3,f,g,None),(0,f,g,None),
            (1,f[:-1],g,None),
            (1,(f[0],)*len(f),g,None),
            (1,f,g,(0,0)),
            (1,f,g,(True,)),
            (1,f,g,(len(flags),)),
        ):
            with self.assertRaises(ValueError):
                genuine_original_dual_spectral_book_referee(
                    h,ff,gg,core)


if __name__=="__main__":
    unittest.main()
