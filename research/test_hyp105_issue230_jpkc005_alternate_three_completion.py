"""Exact true-original JPKC-005 tests: alternate six-incidence completions."""
import unittest
from itertools import combinations
from collections import Counter

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc005_alternate_three_completion import (
    general_seven_original,alternate_completion_certificate,
    _honest_W34_structural_stress,_canonical,_other_gq_anchor,
    MAX_SEEDS_PER_ORIGINAL_SIXSET,
    SEED_REACHABLE,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


class JPKC005Tests(unittest.TestCase):
    def test_independent_all_62370_true_original_W32_structural_seven_classes(self):
        for scheme in ("S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                ctx=ProjectionClosure(model)
                counts=Counter()
                for Q,kind in selected_left_six(model):
                    actual=general_seven_original(ctx,Q)
                    expected=classify_seven_prechecked(
                        Q,ctx.f,ctx.g,ctx.edges)
                    self.assertEqual(actual,expected)
                    if actual:
                        counts[actual]+=1
                source=seven_census(model,independent_checks=False)
                self.assertEqual(sum(counts.values()),source["S_seven"])
                self.assertEqual(dict(counts),
                    {k:v for k,v in source["seven_class_motif_counts"].items() if v})

    def test_true_original_W32_all_eligible_endpoint_bad_seeds_and_GQ_alternates(self):
        expected={
            # E, true S, path coverage, accepted (P,Q) hits,
            # exact source-positive class hits (A/B, B/A, D6)
            "lex":(786,259,154,214,(82,68,64)),
            "reverse":(676,169,86,90,(30,36,24)),
            "S68":(544,68,8,8,(2,6,0)),
            "S72":(600,72,10,10,(4,6,0)),
        }
        for scheme,(E,S,coverage,hits,classes) in expected.items():
            with self.subTest(scheme=scheme):
                row=alternate_completion_certificate(fixture(1,scheme),
                                                     include_examples=True)
                self.assertEqual(row["endpoint_bad_oriented_proper_P3"],E)
                self.assertEqual(row["W32_true_original_S"],S)
                self.assertEqual(
                    row["endpoint_bad_physical_seeds_with_accepted_alternate_completion"],
                    coverage)
                self.assertEqual(row["accepted_seed_completion_pairs"],hits)
                self.assertEqual(
                    tuple(row["accepted_extension_by_true_original_seven_class"][t]
                          for t in ("A-left/B-right","B-left/A-right","D6")),
                    classes)
                self.assertTrue(row["J17_all_h_only_canonical_original_GQ_three_walk_if_positive"])
                self.assertEqual(row["J17_noncanonical_second_GQ_anchor_positive_completions"],0)
                self.assertEqual(
                    row["alternate_three_incidence_completion_GQ_walk_types"].get(
                        "second_true_original_GQ_walk",0),0)
                self.assertTrue(row["full_seven_enumeration_executed"])
                self.assertTrue(row["J14_witness_320S_verified"])
                self.assertEqual(
                    row["endpoint_bad_physical_seeds_with_accepted_alternate_completion"]+
                    row["endpoint_bad_physical_seeds_without_accepted_completion"],E)
                self.assertEqual(sum(row["completion_options_per_oriented_physical_seed"].values()),E)
                self.assertLessEqual(row["observed_max_physical_P3_seed_hits_per_accepted_Q"],320)
                self.assertLessEqual(
                    row["maximum_realized_physical_P3_per_original_three_seed"],16)
                self.assertEqual(
                    row["accepted_extension_by_true_original_seven_class"]["C/A"],0)
                self.assertEqual(
                    row["accepted_extension_by_true_original_seven_class"]["C/B"],0)
                self.assertEqual(sum(row["accepted_extension_by_true_original_seven_class"].values()),
                                 row["accepted_seed_completion_pairs"])
                self.assertTrue(all(x<=2 for x in
                                    row["alternate_completion_intersection_with_canonical_three"]))
                self.assertEqual(sum(row["alternate_three_incidence_completion_GQ_walk_types"].values()),
                                 row["accepted_seed_completion_pairs"])
                for Q in row["actual_original_completion_examples"].values():
                    self.assertEqual(len(set(Q["six_original_ids"])),6)
                    self.assertEqual(len(set(Q["alternate_completion_original_ids"])),3)
                    self.assertNotEqual(set(Q["alternate_completion_original_ids"]),
                                        set(Q["original_canonical_incidence_ids"]))
                    self.assertIn(
                        general_seven_original(ProjectionClosure(fixture(1,scheme)),
                                               Q["six_original_ids"]),SEED_REACHABLE)
                self.assertFalse(row["all_h_universal_seven_lower_PROVED_A"])

    def test_true_original_W34_lex_random_unblocked_positive_closure(self):
        for scheme,unblocked in (("lex",15064),("random",16042)):
            row=_honest_W34_structural_stress(fixture(2,scheme))
            self.assertEqual(row["s"],4)
            self.assertFalse(row["full_seven_enumeration_executed"])
            self.assertFalse(row["full_W34_seven_census_PROVED"])
            self.assertEqual(row["unblocked_original_sixset_structural_crosscheck"],unblocked)
            self.assertTrue(row["J17_all_h_only_canonical_original_GQ_three_walk_if_positive"])
            self.assertEqual(row["unblocked_Q_classes"],
                             {"B/B-overlap":row["unblocked_original_sixset_structural_crosscheck"]})

    def test_true_original_W34_D4_spread_no_false_synthetic_completion(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,proof=spread_adversary_model(2)
        row=_honest_W34_structural_stress(model)
        self.assertEqual(proof["M_f_original_exact"],259)
        self.assertFalse(row["full_seven_enumeration_executed"])
        self.assertEqual(row["unblocked_original_sixset_structural_crosscheck"],15298)
        self.assertTrue(row["J17_all_h_only_canonical_original_GQ_three_walk_if_positive"])

    def test_original_alt_GQ_three_incidence_recovery_exact(self):
        c=ProjectionClosure(fixture(1,"S68"))
        for (q,r),(p,l) in c.projection.items():
            anchor=tuple(sorted(_canonical(c,q,r)))
            self.assertEqual(_other_gq_anchor(c,anchor),(q,r))
            break
        # A triple not forming the genuine length-three GQ projection is
        # classified as 'not a second GQ anchor', never fabricated.
        bad=(0,1,2)
        found=_other_gq_anchor(c,bad)
        if found is not None:
            self.assertEqual(frozenset(bad),_canonical(c,*found))

    def test_fail_closed_scope_and_limits(self):
        with self.assertRaisesRegex(ValueError,"W32-only"):
            alternate_completion_certificate(fixture(2,"lex"))
        with self.assertRaisesRegex(ValueError,"index budget"):
            alternate_completion_certificate(fixture(1,"lex"),
                                             max_accepted_sixsets=1)
        with self.assertRaisesRegex(ValueError,"index budget"):
            alternate_completion_certificate(fixture(1,"lex"),
                                             max_accepted_sixsets=0)
        with self.assertRaisesRegex(ValueError,"path budget"):
            alternate_completion_certificate(fixture(1,"S68"),max_paths=1)
        corrupted=fixture(1,"lex")
        left=list(corrupted["left_labels"])
        left[0]=left[1]
        corrupted["left_labels"]=tuple(left)
        with self.assertRaises(ValueError):
            alternate_completion_certificate(corrupted)
        with self.assertRaisesRegex(ValueError,"six distinct original"):
            general_seven_original(ProjectionClosure(fixture(1,"lex")),(1,1,2,3,4,5))


if __name__=="__main__":
    unittest.main()
