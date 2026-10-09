"""G3-B2-A independent, exhaustive two-reader rollback/fork/freshness oracles."""
import itertools
import unittest

from uct005_g3b2a_freshness import (
    SignedSnapshot, SingleWriter, Reader, Checkpoint, SymbolicCostProfile,
    read_signed_state, indistinguishable_without_anchor,
)


def reference_parity(bits, left, right):
    result = 0
    for idx in range(left, right + 1):
        if bits[idx] == 1:
            result = 1 - result
    return result


class G3B2AFreshnessTests(unittest.TestCase):
    def test_identical_observation_is_not_latest_freshness(self):
        # Exhaustive W0/W1 worlds, 2..4 data bits, arbitrary SET(i,b).
        # Proof is not about our particular verifier: the common input
        # transcript is literally identical, but correct LATEST answer
        # differs for at least one range.
        counterexamples = 0
        for n in (2, 3, 4):
            for initial in itertools.product((0, 1), repeat=n):
                no_change = SingleWriter(initial)
                for i in range(n):
                    hidden = SingleWriter(initial)
                    hidden.set(i, 1 - initial[i])
                    for left in range(n):
                        for right in range(left, n):
                            predicted = int(left <= i <= right)
                            self.assertEqual(
                                indistinguishable_without_anchor(
                                    no_change, hidden,
                                    no_change.history[0], left, right),
                                bool(predicted))
                            if predicted:
                                counterexamples += 1
                            # Concrete F0 two clients receive the *same*
                            # epoch-0 certificate, no trusted epoch news.
                            w0 = read_signed_state(
                                Reader(no_change.history[0]),
                                no_change.history[0], no_change.issuer,
                                left, right)
                            w1 = read_signed_state(
                                Reader(hidden.history[0]),
                                hidden.history[0], hidden.issuer,
                                left, right)
                            self.assertEqual((w0.status, w0.value, w0.served_epoch),
                                             (w1.status, w1.value, w1.served_epoch))
                            self.assertEqual(w0.value,
                                reference_parity(initial, left, right))
                            if predicted:
                                self.assertNotEqual(
                                    w1.value,
                                    reference_parity(hidden.history[-1].bits,
                                                     left, right))
        self.assertGreater(counterexamples, 0)

    def test_every_bounded_update_history_prefix_under_two_readers(self):
        # Two clients are independent, no client-to-client communication.
        # Exhaust all 2^n initial states and SET sequences up to three,
        # including no-op SET, for small n. Check prefix acceptance F0 and
        # anchored exact freshness F1 on all 2-reader prefix pairs.
        examined = 0
        for n, depth in ((2, 3), (3, 2), (4, 1)):
            for initial in itertools.product((0, 1), repeat=n):
                operations = tuple(itertools.product(range(n), (0, 1)))
                for ops in itertools.product(operations, repeat=depth):
                    writer = SingleWriter(initial)
                    for i, bit in ops:
                        writer.set(i, bit)
                    for early in range(depth + 1):
                        for later in range(depth + 1):
                            a, b = Reader(writer.history[0]), Reader(writer.history[0])
                            fa = read_signed_state(a, writer.history[early],
                                        writer.issuer, 0, n - 1)
                            fb = read_signed_state(b, writer.history[later],
                                        writer.issuer, 0, n - 1)
                            self.assertEqual((fa.status, fb.status), ("ACCEPT", "ACCEPT"))
                            self.assertEqual(
                                (fa.value, fb.value),
                                (reference_parity(writer.history[early].bits, 0, n - 1),
                                 reference_parity(writer.history[later].bits, 0, n - 1)))
                            a1, b1 = Reader(writer.history[0]), Reader(writer.history[0])
                            ra = read_signed_state(a1, writer.history[early],
                                        writer.issuer, 0, n - 1, anchor=writer.anchor)
                            rb = read_signed_state(b1, writer.history[later],
                                        writer.issuer, 0, n - 1, anchor=writer.anchor)
                            self.assertEqual(ra.status,
                                 "ACCEPT" if early == depth else "STALE_OR_EQUIVOCATING_ROOT")
                            self.assertEqual(rb.status,
                                 "ACCEPT" if later == depth else "STALE_OR_EQUIVOCATING_ROOT")
                            examined += 1
        self.assertGreater(examined, 250)

    def test_anchored_rejoin_refuses_replay_and_fails_closed_when_unreachable(self):
        writer = SingleWriter((0, 0, 0))
        c1 = Reader(writer.history[0])
        c2 = Reader(writer.history[0])
        one = writer.set(0, 1)
        self.assertEqual(read_signed_state(
             c1, one, writer.issuer, 0, 2, anchor=writer.anchor).status, "ACCEPT")
        two = writer.set(2, 1)
        rejected = read_signed_state(c2, one, writer.issuer, 0, 2, anchor=writer.anchor)
        self.assertEqual(rejected.status, "STALE_OR_EQUIVOCATING_ROOT")
        self.assertEqual(c2.checkpoint.epoch, 0)
        blocked = read_signed_state(c2, two, writer.issuer, 0, 2,
                                    anchor=writer.anchor, anchor_available=False)
        self.assertEqual(blocked.status, "NO_TRUSTED_ANCHOR")
        self.assertIsNone(blocked.value)
        self.assertEqual(blocked.costs.anchor_calls, 1)
        self.assertEqual(blocked.costs.anchor_received_bits, 0)
        self.assertEqual(blocked.costs.verifier_received_bits, 0)
        self.assertEqual(blocked.costs.server_snapshot_cell_reads, 0)
        self.assertEqual(c2.checkpoint.epoch, 0)
        accepted = read_signed_state(c2, two, writer.issuer, 0, 2, anchor=writer.anchor)
        self.assertEqual((accepted.status, accepted.value), ("ACCEPT", 0))
        self.assertEqual(c2.checkpoint.epoch, 2)
        # The older client cannot silently regress once it accepted epoch 1.
        old = read_signed_state(c1, writer.history[0],
                                writer.issuer, 0, 2)
        self.assertEqual(old.status, "ROLLBACK_OR_FORK_FROM_CHECKPOINT")
        self.assertEqual(c1.checkpoint.epoch, 1)

    def test_signature_and_parent_check_are_separate_from_freshness(self):
        writer = SingleWriter((0, 0))
        genuine = writer.set(1, 1)
        genesis = writer.history[0]
        forged = SignedSnapshot(genuine.epoch, genuine.parent_seal,
                                (1, 1), genuine.seal)
        self.assertEqual(read_signed_state(Reader(genesis), forged,
                         writer.issuer, 0, 1).status,
                         "INVALID_SIGNATURE_OR_PAYLOAD")
        signed_but_stale = read_signed_state(Reader(genesis), genesis,
                                            writer.issuer, 0, 1)
        self.assertEqual(signed_but_stale.status, "ACCEPT")
        self.assertEqual(signed_but_stale.value, 0)
        self.assertEqual(reference_parity(genuine.bits, 0, 1), 1)

    def test_fork_requires_writer_equivocation_when_author_is_single_chain(self):
        writer = SingleWriter((0, 0, 0))
        honest = writer.set(0, 1)
        alternative = writer.issuer.adversarial_double_sign(
            writer.history[0], 1, 1)
        self.assertEqual(alternative.epoch, honest.epoch)
        self.assertNotEqual(alternative.seal, honest.seal)
        self.assertTrue(writer.issuer.verify(alternative))
        left, right = Reader(writer.history[0]), Reader(writer.history[0])
        self.assertEqual(read_signed_state(left, honest,
             writer.issuer, 0, 0).status, "ACCEPT")
        self.assertEqual(read_signed_state(right, alternative,
             writer.issuer, 0, 0).status, "ACCEPT")
        self.assertNotEqual(left.checkpoint.seal, right.checkpoint.seal)
        # This exact fork requires compromised/equivocating author,
        # not a Byzantine SERVER by itself.
        self.assertEqual(read_signed_state(Reader(writer.history[0]),
             alternative, writer.issuer, 0, 0,
             anchor=writer.anchor).status, "STALE_OR_EQUIVOCATING_ROOT")
        self.assertEqual(read_signed_state(Reader(writer.history[0]),
             honest, writer.issuer, 0, 0,
             anchor=writer.anchor).status, "ACCEPT")
        self.assertEqual(read_signed_state(left, alternative,
             writer.issuer, 0, 0).status, "ROLLBACK_OR_FORK_FROM_CHECKPOINT")
        with self.assertRaises(ValueError):
            writer.anchor.publish(alternative, writer.issuer)

    def test_trusted_reader_really_stores_only_epoch_and_token(self):
        w = SingleWriter((0, 1, 0, 1))
        c = Reader(w.history[0])
        self.assertIsInstance(c.checkpoint, Checkpoint)
        self.assertEqual(c.n, 4)
        self.assertFalse(hasattr(c.checkpoint, "bits"))
        self.assertEqual(c.clone().checkpoint, c.checkpoint)
        final = w.set(0, 1)
        self.assertEqual(read_signed_state(c, final, w.issuer, 0, 3,
                                            anchor=w.anchor).status, "ACCEPT")
        self.assertFalse(hasattr(c.checkpoint, "bits"))

    def test_exact_logical_cost_ledger_and_no_false_free_anchor(self):
        writer = SingleWriter((0, 0, 0, 0))
        receipt = writer.set(2, 1)
        profile = SymbolicCostProfile(signature_bits=128,
                                      root_bits=128, epoch_bits=8)
        unanchored = read_signed_state(Reader(writer.history[0]), receipt,
                 writer.issuer, 0, 3, profile=profile)
        anchored = read_signed_state(Reader(writer.history[0]), receipt,
                 writer.issuer, 0, 3, profile=profile,
                 anchor=writer.anchor)
        self.assertEqual(unanchored.costs.verifier_received_bits, 4+128+128+16)
        self.assertEqual(anchored.costs.anchor_received_bits, 128+8)
        self.assertEqual(anchored.costs.verifier_received_bits,
                         unanchored.costs.verifier_received_bits)
        self.assertEqual(anchored.costs.server_snapshot_cell_reads, 4)
        self.assertEqual((anchored.costs.anchor_calls,
                          unanchored.costs.anchor_calls), (1, 0))
        self.assertEqual(writer.anchor.publications, 1)
        self.assertEqual(anchored.costs.reader_trusted_checkpoint_bits, 128+8)
        # No claim that symbolic signature verification is O(1) CPU or secure.
        with self.assertRaises(ValueError):
            SymbolicCostProfile(epoch_bits=0)

if __name__ == "__main__":
    unittest.main()
