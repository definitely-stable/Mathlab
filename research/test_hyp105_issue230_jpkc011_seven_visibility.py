"""JPKC-011: independent exact true ORIGINAL sixset visibility falsifiers."""
from collections import Counter
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc010_mixed_positive_transfer import (
    mixed_positive_certificate,
)
from hyp105_issue230_jpkc011_seven_visibility import (
    visibility_certificate, visibility_right_four_factor_fiber,
    STATES, ALL_TAGS, C_HALF_TAGS, BB_TAGS, VISIBLE_BAD, PROJECTION_ONLY,
    VISIBLE_OTHER, INVISIBLE,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


class OriginalSevenVisibilityTests(unittest.TestCase):
    def test_complete_W32_true_original_all_seven_GF5_classes(self):
        # Frozen FULL ORIGINAL seven-class W32 exact hosted visibility pins.
        expected = {
            "lex": (259,68,5,17,169,11225795),
            "reverse": (169,31,4,4,130,7627209),
            "S68": (68,4,1,0,63,3112510),
            "S72": (72,5,0,1,66,3283610),
        }
        for scheme, (full,bad,physical,other,invisible,weighted) in expected.items():
            with self.subTest(scheme=scheme):
                x = visibility_certificate(fixture(1, scheme),
                                           direct_local_oracle=True)
                self.assertEqual(x["all_original_left_sixcoordinate_candidates"], 62370)
                self.assertTrue(x["all_positive_Q_local_diagonal_equals_global_path_oracle"])
                self.assertGreater(x["source_triples_independently_verified"], 0)
                self.assertTrue(x["true_original_f_g_globally_injective"])
                self.assertEqual(x["J38_complete_original_Q_visibility_partition"],{
                    VISIBLE_BAD:bad, PROJECTION_ONLY:physical,
                    VISIBLE_OTHER:other, INVISIBLE:invisible})
                self.assertEqual(x["complete_original_positive_seven_S"],full)
                self.assertEqual(x["J40_full_original_GF5_floor_numerator"],weighted)
                self.assertEqual(sum(x["J38_complete_original_Q_visibility_partition"].values()),
                                 x["complete_original_positive_seven_S"])
                self.assertEqual(sum(x["J40_GF5_floor_by_visibility"].values()),
                                 x["J40_full_original_GF5_floor_numerator"])
                self.assertEqual(x["positive_Q_invisible_to_JPKC010_bad_seed_ledger"],
                                 x["complete_original_positive_seven_S"]-bad)
                self.assertEqual(
                    x["original_positive_Q_with_broad_blocked_projection_P3"],
                    x["J38_complete_original_Q_visibility_partition"][VISIBLE_BAD] +
                    x["J38_complete_original_Q_visibility_partition"][PROJECTION_ONLY])
                self.assertEqual(x["accepted_original_sixsets_exactly_once"],
                                 x["complete_original_positive_seven_S"])
                if scheme in ("lex", "reverse", "S68"):
                    self.assertEqual(
                        x["original_positive_Q_with_broad_blocked_projection_P3"],
                        {"lex": 73, "reverse":35, "S68":5}[scheme])
                    self.assertGreater(
                        x["J38_complete_original_Q_visibility_partition"][PROJECTION_ONLY], 0)
                if scheme in ("S68","S72"):
                    classes=x["J38_exact_seven_class_visibility"]
                    missing_wedges=(
                        classes["A-left/B-right"][INVISIBLE]+
                        classes["B-left/A-right"][INVISIBLE])
                    self.assertEqual(missing_wedges,{"S68":60,"S72":61}[scheme])
                self.assertTrue(
                    x["J38_distinguishes_internal_physical_projection_block_from_factor_bad"])
                self.assertFalse(x["root_A_proved"])

    def test_structural_C_half_P3_invisible_and_BB_endpoint_bad_exclusion(self):
        for scheme in ("lex", "reverse", "S68", "S72"):
            with self.subTest(scheme=scheme):
                c = visibility_certificate(fixture(1, scheme),
                                           direct_local_oracle=False)
                tags = c["J38_exact_seven_class_visibility"]
                self.assertEqual(set(tags), set(ALL_TAGS))
                for cls in C_HALF_TAGS:
                    self.assertEqual(tags[cls][VISIBLE_BAD], 0)
                    self.assertEqual(tags[cls][PROJECTION_ONLY], 0)
                    self.assertEqual(tags[cls][VISIBLE_OTHER], 0)
                    self.assertEqual(tags[cls][INVISIBLE],
                                     tags[cls]["all_positive_original_Q"])
                    self.assertEqual(tags[cls]["max_oriented_proper_P3_per_Q"], 0)
                for cls in BB_TAGS:
                    self.assertEqual(tags[cls][VISIBLE_BAD], 0)
                self.assertEqual(sum(
                    tags[tag]["all_positive_original_Q"] * R3_CERTIFIED_FLOORS[tag]
                    for tag in ALL_TAGS),
                    c["J40_full_original_GF5_floor_numerator"])

    def test_same_original_maps_match_independent_jpkc010_all_bad_P3_Q_sets(self):
        for scheme in ("S68", "S72"):
            with self.subTest(scheme=scheme):
                model = fixture(1, scheme)
                visibility = visibility_certificate(model, direct_local_oracle=True)
                ledger = mixed_positive_certificate(model, independent_W32=True)
                self.assertEqual(
                    visibility["J38_complete_original_Q_visibility_partition"][VISIBLE_BAD],
                    ledger["distinct_positive_original_sixsets_reached"])
                self.assertEqual(
                    {tag: visibility["J38_exact_seven_class_visibility"][tag][VISIBLE_BAD]
                     for tag in ledger["class_distinct_positive_original_sixsets_reached"]},
                    ledger["class_distinct_positive_original_sixsets_reached"])

    def test_two_globally_injective_W32_fiber_states_do_not_claim_full_24(self):
        for scheme in ("S68","S72"):
            with self.subTest(scheme=scheme):
                data = visibility_right_four_factor_fiber(scheme, states=2)
                self.assertFalse(data["all_24_globally_injective_states_exhausted"])
                self.assertEqual(data["legal_complete_global_maps_examined"], 2)
                self.assertEqual(data["all_states"][0]["full_original_S"],
                                 {"S68":68,"S72":72}[scheme])
                for row in data["all_states"]:
                    self.assertEqual(sum(row["partition"].values()),row["full_original_S"])
                    self.assertEqual(sum(row["GF5_floor_by_visibility"].values()),
                                     sum(sum(row["class_visibility"][tag][state] *
                                             R3_CERTIFIED_FLOORS[tag]
                                             for state in STATES) for tag in ALL_TAGS))

    def test_fail_closed_invalid_original_map_and_path_or_sixset_budget(self):
        model = fixture(1, "S68")
        broken = dict(model)
        left = list(model["left_labels"])
        left[0] = left[1]
        broken["left_labels"] = tuple(left)
        with self.assertRaises(ValueError):
            visibility_certificate(broken)
        with self.assertRaisesRegex(ValueError,"budget"):
            visibility_certificate(model, max_sixsets=1)
        with self.assertRaisesRegex(ValueError,"path budget"):
            visibility_certificate(model, max_paths=1)
        with self.assertRaisesRegex(ValueError,"W32 only"):
            visibility_certificate(fixture(2,"lex"))
        for bad in (0,-1,25,True):
            with self.subTest(states=bad):
                with self.assertRaises(ValueError):
                    visibility_right_four_factor_fiber("S68", states=bad)
        with self.assertRaises(ValueError):
            visibility_right_four_factor_fiber("lex",states=1)
        with self.assertRaisesRegex(ValueError,"sample_Q"):
            visibility_certificate(model,sample_Q=26)


if __name__=="__main__":
    unittest.main()
