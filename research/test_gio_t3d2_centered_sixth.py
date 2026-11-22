"""Independent GIO-003 G6-D2: centered missing-sixth and Wenger family tests."""
from fractions import Fraction as Q
from itertools import product
from math import gcd,isqrt
import unittest

from gio_t3d2_centered_sixth import (
    SCHEMA,PARENT_G6D1,certificate,raw_trace_cube,
    sixth_moment_certificate,exact_codegrees,centered_gram,
    fractional_psd,direct_centered_spectral_certificate,
    mixing_constants,uniform_direct_spectral_constants,integrated_quadratic_moment_ledger,
    integrated_quadratic_direct_ledger,validate_family_gate,
    validate_direct_family_gate,synthetic_2block_missing_barrier,
    wenger_W2_prime_source,wenger_W2_spectral_parameters,
    wenger_finite_exact_case,wenger_quadratic_theorem_ledger,
    wenger_original_six_id_inverse_case,
    is_prime,
)
from gio_t3d_cubic_missing import (
    construct_missing_matrices,matmul,transpose,
)
from gio_t3c2_partial_books import make_model
from gio_t3c_intrinsic_defect import (
    defect_matrices,typed_maps,typed_conflicts_and_gram,
    direct_original_owner_conflicts,
)


def brute_original_F(m):
    """Independently scan true original point->line three-edge paths."""
    point_lines=[set() for _ in range(m["points"])]
    for ell,line in enumerate(m["lines"]):
        for p in line:
            point_lines[p].add(ell)
    F=[]
    for p in range(m["points"]):
        row=[]
        for ell,line in enumerate(m["lines"]):
            if ell in point_lines[p]:
                row.append(0)
                continue
            feet=sum(1 for q in line
                     if len(point_lines[p]&point_lines[q])>0)
            assert feet in (0,1)
            row.append(int(feet==0))
        F.append(row)
    return F


def independent_closed_6walk_F(F):
    """6walk with three missing point-to-line incidence layers, O(P^3L)."""
    P=len(F);L=len(F[0])
    # Build K manually via sets, not the production matmul.
    masks=[{j for j,x in enumerate(row) if x} for row in F]
    K=[[len(masks[i]&masks[j]) for j in range(P)] for i in range(P)]
    six=sum(K[i][j]*K[j][k]*K[k][i]
            for i in range(P) for j in range(P) for k in range(P))
    # Explicit independent dual count, not a symmetry assumption.
    Frows=[{i for i in range(P) if F[i][j]} for j in range(L)]
    C=[[len(Frows[i]&Frows[j]) for j in range(L)] for i in range(L)]
    dual=sum(C[i][j]*C[j][k]*C[k][i]
             for i in range(L) for j in range(L) for k in range(L))
    assert six==dual
    return six


def brute_all_prime_wenger_lines(q):
    """Independent line-first incidence formula from W'_2(q), not builder."""
    pts=list(product(range(q),repeat=3))
    lines=list(product(range(q),repeat=3))
    return tuple(tuple(i for i,(a,b,c) in enumerate(pts)
                       if (v+b-u*a)%q==0 and (w+c-u*a*a)%q==0)
                 for (u,v,w) in lines)


