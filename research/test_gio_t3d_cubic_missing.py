"""Independent GIO-003 G6-D1 cubic missing-projection and stronger T3 gate."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt
import random
import unittest

from gio_t3d_cubic_missing import (
    SCHEMA,PARENT_G6C3,cube_ceil,construct_missing_matrices,
    polynomial_identity,centered_rayleigh,cubic_bound_finite,
    bounded_cubic_source_constants,cubic_heavy_low_ledger,
    validate_cubic_domain,delta_one_equal_no_go,finite_case,certificate,
    necessary_small_excess_screen,graph_distance_falsifier,
)
from gio_t3c2_partial_books import make_model
from gio_t3c_intrinsic_defect import defect_matrices,typed_conflicts_and_gram


def independent_threepath_missing(m):
    """Brute original incidence 3-paths from source flag owners ONLY.

    Completely independent of new matrix-polynomial and old source_graph
    projected/missing fields.
    """
    byp={p:set() for p in range(m["points"])}
    for j,line in enumerate(m["lines"]):
        for p in line:
            byp[p].add(j)
    F=[]
    for p in range(m["points"]):
        row=[]
        for ell,line in enumerate(m["lines"]):
            if ell in byp[p]:
                row.append(0)
                continue
            paths=0
            for first in byp[p]:
                for q in m["lines"][first]:
                    if q!=p and q in line:
                        paths+=1
            assert paths in (0,1)
            row.append(int(paths==0))
        F.append(row)
    return F


def independent_direct_cubic(mats):
    """Check global cubic equation via literal 3walk and first/last flags."""
    B=mats["B"];F=mats["F"]
    P=mats["vp"];L=mats["vl"]
    s,t=mats["s"],mats["t"]
    h=s+t
    point_lines=[{j for j in range(L) if B[p][j]} for p in range(P)]
    line_points=[{p for p in range(P) if B[p][ell]} for ell in range(L)]
    for p in range(P):
        for ell in range(L):
            count=sum(1 for J in point_lines[p] for q in line_points[J]
                      if ell in point_lines[q])
            assert count-h*B[p][ell]+F[p][ell]==1
    return True


def independent_cubic_energy(mats,seed=91):
    rng=random.Random(seed)
    B=mats["B"];F=mats["F"]
    h=mats["s"]+mats["t"]
    VP=mats["vp"];VL=mats["vl"]
    rows=0
    # (T-hI)B=J-F; for centered v, v^T[(T-hI)B] = -v^T F,
    # but via direct dot-products with original incidence flags.
    for _ in range(13):
        raw=[rng.randrange(-5,6) for _ in range(VP)]
        v=[VP*x-sum(raw) for x in raw]
        assert sum(v)==0
        dotB=[sum(v[p]*B[p][ell] for p in range(VP))
              for ell in range(VL)]
        T= mats["T"]
        dotT=[sum(v[p]*T[p][q] for p in range(VP))
              for q in range(VP)]
        mat_poly=[sum(dotT[p]*B[p][ell] for p in range(VP))
                  -h*dotB[ell] for ell in range(VL)]
        dotF=[sum(v[p]*F[p][ell] for p in range(VP))
              for ell in range(VL)]
        assert mat_poly==[-x for x in dotF]
        assert sum(x*x for x in dotF)<=(
            mats["delta_line"]*mats["delta_point"]*
            sum(vv*vv for vv in v))
        rows+=1
    return rows


class TestG6D1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.cases={(c["kind"],c["scheme"]):c for c in cls.c["exact_finite_sources"]}

    def test_01_specification_and_no_infinite_claim(self):
        x=self.c
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["parent_G6C3_HEAD"],PARENT_G6C3)
        self.assertEqual(x["claim"],
            "CONDITIONAL_T3_EXCESS_O_R_THREE_HALVES_CUBIC_IDENTITY")
        self.assertTrue(x["local_cubic_identity_proved_without_GQ"])
        self.assertTrue(x["source_selector_moments_reused_from_G6C3"])
        for p in ("no_unrestricted_T3",
                  "no_infinite_nonGQ_half_integer_excess_family_constructed",
                  "no_Lean_or_independent_external_referee",
                  "no_numeric_external_C6_constants"):
            self.assertTrue(x[p])

    def test_02_independent_source_threepath_F_matches_polynomial_F(self):
        for name in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            m=make_model(name)
            T=construct_missing_matrices(m)
            F=independent_threepath_missing(m)
            self.assertEqual(T["F"],F)
            self.assertEqual(sum(map(sum,F)),m["points"]*m["excess_lines"])
            self.assertEqual([sum(z) for z in F],
                             [m["excess_lines"]]*m["points"])
            self.assertEqual(
                [sum(F[p][ell] for p in range(m["points"]))
                 for ell in range(len(m["lines"]))],
                [m["excess_points"]]*len(m["lines"]))

    def test_03_independent_threewalk_matrix_identity_on_all_actual_entries(self):
        for name in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            m=make_model(name)
            z=construct_missing_matrices(m)
            self.assertTrue(independent_direct_cubic(z))
            self.assertTrue(polynomial_identity(z)["exact_point_and_line_cubic_identity"])

    def test_04_independent_centered_integer_matrix_energy(self):
        for name in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            z=construct_missing_matrices(make_model(name))
            self.assertEqual(independent_cubic_energy(z),13)
            cen=centered_rayleigh(z)
            self.assertGreaterEqual(cen["point"]["centered_integer_Rayleigh_checks"],14)
            self.assertGreaterEqual(cen["line"]["centered_integer_Rayleigh_checks"],14)

    def test_05_true_GQ_is_exact_zero_F_but_nonGQ_is_not(self):
        for name in ("W32","W33","Qminus24","dualQminus42"):
            z=construct_missing_matrices(make_model(name))
            self.assertEqual(sum(sum(v) for v in z["F"]),0)
            self.assertEqual(z["delta_line"],0)
            self.assertEqual(z["delta_point"],0)
            self.assertEqual(cubic_bound_finite(z)["cube_root_term"],0)
        for name in ("doubleW32","switchedDoubleW32"):
            z=construct_missing_matrices(make_model(name))
            self.assertEqual(z["delta_line"],15)
            self.assertEqual(z["delta_point"],15)
            self.assertEqual(sum(map(sum,z["F"])),450)
            self.assertGreater(cubic_bound_finite(z)["cube_root_term"],0)

    def test_06_equal_order_excess_one_exact_trace_no_go(self):
        for q in (2,3,4,5,6,7,8,9,11,16,17,19,23,64,100):
            o=delta_one_equal_no_go(q)
            self.assertTrue(o["strict_trace_contradiction"])
            self.assertLess(o["exact_trace_discrepancy"],0)
            self.assertTrue(o["no_equal_order_one_excess_girth8_source"])
            self.assertEqual(o["putative_vertices_per_side"],
                             (q+1)*(q*q+1)+1)
            self.assertEqual(o["putative_centered_T_trace"],
                             o["putative_vertices_per_side"]*(q+1)-(q+1)**2)

    def test_07_excess_one_no_go_uses_irreducible_rational_cubic(self):
        for q in (2,3,4,5,11):
            # x(x-2q)^2-1 has only possible integer roots +/-1,
            # neither is a root for any thick q>=2.
            self.assertNotEqual((1-2*q)**2-1,0)
            self.assertNotEqual(-(1+2*q)**2-1,0)
            o=delta_one_equal_no_go(q)
            V=o["putative_vertices_per_side"]
            trace=o["putative_centered_T_trace"]
            self.assertNotEqual(3*trace,4*q*(V-1))

    def test_08_cube_root_exact_and_input_fail_closed(self):
        for n in (0,1,2,7,8,9,26,27,28,63,64,65,10000,10**12):
            k=cube_ceil(n)
            self.assertGreaterEqual(k**3,n)
            if k:
                self.assertLess((k-1)**3,n)
        for bad in (-1,1.5,True):
            with self.assertRaises(ValueError):
                cube_ceil(bad)

    def test_09_fixed_C_3_over_2_source_envelope(self):
        for b,C in ((1,0),(1,1),(2,2),(3,5),(10,2)):
            x=bounded_cubic_source_constants(b,C)
            self.assertGreaterEqual(x["spectral_Lambda0"],0)
            self.assertLessEqual(4*(b+1)*C*C,
                                 x["cubic_root0"]**3)
            self.assertEqual(x["combined_owner_conflict_J0"],
                             2*x["point_or_line_conflict_j0"])

    def test_10_actual_finite_adversarial_and_correlated_f_spectral_bounds(self):
        for x in self.c["exact_finite_sources"]:
            self.assertTrue(x["cubic_identity"]["exact_point_and_line_cubic_identity"])
            s,t=x["source_s"],x["source_t"]
            r=min(s,t);C=x["checked_finite_C"]
            self.assertLessEqual(
                x["direct_cubic_bound"]["delta_line"]**2,C*C*r**3)
            self.assertLessEqual(
                x["source_conflict"]["J"],
                x["explicit_source_constants"]["combined_owner_conflict_J0"]*r**4)
            self.assertTrue(x["finite_case_not_infinite_family"])

    def test_11_four_error_closure_for_fractional_excess_domain(self):
        for x in self.c["formal_half_integer_excess_ledgers"]:
            self.assertTrue(x["FORMAL_ONLY"])
            b=x["fixed_before_source"]["balance_b"]
            C=x["fixed_before_source"]["excess_C"]
            r0=int(x["closure"]["sufficient_r0"])
            ep=Q(x["closure"]["eps"])
            rho=Q(x["closure"]["rho"])
            w=Q(x["selector"]["w"])
            mom=x["moment"];sel=x["selector"]
            self.assertEqual(x["linear_source_gate_replaced_by"],
                             "Delta_L^2 <= C^2*r^3")
            self.assertLessEqual(mom["improper"],ep*r0)
            self.assertLessEqual(mom["E"]**2,ep**2*r0)
            self.assertLessEqual(mom["blocker_D"]**8,ep**8*r0)
            self.assertLessEqual(12*b*b*rho*sel["q3"]**2*mom["L6"],ep**2)
            self.assertEqual(8*ep,w)
            self.assertTrue(x["closure"]["four_error_budgets_checked"])
            self.assertGreater(Q(x["closure"]["delta"]),0)

    def test_12_exact_domain_guard_includes_true_3_over_2_not_r2(self):
        # Use r even perfect-square to avoid rounding ambiguity.
        z=cubic_heavy_low_ledger(2,3,Q(1),Q(1))
        r=int(z["closure"]["sufficient_r0"])
        # Round up to a square to get integer C*r^(3/2)
        root=isqrt(r)+(isqrt(r)**2<r)
        r=root*root
        DL=3*root**3
        DP=DL
        self.assertTrue(validate_cubic_domain(r,r,DL,DP,0,z))
        with self.assertRaises(ValueError):
            validate_cubic_domain(r,r,DL+1,DP+1,0,z)
        with self.assertRaises(ValueError):
            validate_cubic_domain(r,r,0,1,0,z)
        with self.assertRaises(ValueError):
            validate_cubic_domain(r,r,r*r,r*r,0,z)
        with self.assertRaises(ValueError):
            validate_cubic_domain(r,r,0,0,-1,z)

    def test_13_exponential_external_input_values_are_FORMAL_ONLY(self):
        for z in self.c["formal_half_integer_excess_ledgers"]:
            self.assertTrue(z["external_numeric_graph_C6_constants_NOT_proved"])
            self.assertTrue(z["no_GQ_or_template"])
            self.assertTrue(z["no_full_unrestricted_T3"])
            self.assertTrue(z["no_existing_positive_excess_infinite_family_asserted"])
        for params in ((1,1,1,1),(1,1,Q(1),1),
                       (1,1,Q(1,2),Q(1)),(1,1,Q(1),Q(0))):
            with self.assertRaises(ValueError):
                cubic_heavy_low_ledger(*params)

    def test_14_line_point_dual_regression_not_equal_order_shortcut(self):
        left=self.cases["Qminus24","lex"]
        right=self.cases["dualQminus42","lex"]
        self.assertEqual(left["source_s"],right["source_t"])
        self.assertEqual(left["source_t"],right["source_s"])
        self.assertEqual(left["points"],right["lines"])
        self.assertEqual(left["lines"],right["points"])
        self.assertTrue(left["cubic_identity"]["exact_dual_no_GQ_identity"])
        self.assertTrue(right["cubic_identity"]["exact_dual_no_GQ_identity"])

    def test_16_exact_moore_excess_divisibility_unequal_orders(self):
        for s,t in ((2,4),(4,2),(3,5),(5,3),(5,8),(8,5)):
            d=__import__("math").gcd(s+1,t+1)
            q=(t+1)//d;p=(s+1)//d
            for a in (0,1,2,3,7):
                z=necessary_small_excess_screen(s,t,q*a,p*a)
                self.assertEqual(z["positive_excess_quantum"],a)
                self.assertEqual(z["excess_step_lines"],q)
                self.assertEqual(z["excess_step_points"],p)
                self.assertTrue(z["actual_source_existence_NOT_proved"])
            with self.assertRaises(ValueError):
                necessary_small_excess_screen(s,t,q*2,p*2+1)

    def test_17_no_fake_connectedness_or_diameter_on_double_source(self):
        for name,expected in (("W32",1),("Qminus24",1),
                              ("doubleW32",2),
                              ("switchedDoubleW32",1)):
            m=make_model(name)
            got=graph_distance_falsifier(m)
            self.assertEqual(got["actual_components"],expected)
            self.assertTrue(got["literal_BFS_source_not_just_parameter_guess"])
            if name in ("W32","Qminus24"):
                self.assertTrue(got["size_enforced_connected"])
                self.assertTrue(got["size_enforced_diameter_at_most_five"])
                self.assertLessEqual(got["actual_max_finite_distance"],5)
            else:
                self.assertFalse(got["size_enforced_connected"])
                self.assertFalse(got["size_enforced_diameter_at_most_five"])

    def test_18_small_positive_excess_size_forces_connected_only_conditionally(self):
        # These are pure *necessary* parameter gates, not actual graph
        # existence certificates; no nonGQ family is synthesized.
        for q in (2,3,5,7,11,13):
            z=necessary_small_excess_screen(q,q,1,1)
            self.assertTrue(z["connectedness_forced_by_size"])
            self.assertTrue(z["diameter_at_most_five_if_actual_source"])
            self.assertTrue(z["actual_source_existence_NOT_proved"])
            self.assertLess(z["delta_line"],z["Moore_lines"])
            # G6-D separately proves this hypothetical Delta=1
            # parameter source is actually impossible for q>=2.
            self.assertTrue(delta_one_equal_no_go(q)["strict_trace_contradiction"])
        for bad in ((2,4,1,0),(1,2,0,0),(2,2,-1,-1),(2,2,0,1)):
            with self.assertRaises(ValueError):
                necessary_small_excess_screen(*bad)

    def test_15_no_false_derivation_from_degree_only_when_girth_fails(self):
        from gio_t3c_intrinsic_defect import shortcycle_edit_from_gq
        edited,original,sw=shortcycle_edit_from_gq("W32")
        m=make_model("W32")
        self.assertEqual(len(edited),len(m["flags"]))
        # Genuine source C4 destroys uniqueness of 3paths; input gate
        # source_graph from G6-C1 fails closed (not cubic identity).
        from gio_t3c_intrinsic_defect import source_graph
        lines=[set() for _ in range(len(m["lines"]))]
        for p,l in edited:
            lines[l].add(p)
        with self.assertRaises(ValueError):
            source_graph(lines,m["points"],m["s"],m["t"])


if __name__=="__main__":
    unittest.main()
