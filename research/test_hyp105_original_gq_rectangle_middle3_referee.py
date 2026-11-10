"""HYP-105 AA4-GQ-K22: independent source sharp middle-three and bad-owner ledger."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_defect_factor_referee import genuine_symplectic_source
from hyp105_original_full_w34_weighted_risk_referee import (
    SCHEMA,ROOT_STATUS,_validate_original_incidence_no_K22,
    _original_rectangle_no_k22_audit,_source,_true_original_proper_P3,
    _pair_bad,_rank_probability3,canonical_report
)


class TestOriginalGQRectangleMiddleThree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r=canonical_report()
        cls.rows=cls.r["complete_independently_verified_original_W32_W34_source_census"]

    def test_all_h_provenance_and_root_scientific_stop(self):
        r=self.r
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertEqual(r["issue"],230)
        self.assertTrue(r["all_h_true_original_GQ_rectangle_no_K2_2_strict_max_three_middle_paths"])
        self.assertTrue(r["all_h_distinct_same_middle_flag_paths_are_source_incompatible"])
        self.assertTrue(r["all_h_middle_owner_coarse_effective_multiplicity_safety_gate"])
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["all_h_global_B_over_M_below_3_over_4_PROVED"])
        self.assertFalse(r["ASET_exponent_claimed"])

    def test_all_eight_genuine_original_symplectic_source_K22_absent(self):
        for r in self.rows:
            a=r["true_original_GQ_rectangle_K22_audit"]
            inv=a["original_source_incidence_K2_2_independent_audit"]
            n=r["source_GQ_point_count"]
            self.assertEqual(inv["original_point_pairs_checked"],n*(n-1)//2)
            self.assertEqual(inv["original_line_pairs_checked"],n*(n-1)//2)
            self.assertLessEqual(inv["max_original_lines_shared_by_two_points"],1)
            self.assertLessEqual(inv["max_original_points_shared_by_two_lines"],1)
            self.assertTrue(inv["true_source_incidence_K2_2_free"])
            self.assertTrue(a["four_neighbor_K2_2_incidence_forbidden"])
            self.assertEqual(a["all_h_middle_flag_same_endpoint_P3_upper"],3)

    def test_independent_original_K22_validator_REJECTS_four_incidence_rectangle(self):
        fake=((0,0),(0,1),(1,0),(1,1))
        with self.assertRaisesRegex(AssertionError,"FORBIDDEN"):
            _validate_original_incidence_no_K22(fake)

    def test_genuine_original_GQ_incidence_fixture_independent_of_label_scheme(self):
        for s in (2,4):
            f=tuple(map(tuple,genuine_symplectic_source(s)))
            x=_validate_original_incidence_no_K22(f)
            self.assertEqual(x["max_original_lines_shared_by_two_points"],1)
            self.assertEqual(x["max_original_points_shared_by_two_lines"],1)
            self.assertTrue(x["true_source_incidence_K2_2_free"])

    def test_exact_ALL_rectangles_and_physical_vertices_no_four_corner_neighbors(self):
        for r in self.rows:
            c=_source(r["original_s"],r["original_scheme"],r["original_CORE"])
            actual=_original_rectangle_no_k22_audit(c)
            self.assertEqual(actual,r["true_original_GQ_rectangle_K22_audit"])
            self.assertEqual(actual["original_source_rectangle_vertex_pairs_exhaustively_checked"],
                len(c["ids"])*len(c["adj"]))
            self.assertLessEqual(actual["max_real_neighbors_of_source_rectangle_corners"],3)

    def test_reproducible_TRUE_original_W32_three_middle_paths_sharp_witness(self):
        r=self.rows[1]
        self.assertEqual(r["original_s"],2)
        self.assertEqual(r["original_scheme"],"reverse")
        self.assertEqual(r["max_same_original_middle_flag_P3_per_bin"],3)
        w=r["genuine_original_three_same_middle_flag_path_witness"]
        self.assertIsNotNone(w)
        self.assertEqual(len(w["three_real_paths"]),3)
        c=_source(2,"reverse","full")
        midd=w["original_named_middle_source_flag"]
        e=tuple(map(tuple,w["actual_physical_ordered_endpoints"]))
        mids=set()
        for item in w["three_real_paths"]:
            v=tuple(map(tuple,item["physical_vertices"]))
            os=item["original_flag_owners"]
            self.assertEqual(len(os),3)
            self.assertEqual((v[0],v[-1]),e)
            self.assertEqual(os[1],midd)
            mids.add((v[1],v[2]))
            for z in range(3):
                self.assertEqual(c["owner"][tuple(sorted((v[z],v[z+1])))],os[z])
        self.assertEqual(len(mids),3)

    def test_all_complete_original_W32_W34_three_upper_no_four_witness(self):
        self.assertEqual([r["max_same_original_middle_flag_P3_per_bin"]
                          for r in self.rows],[2,3,3,2,2,2,2,2])
        for row in self.rows:
            self.assertLessEqual(row["max_same_original_middle_flag_P3_per_bin"],3)
            self.assertTrue(row["full_source_complete_census"])
            self.assertEqual(row["true_source_physical_edges"],
                             2*row["source_retained_original_flags"])

    def test_exact_all_same_middle_bad_source_mass_partition(self):
        for r in self.rows:
            B=Fraction(r["B"])
            same=Fraction(r["exact_incompatible_B_same_original_middle_flag"])
            different=Fraction(r["exact_incompatible_B_different_original_middle_flags"])
            M=Fraction(r["M"])
            diag=Fraction(r["diagonal_source_path_weight"])
            quadratic=Fraction(r["exact_original_middle_owner_quadratic_energy"])
            self.assertEqual(B,same+different)
            self.assertEqual(same,quadratic-diag)
            self.assertGreaterEqual(same,0)
            self.assertGreaterEqual(different,0)
            self.assertGreaterEqual(quadratic,diag)
            self.assertLessEqual(quadratic,3*diag)
            self.assertLessEqual(quadratic,M)
            self.assertEqual(Fraction(r["exact_same_middle_original_owner_bad_fraction_of_total_B"]),
                             same/B if B else Fraction(0))

    def test_exact_bad_source_midpair_counts_real_incompatible(self):
        for row in self.rows:
            self.assertGreaterEqual(row["same_middle_original_flag_incompatible_ordered_path_pairs"],0)
            self.assertLess(row["same_middle_original_flag_incompatible_ordered_path_pairs"],
                            row["true_original_ordered_same_endpoint_path_pairs"])
            self.assertEqual(sum(row["full_disjoint_actual_path_pair_source_classes"].values()),
                             row["true_original_ordered_same_endpoint_path_pairs"])

    def test_original_midflag_only_weight_source_safety_sufficient(self):
        for row in self.rows:
            self.assertGreaterEqual(row["source_midflag_only_sufficient_safe_endpoint_bins"],0)
            self.assertLessEqual(row["source_midflag_only_sufficient_safe_endpoint_bins"],
                                 row["true_original_ordered_endpoint_bins"])
            self.assertGreaterEqual(Fraction(row["source_midflag_only_sufficient_safe_M_share"]),0)
            self.assertLessEqual(Fraction(row["source_midflag_only_sufficient_safe_M_share"]),1)

    def test_all_genuine_original_middle_pair_cliques_from_edges(self):
        for c in (_source(2,"lex","full"),_source(2,"reverse","full"),
                  _source(2,"shift","Z17")):
            groups=defaultdict(list)
            for p,os in _true_original_proper_P3(c):
                groups[(p[0],p[-1],os[1])].append((p,os))
            self.assertGreater(len(groups),0)
            for key,group in groups.items():
                self.assertLessEqual(len(group),3)
                for a,b in combinations(group,2):
                    self.assertNotEqual(_pair_bad(a[0],a[1],b[0],b[1],c["J"]),
                                        "compatible")

    def test_all_h_three_owner_weighted_second_moment_Cauchy_exact(self):
        for row in self.rows:
            D=Fraction(row["diagonal_source_path_weight"])
            mid=Fraction(row["exact_original_middle_owner_quadratic_energy"])
            self.assertGreaterEqual(D,mid/3)
            self.assertGreaterEqual(mid,D)
            self.assertGreater(D,0)

    def test_only_middle_owner_source_can_ensure_n_eff_le4(self):
        # One middle owner has THREE positive weights; effective path count<=3,
        # strictly below the 4-path danger threshold regardless of correlations.
        for weights in ((1,1,1),(1,2,4),(2,3,3),(3,3,7)):
            p=[Fraction(v) for v in weights]
            W=sum(p,Fraction(0));D=sum((v*v for v in p),Fraction(0))
            q=W*W
            self.assertGreaterEqual(D,q/3)
            self.assertGreaterEqual(D,q/4)

    def test_two_midflags_skewed_group_masses_source_only_safe(self):
        # Coarse criterion Σ_i W_mid² >= 3/4*(Σ_i W_mid)² implies
        # actual D >= 1/3 Σ_i W_mid² >= M/4, without inspecting path weights.
        sourceweights=(Fraction(10),Fraction(1))
        W=sum(sourceweights,Fraction(0))
        Q=sum(v*v for v in sourceweights)
        self.assertGreaterEqual(Q,Fraction(3,4)*W*W)
        self.assertGreaterEqual(Q/3,W*W/4)
        self.assertLessEqual(3*W*W/Q,4)

    def test_strict_all_h_compensation_and_global_risk_not_promoted(self):
        for row in self.rows:
            G=Fraction(row["G"])
            M=Fraction(row["M"])
            S=Fraction(row["all_h_hybrid_safe_bin_slack_G_above_quarter"])
            T=Fraction(row["all_h_hybrid_unsafe_bin_deficit_G_below_quarter"])
            self.assertGreaterEqual(G,M/4+S-T)
            self.assertEqual(
                row["all_h_hybrid_sufficient_global_B_below_three_quarters"],S>T)
            self.assertLess(Fraction(row["B_over_M"]),Fraction(3,4))
        self.assertFalse(self.r["all_h_global_B_over_M_below_3_over_4_PROVED"])

    def test_real_original_lex_s2_s4_exact_prior_path_count_and_rational_B(self):
        self.assertEqual([x["full_true_coordinate_proper_P3_count"] for x in self.rows[:5]],
                         [1346,1154,838,83892,82846])
        self.assertEqual(Fraction(self.rows[0]["B_over_M"]),
                         Fraction(395498199363009600,1190067603581473393))
        self.assertEqual(Fraction(self.rows[3]["B_over_M"]),
                         Fraction(6455794325016624278974180549344,
                                  34112625017517015558762952579019))

    def test_invalid_original_source_geometry_and_forged_incidence_fail_closed(self):
        for s in (1,3,8):
            with self.assertRaises(ValueError):_source(s)
        forged=((0,0),(0,1),(1,0),(1,1),(2,2))
        with self.assertRaisesRegex(AssertionError,"K2,2"):
            _validate_original_incidence_no_K22(forged)


if __name__=="__main__":
    unittest.main()
