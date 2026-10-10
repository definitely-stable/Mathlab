"""C16 genuine original incidence joint-map and adversarial source tests."""
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import PAIRS, selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c14_domain_certificates import (
    _completion_pairs, _filled_model,
)
from hyp105_g5e2b3e1c16_two_sided_source import (
    two_sided_source_certificate,
)


class C16TwoSidedSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = pair_labeled_symplectic(1, "reverse-line")
        cls.f = {i: PAIRS.index(cls.m["left_labels"][i]) for i in range(12)}
        cls.g = {i: PAIRS.index(cls.m["right_labels"][i]) for i in range(12)}
        cls.root = two_sided_source_certificate(cls.m, cls.f, cls.g)

    def test_nested_both_side_nonnegative_exact_hierarchy(self):
        x = self.root
        self.assertEqual(x["actual_joint_completions"], 36)
        self.assertEqual(x["actual_motif_classifications"], 62370 * 36)
        self.assertEqual(x["left_pinned_candidates_per_left_completion"], 6723)
        self.assertEqual(x["C15_eligible_one_right_lower_S"], 12)
        self.assertEqual(
            x["C15_eligible_one_right_lower_GF5_numerator"], 513393)
        self.assertGreater(x["distinct_original_sixsets_in_union"], 62370)
        for metric in ("S", "GF5_numerator"):
            order = [
                "C15_eligible_one_right_lower_",
                "C16_two_sided_signature_lower_",
                "C16_one_left_signature_group_lower_",
                "C16_shared_left_groupwise_right_lower_",
                "C16_exact_joint_box_lower_",
            ]
            values = [x[p + metric] for p in order]
            self.assertEqual(values, sorted(values))
        self.assertEqual(x["C16_exact_joint_box_lower_S"], 148)
        self.assertEqual(
            x["C16_exact_joint_box_lower_GF5_numerator"], 6676842)

    def test_true_36_full_joint_maps_independent_seven_recount(self):
        x = self.root
        maps = list(_completion_pairs(self.m, self.f, self.g, 36))
        self.assertEqual(len(maps), 36)
        scores = [
            seven_census(_filled_model(self.m, fl, gr),
                         independent_checks=False)
            for fl, gr in maps
        ]
        self.assertEqual(
            tuple(s["S_seven"] for s in scores),
            x["S_by_every_actual_joint_completion"])
        self.assertEqual(
            tuple(s["GF5_seven_lower_numerator"] for s in scores),
            x["GF5_by_every_actual_joint_completion"])
        for s in scores:
            for metric, name in (
                ("S_seven", "C16_two_sided_signature_lower_S"),
                ("GF5_seven_lower_numerator",
                 "C16_two_sided_signature_lower_GF5_numerator"),
            ):
                self.assertGreaterEqual(s[metric], x[name])

    def test_noncanonical_left_tail_changes_sixset_membership(self):
        # Critical C15 -> C16 repair: variable-left selected_left_six
        # cannot be identified with a single canonical filler.
        maps = list(_completion_pairs(self.m, self.f, self.g, 36))
        fa, ga = maps[0]
        fb, gb = next((f, g) for f, g in maps if f != fa)
        a = {ids for ids, _ in selected_left_six(
            _filled_model(self.m, fa, ga))}
        b = {ids for ids, _ in selected_left_six(
            _filled_model(self.m, fb, gb))}
        self.assertEqual(len(a), 62370)
        self.assertEqual(len(b), 62370)
        self.assertNotEqual(a, b)
        self.assertGreater(len(a | b), 62370)

    def test_prefix_extension_is_monotone_for_both_scores(self):
        f = dict(self.f)
        g = dict(self.g)
        f[12] = next(v for v in range(15) if v not in f.values())
        g[12] = next(v for v in range(15) if v not in g.values())
        child = two_sided_source_certificate(self.m, f, g)
        self.assertEqual(child["actual_joint_completions"], 4)
        for suffix in ("S", "GF5_numerator"):
            for name in (
                "C16_two_sided_signature_lower_",
                "C16_one_left_signature_group_lower_",
                "C16_shared_left_groupwise_right_lower_",
                "C16_exact_joint_box_lower_",
            ):
                self.assertGreaterEqual(child[name + suffix],
                                        self.root[name + suffix])

    def test_nonprefix_original_pins_other_true_four_map_box(self):
        # Independent non-prefix adversary: neither the left nor the right
        # missing source IDs are a terminal 12+ prefix. All four real joint
        # completions must match independent accepted seven_census scores.
        f = {i: PAIRS.index(e)
             for i, e in enumerate(self.m["left_labels"]) if i not in (1, 13)}
        g = {i: PAIRS.index(e)
             for i, e in enumerate(self.m["right_labels"]) if i not in (0, 12)}
        x = two_sided_source_certificate(self.m, f, g)
        real = [
            seven_census(_filled_model(self.m, fl, gr),
                         independent_checks=False)
            for fl, gr in _completion_pairs(self.m, f, g, 4)
        ]
        self.assertEqual(x["actual_joint_completions"], 4)
        self.assertEqual(
            x["S_by_every_actual_joint_completion"],
            tuple(t["S_seven"] for t in real))
        self.assertEqual(
            x["GF5_by_every_actual_joint_completion"],
            tuple(t["GF5_seven_lower_numerator"] for t in real))
        self.assertEqual(x["C16_exact_joint_box_lower_S"],
                         min(t["S_seven"] for t in real))
        self.assertEqual(
            x["C16_exact_joint_box_lower_GF5_numerator"],
            min(t["GF5_seven_lower_numerator"] for t in real))

    def test_complete_pins_exact_and_fail_closed_budgets(self):
        complete_f = {
            i: PAIRS.index(e) for i, e in enumerate(self.m["left_labels"])}
        complete_g = {
            i: PAIRS.index(e) for i, e in enumerate(self.m["right_labels"])}
        x = two_sided_source_certificate(self.m, complete_f, complete_g)
        real = seven_census(self.m, independent_checks=False)
        self.assertEqual(x["C16_exact_joint_box_lower_S"], real["S_seven"])
        self.assertEqual(
            x["C16_exact_joint_box_lower_GF5_numerator"],
            real["GF5_seven_lower_numerator"])
        with self.assertRaises(ValueError):
            two_sided_source_certificate(
                self.m, self.f, self.g, max_motif_evaluations=1)
        with self.assertRaises(ValueError):
            two_sided_source_certificate(
                self.m, self.f, self.g, max_joint_maps=35)
        with self.assertRaises(ValueError):
            two_sided_source_certificate(
                self.m, self.f, {0: 0})
        with self.assertRaises(ValueError):
            two_sided_source_certificate(
                self.m, {0: 0, 1: 0}, self.g)
        with self.assertRaises(ValueError):
            two_sided_source_certificate(
                self.m, self.f, self.g, max_free_left=-1)


if __name__ == "__main__":
    unittest.main()
