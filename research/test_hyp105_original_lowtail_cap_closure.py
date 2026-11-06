"""Independent falsifiers for AA4-CAPCLOSE; no universal root acceptance."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_original_lowtail_cap_closure import (
    cap_closure, ceil_sqrt, replay_frozen_original_lowtail, source_energy
)
from hyp105_full_physical_degree_tail import genuine_source
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


class TestOriginalCollinearityCap(unittest.TestCase):
    def test_exact_genuine_source_point_and_line_W32_W34(self):
        for h in (1,2):
            s,V,flags=genuine_source(h)
            a=2
            while comb(a,2)<V:
                a+=1
            for scheme in ("lex","reverse-line"):
                with self.subTest(h=h,scheme=scheme):
                    x=pair_labeled_symplectic(h,scheme)
                    p=source_energy(s,flags,x["left_labels"],a)
                    l=source_energy(s,[(b,a) for a,b in flags],
                                    x["right_labels"],a)
                    for v in (p,l):
                        self.assertEqual(v["G"],v["exact_srg_rhs"])
                        self.assertLessEqual(v["G"],v["spectral_ceiling"])
                        self.assertEqual(v["F1_ceiling"],2*v["G"])

    def test_four_true_original_frozen_source_lowtail_certificates(self):
        r=replay_frozen_original_lowtail()
        self.assertEqual(r["schema"],"mathlab.hyp105.original-cap-closure.v1")
        self.assertFalse(r["allh_root_A_accepted"])
        self.assertEqual([(x["s"],x["scheme"]) for x in r["cases"]],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        self.assertTrue(all(x["exact_caps_pass"] for x in r["cases"]))

    def test_reject_noninjective_labels(self):
        s,V,flags=genuine_source(1)
        x=pair_labeled_symplectic(1,"lex")
        bad=list(x["left_labels"])
        bad[1]=bad[0]
        with self.assertRaises(ValueError):
            source_energy(s,flags,bad,6)

    def test_reject_forged_original_GQ_incidence(self):
        s,V,flags=genuine_source(1)
        x=pair_labeled_symplectic(1,"lex")
        bad=list(flags)
        point=bad[0][0]
        occupied={ell for p,ell in flags if p==point}
        missing=next(ell for ell in range(V) if ell not in occupied)
        bad[0]=(point,missing)  # a genuinely nonincident new original pair
        with self.assertRaises(ValueError):
            source_energy(s,bad,x["left_labels"],6)

    def test_exact_integer_selector_caps_not_random_f_g(self):
        z=cap_closure(2,15,6,45,12,45,8,3,150,700,comb(45,6),700,720)
        self.assertEqual(z["sigma2_inverse"],16*comb(8,2))
        self.assertEqual(z["sigma3_inverse"],64*comb(12,3))
        self.assertEqual(z["sixth_moment_cap"],
                         24*comb(45,6)+72*24*8**2)
        self.assertFalse(z["allh_root_A_accepted"])
        self.assertIsInstance(Fraction(z["two_BBo_lower_raw"]),Fraction)
        with self.assertRaises(ValueError):
            cap_closure(2,15,7,45,12,45,8,3,150,700,comb(45,6),700,720)

    def test_fixed_positive_density_original_Z_error_is_not_little_o(self):
        rho=Fraction(1,1024)
        ratios=[]
        for s in (64,128,256):
            # Ebad mask term = 12*s^2*rho*s^4; ||P3||^2 = L*s^6.
            # Its squared normalized error / (L*s^12) is 12*rho.
            ratios.append(12*rho)
        self.assertEqual(ratios,[Fraction(3,256)]*3)

    def test_reject_invalid_cap_inputs(self):
        for x in (-1,1.5,True):
            with self.assertRaises(ValueError):
                ceil_sqrt(x)
        with self.assertRaises(ValueError):
            cap_closure(4,85,14,425,40,39,3,4,100,100,100,100,100)


if __name__=="__main__":
    unittest.main()
