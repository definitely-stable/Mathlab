"""INDEX-001 G2-B2-B: offline checkpoint policy on a *fixed reference* protocol.

Prices actual application frame bytes, clean-restart bytes, steady-state
byte-steps and checkpoint temporary coexistence. Not physical NAND I/O,
new online-competitive theorem, hardware crash proof or production code.
"""
import argparse
from dataclasses import dataclass
import itertools
import json
from pathlib import Path
import tempfile

from index001_durable import (
    DurableRangeStore, InjectedCrash, SNAP_HEAD, WAL_ENTRY,
)
from index001_workload_io import workload_traces


@dataclass(frozen=True)
class Weights:
    write: int
    recovery: int
    footprint: int

    def __post_init__(self):
        if any(not isinstance(v, int) or v < 0
               for v in (self.write, self.recovery, self.footprint)):
            raise ValueError("all resource weights must be nonnegative integers")
        if self.write + self.recovery + self.footprint == 0:
            raise ValueError("some resource dimension must be priced")


def _inputs(size, restarts, checkpoints, max_steady_age, peak_cap):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be positive")
    if any(not isinstance(r, int) or r < 0 for r in restarts):
        raise ValueError("restart multiplicities must be nonnegative integers")
    if (any(not isinstance(t, int) for t in checkpoints)
            or tuple(checkpoints) != tuple(sorted(set(checkpoints)))
            or any(not 1 <= t <= len(restarts) for t in checkpoints)):
        raise ValueError("checkpoints must be unique sorted update indices")
    if max_steady_age is not None and (
            not isinstance(max_steady_age, int) or max_steady_age < 0):
        raise ValueError("invalid steady WAL age cap")
    if peak_cap is not None and (
            not isinstance(peak_cap, int) or peak_cap <= 0):
        raise ValueError("invalid temporary peak-byte cap")


def score(size, restarts, checkpoints=(), weights=Weights(1, 1, 0),
          max_steady_age=None, peak_cap=None):
    """Exact cost vector and weighted score, including initial snapshot.

    A clean restart is a *read observation*, not an additional user update.
    Returns None for infeasible schedules under caps.
    """
    restarts = tuple(restarts)
    checkpoints = tuple(checkpoints)
    _inputs(size, restarts, checkpoints, max_steady_age, peak_cap)
    if not isinstance(weights, Weights):
        raise ValueError("invalid weights")
    snapshot = SNAP_HEAD.size + 4 * size + 4
    entry = WAL_ENTRY.size
    if peak_cap is not None and snapshot > peak_cap:
        return None
    age = 0
    written = snapshot + entry * len(restarts)
    read = 0
    footprint = 0
    peak = snapshot
    max_age = 0
    ages = []
    checkpoint_set = set(checkpoints)
    for time, restart_count in enumerate(restarts, 1):
        age_before = age + 1
        if time in checkpoint_set:
            transient = 2 * snapshot + entry * age_before
            peak = max(peak, transient)
            if peak_cap is not None and transient > peak_cap:
                return None
            age = 0
            written += snapshot
        else:
            age = age_before
        steady = snapshot + entry * age
        peak = max(peak, steady)
        if max_steady_age is not None and age > max_steady_age:
            return None
        if peak_cap is not None and steady > peak_cap:
            return None
        max_age = max(max_age, age)
        ages.append(age)
        read += restart_count * steady
        footprint += steady
    return {
        "checkpoints": list(checkpoints),
        "steady_wal_ages": ages,
        "written_bytes": written,
        "recovery_read_bytes": read,
        "steady_footprint_byte_steps": footprint,
        "peak_path_bytes": peak,
        "max_steady_wal_records": max_age,
        "weighted_cost": weights.write * written + weights.recovery * read
                         + weights.footprint * footprint,
    }


