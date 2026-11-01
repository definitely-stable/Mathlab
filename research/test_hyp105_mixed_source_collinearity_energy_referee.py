"""AA4-MIXENERGY — exact original point-book fourth-moment factor."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_mixed_source_collinearity_energy_referee import (
    allh_original_mixed_energy_envelope,
    original_mixed_source_energy_referee,
)
from hyp105_four_internal_blocker_weighted_referee import four_blocker_referee


def maps(power,shift=0,point_shift=0):
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    labels=tuple(combinations(range(a),2))[:V]
    return (
        tuple(labels[(19*i+point_shift)%V] for i in range(V)),
        tuple(labels[(19*i+shift)%V] for i in range(V))
    )


class TrueOriginalMixedSourceEnergy(unittest.TestCase):
    def test_exact_all_h_uniform_spectral_envelope_7_vs_old_64(self):
        for h in range(6,28):
            s=2**h
            r=allh_original_mixed_energy_envelope(s)
            self.assertLess(r["exact_rational_all_h_coeff_bound"],7)
            self.assertEqual(r["new_first_mixed_CS_factor_F1_upper_coefficient"],7)
            self.assertEqual(r["historical_F1_upper_coefficient"],64)
            self.assertEqual(r["F2_original_unchanged_coefficient"],32)
            self.assertEqual(r["new_B0_multiplier"],15)
            self.assertEqual(r["new_B0_over_old"],Fraction(15,64))
            self.assertEqual(15*15,225)
            self.assertGreaterEqual(15*15,7*32)

    def test_true_W32_full_source_all_arbitrary_correlated_maps(self):
        for shift in (0,1,3,7,11):
            with self.subTest(shift=shift):
                f,g=maps(1,shift)
                r=original_mixed_source_energy_referee(1,f,g)
                self.assertEqual(r["original_core_source_IDs"],45)
                self.assertEqual(r["actual_true_original_both_diagonals"],90)
                self.assertEqual(
                    r["original_mixed_phi"]-r["original_mixed_incident_psi"],
                    r["actual_source_mixed_nonincident_blocker_triples"])
                self.assertLessEqual(
                    r["original_source_first_factor_F1"],
                    2*r["source_collinearity_squared_energy"])
                self.assertGreaterEqual(r["source_index_restriction_loss"],0)
                self.assertEqual(
                    r["source_collinearity_squared_energy"],
                    r["source_collinearity_exact_anti_book_formula"])

    def test_true_W32_full_core_crosschecks_historical_independent_mixed_referee(self):
        f,g=maps(1,0)
        new=original_mixed_source_energy_referee(1,f,g)
        old=four_blocker_referee(1,f,g)
        for a,b in (("original_mixed_phi","phi"),
                    ("original_mixed_incident_psi","incident_defect"),
                    ("actual_source_mixed_nonincident_blocker_triples","blocked_triples")):
            self.assertEqual(new[a],old["primal"][b])
        self.assertEqual(new["actual_true_original_both_diagonals"],old["primal"]["edges"])

    def test_true_W32_original_core_sparse_and_empty_keeps_FULL_source(self):
        _,_,flags=genuine_source(1)
        f,g=maps(1,3)
        full=original_mixed_source_energy_referee(1,f,g)
        for core in ((),tuple(range(0,45,2)),
                     tuple(i for i in range(45) if i%4==0),
                     tuple(i for i in range(45) if i%5)):
            with self.subTest(core=len(core)):
                r=original_mixed_source_energy_referee(1,f,g,core)
                self.assertEqual(
                    r["source_collinearity_squared_energy"],
                    full["source_collinearity_squared_energy"])
                self.assertEqual(r["original_pencil_book_Mf"],
                                 full["original_pencil_book_Mf"])
                self.assertEqual(r["actual_true_original_both_diagonals"],2*len(core))
                self.assertEqual(
                    r["source_book_kernel_full_core_cross_Ksum"],
                    r["independent_physical_corner_degree_product"])
                self.assertLessEqual(
                    r["original_mixed_second_factor_F2"],
                    r["actual_mixed_K_max"]*
                    r["source_book_kernel_full_core_cross_Ksum"])
                if not core:
                    self.assertEqual(r["original_mixed_phi"],0)
                    self.assertEqual(r["original_mixed_second_factor_F2"],0)

    def test_true_W34_full_source_and_sparse_CORRELATED_maps(self):
        _,V,flags=genuine_source(2)
        for shift,point_shift,core in (
            (0,0,None),(7,3,tuple(range(0,425,2))),
            (19,7,tuple(i for i in range(425) if i%3==0)),
            (1,1,tuple(i for i in range(425) if i%7==0))
        ):
            with self.subTest(shift=shift,core=None if core is None else len(core)):
                f,g=maps(2,shift,point_shift)
                r=original_mixed_source_energy_referee(2,f,g,core)
                self.assertEqual(r["original_core_source_IDs"],
                                 len(flags) if core is None else len(core))
                self.assertEqual(r["source_collinearity_squared_energy"],
                                 r["source_collinearity_exact_anti_book_formula"])
                self.assertTrue(r["exact_direct_first_cauchy_passed"])
                self.assertTrue(r["original_full_core_not_independently_relabelled"])
                self.assertEqual(
                    r["original_mixed_phi"]-r["original_mixed_incident_psi"],
                    r["actual_source_mixed_nonincident_blocker_triples"])

    def test_true_W34_protected_real_original_K44_source_and_sparse(self):
        f,g,ids=planted_original_k44()
        z=original_mixed_source_energy_referee(2,f,g,ids)
        self.assertEqual(z["actual_true_original_both_diagonals"],32)
        self.assertEqual(z["original_core_source_IDs"],16)
        self.assertEqual(z["original_mixed_phi"]-z["original_mixed_incident_psi"],
                         z["actual_source_mixed_nonincident_blocker_triples"])
        self.assertGreaterEqual(z["source_index_restriction_loss"],0)

    def test_source_anti_book_identity_strict_for_different_genuine_f_maps(self):
        # Complete full K_a coordinate pair lists yield FIXED star sizes.
        # Reassigning them to different genuine original point factors
        # can change the ORIGINAL collinearity book, then squared energy
        # changes by precisely MINUS FOUR times that book change.
        result=[]
        for shift in (0,1,2,3,4,7):
            f,g=maps(1,0,shift)
            r=original_mixed_source_energy_referee(1,f,g,())
            result.append((r["original_pencil_book_Mf"],
                           r["source_collinearity_squared_energy"],
                           r["source_f_coordinate_stars"]))
        self.assertEqual(len({row[2] for row in result}),1)
        self.assertGreater(len({row[0] for row in result}),1)
        for m,e,k in result:
            self.assertEqual(e+4*m,2*(15)*(2*2-1)+3*sum(x*x for x in k))

    def test_reject_non_original_core_duplicate_missing_maps(self):
        f,g=maps(1,0)
        _,_,flags=genuine_source(1)
        for h,ff,gg,core in (
            (3,f,g,None),(0,f,g,None),(1,f[:-1],g,None),
            (1,(f[0],)*len(f),g,None),
            (1,f,g,(0,0)),(1,f,g,(True,)),
            (1,f,g,(len(flags),))
        ):
            with self.assertRaises(ValueError):
                original_mixed_source_energy_referee(h,ff,gg,core)
        for bad in (0,1,2,63,65,96,128.0,True,-64):
            with self.assertRaises(ValueError):
                allh_original_mixed_energy_envelope(bad)


if __name__=="__main__":
    unittest.main()
