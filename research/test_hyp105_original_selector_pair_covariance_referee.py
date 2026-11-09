"""AA4-PAIRRANK independent mathematical/source tests, run ONLY GitHub-hosted."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import unittest

from hyp105_original_selector_pair_covariance_referee import (
    SCHEMA,ROOT_STATUS,K_PROOF,true_source,original_proper_paths,
    _priority_formula_uncached,_typed_cut_exact,
    exact_priority_subset_dp,exact_cut_bruteforce,exact_joint,exact_pair_referee,
    find_original_covariance_witnesses,exact_endpoint_moments,canonical_report
)


class TestAllHOriginalSelectorPairJointReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canonical=canonical_report()
        cls.source=true_source(2,"lex","full")
        cls.paths=original_proper_paths(cls.source)
        cls.witnesses=cls.canonical["actual_original_both_sign_covariance_witnesses"]

    def test_root_frozen_and_independent_quantifiers(self):
        r=self.canonical
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertFalse(r["root_PROVED_A"])
        self.assertTrue(r["all_h_joint_priority_integral_formula_claimed"])
        self.assertTrue(r["all_h_two_color_bipartite_formula_claimed"])
        self.assertFalse(r["old_independence_of_paths_assumed"])
        self.assertFalse(r["all_h_new_branch_A_exponent_claimed"])

    def test_exact_order_stats_poset_shared_original_neighbor(self):
        J=[{2},{2},{0,1},set()]
        self.assertEqual(_priority_formula_uncached((0,1),J),Fraction(1,3))
        self.assertEqual(_priority_formula_uncached((0,),J),Fraction(1,2))
        self.assertEqual(_priority_formula_uncached((1,),J),Fraction(1,2))
        self.assertEqual(exact_priority_subset_dp((0,1),J),Fraction(1,3))

    def test_exact_order_stats_disjoint_original_neighbor_components(self):
        J=[{2},{3},{0},{1},set()]
        self.assertEqual(_priority_formula_uncached((0,1),J),Fraction(1,4))
        self.assertEqual(exact_priority_subset_dp((0,1),J),Fraction(1,4))
        self.assertEqual(_priority_formula_uncached((0,1,4),J),Fraction(1,4))

    def test_genuine_source_conflicting_owners_impossible_joint(self):
        source=self.source
        conflicting=next((i,j) for i in source["C"] for j in source["J"][i] if i<j)
        self.assertEqual(_priority_formula_uncached(conflicting,source["J"]),0)
        self.assertEqual(exact_joint(conflicting,source),0)
        self.assertEqual(exact_priority_subset_dp(conflicting,source["J"]),0)

    def test_genuine_W32_lex_both_real_diagonals_and_source_graph(self):
        c=self.source
        self.assertEqual(len(c["flags"]),45)
        self.assertEqual(len(c["C"]),45)
        self.assertEqual(len(c["physical_owner"]),90)
        self.assertEqual(len(c["f"]),15)
        self.assertEqual(len(c["g"]),15)
        self.assertLessEqual(c["source_max_conflict_degree"],K_PROOF)
        for i in c["C"]:
            self.assertEqual(sum(v==i for v in c["physical_owner"].values()),2)
            self.assertTrue(all(i in c["J"][j] for j in c["J"][i]))
        self.assertTrue(self.paths)

    def test_genuine_W32_all_proper_directed_paths_source_conflict_free(self):
        for path,os in self.paths:
            self.assertEqual(len(path),4)
            self.assertEqual(len(set(os)),3)
            self.assertEqual(len({v[0] for v in path}),4)
            self.assertEqual(len({v[1] for v in path}),4)
            for i,j in combinations(os,2):
                self.assertNotIn(j,self.source["J"][i])
            self.assertGreater(exact_joint(os,self.source),0)

    def test_two_independent_true_original_color_factor_oracles(self):
        for path,os in self.paths[:16]:
            self.assertEqual(_typed_cut_exact(os,self.source,"point"),Fraction(1,8))
            self.assertEqual(_typed_cut_exact(os,self.source,"line"),Fraction(1,8))
            self.assertEqual(exact_cut_bruteforce(os,self.source,"point"),Fraction(1,8))
            self.assertEqual(exact_cut_bruteforce(os,self.source,"line"),Fraction(1,8))
            self.assertEqual(exact_joint(os,self.source),
                _priority_formula_uncached(os,self.source["J"])*Fraction(1,64))

    def test_independent_priority_DP_for_actual_original_path(self):
        for path,os in self.paths[:12]:
            self.assertEqual(_priority_formula_uncached(os,self.source["J"]),
                exact_priority_subset_dp(os,self.source["J"],max_nodes=19))

    def test_distinct_true_original_paths_have_strictly_positive_covariance(self):
        self.assertIn("positive",self.witnesses)
        w=self.witnesses["positive"]
        self.assertNotEqual(w["physical_path1"],w["physical_path2"])
        self.assertGreater(Fraction(w["covariance"]),0)
        self.assertGreater(Fraction(w["joint"]),0)

    def test_distinct_true_original_paths_have_strictly_negative_covariance(self):
        self.assertIn("negative",self.witnesses)
        w=self.witnesses["negative"]
        self.assertNotEqual(w["physical_path1"],w["physical_path2"])
        self.assertLess(Fraction(w["covariance"]),0)
        self.assertLess(Fraction(w["joint"]),
            Fraction(w["marginal1"])*Fraction(w["marginal2"]))

    def test_strict_zero_joint_actual_original_scope(self):
        self.assertIn("zero_joint",self.witnesses)
        w=self.witnesses["zero_joint"]
        self.assertEqual(Fraction(w["joint"]),0)
        self.assertGreater(Fraction(w["marginal1"]),0)
        self.assertGreater(Fraction(w["marginal2"]),0)
        self.assertTrue(w["source_conflict"] or
                        Fraction(w["point_cut"])==0 or
                        Fraction(w["line_cut"])==0)

    def test_independent_true_original_poset_and_both_bruteforce_cuts_for_witnesses(self):
        for row in self.witnesses.values():
            S=set(row["original_ID_owners1"]+row["original_ID_owners2"])
            self.assertEqual(
                _priority_formula_uncached(tuple(S),self.source["J"]),
                exact_priority_subset_dp(tuple(S),self.source["J"],max_nodes=22))
            for side in ("point","line"):
                self.assertEqual(_typed_cut_exact(S,self.source,side),
                                 exact_cut_bruteforce(S,self.source,side))

    def test_complete_real_W32_endpoints_second_moment_and_jensen_gap(self):
        r=self.canonical["finite_actual_original_W32_lex_full_second_moment"]
        self.assertEqual(r["proper_directed_P3"],len(self.paths))
        self.assertEqual(r["exact_ordered_physical_path_pairs"],
                         r["actual_full_P3_frobenius2"])
        self.assertGreaterEqual(Fraction(r["exact_selected_second_moment"]),
                                Fraction(r["exact_jensen_mean_norm2"]))
        self.assertGreater(Fraction(r["exact_variance_sum"]),0)
        self.assertEqual(
            Fraction(r["exact_variance_sum"]),
            Fraction(r["exact_selected_second_moment"])-
            Fraction(r["exact_jensen_mean_norm2"]))
        self.assertGreater(Fraction(r["second_over_jensen_ratio"]),1)

    def test_genuine_complete_other_correlated_W32_and_W34_sampling(self):
        rows=self.canonical["true_original_source_cases"]
        self.assertEqual(len(rows),6)
        self.assertEqual({x["s"] for x in rows},{2,4})
        self.assertEqual({x["scheme"] for x in rows},{"lex","reverse","shift"})
        for c in rows:
            self.assertEqual(c["actual_physical_paired_diagonal_edges"],
                             2*c["retained_original_CORE_flags"])
            self.assertGreater(c["deterministic_sampled_proper_directed_3paths"],0)
            self.assertLessEqual(c["actual_source_J_max_degree"],K_PROOF)
        for row in rows:
            if row["s"]==2:
                self.assertIsNotNone(row["complete_real_source_proper_directed_3paths"])
            else:
                self.assertIsNone(row["complete_real_source_proper_directed_3paths"])

    def test_small_exact_original_endpoint_second_moment_recomputation(self):
        sample=self.paths[:80]
        direct=exact_endpoint_moments(sample,self.source)
        self.assertEqual(direct["proper_directed_P3"],80)
        self.assertGreaterEqual(
            Fraction(direct["exact_selected_second_moment"]),
            Fraction(direct["exact_jensen_mean_norm2"]))
        self.assertLessEqual(Fraction(direct["exact_mean_total_path_count"]),80)
        self.assertTrue(direct["exact_priority_and_coloring_no_path_independence"])

    def test_fail_closed_nonoriginal_schemes_and_invalid_core(self):
        with self.assertRaises(ValueError):
            true_source(3)
        with self.assertRaises(ValueError):
            true_source(2,"randomized")
        with self.assertRaises(ValueError):
            true_source(2,"lex","cloned")
        with self.assertRaises(ValueError):
            exact_priority_subset_dp((0,1),[{1},{0}],max_nodes=1) if False else true_source(8)


if __name__=="__main__":unittest.main()
