"""INDEX-001 G2-B2-B: independent exhaustive optimization and POSIX file checks."""
import itertools
import unittest

from index001_checkpoint_policy import (
    Weights, actual_filesystem_trace, build_report,
    checkpoint_orphan_observation, exhaustive_offline, optimal_offline, score,
)
from index001_workload_io import workload_traces


def independent_bruteforce(size, restarts, weights, age_limit=None, peak_limit=None):
    """Own formula and subset enumeration; never calls score()/DP recurrence."""
    n = len(restarts)
    s, e = 24 + 4 * size, 28
    result = None
    for bitvec in itertools.product((0, 1), repeat=n):
        age = 0
        total_w = s + n * e
        total_r = 0
        total_f = 0
        peak = s
        maximum_age = 0
        feasible = peak_limit is None or s <= peak_limit
        checkpoint_path = []
        for t, (bit, reads) in enumerate(zip(bitvec, restarts), 1):
            pending = age + 1
            if bit:
                checkpoint_path.append(t)
                transient = 2 * s + e * pending
                total_w += s
                age = 0
            else:
                transient = s + e * pending
                age = pending
            peak = max(peak, transient)
            maximum_age = max(maximum_age, age)
            if age_limit is not None and age > age_limit:
                feasible = False
            if peak_limit is not None and peak > peak_limit:
                feasible = False
            total_r += reads * (s + e * age)
            total_f += s + e * age
        if not feasible:
            continue
        val = (weights.write * total_w + weights.recovery * total_r
               + weights.footprint * total_f)
        candidate = (val, tuple(checkpoint_path))
        if result is None or candidate < result[0]:
            result = (candidate, {
                "checkpoints": checkpoint_path, "weighted_cost": val,
                "written_bytes": total_w, "recovery_read_bytes": total_r,
                "steady_footprint_byte_steps": total_f, "peak_path_bytes": peak,
                "max_steady_wal_records": maximum_age,
            })
    return None if result is None else result[1]


