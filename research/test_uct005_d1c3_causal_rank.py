"""Independent D1-C3 causal GF(2) rank and full SET-execution falsifiers."""
import unittest
from itertools import product

from uct005_d1c3_causal_rank import (
    causal_rank, independent_answer_signatures, last_writer_row,
    rank_gf2, examples, report,
)


class CausalRankStopTests(unittest.TestCase):
    def test_fixed_examples_and_false_additive_cut(self):
        w = examples()
        a = w["duplicate_reader_PIN_same_epoch"]
        self.assertEqual(a["joint_rank"], 3)
        self.assertEqual(a["sum_individual_reader_ranks"], 6)
        b = w["unchanged_coordinate_across_many_epochs"]
        self.assertEqual(b["joint_rank"], 1)
        self.assertEqual(b["sum_individual_epoch_ranks"], 4)
        self.assertEqual(w["independently_hidden_historical_SET_payloads"]["joint_rank"], 4)
        self.assertEqual(w["charged_public_SET_payloads"]["joint_rank"], 1)
        self.assertEqual(w["last_writer_erases_prior_answer_dependency"]["joint_rank"], 1)

    def test_all_schedules_all_initial_and_SET_values_exhaustive(self):
        # Literal state-array simulation is independent of the XOR-row code.
        for n in range(1, 4):
            ranges = tuple((l, r) for l in range(n) for r in range(l + 1, n + 1))
            for H in range(4):
                for updates in product(range(n), repeat=H):
                    updates = tuple(updates)
                    # Every named half-open range at each epoch for reader0,
                    # and overlapping singleton/full-range observations for
                    # reader1. Includes repeated reads and no-op SET histories.
                    all0 = tuple((0, t, l, r) for t in range(H + 1)
                                 for l, r in ranges)
                    overlap = tuple((1, t, 0, n) for t in range(H + 1))
                    queries = all0 + overlap
                    for mask in range(1 << H):
                        public = tuple((t, t & 1) for t in range(H)
                                       if mask & (1 << t))
                        got = causal_rank(n, updates, queries, public)
                        actual = independent_answer_signatures(
                            n, updates, queries, public)
                        with self.subTest(n=n, updates=updates, public=public):
                            self.assertEqual(len(actual), got["answer_tuple_count"])
                            self.assertEqual(got["joint_rank"], len(actual).bit_length() - 1)
                            self.assertLessEqual(got["joint_rank"], n + H - len(public))
                            self.assertLessEqual(got["joint_rank"],
                                                 got["distinct_hidden_provenance_variables_used"])
                            self.assertLessEqual(got["joint_rank"],
                                                 got["sum_individual_reader_ranks"])
                            self.assertLessEqual(got["joint_rank"],
                                                 got["sum_individual_epoch_ranks"])
                            self.assertFalse(got["full_F1_joint_lower_proved"])

    def test_sparse_named_query_families_and_noop_are_not_conflated(self):
        for n in range(1, 4):
            for updates in product(range(n), repeat=3):
                updates = tuple(updates)
                q = tuple((j % 2, j, j % n, (j % n) + 1) for j in range(4))
                for known in ((), ((0, 0),), ((1, 1), (2, 0))):
                    a = causal_rank(n, updates, q, known)
                    self.assertEqual(
                        len(independent_answer_signatures(n, updates, q, known)),
                        a["answer_tuple_count"])
                # public SET values don't make epochs vanish: the historical
                # initial x remains secret until explicitly sent.
                all_public = ((0, 0), (1, 0), (2, 0))
                self.assertLessEqual(causal_rank(n, updates, q, all_public)["joint_rank"], n)

    def test_overwritten_old_symbols_do_not_reappear(self):
        r = last_writer_row(2, (0, 1, 0), 3, 0, 2)
        # Last writer of coord0 is b2 at index 4; coord1 is b1 at index3.
        self.assertEqual(r, (1 << 4) | (1 << 3))
        self.assertEqual(rank_gf2((3, 5, 6)), 2)
        self.assertEqual(rank_gf2((3, 3, 0)), 1)

    def test_reject_bad_contract_inputs_and_boolean_lookalikes(self):
        cases = (
            (0, (), (), ()),
            (True, (), (), ()),
            (2, (2,), (), ()),
            (2, (True,), (), ()),
            (2, (), ((0, 1, 0, 1),), ()),
            (2, (), ((2, 0, 0, 1),), ()),
            (2, (), ((0, 0, 1, 1),), ()),
            (2, (), ((0, 0, 0, 3),), ()),
            (2, (0,), (), ((0, 0), (0, 1))),
            (2, (0,), (), ((1, 1),)),
            (2, (0,), (), ((0, True),)),
        )
        for args in cases:
            with self.subTest(args=args), self.assertRaises(ValueError):
                causal_rank(*args)
        with self.assertRaises(ValueError):
            rank_gf2((-1,))
        with self.assertRaises(ValueError):
            last_writer_row(2, (0,), 2, 0, 1)
        with self.assertRaises(ValueError):
            independent_answer_signatures(8, (0, 0, 0), ((0, 0, 0, 1),))

    def test_no_source_or_original_root_promoted(self):
        z = report()
        self.assertEqual(z["root_novelty"], "OPEN_UNPROVED")
        self.assertIsNone(z["same_F1_nonfactorizing_theorem"])
        self.assertIsNone(z["joint_F1_page_write_or_query_lower"])
        self.assertIsNone(z["hard_adaptive_distribution"])
        self.assertFalse(z["full_primary_theorem_model_transfer"])
        self.assertTrue(z["classical_rank_counting_not_original"])
        self.assertTrue(all(value is None for value in
                            z["charged_F1_resource_axes_not_derived"].values()))


if __name__ == "__main__":
    unittest.main()