def optimal_offline(size, restarts, weights=Weights(1, 1, 0),
                    max_steady_age=None, peak_cap=None):
    """O(U^2) time/O(U^2) witness memory; exact clairvoyant optimum.

    Dynamic state is last checkpoint age, tie-break by checkpoint tuple.
    """
    restarts = tuple(restarts)
    _inputs(size, restarts, (), max_steady_age, peak_cap)
    if not isinstance(weights, Weights):
        raise ValueError("invalid weights")
    snapshot = SNAP_HEAD.size + size * 4 + 4
    entry = WAL_ENTRY.size
    if peak_cap is not None and snapshot > peak_cap:
        return None
    # Dictionary: age -> (variable cost, lexicographically least path).
    dp = {0: (0, ())}
    for time, count in enumerate(restarts, 1):
        nxt = {}
        for age, (cost, path) in dp.items():
            before = age + 1
            for checkpoint in (False, True):
                if checkpoint:
                    peak = 2 * snapshot + entry * before
                    next_age = 0
                else:
                    peak = snapshot + entry * before
                    next_age = before
                if ((max_steady_age is not None and next_age > max_steady_age)
                        or (peak_cap is not None and peak > peak_cap)):
                    continue
                add = ((weights.recovery * count + weights.footprint)
                       * (snapshot + entry * next_age))
                if checkpoint:
                    add += weights.write * snapshot
                candidate = (cost + add,
                             path + ((time,) if checkpoint else ()))
                if next_age not in nxt or candidate < nxt[next_age]:
                    nxt[next_age] = candidate
        dp = nxt
        if not dp:
            return None
    path = min(dp.values(), key=lambda p: p)[1]
    result = score(size, restarts, path, weights, max_steady_age, peak_cap)
    if result is None:
        raise AssertionError("DP returned infeasible policy")
    return result


def exhaustive_offline(size, restarts, weights=Weights(1, 1, 0),
                       max_steady_age=None, peak_cap=None):
    """Independent checkpoint-subset search; only for U<=12."""
    restarts = tuple(restarts)
    if len(restarts) > 12:
        raise ValueError("enumeration restricted to at most 12 updates")
    best = None
    for bits in itertools.product((False, True), repeat=len(restarts)):
        path = tuple(i + 1 for i, mark in enumerate(bits) if mark)
        result = score(size, restarts, path, weights, max_steady_age, peak_cap)
        if result is None:
            continue
        key = (result["weighted_cost"], path)
        if best is None or key < best[0]:
            best = (key, result)
    return None if best is None else best[1]


def _dense_runs(values, lo, hi):
    if lo == hi:
        return ()
    out = []
    first = lo
    for i in range(lo + 1, hi + 1):
        if i == hi or values[i] != values[first]:
            out.append((first, i, values[first]))
            first = i
    return tuple(out)


