"""Independent genuine-original selector Jensen and SHARP fourth-moment gates."""
from fractions import Fraction
from itertools import permutations
from math import comb
import unittest

from hyp105_original_selector_sharp_fourth_referee import (
    ROOT_STATUS, ceil_graph_exact_ledger, color_probability_exact,
    exact_local_priority_floor, original_case, conflict_graph, physical_core,
    independent_proper_path_referee, sharp_fourth_moment,
    selected_physical_source, selected_c6_original_D6_injection,
    sixcycle_sixth_bound, finite_original_selector_case,
    canonical_report,
)


class TestOriginalSelectorSharpFourth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=canonical_report()

    def test_exact_independent_color_probabilities_r2_r3_exhaustive(self):
        self.assertEqual(color_probability_exact(2)["assignments"],64)
        self.assertEqual(color_probability_exact(2)["successful"],4)
        self.assertEqual(color_probability_exact(2)["exact_probability"],Fraction(1,16))
        self.assertEqual(color_probability_exact(3)["assignments"],256)
        self.assertEqual(color_probability_exact(3)["successful"],4)
        self.assertEqual(color_probability_exact(3)["exact_probability"],Fraction(1,64))

    def test_exact_local_source_priority_first_r_event_with_all_b_factorials(self):
        # Exhaustively enumerate all local priority orderings, not calling
        # the original selector or assuming independent ORIGINAL flag wins.
        for r in (2,3):
            for b in range(r,min(7,r+4)+1):
                with self.subTest(r=r,b=b):
                    successful=sum(
                        set(order[:r])==set(range(r))
                        for order in permutations(range(b)))
                    self.assertEqual(Fraction(successful, __import__("math").factorial(b)),
                                     exact_local_priority_floor(b,r))
                    self.assertEqual(exact_local_priority_floor(b,r),
                                     Fraction(1,comb(b,r)))

    def test_genuine_W32_W34_source_all_selector_Jensen_and_properness(self):
        z=self.result["genuine_original_source_selector_moment_cases"]
        self.assertEqual([(q["s"],q["scheme"]) for q in z],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        for q in z:
            for r in ("original_proper_r2","original_proper_r3"):
                value=q[r]
                self.assertTrue(value["all_check_pass"])
                sigma=Fraction(value["selector_uniform_sigma"])
                actual=Fraction(value["original_adaptive_weighted_endpoint_Frobenius2"])
                raw=value["original_proper_endpoint_Frobenius2"]
                self.assertGreaterEqual(actual,sigma*sigma*raw)
                self.assertLessEqual(actual,value["selected_energy_upper_original_trace"])
                self.assertGreater(value["proper_paths"],0)

    def test_original_SHARP_4th_partition_exact_no_loss_of_factor_two(self):
        for q in self.result["genuine_original_source_selector_moment_cases"]:
            z=q["SHARP_original_fourth"]
            self.assertTrue(all(z["checks"].values()))
            self.assertEqual(
                z["trace_A4"],z["proper_P2_norm2"]+z["improper_B2_norm2"])
            self.assertLessEqual(
                z["improper_B2_norm2"],
                z["physical_Delta"]*(z["physical_Qx"]+z["physical_Qy"]))
            self.assertEqual(z["old_double_ceiling"],2*z["sharp_fourth_ceiling"])
            self.assertGreater(z["old_double_ceiling"],z["sharp_fourth_ceiling"])
            self.assertLessEqual(z["trace_A4"],z["sharp_fourth_ceiling"])

    def test_true_original_selected_source_sixth_C6_and_Young(self):
        for q in self.result["genuine_original_source_selector_moment_cases"]:
            z=q["selected_sixth"]
            self.assertTrue(z["valid"])
            self.assertLessEqual(z["trace_A6"],z["sixth_walk_injection_bound"])
            self.assertLessEqual(z["trace_A6"],z["sixth_Young_bound"])
            self.assertEqual(z["m"],2*q["true_original_selected_source_flags"])
            self.assertTrue(q["selected_original_D6_injection"]["injective"])
            self.assertEqual(q["selected_original_D6_injection"]["unoriented_physical_c6"],
                             q["selected_original_D6_injection"]["six_distinct_original_D6_ID_sets"])

    def test_new_original_all_order_L4_halved_and_dyadic_h0_four_lower(self):
        for C,c,old_h in ((Fraction(1),Fraction(1),876),
                          (Fraction(2),Fraction(1,5),906),
                          (Fraction(7,3),Fraction(1,17),912)):
            with self.subTest(C=C,c=c):
                z=ceil_graph_exact_ledger(C,c)
                self.assertTrue(all(z["checks"].values()))
                self.assertEqual(z["sharp_L4"]*2,z["old_L4"])
                self.assertLess(z["sharp_D"],z["old_D"])
                self.assertLess(z["sharp_s0"],z["old_s0"])
                self.assertEqual(z["old_h0"],old_h)
                self.assertEqual(z["sharp_h0"],old_h-4)
                self.assertEqual(z["rho"]*12*z["q3"]**2*z["L6"],1)
                self.assertEqual(z["delta"],c/2**120)

    def test_formal_original_parent_root_ledger_agrees_before_sharpening(self):
        # Import parent prior only in TEST, never in the new main proof.
        from hyp105_original_root_proof_dag_gate import exact_conditional_ledger
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(7,3),Fraction(1,17))):
            parent=exact_conditional_ledger(C,c)
            new=ceil_graph_exact_ledger(C,c)
            for field,old_field in (
                ("T","T"),("q2","q2"),("q3","q3"),("L6","L6"),
                ("old_L4","L4"),("old_D","D"),("old_s0","s0"),
                ("old_h0","h0"),("rho","rho"),("delta","delta")
            ):
                self.assertEqual(new[field],parent[old_field],(field,C,c))

    def test_original_W34_nonempty_source_sixID_D6_seed_survives_independent_selector(self):
        # Parent D6 source inverse ONLY in separate test, NOT in main proof.
        from hyp105_original_sixid_inverse_referee import inverse_d6
        seeds=[
            ("lex",(111,116,203,224,383,412)),
            ("reverse-line",(47,224,229,273,300,355)),
        ]
        for scheme,seed in seeds:
            with self.subTest(scheme=scheme):
                c=original_case(2,scheme)
                C=tuple(range(len(c["flags"])))
                J=conflict_graph(c,C)
                cycles=inverse_d6(seed,c)
                self.assertEqual(len(cycles),1)
                cyc=cycles[0]
                left={v[0]:i%2 for i,v in enumerate(cyc)}
                right={v[1]:i%2 for i,v in enumerate(cyc)}
                left=tuple(left.get(i,i%2) for i in range(c["a"]))
                right=tuple(right.get(i,i%2) for i in range(c["a"]))
                priority=tuple(seed)+tuple(i for i in C if i not in seed)
                adj,owners,kept=selected_physical_source(
                    c,C,J,priority,left,right)
                self.assertTrue(set(seed)<=set(kept))
                d=selected_c6_original_D6_injection(c,adj,owners)
                self.assertGreaterEqual(d["unoriented_physical_c6"],1)
                self.assertIn(tuple(sorted(seed)),
                              d["independent_original_D6_source_ID_sets"])
                sixth=sixcycle_sixth_bound(adj,owners)
                self.assertTrue(sixth["valid"])

    def test_negative_original_source_mutations_and_priority_fail_closed(self):
        with self.assertRaises(ValueError):original_case(3,"lex")
        with self.assertRaises(ValueError):original_case(2,"lex",shift_f=1.2)
        c=original_case(1,"lex")
        with self.assertRaises(ValueError):conflict_graph(c,(1,1,2))
        with self.assertRaises(ValueError):conflict_graph(c,(-1,1))
        C=tuple(range(45))
        J=conflict_graph(c,C)
        with self.assertRaises(ValueError):selected_physical_source(
            c,C,J,C[:-1],tuple(0 for _ in range(c["a"])),
            tuple(0 for _ in range(c["a"])))
        with self.assertRaises(ValueError):selected_physical_source(
            c,C,J,C,tuple(2 for _ in range(c["a"])),
            tuple(0 for _ in range(c["a"])))
        for r in (1,4,1.5,True):
            with self.assertRaises(ValueError):color_probability_exact(r)
        with self.assertRaises(ValueError):ceil_graph_exact_ledger(1,Fraction(1))
        with self.assertRaises(ValueError):ceil_graph_exact_ledger(Fraction(1),Fraction(0))

    def test_report_exact_genuine_original_source_provenance_and_root_stop(self):
        z=self.result
        self.assertEqual(z["schema"],"mathlab.hyp105.original-selector-jensen-sharp4.v1")
        self.assertEqual(z["root_230_status"],ROOT_STATUS)
        self.assertTrue(z["all_order_selector_probability_and_Jensen_independent_proof"])
        self.assertTrue(z["all_order_exact_SHARP_fourth_moment_proof"])
        self.assertTrue(z["all_order_selected_bipartite_sixth_moment_rederived"])
        self.assertFalse(z["original_external_graph_SS6_numerical_constants_known"])
        self.assertFalse(z["root_Branch_A_unconditionally_accepted"])
        self.assertFalse(z["root_ASET_exponent_proved"])
        self.assertEqual(len(z["formal_graph_constant_ledgers"]),3)
        self.assertEqual(len(z["genuine_original_source_selector_moment_cases"]),4)
        self.assertEqual([v["exact_probability"] for v in z["coordinate_proper_color_probabilities"]],
                         ["1/16","1/64"])
        self.assertEqual([(q["old_h0"],q["sharp_h0"]) for q in z["formal_graph_constant_ledgers"]],
                         [(876,872),(906,902),(912,908)])


if __name__=="__main__":
    unittest.main()
