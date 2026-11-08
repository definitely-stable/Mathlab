"""Independent original full GQ projection and mixed A/C blocker red-team."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_original_gq_projection_mixed_ac_referee import (
    SCHEMA, ROOT_STATUS, K, exact_min_a,
    original_all_h_endpoint_envelope, _fixture, _gq, _project,
    _endpoints, _physical, _core, _symbol_book, _triangles,
    _actual_blocked_paths, genuine_original_GQ_AC_case, canonical_report,
)


class TestOriginalGQProjectionMixedAC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q=canonical_report()

    def test_all_h_five_exact_original_algebraic_GQ_endpoint_envelopes(self):
        z=self.q["ALL_h_genuine_original_endpoints_exact_arithmetic_envelopes"]
        self.assertEqual([v["s"] for v in z],[64,128,256,1024,65536])
        for v in z:
            s=v["s"];a=v["a"];V=v["V"];N=v["N"]
            self.assertEqual(a,exact_min_a(V))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertEqual(N,(s+1)*V)
            self.assertLessEqual(v["exact_missing_typed_endpoint_count"]+
                                 v["original_incident_typed_endpoint_count"]+
                                 v["max_original_SRGe_col_projected_endbad"],24*s**5)
            self.assertEqual(len(v["all_order_9_source_GQ_endpoint_gates"]),9)
            self.assertTrue(all(v["all_order_9_source_GQ_endpoint_gates"].values()))

    def test_six_genuine_original_nonempty_Z_true_complete_GQ_endpoint_partition(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        self.assertEqual(len(z),6)
        self.assertEqual([(x["s"],x["scheme"]) for x in z][:5],
                         [(2,"lex"),(2,"reverse-line"),(4,"lex"),
                          (4,"reverse-line"),(4,"lex")])
        for t in z:
            with self.subTest(s=t["s"],scheme=t["scheme"]):
                s=t["s"];V=(s+1)*(s*s+1);N=(s+1)*V
                v=t["original_fullGQ_endpoints"]
                self.assertGreater(t["original_deleted_named_IDs"],0)
                self.assertEqual(v["original_nonincident_q_r_projection_pairs"],
                                 V*(V-s-1))
                self.assertTrue(v["exact_original_incidence_ID_3_source_roles_s2"])
                self.assertTrue(v["exact_all_typed_ENDPOINT_census_complete"])
                self.assertEqual(
                    v["typed_missing_pair_endpoints"]+
                    v["typed_original_incident_pair_endpoints"]+
                    v["typed_original_nonZ_projection_endbad"]+
                    v["typed_deleted_AFTER_nonZ_endpoint_exclusions"]+
                    v["typed_good_GQ_projection_original_Z_avoiding_endpoints"],
                    v["typed_offcoordinate_endpoint_total"])
                self.assertEqual(v["typed_original_incident_pair_endpoints"],4*N)
                self.assertLessEqual(
                    v["typed_original_nonZ_projection_endbad"],
                    8*s*(v["true_original_collinear_f_overlap_pairs"]+
                         v["true_original_collinear_g_overlap_pairs"]))
                self.assertLessEqual(v["typed_deleted_RAW_full_GQ_projection_endpoints"],
                                     12*s*s*t["original_deleted_named_IDs"])

    def test_NEW_exact_original_Z_endpoint_overlap_rebate_identity(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        for t in z:
            v=t["original_fullGQ_endpoints"]
            self.assertTrue(v["exact_full_GQ_original_Z_mask_inclusion_exclusion"])
            self.assertEqual(v["typed_deleted_RAW_full_GQ_projection_endpoints"]+
                             v["typed_deleted_ORIGINAL_3role_overcount_credit"],
                             12*t["s"]**2*t["original_deleted_named_IDs"])
            self.assertEqual(
                v["typed_deleted_ORIGINAL_3role_overcount_credit"]%4,0)
            self.assertGreaterEqual(v["typed_deleted_RAW_full_GQ_projection_endpoints"],
                                    v["typed_deleted_AFTER_nonZ_endpoint_exclusions"])
        self.assertTrue(any(
            t["original_fullGQ_endpoints"]["typed_deleted_ORIGINAL_3role_overcount_credit"]>0
            for t in z), "require a genuinely overlapping adversarial ORIGINAL Z")

    def test_point_and_line_original_FULL_allowed_A_vs_paired_C_mixed_exact_degree_Theta(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        for t in z:
            self.assertGreaterEqual(t["original_full_A_IDs"],t["original_paired_C_IDs"])
            self.assertGreater(t["original_paired_C_IDs"],0)
            self.assertEqual(t["original_CORE_real_physical_edges"],
                             2*t["original_paired_C_IDs"])
            self.assertLessEqual(t["original_core_actual_Delta"],
                                 t["diagnostic_T"]*t["s"])
            x=t["independent_FULL_A_CORE_C_mixed_point_book"]
            y=t["independent_FULL_A_CORE_C_mixed_line_book"]
            self.assertEqual(x["Theta"],x["Theta_source_expansion"])
            self.assertEqual(y["Theta"],y["Theta_source_expansion"])
            self.assertEqual(x["Theta"],y["Theta"])
            for v in (x,y):
                self.assertLessEqual(v["Theta"],
                                     v["sum_4A_core_physical_degree_bound"])
                self.assertLessEqual(v["B"]**2,v["F1"]*v["F2"])
                self.assertLessEqual(v["F1"],2*v["G"])
                self.assertLessEqual(v["F2"],
                    2*(t["s"]+1)*(t["full_original_K_conflict_cap"]+1)*v["Theta"])

    def test_original_point_line_books_NOT_asserted_equal_for_correlated_labels(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        self.assertTrue(any(
            t["independent_FULL_A_CORE_C_mixed_point_book"]["G"] !=
            t["independent_FULL_A_CORE_C_mixed_line_book"]["G"] or
            t["independent_FULL_A_CORE_C_mixed_point_book"]["B"] !=
            t["independent_FULL_A_CORE_C_mixed_line_book"]["B"]
            for t in z), "need a genuine original correlated source non-dual asymmetric example")

    def test_independent_original_source_first_inner_triple_to_book_injections(self):
        for t in self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]:
            for k,book in (
                ("point_first_inner_source_triples",
                 "independent_FULL_A_CORE_C_mixed_point_book"),
                ("line_first_inner_source_triples",
                 "independent_FULL_A_CORE_C_mixed_line_book"),
            ):
                x=t[k]
                self.assertTrue(x["source_witness_injective"])
                self.assertLessEqual(x["T"],t[book]["B"])
                self.assertLessEqual(x["completion"]**2,x["T"]*x["sumsq"])
                self.assertLessEqual(x["completion"]**2,
                                     x["B"]*t["original_core_actual_Delta"]*x["tr4"])
                self.assertGreaterEqual(x["tr4"],0)

    def test_four_actual_original_physical_P3_blockers_do_not_exceed_source_books(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        total=0
        for t in z:
            x=t["four_original_physical_actual_proper_P3_blockers"]
            tx=t["point_first_inner_source_triples"]
            ty=t["line_first_inner_source_triples"]
            for key,b in (("x1",tx),("x2",tx),("y1",ty),("y2",ty)):
                self.assertLessEqual(x[key],b["completion"])
                self.assertLessEqual(x[key]**2,b["B"]*t["original_core_actual_Delta"]*b["tr4"])
                total+=x[key]
            self.assertLessEqual(x["blocked_any"],
                                 sum(x[k] for k in ("x1","x2","y1","y2")))
            self.assertLessEqual(x["endpoint_good"],x["proper"])
        self.assertGreater(total,0,"require non-vacuous true blocked original GQ paths")

    def test_mixed_book_full_allowed_A_is_not_wrongly_shrunk_to_paired_C(self):
        z=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        self.assertTrue(all(t["original_full_A_IDs"]>=t["original_paired_C_IDs"] for t in z))
        self.assertTrue(any(t["original_full_A_IDs"]>t["original_paired_C_IDs"] for t in z))
        self.assertTrue(any(
            t["independent_FULL_A_CORE_C_mixed_point_book"]["Theta"]>0 and
            t["independent_FULL_A_CORE_C_mixed_line_book"]["Theta"]>0
            for t in z))
        self.assertTrue(any(
            t["original_full_A_IDs"]-t["original_paired_C_IDs"]>=10
            for t in z))

    def test_exact_full_original_GQ_projection_nonincidence_uniqueness(self):
        c=_fixture(1,"lex",0,0,(0,),4,K)
        g=_gq(c)
        bypoint=0
        for q in range(c["V"]):
            for r in range(c["V"]):
                p=_project(c,g,q,r)
                if (q,r) in g["id_of"]:
                    self.assertIsNone(p)
                else:
                    self.assertIsNotNone(p)
                    self.assertEqual(len(p[2]),3)
                    self.assertEqual(len(set(p[2])),3)
                    bypoint+=1
        self.assertEqual(bypoint,c["V"]*(c["V"]-c["s"]-1))

    def test_all_h_24s5_endpoints_are_only_asserted_for_s_ge64_not_finite_s2(self):
        rows=self.q["genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles"]
        self.assertTrue(all(q["s"] in (2,4) for q in rows))
        self.assertEqual(self.q["ALL_h_genuine_original_endpoints_exact_arithmetic_envelopes"][0]["s"],64)
        with self.assertRaises(ValueError):
            original_all_h_endpoint_envelope(4)
        with self.assertRaises(ValueError):
            original_all_h_endpoint_envelope(96)

    def test_invalid_original_IDs_diagnostic_threshold_and_fake_source_fail(self):
        with self.assertRaises(ValueError):
            genuine_original_GQ_AC_case(3,"lex",(0,))
        with self.assertRaises(ValueError):
            genuine_original_GQ_AC_case(1,"lex",(0,0))
        with self.assertRaises(ValueError):
            genuine_original_GQ_AC_case(1,"lex",(99,))
        with self.assertRaises(ValueError):
            genuine_original_GQ_AC_case(1,"lex",(0,),threshold=0)
        with self.assertRaises(ValueError):
            genuine_original_GQ_AC_case(1,"lex",(0,),K0=-1)
        with self.assertRaises(ValueError):
            exact_min_a(0)

    def test_governance_explicitly_stops_without_false_root_proof_claim(self):
        z=self.q
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["root_230_status"],ROOT_STATUS)
        self.assertFalse(z["root_Branch_A_independently_accepted"])
        self.assertFalse(z["root_new_ASET_exponent"])
        self.assertFalse(z["root_external_graph_SS6_numeric_constants_known"])
        self.assertTrue(z["root_objective_original_seven_motif_S_s_not_R3"])
        self.assertTrue(z["new_exact_adversarial_original_Z_projection_overlap_rebate_identity"])
        self.assertTrue(z["prior_original_geometric_lemmas_need_full_independent_acceptance"])


if __name__=="__main__":
    unittest.main()
