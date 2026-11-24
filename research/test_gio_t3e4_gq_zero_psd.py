"""G6-E4 independent exact original GQ minus matching ZERO-PSD tests."""
import unittest
from fractions import Fraction as Q
from itertools import product
from collections import Counter

from gio_t3d3_affine_arc import Field
from gio_t3e1_subgq_pds import actual_smaller_source
from gio_t3e2_corrigendum_quasi_pds import actual_corrigendum_source
from gio_t3e3_even_corrigendum import actual_even_source
from gio_t3c_intrinsic_defect import typed_maps
from gio_t3d7_local_psd_rowtop import (
    minimal_pair_alphabet,source_local_constants,
    integrated_local_ledger,
)
from gio_t3e4_gq_zero_psd import (
    SCHEMA,PARENT_G6E3,PAPER,exact_zero_PSD_gate,require_zero,
    require_status,universal_threshold,
    actual_original_embedding,
    independent_original_collinearity_conflicts,
    literal_zero_case,local_zero_FORMAL_ledgers,certificate,
)


def independently_count_collinearity_edges(src,side):
    """A second brute original vertex-by-source-line collinearity oracle."""
    if side=="point":
        n=src["points"]
        counts=Counter()
        for line in src["lines"]:
            for i in line:
                for j in line:
                    if i<j:
                        counts[i,j]+=1
    elif side=="line":
        n=len(src["lines"])
        on=[set() for _ in range(src["points"])]
        for ell,line in enumerate(src["lines"]):
            for p in line:
                on[p].add(ell)
        counts=Counter()
        for inc in on:
            for i in inc:
                for j in inc:
                    if i<j:
                        counts[i,j]+=1
    else:
        raise ValueError("typed actual source")
    assert all(v==1 for v in counts.values())
    return n,counts


def independent_a_from_f(src,side,scheme):
    labels=typed_maps(src,scheme)
    f=labels["f" if side=="point" else "g"]
    n,col=independently_count_collinearity_edges(src,side)
    a=minimal_pair_alphabet(n)
    assert len(f)==n
    assert len(set(tuple(sorted(f[i])) for i in range(n)))==n
    assert all(len(set(f[i]))==2 for i in range(n))
    return sum(bool(set(f[i])&set(f[j])) for i,j in col),a


