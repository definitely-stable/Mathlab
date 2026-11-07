"""AA4-RHOPARETO: independent original all-order deletion-risk source math."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_original_global_rho_pareto_referee import (
    R, K, PAL, D6_GF5, BBO_PRODUCED_GF5, BBO_GENERAL_GF5,
    ROOT_STATUS, RHO_OLD_T, MAX_T, ZERO_DELETION_BBO,
    ceil_fraction, ceil_sqrt, symbolic_external_SS6_data,
    rho_of_t, bbo_produced_floor, optimal_source_rho_frontier,
    DEPENDENCIES, proof_dependency_graph, _original_finite_case,
    canonical_report,
)


class TestOriginalGlobalRhoPareto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=canonical_report()

    def test_exact_all_h_three_formal_external_graph_constant_ledgers(self):
        cases=((Fraction(1),Fraction(1),810),
               (Fraction(2),Fraction(1,5),840),
               (Fraction(7,3),Fraction(1,17),847))
        for C,c,h in cases:
            with self.subTest(C=C,c=c):
                d=optimal_source_rho_frontier(C,c)
                self.assertEqual(d["h0"],h)
                self.assertTrue(all(d["tests"].values()))
                self.assertEqual(d["T"],ceil_fraction(Fraction(17*R**3,2)*C**3))
                self.assertEqual(d["L6"],24+153*d["T"]**2)
                self.assertEqual(d["delta"],c/Fraction(R**6))
                self.assertEqual(d["source_low_MAXIMIZED_rho_signed_R3_floor"],
                                 d["HEAVY_original_D6_signed_R3_floor"])
                self.assertGreater(d["rho_star"],d["rho_old"])

    def test_independent_exact_rho_frontier_improves_parent_740_over_50_percent(self):
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            d=optimal_source_rho_frontier(C,c)
            self.assertGreater(d["rho_star_over_rho_old"],Fraction(3,2))
            self.assertLess(d["rho_star_over_rho_old"],
                            Fraction(119**2,96**2))
            self.assertGreater(d["rho_star_over_before_sharp_LOW_PARENT"],46)
            self.assertLess(d["rho_star"],Fraction(1,32))
            self.assertLess(d["rho_star"],Fraction(3,64))
            self.assertGreaterEqual(d["source_core_fraction"],Fraction(3,4))
            self.assertGreaterEqual(d["full_Q_HEAVY_surviving_edge_fraction"],Fraction(1,16))

    def test_NEW_rho_star_is_exact_max_at_fixed_three_eighths_loss_budgets(self):
        d=optimal_source_rho_frontier(Fraction(1),Fraction(1))
        t=d["t_original_rho_new_max_risk_preserving"]
        delta=d["delta"]
        self.assertEqual(t,MAX_T-2*Fraction(D6_GF5,BBO_PRODUCED_GF5)*delta)
        self.assertEqual(rho_of_t(d,t),d["rho_star"])
        self.assertEqual(bbo_produced_floor(t),
                         Fraction(D6_GF5,BBO_PRODUCED_GF5)*delta)
        self.assertEqual(BBO_PRODUCED_GF5*bbo_produced_floor(t),
                         D6_GF5*delta)
        # At ANY slightly larger t (until max t), this particular
        # proved LOW budget no longer certifies the same HEAVY floor.
        bad=(t+MAX_T)/2
        self.assertGreater(rho_of_t(d,bad),d["rho_star"])
        self.assertLess(BBO_PRODUCED_GF5*bbo_produced_floor(bad),
                        D6_GF5*delta)
        self.assertEqual(bbo_produced_floor(MAX_T),0)
        # This rejects an invalid rho increase under the unchanged
        # risk benchmark. It does NOT refute the original conjecture.

    def test_zero_deleted_original_source_BBo_new_strong_floor(self):
        d=optimal_source_rho_frontier(Fraction(1),Fraction(1))
        self.assertEqual(ZERO_DELETION_BBO,Fraction(119,48))
        self.assertEqual(bbo_produced_floor(Fraction(0)),ZERO_DELETION_BBO)
        self.assertEqual(rho_of_t(d,Fraction(0)),0)
        self.assertEqual(bbo_produced_floor(Fraction(4)),Fraction(23,48))
        self.assertEqual(ZERO_DELETION_BBO/Fraction(23,48),Fraction(119,23))
        self.assertEqual(d["source_low_ZERO_deletion_signed_R3_floor"],
                         BBO_PRODUCED_GF5*Fraction(119,48)/PAL**6)
        self.assertLess(d["source_low_OLD_signed_R3_floor"],
                        d["source_low_ZERO_deletion_signed_R3_floor"])

    def test_monotone_continuous_deletion_and_retained_BBo_tradeoff(self):
        d=optimal_source_rho_frontier(Fraction(2),Fraction(1,5))
        seq=(Fraction(0),Fraction(1),Fraction(2),Fraction(3),
             Fraction(4),d["t_original_rho_new_max_risk_preserving"],MAX_T)
        for i in range(len(seq)-1):
            self.assertLess(seq[i],seq[i+1])
            self.assertLess(rho_of_t(d,seq[i]),rho_of_t(d,seq[i+1]))
            self.assertGreater(bbo_produced_floor(seq[i]),
                               bbo_produced_floor(seq[i+1]))
        for t in (Fraction(1),Fraction(7,3),Fraction(4),seq[-2]):
            expected=Fraction(16,3)-3*Fraction(1,8)-t
            self.assertEqual(2*bbo_produced_floor(t),expected)

    def test_external_graph_constants_are_formal_not_published_numeric(self):
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2)),(Fraction(1,2),Fraction(1))):
            with self.assertRaises(ValueError):
                symbolic_external_SS6_data(C,c)
        d=symbolic_external_SS6_data(Fraction(1),Fraction(1))
        for t in (-1,Fraction(-1,2),Fraction(5),0,4.0):
            with self.assertRaises(ValueError):
                rho_of_t(d,t)
        with self.assertRaises(ValueError):
            bbo_produced_floor(Fraction(5))
        with self.assertRaises(ValueError):
            ceil_sqrt(-1)
        with self.assertRaises(ValueError):
            ceil_fraction(1)

    def test_genuine_original_source_finite_Z_fullQ_physical_graph_and_W3(self):
        vals=self.result["actual_original_full_Q_Z_and_Blakley_Roy_finite_falsifiers"]
        self.assertEqual(len(vals),5)
        self.assertEqual([(z["s"],z["scheme"]) for z in vals][:4],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        self.assertTrue(any(z["original_paired_core_physical_edge_count"]>0
                            for z in vals))
        for v in vals:
            with self.subTest(s=v["s"],scheme=v["scheme"]):
                self.assertTrue(v["real_original_source_unique_edge_owners"])
                self.assertTrue(v["real_original_full_Q_frozen_before_Z"])
                self.assertTrue(v["real_original_3walk_degree_edge_center_identity"])
                self.assertGreater(v["original_incidence_ID_count"],0)
                self.assertGreater(v["original_deleted_ID_count"],0)
                self.assertEqual(v["original_paired_core_physical_edge_count"],
                                 2*v["original_paired_core_flag_count"])
                self.assertGreaterEqual(v["original_full_Q_touching_edges"]-
                                        v["original_full_Q_surviving_edges"],0)
                self.assertLessEqual(v["original_full_Q_touching_edges"]-
                                     v["original_full_Q_surviving_edges"],
                                     2*v["original_deleted_ID_count"])
                self.assertGreaterEqual(v["original_paired_core_uncut_W3"],
                                        Fraction(v["independent_true_graph_Blakley_Roy_lower"]))
                self.assertIn(v["physical_vertices_including_isolates"],
                              (36,196))

    def test_all_order_genuine_original_source_envelope_independent_integer_math(self):
        for h in (6,7,8,10,16):
            s=1<<h
            V=(s+1)*(s*s+1)
            N=(s+1)*V
            a=(1+__import__("math").isqrt(1+8*V))//2
            while comb(a,2)<V:a+=1
            Cs=(s*s+1)*(s*s+a-2)
            self.assertLessEqual(32*V,33*s**3)
            self.assertLessEqual(16*N,17*s**4)
            self.assertLessEqual(4*a*a,9*s**3)
            self.assertLessEqual(4*Cs,5*s**4)
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)

    def test_all_22_original_global_proof_DAG_interfaces_are_strictly_typed(self):
        d=proof_dependency_graph()
        self.assertEqual(len(d),22)
        self.assertEqual(d[-1]["gate"],"ROOT_HEAVY_LOW_R3_IMPLICATION")
        self.assertEqual(
            [z["gate"] for z in d
             if z["scientific_claim_status"]=="PUBLISHED_EXISTENTIAL_INPUT"],
            ["EXTERNAL_ORDINARY_C6_SS6"])
        complete=set()
        for z in d:
            self.assertTrue(set(z["requires"])<=complete)
            self.assertNotIn(z["gate"],complete)
            self.assertTrue(z["exact_scope"])
            complete.add(z["gate"])
        self.assertIn("LOW_MIXED_FOUR_BLOCKERS",complete)
        self.assertIn("HEAVY_REAL_NO_CLONE_CHUNK",complete)
        self.assertIn("LOW_SOURCE_PARETO_DELETION",complete)
        self.assertIn("R3_ADDITIVE_ORIGINAL_EVENT_SUM",complete)

    def test_new_global_math_symbols_match_frozen_parent_740_ONLY_IN_TEST(self):
        # The new research certifier imports NO old source root proof modules.
        from hyp105_original_low_spectral_rho16 import exact_low_source_ledger
        from hyp105_original_risk_additive_ie_rootbridge import root_symbolic_bridge
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            d=optimal_source_rho_frontier(C,c)
            old=exact_low_source_ledger(C,c)
            risk=root_symbolic_bridge(C,c)
            for name in ("T","q2","q3","L6","L4","B0","E","D","s0","h0"):
                self.assertEqual(d[name],old[name])
                self.assertEqual(d[name],risk[name])
            self.assertEqual(d["rho_old"],Fraction(old["rho"]))
            self.assertEqual(d["delta"],Fraction(old["delta"]))

    def test_invalid_true_original_source_IDs_and_h_fail_closed(self):
        with self.assertRaises(ValueError):
            _original_finite_case(3,"lex",(0,))
        with self.assertRaises(ValueError):
            _original_finite_case(1,"lex",(-1,))
        with self.assertRaises(ValueError):
            _original_finite_case(1,"lex",(45,))
        with self.assertRaises(ValueError):
            _original_finite_case(True,"lex",(0,))
        # The actual point/line incidence constructor is NOT replaced
        # by a synthetic near-regular host in any of these checks.

    def test_unique_complete_machine_report_stops_scientific_promotion(self):
        z=self.result
        self.assertEqual(z["schema"],
                         "mathlab.hyp105.original-global-rho-pareto-source-referee.v1")
        self.assertEqual(z["root_230_status"],ROOT_STATUS)
        self.assertFalse(z["final_ROOT_Branch_A_independently_accepted"])
        self.assertFalse(z["root_new_ASET_exponent_proved"])
        self.assertFalse(z["published_ordinary_C6_graph_constants_numerically_known"])
        self.assertTrue(z["all_order_original_named_Z_PARETO_parameterization_proved"])
        self.assertTrue(z["all_order_rho_STAR_strictly_improves_parent_rho_more_than_50percent"])
        self.assertTrue(z["same_preexisting_ALLH_dyadic_threshold_h0"])
        self.assertTrue(z["all_order_zero_original_Z_low_BBo_floor_119over48"])
        self.assertTrue(z["all_order_new_rho_keeps_same_HEAVY_R3_floor"])
        self.assertTrue(z["root_risk_R3_is_additive_3v3_event_probability_SUM"])
        self.assertEqual(len(z["formal_graph_constant_Pareto_gates"]),3)
        self.assertEqual([q["h0"] for q in z["formal_graph_constant_Pareto_gates"]],
                         [810,840,847])
        self.assertTrue(all(all(v["all_quantified_original_source_Pareto_gates"].values())
                            and v["LOW_weighted_R3_at_new_rho"]==
                                v["HEAVY_weighted_R3_at_new_rho"]
                            and not v["external_graph_numeric_constants_certified"]
                            for v in z["formal_graph_constant_Pareto_gates"]))


if __name__=="__main__":
    unittest.main()
