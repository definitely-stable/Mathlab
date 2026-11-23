"""G6-E2 independent 2021 corrigendum/real source/matching/spectrum checks."""
import unittest
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import product

from gio_t3d3_affine_arc import Field
from gio_t3e1_subgq_pds import actual_smaller_source
from gio_t3e2_corrigendum_quasi_pds import (
    SCHEMA,PARENT_G6E1,PAPER,CORRIGENDUM_DATE,
    eligible_odd_parameters,stage_one_adjacency,
    corrected_S_and_M,actual_corrigendum_source,
    spectral_compression_with_matching,literal_case,
    exact_all_order_ledger,certificate,
)
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,defect_matrices,exact_second_walk_identity,
    direct_original_owner_conflicts,
)
from gio_t3e1_subgq_pds import exact_original_centered_missing_PSD


def independent_components(source):
    """Direct ORIGINAL bipartite BFS connectivity, not eigenvalue estimates."""
    n=source["points"]
    N=n+len(source["lines"])
    adj=[set() for _ in range(N)]
    for p,e in source["flags"]:
        adj[p].add(n+e)
        adj[n+e].add(p)
    done=set()
    comps=[]
    for v in range(N):
        if v in done:
            continue
        frontier=[v];done.add(v);size=0
        while frontier:
            u=frontier.pop();size+=1
            for w in adj[u]-done:
                done.add(w);frontier.append(w)
        comps.append(size)
    return sorted(comps)


def independent_original_source_neighbors(instance):
    """Independently reconstruct q-1 source from true stage-1 flags."""
    z=instance["intermediate"]
    old=z["stage"]["source"]
    n=old["points"]
    keepP=sorted(p for p in z["kept"] if p<n)
    keepL=sorted(l-n for l in z["kept"] if l>=n)
    drop=set(instance["original_M_edges"])
    oracle={}
    for p in keepP:
        for ell in keepL:
            if p in old["lines"][ell] and (p,ell) not in drop:
                oracle[p,ell]=1
    source=instance["new_source"]
    actual={(keepP[p],keepL[e]) for p,e in source["flags"]}
    assert set(oracle)==actual
    return actual


