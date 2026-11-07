"""AA4-HEAVYREF independently validate genuine-original no-clone and SS6 gates."""
import unittest
from fractions import Fraction
from itertools import product, combinations
from math import comb

from hyp105_original_heavy_no_clone_sharp_ss6 import (
    ROOT_STATUS, K, R, SS6_T_FACTOR, OLD_T_FACTOR,
    genuine_envelope, allh_sharp_heavy_ledger, _actual_original,
    _physical, _conflicts, _source_caro_wei, _full_source_color_cut,
    _winner_chunk, _fresh_heavy_case, _all_c6, _original_cycle_ids,
    canonical_report, mutations,
)


class TestActualOriginalHeavyNoClone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_independent_all_s_ge_64_genuine_envelope_and_min_alphabet(self):
        for h in (6,7,8,10,14):
            with self.subTest(h=h):
                z=genuine_envelope(1<<h)
                self.assertTrue(all(z["checks"].values()))
                self.assertLess(comb(z["a"]-1,2),z["V"])
                self.assertGreaterEqual(comb(z["a"],2),z["V"])
                self.assertLessEqual(16*z["N"],17*z["s"]**4)
                self.assertLessEqual(4*z["a"]**2,9*z["s"]**3)
                self.assertLessEqual(4*z["C_s"],5*z["s"]**4)

    def test_SHARP_Caro_Wei_source_fraction_and_no_clone_density_exact(self):
        z=allh_sharp_heavy_ledger(Fraction(1),Fraction(1))
        self.assertEqual(z["selected_fraction"],Fraction(1,20608))
        self.assertEqual(z["density"],Fraction(1,370944))
        self.assertEqual(z["SS6_T_factor"],Fraction(17*R**3,2))
        self.assertEqual(z["T"],433854371818635264)
        self.assertEqual(z["old_T"],2**64)
        self.assertEqual(z["delta"],Fraction(1,R**6))
        self.assertGreater(Fraction(2**120,R**6),500)
        self.assertTrue(all(z["checks"].values()))

    def test_three_formal_external_graph_constants_sharper_h0_delta_rho(self):
        for C,c,h0 in (
            (Fraction(1),Fraction(1),818),
            (Fraction(2),Fraction(1,5),848),
            (Fraction(7,3),Fraction(1,17),854),
        ):
            with self.subTest(C=C,c=c):
                z=allh_sharp_heavy_ledger(C,c)
                self.assertEqual(z["h0"],h0)
                self.assertTrue(all(z["checks"].values()))
                self.assertEqual(12*z["rho"]*z["q3"]**2*z["L6"],1)
                self.assertEqual(z["delta"],c/R**6)
                self.assertGreater(z["risk_GF5_numerator"],0)
                self.assertLess(z["T"],z["old_T"])
                self.assertTrue(z["s0"]<=1<<z["h0"])
                self.assertTrue(z["s0"]>1<<(z["h0"]-1))

    def test_direct_original_Z_source_and_two_diagonals_preserve_ownership(self):
        for h,scheme in ((1,"lex"),(1,"reverse-line"),
                         (2,"lex"),(2,"reverse-line")):
            c=_actual_original(h,scheme)
            flags=c["flags"]
            full,owner=_physical(c,range(len(flags)))
            self.assertEqual(len(owner),2*len(flags))
            self.assertEqual(sum(map(len,full.values())),4*len(flags))
            self.assertTrue(all(0<=i<len(flags) for i in owner.values()))
            with self.assertRaises(ValueError):_physical(c,(0,0))
            with self.assertRaises(ValueError):_physical(c,(-1,))

    def test_TRUE_original_heavy_Caro_Wei_priority_potential_and_pair_cuts(self):
        for h,scheme,shiftf,shiftg in (
            (1,"lex",0,0),(1,"reverse-line",1,2),
            (2,"lex",0,0),(2,"reverse-line",7,19),
        ):
            c=_actual_original(h,scheme,shiftf,shiftg)
            subset=tuple(i for i in range(len(c["flags"])) if i%3==1)
            J=_conflicts(c,subset)
            chosen,w,pot=_source_caro_wei(J)
            self.assertGreaterEqual(len(chosen),w)
            self.assertTrue(all(a-b<=1 for a,b in zip(pot,pot[1:])))
            self.assertTrue(all(j not in J[i] for i,j in combinations(chosen,2)))
            L,lb=_full_source_color_cut(c,chosen,0)
            B,rb=_full_source_color_cut(c,L,1)
            self.assertGreaterEqual(2*len(L),len(chosen))
            self.assertGreaterEqual(2*len(B),len(L))
            self.assertTrue(all(lb[c["f"][c["flags"][i][0]][0]]!=
                                lb[c["f"][c["flags"][i][0]][1]]
                                for i in B))
            self.assertTrue(all(rb[c["g"][c["flags"][i][1]][0]]!=
                                rb[c["g"][c["flags"][i][1]][1]]
                                for i in B))

    def test_exhaustive_SMALL_simple_bipartite_no_clone_pigeonhole(self):
        # Exhaustively exercise every 3x4 simple physical bipartite graph
        # and every nonempty original R subset. This is an abstract
        # pigeonhole falsifier, not an artificial replacement for W(3,s).
        Y=set(range(3,7))
        for mask in range(1<<12):
            E={(i,j) for k,(i,j) in enumerate(product(range(3),range(3,7)))
               if mask&(1<<k)}
            for bits in range(1,8):
                Rset={u for u in range(3) if bits&(1<<u)}
                z=_winner_chunk(E,Rset,Y,7)
                self.assertTrue(z["source_no_clone"])
                self.assertTrue(z["winner_real_physical_subgraph"])
                self.assertTrue(z["cross_edge_pigeonhole_exact"])
                self.assertLessEqual(z["winner_v"],2*len(Rset))
                self.assertGreaterEqual(z["winner_m"]*14,
                                        z["E_cross"]*len(Rset))
                self.assertEqual(z["actual_winner_edges"],tuple(sorted(
                    set(z["actual_winner_edges"]))))
        with self.assertRaises(ValueError):
            _winner_chunk({(0,1)},{0},{0},2)

    def test_FIVE_actual_genuine_original_W32_W34_f_g_correlated_heavy_cases(self):
        cases=self.report["genuine_true_original_heavy_cases"]
        self.assertEqual(len(cases),5)
        self.assertEqual([(z["s"],z["scheme"]) for z in cases][:4],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        positive=0
        for z in cases:
            with self.subTest(s=z["s"],scheme=z["scheme"],
                              f=z["shift_f"],g=z["shift_g"]):
                self.assertFalse(z["root_unconditionally_accepted"])
                self.assertGreater(z["full_original_Q_before_Z"],0)
                self.assertGreater(z["deleted_original_ID_count"],0)
                self.assertGreater(z["true_original_heavy_source_owners_L"],0)
                self.assertLessEqual(z["actual_original_deleted_tail_edges"],
                                     2*z["deleted_original_ID_count"])
                self.assertGreaterEqual(z["source_original_independent_flags"],
                                        Fraction(z["source_original_Caro_Wei"]))
                self.assertGreaterEqual(
                    4*z["source_after_second_full_pair_cut"]*
                    (z["true_original_heavy_source_owners_L"]+
                     2*z["true_source_conflict_edges"]),
                    z["true_original_heavy_source_owners_L"]**2)
                self.assertGreaterEqual(2*z["source_heavy_majority_witness_count"],
                                        z["source_after_second_full_pair_cut"])
                w=z["actual_no_clone_winner"]
                self.assertTrue(w["source_no_clone"])
                self.assertEqual(w["winner_m"],w["actual_winner_edges"])
                self.assertEqual(w["winner_v"],w["actual_winner_vertices"])
                self.assertLessEqual(w["winner_v"],2*w["heavy_R"])
                self.assertGreaterEqual(
                    Fraction(z["actual_winner_m_over_v"]),
                    Fraction(z["instance_sharp_source_density_lower"]))
                self.assertGreaterEqual(
                    Fraction(z["actual_winner_e3_over_v4"]),
                    Fraction(z["instance_SS6_cubed_lower"]))
                self.assertEqual(z["actual_original_winner_D6_six_ID_count"],
                                 z["actual_original_no_clone_winner_C6"])
                positive+=z["actual_original_selected_C6"]
        self.assertGreater(positive,0)
        self.assertTrue(any(x["actual_original_no_clone_winner_C6"]>0 for x in cases))

    def test_independent_actual_ORIGINAL_heavy_matches_frozen_parent_only_in_TEST(self):
        # The main new source referee never imports the parent. A separate
        # comparison with #730 rejects accidental mismatch of true-source
        # owners, full-Q deletion, source conflict, two-cuts and no-clone.
        from hyp105_original_deletion_adaptive_heavy_tail import (
            _real_original_selector_adaptive_heavy,
        )
        for h,scheme,T,Z in (
            (1,"lex",Fraction(1,2),(0,)),
            (1,"reverse-line",Fraction(3,4),(1,13,33)),
            (2,"lex",Fraction(1),(0,10,100,200)),
            (2,"reverse-line",Fraction(5,4),(0,25,26,33,34)),
        ):
            with self.subTest(h=h,scheme=scheme):
                c=_actual_original(h,scheme)
                independent=_fresh_heavy_case(h,scheme,T,Z)
                historical=_real_original_selector_adaptive_heavy(
                    h,c["f"],c["g"],Z,T)
                self.assertEqual(independent["full_original_Q_before_Z"],
                                 historical["full_original_QT_vertices"])
                self.assertEqual(independent["actual_original_deleted_tail_edges"],
                                 historical["actual_original_heavy_edges_removed_by_Z"])
                self.assertEqual(independent["true_original_heavy_source_owners_L"],
                                 len(historical["retained_heavy_original_flag_IDs"]))
                self.assertEqual(independent["source_after_second_full_pair_cut"],
                                 historical["original_both_typed_cuts_selected_count"])
                self.assertEqual(independent["actual_original_selected_C6"],
                                 historical["actual_physical_selected_C6"])
                self.assertEqual(independent["actual_original_no_clone_winner_C6"],
                                 historical["actual_winner_uncloned_physical_C6"])

    def test_all_five_adversarial_sufficient_budget_mutations_fail_closed(self):
        m=mutations(Fraction(1),Fraction(1))
        self.assertEqual(len(m),5)
        self.assertTrue(all(z["failed_gates"] for z in m))
        self.assertEqual({z["name"] for z in m},{
            "assume_weaker_conflict_graph_cap",
            "assume_weaker_physical_vertex_alphabet",
            "assume_weaker_original_source_size",
            "reduce_below_proved_ordinary_C6_threshold",
            "increase_original_D6_multiplier_without_proof",
        })
        for C,c in ((0,Fraction(1)),(1,Fraction(0)),(Fraction(1),2),
                    (Fraction(1),Fraction(2)),(Fraction(1),Fraction(0))):
            with self.assertRaises(ValueError):
                allh_sharp_heavy_ledger(C,c)
        with self.assertRaises(ValueError):genuine_envelope(63)
        with self.assertRaises(ValueError):genuine_envelope(65)
        with self.assertRaises(ValueError):genuine_envelope(True)
        with self.assertRaises(ValueError):
            _fresh_heavy_case(1,"lex",Fraction(1,2),(45,))
        with self.assertRaises(ValueError):
            _fresh_heavy_case(1,"lex",0,(0,))

    def test_complete_machine_proof_scientific_draft_and_real_source(self):
        z=self.report
        self.assertEqual(z["schema"],"mathlab.hyp105.original-heavy-no-clone-sharp-SS6.v1")
        self.assertEqual(z["root_230_status"],ROOT_STATUS)
        self.assertFalse(z["root_Branch_A_unconditionally_accepted"])
        self.assertFalse(z["root_ASET_exponent_proved"])
        self.assertFalse(z["external_published_C_graph_c_graph_values_numerically_known"])
        self.assertEqual(z["new_R"],370944)
        self.assertEqual(z["new_SS6_T_coefficient"],"433854371818635264")
        self.assertEqual(z["old_SS6_T_coefficient"],str(2**64))
        self.assertGreater(Fraction(z["D6_sixset_lower_improvement_factor"]),500)
        self.assertTrue(z["all_order_original_Caro_Wei_cuts_no_clone_heavy_proved"])
        self.assertTrue(z["all_order_SS6_d6_conditional_improvement_proved"])
        self.assertTrue(z["all_order_original_lowtail_lemma_inherited_not_reproved"])
        self.assertEqual([q["h0_sharp_heavy_and_L4"]
                          for q in z["formal_graph_constant_ledgers"]],[818,848,854])
        self.assertTrue(all(q["all_conditional_exact_budgets"] and
                            not q["external_graph_SS6_constants_numerically_known"]
                            for q in z["formal_graph_constant_ledgers"]))
        self.assertEqual([q["s"] for q in z["actual_original_envelopes"]],
                         [64,128,256,1024])
        self.assertEqual(len(z["genuine_true_original_heavy_cases"]),5)


if __name__=="__main__":
    unittest.main()
