"""Independent finite validation for D1-B2-E, not a novel lower-bound proof."""
import itertools
import unittest

from uct005_d1b2e_total_pin_budget import (
    UNKNOWN_RESOURCE_AXES,
    complete_audit_gate, independent_member_lookup_countermodel,
    identical_f1_budget_witness, persistent_budget_filter,
    projection_signature,
)


class FullAuditClassicalGateTests(unittest.TestCase):
    def test_independent_full_vector_projection_oracle_h_le_8(self):
        # Independent enum of vectors and visible trusted/remote coordinates.
        for h in range(9):
            words = tuple(itertools.product((0, 1), repeat=h))
            for trusted in range(h + 2):
                for response in range(h + 2):
                    signatures = {
                        (word[:trusted], word[trusted:trusted + response])
                        for word in words
                    }
                    result = complete_audit_gate(h, trusted, response)
                    self.assertEqual(len(signatures), result["distinct_state_transcripts"])
                    self.assertEqual(result["membership_vectors"], 1 << h)
                    self.assertEqual(result["injective_full_audit"],
                                     trusted + response >= h)
                    if trusted + response < h:
                        witness = result["distinct_collision_witness"]
                        self.assertIsNotNone(witness)
                        left, right = tuple(witness["a"]), tuple(witness["b"])
                        self.assertNotEqual(left, right)
                        self.assertEqual(projection_signature(left, trusted, response),
                                         projection_signature(right, trusted, response))
                    else:
                        self.assertIsNone(result["distinct_collision_witness"])

    def test_variable_length_response_count_does_not_add_a_full_bit(self):
        # A length<=b remote binary transcript admits (2^(b+1)-1)
        # different strings, not 2^b; but cannot double the full-state
        # capacity and thus preserves the integer H<=s+b conclusion.
        for trusted in range(7):
            for max_reply_bits in range(7):
                replies = {
                    "".join(b)
                    for k in range(max_reply_bits + 1)
                    for b in itertools.product("01", repeat=k)
                }
                self.assertEqual(len(replies), (1 << (max_reply_bits + 1)) - 1)
                signatures = (1 << trusted) * len(replies)
                self.assertLess(signatures, 1 << (trusted + max_reply_bits + 1))
                self.assertGreaterEqual(signatures, 1 << (trusted + max_reply_bits))
                self.assertEqual(signatures.bit_length() - 1,
                                 trusted + max_reply_bits)

    def test_individual_member_query_refutes_false_full_vector_transfer(self):
        for h in range(2, 9):
            result = independent_member_lookup_countermodel(h)
            self.assertEqual(result["trusted_membership_bits"], 0)
            self.assertEqual(result["remote_bits_read_per_single_epoch_query"], 1)
            self.assertEqual(result["all_exact_queries_checked"], h * (1 << h))
            self.assertGreater(h, 1)

    def test_invalid_gate_parameters(self):
        for args in ((-1, 0, 0), (11, 0, 0), (1, -1, 0), (2, 1, -1)):
            with self.assertRaises(ValueError):
                complete_audit_gate(*args)
        with self.assertRaises(ValueError):
            independent_member_lookup_countermodel(1)
        with self.assertRaises(ValueError):
            projection_signature((0, 2), 1, 1)
        with self.assertRaises(ValueError):
            projection_signature((1, 0), -1, 1)


