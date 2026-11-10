"""AA4-FULL-W34: all-order source-middle inversion and full original weighted risk tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_full_w34_weighted_risk_referee import (
    SCHEMA,ROOT_STATUS,K,Q,THRESHOLD,_source,_true_original_proper_P3,
    _rank_probability3,_pair_bad,_exact_clique,_full_exact_case,
    canonical_report
)


class TestIndependentOriginalFullW34Risk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.rows=cls.report["complete_independently_verified_original_W32_W34_source_census"]

    def test_root_unpromoted_and_scoped_research(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["issue"],230)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["all_h_global_B_over_M_below_3_over_4_PROVED"])
        self.assertFalse(r["numerical_external_C6_graph_constants_claimed"])
        self.assertFalse(r["ASET_exponent_claimed"])
        self.assertFalse(r["local_s2_counterexample_to_global_B_over_M_claimed"])
        self.assertTrue(r["all_h_new_source_hybrid_diagonal_plus_weighted_Motzkin_theorem"])
        self.assertTrue(r["all_h_nonvacuous_risk_requires_omega5_AND_effective_multiplicity_gt4"])
        self.assertTrue(r["all_h_unique_oriented_middle_physical_edge_and_max_four_paths_per_original_midflag"])

    def test_complete_original_W32_baselines_all_physical_paths(self):
        self.assertEqual([x["full_true_coordinate_proper_P3_count"] for x in self.rows[:3]],
                         [1346,1154,838])
        self.assertEqual([x["true_source_physical_edges"] for x in self.rows[:3]],
                         [90,90,84])
        for x in self.rows[:3]:
            self.assertEqual(x["source_original_flag_ID_count"],45)
            self.assertEqual(x["source_GQ_point_count"],15)
            self.assertEqual(x["actual_physical_pair_alphabet_size"],6)
            self.assertTrue(x["full_source_complete_census"])
        self.assertEqual(self.rows[2]["source_deleted_original_IDs"],3)

    def test_complete_original_W34_FULL_425_flags_and_850_edges(self):
        self.assertEqual([x["full_true_coordinate_proper_P3_count"] for x in self.rows[3:5]],
                         [83892,82846])
        for row in self.rows[3:6]:
            self.assertEqual(row["original_s"],4)
            self.assertEqual(row["original_CORE"],"full")
            self.assertEqual(row["source_GQ_point_count"],85)
            self.assertEqual(row["source_original_flag_ID_count"],425)
            self.assertEqual(row["source_retained_original_flags"],425)
            self.assertEqual(row["true_source_physical_edges"],850)
            self.assertEqual(row["source_deleted_original_IDs"],0)
            self.assertEqual(row["actual_physical_pair_alphabet_size"],14)
            self.assertTrue(row["full_source_complete_census"])

    def test_partial_original_W34_even_and_Z17_are_FULL_CENSUS_OF_CORES(self):
        for row in self.rows[6:]:
            self.assertEqual(row["original_s"],4)
            self.assertEqual(row["source_original_flag_ID_count"],425)
            self.assertLess(row["source_retained_original_flags"],425)
            self.assertEqual(row["true_source_physical_edges"],2*row["source_retained_original_flags"])
            self.assertGreater(row["source_deleted_original_IDs"],0)
            self.assertTrue(row["full_source_complete_census"])
            self.assertTrue(row["source_rho_small_Z_admissibility_NOT_claimed"])

    def test_all_original_path_probabilities_positive_and_J_K64(self):
        for row in self.rows:
            self.assertLessEqual(row["original_J_max_degree"],K)
            self.assertGreater(row["exact_unique_original_source_priority_threeowner_triples"],0)
            self.assertGreater(row["full_true_coordinate_proper_P3_count"],0)
            self.assertGreater(row["true_original_ordered_endpoint_bins"],0)
            self.assertGreater(row["true_original_ordered_same_endpoint_path_pairs"],0)
            self.assertGreaterEqual(row["true_original_ordered_same_endpoint_path_pairs"],
                row["full_true_coordinate_proper_P3_count"])

    def test_original_directed_middle_source_anchor_unique_per_endpoint(self):
        for row in self.rows:
            self.assertLessEqual(row["max_same_original_middle_flag_P3_per_bin"],4)
            self.assertGreater(row["max_same_original_middle_flag_P3_per_bin"],0)
        c=_source(2,"lex","full")
        for path,owners in _true_original_proper_P3(c):
            p,l=c["flags"][owners[1]]
            self.assertEqual(tuple(sorted((path[1][0],path[2][0]))),c["f"][p])
            self.assertEqual(tuple(sorted((path[1][1],path[2][1]))),c["g"][l])

    def test_weighted_M_B_G_and_disjoint_path_pair_conservation(self):
        for row in self.rows:
            M=Fraction(row["M"])
            G=Fraction(row["G"])
            B=Fraction(row["B"])
            self.assertGreater(M,0)
            self.assertGreater(G,0)
            self.assertGreaterEqual(B,0)
            self.assertEqual(G+B,M)
            self.assertEqual(G/M,Fraction(row["G_over_M"]))
            self.assertEqual(B/M,Fraction(row["B_over_M"]))
            self.assertEqual(sum(row["full_disjoint_actual_path_pair_source_classes"].values()),
                         row["true_original_ordered_same_endpoint_path_pairs"])

    def test_new_all_h_hybrid_bound_exact_Fractions_every_original_case(self):
        for row in self.rows:
            M=Fraction(row["M"]);G=Fraction(row["G"])
            diag=Fraction(row["diagonal_source_path_weight"])
            ms=Fraction(row["weighted_Motzkin_only_source_G_lower"])
            hybrid=Fraction(row["new_weighted_hybrid_Motzkin_diagonal_G_lower"])
            self.assertGreaterEqual(G,hybrid)
            self.assertGreaterEqual(hybrid,diag)
            self.assertGreaterEqual(hybrid,ms)
            self.assertGreaterEqual(ms,M/Q)
            self.assertEqual(Fraction(row["new_certified_B_over_M_hybrid_upper"]),1-hybrid/M)
            self.assertEqual(hybrid-ms,Fraction(row["hybrid_improvement_above_motzkin_G_lower"]))
            self.assertGreaterEqual(diag,0)

    def test_improved_neff_bin_obstruction_numerically_all_sources(self):
        for row in self.rows:
            self.assertLessEqual(row["bins_jointly_omega_at_least_5_and_n_eff_gt_4"],
                                 row["bins_with_omega_at_least_5"])
            self.assertLessEqual(Fraction(row["M_share_jointly_omega_at_least_5_and_n_eff_gt_4"]),
                                 Fraction(row["M_share_omega_at_least_5"]))
            self.assertLessEqual(row["bins_with_actually_local_B_over_M_gt_3_over_4"],
                                 row["bins_jointly_omega_at_least_5_and_n_eff_gt_4"])

    def test_actual_local_endpoint_bad_extreme_original_source_witness(self):
        for row in self.rows:
            x=row["top_actual_bad_local_endpoint_witness"]
            self.assertEqual(len(x["real_path_owners"]),x["paths"])
            self.assertEqual(len(x["real_path_vertices"]),x["paths"])
            self.assertEqual(len(x["source_marginals"]),x["paths"])
            self.assertGreater(Fraction(x["local_M"]),0)
            self.assertEqual(Fraction(x["local_B"])/Fraction(x["local_M"]),
                             Fraction(x["local_ratio"]))
            self.assertLessEqual(Fraction(x["local_B"]),Fraction(x["local_M"]))
            c=_source(row["original_s"],row["original_scheme"],row["original_CORE"])
            ends=tuple(map(tuple,x["endpoints"]))
            W=Fraction(0)
            D=Fraction(0)
            for vs,os,p in zip(x["real_path_vertices"],x["real_path_owners"],x["source_marginals"]):
                phys=tuple(map(tuple,vs))
                self.assertEqual((phys[0],phys[-1]),ends)
                self.assertEqual(len(phys),4)
                self.assertEqual(len(os),3)
                self.assertTrue(set(os)<=set(c["ids"]))
                for j in range(3):
                    key=tuple(sorted((phys[j],phys[j+1])))
                    self.assertEqual(c["owner"][key],os[j])
                proba=_rank_probability3(tuple(os),c["J"])/64
                self.assertEqual(Fraction(p),proba)
                W+=proba;D+=proba**2
            self.assertEqual(W*W,Fraction(x["local_M"]))
            self.assertEqual(W*W/D,Fraction(x["effective_multiplicity"]))

    def test_real_original_exact_W32_lex_prior_independent_risk_regression(self):
        row=self.rows[0]
        self.assertEqual(Fraction(row["M"]),
                         Fraction(170009657654496199,164130319761408000000))
        self.assertEqual(Fraction(row["B_over_M"]),
                         Fraction(395498199363009600,1190067603581473393))
        self.assertEqual(row["max_incompatibility_clique_over_all_real_endpoints"],6)
        self.assertEqual(row["true_original_ordered_same_endpoint_path_pairs"],4370)

    def test_real_original_exact_W32_reverse_prior_independent_risk_regression(self):
        row=self.rows[1]
        self.assertEqual(Fraction(row["B_over_M"]),
                         Fraction(2197221736032,6861627242215))
        self.assertEqual(row["max_incompatibility_clique_over_all_real_endpoints"],4)
        self.assertEqual(row["true_original_ordered_same_endpoint_path_pairs"],2942)

    def test_true_original_odd_cycle_classification_symmetry(self):
        c=_source(2,"lex","full")
        paths=list(_true_original_proper_P3(c))
        bins={}
        for v in paths:
            key=v[0][0],v[0][-1]
            bins.setdefault(key,[]).append(v)
        counts=Counter()
        for group in bins.values():
            for a,b in combinations(group,2):
                reason=_pair_bad(*a,*b,c["J"])
                self.assertEqual(reason,_pair_bad(*b,*a,c["J"]))
                counts[reason]+=1
        self.assertGreater(counts["compatible"],0)
        self.assertGreater(counts["original_J_conflict"],0)
        self.assertGreater(counts["first_typed_opposite_depth"],0)
        self.assertGreater(counts["second_typed_opposite_depth"],0)

    def test_exact_rank_probability_local_sources_and_valid_rejection(self):
        c=_source(2,"lex","full")
        path,os=next(iter(_true_original_proper_P3(c)))
        self.assertGreater(_rank_probability3(os,c["J"]),0)
        self.assertLessEqual(_rank_probability3(os,c["J"]),1)
        with self.assertRaises(ValueError):
            _rank_probability3((os[0],os[0],os[2]),c["J"])
        with self.assertRaises(ValueError):
            _rank_probability3((os[0],),c["J"])

    def test_abstract_graph_clique_exact_small(self):
        for n in range(1,8):
            self.assertEqual(_exact_clique([set(range(n))-{i} for i in range(n)]),n)
            self.assertEqual(_exact_clique([set() for i in range(n)]),1)

    def test_abstract_omega_large_neff_small_forced_strict_good(self):
        # A K5 with weights (10,1,1,1,1), n_eff=(14)^2/(100+4)<4.
        w=[Fraction(10),Fraction(1),Fraction(1),Fraction(1),Fraction(1)]
        W=sum(w,Fraction(0));M=W*W;diag=sum((p*p for p in w),Fraction(0))
        self.assertEqual(_exact_clique([set(range(5))-{i} for i in range(5)]),5)
        self.assertGreater(diag,M/4)
        self.assertLess(1-diag/M,Fraction(3,4))
        self.assertGreater(diag,M/5)

    def test_abstract_true_large_k_local_bad_can_exceed_three_fourths(self):
        w=[Fraction(1)]*5
        W=sum(w);M=W*W
        B=M-sum(x*x for x in w)
        self.assertEqual(B/M,Fraction(4,5))
        self.assertGreater(B/M,THRESHOLD)

    def test_invalid_original_geometry_settings_fail_closed(self):
        for s in (1,3,8):
            with self.assertRaises(ValueError):_source(s)
        with self.assertRaises(ValueError):_source(2,"noninjective")
        with self.assertRaises(ValueError):_source(2,"lex","broken")


if __name__=="__main__":
    unittest.main()
