"""Independent K3-G2-L original-sixset compensation and XOR transport gates."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph,
    random_injection_expectation,
    exact_BA_overlap,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling
from hyp105_g5e2b3e1k3g2l_compensation_transport import (
    exact_original_right_swap_delta, compensation_point, report_small,
    report,
)


class K3G2LExactCompensationTests(unittest.TestCase):
    def test_full_true_original_seven_family_decomposition(self):
        lex=gq_pair_model(1,"lex")
        for model in (lex,swapped_labeling(lex,"right",2,11),
                      swapped_labeling(lex,"left",1,14)):
            with self.subTest(scheme=model["scheme"]):
                row=compensation_point(model)
                mu=Fraction(*row["mu_BA"])
                deficit=Fraction(*row["signed_deficit_D_mu_minus_BA"])
                other=row["S_other_six"]
                self.assertEqual(mu-row["U_BA"],deficit)
                self.assertEqual(
                    sum(row["other_six_family_counts"].values()),other)
                self.assertEqual(row["S"],row["U_BA"]+other)
                self.assertEqual(
                    other-deficit,
                    Fraction(*row["signed_total_surplus_S_minus_mu"]))
                self.assertEqual(row["S"]-mu,other-deficit)
                self.assertEqual(
                    row["negative_residual_without_J"],row["S"]<mu)
                expected=random_injection_expectation(
                    source_weighted_BA_hypergraph(model),
                    a=6,original_vertices=15)
                self.assertEqual(mu,expected)

    def test_XOR_original_sixsource_swaps_and_independent_B0(self):
        lex=gq_pair_model(1,"lex")
        weights=source_weighted_BA_hypergraph(lex)
        for i,j in ((0,14),(1,8),(2,11),(4,9)):
            with self.subTest(i=i,j=j):
                result=exact_original_right_swap_delta(weights,lex,i,j)
                after=swapped_labeling(lex,"right",i,j)
                self.assertEqual(
                    result["signed_delta"],
                    exact_BA_overlap(weights,after["right_labels"])-
                    exact_BA_overlap(weights,lex["right_labels"]))
                self.assertEqual(
                    result["BA_after"],
                    seven_census(after,independent_checks=False)[
                        "seven_class_motif_counts"]["B-left/A-right"])
                self.assertGreater(
                    result["affected_exactly_one_source_sixsets"],0)
                self.assertLessEqual(result["weight_affected_exactly_one"],
                                     sum(weights.values()))

    def test_exact_small_ledger_and_algebraic_beta_gate(self):
        result=report_small()
        self.assertEqual(result["model_count"],11)
        self.assertFalse(result["complete_210_single_swap_shell"])
        self.assertFalse(result["four_constructed_K_maps"])
        self.assertFalse(result["entire_W32_label_space_enumerated"])
        self.assertFalse(result["all_h_true_compensation_inequality_proved"])
        self.assertEqual(result["branch_A_B"],"OPEN")
        for name,row in result["witnesses"].items():
            with self.subTest(name=name):
                mu=Fraction(*row["mu_BA"])
                S=row["S"]
                J=row["Jcross"]
                for beta in (Fraction(0),Fraction(1,5),Fraction(1),Fraction(7)):
                    self.assertEqual(
                        Fraction(*row["signed_deficit_D_mu_minus_BA"]) <=
                        row["S_other_six"]+beta*J,
                        S+beta*J>=mu)
                if J:
                    self.assertEqual(
                        Fraction(*row["necessary_beta_nonnegative_if_J_positive"]),
                        max(Fraction(0),(mu-S)/J))

    def test_constructed_K_high_low_extremes_and_guardrails(self):
        rows=report(shell_limit=0,include_constructed=True)
        self.assertEqual(rows["model_count"],13)
        self.assertEqual(rows["witnesses"]["CE:lex:maximize"]["U_BA"],131)
        self.assertEqual(rows["witnesses"]["CE:lex:minimize"]["U_BA"],33)
        self.assertEqual(
            rows["witnesses"]["CE:correlated-left:maximize"]["U_BA"],120)
        self.assertEqual(
            rows["witnesses"]["CE:correlated-left:minimize"]["U_BA"],40)
        self.assertEqual(rows["witnesses"]["CE:lex:maximize"]["S"],320)
        self.assertEqual(rows["witnesses"]["CE:lex:minimize"]["S"],101)
        self.assertEqual(len(rows["ordered_full_original_ledger_sha256"]),64)
        self.assertTrue(rows["finite_beta_possible_for_all_tested_maps"] or
                        rows["tested_zero_J_S_below_mu_impossible_maps"])
        for kw in ({"shell_limit":-1},{"shell_limit":106},
                   {"shell_limit":True},{"include_constructed":1}):
            with self.assertRaises(ValueError):
                report(**kw)
        w=source_weighted_BA_hypergraph(gq_pair_model(1,"lex"))
        for i,j in ((0,0),(-1,1),(3,15),(True,4)):
            with self.assertRaises(ValueError):
                exact_original_right_swap_delta(w,gq_pair_model(1,"lex"),i,j)


if __name__=="__main__":
    unittest.main()
