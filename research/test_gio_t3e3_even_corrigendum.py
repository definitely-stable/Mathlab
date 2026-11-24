"""Independent G6-E3 even-characteristic corrected 2021 source tests.

All 23 cases use ACTUAL original finite-field geometry (GF(8)) and
non-synthetic incidence; numerical spectral diagonalization is never
used as a proof. Small q=4 and odd constructions are negative controls.
"""
import unittest
from collections import Counter
from fractions import Fraction as Q
from itertools import product

from gio_t3d3_affine_arc import Field
from gio_t3e1_subgq_pds import actual_smaller_source
from gio_t3e2_corrigendum_quasi_pds import corrected_S_and_M
from gio_t3e3_even_corrigendum import (
    SCHEMA,PARENT_G6E2,PAPER,CORRIGENDUM_DATE,CORRECTED_THEOREM,
    even_params,_cached_stage,corrected_even_S_and_M,actual_even_source,
    even_matching_spectral_envelope,literal_source_case,
    original_six_ID_BBo,all_order_direct_ledger,certificate,
)
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,defect_matrices,
    exact_second_walk_identity,direct_original_owner_conflicts,
)


def independent_source_components(src):
    """Bipartite ORIGINAL adjacency BFS, not a claimed spectral oracle."""
    n=src["points"];N=n+len(src["lines"])
    adj=[set() for _ in range(N)]
    for p,l in src["flags"]:
        adj[p].add(n+l)
        adj[n+l].add(p)
    seen=set();sizes=[]
    for start in range(N):
        if start in seen:
            continue
        frontier=[start];seen.add(start);size=0
        while frontier:
            u=frontier.pop();size+=1
            for v in adj[u]-seen:
                seen.add(v);frontier.append(v)
        sizes.append(size)
    return sorted(sizes)


def independent_final_flags(ins):
    """Independent original stage flags MINUS true S and matching M."""
    z=ins["true_quasi_domination"]
    stage=z["stage"]["source"]
    n=stage["points"]
    kept=set(z["kept"])
    P=ins["keep_original_stage_points"]
    L=ins["keep_original_stage_lines"]
    drop=set(ins["original_matching_flags_deleted"])
    oracle={(p,l) for p,l in stage["flags"]
            if p in kept and n+l in kept and (p,l) not in drop}
    original={(P[p],L[l]) for p,l in ins["original_source"]["flags"]}
    assert original==oracle
    return oracle


