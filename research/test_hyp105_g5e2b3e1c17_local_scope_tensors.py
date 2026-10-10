"""C17 independent source-changing local support tensor proof tests."""
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, seven_census,
)
from hyp105_g5e2b3e1c14_domain_certificates import (
    _completion_pairs, _filled_model,
)
from hyp105_g5e2b3e1c16_two_sided_source import (
    two_sided_source_certificate,
)
from hyp105_g5e2b3e1c17_local_scope_tensors import (
    local_scope_sixset_certificate,
)


class C17LocalScopeTensorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = pair_labeled_symplectic(1, "reverse-line")
        cls.f = {i: PAIRS.index(cls.m["left_labels"][i]) for i in range(12)}
        cls.g = {i: PAIRS.index(cls.m["right_labels"][i]) for i in range(12)}

    def _compare_to_independent_C16(self, f, g, max_joint=36):
        local = local_scope_sixset_certificate(self.m, f, g)
        global_cert = two_sided_source_certificate(
            self.m, f, g, max_joint_maps=max_joint)
        for a, b in (
            ("C15_shared_eligible_left_S", "C15_eligible_one_right_lower_S"),
            ("C17_local_two_sided_signature_S_lower",
             "C16_two_sided_signature_lower_S"),
            ("C15_shared_eligible_left_GF5_numerator",
             "C15_eligible_one_right_lower_GF5_numerator"),
            ("C17_local_two_sided_signature_GF5_numerator_lower",
             "C16_two_sided_signature_lower_GF5_numerator"),
        ):
            self.assertEqual(local[a], global_cert[b], (a, b))
        self.assertLessEqual(
            local["C17_local_two_sided_signature_S_lower"],
            global_cert["C16_exact_joint_box_lower_S"])
        self.assertLessEqual(
            local["C17_local_two_sided_signature_GF5_numerator_lower"],
            global_cert["C16_exact_joint_box_lower_GF5_numerator"])
        self.assertFalse(local["full_joint_completion_score_matrix_allocated"])
        return local

    def test_actual_original_W32_36_map_same_motif_signature_lower(self):
        x = self._compare_to_independent_C16(self.f, self.g)
        self.assertEqual(x["candidate_source_instances"], 62370 * 6)
        self.assertGreater(
            x["distinct_original_sixsets_in_source_union"], 62370)
        self.assertEqual(x["C15_shared_eligible_left_S"], 12)
        self.assertEqual(x["C15_shared_eligible_left_GF5_numerator"], 513393)
        self.assertGreater(
            x["C17_local_two_sided_signature_S_lower"], 0)
        self.assertGreater(x["actual_local_motif_classifications"], 0)
        self.assertEqual(
            sum(row["original_distinct_sixsets"]
                for row in x["local_signature_census"]),
            x["distinct_original_sixsets_in_source_union"])

    def test_genuine_nonprefix_original_4_map_adversary(self):
        f = {i: PAIRS.index(e)
             for i, e in enumerate(self.m["left_labels"]) if i not in (1, 13)}
        g = {i: PAIRS.index(e)
             for i, e in enumerate(self.m["right_labels"]) if i not in (0, 12)}
        x = self._compare_to_independent_C16(f, g, max_joint=4)
        self.assertEqual(x["candidate_source_instances"], 2 * 62370)

    def test_off_support_filler_is_not_a_witness(self):
        # Conditional class of a *fixed ORIGINAL J* cannot depend on
        # physical pair images of original points/lines absent from J.
        maps = list(_completion_pairs(self.m, self.f, self.g, 36))
        j = (0, 1, 2, 3, 4, 5)  # six distinct genuine original incidences
        inc = self.m["incidences"]
        u = {inc[e][0] for e in j if inc[e][0] not in self.f}
        v = {inc[e][1] for e in j if inc[e][1] not in self.g}
        by_scope = {}
        for f, g in maps:
            full = _filled_model(self.m, f, g)
            scope = (tuple(f[i] for i in sorted(u)),
                     tuple(g[i] for i in sorted(v)))
            tag = classify_seven_prechecked(
                j, full["left_labels"], full["right_labels"], inc)
            if scope in by_scope:
                self.assertEqual(by_scope[scope], tag)
            else:
                by_scope[scope] = tag

    def test_both_sides_fully_fixed_matches_true_seven_census(self):
        f = {i: PAIRS.index(e) for i, e in enumerate(self.m["left_labels"])}
        g = {i: PAIRS.index(e) for i, e in enumerate(self.m["right_labels"])}
        x = local_scope_sixset_certificate(self.m, f, g)
        actual = seven_census(self.m, independent_checks=False)
        self.assertEqual(
            x["C17_local_two_sided_signature_S_lower"], actual["S_seven"])
        self.assertEqual(
            x["C17_local_two_sided_signature_GF5_numerator_lower"],
            actual["GF5_seven_lower_numerator"])
        self.assertEqual(x["candidate_source_instances"], 62370)

    def test_bounds_fail_closed_before_claiming_truncated_certificates(self):
        with self.assertRaises(ValueError):
            local_scope_sixset_certificate(
                self.m, self.f, self.g, max_missing_right=2)
        with self.assertRaises(ValueError):
            local_scope_sixset_certificate(
                self.m, self.f, self.g, max_left_source_templates=5)
        with self.assertRaises(ValueError):
            local_scope_sixset_certificate(
                self.m, self.f, self.g, max_source_candidates=1000)
        with self.assertRaises(ValueError):
            local_scope_sixset_certificate(
                self.m, self.f, self.g, max_local_classifications=1)
        with self.assertRaises(ValueError):
            local_scope_sixset_certificate(
                self.m, {0: 0, 1: 0}, self.g)


if __name__ == "__main__":
    unittest.main()
