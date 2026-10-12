"""Independent finite quantitative S lower and complete-source adaptive Hall tests."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS
)
from hyp105_g5e2b3e1k3g2g_global_adaptive import (
    adaptive_complete_cross_probe,_source_supports
)
from hyp105_g5e2b3e1k3g2f_w34_seeded_targets import generic_seven_family
from hyp105_g5e2b3e1k3g2d_charging_hall import cross_witnesses


class K3G2GAdaptiveQuantitativeTests(unittest.TestCase):
    def test_w32_full_source_coverage_and_true_B0_lower(self):
        for scheme in ("lex","reverse-line"):
            model=gq_pair_model(1,scheme)
            cert=adaptive_complete_cross_probe(
                model,max_nodes_per_seed=12000,max_targets_per_seed=12,
                first_pass_seed_count=1,max_seeds_per_unmatched=4)
            exact=seven_census(model,witness_sets=True,
                              independent_checks=False)
            self.assertEqual(cert["source_witnesses_considered"],
                             cert["global_Jcross_exact"])
            self.assertEqual(cert["unmatched_after_recovery"],0)
            self.assertTrue(cert["full_finite_Jcross_charge_into_true_S_proved"])
            self.assertTrue(cert[
                "unit_capacity_S_charge_for_considered_witnesses_proved"])
            self.assertLessEqual(cert["positive_seven_S_lower"],
                                 exact["S_seven"])
            self.assertLessEqual(cert[
                "positive_risk_numerator_lower_51_pow_6"],
                exact["GF5_seven_lower_numerator"])
            self.assertLessEqual(cert["global_Jcross_exact"],exact["S_seven"])
            self.assertEqual(cert["positive_risk_denominator"],51**6)
            self.assertEqual(len(cert["actual_constructed_assignment_sha256"]),64)
            for left,ids,tag in cert["actual_assignment_samples"]:
                self.assertEqual(generic_seven_family(model,ids),tag)
                self.assertIn(ids,exact["sets"])
                self.assertEqual(exact["sets"][ids],tag)

    def test_w34_sample_positive_lower_only_and_model_coherence(self):
        for scheme,seed in (("lex",None),("random",20261012)):
            model=gq_pair_model(2,scheme,seed)
            cert=adaptive_complete_cross_probe(
                model,sample_limit=12,max_nodes_per_seed=8000,
                max_targets_per_seed=8,max_seeds_per_unmatched=3)
            self.assertEqual(cert["source_witnesses_considered"],12)
            self.assertEqual(cert["source_sample_limit"],12)
            self.assertEqual(cert["global_Jcross_exact"],
                             len(cross_witnesses(model)))
            self.assertLessEqual(
                cert["matched_after_adaptive_recovery"],12)
            self.assertGreaterEqual(
                cert["matched_after_adaptive_recovery"],
                cert["matched_after_first_pass"])
            self.assertEqual(
                cert["unmatched_after_recovery"]+
                cert["matched_after_adaptive_recovery"],12)
            self.assertFalse(cert["full_finite_Jcross_charge_into_true_S_proved"])
            self.assertFalse(cert["all_h_Jcross_leq_S_proved"])
            self.assertFalse(cert["all_h_S_omega_s6_proved"])
            self.assertFalse(cert["failure_when_budgeted_unmatched_proved"])
            self.assertGreaterEqual(
                cert["positive_seven_S_lower"],
                cert["matched_after_adaptive_recovery"])
            self.assertEqual(
                cert["positive_risk_numerator_lower_51_pow_6"],
                sum(n*R3_CERTIFIED_FLOORS[tag] for tag,n
                    in cert["positive_seven_family_counts"].items()))
            self.assertGreaterEqual(cert["reused_seed_pair_results"],0)
            for _,ids,tag in cert["actual_assignment_samples"]:
                self.assertEqual(generic_seven_family(model,ids),tag)
                self.assertGreater(R3_CERTIFIED_FLOORS[tag],0)

    def test_full_w34_exact_hosted_injections_are_pinned(self):
        # All 128 lex and 75 random ORIGINAL cross-source witnesses are
        # assigned to DISTINCT actual accepted positive seven-family
        # six-column motifs with >=2 original columns in common.
        # This is a FINITE two-map certificate, not an all-h theorem.
        pinned=(
            ("lex",None,128,374,16504153,
             "e6b46c5a5c055c6100a39a7fba7096f16281fb5872d53437678b9987ab071b20"),
            ("random",20261012,75,203,8814887,
             "a00702adc2c12c67ee6885c27e3662f4ad5c2415677033e8f4cecae6889b801c"),
        )
        for scheme,seed,J,targets,risk,digest in pinned:
            m=gq_pair_model(2,scheme,seed)
            result=adaptive_complete_cross_probe(
                m,first_pass_seed_count=1,
                max_seeds_per_unmatched=10,
                max_nodes_per_seed=30000,max_targets_per_seed=12)
            self.assertEqual(result["global_Jcross_exact"],J)
            self.assertEqual(result["source_witnesses_considered"],J)
            self.assertEqual(result["matched_after_adaptive_recovery"],J)
            self.assertEqual(result["unmatched_after_recovery"],0)
            self.assertEqual(result["positive_seven_S_lower"],targets)
            self.assertEqual(result[
                "positive_risk_numerator_lower_51_pow_6"],risk)
            self.assertEqual(
                result["actual_constructed_assignment_sha256"],digest)
            self.assertTrue(result["full_finite_Jcross_charge_into_true_S_proved"])
            self.assertTrue(result[
                "unit_capacity_S_charge_for_considered_witnesses_proved"])
            self.assertFalse(result["all_h_Jcross_leq_S_proved"])
            self.assertFalse(result["all_h_S_omega_s6_proved"])
            # Every assigned target satisfies the exact accepted motif
            # structural predicate, witnessed again without trusting
            # the recorded family string.
            for _,ids,tag in result["actual_assignment_samples"]:
                self.assertEqual(generic_seven_family(m,ids),tag)
                self.assertGreater(R3_CERTIFIED_FLOORS[tag],0)

    def test_quantitative_lower_strict_additivity_across_seven(self):
        # All selected original sixsets MUST be distinct globally. The
        # accepted per-family GF5 numerator lower is additive only then.
        model=gq_pair_model(1,"lex")
        cert=adaptive_complete_cross_probe(
            model,max_nodes_per_seed=8000,max_seeds_per_unmatched=3)
        hist=cert["positive_seven_family_counts"]
        self.assertEqual(sum(hist.values()),cert["positive_seven_S_lower"])
        floor=sum(hist[c]*R3_CERTIFIED_FLOORS[c] for c in hist)
        self.assertEqual(floor,cert[
            "positive_risk_numerator_lower_51_pow_6"])
        self.assertLessEqual(
            Fraction(floor,51**6),
            seven_census(model,independent_checks=False)["GF5_seven_lower"])
        self.assertGreater(floor,0)

    def test_false_zero_budget_proofs_are_fail_closed(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(model,sample_limit=0)
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(model,first_pass_seed_count=0)
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(
                model,first_pass_seed_count=2,max_seeds_per_unmatched=1)
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(model,max_targets_per_seed=0)
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(model,max_nodes_per_seed=True)
        with self.assertRaises(ValueError):
            adaptive_complete_cross_probe(model,max_unique_targets=0)
        # A zero-node budget returns NO candidates for every tested
        # pair; this must be marked explicitly INCONCLUSIVE.
        empty=adaptive_complete_cross_probe(
            model,sample_limit=4,max_nodes_per_seed=0,
            max_seeds_per_unmatched=2)
        self.assertEqual(empty["positive_seven_S_lower"],0)
        self.assertEqual(empty["matched_after_adaptive_recovery"],0)
        self.assertFalse(empty["full_finite_Jcross_charge_into_true_S_proved"])
        self.assertFalse(empty["failure_when_budgeted_unmatched_proved"])

if __name__=="__main__":
    unittest.main()
