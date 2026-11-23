"""Independent GIO-003 G6-D3 affine arcs, Fourier characters and actual sources."""
from collections import Counter
from itertools import combinations,product
from math import comb,gcd
import unittest

from gio_t3d3_affine_arc import (
    SCHEMA,PARENT_G6D2,Field,affine_arc_oracle,
    source_from_affine_arc,fourier_root_character_census,
    binary_fourth_power_all_order,finite_arc_case,
    bad_curve_falsifier,arc_family_theorem,certificate,
)
from gio_t3d2_centered_sixth import (
    wenger_W2_spectral_parameters,integrated_quadratic_direct_ledger,
    wenger_W2_prime_source,
)
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,direct_original_owner_conflicts,
)
from gio_t3c2_partial_books import inverse_certificate,selected_mask
from fractions import Fraction as Q


def independent_incidences(field,exponent):
    """Independently construct actual Fq field graph from LINE-FIRST."""
    q=field.q
    p=list(product(range(q),repeat=3))
    out=[]
    for a,b,c in product(range(q),repeat=3):
        ids=[]
        for idx,(u,v,w) in enumerate(p):
            first=field.add(b,v)==field.mul(a,u)
            last=field.add(c,w)==field.mul(a,field.power(u,exponent))
            if first and last:
                ids.append(idx)
        out.append(tuple(ids))
    return tuple(out)


def independent_arc_det(field,exponent):
    """Explicit no-three-collinear determinant, not production slope test."""
    h={u:field.power(u,exponent) for u in range(field.q)}
    bad=[]
    for u,v,w in combinations(range(field.q),3):
        d=field.sub(
           field.mul(field.sub(v,u),field.sub(h[w],h[u])),
           field.mul(field.sub(w,u),field.sub(h[v],h[u])))
        if d==0:
            bad.append((u,v,w))
    return bad


def independent_fourier_root_hist(field,exponent):
    """Field-linear polynomial root count independently of graph builder."""
    q=field.q
    h=[field.power(z,exponent) for z in range(q)]
    counts=Counter()
    for a,b,c in product(range(q),repeat=3):
        count=0
        for u in range(q):
            lhs=field.add(a,field.add(field.mul(b,u),
                                    field.mul(c,h[u])))
            count+=(lhs==0)
        counts[count]+=1
    return counts


