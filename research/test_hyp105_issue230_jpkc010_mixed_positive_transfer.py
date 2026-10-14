"""Fail-closed genuine ORIGINAL W32/W34 mixed GF5 continuation regression."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc010_mixed_positive_transfer import (
    mixed_positive_certificate, complete_right_four_factor_fiber,
    REACHABLE, FIBERS,
)


class JPKC010Tests(unittest.TestCase):
    def test_all_W32_original_schemes_full_mixed_ledger(self):
        for scheme, expected in (("lex", None), ("reverse", None),
                                 ("S68", 68), ("S72", 72)):
            with self.subTest(scheme=scheme):
                c = mixed_positive_certificate(fixture(1, scheme))
                self.assertTrue(c["complete_endpoint_bad_seed_census"])
                self.assertTrue(c["one_complete_globally_injective_original_f_g"])
                self.assertTrue(c["J35_exact_Hall_D6_equals_source_topology_D6"])
                self.assertTrue(c["J35_true_original_incidence_ids_and_GF5_positions"])
                self.assertTrue(c["J35_W32_full_source_three_extension_set_equality"])
                self.assertEqual(
                    sum(c["seed_positive_type_partition"].values()),
                    c["examined_real_endpoint_bad_physical_seeds"])
                self.assertEqual(
                    sum(c["class_witness_pairs"].values()),
                    c["positive_original_seed_Q_witness_pairs"])
                self.assertLessEqual(
                    c["J36_class_sensitive_ceil_charge_lower_for_full_S"],
                    c["distinct_positive_original_sixsets_reached"])
                self.assertLessEqual(
                    c["distinct_positive_original_sixsets_reached"],
                    c["independent_full_original_W32_seven_S"])
                if expected is not None:
                    self.assertEqual(c["independent_full_original_W32_seven_S"],
                                     expected)
                    self.assertEqual(
                        c["AA_original_source_stage"].get(
                            "AA_selected_D6_occurrences", 0), 0)
                pins = {
                    "lex": (786, 68, 26, 94, 24),
                    "reverse": (676, 31, 11, 62, 2),
                    "S68": (544, 4, 2, 8, 0),
                    "S72": (600, 5, 2, 10, 0),
                }
                population, reached, charge, wedge_only, mixed = pins[scheme]
                self.assertEqual(
                    c["examined_real_endpoint_bad_physical_seeds"], population)
                self.assertEqual(
                    c["distinct_positive_original_sixsets_reached"], reached)
                self.assertEqual(
                    c["J36_class_sensitive_ceil_charge_lower_for_full_S"], charge)
                self.assertEqual(
                    c["seed_positive_type_partition"].get("single_wedge_no_D6", 0)
                    + c["seed_positive_type_partition"].get("both_wedges_no_D6", 0),
                    wedge_only)
                self.assertEqual(
                    c["seed_positive_type_partition"].get("D6_and_wedge", 0), mixed)
                cross_pins = {
                    "lex": (4616, 47, 5, 4792, 59, 5),
                    "reverse": (3912, 13, 0, 3784, 10, 0),
                    "S68": (2632, 1, 0, 2696, 4, 0),
                    "S72": (2928, 7, 0, 3312, 3, 0),
                }
                self.assertEqual(tuple(
                    c["original_JPKC009_cross_key_stages_on_same_f_g"][side][stage]
                    for side in ("left", "right")
                    for stage in (
                        "JPKC009_raw_original_source_demand_cross",
                        "JPKC009_Hall_original_source_demand_cross",
                        "JPKC009_selected_D6_original_source_demand_cross",
                    )), cross_pins[scheme])
                self.assertFalse(c["root_A_proved"])

    def test_original_source_cross_Q_pair_is_incidence_not_physical_proxy(self):
        c = mixed_positive_certificate(fixture(1, "lex"))
        hist = c["positive_original_Q_cross_anchor_shared_ID_multiplicity"]
        self.assertEqual(sum(hist.values()), sum(
            c["positive_original_Q_cross_anchor_pairs_by_GF5_class"].values()))
        self.assertLessEqual(sum(hist.values()),
                             c["positive_original_Q_pairs_sharing_incidence"])
        self.assertTrue(all(1 <= int(k) <= 5 for k in hist))

    def test_pinned_coherent_fibers_early_states_not_falsely_complete(self):
        for scheme, base in (("S68", 68), ("S72", 72)):
            with self.subTest(scheme=scheme):
                x = complete_right_four_factor_fiber(scheme, states=2)
                self.assertEqual(x["original_line_block"], FIBERS[scheme])
                self.assertEqual(x["legally_globally_injected_states_examined"], 2)
                self.assertFalse(x["entire_24_state_right_factor_fiber_exhausted"])
                self.assertEqual(x["states"][0]["full_original_seven_S"], base)
                self.assertEqual(
                    x["min_class_charge_on_examined_states"],
                    min(row["mixed_class_charge"] for row in x["states"]))
                self.assertLessEqual(
                    x["min_class_charge_on_examined_states"],
                    x["min_full_original_seven_S_on_examined_states"])

    def test_true_original_W34_targeted_no_full_claim(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        spread, proof = spread_adversary_model(2)
        self.assertEqual(proof["M_f_original_exact"], 259)
        for name, model in (("lex", fixture(2, "lex")), ("spread", spread)):
            with self.subTest(name=name):
                c = mixed_positive_certificate(
                    model, limit_seeds=2, independent_W32=False)
                self.assertEqual(c["s"], 4)
                self.assertEqual(c["examined_real_endpoint_bad_physical_seeds"], 2)
                self.assertFalse(c["complete_endpoint_bad_seed_census"])
                self.assertIsNone(c["independent_full_original_W32_seven_S"])
                self.assertFalse(c["full_W34_seven_census"])
                self.assertFalse(c["J35_W32_full_source_three_extension_set_equality"])
                self.assertTrue(c["J35_exact_Hall_D6_equals_source_topology_D6"])

    def test_fail_closed_bad_global_map_incomplete_fiber_and_budgets(self):
        model = fixture(1, "S68")
        corrupt = dict(model)
        labels = list(model["right_labels"])
        labels[0] = labels[1]
        corrupt["right_labels"] = tuple(labels)
        with self.assertRaises(ValueError):
            mixed_positive_certificate(corrupt)
        with self.assertRaisesRegex(ValueError, "seed-to-Q witness pair budget"):
            mixed_positive_certificate(model, max_pairs=1)
        with self.assertRaisesRegex(ValueError, "restricted to W32"):
            mixed_positive_certificate(fixture(2, "lex"))
        for bad in (0, -1, 25, True):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    complete_right_four_factor_fiber("S68", states=bad)
        with self.assertRaises(ValueError):
            complete_right_four_factor_fiber("lex", states=1)


if __name__ == "__main__":
    unittest.main()
