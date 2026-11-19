"""AA4-LOW-AC-CLEAN: independent true GQ endpoint/dual source book tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_low_projection_clean_books import (
    SCHEMA,STATUS,PARENT,canonical_pair,other,min_pairs,genuine_original,
    true_gq_projection,physical_source_edges,physical_graph,key_books,
    _decode_from_key,physical_first_triples,true_paths_and_blockers,
    projected_delete_role_report,certificate_case,certificate,
)


class TestLOWProjectionCleanSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_true_original_dual_GQ_W32_W34_cardinality(self):
        for s in (2,4):
            z=genuine_original(s,"lex",core_scheme="full")
            self.assertEqual(z["V"],(s+1)*(s*s+1))
            self.assertEqual(z["N"],(s+1)**2*(s*s+1))
            self.assertEqual(z["A"],z["C"])
            self.assertEqual(len(set(z["f"])),z["V"])
            self.assertEqual(len(set(z["g"])),z["V"])

    def test_02_real_GQ_offincidence_projection_unique_all_pairs(self):
        for s in (2,4):
            src=genuine_original(s,"reverse")
            g=true_gq_projection(src)
            self.assertEqual(len(g["proj"]),src["V"]**2-src["N"])
            for (q,r),(p,ell) in g["proj"].items():
                self.assertNotIn((q,r),g["fid"])
                for a in ((q,ell),(p,ell),(p,r)):
                    self.assertIn(a,g["fid"])
                self.assertNotEqual(q,p)

    def test_03_ALL_named_original_flags_are_s2_each_projection_role(self):
        for s in (2,4):
            src=genuine_original(s,"shift")
            g=true_gq_projection(src)
            for role in ("qell","pell","pr"):
                self.assertEqual(len(g["roles"][role]),src["N"])
                self.assertEqual(set(g["roles"][role].values()),{s*s})
                self.assertEqual(sum(g["roles"][role].values()),
                                 src["V"]**2-src["N"])

    def test_04_original_A_and_C_two_real_disjoint_physical_diagonals(self):
        for c in self.c["original_true_W32_W34_cases"]:
            self.assertEqual(c["ORIGINAL_physical_FULL_A_edges"],2*c["original_A_full_allowed_flags"])
            self.assertEqual(c["ORIGINAL_physical_paired_CORE_edges"],2*c["original_paired_CORE_flags"])
            self.assertGreaterEqual(c["original_A_full_allowed_flags"],
                                    c["original_paired_CORE_flags"])
            self.assertTrue(c["original_A_NOT_CORE_projection_anchors_supported"])

    def test_05_genuine_full_A_core_C_theta_and_weighted_fourth_trace(self):
        for c in self.c["original_true_W32_W34_cases"]:
            self.assertGreaterEqual(c["exact_TRUE_original_mixed_theta"],0)
            self.assertGreaterEqual(c["original_CORE_trace4"],0)
            self.assertLessEqual(c["original_CORE_degree_weighted_trace4"],
                                 c["original_CORE_actual_Delta"]*c["original_CORE_trace4"])

    def test_06_new_clean_book_never_exceeds_old_original_full_A_C_book(self):
        for c in self.c["original_true_W32_W34_cases"]:
            for side in ("source_point_x","source_line_y"):
                b=c[side]
                self.assertLessEqual(b["NEW_projection_clean_endpoint_good_A_C_book"],
                                     b["full_historical_A_C_book"])
                self.assertEqual(b["removed_invalid_original_source_book_keys"],
                    b["full_historical_A_C_book"]-
                    b["NEW_projection_clean_endpoint_good_A_C_book"])
                self.assertEqual(b["removed_invalid_original_source_book_keys"],
                    sum(b["original_filtered_reason_counts"].values()))

    def test_07_nonvacuous_STRICT_source_reduction_point_and_line(self):
        cases=self.c["original_true_W32_W34_cases"]
        for side in ("source_point_x","source_line_y"):
            valid=[c for c in cases
                   if c[side]["removed_invalid_original_source_book_keys"]>0]
            self.assertGreater(len(valid),0)
            self.assertTrue(any(c["s"]==4 for c in valid))

    def test_08_new_PHYSICAL_first_source_key_has_explicit_left_inverse(self):
        for s,mode in ((2,"reverse"),(4,"lex"),(4,"reverse")):
            src=genuine_original(s,mode)
            gq=true_gq_projection(src)
            physical=physical_graph(src)
            books=key_books(src,gq)
            tri=physical_first_triples(src,gq,physical,books)["triples"]
            for side in ("x","y"):
                self.assertEqual(len(set(tri[side].values())),len(tri[side]))
                for triple,key in tri[side].items():
                    self.assertIn(key,books["clean"][side])
                    self.assertEqual(_decode_from_key(src,key,side),triple)

    def test_09_all_TRUE_physical_first_triples_are_subset_of_clean_books(self):
        for c in self.c["original_true_W32_W34_cases"]:
            for side in ("source_point_x","source_line_y"):
                b=c[side]
                self.assertLessEqual(b["actual_first_physical_blocker_triples"],
                                     b["NEW_projection_clean_endpoint_good_A_C_book"])
                self.assertTrue(b["clean_source_witness_is_left_invertible"])

    def test_10_exact_weighted_first_blocker_chain_point_and_dual(self):
        for c in self.c["original_true_W32_W34_cases"]:
            for side in ("source_point_x","source_line_y"):
                b=c[side]
                self.assertLessEqual(b["actual_first_physical_blocker_paths"],
                                     b["clean_true_first_two_walk_weight"])
                self.assertLessEqual(b["clean_true_first_two_walk_weight"]**2,
                    b["actual_first_physical_blocker_triples"]*b["clean_exact_two_walk_square"])
                self.assertLessEqual(b["clean_exact_two_walk_square"],
                    c["original_CORE_degree_weighted_trace4"])
                self.assertLessEqual(b["actual_first_physical_blocker_paths"]**2,
                    b["NEW_projection_clean_endpoint_good_A_C_book"]*
                    c["original_CORE_degree_weighted_trace4"])
                self.assertTrue(b["all_original_weighted_blocker_charge_exactly_checked"])

    def test_11_all_four_FIRST_LAST_inner_blockers_reverse_same_projection(self):
        for c in self.c["original_true_W32_W34_cases"]:
            b=c["original_ALL_four_blocker_counts"]
            self.assertEqual(b.get("x1",0),b.get("x2",0))
            self.assertEqual(b.get("y1",0),b.get("y2",0))
            self.assertEqual(b.get("x1",0),c["source_point_x"]["actual_first_physical_blocker_paths"])
            self.assertEqual(b.get("y1",0),c["source_line_y"]["actual_first_physical_blocker_paths"])
            self.assertLessEqual(c["actual_four_blocker_union"],sum(b.values()))

    def test_12_real_GQ_actual_proper_P3_and_endpoint_good_are_counted(self):
        for c in self.c["original_true_W32_W34_cases"]:
            self.assertLessEqual(c["actual_TRUE_endpoint_good_P3"],
                                 c["actual_original_proper_physical_P3"])
            self.assertLessEqual(c["actual_four_blocker_union"],
                                 c["actual_TRUE_endpoint_good_P3"])
        self.assertTrue(any(c["actual_TRUE_endpoint_good_P3"]>0
                            for c in self.c["original_true_W32_W34_cases"]))

    def test_13_REAL_original_anchors_outside_C_must_not_be_deleted(self):
        cases=[c for c in self.c["original_true_W32_W34_cases"]
               if c["original_FULL_not_equal_CORE"] and
               c["source_point_x"]["original_anchor_triples_OUTSIDE_CORE"]+
               c["source_line_y"]["original_anchor_triples_OUTSIDE_CORE"]>0]
        self.assertTrue(cases)
        self.assertTrue(any(c["s"]==4 for c in cases))
        self.assertTrue(all(c["original_A_NOT_CORE_projection_anchors_supported"] for c in cases))

    def test_14_original_deleted_projection_role_counts_exact_all_h_finite(self):
        for c in self.c["original_true_W32_W34_cases"]:
            p=c["deletion_projection"];s=c["s"]
            for k in ("exact_bad_source_qell_role","exact_bad_source_pell_role",
                      "exact_bad_source_pr_role"):
                self.assertEqual(p[k],s*s*p["original_source_deleted_IDs"])
            self.assertLessEqual(p["physical_deleted_endpoints_upper"],
                                 p["all_h_deleted_physical_bound"])
            self.assertEqual(p["all_h_role_count_per_named_flag"],s*s)

    def test_15_nonempty_Z_removed_source_role_union_not_assumed_disjoint(self):
        cases=[c["deletion_projection"] for c in self.c["original_true_W32_W34_cases"]
               if c["deletion_projection"]["original_source_deleted_IDs"]>0]
        self.assertGreater(len(cases),0)
        for p in cases:
            self.assertGreater(p["number_bad_genuine_projection_pairs"],0)
            self.assertLessEqual(p["number_bad_genuine_projection_pairs"],
                p["exact_bad_source_qell_role"]+p["exact_bad_source_pell_role"]+
                p["exact_bad_source_pr_role"])
            self.assertEqual(p["physical_endpoint_orientations_per_qr"],4)

    def test_16_full_original_root_no_Z_projection_deleted_term_exact_zero(self):
        cases=[c for c in self.c["original_true_W32_W34_cases"]
               if c["deletion_projection"]["original_source_deleted_IDs"]==0]
        self.assertGreater(len(cases),0)
        for c in cases:
            p=c["deletion_projection"]
            self.assertEqual(p["number_bad_genuine_projection_pairs"],0)
            self.assertEqual(p["all_h_deleted_physical_bound"],0)

    def test_17_illegal_true_symplectic_source_and_CORE_rejected(self):
        with self.assertRaises(ValueError):
            genuine_original(3,"lex")
        with self.assertRaises(ValueError):
            genuine_original(2,"invalid")
        with self.assertRaises(ValueError):
            genuine_original(2,"lex",removed=(-1,))
        with self.assertRaises(ValueError):
            genuine_original(2,"lex",removed=(999,))
        with self.assertRaises(ValueError):
            genuine_original(2,"lex",core_scheme="wrong")
        with self.assertRaises(ValueError):
            min_pairs(0)

    def test_18_actual_source_full_vs_core_and_full_original_GQ(self):
        for c in self.c["original_true_W32_W34_cases"]:
            self.assertEqual(c["true_genuine_offincidence_projection_count"],
                             (c["s"]+1)**2*(c["s"]**2+1)**2 -c["original_GQ_named_flags"])
            self.assertTrue(c["each_original_GQ_source_flag_in_each_three_roles_exactly_s2"])

    def test_19_material_nonempty_clean_books_and_blocked_true_P3(self):
        cases=self.c["original_true_W32_W34_cases"]
        self.assertTrue(any(c["source_point_x"]["NEW_projection_clean_endpoint_good_A_C_book"]>0
                            for c in cases))
        self.assertTrue(any(c["source_line_y"]["NEW_projection_clean_endpoint_good_A_C_book"]>0
                            for c in cases))
        self.assertTrue(any(c["source_point_x"]["actual_first_physical_blocker_paths"]>0 or
                            c["source_line_y"]["actual_first_physical_blocker_paths"]>0
                            for c in cases))

    def test_20_stops_ROOT_PROVED_A_and_NEW_source_scope(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["parent_pr"],779)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["status"],STATUS)
        for k in (
            "newly_proved_original_projection_filtered_books_x_y",
            "all_h_true_GQ_three_projection_anchor_roles_exact_s2",
            "original_FULL_A_vs_CORE_C_never_conflated",
            "independent_all_h_four_physical_blocker_reverse_and_dual_books_proved",
            "all_h_weighted_fourth_trace_not_independent_path_probability",
            "exact_SOURCE_book_reduction_valid_but_NO_universal_B0_improvement_claim",
            "source_P3_to_BBo_full_inverse_not_newly_accepted",
            "no_numerical_C6_graph_constants_invented"):
            self.assertTrue(c[k],k)
        self.assertFalse(c["root_unweighted_seven_class_PROVED_A"])
        self.assertEqual(len(c["original_true_W32_W34_cases"]),7)
        self.assertEqual(c["next_scientific_gate"],
                         "ORIGINAL_P3_BBo_SIXSET_TWO_DIRECTION_INVERSE_AND_ROOT_DAG")


if __name__=="__main__":
    unittest.main()
