"""AA4-LOWSPEC independent all-h source and physical 3-return red-team tests."""
from collections import Counter
from fractions import Fraction
import unittest

from hyp105_original_low_spectral_rho16 import (
    R, K, ROOT_STATUS, exact_low_source_ledger,
    _original_case, _gq_geometry, _collinear_symbol_pairs, _endpoint_referee,
    _physical_source, _full_conflicts, _true_low_core, _physical_powers,
    _true_source_returns, _walk_coordinate_referee, _projection,
    _actual_produced_bbo, genuine_original_finite_case, canonical_report,
)


class TestOriginalLowSpectralRho16(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=canonical_report()

    def test_all_order_sharp_root_constant_three_FORMAL_rational_probes(self):
        samples=(
            (Fraction(1),Fraction(1),810),
            (Fraction(2),Fraction(1,5),840),
            (Fraction(7,3),Fraction(1,17),847),
        )
        for C,c,h in samples:
            with self.subTest(C=C,c=c):
                x=exact_low_source_ledger(C,c)
                self.assertTrue(all(x["checks"].values()))
                self.assertEqual(x["h0"],h)
                self.assertEqual(x["T"],__import__(
                    "hyp105_original_heavy_no_clone_sharp_ss6",
                    fromlist=["allh_sharp_heavy_ledger"]
                ).allh_sharp_heavy_ledger(C,c)["T"])
                self.assertEqual(x["LOW_BBo_min_sextic"],"23/48")
                self.assertEqual(x["W3_min_sextic"],"16/3")
                self.assertEqual(x["source_core_fraction_exact"],
                                 str(Fraction(51,64)-Fraction(x["rho"])))
                self.assertEqual(Fraction(x["rho"])*12*x["q3"]**2*x["L6"],16)
                self.assertEqual(Fraction(x["delta"]),c/R**6)
                self.assertLess(x["s0"],1<<h)
                self.assertGreater(x["s0"],1<<(h-1))
                self.assertGreater(Fraction(x["source_rho_improvement_factor"]),30)

    def test_source_spectral_coordinate_gap3_is_not_gap2_local_shortcut(self):
        # This simple actual-vertex *abstract* P4 (not a synthetic GQ host)
        # has x0==x3 but x0!=x2 and x1!=x3, so gap-3 source
        # wrongness CANNOT be explained by gap-2 patterns on that path.
        path=((0,0),(1,1),(2,2),(0,3))
        self.assertEqual(path[0][0],path[-1][0])
        self.assertNotEqual(path[0][0],path[2][0])
        self.assertNotEqual(path[1][0],path[3][0])
        graph={p:set() for p in path}
        for u,v in zip(path,path[1:]):
            graph[u].add(v);graph[v].add(u)
        A2,A3=_physical_powers(graph)
        Delta=max(map(len,graph.values()))
        for x in (0,1,2):
            S=[v for v in graph if v[0]==x]
            q2=sum(A2[u].get(v,0) for u in S for v in S)
            q3=sum(A3[u].get(v,0) for u in S for v in S)
            self.assertGreaterEqual(Delta*q2,q3)
        self.assertGreater(A3[path[0]].get(path[-1],0),0)

    def test_genuine_all_original_W32_W34_point_line_projection_unique_s2(self):
        for h,scheme,shf,shg in (
            (1,"lex",0,0),(1,"reverse-line",2,4),
            (2,"lex",0,0),(2,"reverse-line",11,23),
            (2,"lex",7,19),
        ):
            with self.subTest(h=h,scheme=scheme,shf=shf,shg=shg):
                c=_original_case(h,scheme,shf,shg)
                g=_gq_geometry(c)
                z=_endpoint_referee(c,g,{0,3})
                self.assertTrue(all(z["checks"].values()))
                self.assertTrue(z["original_three_anchor_exposure_s2_each"])
                self.assertLessEqual(z["deleted_original_projection_endpoint_count"],
                                     12*c["s"]**2*2)
                self.assertEqual(z["incident_original_source_pair_endpoint_count"],
                                 4*len(c["flags"]))
                for q in range(c["V"]):
                    for r in range(c["V"]):
                        a=_projection(c,g,q,r)
                        self.assertEqual(a is None, r in g["byp"][q])

    def test_finite_true_original_nonZ_exception_union_independent_of_f_g(self):
        for z in self.data["genuine_original_source_cases"]:
            ep=z["original_ENDPOINT"]
            self.assertTrue(all(ep["checks"].values()))
            self.assertLessEqual(ep["endbad_original_projected_pair_endpoint_count"],
                8*z["s"]*(ep["true_original_point_collision_pairs"]+
                          ep["true_original_line_collision_pairs"]))
            self.assertEqual(
                ep["total_typed_offcoordinate_endpoint_pairs"],
                sum(ep[k] for k in (
                    "missing_original_factor_pair_endpoint_count",
                    "incident_original_source_pair_endpoint_count",
                    "endbad_original_projected_pair_endpoint_count",
                    "deleted_original_projection_endpoint_count",
                    "admissible_original_projection_endpoint_count"))
            )

    def test_independent_real_original_Qx_Qy_equals_A2_return_masses(self):
        for z in self.data["genuine_original_source_cases"]:
            v=z["actual_ORIGINAL_source_spectral_3walk"]
            self.assertEqual(v["source_Qx"],v["physical_A2_coordinate_returns_x"])
            self.assertEqual(v["source_Qy"],v["physical_A2_coordinate_returns_y"])
            self.assertTrue(all(v["checks"].values()))
            self.assertEqual(v["real_core_two_diagonal_edges"],
                             2*z["original_low_paired_core_flags"])
            self.assertGreaterEqual(v["physical_vertices_including_isolates"],
                                    z["s"]**2)

    def test_REAL_PHYSICAL_gap3_spectral_Acubed_bound_and_total_bad_3Delta_Q(self):
        nonzero=0
        for z in self.data["genuine_original_source_cases"]:
            with self.subTest(s=z["s"],scheme=z["scheme"],
                              shf=z["fixed_complete_f_shift"],
                              shg=z["fixed_complete_g_shift"]):
                t=z["actual_ORIGINAL_source_spectral_3walk"]
                D=t["physical_max_degree"]
                Q=t["source_Qx"]+t["source_Qy"]
                self.assertLessEqual(t["physical_A3_coordinate_gap3_x"],
                                     D*t["source_Qx"])
                self.assertLessEqual(t["physical_A3_coordinate_gap3_y"],
                                     D*t["source_Qy"])
                self.assertLessEqual(t["actual_bad_gap3"],
                                     t["physical_A3_coordinate_gap3_x"]+
                                     t["physical_A3_coordinate_gap3_y"])
                self.assertLessEqual(t["improper_threewalks"],3*D*Q)
                self.assertEqual(t["threewalks_total"],
                                 t["proper_threewalks"]+t["improper_threewalks"])
                nonzero+=t["actual_bad_gap3"]
        self.assertGreater(nonzero,0)

    def test_actual_true_original_Z_and_FULL_before_deletion_core(self):
        for z in self.data["genuine_original_source_cases"]:
            p=z["original_prune"]
            self.assertLessEqual(p["Delta"],(8 if z["s"]==2 else 5)*z["s"])
            self.assertGreater(z["original_deleted_source_IDs"],0)
            self.assertGreater(z["original_low_paired_core_flags"],0)
            self.assertGreater(z["original_flags_total"],
                               z["original_low_paired_core_flags"])
            self.assertGreaterEqual(p["original_full_conflict_edge_count"],0)

    def test_real_BBo_six_ID_physical_path_reversal_and_original_anchors_outside_CORE(self):
        good=0
        outside=0
        for z in self.data["genuine_original_source_cases"]:
            p=z["actual_original_good_BBo_sixID_projection"]
            self.assertTrue(p["exact_two_directed_reversals_per_sixset"])
            self.assertEqual(p["accepted_original_proper_directed_paths"],
                             2*p["distinct_produced_original_BBo_sixID_sets"])
            self.assertGreaterEqual(p["original_projected_anchor_outside_paired_core_paths"],0)
            good+=p["accepted_original_proper_directed_paths"]
            outside+=p["original_projected_anchor_outside_paired_core_paths"]
        self.assertGreater(good,0)
        self.assertGreater(outside,0)

    def test_ORIGINAL_BBo_source_sixsets_classify_as_historical_positive_TEST_ONLY(self):
        # Historical classifier is used ONLY in a test to check independent
        # source/physical labels. Main module is classifier-free.
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        cases=self.data["genuine_original_source_cases"]
        checked=0
        for z in cases:
            h=1 if z["s"]==2 else 2
            c=_original_case(h,z["scheme"],
                            z["fixed_complete_f_shift"],
                            z["fixed_complete_g_shift"])
            for ids in z["actual_original_good_BBo_sixID_projection"]["sample_original_sixsets"]:
                self.assertEqual(classify_seven_prechecked(
                    ids,c["f"],c["g"],c["flags"]),"B/B-overlap")
                checked+=1
        self.assertGreater(checked,0)

    def test_deletion_mask_16_units_heavy_threshold_unmodified_LOW_improved(self):
        # Relative to #739, same T/R graph theorem interface, but new
        # L6/L4/B0/RHO and improved actual source low estimate.
        from hyp105_original_heavy_no_clone_sharp_ss6 import allh_sharp_heavy_ledger
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            parent=allh_sharp_heavy_ledger(C,c)
            new=exact_low_source_ledger(C,c)
            self.assertEqual(new["T"],parent["T"])
            self.assertEqual(Fraction(new["delta"]),parent["delta"])
            self.assertLess(new["L6"],parent["L6"])
            self.assertLess(new["L4"],parent["L4_SHARP"])
            self.assertLess(new["B0"],parent["B0"])
            self.assertLess(new["h0"],parent["h0"])
            self.assertGreater(Fraction(new["rho"]),parent["rho"]*16)
            self.assertEqual(Fraction(new["LOW_BBo_min_sextic"]),Fraction(23,48))

    def test_malformed_source_or_numeric_external_bounds_fail_closed(self):
        for C,c in ((1,Fraction(1)),
                    (Fraction(1),1),
                    (Fraction(0),Fraction(1)),
                    (Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2))):
            with self.assertRaises(ValueError):exact_low_source_ledger(C,c)
        for h in (0,3,1.1,True):
            with self.assertRaises(ValueError):_original_case(h,"lex")
        with self.assertRaises(ValueError):_true_low_core(
            _original_case(1,"lex"),
            _gq_geometry(_original_case(1,"lex")),
            0,8,{0})

    def test_complete_GQ_mathematical_STOP_no_external_constants_promoted(self):
        x=self.data
        self.assertEqual(x["schema"],
                         "mathlab.hyp105.original-low-spectral-endpoint-rho16.v1")
        self.assertEqual(x["root_230_status"],ROOT_STATUS)
        self.assertTrue(x["all_order_symmetric_A3_coordinate_return_spectral_proof"])
        self.assertTrue(x["all_order_original_nonZ_endpoint_24s5_count_proof"])
        self.assertTrue(x["all_order_improved_original_LOW_BBo_23over48_conditional"])
        self.assertFalse(x["actual_external_graph_SS6_constants_numerical_values_known"])
        self.assertFalse(x["root_Branch_A_unconditionally_accepted"])
        self.assertFalse(x["root_ASET_exponent_proved"])
        self.assertEqual(len(x["formal_graph_theorem_ledger"]),3)
        self.assertEqual(len(x["genuine_original_source_cases"]),5)
        self.assertTrue(all(all(row["checks"].values())
                            for row in x["formal_graph_theorem_ledger"]))


if __name__=="__main__":
    unittest.main()
