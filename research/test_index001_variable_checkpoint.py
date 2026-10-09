"""Independent finite checks for INDEX-001 G2-B4-A variable-size checkpoint costs."""
from fractions import Fraction
from itertools import product
from math import comb
import random
import unittest
import zlib
import struct

from index001_checkpoint_policy import Weights
from index001_oracle import ExactRangeMap, count_maps_with_k_runs
from index001_variable_checkpoint import (
    WITNESS, build_report, compare, decode_snapshot, decode_wal,
    encode_snapshot, encode_wal, offline_bruteforce, offline_dp,
    online_threshold, scaling_bad_family, scaling_bound_instance,
    score, trace_sizes, uvarint,
)


class VariableCheckpointTests(unittest.TestCase):
    def test_complete_binary_state_count_and_canonical_crc_roundtrip(self):
        for n in range(1, 9):
            counts = [0] * (n + 1)
            for values in product((0, 1), repeat=n):
                encoded = encode_snapshot(values)
                self.assertEqual(decode_snapshot(encoded), values)
                runs = 1 + sum(a != b for a, b in zip(values, values[1:]))
                self.assertEqual(len(encoded), 10 + 2 * runs)
                counts[runs] += 1
            for k in range(1, n + 1):
                self.assertEqual(counts[k], 2 * comb(n - 1, k - 1))
                self.assertEqual(counts[k], count_maps_with_k_runs(n, 2, k))

    def test_varint_boundaries_and_wal_exact_sizes(self):
        self.assertEqual(uvarint(0), b"\x00")
        self.assertEqual(uvarint(127), b"\x7f")
        self.assertEqual(uvarint(128), b"\x80\x01")
        self.assertEqual(len(encode_wal(130, 1, 2, 1)), 9)
        self.assertEqual(len(encode_wal(130, 127, 130, 1)), 10)
        for n, lo, hi in ((1, 0, 1), (130, 127, 130), (20000, 19000, 20000)):
            frame = encode_wal(n, lo, hi, 1)
            self.assertEqual(decode_wal(n, frame), (lo, hi, 1))
        a = (0,) * 127 + (1,)
        b = (0,) * 128
        self.assertNotEqual(len(encode_snapshot(a)), len(encode_snapshot(b)))
        # The run length encoding must grow at boundary 127->128.
        self.assertEqual(len(encode_snapshot((0,) * 127)), 12)
        self.assertEqual(len(encode_snapshot((0,) * 128)), 14)

    def test_crc_and_canonical_decoder_rejections(self):
        snap = encode_snapshot((0, 0, 1))
        bad = bytearray(snap)
        bad[6] ^= 1
        with self.assertRaises(ValueError):
            decode_snapshot(bytes(bad))
        with self.assertRaises(ValueError):
            decode_snapshot(snap[:-1])
        with self.assertRaises(ValueError):
            decode_snapshot(encode_snapshot((0, 0, 1)) + b"\x00")
        # A repeated equal symbol violates *maximal* run canonicalization,
        # even if CRC and total cell count are correct.
        payload = b"IXR1" + b"\x02\x02" + b"\x01\x00\x01\x00"
        forged = payload + struct.pack("<I", zlib.crc32(payload))
        with self.assertRaises(ValueError):
            decode_snapshot(forged)
        wal = encode_wal(6, 1, 2, 1)
        with self.assertRaises(ValueError):
            decode_wal(6, wal[:-1])
        with self.assertRaises(ValueError):
            encode_wal(6, 2, 2, 1)
        with self.assertRaises(ValueError):
            uvarint(-1)

    def test_dense_trace_and_independent_run_map(self):
        n = 6
        s, e, states = trace_sizes(n, WITNESS)
        self.assertEqual(s, (12, 16, 20, 22, 12))
        self.assertEqual(e, (0, 9, 9, 9, 9))
        runs = ExactRangeMap(n)
        for op, expected in zip(WITNESS, states[1:]):
            runs.assign(*op)
            self.assertEqual(tuple(runs.lookup(i) for i in range(n)), expected)
        self.assertEqual(states[-1], (0,) * 6)

    def test_counterexample_to_unmodified_two_bound(self):
        r = (0, 0, 0, 1)
        w = Weights(0, 1, 0)
        self.assertEqual(online_threshold(6, WITNESS), (3,))
        online = score(6, WITNESS, r, (3,), w)
        offline = offline_dp(6, WITNESS, r, w)
        independent = offline_bruteforce(6, WITNESS, r, w)
        self.assertEqual(offline, independent)
        self.assertEqual(online["steady_file_bytes"][-1], 31)
        self.assertEqual(offline["steady_file_bytes"][-1], 12)
        self.assertEqual(online["recovery_read_bytes"], 31)
        self.assertEqual(offline["recovery_read_bytes"], 12)
        self.assertEqual(Fraction(online["weighted_cost"], offline["weighted_cost"]),
                         Fraction(31, 12))
        self.assertGreater(Fraction(31, 12), 2)
        self.assertEqual(compare(6, WITNESS, r, w)["ratio"], [31, 12])
        # Failure also persists with strictly positive write weight.
        self.assertGreater(Fraction(*compare(
            6, WITNESS, (0, 0, 0, 100), Weights(1, 6, 0))["ratio"]), 2)

    def test_independent_offline_dp_small_census(self):
        # Full operations alphabet for n<=3, U<=3; independent all-subsets
        # oracle, two price vectors and all restart counts in {0,2}.
        for n in (1, 2, 3):
            actions = tuple((lo, hi, v) for lo in range(n)
                            for hi in range(lo + 1, n + 1) for v in (0, 1))
            for horizon in range(4):
                for ops in product(actions, repeat=horizon):
                    for r in product((0, 2), repeat=horizon):
                        for w in (Weights(0, 1, 0), Weights(1, 6, 1)):
                            self.assertEqual(offline_dp(n, ops, r, w),
                                             offline_bruteforce(n, ops, r, w))

    def test_parameter_dependent_bound_and_random_large_traces(self):
        rng = random.Random(173)
        for n in range(1, 7):
            for _ in range(65):
                operations = []
                r = []
                for _ in range(5):
                    lo = rng.randrange(n)
                    hi = rng.randrange(lo + 1, n + 1)
                    operations.append((lo, hi, rng.randrange(2)))
                    r.append(rng.randrange(4))
                for w in (Weights(1, 6, 0), Weights(0, 1, 0),
                          Weights(1, 0, 0), Weights(0, 0, 1)):
                    result = compare(n, operations, r, w)
                    kappa = Fraction(*result["kappa"])
                    self.assertLessEqual(Fraction(*result["ratio"]), 2 * kappa)
                    self.assertLessEqual(result["online"]["written_bytes"],
                                         2 * result["offline"]["written_bytes"])

    def test_unbounded_threshold_specific_family(self):
        previous_ratio = None
        for n in (3, 5, 31, 129, 511):
            ops, high_checkpoint = scaling_bad_family(n)
            self.assertEqual(online_threshold(n, ops)[-1], high_checkpoint)
            self.assertEqual(ops[-1], (0, n, 0))
            self.assertEqual(ops[(n - 1) // 2:high_checkpoint],
                             ((0, 1, 0),) * (high_checkpoint - (n - 1) // 2))
            row = scaling_bound_instance(n)
            width = len(uvarint(n))
            exact = Fraction(16 + 3 * width + 2 * n, 10 + 2 * width)
            self.assertEqual(Fraction(*row["ratio"]), exact)
            self.assertGreater(exact, 2)
            if previous_ratio is not None:
                self.assertGreater(exact, previous_ratio)
            previous_ratio = exact

    def test_reveal_order_and_reproducible_witness(self):
        self.assertEqual(online_threshold(6, WITNESS),
                         online_threshold(6, WITNESS))
        result = build_report()
        self.assertEqual(result, build_report())
        self.assertEqual(result["naive_threshold_witness"]["ratio"], [31, 12])
        self.assertEqual(result["novel_general_theorem"], "NOT_ESTABLISHED")
        self.assertEqual(result["nand_bytes"], "NOT_MEASURED")


if __name__ == "__main__":
    unittest.main()