def _assert_state(store, values):
    for i, value in enumerate(values):
        if store.lookup(i) != value:
            raise AssertionError("durable map diverged from independent dense oracle")
    n = len(values)
    for lo, hi in ((0, n), (0, 0), (n // 4, 3 * n // 4), (n - 1, n)):
        if store.scan(lo, hi) != _dense_runs(values, lo, hi):
            raise AssertionError("incorrect exact range scan")


def actual_filesystem_trace(operations, restarts, checkpoints, size=32,
                            weights=Weights(1, 1, 0)):
    """Check predicted cost vector against *real* POSIX file operations.

    Excludes the initial construction-time snapshot read from explicit
    'restart' reads and never treats fsync/truncate as zero NAND writes.
    """
    restarts = tuple(restarts)
    checkpoints = tuple(checkpoints)
    if len(restarts) != len(operations):
        raise ValueError("restart horizon must match update trace")
    predicted = score(size, restarts, checkpoints, weights)
    expected = [0] * size
    entry = WAL_ENTRY.size
    snap_bytes = SNAP_HEAD.size + size * 4 + 4
    written = 0
    reopened_read = 0
    byte_steps = 0
    wal_age = 0
    fsync_files = 0
    fsync_dirs = 0
    truncates = 0
    observations = 0
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        store = DurableRangeStore(folder, size)
        written += store.ledger.total_application_written
        for time, ((lo, hi, v), repeats) in enumerate(zip(operations, restarts), 1):
            if not (0 <= lo < hi <= size):
                raise ValueError("invalid trace operation")
            expected[lo:hi] = [v] * (hi - lo)
            before = store.ledger.total_application_written
            before_sync = store.ledger.fsync_files
            before_dir = store.ledger.fsync_dirs
            before_trunc = store.ledger.wal_truncates
            store.assign(lo, hi, v)
            wal_age += 1
            if time in checkpoints:
                store.checkpoint()
                wal_age = 0
            written += store.ledger.total_application_written - before
            fsync_files += store.ledger.fsync_files - before_sync
            fsync_dirs += store.ledger.fsync_dirs - before_dir
            truncates += store.ledger.wal_truncates - before_trunc
            snapshot_len = store.snapshot_path.stat().st_size
            wal_len = store.wal_path.stat().st_size
            if snapshot_len != snap_bytes or wal_len != entry * wal_age:
                raise AssertionError("post-operation physical file length differs")
            if store.folder.joinpath("snapshot.tmp").exists():
                raise AssertionError("successful checkpoint left temporary image")
            byte_steps += snapshot_len + wal_len
            _assert_state(store, expected)
            for _ in range(repeats):
                store = DurableRangeStore(folder, size)
                observations += 1
                reopened_read += store.ledger.total_application_read
                if store.ledger.snapshot_read != snap_bytes:
                    raise AssertionError("restart snapshot read length mismatch")
                if store.ledger.wal_read != entry * wal_age:
                    raise AssertionError("restart WAL read length mismatch")
                _assert_state(store, expected)
        _assert_state(DurableRangeStore(folder, size), expected)
        result = {
            "written_bytes": written,
            "recovery_read_bytes": reopened_read,
            "steady_footprint_byte_steps": byte_steps,
            "checkpoint_events": truncates,
            "observed_restarts": observations,
            "fsync_files_during_updates": fsync_files,
            "fsync_dirs_during_updates": fsync_dirs,
            "steady_snapshot_bytes": (folder / "snapshot.bin").stat().st_size,
            "steady_wal_bytes": (folder / "wal.bin").stat().st_size,
        }
    if (written != predicted["written_bytes"]
            or reopened_read != predicted["recovery_read_bytes"]
            or byte_steps != predicted["steady_footprint_byte_steps"]):
        raise AssertionError("independent filesystem ledger disagrees with formal cost vector")
    return result


def checkpoint_orphan_observation(size=8, failpoint="after_checkpoint_partial"):
    """Measure a staged temp image after a *simulated* interrupted checkpoint."""
    if failpoint not in ("after_checkpoint_partial", "after_checkpoint_sync",
                         "after_checkpoint_replace", "after_checkpoint_dirsync",
                         "after_wal_truncate"):
        raise ValueError("unsupported fault stage")
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        store = DurableRangeStore(folder, size)
        store.assign(1, size, 7)
        try:
            store.checkpoint(failure=failpoint)
            raise AssertionError("expected injected stop")
        except InjectedCrash:
            pass
        before = {name: (folder / name).stat().st_size
                  if (folder / name).exists() else None
                  for name in ("snapshot.bin", "snapshot.tmp", "wal.bin")}
        recovered = DurableRangeStore(folder, size)
        _assert_state(recovered, [0] + [7] * (size - 1))
        return {
            "failure": failpoint,
            "files_after_stop": before,
            "recovered_seq": recovered.seq,
            "reopen_application_read_bytes": recovered.ledger.total_application_read,
            "orphan_temp_not_auto_reclaimed": (folder / "snapshot.tmp").exists(),
        }


def build_report():
    tasks = workload_traces()
    out = {}
    for name, steps in tasks.items():
        u = len(steps)
        if name == "nested_ranges":
            counts = tuple(2 if t in (3, u - 1) else 0 for t in range(1, u + 1))
        elif name == "alternating_singletons":
            counts = tuple(1 if t % 4 == 0 else 0 for t in range(1, u + 1))
        else:
            counts = tuple(1 if t == u else 0 for t in range(1, u + 1))
        weights = Weights(1, 6, 0)
        opt = optimal_offline(32, counts, weights)
        brute = exhaustive_offline(32, counts, weights)
        if opt != brute:
            raise AssertionError("offline DP not equal to independent enumeration")
        actual = actual_filesystem_trace(steps, counts, opt["checkpoints"], 32, weights)
        fixed = {}
        for t in (1, 4, 16):
            path = tuple(k for k in range(1, u + 1) if k % t == 0)
            fixed[str(t)] = score(32, counts, path, weights)
        out[name] = {
            "updates": u,
            "restart_observations": list(counts),
            "offline_optimum": opt,
            "filesystem_oracle": actual,
            "periodic": fixed,
        }
    return {
        "schema": "mathlab.index001.g2b2b.checkpoint-policy.v1",
        "classification": "OFFLINE_EXACT_REFERENCE_MODEL_NOT_ONLINE_THEOREM",
        "hardware_nand_bytes": "NOT_MEASURED",
        "device_durability": "NOT_PROVED",
        "workloads": out,
        "staged_fault_examples": [
            checkpoint_orphan_observation(8, "after_checkpoint_partial"),
            checkpoint_orphan_observation(8, "after_checkpoint_sync"),
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        for name, row in report["workloads"].items():
            policy = row["offline_optimum"]
            print(f"{name}: checkpoints={policy['checkpoints']}; "
                  f"W={policy['written_bytes']}; R={policy['recovery_read_bytes']}; "
                  f"F={policy['steady_footprint_byte_steps']}; "
                  f"J={policy['weighted_cost']}")
        print("INDEX001_G2B2B_CHECKPOINT_POLICY_ORACLE_PASS")


if __name__ == "__main__":
    main()