class PaidF1BudgetChecks(unittest.TestCase):
    def test_differential_all_small_initial_words_and_pages(self):
        for n in range(1, 6):
            for word in itertools.product((0, 1), repeat=n):
                for page in (1, 2, 64):
                    result = identical_f1_budget_witness(word, page, 8, 1600)
                    self.assertEqual(result["root_novelty"], "OPEN_UNPROVED")
                    self.assertEqual(result["epoch_count"], 3)
                    self.assertEqual(result["reader_pin_epochs"], [0, 2])
                    self.assertEqual(result["noop_epochs"], [2])
                    self.assertTrue(result["total_trusted_state_includes_both_reader_roots"])
                    self.assertEqual(result["full_pareto_judgment"],
                                     "FORBIDDEN_MISSING_RESOURCE_AND_SECURITY_AXES")
                    self.assertGreater(len(result["unknown_unpriced_axes"]), 3)
                    snapshot = (((n + 7) // 8 + page - 1) // page
                                + (48 + page - 1) // page)
                    bitmap = (((2 * 8 + 7) // 8 + page - 1) // page)
                    self.assertEqual(result["page001_snapshot_full_pages"], snapshot)
                    self.assertEqual(result["remote_bitmap_full_pages"], bitmap)
                    costs = result["known_axes_by_candidate"]
                    e = costs["E_TRUSTED_PIN_ENTRIES"]
                    r = costs["R_AUTH_REMOTE_BITMAP"]
                    self.assertEqual(e["remote_pages_with_three_live_versions"],
                                     3 * snapshot)
                    self.assertEqual(r["remote_pages_with_three_live_versions"],
                                     3 * snapshot + bitmap)
                    self.assertEqual(e["snapshot_set_full_page_writes"], 3 * snapshot)
                    self.assertEqual(r["snapshot_set_full_page_writes"], 3 * snapshot)
                    self.assertGreater(r["remote_bitmap_page_writes"], 0)
                    self.assertGreater(r["remote_bitmap_verifier_hashed_bytes"], 0)
                    self.assertGreater(e["trusted_authority_pin_record_page_reads"], 0)
                    self.assertEqual(r["remote_delete_request_bytes"],
                                     8 * r["remote_delete_page_calls"])
                    self.assertEqual(e["remote_delete_request_bytes"],
                                     8 * e["remote_delete_page_calls"])

    def test_exact_n33_p2_threshold_and_reader_roots(self):
        case = identical_f1_budget_witness((0,) * 33, 2, 8, 1600)
        costs = case["known_axes_by_candidate"]
        r = costs["R_AUTH_REMOTE_BITMAP"]
        e = costs["E_TRUSTED_PIN_ENTRIES"]
        self.assertEqual(case["page001_snapshot_full_pages"], 27)
        self.assertEqual(case["remote_bitmap_full_pages"], 1)
        self.assertEqual(r["remote_pages_with_three_live_versions"], 82)
        self.assertEqual(e["remote_pages_with_three_live_versions"], 81)
        self.assertEqual(r["trusted_bits_with_two_active_pins"], 1313)
        self.assertEqual(e["trusted_bits_with_two_active_pins"], 1649)
        self.assertEqual(r["persistent_trusted_peak_bits"], 1313)
        self.assertEqual(e["persistent_trusted_peak_bits"], 1649)
        self.assertEqual(case["within_modeled_persistent_trust_budget"],
                         {"R_AUTH_REMOTE_BITMAP": True,
                          "E_TRUSTED_PIN_ENTRIES": False})
        for cap, expected in (
            (1312, (False, False)),
            (1313, (True, False)),
            (1648, (True, False)),
            (1649, (True, True)),
        ):
            got = persistent_budget_filter(
                {"R": r["persistent_trusted_peak_bits"],
                 "E": e["persistent_trusted_peak_bits"]},
                cap)
            self.assertEqual((got["R"], got["E"]), expected)
        # If reader-held independent roots were silently omitted, the remote
        # candidate would be understated by exactly 80 bytes = 640 bits.
        self.assertEqual(r["persistent_trusted_peak_bits"] -
                         (33 + 40 * 8 + 40 * 8), 80 * 8)

    def test_fail_closed_unpriced_axes_and_invalid_budget(self):
        self.assertIn("transient_trusted_scratch_peak_bytes", UNKNOWN_RESOURCE_AXES)
        self.assertIn("security_assumption_uniform_asymptotics", UNKNOWN_RESOURCE_AXES)
        for bad in (-1, 1.0, True):
            with self.assertRaises(ValueError):
                persistent_budget_filter({"A": 10}, bad)
        for wrong in ({}, {"A": -1}, {"A": None}, {"A": True}):
            with self.assertRaises(ValueError):
                persistent_budget_filter(wrong, 10)
        with self.assertRaises(ValueError):
            identical_f1_budget_witness((0, 1), 2, epoch_capacity=3)
        with self.assertRaises(ValueError):
            identical_f1_budget_witness((0, 1), 0)
        with self.assertRaises(ValueError):
            identical_f1_budget_witness((0, 2), 1)


if __name__ == "__main__":
    unittest.main()
