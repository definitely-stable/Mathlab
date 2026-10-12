"""True original C0/B0 dual-source exact two-family falsifier tests."""
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model,exact_two_family_point,source_corpus,
    correlated_twofamily_probe,_anchors,
)


class K3G2MTwoFamilyTests(unittest.TestCase):
    def test_original_GQ_dual_involution(self):
        base=gq_pair_model(1,"lex")
        for model in (base,swapped_labeling(base,"left",1,14),
                      swapped_labeling(base,"right",2,11)):
            twice=dual_model(dual_model(model))
            for k in ("s","a","incidences","left_labels","right_labels"):
                self.assertEqual(model[k],twice[k])
            self.assertEqual(model["N"],twice["N"])

    def test_exact_three_independent_original_source_oracles(self):
        base=gq_pair_model(1,"lex")
        examples=[
            (base,98,110,259,[10000,143]),
            (swapped_labeling(base,"right",2,11),None,None,None,None),
            (_anchors()[0][1],44,37,90,[10638,143]),
        ]
        left_cache={};right_cache={}
        for model,BA,AB,S,mu in examples:
            with self.subTest(scheme=model["scheme"]):
                row=exact_two_family_point(
                    model,left_cache=left_cache,right_cache=right_cache)
                self.assertEqual(row["U_BA"]+row["U_AB"],row["two_family"])
                self.assertEqual(row["S_seven"]-row["two_family"],
                                 row["five_other_family"])
                self.assertEqual(row["dual_seven_S_invariant"],True)
                self.assertEqual(row["distinct_original_left_6candidates"],62370)
                self.assertEqual(row["distinct_original_dual_left_6candidates"],62370)
                self.assertEqual(
                    Fraction(*row["two_family_minus_mu"]),
                    row["U_BA"]+row["U_AB"]-Fraction(*row["mu_BA"]))
                self.assertEqual(
                    Fraction(*row["all_seven_minus_mu"]),
                    row["S_seven"]-Fraction(*row["mu_BA"]))
                if BA is not None:
                    self.assertEqual((row["U_BA"],row["U_AB"],row["S_seven"]),
                                     (BA,AB,S))
                    self.assertEqual(row["mu_BA"],mu)
                self.assertGreater(row["strict_positive_GF5_lower_numerator"],0)
                self.assertFalse(row["no_all_h_positive_claim"] is False)

    def test_complete_small_source_corpus_exact(self):
        r=source_corpus(shell_limit=0,include_constructed=False)
        self.assertEqual(r["named_exact_original_source_maps"],9)
        self.assertFalse(r["complete_single_swap_shell"])
        self.assertFalse(r["constructed_high_low_four"])
        self.assertTrue(len(r["full_source_corpus_sha256"])==64)
        self.assertFalse(r["universal_all_h_two_family_claim"])
        self.assertFalse(r["universal_all_h_full_S_claim"])
        self.assertFalse(r["entire_W32_pair_map_space_exhausted"])
        self.assertEqual(r["selected_full_true_source_ledger"]["corr:5"][
            "U_BA"],44)
        self.assertEqual(r["selected_full_true_source_ledger"]["corr:5"][
            "U_AB"],37)

    def test_adversarial_replay_small_deterministic(self):
        kw={"steps":1,"proposals_per_step":2,
            "anchor_limit":1,"seed":20261012}
        a=correlated_twofamily_probe(**kw)
        b=correlated_twofamily_probe(**kw)
        self.assertEqual(a,b)
        self.assertEqual(a["anchors_tested"],1)
        self.assertEqual(a["candidate_moves_precisely_delta_scored"],2)
        self.assertEqual(a["complete_original_B0_C0_dual_replays"],2)
        self.assertFalse(a["all_h_branch_A_B_proved"])
        self.assertFalse(a["whole_W32_map_space_exhausted"])
        for record in a["result"][0]["selected_path"]:
            self.assertTrue(len(record["physical_global_labels_sha256"])==64)
            if record["finite_two_family_counterexample"]:
                self.assertLess(Fraction(*record["two_family_minus_mu"]),0)

    def test_fail_closed_search_budget_and_model(self):
        for bad in ({"steps":0},{"steps":9},{"steps":True},
                    {"proposals_per_step":0},
                    {"proposals_per_step":106},
                    {"proposals_per_step":True},
                    {"anchor_limit":0},{"anchor_limit":4},
                    {"anchor_limit":True},{"seed":True}):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                correlated_twofamily_probe(**bad)
        for bad in ({"shell_limit":-1},{"shell_limit":106},
                    {"shell_limit":True},{"include_constructed":1}):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                source_corpus(**bad)


if __name__=="__main__":
    unittest.main()
