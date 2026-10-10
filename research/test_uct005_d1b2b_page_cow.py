"""D1-B2-B independently audited page-image, history, adversarial and GC tests."""
import itertools
import unittest

from uct005_d1b2b_page_cow import (
    ANCHOR_BYTES, NODE, NODE_BYTES, ROOT_BYTES, PIN_RECORD_BYTES,
    Abort, PageCowTree, ROOT, _ceil, _decode, _encode,
)


class B2BPageCowTests(unittest.TestCase):
    def test_frozen_wire_fields_and_byte_conservation(self):
        self.assertEqual(NODE.size, 90)
        self.assertEqual(NODE_BYTES, 122)
        self.assertEqual(ROOT_BYTES, 48)
        self.assertEqual(ANCHOR_BYTES, 40)
        self.assertEqual(PIN_RECORD_BYTES, 41)
        with self.assertRaises(Abort):
            _decode(bytes(NODE_BYTES))
        with self.assertRaises(Abort):
            _decode(_encode(0, 1, 0)[:-1])
        with self.assertRaises(ValueError):
            _encode(0, 2**32, 0)
        for p in (1, 2, 64, 4096):
            for n in (1, 2, 3, 8, 33):
                t = PageCowTree((0,) * n, p)
                records = 2 * n - 1
                self.assertEqual(t.node_pages, (122 + p - 1) // p)
                self.assertEqual(t.root_pages, (48 + p - 1) // p)
                self.assertEqual(len(t.nodes), records)
                self.assertEqual(t.ledger["setup_node_page_writes"],
                                 records * t.node_pages)
                self.assertEqual(t.ledger["setup_root_page_writes"], t.root_pages)
                self.assertEqual(t.ledger["setup_remote_upload_bytes"],
                                 (records * t.node_pages + t.root_pages) * p)
                self.assertEqual(t.remote_pages,
                                 records * t.node_pages + t.root_pages +
                                 t.bitmap_pages)
                self.assertEqual(t.nodes[1][-32:], _decode(t.nodes[1])["digest"])
                self.assertNotIn("writer_bits", t.__dict__)
                self.assertNotIn("trusted_history", t.__dict__)
                self.assertNotIn("root_directory", t.__dict__)
                self.assertGreaterEqual(t.trusted_bits, 8*ANCHOR_BYTES)

    def test_exhaustive_two_independent_readers_all_ranges_and_noop(self):
        for n in range(1, 7):
            for state in itertools.product((0, 1), repeat=n):
                t = PageCowTree(state, 1 + n % 3)
                p0 = t.pin_current(0)
                old0 = tuple(state)
                words = [old0]
                # toggle bit 0; explicit same-bit no-op; toggle n-1
                for pos, nextbit in (
                    (0, state[0] ^ 1),
                    (min(1, n - 1), None),
                    (n - 1, None),
                ):
                    b = list(words[-1])
                    if nextbit is None and len(words) == 2:
                        nextbit = b[pos]  # enforce epoch-2 no-op
                    if nextbit is None:
                        nextbit = b[pos] ^ 1
                    b[pos] = nextbit
                    words.append(tuple(b))
                    self.assertEqual(t.set(pos, nextbit), len(words) - 1)
                    if len(words) == 3:
                        p2 = t.pin_current(1)
                self.assertEqual(p0, 0)
                self.assertEqual(p2, 2)
                self.assertEqual(t.ledger["set_changed_logical_bits"], 2)
                self.assertEqual(t.ledger["set_anchor_publications"], 3)
                self.assertEqual(len(t.roots), 4)
                for left in range(n):
                    for right in range(left + 1, n + 1):
                        for reader in (0, 1):
                            self.assertEqual(t.query(reader, left, right),
                                             sum(words[3][left:right]) & 1)
                        self.assertEqual(t.query(0, left, right, as_of=0),
                                         sum(words[0][left:right]) & 1)
                        self.assertEqual(t.query(1, left, right, as_of=2),
                                         sum(words[2][left:right]) & 1)
                self.assertGreater(t.ledger["query_node_page_reads"], 0)
                self.assertGreater(t.ledger["query_root_page_reads"], 0)
                self.assertGreater(t.ledger["query_proof_payload_bytes"], 0)
                self.assertGreater(t.ledger["anchor_read_calls"], 0)
                self.assertEqual(t.gc() > 0, True)
                self.assertEqual(set(t.roots), {0, 2, 3})
                self.assertEqual(t.query(0, 0, n, as_of=0),
                                 sum(words[0]) & 1)
                self.assertEqual(t.query(1, 0, n, as_of=2),
                                 sum(words[2]) & 1)
                t.unpin(0, 0)
                t.gc()
                self.assertEqual(set(t.roots), {2, 3})
                with self.assertRaises(Abort):
                    t.query(0, 0, n, as_of=0)
                t.unpin(1, 2)
                t.gc()
                self.assertEqual(set(t.roots), {3})
                with self.assertRaises(Abort):
                    t.query(1, 0, n, as_of=2)
                self.assertEqual(t.query(1, 0, n), sum(words[3]) & 1)
                self.assertGreater(t.ledger["gc_node_slot_scan_page_reads"], 0)
                self.assertGreater(t.ledger["gc_root_slot_scan_page_reads"], 0)
                self.assertGreater(t.ledger["gc_bitmap_page_writes"], 0)

    def test_manifest_tampering_node_omission_and_noncanonical_proof(self):
        t = PageCowTree((1, 0, 0, 1, 0), 2)
        self.assertEqual(t.pin_current(0), 0)
        manifest, records = t.make_proof(0, 1, 4)
        self.assertEqual(t.query(0, 1, 4, as_of=0, presented_root=manifest,
                                 presented_records=records), 1)
        bad = bytearray(manifest)
        bad[-1] ^= 1
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_root=bytes(bad),
                    presented_records=records)
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_root=manifest[:-1],
                    presented_records=records)
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_root=manifest,
                    presented_records=records[:-1])
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_root=manifest,
                    presented_records=records + (records[0],))
        badnode = bytearray(records[0])
        badnode[20] ^= 8
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_root=manifest,
                    presented_records=(bytes(badnode),) + records[1:])
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_records=(records[0],))
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_records=("not bytes",))
        with self.assertRaises(Abort):
            t.query(0, 1, 4, as_of=0, presented_epoch=1)
        with self.assertRaises(Abort):
            t.query(1, 0, 5, as_of=0)
        with self.assertRaises(Abort):
            t.query(0, 0, 5, anchor_available=False)
        root_id = ROOT.unpack(t.roots[0])[1]
        original = t.nodes[root_id]
        t.nodes[root_id] = original[:-1]  # Byzantine storage corruption
        with self.assertRaises(Abort):
            t.query(0, 0, 5)
        with self.assertRaises(Abort):
            t.gc()  # all-or-nothing: corruption must not delete live data
        self.assertEqual(len(t.roots), 1)
        t.nodes[root_id] = original
        self.assertEqual(t.query(0, 0, 5), 0)
        t.nodes.pop(root_id)
        with self.assertRaises(Abort):
            t.query(0, 0, 5)

    def test_latest_anchor_replay_pin_race_and_cost_separation(self):
        t = PageCowTree((0, 1, 0), 1)
        old = t.roots[0]
        generation_before = t.generation
        t.pin_current(0)
        with self.assertRaises(Abort):
            t.gc(expected_generation=generation_before)
        e = t.set(1, 1)  # no-op; epoch still increments
        self.assertEqual(e, 1)
        self.assertEqual(t.ledger["set_changed_logical_bits"], 0)
        with self.assertRaises(Abort):
            t.query(0, 0, 3, presented_root=old)
        with self.assertRaises(Abort):
            t.query(0, 0, 3, presented_epoch=0)
        self.assertEqual(t.query(0, 0, 3, as_of=0), 1)
        with self.assertRaises(Abort):
            t.gc(expected_generation=generation_before)
        before_remote = t.ledger["set_node_page_writes"]
        before_authority = t.ledger["authority_pin_page_writes"]
        t.pin_current(1)
        self.assertEqual(t.ledger["set_node_page_writes"], before_remote)
        self.assertEqual(t.ledger["authority_pin_page_writes"],
                         before_authority + _ceil(PIN_RECORD_BYTES, 1))
        self.assertEqual(t.trusted_bits, 8 * (40 + 32 + 2*40 + 2*41))
        with self.assertRaises(ValueError):
            t.unpin(1, 0)
        for bit in (True, -1, 2):
            with self.assertRaises(ValueError):
                t.set(0, bit)


if __name__ == "__main__":
    unittest.main()
