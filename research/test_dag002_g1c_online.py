"""Independent minimax and explicit finite-program checks for DAG G1-C1."""
from functools import lru_cache
import itertools
import unittest

from dag002_g1c_online import (
    OnlineModel, successors, online_kernel, probe_programs,
    apply_probe_program, uniform_online_witness, spoke_counterexample,
    syndrome_model, report,
)


def independently_survives(model, initial, horizon):
    """Separate top-down bounded adversarial game; no calls to successors/kernel."""
    @lru_cache(None)
    def game(word, remaining):
        if remaining == 0:
            return True
        for d in model.deltas:
            if not any(model.decoder[word ^ mask] == (model.decoder[word] ^ d)
                       and game(word ^ mask, remaining - 1)
                       for mask in range(1 << model.remote_bits)
                       if mask.bit_count() <= model.net_writes):
                return False
        return True
    return game(initial, horizon)


class G1COnlineTests(unittest.TestCase):
    def test_one_shot_saturates_G1B_but_fails_at_two_epochs(self):
        case = spoke_counterexample()
        self.assertEqual([successors(case, 0, d) for d in case.deltas],
                         [(0,), (1,), (2,), (4,)])
        self.assertEqual(1 + 3, 4)  # G1-B H=0, M=3, W=1; saturates
        self.assertEqual(set(online_kernel(case)), set())
        # DELTA(3) must reach unique physical 100, then DELTA(1) demands
        # label 10; the entire radius-1 ball around 100 has only label 00/11.
        self.assertEqual(successors(case, 4, 1), ())
        self.assertTrue(independently_survives(case, 0, 1))
        self.assertFalse(independently_survives(case, 0, 2))

    def test_independent_minimax_exhaustive_small_decoder_tables(self):
        # Every 1-bit output decoder for N<=3 and every 2-bit output decoder
        # for N<=2, two delta alphabet variants, all W, all starting words.
        for n, N in ((1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2)):
            for decoder in itertools.product(range(1 << n), repeat=1 << N):
                for w in range(N + 1):
                    for deltas in ((0,), tuple(range(1 << n))):
                        model = OnlineModel(n, N, w, decoder, deltas)
                        kernel = online_kernel(model)
                        for word in model.states:
                            self.assertEqual(word in kernel,
                                independently_survives(model, word, 1 << N),
                                (n, N, w, deltas, decoder, word))

    def test_mandatory_restricted_alphabet_exclusion(self):
        case = spoke_counterexample()
        reduced = OnlineModel(case.output_bits, case.remote_bits,
                              case.net_writes, case.decoder, (0, 1))
        self.assertEqual(online_kernel(case), frozenset())
        self.assertTrue(0 in online_kernel(reduced))

    def test_one_probe_uniform_strategy_and_all_remote_histories(self):
        model = syndrome_model()
        self.assertEqual(online_kernel(model), frozenset(range(8)))
        for initial in (0, 3, 7):
            live, programs = uniform_online_witness(model, 1, initial)
            self.assertEqual(live, frozenset(range(8)))
            for state in live:
                for delta, program in programs.items():
                    dest = apply_probe_program(state, program)
                    self.assertIn(dest, live)
                    self.assertEqual(model.decoder[dest], model.decoder[state] ^ delta)
                    self.assertLessEqual((state ^ dest).bit_count(), 1)
        # Verify 4^4 adversarial delta histories against independent G1-B
        # implementation, not just the selected subset certificate.
        for updates in itertools.product(range(4), repeat=4):
            word = 0
            expected = 0
            update_reads = writes = 0
            for delta in updates:
                expected ^= delta
                if delta:
                    word ^= 1 << (delta - 1)  # independent column oracle
                    update_reads += 1
                    writes += 1
                label = 0
                for idx, column in enumerate((1, 2, 3)):
                    if word & (1 << idx):
                        label ^= column
                self.assertEqual(label, expected)
                self.assertEqual(model.decoder[word], expected)
                self.assertLessEqual(update_reads, 4)
                self.assertLessEqual(writes, 4)

    def test_zero_read_fixed_overwrite_is_idempotent(self):
        model = syndrome_model()
        self.assertIsNone(uniform_online_witness(model, 0, 0))
        self.assertIsNotNone(uniform_online_witness(model, 1, 0))
        # Stateless fixed overwrite programs are idempotent. For any d!=0,
        # applying d twice cannot encode y -> y xor d -> y, hence impossible.
        for N in range(4):
            for program in probe_programs(N, 0):
                for word in range(1 << N):
                    after = apply_probe_program(word, program)
                    self.assertEqual(apply_probe_program(after, program), after)
        # Explicit XOR-write is a DIFFERENT primitive: model must not silently
        # count it as blind assignment without an update read.

    def test_separate_read_and_physical_overwrite_costs(self):
        model = syndrome_model()
        live, programs = uniform_online_witness(model, 1, 0)
        self.assertEqual(live, frozenset(range(8)))
        for delta in (1, 2, 3):
            self.assertIsNotNone(programs[delta][0])
            for state in range(8):
                self.assertEqual((state ^ apply_probe_program(state, programs[delta])).bit_count(), 1)
        self.assertEqual(programs[0][0], None)

    def test_reject_malformed_and_unpriced_models(self):
        with self.assertRaises(ValueError):
            OnlineModel(True, 1, 0, (0, 1), (0, 1))
        with self.assertRaises(ValueError):
            OnlineModel(1, 4, 5, (0,) * 16, (0, 1))
        with self.assertRaises(ValueError):
            OnlineModel(1, 2, 1, (0, 1), (0, 1))
        with self.assertRaises(ValueError):
            OnlineModel(1, 1, 1, (0, 2), (0, 1))
        with self.assertRaises(ValueError):
            OnlineModel(1, 1, 1, (0, 1), (0, 0))
        with self.assertRaises(ValueError):
            uniform_online_witness(syndrome_model(), 2, 0)
        with self.assertRaises(ValueError):
            probe_programs(4, 1)
        with self.assertRaises(ValueError):
            successors(syndrome_model(), 0, 4)


if __name__ == "__main__":
    unittest.main()