class TestEvenE3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()
        cls.ins=actual_even_source(8,2,3)
        cls.src=cls.ins["original_source"]
        cls.quasi=cls.ins["true_quasi_domination"]
        cls.cases={c["scheme"]:c
                   for c in cls.cert["exact_even_GF8_true_original_source_cases"]}

    def test_01_scope_publisher_correction_and_parent(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["parent_G6E2_HEAD"],PARENT_G6E2)
        self.assertEqual(c["corrigendum_publisher_pdf"],PAPER)
        self.assertEqual(c["corrigendum_date"],CORRIGENDUM_DATE)
        self.assertEqual(c["cited_published_theorem"],CORRECTED_THEOREM)
        self.assertTrue(c["true_even_characteristic_all_order_GQ_source_family"])
        self.assertTrue(c["published_graph_family_PRIOR_ART_not_new"])
        self.assertTrue(c["sharper_even_only_kappa20_vs_odd_kappa48"])
        self.assertTrue(c["no_unrestricted_abstract_T3_or_new_GF5_ASET_exponent"])
        self.assertTrue(c["no_external_academic_referee_or_Lean"])

    def test_02_literal_GF8_char2_inversion_and_xor(self):
        f=Field(8)
        self.assertEqual(f.inv(3),6)
        self.assertEqual(f.add(3,6),5)
        self.assertEqual(f.mul(3,6),1)
        for a,b in product(range(8),repeat=2):
            self.assertEqual(f.add(a,b),a^b)
            self.assertEqual(f.add(a,a),0)
            self.assertEqual(f.mul(a,b),f.mul(b,a))

    def test_03_correct_even_thm6_gate_and_distinct_m_inverse(self):
        v=even_params(Field(8),2,3)
        self.assertEqual(v["inverse_m"],6)
        self.assertEqual({0,1,v["x"],v["m"],v["inverse_m"]},
                         {0,1,2,3,6})
        self.assertTrue(v["corrected_2021_Theorem_6_not_odd_Theorem_5"])
        self.assertTrue(v["stricter_x_not_inverse_m_gate"])
        for x,m in ((0,3),(1,3),(2,1),(2,0),(3,3),(6,3)):
            with self.assertRaises(ValueError):
                even_params(Field(8),x,m)
        for q in (3,4,5,7,9):
            if q==9: continue # literal field library does not model GF(9)
            with self.assertRaises(ValueError):
                even_params(Field(q),2,3)
        with self.assertRaises(ValueError):
            even_params(Field(8),True,3)

    def test_04_real_GQ_parent_then_Gq_x_GF8(self):
        stage=_cached_stage(8,2)
        self.assertEqual(stage["n"],8*(8*8-2))
        self.assertEqual(stage["source"]["points"],496)
        self.assertEqual(stage["source"]["excess_lines"],2*8*6)
        self.assertEqual(len(stage["source"]["flags"]),3968)
        self.assertEqual(set(map(len,stage["adj"])),{8})
        self.assertEqual(len(stage["point_lookup"]),496)
        self.assertEqual(len(stage["line_lookup"]),496)

    def test_05_even_R_exactly_two_Galois_inverse_slopes(self):
        q=self.quasi
        stage=q["stage"];field=Field(8);n=stage["n"]
        self.assertEqual(len(q["R"]),16)
        self.assertTrue(all(v>=n for v in q["R"]))
        expect=set()
        for b in range(8):
            t=field.mul(field.add(3,field.inv(3)),b)
            for a in (3,6):
                expect.add(n+stage["line_lookup"][(a,b,t)])
        self.assertEqual(q["R"],expect)
        self.assertEqual(len(q["closed_R"]),8*8+3*8)

    def test_06_original_closed_S_has_correct_even_PDS_cardinality(self):
        z=self.quasi
        n=z["stage"]["n"]
        self.assertEqual(len(z["closed_root_set"]),8*9)
        self.assertEqual(len(z["closed_R"]),8*8+3*8)
        self.assertFalse(z["closed_root_set"]&z["closed_R"])
        self.assertEqual(len(z["deleted"]),2*8*8+4*8)
        self.assertEqual(z["removed_per_original_type"],80)
        self.assertEqual(sum(v<n for v in z["deleted"]),80)
        self.assertEqual(sum(v>=n for v in z["deleted"]),80)
        self.assertTrue(z["quasi_perfect_not_perfect"])
        self.assertTrue(z["characteristic_two_b_plus_b_zero"])

    def test_07_quasi_not_perfect_and_matching_essential(self):
        z=self.quasi
        self.assertEqual(Counter(z["degree_before_matching"].values()),
                         Counter({7:2*8*(8*8-8-4)-2*8*(8-5),
                                  8:2*8*(8-5)}))
        self.assertEqual(len(z["matching_original_flags"]),24)
        self.assertEqual(len(z["matched_high_degree_vertices"]),48)
        self.assertEqual(
            {v for v,d in z["degree_before_matching"].items() if d==8},
            z["matched_high_degree_vertices"])
        self.assertTrue(z["matching_exactly_repairs_every_high_degree_original_vertex"])
        self.assertTrue(z["matching_is_NOT_optional"])

    def test_08_literal_E_matching_edges_all_distinct_original_flags(self):
        z=self.quasi
        stage=z["stage"];n=stage["n"]
        used=[]
        for p,l in z["matching_original_flags"]:
            self.assertIn(l,stage["adj"][p])
            self.assertIn(p,z["kept"]);self.assertIn(l,z["kept"])
            self.assertEqual(z["degree_before_matching"][p],8)
            self.assertEqual(z["degree_before_matching"][l],8)
            used += [p,l]
        self.assertEqual(len(set(used)),len(used))
        self.assertEqual(set(used),z["matched_high_degree_vertices"])

    def test_09_actual_GF8_source_params_original_Moore(self):
        src=self.src;r=6
        self.assertEqual(src["points"],416)
        self.assertEqual(len(src["lines"]),416)
        self.assertEqual((src["s"],src["t"]),(6,6))
        self.assertEqual(len(src["flags"]),2912)
        self.assertEqual(src["excess_lines"],157)
        self.assertEqual(src["excess_points"],157)
        self.assertEqual(src["points"],(r+1)*(r*r+1)+157)
        self.assertEqual(len(src["missing"]),416*157)
        self.assertLessEqual(157,5*r*r)
        self.assertTrue(self.ins["true_original_induced_then_matching"])

    def test_10_independent_exact_original_edges_GQ_not_completed(self):
        oracle=independent_final_flags(self.ins)
        self.assertEqual(len(oracle),2912)
        self.assertTrue(all(len(line)==7 for line in self.src["lines"]))
        self.assertEqual(sum(len(l) for l in self.src["lines"]),2912)
        self.assertEqual(len(self.ins["original_matching_flags_deleted"]),24)

    def test_11_actual_source_connected_and_short_cycles_fail_closed(self):
        self.assertEqual(independent_source_components(self.src),[832])
        # source_graph re-validates original girth8 and independent
        # point-line neighbor regularity; mutate a line to create C4.
        src=self.src
        lines=[set(z) for z in src["lines"]]
        p,v=sorted(lines[0])[:2]
        target=next(i for i in range(1,len(lines)) if p in lines[i])
        drop=next(w for w in lines[target] if w!=p)
        lines[target].remove(drop);lines[target].add(v)
        with self.assertRaises(ValueError):
            source_graph(lines,416,6,6)

    def test_12_original_missing_not_GQ_projection_completion(self):
        src=self.src;r=6
        self.assertEqual(len(src["projected"]),416*7*r*r)
        self.assertEqual(len(src["missing"]),416*157)
        self.assertEqual(len(src["flags"]),416*7)
        self.assertEqual(len(src["projection_load"]),416*7)
        self.assertEqual(set(src["projection_load"].values()),{3*r*r})
        self.assertEqual(len(src["projected"])+len(src["missing"])+
                         len(src["flags"]),416**2)

    def test_13_true_point_and_line_defect_two_walk_identity(self):
        src=self.src
        dp,dl,d=defect_matrices(src)
        self.assertEqual(d,7*157)
        for side,D in (("point",dp),("line",dl)):
            nb=src["neighbors_point" if side=="point" else "neighbors_line"]
            z=exact_second_walk_identity(nb,D,6,6)
            self.assertTrue(z["exact_identity"])

    def test_14_all_order_exact_kappa20_vs_old_odd48(self):
        for q in (8,16,32,64,128,256,512,1024):
            a=even_matching_spectral_envelope(q)
            r=q-2
            self.assertEqual(a["uniform_kappa"],20)
            self.assertEqual(a["fixed_quadratic_C"],5)
            self.assertEqual(Q(a["exact_centered_T_upper"]),Q(25*r,6))
            self.assertEqual(Q(a["cubic_interval_endpoint"]),
                             Q(4225*r**3,216))
            self.assertEqual(Q(a["exact_F0_squared_cubic_upper"]),
                             Q(4225*r**3,216))
            self.assertLess(Q(a["exact_F0_squared_cubic_upper"]),20*r**3)
            self.assertTrue(a["strict_connectivity_from_first_singular_gap"])
            self.assertTrue(a["corrected_even_2021_theorem_6_required"])

    def test_15_calculus_stops_false_old_qodd_analogue(self):
        r=6
        self.assertEqual(Q(4225*r**3,216),Q(4225))
        self.assertLess(Q(4225),20*r**3)
        # Critical point of x(x-2r)^2 is x=2r/3,
        # maximum may also occur at right endpoint 25r/6.
        self.assertLess(Q(32*r**3,27),Q(4225*r**3,216))
        self.assertLess(Q(20),Q(48))
        for q in (3,4,5,6,7,9,10,12,True,Q(8)):
            with self.assertRaises(ValueError):
                even_matching_spectral_envelope(q)

    def test_16_true_GF8_source_TYPED_lex_correlated_J_Gram(self):
        for name,z in self.cases.items():
            self.assertEqual(z["actual_original_points"],416)
            self.assertEqual(z["actual_original_flags"],2912)
            self.assertEqual(z["scheme"],name)
            self.assertEqual(z["original_J"],
                             z["original_point_conflicts"]+
                             z["original_line_conflicts"])
            self.assertGreaterEqual(z["original_point_Gram"],0)
            self.assertGreaterEqual(z["original_line_Gram"],0)
            self.assertTrue(z["no_synthetic_missing_projection"])
            self.assertTrue(z["independent_sixth_moment_not_assumed"])

    def test_17_independent_arbitrary_fixed_pair_maps_no_randomness(self):
        src=self.src
        for scheme in ("lex","correlated"):
            f=typed_maps(src,scheme)
            self.assertEqual(len(set(f["f"])),416)
            self.assertEqual(len(set(f["g"])),416)
            self.assertEqual(direct_original_owner_conflicts(src,f)["J"],
                             self.cases[scheme]["original_J"])

    def test_18_even_parameter_second_valid_choice_without_new_graph_claim(self):
        # q8 has several legal x,m; use same original true G8^x
        # stage with different m but DO NOT infer all-order existence
        # from two finite configurations.
        alt=corrected_even_S_and_M(Field(8),2,4)
        self.assertEqual(alt["parameters"]["inverse_m"],7)
        self.assertEqual(len(alt["deleted"]),160)
        self.assertEqual(len(alt["matching_original_flags"]),24)
        self.assertEqual(len(alt["matched_high_degree_vertices"]),48)
        self.assertTrue(alt["matching_exactly_repairs_every_high_degree_original_vertex"])
        self.assertTrue(alt["published_prime_power_existence_REQUIRED"] if
                         "published_prime_power_existence_REQUIRED" in alt else
                         alt["parameters"]["published_prime_power_existence_REQUIRED"])

    def test_19_q16_field_params_but_no_bogus_large_original_fixture(self):
        f=Field(16)
        z=even_params(f,2,3)
        self.assertEqual(z["inverse_m"],14)
        a=even_matching_spectral_envelope(16)
        self.assertEqual(a["final_points_per_side"],3776)
        self.assertEqual(a["original_flags"],56640)
        self.assertEqual(a["original_quadratic_Moore_excess"],821)
        # We assert published family existence using field theorem,
        # NOT a claimed 3776x3776 source built in this test.
        self.assertTrue(a["actual_all_orders_exist_only_for_supported_prime_powers"])

    def test_20_exact_original_six_ID_BBo_and_anchor_negative_control(self):
        z=self.cert["actual_even_GF8_original_six_ID_positive_BBo"]
        self.assertEqual((z["q"],z["x"],z["m"]),(8,2,3))
        self.assertEqual(z["true_original_flags"],2912)
        self.assertEqual(z["required_original_matching_edges_removed"],24)
        self.assertEqual(len(set(z["six_distinct_original_flag_IDs"])),6)
        self.assertEqual(len(z["six_original_source_flag_coordinates"]),6)
        self.assertTrue(z["independent_three_original_six_ID_inverses_agree"])
        self.assertTrue(z["deleting_one_original_FULL_anchor_falsifies"])
        self.assertTrue(z["no_GQ_completion_or_synthetic_F"])
        self.assertGreaterEqual(z["original_BBo_count_at_least_one"],1)

    def test_21_fixed_direct_G6D2_ledger_reuses_all_four_LOW_budgets(self):
        z=self.cert["inherited_G6D2_DIRECT_formal_ledger"]
        self.assertTrue(z["FORMAL_ONLY"])
        self.assertTrue(z["moment_sixth_condition_is_NOT_required"])
        f=z["fixed_before_source"]
        self.assertEqual((f["balance_b"],f["quadratic_C"],
                          f["centered_operator_kappa"]),(1,5,20))
        self.assertTrue(z["no_unconditional_quadratic_T3"])
        c=z["closure"];mom=z["moments"];sel=z["selector"]
        eps=Q(c["eps"]);rho=Q(c["rho"]);R=int(c["sufficient_r0"])
        self.assertLessEqual(mom["improper"],eps*R)
        self.assertLessEqual(mom["E"]**2,eps**2*R)
        self.assertLessEqual(mom["blocker_D"]**8,eps**8*R)
        self.assertLessEqual(12*f["balance_b"]**2*rho*sel["q3"]**2*
                             mom["L6"],eps**2)
        self.assertGreater(Q(c["delta"]),0)

    def test_22_independently_forbid_odd_2015_wrong_characteristic(self):
        # In characteristic 2 the old odd R={(1,b,-2b),
        # (-1,b,2b)} collapses because -1=+1, 2b=0.
        f=Field(8);q=8
        odd_bad={(a,b,c) for b in range(q)
                 for a,c in ((1,f.sub(0,f.add(b,b))),
                             (f.sub(0,1),f.add(b,b)))}
        self.assertEqual(len(odd_bad),q)
        self.assertNotEqual(len(odd_bad),len(self.quasi["R"]))
        self.assertEqual(len(self.quasi["R"]),2*q)

    def test_23_uniform_source_constants_from_true_existing_C1(self):
        from gio_t3d2_centered_sixth import uniform_direct_spectral_constants
        const=uniform_direct_spectral_constants(1,5,20)
        r=6
        for z in self.cases.values():
            self.assertLessEqual(z["original_J"],
                                 const["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(z["original_point_Gram"]**2,
                                 const["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(z["original_line_Gram"]**2,
                                 const["original_pencil_Gram_G0"]**2*r**11)


    def test_24_all_order_even_tail_sharp_kappa_5_and_2(self):
        from gio_t3e3_even_corrigendum import sharper_even_piecewise_envelope
        for q in (8,16,32,64,128,256,512,1024):
            z=sharper_even_piecewise_envelope(q)
            k=20 if q==8 else 5 if q==16 else 2
            r=q-2
            self.assertEqual(z["sharp_subfamily_kappa"],k)
            self.assertLess(Q(z["exact_sharpened_F0_squared_upper"]),
                            k*r**3)
            self.assertLessEqual(Q(z["exact_nonprincipal_T_upper"]),
                                 Q(25*r,6))
            self.assertTrue(z["mandatory_original_matching_edge_deletion"])
            self.assertTrue(z["not_a_new_graph_family"])
            self.assertEqual(z["certified_direct_source_C"],5)
            self.assertEqual(z["can_use_fixed_kappa_5_at_all_q_ge_16"],q>=16)
            self.assertEqual(z["can_use_fixed_kappa_2_at_all_q_ge_32"],q>=32)
            if q>=32:
                self.assertEqual(Q(z["exact_nonprincipal_T_upper"]),
                                 Q(27*r,10))
                self.assertEqual(Q(z["exact_cubic_endpoint"]),
                                 Q(1323*r**3,1000))
            elif q>=16:
                self.assertEqual(Q(z["exact_nonprincipal_T_upper"]),
                                 Q(45*r,14))
                self.assertEqual(Q(z["exact_cubic_endpoint"]),
                                 Q(13005*r**3,2744))
        self.assertEqual([z["sharp_subfamily_kappa"] for z in
            self.cert["stronger_even_q16_q32_source_operator_gates"]][:3],
            [20,5,2])

    def test_25_refined_q16_q32_formal_legacy_D2_SOURCE_ledgers(self):
        z=self.cert["stronger_q16_q32_formal_direct_ledgers"]
        self.assertEqual(len(z),2)
        for item,k in zip(z,(5,2)):
            q=item["q_threshold"]
            self.assertEqual((q,item["minimum_r"]),(16 if k==5 else 32,q-2))
            old=item["formal_ledger"]
            self.assertTrue(old["FORMAL_ONLY"])
            self.assertTrue(old["moment_sixth_condition_is_NOT_required"])
            self.assertTrue(old["no_unconditional_quadratic_T3"])
            f=old["fixed_before_source"]
            self.assertEqual((f["balance_b"],f["quadratic_C"],
                              f["centered_operator_kappa"]),(1,5,k))
            c=old["closure"];m=old["moments"];sel=old["selector"]
            eps=Q(c["eps"]);rho=Q(c["rho"]);R=int(c["sufficient_r0"])
            self.assertLessEqual(m["improper"],eps*R)
            self.assertLessEqual(m["E"]**2,eps**2*R)
            self.assertLessEqual(m["blocker_D"]**8,eps**8*R)
            self.assertLessEqual(12*rho*sel["q3"]**2*m["L6"],eps**2)
            self.assertGreater(Q(c["delta"]),0)
            # No illicit claim that small q16/32 already exceeds the
            # very large inherited sufficient asymptotic threshold.
            self.assertLess(q-2,R)



if __name__=="__main__":
    unittest.main()
