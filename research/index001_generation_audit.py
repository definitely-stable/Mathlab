"""INDEX-001 G2-B3-A deterministic extra-manifest cost and crash-state audit.

Only bytes returned by application writes and bytes read on the POSIX test
filesystem; no SSD NAND, concurrency or sudden real power-loss assertions.
"""
import argparse
import json
from pathlib import Path
import tempfile

from index001_durable import DurableRangeStore, InjectedCrash
from index001_generations import GenerationRangeStore, MANIFEST_LENGTH


def experiment(size=8):
    if not isinstance(size, int) or size < 4:
        raise ValueError("experiment needs >=4 cells")
    operations = ((0, size, 1), (1, size - 1, 2),
                  (2, 4, 3), (0, 1, 4))
    with tempfile.TemporaryDirectory() as root:
        root = Path(root)
        old = DurableRangeStore(root / "one-slot", size)
        new = GenerationRangeStore(root / "two-slot", size)
        expected = [0] * size
        for i, (lo, hi, val) in enumerate(operations):
            old.assign(lo, hi, val)
            new.assign(lo, hi, val)
            expected[lo:hi] = [val] * (hi - lo)
            if i in (1, 3):
                old.checkpoint()
                new.checkpoint()
            for pos in range(size):
                if old.lookup(pos) != expected[pos] or new.lookup(pos) != expected[pos]:
                    raise AssertionError("independent dense oracle mismatch")
        actual_old = old.ledger.total_application_written
        actual_new = new.ledger.total_application_written
        snapshot_bytes = 24 + size * 4
        wal_bytes = 28 * len(operations)
        checkpoints = 2
        if actual_old != (1 + checkpoints) * snapshot_bytes + wal_bytes:
            raise AssertionError("unexpected 1-slot write bytes")
        if actual_new != ((1 + checkpoints)
                          * (snapshot_bytes + MANIFEST_LENGTH) + wal_bytes):
            raise AssertionError("unexpected 2-slot write bytes")
        if actual_new - actual_old != (1 + checkpoints) * MANIFEST_LENGTH:
            raise AssertionError("manifest metadata charged more/less than once")
        read_old = DurableRangeStore(root / "one-slot", size)
        read_new = GenerationRangeStore(root / "two-slot", size)
        if read_new.ledger.total_application_read != (
                read_old.ledger.total_application_read + MANIFEST_LENGTH):
            raise AssertionError("manifest read-byte difference incorrect")
        for i in range(size):
            if read_old.lookup(i) != expected[i] or read_new.lookup(i) != expected[i]:
                raise AssertionError("recovery differs from dense oracle")
        pre_gc = sum(x for x in new.file_lengths().values() if x is not None)
        if not new.gc_inactive():
            raise AssertionError("expected retained inactive generation")
        post_gc = sum(x for x in new.file_lengths().values() if x is not None)
        if pre_gc - post_gc != snapshot_bytes:
            raise AssertionError("retained generation file size accounting incorrect")
        return {
            "universe": size,
            "operations": len(operations),
            "checkpoints": checkpoints,
            "snapshot_frame": snapshot_bytes,
            "manifest_frame": MANIFEST_LENGTH,
            "one_slot_application_written": actual_old,
            "two_slot_application_written": actual_new,
            "manifest_extra_written": actual_new - actual_old,
            "one_slot_reopen_read": read_old.ledger.total_application_read,
            "two_slot_reopen_read": read_new.ledger.total_application_read,
            "retained_bytes_before_gc": pre_gc,
            "retained_bytes_after_gc": post_gc,
            "gc_unlinks": new.ledger.inactive_gc_unlinks,
        }


def fault_report(size=8):
    stages = ("after_snapshot_partial", "after_snapshot_sync",
              "after_snapshot_replace", "after_snapshot_dirsync",
              "after_manifest_partial", "after_manifest_sync",
              "after_manifest_replace", "after_manifest_dirsync",
              "after_wal_truncate")
    results = []
    for stage in stages:
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, size)
            st.assign(1, size - 1, 3)
            try:
                st.checkpoint(failure=stage)
                raise AssertionError("fault gate missing")
            except InjectedCrash:
                pass
            before = st.file_lengths()
            observed = GenerationRangeStore(temp, size)
            for i in range(size):
                expect = 3 if 1 <= i < size - 1 else 0
                if observed.lookup(i) != expect:
                    raise AssertionError("injected checkpoint lost confirmed value")
            results.append({
                "stage": stage,
                "active_slot_after_recovery": observed.active_slot,
                "recovered_seq": observed.seq,
                "orphan_temp_bytes": sum(v for k, v in before.items()
                                         if k.endswith(".tmp") and v is not None),
                "wal_bytes_before_restart": before["wal.bin"],
            })
    return results


def build_report():
    return {
        "schema": "mathlab.index001.g2b3a.generation-reference.v1",
        "classification": "POSIX_PROCESS_STOP_BOUNDARIES_NOT_HARDWARE_CRASH_PROOF",
        "physical_ssd_nand_bytes": "NOT_MEASURED",
        "concurrent_writer_safety": "NOT_MODELED",
        "reference_cost": experiment(),
        "checkpoint_fault_matrix": fault_report(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = build_report()
    if args.json:
        print(json.dumps(result, sort_keys=True, indent=2))
    else:
        c = result["reference_cost"]
        print(f"1-slot W={c['one_slot_application_written']} 2-slot W={c['two_slot_application_written']} "
              f"manifest extra={c['manifest_extra_written']}")
        print(f"reopen reads: {c['one_slot_reopen_read']} -> {c['two_slot_reopen_read']}; "
              f"retained bytes {c['retained_bytes_before_gc']} -> {c['retained_bytes_after_gc']}")
        print(f"Verified checkpoint fault gates: {len(result['checkpoint_fault_matrix'])}")
        print("INDEX001_G2B3A_GENERATION_REFERENCE_PASS")


if __name__ == "__main__":
    main()
