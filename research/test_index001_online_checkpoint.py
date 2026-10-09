"""INDEX-001 G2-B3-B: finite adversary and exact online theorem oracle tests.

The upper bound is intentionally a restricted elementary statement, not a
published new lower bound or a proof about hardware crashes or online LSM.
"""
import itertools
from fractions import Fraction
import unittest

from index001_checkpoint_policy import Weights, exhaustive_offline, score
from index001_online_checkpoint import (
    adaptive_greedy_trace, build_report, compare, component_bound, cost_ratio,
    finite_worst, online_policy, safe_threshold, snapshot_size,
)


def independent_policy(n, restarts, threshold):
    """No import of algorithm-under-test recurrence. Last checkpoint t multiple of T."""
    return tuple(t for t in range(1, len(restarts) + 1) if t % threshold == 0)


def independent_brute_worst(n, horizon, maximum, weights):
    best = None
    for r in itertools.product(range(maximum + 1), repeat=horizon):
        checkpoint = independent_policy(n, r, safe_threshold(n))
        online = score(n, r, checkpoint, weights)
        # Truly enumerate all checkpoint subsets without calling offline DP.
        oracle = exhaustive_offline(n, r, weights)
        value = Fraction(online["weighted_cost"], oracle["weighted_cost"]) if oracle["weighted_cost"] else Fraction(1)
        if best is None or value > best[0]:
            best = (value, r, checkpoint, tuple(oracle["checkpoints"]))
    return best


