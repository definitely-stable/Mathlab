"""AA4-CLIQUE independent all-h source incompatibility/Motzkin falsification tests."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_original_badpair_clique_motzkin_referee import (
    SCHEMA,ROOT_STATUS,K,Q,Q_OLD_EPS_DENOM,_actual_source,
    _proper_true_original_p3,_source_joint_priority,_original_path_weights,
    _pair_reason,_x_conflict,_clique_number_neighbors,
    _motzkin_weighted_check,_original_endpoint_weight_audit,
    _abstract_typed_arc_graph,_all_abstract_weighted_motzkin_graphs,
    canonical_report
)


class TestAllHOriginalBadPairMotzkin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.rows=cls.report["true_original_W32_full_W34_partial"]

    def test_issue_root_not_proved_and_correct_prerequisites(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertEqual(r["issue"],230)
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["formal_global_root_proof_not_promoted"] is False)
        self.assertFalse(r["numerical_published_graph_supersaturation_constants_not_claimed"] is False)
        self.assertTrue(r["new_all_h_original_selector_implies_incompatibility_clique_bound"])
        self.assertTrue(r["new_all_h_original_B_M_motzkin_bound"])
        self.assertFalse(r["target_original_B_over_M_less_than_3_over_4_proved"])
        self.assertFalse(r["new_fourfold_full_LOW_sixth_moment_claimed"])

    def test_exact_new_uniform_graph_clique_and_epsilon(self):
        r=self.report
        self.assertEqual(Q,16*65**3)
        self.assertEqual(Q,4394000)
        self.assertEqual(Q_OLD_EPS_DENOM,256*65**6)
        self.assertEqual(r["all_h_original_endpoint_conditioned_clique_Q"],Q)
        self.assertEqual(Fraction(r["all_h_improved_epsilon"]),Fraction(1,Q))
        self.assertEqual(Fraction(r["previous_epsilon"]),Fraction(1,Q_OLD_EPS_DENOM))
        self.assertEqual(r["improvement_factor"],4394000)
        self.assertGreater(Fraction(1,Q),Fraction(1,Q_OLD_EPS_DENOM))

    def test_true_original_finite_three_W32_complete(self):
        self.assertEqual(len(self.rows),6)
        for row,num,edges,pairs in zip(self.rows[:3],
            (1346,1154,838),(90,90,84),(4370,2942,1766)):
            self.assertEqual(row["s"],2)
            self.assertTrue(row["full_actual_original_proper_P3_census"])
            self.assertEqual(row["actual_original_source_flags"],45)
            self.assertEqual(row["proper_directed_P3_scanned"],num)
            self.assertEqual(row["actual_original_physical_edges"],edges)
            self.assertEqual(row["ordered_same_end_real_path_pairs"],pairs)
            self.assertLessEqual(row["actual_original_max_J_degree"],64)
        self.assertEqual(self.rows[2]["deleted_named_original_Z_flags"],3)

    def test_actual_true_original_W34_partial_explicitly_not_full(self):
        for r in self.rows[3:]:
            self.assertEqual(r["s"],4)
            self.assertFalse(r["full_actual_original_proper_P3_census"])
            self.assertEqual(r["actual_original_source_flags"],425)
            self.assertEqual(r["proper_directed_P3_scanned"],2000)
            self.assertEqual(r["actual_original_physical_edges"],2*r["retained_original_CORE_flags"])
            self.assertLessEqual(r["actual_original_max_J_degree"],64)
            self.assertGreater(r["ordered_same_end_real_path_pairs"],0)

    def test_actual_original_full_W32_lex_incompatibility_classes(self):
        self.assertEqual(self.rows[0]["all_incompatibility_reasons"],{
            "compatible":2386,
            "true_original_J_conflict":1348,
            "first_typed_inner_opposite_depth":464,
            "second_typed_inner_opposite_depth":172})

    def test_actual_original_full_W32_reverse_incompatibility_classes(self):
        self.assertEqual(self.rows[1]["all_incompatibility_reasons"],{
            "compatible":1654,
            "true_original_J_conflict":744,
            "first_typed_inner_opposite_depth":444,
            "second_typed_inner_opposite_depth":100})

    def test_actual_original_W32_shift_named_original_Z_classes(self):
        self.assertEqual(self.rows[2]["all_incompatibility_reasons"],{
            "compatible":1050,
            "true_original_J_conflict":440,
            "first_typed_inner_opposite_depth":208,
            "second_typed_inner_opposite_depth":68})

    def test_all_actual_source_weighted_M_B_G_conservation(self):
        for row in self.rows:
            M=Fraction(row["exact_weighted_M"])
            B=Fraction(row["exact_weighted_B"])
            G=Fraction(row["exact_weighted_G"])
            self.assertGreater(G,0)
            self.assertGreater(M,0)
            self.assertGreaterEqual(B,0)
            self.assertEqual(M,B+G)
            self.assertEqual(B/M,Fraction(row["actual_incompatible_ratio_B_over_M"]))
            self.assertEqual(G/M,Fraction(row["actual_compatible_ratio_G_over_M"]))
            self.assertEqual(sum(row["all_incompatibility_reasons"].values()),
                row["ordered_same_end_real_path_pairs"])

    def test_all_original_weighted_B_under_stronger_new_uniform_motzkin(self):
        for r in self.rows:
            M=Fraction(r["exact_weighted_M"])
            B=Fraction(r["exact_weighted_B"])
            G=Fraction(r["exact_weighted_G"])
            self.assertLessEqual(B,(1-Fraction(1,Q))*M)
            self.assertGreaterEqual(G,M/Q)
            self.assertGreaterEqual(G,Fraction(r["instance_specific_Motzkin_G_lower"]))
            self.assertEqual(Fraction(r["theorem_uniform_Motzkin_G_over_M_lower"]),Fraction(1,Q))
            self.assertEqual(r["theorem_global_clique_bound_Q"],Q)

    def test_typed_first_and_second_2thirds_weighted_caps_real_original(self):
        for r in self.rows:
            M=Fraction(r["exact_weighted_M"])
            BX=Fraction(r["exact_first_typed_only_weighted_Bx"])
            BY=Fraction(r["exact_second_typed_only_weighted_By"])
            self.assertLessEqual(BX,Fraction(2,3)*M)
            self.assertLessEqual(BY,Fraction(2,3)*M)
            self.assertTrue(r["first_factor_Bx_at_most_2thirds_M"])
            self.assertTrue(r["second_factor_By_at_most_2thirds_M"])
            self.assertLessEqual(r["max_exact_first_typed_clique"],3)
            self.assertLessEqual(r["max_exact_second_typed_clique"],3)

    def test_true_original_J_only_clique_and_weighted_Motzkin_cap(self):
        for r in self.rows:
            M=Fraction(r["exact_weighted_M"])
            BJ=Fraction(r["exact_original_J_only_weighted_Bj"])
            self.assertGreaterEqual(BJ,0)
            self.assertLessEqual(BJ,(1-Fraction(1,65**3))*M)
            self.assertLessEqual(r["max_exact_original_J_only_clique"],65**3)
            self.assertTrue(r["source_J_only_Bj_at_most_1_minus_1_over_65cubed_M"])

    def test_actual_source_small_bin_clique_histogram_conserves_endpoint_bins(self):
        for r in self.rows:
            hist={int(k):v for k,v in r["original_endpoint_clique_histogram"].items()}
            self.assertEqual(sum(hist.values()),r["physical_ordered_endpoint_bins"])
            self.assertGreaterEqual(min(hist),1)
            self.assertEqual(max(hist),r["max_exact_true_original_incompatibility_clique"])
            self.assertLessEqual(max(hist),r["max_proper_paths_in_one_endpoint_bin"])
            self.assertLessEqual(max(hist),Q)

    def test_independent_exact_all_1024_graphs_243_weights_Motzkin(self):
        r=self.report["independent_exhaustive_Motzkin_weighted_graph_falsifier"]
        self.assertEqual(r["all_labeled_five_vertex_simple_graphs"],1024)
        self.assertEqual(r["strict_integer_positive_weight_distributions_per_graph"],243)
        self.assertEqual(r["exact_graph_weight_inequalities_tested"],248832)
        self.assertGreater(r["equality_cases"],0)
        self.assertGreater(r["strict_inequalities"],0)
        self.assertEqual(r["largest_tested_graph_clique"],5)

    def test_abstract_internal_typed_arcs_K4_free_with_sharp_triangle(self):
        r=self.report["independent_typed_arc_K4_free_falsifier"]
        self.assertEqual(r["physical_internal_symbol_alphabet"],5)
        self.assertEqual(r["all_distinct_ordered_internal_arcs"],20)
        self.assertEqual(r["complete_true_abstract_typed_conflict_graph_clique_number"],3)
        self.assertEqual(Fraction(r["universal_single_typed_Bx_B_y_over_M_upper"]),Fraction(2,3))
        self.assertEqual(len(r["genuine_abstract_three_arc_conflict_witness"]),3)

    def test_exact_rational_motzkin_triangle_achieves_sharp_two_thirds(self):
        adj=({1,2},{0,2},{0,1})
        omega,bad,M=_motzkin_weighted_check(adj,
                       (Fraction(1),Fraction(1),Fraction(1)))
        self.assertEqual(omega,3)
        self.assertEqual(bad,Fraction(6))
        self.assertEqual(M,Fraction(9))
        self.assertEqual(bad/M,Fraction(2,3))

    def test_exact_graph_conflict_single_clique_vs_no_edges(self):
        for n in (1,2,3,4,5):
            full=[set(range(n))-{i} for i in range(n)]
            empty=[set() for _ in range(n)]
            self.assertEqual(_clique_number_neighbors(full),n)
            self.assertEqual(_clique_number_neighbors(empty),1)
            omega,bad,M=_motzkin_weighted_check(empty,[Fraction(1)]*n)
            self.assertEqual(omega,1)
            self.assertEqual(bad,0)
            self.assertEqual(M,n*n)

    def test_real_true_original_geometry_and_two_owned_physical_diagonals(self):
        for c in (_actual_source(2,"lex","full"),
                  _actual_source(2,"reverse","full"),
                  _actual_source(2,"shift","Z17")):
            for i in c["ids"]:
                self.assertEqual(sum(v==i for v in c["owner"].values()),2)
                self.assertTrue(all(i in c["J"][j] for j in c["J"][i]))
            self.assertEqual(len(c["owner"]),2*len(c["ids"]))
            self.assertLessEqual(c["actual_J_max"],K)

    def test_independent_source_full_original_pair_marginal_harris(self):
        c=_actual_source(2,"lex","full")
        paths=_proper_true_original_p3(c,40)
        ws=_original_path_weights(c,paths)
        self.assertEqual(len(paths),len(ws))
        for (_,os),p in zip(paths,ws):
            self.assertEqual(p,_source_joint_priority(os,c["J"])/64)
            self.assertGreaterEqual(p,Fraction(1,64*65**3))
            self.assertLessEqual(p,Fraction(1,64))

    def test_no_fake_source_conflicts_inside_actual_proper_paths(self):
        c=_actual_source(2,"lex","full")
        paths=_proper_true_original_p3(c)
        for vs,os in paths:
            self.assertEqual(len(set(os)),3)
            self.assertEqual(len({v[0] for v in vs}),4)
            self.assertEqual(len({v[1] for v in vs}),4)
            self.assertFalse(any(j in c["J"][i] for i,j in combinations(os,2)))

    def test_compatibility_is_true_original_J_or_four_inner_cross_hits(self):
        c=_actual_source(2,"lex","full")
        arr=_proper_true_original_p3(c)
        endpoint=defaultdict(list)
        for a in arr:endpoint[(a[0][0],a[0][-1])].append(a)
        seen=set()
        for group in endpoint.values():
            for a,b in combinations(group,2):
                r=_pair_reason(a,b,c)
                if r not in seen:seen.add(r)
                if r=="first_typed_inner_opposite_depth":
                    self.assertTrue(_x_conflict(a,b,0))
                if r=="second_typed_inner_opposite_depth":
                    self.assertTrue(_x_conflict(a,b,1))
                if r=="compatible":
                    self.assertFalse(_x_conflict(a,b,0))
                    self.assertFalse(_x_conflict(a,b,1))
        self.assertEqual(seen,{"compatible","true_original_J_conflict",
            "first_typed_inner_opposite_depth","second_typed_inner_opposite_depth"})

    def test_independent_previous_true_source_weighted_ledger_test_only(self):
        # Prior AA4 code is used ONLY IN TEST, not imported by the new source.
        from hyp105_original_harris_product_selector_referee import (
            _actual_original_source,_actual_proper_paths,
            _original_source_incompatible_path_weight
        )
        for row in self.rows[:3]:
            old=_actual_original_source(2,row["fixed_source_pair_scheme"],
                                        row["original_CORE_scheme"])
            paths=_actual_proper_paths(old,3)
            r=_original_source_incompatible_path_weight(old,paths)
            self.assertEqual(row["exact_weighted_M"],
                r["actual_exact_mean_Frobenius2_G_plus_B"])
            self.assertEqual(row["exact_weighted_G"],r["actual_exact_compatible_G"])
            self.assertEqual(row["exact_weighted_B"],r["actual_exact_incompatible_B"])

    def test_invalid_original_source_and_bad_abstract_graph_fail_closed(self):
        for s in (1,3,5,8):
            with self.assertRaises(ValueError):_actual_source(s)
        for scheme in ("random","invalid"):
            with self.assertRaises(ValueError):_actual_source(2,scheme)
        with self.assertRaises(ValueError):_actual_source(2,"lex","cloned")
        with self.assertRaises(ValueError):
            _motzkin_weighted_check([set()],(Fraction(0),))
        with self.assertRaises(ValueError):
            _motzkin_weighted_check([set()],(Fraction(1),Fraction(2)))


if __name__=="__main__":
    unittest.main()
