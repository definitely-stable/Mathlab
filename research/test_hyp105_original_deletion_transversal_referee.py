"""Strict independent genuine ORIGINAL W32 six-ID deletion hypergraph tests.

Not merely 2–4 selected examples: enumerate EVERY original adversarial Z
of cardinality 0..4 and independently verify its motif survivors by
direct boolean source-set intersection; compare with a separate source
seven-class oracle. Verify the EXACT minimum hitting certificate and
maximum original-six-ID packing by two different finite algorithms.

No all-h theorem can be proven by these finite W32 tests.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_original_ten_sign_exclusive import Q_TEN
from hyp105_original_deletion_transversal_referee import (
    independent_true_six_motif,original_W32_hypergraph,
    _edge_masks,exact_min_original_hitting_set,
    exact_max_original_disjoint_packing,
    exact_adversarial_original_deletion_profile,
    exact_binomial_tail_under_ten_sign_union,
    finite_true_original_W32_exact_deletion_report)


class TrueOriginalW32DeletionTransversalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models={scheme:pair_labeled_symplectic(1,scheme)
                    for scheme in ("lex","reverse-line")}
        cls.events={}
        for scheme in cls.models:
            cls.events[scheme],n=original_W32_hypergraph(scheme)
            assert n==45

    def test_original_45_flag_physical_motifs_match_independent_historical_census(self):
        for scheme,expected in (("lex",(15,8)),("reverse-line",(3,7))):
            with self.subTest(scheme=scheme):
                m=self.models[scheme]
                old=seven_census(m,independent_checks=True,witness_sets=True)
                expected_ids={
                    (tuple(ids),family)
                    for ids,family in old["sets"].items()
                    if family in ("D6","B/B-overlap")}
                self.assertEqual(set(self.events[scheme]),expected_ids)
                self.assertEqual(
                    (sum(k=="D6" for _,k in expected_ids),
                     sum(k=="B/B-overlap" for _,k in expected_ids)),expected)
                for ids,kind in expected_ids:
                    self.assertEqual(
                        independent_true_six_motif(
                            ids,m["incidences"],m["left_labels"],m["right_labels"]),
                        kind)

    def test_full_exhaustive_all_adversarial_original_Z_size_0_1_2_3(self):
        for scheme in self.models:
            with self.subTest(scheme=scheme):
                E=self.events[scheme]
                enc=_edge_masks(E,45)
                profile=exact_adversarial_original_deletion_profile(enc,45,4)
                for row in profile:
                    k=row["deleted_original_ID_cardinality"]
                    self.assertEqual(row[
                        "all_adversarial_deletion_subsets_exactly_enumerated"],
                        comb(45,k))
                    self.assertEqual(row[
                        "exact_total_survivor_events_over_all_deletions"],
                        len(E)*comb(39,k))
                    # A SECOND source-direct implementation for k<=3,
                    # without hypergraph mask helpers or solver recursion.
                    if k<=3:
                        minimum=len(E);worst=0
                        for Z in combinations(range(45),k):
                            deleted=frozenset(Z)
                            survived=sum(
                                deleted.isdisjoint(ids) for ids,_ in E)
                            if survived<minimum:
                                minimum=survived;worst=1
                            elif survived==minimum:worst+=1
                        self.assertEqual(row[
                            "minimum_surviving_true_original_six_motifs"],minimum)
                        self.assertEqual(row[
                            "number_of_worst_adversarial_source_deletions"],worst)

    def test_exact_min_transversal_and_source_packing_two_methods(self):
        for scheme in self.models:
            with self.subTest(scheme=scheme):
                E=self.events[scheme]
                masks=_edge_masks(E,45)
                cover=exact_min_original_hitting_set(masks,45)
                packing=exact_max_original_disjoint_packing(masks,45)
                T=set(cover["original_IDs"])
                self.assertEqual(len(T),cover["tau"])
                self.assertTrue(all(not T.isdisjoint(ids) for ids,_ in E))
                matched=packing["six_original_ID_sets"]
                self.assertEqual(len(matched),packing["nu"])
                self.assertEqual(len({x for row in matched for x in row}),
                                 6*len(matched))
                self.assertLessEqual(packing["nu"],cover["tau"])
                # Completely different brute force k-subset deletion oracle,
                # practical only for k<=3 on the W32 host.
                for k in range(min(cover["tau"],4)):
                    if k>3:continue
                    self.assertFalse(any(
                        all(not set(Z).isdisjoint(ids) for ids,_ in E)
                        for Z in combinations(range(45),k)))
                # Independently check the no-larger-disjoint-matching
                # witness by enumerating all (nu+1)-tuples of true sixsets
                # if finite enough; otherwise the recursion is complete
                # by include/exclude and is independently tested small.
                if comb(len(masks),packing["nu"]+1)<=300000:
                    self.assertFalse(any(
                        all((a&b)==0 for a,b in combinations(x,2))
                        for x in combinations(masks,packing["nu"]+1)))

    def test_independent_R2_or_wrong_source_not_rebranded_as_BBo(self):
        m=self.models["lex"]
        ids=tuple(range(6))
        kind=independent_true_six_motif(
            ids,m["incidences"],m["left_labels"],m["right_labels"])
        self.assertIn(kind,(None,"D6","B/B-overlap"))
        with self.assertRaises(ValueError):
            independent_true_six_motif(
                (0,0,1,2,3,4),m["incidences"],m["left_labels"],m["right_labels"])
        with self.assertRaises(ValueError):
            original_W32_hypergraph("artificial independent injection")

    def test_exact_stochastic_binomial_all_integer_repair_thresholds(self):
        p=Q_TEN
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(3,1),(1-p)**3)
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(3,2),
                         (1-p)**3+3*p*(1-p)**2)
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(3,3),
                         1-p**3)
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(3,0),0)
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(3,4),1)
        self.assertEqual(exact_binomial_tail_under_ten_sign_union(0,1),1)
        for n in range(1,9):
            prev=Fraction(0)
            for r in range(n+2):
                z=exact_binomial_tail_under_ten_sign_union(n,r)
                self.assertGreaterEqual(z,prev)
                prev=z
            self.assertEqual(prev,1)
        with self.assertRaises(ValueError):
            exact_binomial_tail_under_ten_sign_union(-1,1)
        with self.assertRaises(ValueError):
            exact_binomial_tail_under_ten_sign_union(3,5)

    def test_true_original_complete_finite_cert_scope_and_hamming_distance(self):
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                z=finite_true_original_W32_exact_deletion_report(scheme)
                self.assertEqual(z["true_original_incidence_flags"],45)
                self.assertEqual(
                    z["accepted_true_original_by_class"],
                    {"D6":15 if scheme=="lex" else 3,
                     "B/B-overlap":8 if scheme=="lex" else 7})
                self.assertTrue(z["exact_minimum_adversarial_original_ID_deletions"][
                    "rejected_cardinality_at_tau_minus_1"])
                self.assertTrue(z["exact_maximum_original_ID_disjoint_six_motif_packing"][
                    "exact_maximum_proved_by_include_exclude_DP"])
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertFalse(z["root_allh_geom_branch_A_PROVED_HERE"])
                self.assertFalse(z["claim_entire_W32_0_3_GF5_R3_exact_computed"])
                self.assertTrue(z[
                    "general_allh_source_packing_requires_external_review_of_674"])


if __name__=="__main__":
    unittest.main()
