"""HYP-105 AA4-HARRIS: all-h ORIGINAL source priority and LOW ledger acceptance."""
from fractions import Fraction
from math import comb
from itertools import combinations
import unittest

from hyp105_original_harris_product_selector_referee import (
    SCHEMA,ROOT_STATUS,K,R,_ceil_sqrt,_constant_ledger,formal_harris_upgrade,
    _actual_original_source,_actual_proper_paths,_rank_exact_independent,
    _rank_independent_linear_extensions,_path_priority_cert,
    _independent_typed_cut_exhaustive,_original_source_incompatible_path_weight,
    _small_graph_rank_exhaustive,canonical_report
)


class TestOriginalHarrisProductAllHReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.formal=cls.report["all_h_derived_original_LOW_arithmetic_FORMAL"]
        cls.source=cls.report["true_original_W32_complete_W34_sample_physical_sources"]
        cls.bad=cls.report["independent_exact_W32_Harris_bad_pair_B_uniform_bound"]

    def test_root_remains_unpromoted_with_exact_provenance(self):
        d=self.report
        self.assertEqual(d["schema"],SCHEMA)
        self.assertEqual(d["status"],ROOT_STATUS)
        self.assertEqual(d["issue"],230)
        self.assertFalse(d["root_PROVED_A"])
        self.assertFalse(d["new_global_seven_class_root_proof_certified"])
        self.assertFalse(d["external_C6_numeric_graph_constants_assumed"])
        self.assertTrue(d["new_all_h_original_J_free_owner_Harris_product_theorem"])
        self.assertTrue(d["source_adaptive_degree_floor_uniform_independent_of_f_g_correlation"])

    def test_universal_q2_q3_harris_exact_integer_improvement(self):
        d=self.formal[0]
        old=d["historical"];new=d["harris"]
        self.assertEqual(old["q2"],16*comb(130,2))
        self.assertEqual(old["q3"],64*comb(195,3))
        self.assertEqual(old["q2"],134160)
        self.assertEqual(old["q3"],77879360)
        self.assertEqual(new["q2"],16*65**2)
        self.assertEqual(new["q3"],64*65**3)
        self.assertEqual(new["q2"],67600)
        self.assertEqual(new["q3"],17576000)
        self.assertEqual(Fraction(d["q3_improvement"]),
                         Fraction(77879360,17576000))
        self.assertEqual(Fraction(d["adversarial_original_Z_deletion_radius_improvement"]),
            Fraction(77879360,17576000)**2)

    def test_exact_formal_original_exponent_thresholds_decrease_8(self):
        expected=[(751,743),(781,773),(787,779)]
        for p,(a,b) in zip(self.formal,expected):
            self.assertEqual(p["historical"]["h0"],a)
            self.assertEqual(p["harris"]["h0"],b)
            self.assertEqual(p["h0_dyadic_exponent_improvement"],8)
            self.assertLess(int(p["harris"]["s0"]),int(p["historical"]["s0"]))
            self.assertLess(p["harris"]["L4"],p["historical"]["L4"])
            self.assertLess(p["harris"]["E"],p["historical"]["E"])
            self.assertLess(p["harris"]["D"],p["historical"]["D"])

    def test_all_formal_ledger_gates_true_and_heavy_unmodified(self):
        for r in self.formal:
            new=r["harris"];old=r["historical"]
            self.assertEqual(new["T"],old["T"])
            self.assertEqual(new["L6"],old["L6"])
            self.assertEqual(new["R"],old["R"])
            self.assertEqual(new["delta"],old["delta"])
            self.assertEqual(new["low_BBo_sextic_floor"],
                             old["low_BBo_sextic_floor"])
            self.assertEqual(new["GF5_additive_accepted_signed_sextic_floor"],
                             old["GF5_additive_accepted_signed_sextic_floor"])
            self.assertTrue(all(new["conditional_all_h_checks"].values()))
            self.assertTrue(all(old["conditional_all_h_checks"].values()))
            self.assertTrue(r["HEAVY_threshold_T_unchanged"])
            self.assertTrue(r["signed_GF5_proof_gate_unchanged"])
            self.assertFalse(r["real_published_numeric_C0_c0_assumed"])

    def test_improved_deleted_original_Z_rho_is_positive_below_strict_heavy_cap(self):
        for z in self.formal:
            old=z["historical"];new=z["harris"]
            oldrho=Fraction(old["rho"]);rho=Fraction(new["rho"])
            self.assertGreater(rho,oldrho)
            self.assertLess(rho,Fraction(1,2**32))
            self.assertLess(rho,Fraction(3,64))
            self.assertLess(rho,Fraction(1,32))
            self.assertEqual(rho/oldrho,
                Fraction(old["q3"],new["q3"])**2)
            self.assertEqual(12*new["q3"]**2*new["L6"]*rho,
                Fraction(new["tstar"])**2)

    def test_current_historical_original_lowchain_exact_test_only_crosscheck(self):
        # Main referee does not import predecessor; TEST-ONLY independent frozen comparison.
        from hyp105_original_lowchain_partition_referee import formal_low_heavy_glue
        for x in self.formal:
            old=x["historical"]
            f=formal_low_heavy_glue(
                Fraction(old["C0_FORMAL"]),Fraction(old["c0_FORMAL"]))
            for key in ("q2","q3","T","L6","L4","B0","E","D","h0"):
                self.assertEqual(old[key],f[key])
            self.assertEqual(old["s0"],str(f["s0"]))
            self.assertEqual(old["rho"],f["rho_star"])
            self.assertEqual(old["low_BBo_sextic_floor"],
                             f["LOW_original_BBo_sextic_coefficient"])

    def test_invalid_external_graph_constants_and_noninteger_roots_fail_closed(self):
        for x,y in ((1,1),(Fraction(1,2),Fraction(1)),
                    (Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2))):
            with self.assertRaises(ValueError):formal_harris_upgrade(x,y)
        with self.assertRaises(ValueError):_ceil_sqrt(-1)
        with self.assertRaises(ValueError):
            _constant_ledger(Fraction(1),Fraction(1),"pretend_PROVED_A")

    def test_exact_independent_typed_factor_cuts_2_and_3(self):
        a=_independent_typed_cut_exhaustive(2)
        b=_independent_typed_cut_exhaustive(3)
        self.assertEqual(a["literal_cut_assignments"],64)
        self.assertEqual(b["literal_cut_assignments"],256)
        self.assertEqual(a["favorable_assignments"],4)
        self.assertEqual(b["favorable_assignments"],4)
        self.assertEqual(Fraction(a["two_independent_typed_cut_probability"]),Fraction(1,16))
        self.assertEqual(Fraction(b["two_independent_typed_cut_probability"]),Fraction(1,64))

    def test_independent_all_abstract_five_owner_J_graphs_r2_r3(self):
        r=self.report["independent_abstract_J_small_graph_total_priority_falsifier"]
        self.assertEqual(r["n_source_vertices"],5)
        self.assertEqual(r["exhaustively_enumerated_simple_J_graphs"],1024)
        self.assertGreater(r["J_independent_owner_r2_r3_sets_tested"],0)
        self.assertGreater(r["strictly_positive_source_priority_association_cases"],0)
        self.assertEqual(r["J_independent_owner_r2_r3_sets_tested"],
            r["global_priority_permutation_exhaustive_comparisons"])

    def test_true_original_W32_all_source_cases_cardinality_and_both_diagonals(self):
        for r in self.source[:3]:
            self.assertEqual(r["s"],2)
            self.assertEqual(r["original_flags"],45)
            self.assertTrue(r["original_K64_admissible"])
            self.assertEqual(r["physical_REAL_edges"],
                2*r["retained_named_original_CORE_flags"])
            self.assertTrue(all(x["complete_original_physical_path_census"]
                for x in r["r2_r3"]))
            self.assertEqual([x["r"] for x in r["r2_r3"]],[2,3])
        self.assertEqual(self.source[0]["r2_r3"][1]["genuine_physical_coordinate_proper_rpaths"],1346)
        self.assertEqual(self.source[1]["r2_r3"][1]["genuine_physical_coordinate_proper_rpaths"],1154)
        self.assertEqual(self.source[2]["r2_r3"][1]["genuine_physical_coordinate_proper_rpaths"],838)
        self.assertEqual(self.source[2]["adversarial_deleted_original_Z_flags"],3)

    def test_true_original_W34_finite_paired_source_labeled_and_sample_scope(self):
        for r in self.source[3:]:
            self.assertEqual(r["s"],4)
            self.assertEqual(r["original_flags"],425)
            self.assertLessEqual(r["original_source_max_J_degree"],64)
            self.assertEqual(r["physical_REAL_edges"],
                2*r["retained_named_original_CORE_flags"])
            self.assertEqual([x["genuine_physical_coordinate_proper_rpaths"]
                for x in r["r2_r3"]],[160,160])
            self.assertTrue(all(not x["complete_original_physical_path_census"]
                for x in r["r2_r3"]))

    def test_each_original_genuine_path_certifies_local_Harris_and_first_r_floors(self):
        for row in self.source:
            for v in row["r2_r3"]:
                self.assertGreater(v["genuine_physical_coordinate_proper_rpaths"],0)
                self.assertGreater(v["exact_source_priority_poset_DP_sampled_checks"],0)
                z=v["least_factor_witness_true_original_physical_path"]
                q=z["source_certificate"]
                self.assertGreaterEqual(Fraction(q["exact_priority_joint"]),
                    Fraction(q["Harris_local_product_floor"]))
                self.assertGreaterEqual(Fraction(q["exact_priority_joint"]),
                    Fraction(q["historical_local_first_r_floor"]))
                self.assertEqual(
                    Fraction(q["Harris_adaptive_max_both_floors"]),
                    max(Fraction(q["Harris_local_product_floor"]),
                        Fraction(q["historical_local_first_r_floor"])))
                self.assertGreaterEqual(Fraction(q["exact_path_survival"]),
                    Fraction(q["new_uniform_K64_survival_floor"]))
                self.assertEqual(len(q["original_owners"]),v["r"])
                self.assertEqual(len(z["physical_vertices"]),v["r"]+1)

    def test_abstract_owners_in_J_conflict_are_not_Harris_association_scope(self):
        J=[{1},{0},set()]
        self.assertEqual(_rank_exact_independent((0,1),J),0)
        self.assertGreater(Fraction(1,(1+len(J[0]))*(1+len(J[1]))),0)
        with self.assertRaises(AssertionError):
            _path_priority_cert((0,1),J)

    def test_one_original_owner_priority_minimum_exact_degree_identity(self):
        J=[{2,3},{3},{0},{0,1}]
        self.assertEqual(_rank_exact_independent((0,),J),Fraction(1,3))
        self.assertEqual(_rank_exact_independent((1,),J),Fraction(1,2))
        self.assertEqual(_rank_exact_independent((2,),J),Fraction(1,2))

    def test_local_product_can_be_weaker_than_local_first_r_event(self):
        # Three J-independent owners all compete with SAME outside owner.
        # Both are correct lower bounds; do not falsely assume pointwise dominance.
        J=[{3},{3},{3},{0,1,2}]
        d=_path_priority_cert((0,1,2),J)
        self.assertEqual(Fraction(d["exact_priority_joint"]),Fraction(1,4))
        self.assertEqual(Fraction(d["Harris_local_product_floor"]),Fraction(1,8))
        self.assertEqual(Fraction(d["historical_local_first_r_floor"]),Fraction(1,4))

    def test_three_owner_shared_outside_neighbors_give_strict_Harris_gain(self):
        # J-free owners 0,1,2 compete with the SAME TWO neighbors 3,4.
        # Exactly three owners must occupy the first three among 5 source
        # ranks; the positive association has a strict rational gap.
        J=[{3,4},{3,4},{3,4},{0,1,2},{0,1,2}]
        source=_rank_exact_independent((0,1,2),J)
        independent=_rank_independent_linear_extensions((0,1,2),J)
        own_product=Fraction(1,3)**3
        self.assertEqual(source,Fraction(1,10))
        self.assertEqual(source,independent)
        self.assertGreater(source,own_product)
        self.assertEqual(
            Fraction(_path_priority_cert((0,1,2),J)["Harris_local_product_floor"]),
            own_product)

    def test_true_original_source_direct_priority_vs_independent_DP(self):
        c=_actual_original_source(2,"lex","full")
        proper=_actual_proper_paths(c,3,40)
        for path,owners in proper[:8]:
            cert=_path_priority_cert(owners,c["J"])
            self.assertEqual(Fraction(cert["exact_priority_joint"]),
                _rank_independent_linear_extensions(owners,c["J"],limit=18))

    def test_source_bad_pair_B_new_global_Harris_nonzero_bound(self):
        epsilon=Fraction(1,256*(K+1)**6)
        for r in self.bad:
            self.assertEqual(Fraction(r["all_h_universal_compatible_fraction_epsilon"]),epsilon)
            G=Fraction(r["actual_exact_compatible_G"])
            B=Fraction(r["actual_exact_incompatible_B"])
            M=Fraction(r["actual_exact_mean_Frobenius2_G_plus_B"])
            self.assertGreater(G,0)
            self.assertGreater(B,0)
            self.assertEqual(G+B,M)
            self.assertGreaterEqual(G,
                Fraction(r["constructive_endpoint_conditioned_FKG_G_lower"]))
            self.assertGreaterEqual(G,epsilon*M)
            self.assertLessEqual(B,(1-epsilon)*M)
            self.assertTrue(r["all_h_B_less_equal_1_minus_epsilon_times_M"])
            self.assertEqual(r["ordered_same_end_real_path_pairs"],
                sum(r["four_original_incompatibility_classes"].values()))

    def test_original_W32_exact_weighted_bad_pair_counts_source_only(self):
        expected=[
            {"compatible":2386,"original_J_conflict":1348,
             "original_first_typed_opposite_depth_collision":464,
             "original_second_typed_opposite_depth_collision":172},
            {"compatible":1654,"original_J_conflict":744,
             "original_first_typed_opposite_depth_collision":444,
             "original_second_typed_opposite_depth_collision":100},
            {"compatible":1050,"original_J_conflict":440,
             "original_first_typed_opposite_depth_collision":208,
             "original_second_typed_opposite_depth_collision":68},
        ]
        for row,e in zip(self.bad,expected):
            self.assertEqual(row["four_original_incompatibility_classes"],e)
        self.assertEqual([r["ordered_same_end_real_path_pairs"] for r in self.bad],
                         [4370,2942,1766])
        self.assertEqual(Fraction(self.bad[0]["actual_exact_mean_Frobenius2_G_plus_B"]),
            Fraction(170009657654496199,164130319761408000000))

    def test_new_source_floors_do_not_confuse_first_r_with_exact_joint_probability(self):
        source=_actual_original_source(2,"reverse","full")
        path,owners=_actual_proper_paths(source,3,1)[0]
        c=_path_priority_cert(owners,source["J"])
        self.assertGreaterEqual(Fraction(c["exact_priority_joint"]),
            Fraction(c["Harris_adaptive_max_both_floors"]))
        self.assertEqual(Fraction(c["exact_path_survival"]),
            Fraction(c["exact_priority_joint"])*Fraction(1,64))
        self.assertEqual(Fraction(c["new_uniform_K64_survival_floor"]),
            Fraction(1,64*(K+1)**3))


if __name__=="__main__":unittest.main()
