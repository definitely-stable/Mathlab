"""Independent all-order local and exact FULL global experiment 3-path tests."""
import unittest
from fractions import Fraction as Q

from hyp105_selector_moment_joint_publication import (
    SCHEMA,STATUS,PARENT_PR,certificate,selected_case,chosen_core,
    source_J,priority_masks,global_two_cut_masks,product_selector_distribution,
    conflict,selected_original_graph,proper_matrix,traces,simple_C6,
    integer_root_formal,
)


class TestOriginalSelectorMomentJoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_exact_real_original_W32_W34_global_source(self):
        cases=self.c["genuine_original_selected_GQ_cases"]
        self.assertEqual(len(cases),6)
        self.assertEqual({(z["s"],z["scheme"]) for z in cases},
                         {(s,m) for s in (2,4) for m in
                          ("lex","reverse","correlated")})

    def test_02_nonvacuous_proper_3walk_and_source_conflict(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertEqual(z["source_CORE_flag_count"],4)
            self.assertGreater(z["true_original_SOURCE_J_edges"],0)
            self.assertGreater(z["physical_proper_paths"][3]["paths"],0)
            self.assertGreater(z["physical_proper_paths"][2]["paths"],0)

    def test_03_ONE_priority_global_experiment_exact_denominator(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertEqual(z["priority_outcomes"],24)
            self.assertGreaterEqual(z["global_selected_subset_count"],2)
            self.assertGreater(Q(z["source_W_C"]),0)

    def test_04_two_physical_coordinate_cuts_one_global_assignment(self):
        for s in (2,4):
            m,owners,_=chosen_core(s,"lex")
            J=source_J(m,owners)
            dist,priorities,cuts,nx,ny=product_selector_distribution(m,owners,J)
            self.assertEqual(sum(priorities.values()),24)
            self.assertEqual(sum(dist.values()),Q(1))
            self.assertEqual(sum(cuts.values()),2**(nx+ny))
            self.assertGreaterEqual(nx,2)
            self.assertGreaterEqual(ny,2)
            self.assertLessEqual(nx+ny,16)

    def test_05_TRUE_original_conflict_only_real_source_flags(self):
        for s in (2,4):
            m,owners,w=chosen_core(s,"reverse")
            J=source_J(m,owners)
            self.assertGreater(sum(map(len,J)),0)
            for i in range(len(owners)):
                for j in range(i+1,len(owners)):
                    self.assertEqual(j in J[i],conflict(m,owners[i],owners[j]))
                    self.assertEqual(i in J[j],j in J[i])

    def test_06_expected_selected_original_edge_mass_exact_W_over_2(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            W=Q(z["source_W_C"])
            self.assertEqual(Q(z["expected_selected_edges"]),W/2)
            self.assertEqual(Q(z["expected_selected_trace2"]),W)
            self.assertGreater(W,0)
            self.assertLessEqual(W,4)

    def test_07_independent_expected_sixth_moment_with_true_CORE_delta(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertLessEqual(Q(z["expected_selected_trace6"]),
                                 Q(z["EXPECTED_sixwalk_source_bound"]))
            self.assertTrue(z["selected_graph_C6_every_outcome_zero"])
            self.assertEqual(z["source_six_cycle_D6"],0)

    def test_08_expected_fourth_moment_ONE_global_Cauchy(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertEqual(Q(z["expected_fourth_Cauchy_squared"]),
                             Q(z["expected_selected_trace4"])**2)
            self.assertEqual(Q(z["expected_fourth_Cauchy_upper"]),
                             Q(z["expected_selected_trace2"])*
                             Q(z["expected_selected_trace6"]))
            self.assertLessEqual(Q(z["expected_fourth_Cauchy_squared"]),
                                 Q(z["expected_fourth_Cauchy_upper"]))

    def test_09_original_true_CORE_paired_fourth_trace_supports(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertEqual(z["original_CORE_trace4"],
                             z["core_proper2_Gram"]+
                             z["core_improper2_Gram"])
            self.assertGreater(z["core_proper2_Gram"],0)

    def test_10_original_exact_global_source_J_coordinate_returns(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            self.assertEqual(
                z["original_coordinate_return_Qx"]+
                z["original_coordinate_return_Qy"],
                8*z["source_CORE_flag_count"]+
                4*z["true_original_SOURCE_J_edges"])

    def test_11_proper_r2_same_global_selector_Jensen(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            p=z["physical_proper_paths"][2]
            self.assertGreaterEqual(Q(p["EXPECTED_path_Gram"]),
                                    Q(p["lower_uniform_q_energy"]))
            self.assertLessEqual(Q(p["EXPECTED_path_Gram"]),
                                 Q(p["EXPECTED_selected_proper_energy"]))
            self.assertLessEqual(Q(p["EXPECTED_selected_proper_energy"]),
                                 Q(z["expected_selected_trace4"]))

    def test_12_proper_r3_same_global_selector_Jensen(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            p=z["physical_proper_paths"][3]
            self.assertGreaterEqual(Q(p["EXPECTED_path_Gram"]),
                                    Q(p["lower_uniform_q_energy"]))
            self.assertLessEqual(Q(p["EXPECTED_path_Gram"]),
                                 Q(p["EXPECTED_selected_proper_energy"]))
            self.assertLessEqual(Q(p["EXPECTED_selected_proper_energy"]),
                                 Q(z["expected_selected_trace6"]))

    def test_13_NEW_degree_weighted_original_proper_2path(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            p=z["physical_proper_paths"][2]
            self.assertLessEqual(Q(p["weighted_Gram"]),
                                 16**2*Q(z["expected_selected_trace4"]))
            self.assertGreater(Q(p["weighted_Gram"]),0)

    def test_14_NEW_degree_weighted_original_proper_3path(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            p=z["physical_proper_paths"][3]
            self.assertLessEqual(Q(p["weighted_Gram"]),
                                 16**3*Q(z["expected_selected_trace6"]))
            self.assertGreater(Q(p["weighted_Gram"]),0)

    def test_15_actual_source_K_not_confused_with_ROOT_K(self):
        for z in self.c["genuine_original_selected_GQ_cases"]:
            Kc=z["source_J_max_degree"]
            self.assertGreater(Kc,0)
            self.assertLess(Kc,10)
            for r in (2,3):
                self.assertEqual(z["physical_proper_paths"][r]["q_actual"],
                                 4**r*(Kc+1)**r)

    def test_16_direct_physical_complete_zero_and_full_masks(self):
        m,owners,_=chosen_core(2,"lex")
        a,e=selected_original_graph(m,owners,0)
        self.assertFalse(a)
        self.assertFalse(e)
        self.assertEqual(traces(a,e),(0,0,0))
        self.assertEqual(simple_C6(a),0)
        a,e=selected_original_graph(m,owners,15)
        self.assertEqual(len(e),8)
        self.assertGreater(traces(a,e)[2],0)

    def test_17_fully_global_probability_product_no_path_resampling(self):
        m,owners,_=chosen_core(2,"correlated")
        J=source_J(m,owners)
        pcounts=priority_masks(J)
        cnt,nx,ny=global_two_cut_masks(m,owners)
        d,_,_,_,_=product_selector_distribution(m,owners,J)
        self.assertEqual(sum(pcounts.values()),24)
        self.assertEqual(sum(cnt.values()),2**(nx+ny))
        self.assertEqual(sum(d.values()),Q(1))
        self.assertGreater(len(pcounts),1)
        self.assertGreater(len(cnt),1)

    def test_18_root_universal_constants_from_exact_source_Harris(self):
        q=integer_root_formal()
        self.assertEqual(q["K"],10)
        self.assertEqual(q["q2"],1936)
        self.assertEqual(q["q3"],85184)
        self.assertEqual(q["proper_path_TWO_global_cut_probability_r2"],"1/16")
        self.assertEqual(q["proper_path_TWO_global_cut_probability_r3"],"1/64")
        self.assertTrue(q["old_heuristic_independent_paths_forbidden"])
        self.assertFalse(q["original_ROOT_PROVED_A"])

    def test_19_independent_all_h_proof_status_firewall(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],785)
        self.assertTrue(c["exact_global_selector_priority_and_TWO_global_typed_cuts"])
        self.assertTrue(c["independent_all_h_source_overlap_product_integral_proof"])
        self.assertTrue(c["NEW_weighted_original_path_energy_transfer"])
        self.assertTrue(c["published_ordinary_graph_C6_constants_numeric_unknown"])
        self.assertTrue(c["all_h_C6_source_original_sixID_inverse_inherited_from_772"])
        self.assertTrue(c["full_original_LOW_PRODUCED_publication_signoff_still_open"])
        self.assertFalse(c["original_ROOT_PROVED_A"])

    def test_20_bad_original_input_rejected(self):
        m,owners,_=chosen_core(2,"lex")
        with self.assertRaises(ValueError):
            proper_matrix(m["adj"],1)
        with self.assertRaises(ValueError):
            proper_matrix(m["adj"],4)


if __name__=="__main__":
    unittest.main()