class TestZeroPSDE4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=certificate()
        cls.finite={(x["family"],x["q"],x["scheme"]):x
                    for x in cls.z["true_original_girth8_sources_and_both_typed_flags"]}

    def test_01_scope_parent_and_no_unrestricted_theorem(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6E3_HEAD"],PARENT_G6E3)
        self.assertEqual(z["issue"],793)
        self.assertEqual(z["corrected_2021_source_publication"],PAPER)
        self.assertTrue(z["existing_G6D7_original_PSD_rowtop_source_gate_APPLIED"])
        self.assertTrue(z["new_structural_GQ_submatrix_minus_bounded_matchings"])
        self.assertTrue(z["original_corrected_even_and_odd_families_PREEXIST"])
        self.assertTrue(z["original_GQ_and_singular_perturbation_prior_art"])
        self.assertTrue(z["no_synthetic_F_and_no_assumed_positive_trace_tail"])
        self.assertTrue(z["no_unrestricted_T3_or_new_GF5_ASET_exponent"])
        self.assertTrue(z["no_external_human_referee_or_Lean"])

    def test_02_exact_zero_W_certificate_d0_all_ge3_ell2(self):
        for q in range(3,81):
            a=require_zero(q,0,2)
            self.assertEqual(a["original_degree"],q)
            self.assertEqual(a["r"],q-1)
            self.assertEqual(a["ell"],2)
            self.assertTrue(a["W_zero_on_both_original_types_sufficient"])
            self.assertEqual(a["local_PSD_rowtop_M"],0)

    def test_03_exact_d1_ell4_all_q7_and_above(self):
        for q in range(7,110):
            self.assertTrue(require_status(q,1,4))
        self.assertFalse(require_status(5,1,4))

    def test_04_exact_d1_ell3_boundary_q7_rejected_q8_accepted(self):
        self.assertFalse(require_status(7,1,3))
        self.assertTrue(require_status(8,1,3))
        self.assertTrue(all(require_status(q,1,3)
                            for q in range(8,110)))
        with self.assertRaises(ValueError):
            require_zero(7,1,3)

    def test_05_exact_d1_ell2_boundary_q17_q18(self):
        self.assertFalse(require_status(17,1,2))
        self.assertTrue(require_status(18,1,2))
        self.assertTrue(all(require_status(q,1,2)
                            for q in range(18,150)))
        with self.assertRaises(ValueError):
            require_zero(8,1,2)

    def test_06_actual_published_prime_power_odd_even_subfamilies(self):
        for q in (7,9,11,13,17):
            self.assertTrue(require_status(q,1,4))
            if q>=9: self.assertTrue(require_status(q,1,3))
        for q in (19,23,25,27,31,37):
            self.assertTrue(require_status(q,1,2))
        for q in (8,16):
            self.assertTrue(require_status(q,1,3))
        for q in (32,64,128):
            self.assertTrue(require_status(q,1,2))

    def test_07_multimatching_general_proof_only_no_fabricated_existence(self):
        for q,d,ell in ((64,2,2),(128,3,2),(64,1,2)):
            w=require_zero(q,d,ell)
            self.assertTrue(w["original_SVD_and_matching_embedding_REQUIRED"])
            self.assertTrue(w["actual_source_quadratic_Moore_excess_is_SEPARATE_requirement"])
            self.assertTrue(w["no_new_graph_existence_from_abstract_d"])
        self.assertFalse(require_status(32,2,2))
        self.assertFalse(require_status(64,3,2))
        self.assertEqual(require_zero(64,2,2)["original_degree"],62)
        self.assertEqual(require_zero(128,3,2)["original_degree"],125)

    def test_08_integer_tail_thresholds_monotone_proof(self):
        expected={(0,2):3,(1,4):6,(1,3):8,(1,2):18,
                  (2,2):54,(3,2):109}
        for (d,ell),start in expected.items():
            z=universal_threshold(d,ell)
            self.assertEqual(z["integer_q_tail_threshold"],start)
            self.assertTrue(z["valid_all_larger_integer_q_by_monotonic_linear_over_sqrt"])
            self.assertTrue(z["does_NOT_assert_all_integer_q_are_prime_powers"])
        self.assertEqual(len(self.z["automatic_all_integer_q_tail_thresholds"]),6)

    def test_09_fail_closed_invalid_exact_gates_and_boolean(self):
        for args in ((2,0,2),(3,-1,2),(3,1,2),(8,6,2),
                     (8,1,-1),(True,0,2),(8,False,3),
                     (8,1,3.0)):
            with self.assertRaises(ValueError):
                exact_zero_PSD_gate(*args)
        for args in ((1,2),(2,1),(-1,2),(1,1)):
            with self.assertRaises(ValueError):
                universal_threshold(*args)

    def test_10_independent_true_published_E1_parent_embedding(self):
        for q in (3,4):
            v=actual_original_embedding("E1",q)
            self.assertEqual(v["d"],0)
            self.assertEqual(v["matching_original_edges"],0)
            self.assertTrue(v["published_actual_original_GQ_parent_incidence_verified"])
            self.assertTrue(v["original_final_edges_identical_to_parent_restriction_minus_matching"])
            self.assertTrue(v["original_parent_GQ_has_zero_Moore_excess"])
            self.assertEqual(v["source"]["points"],q*(q*q-2))

    def test_11_independent_true_CORRECTED_ODD_original_embedding(self):
        v=actual_original_embedding("E2-ODD",7,x=2,y=3)
        self.assertEqual(v["d"],1)
        self.assertEqual(v["matching_original_edges"],14)
        self.assertTrue(v["original_final_edges_identical_to_parent_restriction_minus_matching"])
        self.assertEqual(v["source"]["points"],266)
        self.assertEqual(len(v["source"]["flags"]),1596)
        self.assertEqual(v["source"]["excess_lines"],110)

    def test_12_independent_true_CORRECTED_EVEN_original_embedding(self):
        v=actual_original_embedding("E3-EVEN",8,x=2,m=3)
        self.assertEqual(v["d"],1)
        self.assertEqual(v["matching_original_edges"],24)
        self.assertTrue(v["original_final_edges_identical_to_parent_restriction_minus_matching"])
        self.assertEqual(v["source"]["points"],416)
        self.assertEqual(len(v["source"]["flags"]),2912)
        self.assertEqual(v["source"]["excess_lines"],157)

    def test_13_independent_true_point_line_source_collinearity_degree(self):
        for family,q,opts in (
            ("E1",3,{}),("E1",4,{}),
            ("E2-ODD",7,{"x":2,"y":3}),
            ("E3-EVEN",8,{"x":2,"m":3})):
            src=actual_original_embedding(family,q,**opts)["source"]
            d=0 if family=="E1" else 1
            degree=(q-d)*(q-d-1)
            for side in ("point","line"):
                n,col=independently_count_collinearity_edges(src,side)
                self.assertEqual(n,src["points"])
                self.assertEqual(2*len(col),n*degree)

    def test_14_independent_lex_label_original_conflicts_BOTH_types(self):
        for family,q,opts in (
            ("E1",3,{}),("E1",4,{}),
            ("E2-ODD",7,{"x":2,"y":3}),
            ("E3-EVEN",8,{"x":2,"m":3})):
            src=actual_original_embedding(family,q,**opts)["source"]
            for side in ("point","line"):
                got,a=independent_a_from_f(src,side,"lex")
                key=(family,q,"lex")
                self.assertEqual(got,self.finite[key][
                    "independent_original_"+side+"_conflicts"])
                self.assertEqual(a,self.finite[key]["exact_minimal_alphabet"])

    def test_15_independent_correlated_label_original_conflicts(self):
        for family,q,opts in (
            ("E1",4,{}),
            ("E2-ODD",7,{"x":2,"y":3}),
            ("E3-EVEN",8,{"x":2,"m":3})):
            src=actual_original_embedding(family,q,**opts)["source"]
            for side in ("point","line"):
                got,a=independent_a_from_f(src,side,"correlated")
                self.assertEqual(got,self.finite[family,q,"correlated"][
                    "independent_original_"+side+"_conflicts"])

    def test_16_all_finite_trace_source_conflict_gate_with_zero_PSD_W(self):
        for z in self.z["true_original_girth8_sources_and_both_typed_flags"]:
            self.assertTrue(z["actual_original_parent_subset_minus_matching"])
            self.assertTrue(z["both_types_original_W_zero_source_gate"])
            self.assertTrue(z["M_zero_fixed_before_labels"])
            self.assertEqual(z["rowtop_W_zero_exact"],0)
            self.assertTrue(z["no_D2_F0_norm_or_positive_tail_hypothesis"])
            self.assertLessEqual(z["independent_original_point_conflicts"],
                                 z["direct_trace_conflict_cap"])
            self.assertLessEqual(z["independent_original_line_conflicts"],
                                 z["direct_trace_conflict_cap"])
            self.assertEqual(z["exact_original_total_J"],
                z["independent_original_point_conflicts"]+
                z["independent_original_line_conflicts"])
            self.assertGreaterEqual(z["point_original_pencil_Gram"],0)
            self.assertGreaterEqual(z["line_original_pencil_Gram"],0)

    def test_17_SMALL_true_GQ_source_exact_Sylvester_W0_BOTH_sides(self):
        for key in (("E1",3,"lex"),("E1",4,"correlated")):
            z=self.finite[key]
            self.assertEqual(len(z["exact_source_small_Sylvester_zero_W"]),2)
            for side in ("point","line"):
                cert=z["exact_source_small_Sylvester_zero_W"][side]
                self.assertEqual(cert["W_PSD_exact_inertia"]["negative"],0)
                self.assertEqual(cert["W_dominance_PSD_exact_inertia"]["negative"],0)
                self.assertEqual(cert["M"],0)
                self.assertEqual(Q(cert["local"]["exact_rowtop_energy"]),Q(0))
                self.assertTrue(cert["exact_r4_local_budget"])

    def test_18_exact_symbolic_regime_table_and_negative_controls(self):
        got={(x["q"],x["d"],x["ell"]):
             x["W_zero_on_both_original_types_sufficient"]
             for x in self.z["all_order_exact_integer_sqrt_gate_witnesses"]}
        for key,val in (((7,1,3),False),((8,1,2),False),
                        ((17,1,2),False),((32,2,2),False),
                        ((7,1,4),True),((8,1,3),True),
                        ((18,1,2),True),((64,2,2),True),
                        ((128,3,2),True)):
            self.assertEqual(got[key],val)

    def test_19_four_FORMAL_G6D7_legacy_original_FULL_CORE_ledgers(self):
        z=self.z["inherited_G6D7_ZERO_ROW_TOP_FORMAL_ledgers"]
        self.assertEqual(len(z),4)
        values=[(x["source"]["quadratic_excess_C"],
                 x["source"]["cutoff_ell"],
                 x["source"]["local_PSD_M"]) for x in z]
        self.assertEqual(values,[(2,2,0),(5,4,0),(5,3,0),(5,2,0)])
        for x in z:
            d=x["inherited_G6D7_FORMAL_only_ledger"]
            self.assertTrue(d["FORMAL_ONLY"])
            self.assertTrue(d["source"]["no_global_Schatten_or_trace_gate"])
            self.assertEqual(d["fixed_before_source"]["local_M"],0)
            c=d["closure"];m=d["moments"];f=d["fixed_before_source"]
            eps=Q(c["eps"]);rho=Q(c["rho"]);r=int(c["sufficient_r0"])
            self.assertLessEqual(m["improper"],eps*r)
            self.assertLessEqual(m["E"]**2,eps**2*r)
            self.assertLessEqual(m["D"]**8,eps**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*rho*d["selector"]["q3"]**2*m["L6"],
                                 eps**2)
            self.assertGreater(Q(c["delta"]),0)

    def test_20_source_existence_is_separate_from_abstract_d(self):
        for q,d,ell in ((64,2,2),(128,3,2)):
            z=require_zero(q,d,ell)
            self.assertTrue(z["no_new_graph_existence_from_abstract_d"])
            self.assertTrue(z["actual_source_quadratic_Moore_excess_is_SEPARATE_requirement"])
            self.assertTrue(z["original_SVD_and_matching_embedding_REQUIRED"])
        with self.assertRaises(ValueError):
            actual_original_embedding("synthetic-d2",64)

    def test_21_geometry_wrong_match_flag_negatives(self):
        odd=actual_original_embedding("E2-ODD",7,x=2,y=3)
        even=actual_original_embedding("E3-EVEN",8,x=2,m=3)
        self.assertNotEqual(odd["source"]["points"],even["source"]["points"])
        self.assertEqual((odd["matching_original_edges"],even["matching_original_edges"]),
                         (14,24))
        self.assertTrue(odd["no_synthetic_missing_F_or_completed_original_projection"])
        self.assertTrue(even["no_synthetic_missing_F_or_completed_original_projection"])

    def test_22_math_is_source_only_NOT_finite_asymptotic_T3(self):
        z=self.z
        self.assertTrue(z["no_unrestricted_T3_or_new_GF5_ASET_exponent"])
        self.assertTrue(z["no_external_human_referee_or_Lean"])
        for x in z["true_original_girth8_sources_and_both_typed_flags"]:
            self.assertIn(x["family"],("E1","E2-ODD","E3-EVEN"))
            self.assertTrue(x["no_D2_F0_norm_or_positive_tail_hypothesis"])


if __name__=="__main__":
    unittest.main()
