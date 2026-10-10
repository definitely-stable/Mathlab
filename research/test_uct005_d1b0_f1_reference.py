"""Independent exhaustive F1-B0 logic and negative tests; not security proofs."""
import itertools
import unittest

from uct005_d1b0_f1_reference import (
    Abort, REQUIRED_COSTS, SnapshotF1Reference, validate_contract,
)


class F1D1B0Tests(unittest.TestCase):
    def test_contract_cost_units_and_no_free_freshness(self):
        contract = validate_contract()
        self.assertEqual(set(contract["coordinates"]), REQUIRED_COSTS)
        self.assertEqual(contract["root_novelty"], "OPEN_UNPROVED")
        self.assertEqual(contract["reader"]["count"], 2)
        self.assertTrue(contract["reader"]["independent_persistent_state"])
        self.assertTrue(contract["set"]["noop_creates_epoch"])
        self.assertTrue(contract["pin_gc"]["retention"].startswith("latest"))
        self.assertTrue(contract["adversary"]["abort_on_withholding"])
        self.assertEqual(contract["interval"]["representation"], "half-open [l,r)")
        self.assertIn("STATIC", "STATIC")  # no inferred prior-art dynamic reduction

    def test_exhaustive_two_offline_readers_full_snapshot_upper(self):
        for n in range(1, 5):
            for bits in itertools.product((0, 1), repeat=n):
                for pos in range(n):
                    for new_bit in (0, 1):  # includes mandatory epoch no-op
                        m = SnapshotF1Reference(bits, page_bytes=2)
                        epoch0 = m.pin_current(0)
                        epoch1 = m.set(pos, new_bit)
                        self.assertEqual((epoch0, epoch1), (0, 1))
                        m.pin_current(1)
                        now = list(bits)
                        now[pos] = new_bit
                        self.assertNotEqual(
                            m.readers[0][epoch0], m.readers[1][epoch1],
                            "no-op must bind epoch as well as state",
                        )
                        self.assertGreater(m.trusted_bits, n)
                        m.gc()
                        self.assertIn(0, m.remote, "offline PIN must be retained")
                        self.assertIn(1, m.remote, "LATEST must be retained")
                        for a in range(n):
                            for b in range(a + 1, n + 1):
                                self.assertEqual(m.as_of(0, 0, a, b),
                                                 sum(bits[a:b]) & 1)
                                self.assertEqual(m.latest(1, a, b),
                                                 sum(now[a:b]) & 1)
                                self.assertEqual(m.as_of(1, 1, a, b),
                                                 sum(now[a:b]) & 1)
                        self.assertGreater(m.ledger["anchor_read_calls"], 0)
                        self.assertGreater(m.ledger["query_full_page_reads"], 0)
                        self.assertGreater(m.ledger["query_remote_payload_bytes"], 0)

    def test_replay_tamper_missing_history_and_two_pin_gc(self):
        m = SnapshotF1Reference((0, 1, 1, 0), page_bytes=1)
        e0 = m.pin_current(0)
        m.pin_current(1)
        m.set(3, 1)
        e1 = m.pin_current(0)
        self.assertEqual((e0, e1), (0, 1))
        self.assertRaises(Abort, m.latest, 0, 0, 4,
                          presented_epoch=0)
        self.assertRaises(Abort, m.as_of, 1, 0, 0, 4,
                          presented_epoch=1)
        self.assertRaises(Abort, m.latest, 0, 0, 4,
                          presented=b"\xff")
        self.assertRaises(Abort, m.latest, 0, 0, 4,
                          presented=b"\x00")
        self.assertRaises(Abort, m.as_of, 1, 1, 0, 4)
        m.unpin(0, e0)
        self.assertEqual(m.gc(), 0, "reader 1 still pins epoch zero")
        self.assertEqual(m.as_of(1, 0, 0, 4), 0)
        m.unpin(1, e0)
        self.assertGreater(m.gc(), 0, "now the unpinned obsolete epoch can go")
        self.assertRaises(Abort, m.as_of, 1, 0, 0, 4)
        self.assertEqual(m.as_of(0, e1, 0, 4), 1)
        self.assertIn(e1, m.remote)

    def test_charged_snapshot_and_noop_epoch(self):
        m = SnapshotF1Reference((0,) * 33, page_bytes=2)
        # ceil(5 bytes/2)=3 data pages + one entire manifest page
        self.assertEqual(m.remote_pages, 4)
        self.assertEqual(m.ledger["setup_full_page_writes"], 4)
        t0 = m.pin_current(0)
        old_hash = m.latest_root
        t1 = m.set(15, 0)
        self.assertEqual((t0, t1), (0, 1))
        self.assertNotEqual(m.latest_root, old_hash)
        self.assertEqual(m.ledger["set_changed_logical_bits"], 0)
        self.assertEqual(m.ledger["set_full_page_writes"], 4)
        self.assertEqual(m.ledger["set_full_page_reads"], 0)
        self.assertEqual(m.ledger["anchor_publication_bytes"], 40)
        self.assertEqual(m.ledger["anchor_read_request_bytes"], 1)
        self.assertEqual(m.ledger["anchor_read_response_bytes"], 40)
        self.assertEqual(m.remote_pages, 8)
        self.assertEqual(m.retained_pinned_pages, 4)
        self.assertGreaterEqual(m.trusted_bits, 33 + 40 * 8)
        self.assertRaises(ValueError, m.latest, 2, 0, 1)
        self.assertRaises(ValueError, m.pin_current, 2)
        self.assertRaises(ValueError, m.set, -1, 0)
        self.assertRaises(ValueError, m.as_of, 0, 0, 1, 1)


if __name__ == "__main__":
    unittest.main()
