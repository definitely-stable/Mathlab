"""INDEX-001 G2-B2-A: reproducible POSIX application-byte cost comparators.

This is NOT physical SSD/NAND write amplification, real page-I/O measurement,
crash-proof hardware validation, performance timing, or a new theorem.
Only stdlib and the G2-B1 reference; fully deterministic workloads.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import tempfile

from index001_durable import DurableRangeStore, SnapshotReference, SNAP_HEAD, WAL_ENTRY


def workload_traces(size=32):
    if size != 32:
        raise ValueError("G2-B2-A pinned workloads require N=32")
    return {
        "full_overwrite": [(0, size, i + 1) for i in range(8)],
        "alternating_singletons": [((7 * i) % size,
                                    (7 * i) % size + 1,
                                    (i % 3) + 1) for i in range(12)],
        "nested_ranges": [(i, size - i, i + 1) for i in range(10)],
        "repeated_hot_region": [(11 + i % 3, 15 + i % 3, i + 1)
                                for i in range(12)],
    }


def _oracle_scan(values, lo, hi):
    if lo == hi:
        return ()
    out = []
    left = lo
    for p in range(lo + 1, hi + 1):
        if p == hi or values[p] != values[left]:
            out.append((left, p, values[left]))
            left = p
    return tuple(out)


def _assert_exact(store, values):
    if len(values) != store.size:
        raise AssertionError("wrong universe")
    for i, v in enumerate(values):
        if store.lookup(i) != v:
            raise AssertionError(f"incorrect point at {i}")
    n = len(values)
    for lo, hi in ((0, n), (0, 0), (min(1, n), min(11, n)),
                   (min(10, n), min(17, n)), (n - 1, n)):
        if store.scan(lo, hi) != _oracle_scan(values, lo, hi):
            raise AssertionError(f"incorrect scan [{lo},{hi})")


def _amplification(written, assigned):
    if assigned == 0:
        return None
    frac = Fraction(written, 4 * assigned)
    return {"numerator": frac.numerator, "denominator": frac.denominator}


def compare_trace(operations, size=32, thresholds=(1, 4, 16)):
    """Return an exact accounting report for only acknowledged, no-fault writes."""
    if not isinstance(size, int) or size < 1:
        raise ValueError("invalid size")
    if (not thresholds or len(set(thresholds)) != len(thresholds)
            or any(not isinstance(t, int) or t < 1 for t in thresholds)):
        raise ValueError("positive distinct checkpoint thresholds required")
    if any(not (0 <= lo < hi <= size and 0 <= value <= 0xffffffff)
           for lo, hi, value in operations):
        raise ValueError("invalid pinned operation")
    expected = [0] * size
    assigned = sum(hi - lo for lo, hi, _ in operations)
    snapshot_bytes = SNAP_HEAD.size + 4 * size + 4
    with tempfile.TemporaryDirectory() as root:
        root = Path(root)
        direct = SnapshotReference(root / "snapshot-only", size)
        for lo, hi, v in operations:
            direct.assign(lo, hi, v)
            expected[lo:hi] = [v] * (hi - lo)
            _assert_exact(direct, expected)
        direct_out = {
            "written_bytes": direct.ledger.total_application_written,
            "expected_bytes": (1 + len(operations)) * snapshot_bytes,
            "write_calls": direct.ledger.application_write_calls,
            "file_syncs": direct.ledger.fsync_files,
            "directory_syncs": direct.ledger.fsync_dirs,
            "amplification": _amplification(direct.ledger.total_application_written,
                                            assigned),
        }
        if direct_out["written_bytes"] != direct_out["expected_bytes"]:
            raise AssertionError("snapshot-only writes contradict fixed-frame formula")
        direct_restart = SnapshotReference(root / "snapshot-only", size)
        _assert_exact(direct_restart, expected)
        direct_out["restart_read_bytes"] = direct_restart.ledger.total_application_read

        wal_out = []
        for threshold in thresholds:
            path = root / f"wal-{threshold}"
            obj = DurableRangeStore(path, size)
            prefix = [0] * size
            pending = 0
            for lo, hi, v in operations:
                obj.assign(lo, hi, v)
                prefix[lo:hi] = [v] * (hi - lo)
                pending += 1
                if pending == threshold:
                    obj.checkpoint()
                    pending = 0
                _assert_exact(obj, prefix)
            _assert_exact(obj, expected)
            count = len(operations)
            checkpoints = count // threshold
            tail = count % threshold
            predicted = (1 + checkpoints) * snapshot_bytes + count * WAL_ENTRY.size
            actual = obj.ledger.total_application_written
            if obj.ledger.wal_truncates != checkpoints or predicted != actual:
                raise AssertionError("WAL/compaction bytes disagree with frame arithmetic")
            if obj.wal_path.stat().st_size != tail * WAL_ENTRY.size:
                raise AssertionError("unexpected persistent WAL suffix length")
            rebooted = DurableRangeStore(path, size)
            _assert_exact(rebooted, expected)
            if rebooted.ledger.wal_read != tail * WAL_ENTRY.size:
                raise AssertionError("WAL recovery read not equal remaining complete records")
            wal_out.append({
                "threshold": threshold,
                "checkpoints": checkpoints,
                "remaining_log_records": tail,
                "written_bytes": actual,
                "expected_bytes": predicted,
                "wal_bytes": obj.ledger.wal_written,
                "snapshot_bytes": obj.ledger.snapshot_written,
                "write_calls": obj.ledger.application_write_calls,
                "file_syncs": obj.ledger.fsync_files,
                "directory_syncs": obj.ledger.fsync_dirs,
                "wal_truncation_events": obj.ledger.wal_truncates,
                "restart_read_bytes": rebooted.ledger.total_application_read,
                "amplification": _amplification(actual, assigned),
            })
        return {
            "size": size,
            "updates": len(operations),
            "logical_blocks_assigned": assigned,
            "snapshot_frame_bytes": snapshot_bytes,
            "wal_frame_bytes": WAL_ENTRY.size,
            "snapshot_only": direct_out,
            "wal_policies": wal_out,
        }


def build_report():
    return {
        "schema": "mathlab.index001.g2b2.application-io.v1",
        "classification": "DETERMINISTIC_POSIX_APPLICATION_IO_NOT_DEVICE_IO",
        "scope": "one writer; fixed full snapshots; no fault injection or concurrent access",
        "timing_metrics": "NOT_MEASURED",
        "nand_physical_bytes": "NOT_MEASURED",
        "workloads": {
            name: compare_trace(steps)
            for name, steps in workload_traces().items()
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="print deterministic JSON report")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        for name, row in report["workloads"].items():
            direct = row["snapshot_only"]["written_bytes"]
            comparators = ", ".join(
                f"T{p['threshold']}={p['written_bytes']}"
                for p in row["wal_policies"])
            print(f"{name}: updates={row['updates']} "
                  f"snapshot={direct} bytes; WAL {comparators}")
        print("INDEX001_APPLICATION_IO_EXACT_ACCOUNTING_PASS")


if __name__ == "__main__":
    main()
