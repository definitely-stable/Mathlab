"""AA4-PALDIST independent physical-original GF5 palette anti-concentration.

The production finite witness builds two different actual complete W32
global map injections; this test separately validates real original
source/factor incidence, the exact GF5^{12} coefficient vector flow
probabilities using two independent algorithms and a source-disjoint
Poisson-binomial distribution. No artificial random-scheme geometry is
substituted for the original W(3,2) flags.
"""
from fractions import Fraction
from itertools import combinations
from math import comb,exp
from pathlib import Path
import json
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,classify_seven_prechecked)
from hyp105_gf5_original_sixid_flow_referee import (
    original_projected_column_edges,
    gf5_flow_inclusion_exclusion,
    gf5_flow_spanning_tree,SIGNS,
    planted_original_d6,planted_original_bb_overlap)
from hyp105_original_random_palette_distance import (
    Q,source_palette_signed_probability,exact_independent_failure_distribution,
    exact_finite_packing_report,genuine_W32_source_disjoint_motif_report,
    conditional_allh_hamming_distance,check_disjoint_original_sixset_packing)

ROOT=Path(__file__).parent


class OriginalPaletteDistanceTests(unittest.TestCase):
    def test_true_W32_all_initial_accepted_and_greedy_original_packing(self):
        for scheme,d6,bb in (("lex",15,8),("reverse-line",3,7)):
            with self.subTest(scheme=scheme):
                model=pair_labeled_symplectic(1,scheme)
                raw=seven_census(model,independent_checks=False,witness_sets=True)
                self.assertEqual(raw["seven_class_motif_counts"]["D6"],d6)
                self.assertEqual(raw["seven_class_motif_counts"]["B/B-overlap"],bb)
                cert=genuine_W32_source_disjoint_motif_report(scheme)
                chosen=cert["original_source_signed_sixset_witnesses"]
                self.assertTrue(chosen)
                self.assertEqual(len(chosen),cert["six_source_distinct_packing_size"])
                self.assertEqual(len({id for e in chosen
                    for id in e["original_source_IDs"]}),6*len(chosen))
                self.assertEqual(cert["actual_original_flag_count"],45)
                for z in chosen:
                    original_ids=tuple(z["original_source_IDs"])
                    physical=original_projected_column_edges(
                        model["incidences"],original_ids,
                        model["left_labels"],model["right_labels"])
                    self.assertEqual(classify_seven_prechecked(
                        original_ids,model["left_labels"],model["right_labels"],
                        model["incidences"]),z["accepted_class"])
                    plus=frozenset(z["chosen_positive_original_local_indices"])
                    self.assertEqual(plus,SIGNS[0])
                    n=gf5_flow_inclusion_exclusion(physical,plus)
                    m=gf5_flow_spanning_tree(physical,plus)
                    self.assertEqual(n,m)
                    self.assertGreaterEqual(n,5175)
                    self.assertEqual(n,z["chosen_signed_GF5_legal_assignments"])
                a=cert["exact_probability_NO_chosen_3v3_source_event"]
                observed=Fraction(a["numerator"],a["denominator"])
                expected=Fraction(1)
                for z in chosen:
                    expected*=1-Fraction(z[
                        "chosen_signed_GF5_legal_assignments"],51**6)
                self.assertEqual(observed,expected)
                self.assertLessEqual(observed,(1-Q)**len(chosen))
                self.assertEqual(cert["root_230_status"],
                                 "OPEN_WITH_FORMAL_BLOCKER")
                self.assertFalse(cert["root_all_h_branch_A_proved_here"])

    def test_physical_source_original_D6_and_BBo_both_s_and_10_signs(self):
        for power in (1,2):
            for factory,lower in ((planted_original_d6,5265),
                                  (planted_original_bb_overlap,5175)):
                with self.subTest(power=power,factory=factory.__name__):
                    z=factory(power)
                    self.assertEqual(len(set(z["ids"])),6)
                    self.assertEqual(len(z["edges"]),12)
                    for plus in SIGNS:
                        self.assertGreaterEqual(
                            gf5_flow_inclusion_exclusion(z["edges"],plus),
                            lower)
                    canonical=gf5_flow_inclusion_exclusion(z["edges"],SIGNS[0])
                    self.assertEqual(canonical,gf5_flow_spanning_tree(
                        z["edges"],SIGNS[0]))

    def test_exact_disjoint_two_bernoulli_source_events_product(self):
        z=[{"original_source_IDs":list(range(6)),
            "accepted_class":"D6",
            "chosen_signed_GF5_legal_assignments":5265},
           {"original_source_IDs":list(range(6,12)),
            "accepted_class":"B/B-overlap",
            "chosen_signed_GF5_legal_assignments":5175}]
        r=exact_finite_packing_report(45,z)
        p1=Fraction(5265,51**6)
        p2=Fraction(5175,51**6)
        law=exact_independent_failure_distribution((5265,5175))
        self.assertEqual(law,((1-p1)*(1-p2),
                              p1*(1-p2)+p2*(1-p1),p1*p2))
        self.assertEqual(law[0],Fraction(
            r["exact_probability_NO_chosen_3v3_source_event"]["numerator"],
            r["exact_probability_NO_chosen_3v3_source_event"]["denominator"]))
        self.assertEqual(
            Fraction(r["exact_expected_chosen_signed_failures"]["numerator"],
                     r["exact_expected_chosen_signed_failures"]["denominator"]),
            p1+p2)
        self.assertEqual(Q,Fraction(5175,51**6))

    def test_canonical_source_fails_on_repeated_flags_and_wrong_class(self):
        a={"original_source_IDs":list(range(6)),
           "accepted_class":"D6","chosen_signed_GF5_legal_assignments":5265}
        b={"original_source_IDs":[5,6,7,8,9,10],
           "accepted_class":"B/B-overlap",
           "chosen_signed_GF5_legal_assignments":5175}
        with self.assertRaises(ValueError):
            exact_finite_packing_report(45,[a,b])
        b["original_source_IDs"]=[6,7,8,9,10,11]
        b["accepted_class"]="nonaccepted-projected-C6"
        with self.assertRaises(ValueError):
            exact_finite_packing_report(45,[a,b])
        b["accepted_class"]="B/B-overlap"
        b["chosen_signed_GF5_legal_assignments"]=1
        with self.assertRaises(ValueError):
            exact_finite_packing_report(45,[a,b])

    def test_all_h_only_conditional_rational_and_no_unearned_proof(self):
        rho=Fraction(1,2000)  # FORMAL TEST INPUT, NOT a valid #674 rho!
        with self.assertRaises(ValueError):
            conditional_allh_hamming_distance(8,rho,
                parent_deletion_theorem_is_an_assumption=False)
        for s in (2,4,8,16,32):
            r=conditional_allh_hamming_distance(
                s,rho,parent_deletion_theorem_is_an_assumption=True)
            tau=rho*s**4/6
            self.assertEqual(
                r["minimum_integer_source_sixset_packing_if_parent_holds"],
                tau.numerator//tau.denominator+1)
            self.assertTrue(r[
                "requires_external_acceptance_of_parent_674_allh_deletion"])
            self.assertFalse(r["root_allh_accepted"])
            self.assertEqual(
                Fraction(*r["palette_clean_exponential_rate"].values()),
                Q*rho/6)  # {"numerator": n, "denominator": d}
        with self.assertRaises(ValueError):
            conditional_allh_hamming_distance(12,rho,
                parent_deletion_theorem_is_an_assumption=True)


if __name__=="__main__":
    unittest.main()