class TestG6D3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.finite={(z["q"],z["exponent"],z["scheme"]):z
                    for z in cls.c["actual_finite_source_falsifiers"]}

    def test_01_strict_scope_fixed_parent_and_no_novelty_fabrication(self):
        z=self.c
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6D2_HEAD"],PARENT_G6D2)
        self.assertEqual(z["issue"],793)
        self.assertEqual(z["claim"],"STRUCTURAL_AFFINE_ARC_TO_QUADRATIC_T3_ALL_FAMILIES")
        self.assertTrue(z["projective_arc_incidence_construction_prior_art"])
        self.assertTrue(z["generalized_Wenger_Cayley_character_method_prior_art"])
        self.assertTrue(z["new_Mathlab_contribution_conditional_six_source_ID_transfer"])
        self.assertTrue(z["no_unconditional_every_quadratic_source_T3"])
        self.assertTrue(z["no_independent_external_review_or_Lean"])

    def test_02_exact_prime_field_oracles_and_no_composite_fake_field(self):
        for q in (3,5,7):
            f=Field(q)
            for x in range(1,q):
                self.assertEqual(f.mul(x,f.inv(x)),1)
            for a,b,c in product(range(q),repeat=3):
                self.assertEqual(f.mul(a,f.add(b,c)),
                    f.add(f.mul(a,b),f.mul(a,c)))
        for bad in (1,2,6,9,12,True):
            with self.assertRaises(ValueError):
                Field(bad)

    def test_03_exact_binary_finite_field_multiplication_and_inverses(self):
        for q in (4,8,16,32):
            f=Field(q)
            for x in range(1,q):
                self.assertEqual(f.mul(x,f.inv(x)),1)
            for a,b,c in product(range(min(q,8)),repeat=3):
                self.assertEqual(f.mul(a,f.add(b,c)),
                    f.add(f.mul(a,b),f.mul(a,c)))
                self.assertEqual(f.mul(a,b),f.mul(b,a))
            for x in range(q):
                self.assertEqual(f.power(x,q),x)

    def test_04_independent_arc_determinants_and_slope_census(self):
        for q,e in ((3,2),(5,2),(8,2),(8,4),(4,4),(16,4)):
            f=Field(q)
            arc=affine_arc_oracle(f,e)
            bad=independent_arc_det(f,e)
            self.assertEqual(arc["literal_all_collinear_triples"],bad)
            self.assertEqual(arc["projective_arc"],not bool(bad))
            self.assertEqual(arc["noncollinear_triples"],comb(q,3)-len(bad))

    def test_05_prime_and_binary_arc_source_are_real_girth8_graphs(self):
        for z in self.c["actual_finite_source_falsifiers"]:
            q=z["q"]
            self.assertTrue(z["actual_girth_at_least_8"])
            self.assertEqual(z["actual_source_points"],q**3)
            self.assertEqual(z["actual_source_lines"],q**3)
            self.assertEqual(z["actual_SOURCE_original_flags"],q**4)
            self.assertEqual(z["correct_fixed_source_degree"],q)
            self.assertEqual(z["source_nongq_moore_excess"],2*q*(q-1))
            self.assertEqual(z["original_missing_projections"],
                             q**3*2*q*(q-1))
            self.assertEqual(z["original_existing_projections"],
                             q**4*(q-1)**2)
            self.assertTrue(z["forced_connected_at_quadratic_scale"])
            self.assertTrue(z["actual_genuine_graph_NOT_synthetic_F"])
            self.assertTrue(z["no_ambient_GQ_assumption"])

    def test_06_independent_literal_line_first_builder_on_binary_q8(self):
        f=Field(8)
        m=source_from_affine_arc(f,4)
        self.assertEqual(m["lines"],independent_incidences(f,4))
        self.assertEqual(len(m["flags"]),8**4)
        self.assertEqual(len(m["missing"]),8**3*2*8*7)

    def test_07_exact_Wenger_prime_q3_q5_equivalence(self):
        for q in (3,5):
            p=source_from_affine_arc(Field(q),2)
            g=wenger_W2_prime_source(q)
            self.assertEqual(p["lines"],g["lines"])
            self.assertEqual(p["flags"],g["flags"])
            self.assertEqual(p["projected"],g["projected"])
            self.assertEqual(p["missing"],g["missing"])

    def test_08_bad_even_power4_collinear_and_graph_C6_rejection(self):
        v=self.c["actual_bad_source_negative_controls"][0]
        self.assertEqual((v["q"],v["exponent"]),(4,4))
        self.assertTrue(v["original_C6_rejected_by_independent_graph_checker"])
        self.assertIn("6-cycle",v["actual_incidence_first_rejection"])
        self.assertFalse(self.c["q16_nonarc_det_only"]["projective_arc"])
        for q in (4,16):
            with self.assertRaises(ValueError):
                source_from_affine_arc(Field(q),4,require_arc=True)

    def test_09_exact_additive_characters_root_hist_independent(self):
        for q,e in ((3,2),(5,2),(8,2),(8,4)):
            f=Field(q)
            x=fourier_root_character_census(f,e)
            z=independent_fourier_root_hist(f,e)
            self.assertEqual(x["dual_characters_enumerated"],q**3)
            self.assertEqual(z[q],1)
            self.assertEqual(set(z),{0,1,2,q})
            self.assertEqual(z[2],q*(q-1)**2//2)
            self.assertEqual(z[1],2*q*(q-1))
            self.assertEqual(x["exact_zero_count_multiplicity"],
                {str(i):z.get(i,0) for i in (0,1,2,q)})

    def test_10_arc_binary_h2_h4_q8_cospectral_and_different_curves(self):
        x=self.finite[8,2,"lex"]
        y=self.finite[8,4,"lex"]
        self.assertNotEqual([Field(8).power(u,2) for u in range(8)],
                            [Field(8).power(u,4) for u in range(8)])
        self.assertEqual(x["Fourier"]["exact_zero_count_multiplicity"],
                         y["Fourier"]["exact_zero_count_multiplicity"])
        self.assertEqual(x["Fourier"]["centered_F0_norm_squared"],
                         y["Fourier"]["centered_F0_norm_squared"])
        self.assertEqual(x["source_nongq_moore_excess"],
                         y["source_nongq_moore_excess"])
        # These are different polynomial curves; no unsupported
        # claim that their graphs are not isomorphic.

    def test_11_cayley_point_line_eigen_counts_and_multiplicities_all_sources(self):
        for z in self.c["actual_finite_source_falsifiers"]:
            q=z["q"];f=z["Fourier"]
            self.assertEqual(f["principal_BBt_eigenvalue"],q*q)
            self.assertEqual(f["centered_BBt_eigenvalues"],[0,q,2*q])
            self.assertEqual(sum(f["exact_zero_count_multiplicity"].values()),q**3)
            self.assertTrue(f["Fourier_characters_proof_uses_arc_root_bound"])
            self.assertTrue(f["integer_root_counts_no_floating_eigensolver"])

    def test_12_quadratic_excess_uniform_real_source_spectral_bound(self):
        for z in self.c["actual_finite_source_falsifiers"]:
            q=z["q"];r=q-1;v=z["Fourier"]
            self.assertEqual(v["original_source_Moore_excess"],2*q*r)
            self.assertLessEqual(2*q*r,3*r*r)
            self.assertEqual(v["centered_F0_norm_squared"],
                max(q*(q-2)**2,8*q))
            self.assertEqual(v["minimal_integer_kappa"],
                3 if q==3 else 2 if q==4 else 1)
            if q>=5:
                self.assertLessEqual(v["centered_F0_norm_squared"],r**3)

    def test_13_all_order_binary_exponent_4_odd_e_only_arc(self):
        for e in range(2,22):
            z=binary_fourth_power_all_order(e)
            self.assertEqual(z["power_map_cube_injective"],e%2==1)
            self.assertEqual(z["projective_arc_exactly_if_odd_e"],e%2==1)
            if e>=3 and e%2:
                self.assertTrue(z["actual_infinite_nongq_family_when_e_odd_ge3"])
                self.assertEqual((z["fixed_b"],z["fixed_C"],z["fixed_kappa"]),
                                 (1,3,1))
            else:
                self.assertFalse(z["actual_infinite_nongq_family_when_e_odd_ge3"])

    def test_14_source_flag_load_and_original_missing_full_projections(self):
        m=source_from_affine_arc(Field(3),2)
        self.assertEqual(len(m["flags"]),3**4)
        self.assertTrue(all(z==3*(3-1)**2
                       for z in m["projection_load"].values()))
        self.assertEqual(len(m["projected"]),3**4*(3-1)**2)
        self.assertEqual(len(m["missing"]),27*12)
        self.assertEqual(len(set(m["projected"])&set(m["missing"])),0)

    def test_15_arbitrary_lex_and_correlated_labels_do_not_enter_arc_spectrum(self):
        x=self.finite[8,4,"lex"]
        y=self.finite[8,4,"correlated"]
        self.assertEqual(x["Fourier"],y["Fourier"])
        self.assertEqual(x["source_nongq_moore_excess"],y["source_nongq_moore_excess"])
        self.assertEqual(x["minimal_pair_alphabet_first"],y["minimal_pair_alphabet_first"])

    def test_16_original_owner_conflicts_on_true_binary_arc_with_correlated_labels(self):
        # A separate ownership census on the actual non-GQ q=8 source,
        # without calculating a dense floating matrix eigen decomposition.
        m=source_from_affine_arc(Field(8),4)
        from gio_t3d2_centered_sixth import uniform_direct_spectral_constants
        from gio_t3c_intrinsic_defect import defect_matrices,typed_conflicts_and_gram
        for scheme in ("lex","correlated"):
            labels=typed_maps(m,scheme)
            full=dict(m,**labels)
            Dp,Dl,_=defect_matrices(full)
            pp=typed_conflicts_and_gram(full,full["f"],full["neighbors_point"],
                                        Dp,full["s"],full["t"])
            ll=typed_conflicts_and_gram(full,full["g"],full["neighbors_line"],
                                        Dl,full["t"],full["s"])
            J=direct_original_owner_conflicts(full,full)["J"]
            constants=uniform_direct_spectral_constants(1,3,1)
            r=7
            self.assertEqual(J,pp["e_col"]+ll["e_col"])
            self.assertLessEqual(J,
                  constants["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(pp["gram"]**2,
                  constants["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(ll["gram"]**2,
                  constants["original_pencil_Gram_G0"]**2*r**11)

    def test_17_arc_to_original_HYP105_T3_theorem_uses_fixed_family_params(self):
        theorem=self.c["general_affine_projective_q_arc_theorem"]
        self.assertEqual(theorem["fixed_parameters"],{"b":1,"C":3,"kappa":1})
        self.assertTrue(theorem["all_HYP105_original_six_source_flags"])
        self.assertTrue(theorem["actual_full_core_BBo_inverse_from_parent"])
        self.assertTrue(theorem["no_GQ_template_needed_by_source_proof"])
        self.assertTrue(theorem["all_external_ordinary_C6_numbers_FORMAL_ONLY"])
        self.assertTrue(theorem["no_unrestricted_T3_or_ASET_claim"])
        ledger=theorem["exact_formal_parameter_ledger"]
        self.assertEqual(ledger["fixed_before_source"]["centered_operator_kappa"],1)
        self.assertEqual(ledger["fixed_before_source"]["quadratic_C"],3)
        self.assertEqual(ledger["fixed_before_source"]["balance_b"],1)
        self.assertTrue(ledger["closure"]["four_LOW_errors_each_below_eps"])

    def test_18_rejected_arcs_do_not_get_invented_fourier_or_source_T3(self):
        for q,e in ((4,4),(16,4)):
            with self.assertRaises(ValueError):
                fourier_root_character_census(Field(q),e)
        with self.assertRaises(ValueError):
            affine_arc_oracle(Field(3),-1)

    def test_19_cited_Wenger_Fourier_spectrum_consistency_in_prime_cases(self):
        for q in (3,5):
            f=fourier_root_character_census(Field(q),2)
            published=wenger_W2_spectral_parameters(q)
            self.assertEqual(f["centered_F0_norm_squared"],
                             published["exact_centered_F0_norm_squared"])
            self.assertEqual(f["exact_centered_S6"],
                             published["centered_source_sixth_moment"])
            self.assertEqual(f["exact_zero_count_multiplicity"]["1"],
                             published["eigen_multiplicities_BBt"]["q"])
            self.assertEqual(f["exact_zero_count_multiplicity"]["2"],
                             published["eigen_multiplicities_BBt"]["two_q"])


if __name__=="__main__":
    unittest.main()
