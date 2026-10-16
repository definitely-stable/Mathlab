"""Independent exact original seven GF5 curvature rank and global-swap sign tests."""
import unittest
import random
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_issue230_d6aa4av_seven_fullrank_sign_no_go import (
    integer_rank_and_basis, integer_determinant_bareiss,
    integer_determinant_mod_prime, EXACT_SOURCE_BASIS_ROW_ORDER,
    EXACT_SOURCE_BASIS_DETERMINANT, EXACT_ORIGINAL_SEVEN_ROW_WITNESSES,
    original_disjoint_swap_hessian_permutation_sign_identity,
    exact_original_w32_hessian_linear_obstruction, ORDER,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked, R3_CERTIFIED_FLOORS


class ActualOriginalSevenSignedNoGoTests(unittest.TestCase):
    def test_01_exact_rank_and_independent_bareiss_small_random_int(self):
        rng=random.Random(230240)
        for n in (1,2,3,4,5,6,7):
            for _ in range(6):
                M=[[rng.randint(-9,9) for _ in range(n)] for _ in range(n)]
                r=integer_rank_and_basis(M)
                det=integer_determinant_bareiss(M)
                self.assertEqual(bool(det),r["rank"]==n)
                self.assertEqual(len(r["pivot_row_indices"]),r["rank"])
            self.assertEqual(integer_determinant_bareiss(
                [[int(i==j) for j in range(n)] for i in range(n)]),1)
        self.assertEqual(integer_rank_and_basis([(1,2,3),(3,6,9)])["rank"],1)
        for n in (2,3,4,7):
            for _ in range(7):
                a=[[rng.randint(-50,50) for _ in range(n)] for _ in range(n)]
                self.assertEqual(integer_determinant_mod_prime(a,1009),
                                 integer_determinant_bareiss(a)%1009)
        with self.assertRaises(ValueError):
            integer_rank_and_basis([(1,2),(3,)])

    def test_02_all_h_source_line_swap_sign_inversion_on_complete_maps(self):
        # Counterexample-to-sign is an ALGEBRAIC all-h identity, so use
        # independently varied FULL original source permutations.
        for h,scheme in ((1,"S68"),(1,"S72"),(2,"lex"),(2,"random")):
            m=fixture(h,scheme)
            original=tuple(tuple(t) for t in m["right_labels"])
            self.assertEqual(len(set(original)),len(original))
            def F(right):
                # Explicit nonlinear integer input function, no classifier
                return sum((i+3)*((a+1)*(b+2)) for i,(a,b) in enumerate(right))
            for sw1,sw2 in (((0,1),(2,3)),((1,4),(6,7))):
                w=original_disjoint_swap_hessian_permutation_sign_identity(
                    original,sw1,sw2,F)
                self.assertEqual(w["hessian_at_legally_swapped_g"],-w["hessian_original"])
                self.assertTrue(w["all_four_complete_global_line_maps_valid"])
        with self.assertRaises(ValueError):
            original_disjoint_swap_hessian_permutation_sign_identity(
                tuple(range(12)),(1,2),(2,3),sum)

    def test_03_true_original_W32_sparse_24_Hessian_rows_exact_Fraction_rank(self):
        z=exact_original_w32_hessian_linear_obstruction()
        self.assertEqual(z["number_of_really_global_complete_original_Q_four_state_rows"],24)
        self.assertEqual(len(ORDER),7)
        self.assertEqual(set(ORDER),set(R3_CERTIFIED_FLOORS))
        M=z["exact_real_original_integer_Hessian_matrix"]
        self.assertEqual(len(M),24)
        self.assertTrue(all(len(row)==7 for row in M))
        rank=integer_rank_and_basis(M)
        self.assertEqual(rank["rank"],z["exact_Fraction_Gaussian_rank"])
        self.assertEqual(rank["rank"],7)
        self.assertEqual(rank["pivot_row_indices"],EXACT_SOURCE_BASIS_ROW_ORDER)
        sub=[M[i] for i in rank["pivot_row_indices"]]
        self.assertEqual({i:M[i] for i in EXACT_SOURCE_BASIS_ROW_ORDER},
                         EXACT_ORIGINAL_SEVEN_ROW_WITNESSES)
        self.assertEqual(integer_determinant_bareiss(sub),
                         EXACT_SOURCE_BASIS_DETERMINANT)
        self.assertEqual(z["exact_independent_Bareiss_rank_witness_det"],
                         -2650)
        self.assertEqual(integer_determinant_mod_prime(sub,1009),377)
        self.assertEqual(z["exact_independent_F1009_rank_witness_det"],377)
        self.assertTrue(z["any_nonzero_real_fixed_linear_seven_tag_coefficients_have_both_signed_Hessians"])
        self.assertTrue(z["no_universal_seven_tag_linear_mixed_curvature_sign_law_proved"])
        self.assertTrue(z["all_h_signed_inversion_identity_applies"])
        self.assertFalse(z["original_fixed_f_g_seven_minimax_PROVED"])
        self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_04_same_original_W32_historical_tag_real_signed_inversion(self):
        # Completely independent source-Q selection and actual historical
        # seven GF5 rescoring of FOUR true original globally injected maps.
        model=fixture(1,"S68")
        q=tuple(tuple(i) for i in model["incidences"])
        f=tuple(tuple(e) for e in model["left_labels"])
        g=tuple(tuple(e) for e in model["right_labels"])
        original_Q=tuple(ids for ids,_ in selected_left_six(model))
        self.assertEqual(len(original_Q),62370)
        weights=tuple(R3_CERTIFIED_FLOORS[k] for k in ORDER)
        def score(right):
            out=[0]*7
            for ids in original_Q:
                tag=classify_seven_prechecked(ids,f,right,q)
                if tag is not None:out[ORDER.index(tag)]+=1
            return tuple(out)
        s=(0,1);t=(2,3)
        def swap(g,u,v):
            r=list(g)
            r[u],r[v]=r[v],r[u]
            return tuple(r)
        G0=g;Gs=swap(G0,*s);Gt=swap(G0,*t);Gst=swap(Gs,*t)
        y=[score(gg) for gg in (G0,Gs,Gt,Gst)]
        H=tuple(y[3][j]-y[1][j]-y[2][j]+y[0][j] for j in range(7))
        Hr=tuple(y[2][j]-y[0][j]-y[3][j]+y[1][j] for j in range(7))
        self.assertEqual(H,tuple(-x for x in Hr))
        self.assertEqual(sum(H),0) # precise pin from prior independently recorded S68 Hessian
        self.assertEqual(sum(H[j]*weights[j] for j in range(7)),-46107)
        self.assertEqual(len(set(Gst)),15)


if __name__=="__main__":
    unittest.main()