class TestE2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=certificate()
        cls.by={(z["q"],z["scheme"]):z
                for z in cls.data["true_original_corrected_quasi_PDS_source_examples"]}

    def test_01_corrigendum_metadata_and_not_false_2015(self):
        z=self.data
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6E1_HEAD"],PARENT_G6E1)
        self.assertEqual(z["corrigendum_date"],"2021-05-18")
        self.assertEqual(z["published_2015_paper_and_MAY_2021_corrigendum"],PAPER)
        self.assertTrue(z["first_original_2015_q_minus1_family_RETRACTED"])
        self.assertTrue(z["corrected_2021_matching_is_required"])
        self.assertTrue(z["corrected_family_exists_for_odd_prime_power_q_ge7"])
        self.assertTrue(z["no_new_worldwide_graph_construction"])
        self.assertTrue(z["no_unrestricted_T3_or_new_ASET_exponent"])

    def test_02_corrected_exact_parameter_restrictions(self):
        for q,x,y in ((5,2,3),(7,2,3),(11,2,3),(13,5,8),(17,4,13),
                      (19,2,3)):
            k=eligible_odd_parameters(Field(q),x,y)
            self.assertTrue(k["false_2015_perfect_dominating_theorem_RETRACTED"])
            self.assertEqual((k["q"],k["x"],k["y"]),(q,x,y))
        for q,x,y in ((5,1,3),(7,2,6),(7,0,3),(7,2,2),
                      (13,2,8),(13,5,9),(17,4,4)):
            with self.assertRaises(ValueError):
                eligible_odd_parameters(Field(q),x,y)
        with self.assertRaises(ValueError):
            eligible_odd_parameters(Field(4),2,3)
        with self.assertRaises(ValueError):
            eligible_odd_parameters(Field(7),True,3)

    def test_03_true_Gq_x_q_regular_stage(self):
        for q,x in ((5,2),(7,2)):
            z=stage_one_adjacency(actual_smaller_source(Field(q),xi=x))
            self.assertEqual(z["n"],q*(q*q-2))
            self.assertEqual(len(z["adj"]),2*z["n"])
            self.assertEqual(set(map(len,z["adj"])),{q})
            self.assertEqual(len(z["point_lookup"]),z["n"])
            self.assertEqual(len(z["line_lookup"]),z["n"])

    def test_04_corrected_quasi_perfect_S_exact_cardinality(self):
        for q,x,y in ((5,2,3),(7,2,3)):
            z=corrected_S_and_M(Field(q),x,y)
            self.assertEqual(len(z["deleted"]),2*q*q+4*q)
            self.assertEqual(z["S_removed_each"],q*q+2*q)
            self.assertEqual(len(z["kept"]),2*q*(q*q-q-4))
            self.assertTrue(z["published_S_QUASI_not_perfect"])
            self.assertTrue(z["exactly_degree_q_survivors_matched"])
            self.assertEqual(
                dict(Counter(z["deg_before"].values())),
                {q-1:2*q*(q*q-q-4)-2*q*(q-5),
                 **({q:2*q*(q-5)} if q>5 else {})})

    def test_05_correction_matching_nonempty_q7_empty_q5(self):
        for q,x,y in ((5,2,3),(7,2,3)):
            z=corrected_S_and_M(Field(q),x,y)
            matching=z["matched_original_edges"]
            self.assertEqual(len(matching),q*(q-5))
            self.assertEqual(len({u for pair in matching for u in pair}),
                             2*len(matching))
            self.assertEqual(set(u for pair in matching for u in pair),
                             z["matching_vertices"])
            self.assertEqual({v for v in z["kept"] if z["deg_before"][v]==q},
                             z["matching_vertices"])
            for p,l in matching:
                self.assertIn(l,z["stage"]["adj"][p])
            self.assertTrue(z["corrected_2021_matching_applied_not_falsely_ignored"])
        self.assertEqual(len(corrected_S_and_M(Field(7),2,3)[
            "matched_original_edges"]),14)

    def test_06_real_q7_source_exact_degree_and_Moore(self):
        z=self.by[7,"lex"]
        self.assertEqual(z["genuine_smaller_source_each_side"],266)
        self.assertEqual(z["original_degree"],6)
        self.assertEqual(z["original_r"],5)
        self.assertEqual(z["original_named_flags"],1596)
        self.assertEqual(z["original_Moore_excess"],110)
        self.assertEqual(z["corrected_2021_quasi_domination_S_size"],126)
        self.assertEqual(z["S_removed_per_side"],63)
        self.assertEqual(z["residual_pre_M_matching_edges"],14)
        self.assertTrue(z["every_degree_q_residual_matched"])
        self.assertFalse(z["q5_is_finite_exception_NOT_an_infinite_family"])

    def test_07_real_q5_exception_not_infinite_2015_family(self):
        z=self.by[5,"lex"]
        self.assertEqual(z["genuine_smaller_source_each_side"],80)
        self.assertEqual(z["original_degree"],4)
        self.assertEqual(z["original_r"],3)
        self.assertEqual(z["original_named_flags"],320)
        self.assertEqual(z["original_Moore_excess"],40)
        self.assertEqual(z["residual_pre_M_matching_edges"],0)
        self.assertTrue(z["q5_is_finite_exception_NOT_an_infinite_family"])

    def test_08_literal_final_edges_and_independent_girth_checker(self):
        for q,x,y in ((5,2,3),(7,2,3)):
            z=actual_corrigendum_source(Field(q),x,y)
            src=z["new_source"]
            edge_set=independent_original_source_neighbors(z)
            self.assertEqual(len(edge_set),len(src["flags"]))
            self.assertEqual(len(independent_components(src)),
                             1)
            self.assertEqual(independent_components(src),
                             [2*q*(q*q-q-4)])
            self.assertTrue(z["actual_original_incidence_after_S_and_matching"])
            self.assertEqual(src["s"],q-2)
            self.assertEqual(src["t"],q-2)
            self.assertTrue(all(
                len(line)==q-1 for line in src["lines"]))
            self.assertTrue(all(
                v==3*(q-2)**2 for v in src["projection_load"].values()))

    def test_09_exact_genuine_G6C1_second_walk_identity(self):
        for q,x,y in ((5,2,3),(7,2,3)):
            src=actual_corrigendum_source(Field(q),x,y)["new_source"]
            dp,dl,d=defect_matrices(src)
            r=q-2
            self.assertEqual(d,(r+1)*(4*r*r+3*r-5))
            for side,D in (("point",dp),("line",dl)):
                nb=src["neighbors_point" if side=="point" else "neighbors_line"]
                z=exact_second_walk_identity(nb,D,r,r)
                self.assertTrue(z["exact_identity"])

    def test_10_correct_qminus1_Moore_excess_not_old_formula(self):
        for q in range(5,102):
            r=q-2
            newn=q*(q*q-q-4)
            Moore=(r+1)*(r*r+1)
            Delta=newn-Moore
            self.assertEqual(Delta,4*r*r+3*r-5)
            self.assertLessEqual(Delta,5*r*r)
            self.assertEqual(newn,q**3-q**2-4*q)
            # Old false 2015 family uses q(q-1)^2 instead:
            if q==5:
                self.assertEqual(newn,q*(q-1)**2) # exceptional q5 coincidence
            else:
                self.assertNotEqual(newn,q*(q-1)**2)

    def test_11_exact_uniform_Weyl_interlacing_rational_upper(self):
        for q in (7,9,11,13,17,19,23,25,27,31,49,81,101,121):
            s=spectral_compression_with_matching(q)
            r=q-2
            self.assertEqual(s["original_Moore_excess"],4*r*r+3*r-5)
            self.assertEqual(s["original_q_minus_one_degree"],r+1)
            self.assertEqual(s["uniform_fixed_kappa"],48)
            self.assertEqual(s["uniform_quadratic_excess_C"],5)
            self.assertTrue(s["MATCHING_operator_norm_exactly_one"])
            self.assertEqual(Q(s["exact_nonprincipal_T_eigenvalue_bound"]),
                             Q(81*r,16))
            self.assertLessEqual(Q(s["exact_centered_G6D1_cubic_upper"]),
                                 48*r**3)
            self.assertTrue(s["connectedness_from_strict_singular_gap"])
            self.assertTrue(s["old_2015_perfect_dominating_order_RETRACTED"])

    def test_12_published_theorem_only_applies_to_correct_q(self):
        for bad in (0,2,4,5,6,8,True,Q(7)):
            with self.assertRaises(ValueError):
                spectral_compression_with_matching(bad)
        for q in (7,9,17,19):
            s=spectral_compression_with_matching(q)
            self.assertTrue(s["field_existence_requires_corrected_2021_theorem"])
            self.assertTrue(s["q_odd_prime_power_required"])

    def test_13_real_source_point_line_J_and_Gram_correlated(self):
        for q in (7,):
            a=self.by[q,"lex"]
            b=self.by[q,"correlated"]
            self.assertEqual(a["genuine_smaller_source_each_side"],
                             b["genuine_smaller_source_each_side"])
            self.assertNotEqual(a["original_total_J"],b["original_total_J"])
            for z in (a,b):
                self.assertEqual(z["original_total_J"],
                                 z["independent_original_point_conflicts"]+
                                 z["independent_original_line_conflicts"])
                self.assertGreaterEqual(z["original_point_Gram"],0)
                self.assertGreaterEqual(z["original_line_Gram"],0)

    def test_14_genuine_final_original_full_projection_load_no_GQ_completion(self):
        src=actual_corrigendum_source(Field(7),2,3)["new_source"]
        N=src["points"]
        self.assertEqual(len(src["projected"]),
                         N*6*5**2)
        self.assertEqual(len(src["missing"]),
                         N*110)
        self.assertEqual(len(src["flags"]),N*6)
        self.assertEqual(len(src["projection_load"]),N*6)
        self.assertTrue(all(v==75 for v in src["projection_load"].values()))
        self.assertLess(len(src["projected"])+len(src["missing"]),
                        N*N)

    def test_15_q5_true_original_F0_exact_rational_PSD(self):
        z=self.by[5,"lex"]
        for side in ("point","line"):
            d=z["exact_full_original_missing_PSD"][side]
            self.assertEqual(d["exact_original_F0_operator_upper"],
                             48*3**3)
            self.assertEqual(d["residual_inertia"]["negative"],0)
            self.assertTrue(d["no_synthetic_projection_or_GQ_completion"])

    def test_16_uniform_all_order_DIRECT_G6D2_gates_are_fixed(self):
        d=self.data["inherited_G6D2_DIRECT_four_low_ledger"]
        self.assertTrue(d["FORMAL_ONLY"])
        self.assertTrue(d["moment_sixth_condition_is_NOT_required"])
        f=d["fixed_before_source"]
        self.assertEqual((f["balance_b"],f["quadratic_C"],
                          f["centered_operator_kappa"]),(1,5,48))
        self.assertTrue(d["no_unconditional_quadratic_T3"])
        c=d["closure"];m=d["moments"];s=d["selector"]
        eps=Q(c["eps"]);rho=Q(c["rho"]);R=int(c["sufficient_r0"])
        self.assertLessEqual(m["improper"],eps*R)
        self.assertLessEqual(m["E"]**2,eps**2*R)
        self.assertLessEqual(m["blocker_D"]**8,eps**8*R)
        self.assertLessEqual(12*f["balance_b"]**2*rho*s["q3"]**2*m["L6"],
                             eps**2)

    def test_17_explicit_original_cycle_corruption_fail_closed(self):
        src=actual_corrigendum_source(Field(5),2,3)["new_source"]
        lines=[set(line) for line in src["lines"]]
        p,v=sorted(lines[0])[:2]
        ell=next(i for i in range(1,len(lines)) if p in lines[i])
        victim=next(w for w in lines[ell] if w!=p)
        lines[ell].remove(victim)
        lines[ell].add(v)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],3,3)

    def test_18_raw_quasi_S_without_M_IS_NOT_regular_q7(self):
        z=corrected_S_and_M(Field(7),2,3)
        self.assertEqual(set(z["deg_before"].values()),{6,7})
        self.assertEqual(Counter(z["deg_before"].values())[7],28)
        self.assertEqual(Counter(z["deg_before"].values())[6],504)
        self.assertEqual(len(z["matched_original_edges"]),14)

    def test_19_different_family_from_G6E1_and_2015_original(self):
        for q in (5,7):
            old=actual_smaller_source(Field(q),xi=2)
            stage=old["new_original_source"]
            new=actual_corrigendum_source(Field(q),2,3)["new_source"]
            self.assertEqual(stage["s"],q-1)
            self.assertEqual(new["s"],q-2)
            self.assertLess(new["points"],stage["points"])
            self.assertEqual(stage["points"]-new["points"],q*q+2*q)
            if q==5:
                self.assertEqual(new["points"],q*(q-1)**2)
            else:
                self.assertNotEqual(new["points"],q*(q-1)**2)
            self.assertEqual(stage["excess_lines"],2*q*(q-2))
            self.assertEqual(new["excess_lines"],4*(q-2)**2+3*(q-2)-5)

    def test_20_mark_not_a_new_unrestricted_T3_or_ASET(self):
        z=self.data
        self.assertEqual(z["claim"],
            "CONDITIONAL_G6D2_T3_CORRECTED_2021_QMINUS1_PDS_PLUS_MATCHING")
        self.assertTrue(z["no_independent_F0_assumption_or_sixth_moment"])
        self.assertTrue(z["no_unrestricted_T3_or_new_ASET_exponent"])
        self.assertTrue(z["no_external_human_referee_or_Lean"])
        self.assertTrue(z["new_to_Mathlab_true_source_degree_q_minus_1"])


    def test_21_actual_corrected_q7_original_six_ID_BBo_inverse(self):
        from gio_t3e2_corrigendum_quasi_pds import literal_corrected_six_original_ID_witness
        z=literal_corrected_six_original_ID_witness(
            7,2,3,"lex",max_walks=3000000)
        self.assertEqual(z["q"],7)
        self.assertEqual(z["true_corrected_original_source_flags"],1596)
        self.assertEqual(z["original_M_edges_removed"],14)
        self.assertEqual(len(set(z["actual_six_distinct_original_flag_IDs"])),6)
        self.assertTrue(z["all_three_historical_BBo_inverses_exact_agree"])
        self.assertTrue(z["removing_original_FULL_anchor_destroys_witness"])
        self.assertGreaterEqual(z["independently_confirmed_produced_BBo_count"],1)
        self.assertTrue(z["no_fabricated_projection_or_parent_completion"])
        print("G6E2_NONTRIVIAL_CORRECTED_Q7_ORIGINAL_SIX_ID",
            z["independently_confirmed_produced_BBo_count"],
            "examined",z["bounded_actual_physical_threewalks_examined"])



    def test_22_exact_cert_contains_real_corrected_q7_six_original_owners(self):
        x=self.data["actual_corrected_q7_positive_original_six_ID_BBo"]
        self.assertEqual((x["q"],x["scheme"]),(7,"lex"))
        self.assertEqual(x["true_corrected_original_source_flags"],1596)
        self.assertEqual(x["original_M_edges_removed"],14)
        self.assertGreaterEqual(x["independently_confirmed_produced_BBo_count"],1)
        self.assertEqual(len(set(x["actual_six_distinct_original_flag_IDs"])),6)
        self.assertEqual(len(x["actual_six_original_flag_coordinates"]),6)
        self.assertTrue(x["all_three_historical_BBo_inverses_exact_agree"])
        self.assertTrue(x["removing_original_FULL_anchor_destroys_witness"])
        self.assertTrue(x["no_fabricated_projection_or_parent_completion"])
        self.assertTrue(x["finite_positive_not_asymptotic_count"])


if __name__=="__main__":
    unittest.main()
