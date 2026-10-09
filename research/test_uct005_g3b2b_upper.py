"""UCT-005 G3-B2-B independent small-state and Byzantine transcript oracles."""
import itertools
import json
import unittest
from math import ceil, log2

from uct005_g3b2b_range_tree import (
    AnchorValue, Reader, TreeWriter, checked_query, query_writer,
)
from uct005_g3b2b_baselines import (
    SnapshotWriter, ReplicaWriter, ReplicaReader, snapshot_query, replica_query,
)


def direct_range(bits, left, right):
    """Independent reference, no authenticated-tree implementation reused."""
    parity = 0
    for i in range(left, right + 1):
        if bits[i]:
            parity = 1 - parity
    return parity


def tamper_first_frontier(piece):
    if piece["t"] == "c":
        piece["p"] = 1 - piece["p"]
    else:
        tamper_first_frontier(piece["l"])


def canonical(message):
    return json.dumps(message, separators=(",", ":"), sort_keys=True).encode("ascii")


class G3B2BUpperFrontierTests(unittest.TestCase):
    def test_exhaustive_one_epoch_all_initial_states_sets_ranges(self):
        examined = 0
        for n in (2, 3, 4):
            for original in itertools.product((0, 1), repeat=n):
                for index in range(n):
                    for assigned in (0, 1):
                        tree = TreeWriter(original)
                        full = SnapshotWriter(original)
                        replica = ReplicaWriter(original)
                        t_client = Reader(tree.epochs[0])
                        s_client = Reader(full.anchor)
                        r_client = ReplicaReader(original, replica.anchor)
                        tc = tree.set(index, assigned)
                        sc = full.set(index, assigned)
                        rc = replica.set(index, assigned)
                        expected_bits = list(original)
                        expected_bits[index] = assigned
                        expected_bits = tuple(expected_bits)
                        height = ceil(log2(n))
                        self.assertEqual(tc.remote_node_reads,
                                         tc.remote_node_writes)
                        self.assertGreaterEqual(tc.remote_node_writes, 2)
                        self.assertLessEqual(tc.remote_node_writes, height + 1)
                        self.assertEqual(tc.hash_calls, 2 * tc.remote_node_writes)
                        self.assertEqual(tc.anchor_publication_bytes, 40)
                        self.assertEqual(sc["remote_bit_reads_for_hash"], n)
                        self.assertEqual(sc["remote_bit_writes"], 1)
                        self.assertEqual(rc["anchor_publication_bytes"], 40)
                        for a in range(n):
                            for b in range(a, n):
                                expect = direct_range(expected_bits, a, b)
                                t = query_writer(tree, t_client, 1, a, b)
                                s = snapshot_query(s_client, full, a, b)
                                r = replica_query(r_client, replica, a, b)
                                self.assertEqual((t.status, s.status, r.status),
                                                 ("ACCEPT", "ACCEPT", "ACCEPT"))
                                self.assertEqual((t.value, s.value, r.value),
                                                 (expect, expect, expect))
                                for result in (t, s, r):
                                    self.assertEqual(result.cost.anchor_calls, 1)
                                    self.assertEqual(result.cost.anchor_response_bytes, 40)
                                    self.assertEqual(result.cost.anchor_request_bytes, 1)
                                    self.assertGreater(result.cost.untrusted_response_bytes, 0)
                                    self.assertGreater(result.cost.untrusted_request_bytes, 0)
                                self.assertEqual(t.cost.trusted_checkpoint_bytes, 40)
                                self.assertEqual(s.cost.trusted_checkpoint_bytes, 40)
                                self.assertEqual(r.cost.trusted_checkpoint_bytes,
                                                 40 + (n + 7) // 8)
                                examined += 1
        self.assertGreater(examined, 1000)

    def test_server_replay_forks_stale_latest_and_anchor_outage(self):
        for n in (2, 3, 4):
            tree = TreeWriter((0,) * n)
            snapshot = SnapshotWriter((0,) * n)
            replica = ReplicaWriter((0,) * n)
            a, b = Reader(tree.epochs[0]), Reader(tree.epochs[0])
            s = Reader(snapshot.anchor)
            r = ReplicaReader((0,) * n, replica.anchor)
            tree.set(0, 1)
            snapshot.set(0, 1)
            replica.set(0, 1)
            self.assertEqual(query_writer(tree, a, 0, 0, 0).status,
                             "STALE_OR_EQUIVOCATING_ROOT")
            self.assertEqual(snapshot_query(s, snapshot, 0, 0, epoch=0).status,
                             "STALE_OR_EQUIVOCATING_ROOT")
            self.assertEqual(replica_query(r, replica, 0, 0,
                             response=replica.serve(1)).status,
                             "STALE_OR_EQUIVOCATING_LOG")
            self.assertEqual(query_writer(tree, a, 1, 0, 0).value, 1)
            self.assertEqual(query_writer(tree, b, 1, 0, 0).status, "ACCEPT")
            tree.set(0, 0)
            snapshot.set(0, 0)
            replica.set(0, 0)
            self.assertEqual(query_writer(tree, a, 1, 0, 0).status,
                             "STALE_OR_EQUIVOCATING_ROOT")
            self.assertEqual(snapshot_query(s, snapshot, 0, 0,
                             epoch=1).status, "STALE_OR_EQUIVOCATING_ROOT")
            self.assertEqual(query_writer(tree, a, 2, 0, 0,
                             anchor_available=False).status, "NO_TRUSTED_ANCHOR")
            self.assertEqual(snapshot_query(s, snapshot, 0, 0,
                             anchor_available=False).status, "NO_TRUSTED_ANCHOR")
            self.assertEqual(replica_query(r, replica, 0, 0,
                             anchor_available=False).status, "NO_TRUSTED_ANCHOR")
            self.assertEqual(a.checkpoint.epoch, 1)
            self.assertEqual(query_writer(tree, a, 2, 0, 0).value, 0)
            self.assertEqual(snapshot_query(s, snapshot, 0, 0).value, 0)
            self.assertEqual(replica_query(r, replica, 0, 0).value, 0)

    def test_forged_tree_siblings_range_and_canonical_framing(self):
        for n in (2, 3, 4):
            tree = TreeWriter((0, 1) * (n // 2) + ((1,) if n % 2 else ()))
            genesis = tree.epochs[0]
            reader = Reader(genesis)
            original, reads = tree.serve(0, 0, 0)
            self.assertEqual(checked_query(reader, n, 0, 0, original,
                            reads, genesis).status, "ACCEPT")
            payload = json.loads(original)
            tamper_first_frontier(payload["proof"])
            malicious = canonical(payload)
            for bad in (malicious, b"not-json", b'{"e":0,"e":0,"proof":{}}',
                        original + b" ", b'{"e":true,"proof":{}}'):
                got = checked_query(reader, n, 0, 0, bad, reads, genesis)
                self.assertEqual(got.status, "INVALID_PROOF")
                self.assertEqual(reader.checkpoint, genesis)
            payload = json.loads(original)
            payload["proof"] = {"t": "c", "p": 0, "d": "0" * 64}
            self.assertEqual(checked_query(reader, n, 0, 0,
                             canonical(payload), reads, genesis).status,
                             "INVALID_PROOF")

    def test_one_query_can_be_linearized_at_precommit_anchor_read(self):
        tree = TreeWriter((0, 0))
        before = tree.anchor
        response, reads = tree.serve(0, 0, 1)
        # An update committed AFTER the trusted anchor read is out of scope.
        tree.set(0, 1)
        reader = Reader(before)
        got = checked_query(reader, 2, 0, 1, response, reads, before)
        self.assertEqual((got.status, got.value, got.epoch), ("ACCEPT", 0, 0))
        self.assertEqual(query_writer(tree, reader, 1, 0, 1).value, 1)

    def test_missing_log_message_and_malformed_updates_are_fail_closed(self):
        w = ReplicaWriter((0, 0, 0))
        c = ReplicaReader((0, 0, 0), w.genesis)
        w.set(0, 1)
        w.set(1, 1)
        correct = w.serve(0)
        payload = json.loads(correct)
        cases = []
        cases.append(canonical({"updates": payload["updates"][:1]}))
        cases.append(canonical({"updates": [payload["updates"][1]]}))
        altered = json.loads(correct)
        altered["updates"][0]["b"] ^= 1
        cases.append(canonical(altered))
        tampered = json.loads(correct)
        tampered["updates"][0]["e"] = 10
        cases.append(canonical(tampered))
        cases.append(b'{"updates":[{"b":true,"e":1,"i":0}]}')
        for bad in cases:
            result = replica_query(c, w, 0, 2, response=bad)
            self.assertNotEqual(result.status, "ACCEPT")
            self.assertEqual(c.bits, (0, 0, 0))
            self.assertEqual(c.checkpoint.epoch, 0)
        self.assertEqual(replica_query(c, w, 0, 2).value, 0)
        self.assertEqual(c.bits, (1, 1, 0))

    def test_exact_protocol_wire_counts_and_upper_frontier_examples(self):
        n = 64
        bits = (0,) * n
        tree, full, replica = TreeWriter(bits), SnapshotWriter(bits), ReplicaWriter(bits)
        ta, fa, ra = Reader(tree.epochs[0]), Reader(full.anchor), ReplicaReader(bits, replica.anchor)
        for i in range(8):
            tree.set(i, 1)
            full.set(i, 1)
            replica.set(i, 1)
        t_wire, server_reads = tree.serve(8, 12, 19)
        t = query_writer(tree, ta, 8, 12, 19)
        f = snapshot_query(fa, full, 12, 19)
        r = replica_query(ra, replica, 12, 19)
        self.assertEqual(t.cost.untrusted_response_bytes, len(t_wire))
        self.assertEqual(t.cost.server_node_reads, server_reads)
        self.assertEqual(f.cost.untrusted_response_bytes, len(full.serve(8)))
        self.assertEqual(r.cost.untrusted_response_bytes, len(replica.serve(0)))
        self.assertEqual((t.value, f.value, r.value), (0, 0, 0))
        # JSON hex hashes can exceed a 64-bit full snapshot: NO blanket
        # tiny-n advantage or misleading constant-factor claim.
        self.assertGreater(t.cost.untrusted_response_bytes,
                           f.cost.untrusted_response_bytes)
        large = 4096
        tw = TreeWriter((0,) * large)
        fw = SnapshotWriter((0,) * large)
        tb = query_writer(tw, Reader(tw.anchor), 0, 0, 0)
        fb = snapshot_query(Reader(fw.anchor), fw, 0, 0)
        self.assertLess(tb.cost.untrusted_response_bytes,
                        fb.cost.untrusted_response_bytes)
        self.assertEqual(tree.setup_nodes, 127)
        self.assertEqual(tree.setup_hash_calls, 254)
        self.assertEqual(tree.update_costs[-1].remote_node_writes, 7)
        self.assertEqual(len(ta.__dict__), 1)
        self.assertFalse(hasattr(ta.checkpoint, "bits"))
        self.assertEqual(len(ra.bits), n)
        # No universal order claim: replica catches up proportionally to missed SETs.

    def test_full_snapshot_tampering_idempotent_epoch_and_two_readers(self):
        for n in (2, 3, 4):
            writer = SnapshotWriter((0,) * n)
            a, b = Reader(writer.anchor), Reader(writer.anchor)
            initial_digest = writer.anchor.digest
            writer.set(0, 0)  # idempotent SET is nevertheless a new commit
            self.assertEqual(writer.anchor.digest, initial_digest)
            self.assertEqual(snapshot_query(a, writer, 0, 0, epoch=0).status,
                             "STALE_OR_EQUIVOCATING_ROOT")
            old_checkpoint = a.checkpoint
            forged = json.loads(writer.serve(1))
            forged["bits"][0] = 1
            self.assertEqual(snapshot_query(a, writer, 0, n - 1,
                             response=canonical(forged)).status, "INVALID_PROOF")
            self.assertEqual(a.checkpoint, old_checkpoint)
            self.assertEqual(snapshot_query(a, writer, 0, n - 1).value, 0)
            self.assertEqual(snapshot_query(b, writer, 0, n - 1).value, 0)
            writer.set(n - 1, 1)
            self.assertEqual(snapshot_query(a, writer, n - 1, n - 1,
                             epoch=1).status, "STALE_OR_EQUIVOCATING_ROOT")
            self.assertEqual(snapshot_query(b, writer, n - 1, n - 1).value, 1)

    def test_input_validation_and_adversarial_anchor_reversal(self):
        for values in ((), (2,), (True,), (0,) * 0):
            with self.assertRaises(ValueError):
                TreeWriter(values)
        tree = TreeWriter((0, 0, 0))
        reader = Reader(tree.anchor)
        tree.set(0, 1)
        self.assertEqual(query_writer(tree, reader, 1, 0, 0).status, "ACCEPT")
        ancient = tree.epochs[0]
        response, reads = tree.serve(0, 0, 0)
        self.assertEqual(checked_query(reader, 3, 0, 0, response, reads,
                         ancient).status, "ANCHOR_ROLLBACK_OR_FORK")
        self.assertEqual(reader.checkpoint.epoch, 1)
        swapped = AnchorValue(1, b"x" * 32)
        current, reads = tree.serve(1, 0, 0)
        self.assertEqual(checked_query(reader, 3, 0, 0, current, reads,
                         swapped).status, "ANCHOR_ROLLBACK_OR_FORK")
        for a, b in ((-1, 0), (0, 3), (1, 0)):
            with self.assertRaises(ValueError):
                query_writer(tree, reader, 1, a, b)


if __name__ == "__main__":
    unittest.main()
