"""Independent original all-h K-free source LOW / root minimax referee tests."""
import unittest
from fractions import Fraction
from math import comb
from hyp105_root_endtoend_kfree_optimized import (
    SCHEMA,STATUS,R_Z0,K_NEW,ERROR_ALLOC,_ceil,_ceil_sqrt,_dyadic_h,
    _energy_budget,prior_fixed_K64_Harris_budget,fixed_K_referee,
    genuine_original_source,source_model,physical_core_referee,
    genuine_case,certificate,DEPENDENCY_GATE,
)


class TestOriginalRootKFreeEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_strict_original_source_J_K_plus_one_pruning_math(self):
        for K in range(5,65):
            c=Fraction(7,8)-Fraction(5,K+1)
            self.assertGreater(c,0)
            if K==5:self.assertEqual(c,Fraction(1,24))
            if K==11:self.assertEqual(c,Fraction(11,24))
            if K==64:self.assertEqual(c,Fraction(83,104))
        self.assertLessEqual(Fraction(5,12),Fraction(7,8))

    def test_02_Blackley_Roy_real_physical_walk_core_exact(self):
        for row in self.cert["genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers"]:
            for mode in ("no_Q_K11","low_Q_K11","test_nontrivial_K3_pruning"):
                p=row[mode]
                self.assertEqual(p["original_CORE_real_edges"],
                                 2*p["original_pruned_CORE_flags"])
                self.assertGreaterEqual(p["actual_original_N"],p["original_pruned_CORE_flags"])
                self.assertTrue(p["Blakley_Roy_exact_true_actual_physical_graph_verified"])
                self.assertLessEqual(p["original_CORE_max_J_degree"],p["K"])
                self.assertLessEqual(p["original_CORE_max_physical_degree"],
                                     p["diagnostic_T_not_HEAVY_all_h"]*p["s"])

    def test_03_full_source_pencil_J_equals_independent_original_collinearity(self):
        for row in self.cert["genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers"]:
            for name in ("no_Q_K11","low_Q_K11"):
                p=row[name]
                self.assertEqual(p["original_full_J_edges"],
                    p["original_collinear_point_J_edges"]+
                    p["original_collinear_line_J_edges"])
                self.assertGreaterEqual(p["original_full_J_edges"],0)

    def test_04_true_original_W32_W34_complete_injective_and_genuine_flags(self):
        for s in (2,4):
            for scheme in ("lex","reverse","shift"):
                m=genuine_original_source(s,scheme)
                self.assertEqual(m["N"],(s+1)**2*(s*s+1))
                self.assertEqual(m["V"],(s+1)*(s*s+1))
                self.assertEqual(len(m["flags"]),len(set(m["flags"])))
                self.assertEqual(len(m["f"]),m["V"])
                self.assertEqual(len(m["g"]),m["V"])
                self.assertEqual(len(set(m["f"])),m["V"])
                self.assertEqual(len(set(m["g"])),m["V"])
                self.assertGreaterEqual(comb(m["a"],2),m["V"])

    def test_05_full_J_pruning_independent_of_actual_full_Q_mask(self):
        m=source_model(genuine_original_source(4,"lex"))
        q0=physical_core_referee(m,11,10)
        q1=physical_core_referee(m,11,1)
        self.assertEqual(q0["original_flags_removed_by_J_gt_K"],
                         q1["original_flags_removed_by_J_gt_K"])
        self.assertGreaterEqual(q1["original_flags_removed_by_FULL_Q"],0)
        self.assertGreaterEqual(q0["original_pruned_CORE_flags"],
                                q1["original_pruned_CORE_flags"])
        self.assertLessEqual(q1["original_CORE_max_physical_degree"],4)

    def test_06_small_K_3_pruning_positive_true_original_controls(self):
        rows=self.cert["genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers"]
        self.assertTrue(any(z["test_nontrivial_K3_pruning"]["original_flags_removed_by_J_gt_K"]>0 for z in rows))
        for z in rows:
            k3=z["test_nontrivial_K3_pruning"]
            self.assertLessEqual(k3["original_CORE_max_J_degree"],3)

    def test_07_K_4_or_less_not_supported_by_all_h_global_edge_bound(self):
        for K in (-2,0,1,3,4):
            with self.assertRaises(ValueError):
                _energy_budget(K,Fraction(1),Fraction(1))
        self.assertGreater(_energy_budget(5,Fraction(1),Fraction(1))
                           ["all_h_sufficient_integer_s0"],64)

    def test_08_malformed_budget_or_fake_graph_constants_fail_closed(self):
        for C0,c0 in ((Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                      (Fraction(1),Fraction(2)),(1,Fraction(1)),
                      (Fraction(1),0.2)):
            with self.assertRaises((TypeError,ValueError)):
                _energy_budget(11,C0,c0)
        for alloc in ((Fraction(1,2),Fraction(1,2),Fraction(1,2)),
                      (Fraction(0),Fraction(1,8),Fraction(1,8)),
                      (Fraction(-1),Fraction(1,8),Fraction(1,8))):
            with self.assertRaises(ValueError):
                _energy_budget(11,Fraction(1),Fraction(1),alloc)

    def test_09_original_fixed_K11_core_and_source_walk_floor(self):
        p=_energy_budget(11,Fraction(1),Fraction(1))
        self.assertEqual(p["original_low_CORE_fraction_floor"],[11,24])
        self.assertEqual(p["original_Blackley_Roy_W3_fraction_floor"],[2662,2187])
        self.assertEqual(p["true_original_FULL_J_high_degree_strictly_above_K"],12)
        self.assertEqual(p["original_HEAVY_R_zero"],93312)
        self.assertEqual(p["source_owner_selected_moment_harris_q2"],2304)
        self.assertEqual(p["source_owner_selected_moment_harris_q3"],110592)
        self.assertEqual(p["error_fractions"],
                         [[1,64],[1,64],[15,16]])
        self.assertEqual(p["at_least_original_produced_BBo_coefficient"],[1331,69984])

    def test_10_K5_pos_core_not_falsely_claimed_at_K4(self):
        p=_energy_budget(5,Fraction(1),Fraction(1))
        self.assertEqual(p["original_low_CORE_fraction_floor"],[1,24])
        self.assertEqual(p["original_Blackley_Roy_W3_fraction_floor"],[2,2187])
        self.assertGreater(Fraction(*p["at_least_original_produced_BBo_coefficient"]),
                           Fraction(*p["heavy_original_D6_delta"]))
        with self.assertRaises(ValueError):
            _energy_budget(4,Fraction(1),Fraction(1))

    def test_11_formal_three_external_constant_scenarios_match_prev_head(self):
        probes=((Fraction(1),Fraction(1),743,673),
                (Fraction(2),Fraction(1,5),773,703),
                (Fraction(7,3),Fraction(1,17),779,710))
        for C0,c0,old,new in probes:
            base=prior_fixed_K64_Harris_budget(C0,c0)
            q=_energy_budget(K_NEW,C0,c0)
            self.assertEqual(base["h0"],old)
            self.assertEqual(q["all_h_sufficient_dyadic_h0"],new)
            self.assertLess(q["all_h_sufficient_integer_s0"],base["s0"])
            self.assertGreater(base["q2"],q["source_owner_selected_moment_harris_q2"])
            self.assertGreater(base["q3"],q["source_owner_selected_moment_harris_q3"])

    def test_12_K11_is_tested_winner_but_not_claimed_global_real_C0_optimum(self):
        for q in self.cert["formal_graph_constant_probe_K_optimization"]:
            self.assertIn(11,q["winning_integer_K_in_examined_range_5_through_64"])
            self.assertGreater(q["dyadic_h0_gain_from_fixed64"],60)
            self.assertTrue(q["external_C6_constants_remain_existential"])
            self.assertFalse(q["root_PROVED_A"])
        self.assertEqual(len(self.cert["formal_graph_constant_probe_K_optimization"]),3)

    def test_13_exact_nonrounded_all_h_s0_error_thresholds_independently(self):
        for K in (5,8,11,12,64):
            p=_energy_budget(K,Fraction(1),Fraction(1))
            s0=p["all_h_sufficient_integer_s0"]
            w=Fraction(*p["original_Blackley_Roy_W3_fraction_floor"])
            alpha=[Fraction(*x) for x in p["error_fractions"]]
            T=p["original_LOW_L6"]
            self.assertGreater(s0,0)
            self.assertEqual(_dyadic_h(s0),p["all_h_sufficient_dyadic_h0"])
            self.assertGreaterEqual(s0,p["coordinate_threshold"])
            self.assertGreaterEqual(s0,p["endpoint_threshold"])
            self.assertGreaterEqual(s0,p["mixed_four_blocker_threshold"])
            self.assertEqual(w*(1-sum(alpha))/2,
                             Fraction(*p["at_least_original_produced_BBo_coefficient"]))
            self.assertGreaterEqual(Fraction(*p["at_least_original_produced_BBo_coefficient"]),
                                    Fraction(*p["heavy_original_D6_delta"]))

    def test_14_error_allocation_does_not_erase_strict_root_motif_floor(self):
        for alloc in ((Fraction(1,8),)*3,
                      (Fraction(1,16),Fraction(1,16),Fraction(3,4)),
                      (Fraction(1,32),Fraction(1,32),Fraction(7,8)),
                      ERROR_ALLOC):
            p=_energy_budget(11,Fraction(1),Fraction(1),alloc)
            self.assertLess(sum(Fraction(*x) for x in p["error_fractions"]),1)
            self.assertGreater(Fraction(*p["at_least_original_produced_BBo_coefficient"]),0)

    def test_15_actual_original_W3_direct_degree_formula_full_and_sparse(self):
        for s in (2,4):
            m=source_model(genuine_original_source(s,"reverse"))
            full=physical_core_referee(m,100,10)
            self.assertEqual(full["original_CORE_real_edges"],2*m["N"])
            self.assertEqual(full["original_pruned_CORE_flags"],m["N"])
            self.assertGreater(full["original_full_3walk_count"],0)
            empty=physical_core_referee(m,100,0)
            self.assertEqual(empty["original_pruned_CORE_flags"],0)
            self.assertEqual(empty["original_full_3walk_count"],0)

    def test_16_no_GF5_R3_B75_root_misstatement(self):
        c=self.cert
        self.assertFalse(c["closed_root_PROVED_A"])
        self.assertFalse(c["GF5_or_B75_required_for_ROOT"])
        self.assertFalse(c["general_ASET_exponent_claimed"])
        self.assertTrue(c["all_h_GQ_and_source_inverses_inherited_not_newly_accepted"])
        self.assertTrue(c["all_h_unknown_graph_constants_not_numeric"])

    def test_17_dependencies_including_sixID_inverses_are_not_marked_machine_proved(self):
        q={row["id"]:row for row in self.cert["dependency_gate"]}
        self.assertGreaterEqual(len(q),14)
        for id_ in ("GQ_SRG","HEAVY_OWNER","EXT6","C6_D6","LOW_CORE",
                    "LOW_WALK","LOW_COORD","LOW_SELECTOR","LOW_MOMENT",
                    "LOW_ENDPOINT","LOW_BLOCKERS","LOW_BBO","QUANTIFIERS"):
            self.assertIn(id_,q)
        self.assertIn("INHERITED",q["GQ_SRG"]["proof_status"])
        self.assertIn("PREDECESSOR",q["LOW_BLOCKERS"]["proof_status"])
        self.assertEqual(q["QUANTIFIERS"]["proof_status"],"NEW_ALL_ORDER_DERIVATION")
        self.assertEqual(q["LOW_CORE"]["proof_status"],"NEW_ALL_ORDER_DERIVATION")

    def test_18_source_K11_degree_witness_high_counter_exact_handshaking(self):
        for s in (2,4):
            m=source_model(genuine_original_source(s,"shift"))
            for K in (0,2,3,11):
                high=sum(len(x)>K for x in m["source_J_neighbors"])
                self.assertLessEqual(high*(K+1),2*m["source_J_edge_count"])

    def test_19_genuine_partial_heavy_Q_with_nonempty_real_paired_core(self):
        rows=self.cert["genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers"]
        self.assertTrue(any(z["actual_partial_Q_nonempty_CORE_case"] is not None
                            for z in rows))
        for z in rows:
            self.assertEqual(z["tested_exact_original_physical_T_grid_count"],11)
            q=z["actual_partial_Q_nonempty_CORE_case"]
            if q is None:
                continue
            self.assertGreater(q["genuine_FULL_Q_vertices"],0)
            self.assertGreater(q["original_pruned_CORE_flags"],0)
            self.assertLess(q["original_pruned_CORE_flags"],q["actual_original_N"])
            self.assertGreater(q["original_CORE_real_edges"],0)
            self.assertLessEqual(q["original_CORE_max_J_degree"],11)
            self.assertLessEqual(q["original_CORE_max_physical_degree"],
                                 q["diagnostic_T_not_HEAVY_all_h"]*q["s"])
            self.assertTrue(q["Blakley_Roy_exact_true_actual_physical_graph_verified"])

    def test_20_result_scope_and_number_of_true_source_cases(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],772)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["all_h_K_minimum_from_source_J_bound"],5)
        self.assertTrue(c["all_h_K11_valid_one_fixed_choice_before_maps"])
        self.assertTrue(c["standalone_all_h_conditional_root_implication_proved_in_manuscript"])
        self.assertEqual(len(c["genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers"]),5)


if __name__=="__main__":
    unittest.main()
