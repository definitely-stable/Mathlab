"""AA4-AW independent finite permutation rigidity + true original GF5 falsifiers."""
import unittest
from itertools import permutations, combinations
from math import factorial
from collections import Counter

from hyp105_issue230_d6aa4aw_nonlinear_swap_rigidity import (
    finite_permutation_kernel_rank_mod_prime,
    full_global_disjoint_hessian,
    assignment_value,
    source_all_h_rigidity_certificate,
    actual_original_W32_four_map_nonlinear_witness,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked, R3_CERTIFIED_FLOORS


def independent_prime_rank(matrix, prime=1009):
    """Independent rectangular finite-field elimination in row-major form."""
    rows=[[x%prime for x in r] for r in matrix]
    ncols=len(rows[0])
    pivot_row=0
    for col in range(ncols):
        nonzero=next((j for j in range(pivot_row,len(rows))
                      if rows[j][col]%prime),None)
        if nonzero is None:continue
        rows[pivot_row],rows[nonzero]=rows[nonzero],rows[pivot_row]
        inv=pow(rows[pivot_row][col],-1,prime)
        for k in range(col,ncols):
            rows[pivot_row][k]=(rows[pivot_row][k]*inv)%prime
        for rr in range(pivot_row+1,len(rows)):
            val=rows[rr][col]
            if val:
                for k in range(col,ncols):
                    rows[rr][k]=(rows[rr][k]-val*rows[pivot_row][k])%prime
        pivot_row+=1
        if pivot_row==ncols:break
    return pivot_row


class OriginalNonlinearPermutationRigidityTests(unittest.TestCase):
    def test_01_full_S4_S5_independent_modular_Hessian_kernel(self):
        for n,expected in ((4,(24,14,10)),(5,(120,103,17))):
            z=finite_permutation_kernel_rank_mod_prime(n)
            self.assertEqual((
                z["full_permutation_states"],z["rank_over_F1009"],
                z["full_kernel_dimension"]),expected)
            self.assertTrue(z["rank_matches_assignment_theorem"])
            self.assertEqual(z["expected_exact_assignment_span_dimension"],
                             (n-1)**2+1)
            self.assertEqual(z["enumerated_mixed_Hessian_equations"],
                             factorial(n)*3*__import__("math").comb(n,4))

    def test_02_independently_rank_assignment_indicator_matrix_S4(self):
        n=4
        S=tuple(permutations(range(n)))
        a=[[int(state[i]==j) for i in range(n) for j in range(n)] for state in S]
        self.assertEqual(independent_prime_rank(a),10)
        z=finite_permutation_kernel_rank_mod_prime(n)
        self.assertEqual(len(S)-z["rank_over_F1009"],independent_prime_rank(a))
        # All 24 permutations and each 3 pairwise disjoint swap pair:
        # a general REAL assignment functional has identically zero Hessian.
        coeffs=[[3*i*j+2*i-7*j+i*j*j for j in range(n)] for i in range(n)]
        for state in S:
            for first,second in (
                ((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))):
                self.assertEqual(full_global_disjoint_hessian(
                    state,first,second,lambda v:assignment_value(v,coeffs,11)),0)

    def test_03_original_global_all_h_exact_scope_and_no_root_promotion(self):
        for h in tuple(range(1,37))+(48,64,80):
            z=source_all_h_rigidity_certificate(1<<h)
            self.assertEqual(z["actual_original_source_LINE_factor_count"],
                ((1<<h)+1)*(((1<<h)**2)+1))
            self.assertTrue(z["zero_mixed_Hessian_iff_one_factor_assignment_linear"])
            self.assertTrue(z["universal_one_sign_mixed_Hessian_forces_zero_then_assignment"])
            self.assertEqual(z["true_original_W32_complete_K6_and_transitive_gauge"],h==1)
            self.assertTrue(z["not_same_global_pair_seven_GF5_minimax"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        for invalid in (1,3,6):
            with self.assertRaises(ValueError):
                source_all_h_rigidity_certificate(invalid)

    def test_04_original_nonlinear_four_map_scalar_sign_reversal_abstract(self):
        n=5
        g=tuple(range(n))
        def F(v):
            return int(v[0]==0 and v[2]==2)
        sig=(0,1);tau=(2,3)
        val=full_global_disjoint_hessian(g,sig,tau,F)
        # For this indicator, both selected value tests are true at base,
        # false at single and double swaps, so H=+1.
        self.assertEqual(val,1)
        gs=list(g);gs[0],gs[1]=gs[1],gs[0]
        self.assertEqual(full_global_disjoint_hessian(
            tuple(gs),sig,tau,F),-1)
        self.assertNotEqual(val,0)
        with self.assertRaises(ValueError):
            full_global_disjoint_hessian(g,(0,1),(1,2),F)
        with self.assertRaises(ValueError):
            full_global_disjoint_hessian((0,0,1,2),(0,1),(2,3),F)

    def test_05_independent_abstract_K4_edge_transitive_gauge_average(self):
        # This is ABSTRACT complete K4 physical E as small finite symmetry
        # oracle only, explicitly NOT a fake true W(3,s).
        E=tuple(combinations(range(4),2))
        owners={e:i for i,e in enumerate(E)}
        coeff=[[5*i*i+7*(j+1)**2+3*i*j for j in range(6)] for i in range(6)]
        original=tuple(range(6))
        def F(v):return assignment_value(v,coeff,19)
        perms=tuple(permutations(range(4)))
        def physical_relabel(g,physical):
            return tuple(owners[tuple(sorted(physical[k] for k in E[i]))]
                         for i in g)
        for g in (original,(1,5,2,0,4,3)):
            vals=[F(physical_relabel(g,t)) for t in perms]
            self.assertEqual(sum(vals),
                factorial(4)*19 + (factorial(4)//6)*sum(sum(row) for row in coeff))
        # Average of an assignment function is constant, not necessarily
        # the assignment function itself.
        self.assertNotEqual(F(original),F((1,5,2,0,4,3)))

    def test_06_true_original_W32_all_seven_and_nonlinear_anti_curvature(self):
        r=actual_original_W32_four_map_nonlinear_witness("S68")
        self.assertEqual(r["full_original_six_incidence_ID_left_candidates"],62370)
        self.assertEqual(r["scalar_mixed_Hessians"]["unweighted_S7"],0)
        self.assertEqual(
            r["scalar_mixed_Hessians"]["historical_51palette_selected_floor_numerator"],
            -46107)
        self.assertTrue(r["same_full_original_point_map_all_states"])
        self.assertTrue(r["original_line_global_physical_support_unchanged"])
        self.assertEqual(sum(r["true_original_classwise_mixed_Hessian"]),0)
        self.assertEqual(len(r["four_complete_original_global_seven_class_vectors"]),4)
        self.assertTrue(r["opposite_sign_by_shifting_original_baseline_to_first_swapped_full_map"])
        self.assertEqual(
            r["four_complete_original_global_seven_class_vectors"],
            ((0,44,21,0,0,2,1),(0,56,25,0,0,4,2),
             (0,67,41,0,0,2,0),(1,73,51,0,0,3,1)))
        self.assertEqual(r["scalar_mixed_Hessians"],{
            "unweighted_S7":0,
            "historical_51palette_selected_floor_numerator":-46107,
            "NONLINEAR_squared_S7":1596,
            "NONLINEAR_sum_seven_class_squares":368,
        })
        self.assertNotEqual(r["scalar_mixed_Hessians"]["NONLINEAR_squared_S7"],0)
        # The SAME original actual g first-swap transform reverses the
        # nonlinear signed curvature, not just the linear selected floor.
        # These are nonconstant right-map functionals even when physical
        # full K6 coordinate gauge symmetry is factored out.

    def test_07_TRUE_W32_physical_coordinate_relabel_invariance_nonlinear(self):
        m=fixture(1,"S68")
        source=tuple(tuple(t) for t in m["incidences"])
        f=tuple(tuple(t) for t in m["left_labels"])
        g=tuple(tuple(t) for t in m["right_labels"])
        p=tuple(ids for ids,k in selected_left_six(m))
        self.assertEqual(len(p),62370)
        def counts(right):
            out=Counter()
            for ids in p:
                k=classify_seven_prechecked(ids,f,right,source)
                if k is not None:out[k]+=1
            return out
        C=counts(g)
        # Nontrivial 6-vertex permutation acts on all 15 right edge
        # pair images at once; ORIGINAL line factors and six-Q unchanged.
        perm=(2,0,5,1,4,3)
        g2=tuple(tuple(sorted(perm[x] for x in e)) for e in g)
        self.assertEqual(len(set(g2)),15)
        D=counts(g2)
        self.assertEqual(C,D)
        self.assertEqual(sum(v*v for v in C.values()),
                         sum(v*v for v in D.values()))
        self.assertEqual(sum(C[k]*w for k,w in R3_CERTIFIED_FLOORS.items()),
                         sum(D[k]*w for k,w in R3_CERTIFIED_FLOORS.items()))


if __name__=="__main__":
    unittest.main()
