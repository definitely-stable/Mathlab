"""DAG-002 G2-B2-C1: exact paid store, manifest restart and memory limit."""
import unittest

from dag002_g2b2c1_billed_updater import (
    BilledPowerUpdater, _manifest_decode, _manifest_encode, census_four,
)
from dag002_g2b2_felsner import source_dfs


class FullyBilledLogicalTests(unittest.TestCase):
    def test_all_four_node_dags(self):
        r = census_four()
        self.assertEqual(r["traces"], 128)
        self.assertEqual(r["query_instances"], 128 * 30)

    def test_reopen_from_only_serialized_pages_no_cached_updater_state(self):
        trace = ((), (), (0,), (1,), (2, 3), (0, 1, 4))
        a = BilledPowerUpdater(8, 64)
        for p in trace[:4]:
            a.append(p)
        store = a.store
        b = BilledPowerUpdater(8, 64, store=store)
        for p in trace[4:]:
            b.append(p)
        self.assertEqual(b.report()["vertices"], len(trace))
        for u in range(len(trace)):
            for v in range(len(trace)):
                got, _ = b.query(u, v)
                self.assertEqual(got, source_dfs(trace, u, v))
        self.assertFalse(b.report()["cap_on_actual_process_rss"])
        self.assertTrue(b.report()["backing_store_in_process_memory"])

    def test_charged_reads_include_manifest_support_and_old_labels(self):
        db = BilledPowerUpdater(16, 16)
        first = db.append(())
        self.assertEqual(first.read_pages, 0)
        second = db.append((0,))
        self.assertGreaterEqual(second.read_pages, 3)
        self.assertGreater(db.store.read_address_bytes, 0)
        self.assertGreater(db.store.write_pages, 4)
        before = db.store.read_pages
        db.query(0, 1)
        self.assertGreater(db.store.read_pages, before)

    def test_low_logical_scratch_cap_fails_before_publication(self):
        db = BilledPowerUpdater(16, 64, modeled_scratch_cap=1)
        before = dict(db.store.images)
        with self.assertRaises(MemoryError):
            db.append(())
        self.assertEqual(db.store.images, before)
        with self.assertRaises(ValueError):
            BilledPowerUpdater(16, 64, base=1)

    def test_manifest_validator_rejects_duplicate_and_truncation(self):
        raw = _manifest_encode(2, [0, 1], [[0], [1]])
        self.assertEqual(_manifest_decode(raw), (2, [0, 1], [[0], [1]]))
        for invalid in (raw[:-1], raw + b"\0", b"\0" * 3):
            with self.assertRaises(ValueError):
                _manifest_decode(invalid)
        duplicate = _manifest_encode(2, [0, 1], [[0], [0]])
        with self.assertRaises(ValueError):
            _manifest_decode(duplicate)

    def test_pages_sources_immutable_and_no_mutable_previous_arrays(self):
        db = BilledPowerUpdater(10, 64)
        trace = ((), (), (0,), (0, 1), (3,))
        for p in trace:
            frozen = {key: value for key, value in db.store.images.items()
                      if key in db.store.immutable}
            db.append(p)
            for key, value in frozen.items():
                self.assertEqual(db.store.images[key], value)
        self.assertNotIn("parents", db.__dict__)
        self.assertNotIn("partition", db.__dict__)
        self.assertNotIn("labels", db.__dict__)
        self.assertEqual(db.report()["vertices"], len(trace))


if __name__ == "__main__":
    unittest.main()