class Index001OnlineCheckpointTests(unittest.TestCase):
    def test_exact_threshold_boundary_and_reveal_order(self):
        for n in (1, 4, 32, 255):
            t = safe_threshold(n)
            s = snapshot_size(n)
            self.assertTrue(28*t >= s)
            self.assertTrue(28*(t-1) < s)
            self.assertLessEqual(component_bound(n, t), Fraction(2))
            for length in (0, 1, max(0, t - 1), t, t + 1, 2*t + 1):
                zero = (0,) * length
                maxburst = (3,) * length
                target = independent_policy(n, zero, t)
                self.assertEqual(online_policy(n, zero), target)
                self.assertEqual(online_policy(n, maxburst), target)
                # Decisions do not depend on a different current r_t.
                for k in range(length):
                    history = list(zero)
                    history[k] = 3
                    self.assertEqual(online_policy(n, history), target)

    def test_full_census_against_offline_oracle(self):
        configs = (
            (1, Weights(1, 1, 0)),
            (4, Weights(1, 6, 0)),
            (4, Weights(2, 2, 3)),
            (32, Weights(1, 1, 1)),
            (4, Weights(0, 1, 0)),
            (4, Weights(1, 0, 0)),
        )
        for n, weights in configs:
            for length in range(0, 6):
                for r in itertools.product((0, 1, 2), repeat=length):
                    with self.subTest(size=n, length=length, weights=weights, r=r):
                        result = compare(n, r, weights, independent=True)
                        ratio = Fraction(result["ratio"]["numerator"],
                                         result["ratio"]["denominator"])
                        self.assertLessEqual(ratio, 2)
                        self.assertEqual(result["online_checkpoint"],
                                         list(independent_policy(n, r, safe_threshold(n))))
                        self.assertLessEqual(result["online_written"],
                                             2*result["offline_written"])
                        self.assertLessEqual(result["online_recovery"],
                                             2*result["offline_recovery"])
                        self.assertLessEqual(result["online_byte_steps"],
                                             2*result["offline_byte_steps"])

    def test_finite_worst_witness_independently_recomputed(self):
        weights = Weights(1, 6, 0)
        for horizon in (0, 1, 2, 3, 4, 5):
            actual = finite_worst(4, horizon, 2, weights)
            value, witness, checkpoint, offline = independent_brute_worst(
                4, horizon, 2, weights)
            self.assertEqual(actual["histories_checked"], 3**horizon)
            self.assertEqual(actual["witness"], list(witness))
            self.assertEqual(actual["witness_online_checkpoint"], list(checkpoint))
            self.assertEqual(actual["witness_offline_checkpoint"], list(offline))
            self.assertEqual(actual["ratio"],
                             {"numerator": value.numerator,
                              "denominator": value.denominator})
            self.assertLessEqual(value, 2)

    def test_no_checkpoint_immediate_and_reactive_adversaries(self):
        r = (1, 0, 2, 0, 1)
        self.assertEqual(online_policy(32, r, "never"), ())
        self.assertEqual(online_policy(32, r, "immediate"), (1, 2, 3, 4, 5))
        self.assertEqual(online_policy(32, r, "reactive"), (2, 4))
        greedy = adaptive_greedy_trace(32, 8, "threshold", max_restart=2)
        self.assertEqual(len(greedy), 8)
        self.assertTrue(set(greedy) <= {0, 2})
        self.assertEqual(online_policy(32, greedy),
                         independent_policy(32, greedy, safe_threshold(32)))
        never = finite_worst(4, 4, strategy="never")
        self.assertIsNone(never["reference_bound"])
        immediate = finite_worst(4, 4, strategy="immediate")
        self.assertIsNone(immediate["reference_bound"])
        self.assertLessEqual(finite_worst(4, 4)["ratio"]["numerator"] /
                             finite_worst(4, 4)["ratio"]["denominator"], 2)

    def test_explicit_one_step_nonclairvoyance_witness(self):
        n = 4
        w = Weights(1, 6, 0)
        # Decision is before seeing r1, giving positive regret either way.
        self.assertEqual(online_policy(n, (0,), "immediate"), (1,))
        opt_zero = exhaustive_offline(n, (0,), w)
        now = score(n, (0,), (1,), w)
        self.assertGreater(now["weighted_cost"], opt_zero["weighted_cost"])
        huge = (100,)
        offline = exhaustive_offline(n, huge, w)
        skipped = score(n, huge, (), w)
        self.assertEqual(offline["checkpoints"], [1])
        self.assertGreater(skipped["weighted_cost"], offline["weighted_cost"])

    def test_component_bound_and_custom_thresholds(self):
        for n in (1, 4, 32):
            for t in (1, 2, 3, safe_threshold(n), safe_threshold(n) + 1):
                bound = component_bound(n, t)
                for r in ((0,)*7, (1,)*7, (0, 2, 0, 2, 0, 2, 0)):
                    for w in (Weights(1, 6, 0), Weights(1, 0, 1)):
                        row = compare(n, r, w, "threshold", threshold=t)
                        quotient = Fraction(row["ratio"]["numerator"],
                                            row["ratio"]["denominator"])
                        self.assertLessEqual(quotient, bound)

    def test_report_determinism_and_actual_posix_counters(self):
        result = build_report()
        self.assertEqual(result, build_report())
        self.assertEqual(result["physical_nand_bytes"], "NOT_MEASURED")
        self.assertEqual(result["hard_caps"], "EXCLUDED_FROM_THEOREM")
        self.assertEqual(result["classification"], "ELEMENTARY_2_UPPER_BOUND_NOT_NOVELTY")
        self.assertEqual(len(result["workloads"]), 4)
        for row in result["workloads"].values():
            self.assertEqual(row["competitive_comparison"]["online_written"],
                             row["filesystem_actual_write_bytes"])
            self.assertEqual(row["competitive_comparison"]["online_recovery"],
                             row["filesystem_actual_recovery_bytes"])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            safe_threshold(0)
        for bad in (0, -1, 1.5):
            with self.assertRaises(ValueError):
                component_bound(4, bad)
        with self.assertRaises(ValueError):
            online_policy(4, (-1,))
        with self.assertRaises(ValueError):
            online_policy(4, (0,), "unknown")
        with self.assertRaises(ValueError):
            finite_worst(4, 9)
        with self.assertRaises(ValueError):
            finite_worst(4, 1, 4)
        with self.assertRaises(ValueError):
            adaptive_greedy_trace(4, -1)
        with self.assertRaises(ValueError):
            adaptive_greedy_trace(4, 1, max_restart=-1)


if __name__ == "__main__":
    unittest.main()