class CheckpointPolicyTests(unittest.TestCase):
    def test_dp_equals_independent_full_subset_oracle(self):
        configs = [Weights(1, 0, 0), Weights(1, 1, 0),
                   Weights(1, 6, 0), Weights(2, 3, 1),
                   Weights(0, 1, 1), Weights(0, 0, 1)]
        for u in range(0, 7):
            restart_vectors = [
                (0,) * u, (1,) * u,
                tuple(2 if i == u - 1 else 0 for i in range(u)),
                tuple(i % 3 for i in range(u)),
            ]
            for counts, weights, cap, peak in itertools.product(
                    restart_vectors, configs, (None, 0, 2), (None, 144)):
                with self.subTest(u=u, count=counts, weights=weights, cap=cap, peak=peak):
                    best = independent_bruteforce(4, counts, weights, cap, peak)
                    dp = optimal_offline(4, counts, weights, cap, peak)
                    self.assertEqual(dp is None, best is None)
                    if dp is None:
                        continue
                    self.assertEqual(dp["checkpoints"], best["checkpoints"])
                    for key in ("weighted_cost", "written_bytes",
                                "recovery_read_bytes",
                                "steady_footprint_byte_steps",
                                "peak_path_bytes",
                                "max_steady_wal_records"):
                        self.assertEqual(dp[key], best[key])

    def test_score_is_not_minimized_by_periodic_for_restart_bursts(self):
        n = 10
        counts = tuple(2 if i in (2, 8) else 0 for i in range(n))
        weights = Weights(1, 6, 0)
        opt = optimal_offline(32, counts, weights)
        self.assertEqual(opt, exhaustive_offline(32, counts, weights))
        periodic = [score(32, counts,
                          tuple(t for t in range(1, n + 1) if t % width == 0),
                          weights) for width in (1, 4, 16)]
        self.assertLess(opt["weighted_cost"],
                        min(z["weighted_cost"] for z in periodic))
        self.assertGreater(opt["written_bytes"], score(32, counts, (), weights)["written_bytes"])
        self.assertLess(opt["recovery_read_bytes"],
                        score(32, counts, (), weights)["recovery_read_bytes"])

    def test_steady_and_peak_budget_separate(self):
        n, counts, w = 4, (0, 0, 0), Weights(1, 1, 1)
        s, e = 40, 28
        self.assertIsNone(score(n, counts, (), w, max_steady_age=0))
        self.assertIsNone(score(n, counts, (1, 2, 3), w, peak_cap=s))
        only = score(n, counts, (1, 2, 3), w,
                     max_steady_age=0, peak_cap=2*s + e)
        self.assertIsNotNone(only)
        self.assertEqual(only["peak_path_bytes"], 2*s+e)
        self.assertEqual(only["max_steady_wal_records"], 0)
        self.assertEqual(only["steady_footprint_byte_steps"], 3*s)
        self.assertIsNone(optimal_offline(n, counts, w, 0, 2*s))
        self.assertEqual(optimal_offline(n, (), w)["written_bytes"], s)
        self.assertEqual(optimal_offline(n, (), w)["checkpoints"], [])

    def test_no_restarts_and_no_footprint_cost_never_checkpoint(self):
        for n in (0, 1, 4, 9):
            result = optimal_offline(5, (0,) * n, Weights(1, 0, 0))
            self.assertEqual(result["checkpoints"], [])
            self.assertEqual(result["written_bytes"], 44 + 28*n)

    def test_filesystem_full_trace_and_nonnegative_checkpoint_events(self):
        traces = workload_traces()
        for name, ops in traces.items():
            u = len(ops)
            counts = tuple(2 if t in (3, u) else 0
                           for t in range(1, u + 1))
            policy = optimal_offline(32, counts, Weights(1, 6, 0))
            actual = actual_filesystem_trace(ops, counts, policy["checkpoints"])
            self.assertEqual(actual["written_bytes"], policy["written_bytes"])
            self.assertEqual(actual["recovery_read_bytes"],
                             policy["recovery_read_bytes"])
            self.assertEqual(actual["steady_footprint_byte_steps"],
                             policy["steady_footprint_byte_steps"])
            self.assertEqual(actual["checkpoint_events"],
                             len(policy["checkpoints"]))
            self.assertEqual(actual["observed_restarts"], sum(counts))
            self.assertGreaterEqual(actual["fsync_files_during_updates"], u)
            self.assertGreaterEqual(actual["fsync_dirs_during_updates"],
                                    len(policy["checkpoints"]))
            self.assertEqual(actual["steady_snapshot_bytes"], 152)
            self.assertEqual(actual["steady_wal_bytes"],
                             28 * policy["steady_wal_ages"][-1])

    def test_crash_orphan_temp_occupancy_and_recovery(self):
        snapshots = {
            "after_checkpoint_partial": (56, 28, 28),
            "after_checkpoint_sync": (56, 56, 28),
            "after_checkpoint_replace": (56, None, 28),
            "after_checkpoint_dirsync": (56, None, 28),
            "after_wal_truncate": (56, None, 0),
        }
        for fault, (snapshot, tmp, log) in snapshots.items():
            with self.subTest(fault=fault):
                obs = checkpoint_orphan_observation(8, fault)
                self.assertEqual(obs["recovered_seq"], 1)
                self.assertEqual(obs["files_after_stop"], {
                    "snapshot.bin": snapshot,
                    "snapshot.tmp": tmp,
                    "wal.bin": log,
                })
                self.assertEqual(obs["orphan_temp_not_auto_reclaimed"], tmp is not None)
                self.assertEqual(obs["reopen_application_read_bytes"], snapshot + log)

    def test_report_is_reproducible_and_not_physical_device_claim(self):
        x = build_report()
        y = build_report()
        self.assertEqual(x, y)
        self.assertEqual(x["hardware_nand_bytes"], "NOT_MEASURED")
        self.assertEqual(x["device_durability"], "NOT_PROVED")
        self.assertIn("OFFLINE_EXACT", x["classification"])
        self.assertEqual(len(x["workloads"]), 4)
        for row in x["workloads"].values():
            self.assertEqual(row["offline_optimum"],
                             exhaustive_offline(32, row["restart_observations"],
                                                Weights(1, 6, 0)))
            self.assertTrue(all(row["offline_optimum"]["weighted_cost"]
                                <= p["weighted_cost"] for p in row["periodic"].values()))

    def test_invalid_inputs_and_infeasible_caps(self):
        self.assertEqual(score(4, (0, 1), (2,))["checkpoints"], [2])
        for restarts in ((-1,), (1.0,)):
            with self.assertRaises(ValueError):
                score(4, restarts)
        for checkpoints in ((3,), (1, 1), (2, 1), (0,)):
            with self.assertRaises(ValueError):
                score(4, (0, 1), checkpoints)
        with self.assertRaises(ValueError):
            Weights(-1, 0, 0)
        with self.assertRaises(ValueError):
            Weights(0, 0, 0)
        with self.assertRaises(ValueError):
            score(4, (0,), max_steady_age=-1)
        with self.assertRaises(ValueError):
            score(4, (0,), peak_cap=0)
        with self.assertRaises(ValueError):
            exhaustive_offline(4, (0,) * 13)
        with self.assertRaises(ValueError):
            actual_filesystem_trace([(0, 1, 1)], (), ())


if __name__ == "__main__":
    unittest.main()
