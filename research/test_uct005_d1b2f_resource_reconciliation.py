"""Independent D1-B2-F witness gates: same F1 parity, cost, missing axes."""
import itertools
import unittest
from collections import Counter
from types import SimpleNamespace

from uct005_d1b2f_resource_reconciliation import (
    ALIASES, MODELS, PAGE_API, PRICE_AXES, SERVICE, STATUS, reconcile,
    SOURCE_COUNTERS, _audit_raw_sources,
)
from uct005_d1b2a_partial_pareto import candidate_dominates


class B2FCostLedgerTests(unittest.TestCase):
    def test_exhaustive_words_all_intervals_two_pin_epochs_three_gc(self):
        for n in range(1, 6):
            for bits in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    x = reconcile(n, p, bits, "all_intervals", legacy=False)
                    self.assertEqual(x["status"], STATUS)
                    self.assertEqual(x["root_novelty"], "OPEN_UNPROVED")
                    self.assertEqual(x["pareto"], "UNDECIDABLE_MISSING_AXES")
                    self.assertEqual(x["fully_priced_models"], 0)
                    self.assertEqual(x["workload"]["range_query_count_per_model"],
                                     4*n*(n+1)//2)
                    self.assertEqual(x["workload"]["GC_runs"], 3)
                    self.assertEqual(x["workload"]["PIN_epochs"],
                                     {"reader0":0, "reader1":2})
                    self.assertEqual(x["workload"]["no_op_epochs"], [2])
                    self.assertEqual({y["name"] for y in x["comparators"]},
                                     {z[0] for z in MODELS})
                    self.assertEqual(len(x["comparators"]), 3)
                    for row in x["comparators"]:
                        self.assertEqual(row["cost_model"], PAGE_API)
                        self.assertEqual(row["service"], SERVICE)
                        self.assertEqual(set(row["costs"]), set(PRICE_AXES))
                        self.assertEqual(set(row["audit"]["sources"]) |
                                         set(row["audit"]["unknown_reasons"]),
                                         set(PRICE_AXES))
                        self.assertEqual(set(row["observed"]), set(ALIASES))
                        self.assertTrue(all(type(value) is int and value >= 0
                                            for value in row["observed"].values()))
                        self.assertEqual(row["status"], "PARTIAL_PRICING_NO_FULL_PARETO")
                        self.assertIsNone(row["costs"]["durability_barriers"])
                        self.assertIsNone(row["costs"]["trusted_bits"])
                        self.assertIsNone(row["costs"]["gc_remote_writes"])
                        self.assertIsNone(row["costs"]["verifier_work"])
                        self.assertGreater(row["observed"]["peak_trusted_bits_declared"], 0)
                        self.assertGreater(row["observed"]["authority_pin_page_writes"], 0)
                        self.assertGreater(row["observed"]["gc_remote_page_reads"], 0)
                        self.assertGreater(row["observed"]["gc_logical_pages_freed"], 0)
                        self.assertGreater(row["observed"]["query_reply_payload_bytes"], 0)
                        self.assertEqual(row["observed"]["set_remote_page_writes"] * p,
                                         row["observed"]["set_remote_upload_bytes"])
                    for a in x["comparators"]:
                        for b in x["comparators"]:
                            self.assertIsNone(candidate_dominates(a, b))

    def test_replica_and_tree_are_explicitly_unpriced(self):
        for n,p in ((1,1),(5,2),(33,64)):
            x = reconcile(n,p,profile="representative",legacy=True)
            self.assertEqual(len(x["comparators"]), 5)
            s, cow, seg, tree, replica = x["comparators"]
            self.assertEqual(s["name"], "S_BYTE_SNAPSHOT")
            self.assertEqual(tree["name"], "T_IMMUTABLE_AUTHENTICATED_TREE")
            self.assertEqual(replica["name"], "R_FULL_TRUSTED_REPLICA_AND_LOG")
            self.assertEqual(tree["status"], "LEGACY_LOGICAL_ONLY_NOT_PAGE_PRICED")
            self.assertEqual(replica["status"], "LEGACY_LOGICAL_ONLY_NOT_PAGE_PRICED")
            for legacy_row in (tree, replica):
                self.assertEqual(set(legacy_row["costs"]), set(PRICE_AXES))
                self.assertTrue(all(v is None for v in legacy_row["costs"].values()))
                self.assertEqual(set(legacy_row["audit"]["unknown_reasons"]), set(PRICE_AXES))
                self.assertEqual(legacy_row["observed"], {})
                self.assertEqual(legacy_row["service"], "LEGACY_B2A_LOGICAL_TRACE_WITH_CATCHUP")
                self.assertIs(legacy_row["audit"]["operation_trace_identical"], False)
                self.assertNotEqual(legacy_row["service"], s["service"])
                self.assertIsNone(candidate_dominates(seg, legacy_row))
                self.assertIsNone(candidate_dominates(legacy_row, s))
            self.assertEqual(x["workload"]["range_query_count_per_model"],
                             4*len(x["workload"]["ranges"]))

    def test_known_write_coordinate_win_and_loss_are_not_full_pareto(self):
        # n=257,P=1: unsegmented full bitmap rewrite > segmented.
        x = reconcile(257,1,profile="representative",legacy=False)
        writes = x["remote_SET_page_writes"]
        self.assertLess(writes["T_SEGMENTED_BITMAP_COW"],
                        writes["T_GLOBAL_BITMAP_COW"])
        self.assertGreater(writes["T_SEGMENTED_BITMAP_COW"],
                           writes["S_BYTE_SNAPSHOT"])
        self.assertEqual(x["pareto"], "UNDECIDABLE_MISSING_AXES")
        # Larger records cost at least full node pages: no 1-bit per-node
        # shortcut or speculative dominance.
        for row in x["comparators"]:
            self.assertIsNone(row["costs"]["durability_barriers"])
            self.assertIsNone(row["costs"]["setup_bytes"])

    def test_missing_axis_cannot_be_zero_filled_or_promoted(self):
        x = reconcile(5,2,profile="all_intervals",legacy=False)
        rows = x["comparators"]
        for r in rows:
            self.assertIsNone(candidate_dominates(r,r))
            self.assertEqual(r["audit"]["sources"]["set_remote_page_writes"],
                             "set_remote_page_writes")
            self.assertIn("trusted_bits",r["audit"]["unknown_reasons"])
            self.assertIn("anchor_bytes",r["audit"]["unknown_reasons"])
        with self.assertRaises(ValueError):
            reconcile(0,2)
        with self.assertRaises(ValueError):
            reconcile(4,0)
        with self.assertRaises(ValueError):
            reconcile(4,2,(1,0,1))
        with self.assertRaises(ValueError):
            reconcile(4,2,(1,0,1,2))
        with self.assertRaises(ValueError):
            reconcile(4,2,profile="invented")

    def test_all_raw_counter_sources_are_explicit_and_replayable(self):
        x = reconcile(5, 2, profile="all_intervals", legacy=False)
        for row in x["comparators"]:
            name = row["name"]
            keys = row["audit"]["raw_counter_sources"]
            self.assertEqual(set(keys), set(ALIASES))
            self.assertEqual(keys,
                             {a:list(b) for a,b in SOURCE_COUNTERS[name].items()})
            for diagnostic, contributing_keys in keys.items():
                self.assertGreater(len(contributing_keys), 0)
                if contributing_keys == ["@trusted_bits"]:
                    self.assertEqual(row["observed"][diagnostic],
                                     row["observed"]["peak_trusted_bits_declared"])
                else:
                    self.assertTrue(all(k in row["source_ledger"]
                                        for k in contributing_keys))
                    self.assertEqual(
                        row["observed"][diagnostic],
                        sum(row["source_ledger"][k] for k in contributing_keys))
            self.assertLessEqual(row["observed"]["query_reply_payload_bytes"],
                                 row["observed"]["query_remote_page_reads"] * 2)

        snapshot = x["comparators"][0]
        forged = dict(snapshot["source_ledger"])
        forged.pop("set_full_page_writes")
        fake = SimpleNamespace(ledger=Counter(forged))
        with self.assertRaisesRegex(AssertionError, "missing explicitly charged"):
            _audit_raw_sources("S_BYTE_SNAPSHOT", fake, snapshot["observed"],
                               snapshot["observed"]["peak_trusted_bits_declared"])

    def test_legacy_not_claimed_on_nonmatching_query_set(self):
        x = reconcile(4,2,profile="all_intervals",legacy=True)
        # Legacy B2-A only executes the smaller representative range set.
        # It must not appear on an exhaustive trace that it never ran.
        self.assertEqual(len(x["comparators"]),3)
        self.assertEqual(x["workload"]["profile"],"all_intervals")


if __name__ == "__main__":
    unittest.main()
