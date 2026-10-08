"""Regression tests for TOM-001-C exact finite reference oracle."""

import unittest

from tom_certificate import (
    exact_min_labels,
    exhaustive_min_labels,
    input_states,
    labels_are_sufficient,
    minimum_extra_bits,
    response_profile,
    self_check,
)


class ExactCertificateTests(unittest.TestCase):
    def test_all_16_boolean_functions_match_exhaustive_labels(self):
        for table in range(16):
            with self.subTest(table=table):
                self.assertEqual(exact_min_labels(table, 2),
                                 exhaustive_min_labels(table, 2))

    def test_or_uses_three_metadata_labels(self):
        labels = exact_min_labels(0b1110, 2)
        self.assertEqual(labels, 3)
        self.assertEqual(minimum_extra_bits(labels), 2)

    def test_and_uses_three_metadata_labels(self):
        self.assertEqual(exact_min_labels(0b1000, 2), 3)

    def test_projection_and_constant_need_no_extra_bits(self):
        for table in (0b0000, 0b1111, 0b1100):
            self.assertEqual(exact_min_labels(table, 2), 1)
            self.assertEqual(minimum_extra_bits(exact_min_labels(table, 2)), 0)

    def test_distinct_profiles_same_output_cannot_share_label(self):
        states = input_states(2)
        # All states with a common old output are given the same label:
        # unsound for OR, as the future update response differs.
        labels = tuple((0b1110 >> (2 * x[0] + x[1])) & 1 for x in states)
        self.assertFalse(labels_are_sufficient(0b1110, states, labels))

    def test_response_profiles_cover_each_edit(self):
        p = response_profile(0b1110, (1, 0))
        self.assertEqual(p, (0, 1, 1, 1))
        self.assertEqual(len(p), 4)

    def test_invalid_dimensions_and_bit_counts(self):
        with self.assertRaises(ValueError):
            input_states(0)
        with self.assertRaises(ValueError):
            minimum_extra_bits(0)

    def test_cli_calibration(self):
        self.assertEqual(len(self_check()), 16)


if __name__ == "__main__":
    unittest.main()
