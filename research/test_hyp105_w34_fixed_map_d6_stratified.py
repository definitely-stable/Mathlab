"""AA4-FIXD6 independent true-source original sixset audits."""
import json
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_pair_codegree_triangle_d6 import exact_pair_codegree_triangle_d6
from hyp105_w34_fixed_map_d6_stratified import (
    true_source_D6_stratified_by_frozen_lines,
    true_W34_fixed_f_frozen_g_D6_displacement,
)


class TestTrueW34FixedMapD6Displacement(unittest.TestCase):
    def test_W32_original_lex_two_algorithms_and_frozen_g_conservation(self):
        m = pair_labeled_symplectic(1, "lex")
        f, g = m["left_labels"], m["right_labels"]
        J = frozenset(range(7))
        original = true_source_D6_stratified_by_frozen_lines(1, f, g, J)
        independent = exact_pair_codegree_triangle_d6(
            1, f, g, verify_historical_gf5=True,
            verify_existing_C6_oracle=True)
        self.assertEqual(original["exact_original_GF5_D6"],
                         independent["accepted_original_D6"])
        self.assertEqual(original["exact_original_GF5_D6"], 15)
        self.assertEqual(sum(original["D6_by_unfrozen_source_lines"].values()),
                         15)
        changed = list(g)
        changed[7], changed[8] = changed[8], changed[7]
        altered = true_source_D6_stratified_by_frozen_lines(
            1, f, changed, J)
        self.assertEqual(original["frozen_only_original_D6_sixsets"],
                         altered["frozen_only_original_D6_sixsets"])
        self.assertEqual(original["D6_by_unfrozen_source_lines"][0],
                         altered["D6_by_unfrozen_source_lines"][0])

    def test_fails_closed_on_noninjective_true_source_physical_labels(self):
        m = pair_labeled_symplectic(1, "lex")
        f, g = list(m["left_labels"]), m["right_labels"]
        f[0] = f[1]
        with self.assertRaises((AssertionError, ValueError)):
            true_source_D6_stratified_by_frozen_lines(
                1, f, g, {0, 1})
        with self.assertRaises(ValueError):
            true_source_D6_stratified_by_frozen_lines(
                1, m["left_labels"], g, {85})

    def test_true_W34_same_f_and_frozen_g_global_D6_sector_census(self):
        report = true_W34_fixed_f_frozen_g_D6_displacement()
        self.assertEqual((report["s"], report["V"], report["a"],
                          report["original_source_flags"]), (4, 85, 14, 425))
        self.assertTrue(report["same_full_f_and_frozen_g_J"])
        self.assertTrue(report["frozen_only_D6_original_sixsets_identical"])
        self.assertEqual(report["source_lines_frozen"], 12)
        self.assertEqual(report["source_lines_unfrozen"], 73)
        for name, mass in (("positive", 4), ("zero", 0)):
            item = report[name]
            self.assertEqual(
                item["actual_local_full_H_fresh_hub_pair_mass"], mass)
            self.assertEqual(item["selected_saturated_K32_blocks"], 2)
            self.assertTrue(item["source_ID_DFS_pair_codegree_agree"])
            self.assertEqual(
                sum(item["D6_by_unfrozen_source_lines"].values()),
                item["global_accepted_original_GF5_D6"])
            self.assertEqual(
                sum(item["D6_by_selected_source_flags"].values()),
                item["global_accepted_original_GF5_D6"])
            self.assertEqual(
                item["global_K33_sector_D6"] +
                item["global_non_K33_sector_D6"],
                item["global_accepted_original_GF5_D6"])
            self.assertGreater(item["global_accepted_original_GF5_D6"], 0)
            self.assertGreaterEqual(
                item["global_accepted_original_GF5_D6"],
                item["accepted_original_D6_two_flag_extension_lower"])
            self.assertEqual(
                item["D6_by_unfrozen_source_lines"][0],
                report["frozen_only_original_D6_count"])
        self.assertEqual(
            report["positive"]["accepted_original_D6_two_flag_extension_lower"], 8)
        self.assertEqual(
            report["zero"]["accepted_original_D6_two_flag_extension_lower"], 0)
        self.assertFalse(report["complete_original_seven_class_census"])
        self.assertFalse(report["universal_all_h_S_s_omega_s6_proved"])
        self.assertFalse(report["infinite_counterexample_to_root"])
        # Emit reproducible exact counts in GitHub-hosted test log.
        print("HYP105_AA4_FIXD6_CERTIFICATE=" +
              json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