class TestG6D2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=certificate()
        cls.cases={(x["kind"],x["scheme"]):x
                   for x in cls.data["exact_source_finite_checks"]}

    def test_01_certificate_scope_is_both_routes_and_real_family(self):
        z=self.data
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6D1_HEAD"],PARENT_G6D1)
        self.assertEqual(z["claim"],
         "CONDITIONAL_QUADRATIC_T3_SPECTRAL_GATE_WITH_EXPLICIT_WENGER_FAMILY")
        self.assertTrue(z["sixth_moment_condition_is_sufficient_not_necessary"])
        self.assertTrue(z["full_quadratic_without_a_spectral_gate_remains_OPEN"])
        self.assertTrue(z["real_positive_excess_infinite_family_from_published_Wenger"])
        self.assertTrue(z["published_Wenger_spectral_theorem_is_prior_art"])
        self.assertTrue(z["no_unrestricted_T3_or_ASET_claim"])
        self.assertTrue(z["no_external_referee_or_Lean"])

    def test_02_independent_literal_missing_F_and_point_line_trace6(self):
        for name in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            m=make_model(name)
            z=construct_missing_matrices(m)
            self.assertEqual(z["F"],brute_original_F(m))
            c=sixth_moment_certificate(z)
            self.assertEqual(
                c["ordinary_closed_sixwalks_point_rooted"],
                independent_closed_6walk_F(z["F"]))
            self.assertEqual(c["ordinary_closed_sixwalks_point_rooted"],
                             c["ordinary_closed_sixwalks_line_rooted"])
            self.assertEqual(c["exact_centered_S2"],
                             z["vp"]*z["delta_line"]-
                             z["delta_line"]*z["delta_point"])

    def test_03_exact_jensen_optimal_sixth_moment_scaling(self):
        for x in self.data["exact_source_finite_checks"]:
            z=x["exact_centered_moments"]
            s6=z["exact_centered_S6"];s2=z["exact_centered_S2"]
            P=z["source_points"];L=z["source_lines"]
            self.assertGreaterEqual(s6*(P-1)**2,s2**3)
            self.assertGreaterEqual(s6*(L-1)**2,s2**3)
            self.assertEqual(s6,0 if z["delta_line"]==0 else s6)
            if z["delta_line"]>0:
                self.assertGreater(s6,0)
                self.assertGreater(s2,0)

    def test_04_rational_centered_gram_zero_row_sums_and_psd(self):
        for kind in ("W32","Qminus24","doubleW32","switchedDoubleW32"):
            z=construct_missing_matrices(make_model(kind))
            H=centered_gram(z)
            self.assertTrue(all(sum(row)==0 for row in H))
            self.assertEqual(H,transpose(H))
            k=direct_centered_spectral_certificate(z)[
                 "exact_min_integer_centered_norm_kappa"]
            r=min(z["s"],z["t"])
            A=[[Q(k*r**3)*(i==j)-H[i][j] for j in range(z["vp"])]
                 for i in range(z["vp"])]
            self.assertTrue(fractional_psd(A)["PSD"])
            if k:
                B=[[Q((k-1)*r**3)*(i==j)-H[i][j]
                    for j in range(z["vp"])] for i in range(z["vp"])]
                self.assertFalse(fractional_psd(B)["PSD"])

    def test_05_doubleW32_sharp_nontrivial_missing_mode(self):
        z=construct_missing_matrices(make_model("doubleW32"))
        c=sixth_moment_certificate(z)
        self.assertEqual(z["delta_line"],15)
        self.assertEqual(c["exact_centered_S6"],15**6)
        self.assertEqual(c["exact_centered_S2"],15**2)
        g=direct_centered_spectral_certificate(z)
        self.assertEqual(g["actual_certified_centered_norm_squared_upper"],29*8)
        self.assertEqual(g["exact_min_integer_centered_norm_kappa"],29)
        self.assertEqual(g["Sixth_moment_operator_bound_integer"],29)

    def test_06_exact_codegree_L1_is_sufficient_not_equivalent(self):
        for name in ("W32","doubleW32","switchedDoubleW32"):
            m=construct_missing_matrices(make_model(name))
            g=direct_centered_spectral_certificate(m)
            self.assertTrue(g["independent_codegree_L1_sufficiency_verified"])
            self.assertLessEqual(g["exact_min_integer_centered_norm_kappa"],
                                 g["row_abs_scaled_kappa"])
            self.assertLessEqual(g["exact_min_integer_centered_norm_kappa"],
                                 g["Sixth_moment_operator_bound_integer"])

    def test_07_moment_ledger_exact_rational_four_error_closure(self):
        for z in self.data["exact_all_order_formal_ledgers"]:
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["external_numeric_C6_constants_NOT_verified"])
            self.assertFalse(z["no_unconditional_quadratic_T3"] is False)
            f=z["fixed_before_source"];sel=z["selector"];m=z["moments"]
            c=z["closure"];eps=Q(c["eps"]);rho=Q(c["rho"])
            r=int(c["sufficient_r0"])
            self.assertLessEqual(m["improper"],eps*r)
            self.assertLessEqual(m["E"]**2,eps**2*r)
            self.assertLessEqual(m["blocker_D"]**8,eps**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*
                 rho*sel["q3"]**2*m["L6"],eps**2)
            self.assertEqual(8*eps,Q(sel["w"]))

    def test_08_direct_spectral_ledger_has_NO_sixth_moment_hypothesis(self):
        for z in self.data["direct_centered_spectral_family_ledgers"]:
            self.assertTrue(z["moment_sixth_condition_is_NOT_required"])
            self.assertIn("centered_spectral_gate",z["moments"])
            self.assertNotIn("centered_moment_gate",z["moments"])
            self.assertTrue(z["exact_LDL_source_certificate_available"])
            self.assertNotIn("centered_M",z["fixed_before_source"])
            f=z["fixed_before_source"]
            self.assertGreaterEqual(f["centered_operator_kappa"],0)

    def test_09_fixed_source_domain_guards_reject_moments_or_norm_outside(self):
        x=integrated_quadratic_moment_ledger(1,3,27,Q(1),Q(1))
        y=integrated_quadratic_direct_ledger(1,3,3,Q(1),Q(1))
        r=max(int(x["closure"]["sufficient_r0"]),
              int(y["closure"]["sufficient_r0"]))
        DL=3*r*r
        self.assertTrue(validate_family_gate(r,r,DL,DL,27*r**9,0,x))
        with self.assertRaises(ValueError):
            validate_family_gate(r,r,DL,DL,27*r**9+1,0,x)
        with self.assertRaises(ValueError):
            validate_family_gate(r,r,DL+1,DL+1,0,0,x)
        self.assertTrue(validate_direct_family_gate(r,r,DL,DL,3,0,y))
        with self.assertRaises(ValueError):
            validate_direct_family_gate(r,r,DL,DL,4,0,y)
        with self.assertRaises(ValueError):
            validate_direct_family_gate(r,r,DL,DL,3,-1,y)
        with self.assertRaises(ValueError):
            validate_direct_family_gate(r,r,DL+1,DL+1,2,0,y)

    def test_10_external_C6_values_are_only_formal_placeholders(self):
        for args in ((1,1,1,1,1),(1,1,1,Q(1),1),
                     (1,1,1,Q(1,2),Q(1)),(1,1,1,Q(1),Q(0))):
            with self.assertRaises(ValueError):
                integrated_quadratic_direct_ledger(*args)
        for k in (-1,1.5,True):
            with self.assertRaises(ValueError):
                uniform_direct_spectral_constants(1,3,k)

    def test_11_synthetic_two_block_biregular_masks_are_not_sources(self):
        z=self.data["zero_one_regular_F_barriers_not_source_graphs"]
        self.assertEqual(len(z),2)
        for x in z:
            q=x["q"]
            self.assertTrue(x["mask_IS_NOT_verified_as_incidence_source"])
            self.assertEqual(x["centered_squared_spectral_lower"],q**4)
            self.assertEqual(Q(x["centered_operator_over_q_cubed"]),q)
            self.assertGreaterEqual(x["actual_centered_S6"],q**12)
            self.assertTrue(
                x["no_unconditional_quadratic_conclusion_from_degree_counts"])

    def test_12_wenger_prime_field_realization_matches_independent_lines(self):
        for q in (3,5):
            m=wenger_W2_prime_source(q)
            self.assertEqual(m["lines"],brute_all_prime_wenger_lines(q))
            self.assertEqual(len(m["lines"]),q**3)
            self.assertEqual(m["points"],q**3)
            self.assertEqual(len(m["flags"]),q**4)
            self.assertEqual(m["excess_lines"],2*q*(q-1))
            self.assertEqual(m["excess_points"],2*q*(q-1))
            self.assertGreater(len(m["missing"]),0)
            self.assertEqual(len(m["missing"]),q**3*2*q*(q-1))

    def test_13_wenger_exact_integer_polynomial_and_sixth_trace_q3_q5(self):
        for q in (3,5):
            a=wenger_finite_exact_case(q)
            self.assertTrue(a["all_entries_published_W2_spectral_polynomial_exact"])
            self.assertTrue(a["centered_S2_checked_against_published_eigen_multiplicities"])
            self.assertTrue(a["centered_S6_checked_against_published_eigen_multiplicities"])
            self.assertTrue(a["genuine_original_source_graph_girth8"])
            self.assertEqual(a["spectral_polynomial_constant"],q*(q-1)*(q-2))
            self.assertEqual(a["genuine_nongq_delta"],2*q*(q-1))
        self.assertTrue(wenger_finite_exact_case(3)["exact_PSD_q3_sharp"])

    def test_14_wenger_all_q_arithmetic_has_fixed_b1_C3_kappa3(self):
        for q in (3,4,5,7,8,9,11,16,25,101,1009):
            x=wenger_W2_spectral_parameters(q)
            r=q-1
            self.assertEqual(x["uniform_fixed_operator_kappa"],3)
            self.assertEqual(x["uniform_quadratic_excess_C"],3)
            self.assertEqual(x["optimal_integer_centered_kappa_for_this_q"],
                3 if q==3 else 2 if q==4 else 1)
            if q>=5:
                self.assertLessEqual(x["exact_centered_F0_norm_squared"],r**3)
                self.assertEqual(x["fixed_asymptotic_centered_kappa_for_all_q_ge5"],1)
            self.assertGreater(x["actual_Moore_excess_each"],0)
            self.assertLessEqual(x["actual_Moore_excess_each"],3*r*r)
            self.assertLessEqual(x["exact_centered_F0_norm_squared"],3*r**3)
            self.assertEqual(
                x["exact_centered_F0_norm_squared"],
                max(q*(q-2)**2,8*q))
            self.assertTrue(x["published_W2_not_newly_discovered"])

    def test_15_wenger_moment_gate_is_TOO_STRONG_despite_spectral_success(self):
        # A crucial fail-closed distinction: the finite-degree S6 bound
        # is sufficient but unnecessary for the real known infinite
        # quadratic-excess family. For large q, S6/r9 grows ~q^2.
        for q in (5,11,23,47,101,211):
            x=wenger_W2_spectral_parameters(q)
            m1=x["eigen_multiplicities_BBt"]["q"]
            m2=x["eigen_multiplicities_BBt"]["two_q"]
            self.assertEqual(m1,2*q*(q-1))
            self.assertEqual(m2,q*(q-1)**2//2)
            S6=x["centered_source_sixth_moment"]
            self.assertEqual(S6,m1*(q*(q-2)**2)**3+m2*(8*q)**3)
            self.assertGreater(Q(S6,(q-1)**9),Q(q*q,64))
            self.assertLessEqual(x["exact_centered_F0_norm_squared"],
                                 3*(q-1)**3)

    def test_16_actual_wenger_adversarial_label_source_conflict_transfer(self):
        m=wenger_W2_prime_source(3)
        for scheme in ("lex","correlated"):
            maps=typed_maps(m,scheme)
            z=dict(m,**maps)
            from gio_t3c_intrinsic_defect import defect_matrices
            Dp,Dl,_=defect_matrices(z)
            pt=typed_conflicts_and_gram(z,z["f"],z["neighbors_point"],
                                        Dp,z["s"],z["t"])
            ln=typed_conflicts_and_gram(z,z["g"],z["neighbors_line"],
                                        Dl,z["t"],z["s"])
            J=direct_original_owner_conflicts(z,z)["J"]
            fixed=uniform_direct_spectral_constants(1,3,3)
            r=z["s"]
            self.assertEqual(J,pt["e_col"]+ln["e_col"])
            self.assertLessEqual(J,
                fixed["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(pt["gram"]**2,
                fixed["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(ln["gram"]**2,
                fixed["original_pencil_Gram_G0"]**2*r**11)

    def test_17_wenger_conditional_T3_applies_to_real_infinite_family(self):
        x=self.data["explicit_infinite_Wenger_nongq_quadratic_T3"]
        self.assertEqual(x["source_fixed_parameters"],{"b":1,"C":3,"kappa":1})
        self.assertEqual(x["independently_valid_all_q_ge3_weaker_kappa"],3)
        self.assertTrue(x["arbitrary_complete_minimal_injective_factor_maps"])
        self.assertTrue(x["published_W2_is_known_induced_GQ_subgraph"])
        self.assertTrue(x["cited_published_spectrum_is_NOT_our_novelty"])
        self.assertTrue(x["example_formal_ledger"]["moment_sixth_condition_is_NOT_required"])
        self.assertTrue(x["no_external_numeric_C6_theorem_constants_certified"])

    def test_19_actual_Wenger_historical_source_six_ID_threeway_inverse(self):
        selected=self.data["actual_Wenger_historical_original_BBo_inverses"]
        self.assertEqual(len(selected),3)
        self.assertEqual({x["scheme"] for x in selected},{"lex","correlated"})
        for z in selected:
            self.assertEqual(z["kind"],"actual_Wenger_W2_prime3")
            self.assertEqual(z["ORIGINAL_source_flags"],81)
            self.assertGreater(z["frozen_original_source_missing_pairs"],0)
            self.assertTrue(z["actual_produced_original_BBo_inverse_three_way_checked"])
            self.assertTrue(z["no_projected_anchor_filled_from_GQ"])
            self.assertLessEqual(z["actual_CORE_survivor_flags"],
                                 z["actual_FULL_survivor_flags"])
            self.assertEqual(
                z,wenger_original_six_id_inverse_case(z["scheme"],z["mask"]))

    def test_18_prime_power_scope_not_confused_with_prime_only_literal_oracle(self):
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        with self.assertRaises(ValueError):
            wenger_W2_prime_source(4)
        with self.assertRaises(ValueError):
            wenger_W2_prime_source(2)
        # The published theorem guarantees q=4,8,9,16,.. over finite
        # fields, whereas our literal Python finite-field oracle is
        # deliberately ONLY Z/q for prime q.
        x=wenger_W2_spectral_parameters(4)
        self.assertTrue(x["actual_family_exists_for_all_prime_powers_q_ge3_by_published_work"])


if __name__=="__main__":
    unittest.main()
