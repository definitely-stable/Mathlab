"""INDEX-001 G2-B4-C0: priced one-level WAL comparator (model-only).

No SSD I/O, crash/power loss, concurrency, rank/select or lower bound claim.
The three reference schedules intentionally differ; the exact ledger makes
those differences visible rather than treating a page diff as an actual syscall.
"""
from dataclasses import dataclass
from itertools import product
import json

from index001_page_recourse import (
    image_for, lookup_page_probe, page_difference, packed_image, slot_capacity,
)
from index001_variable_checkpoint import encode_wal, decode_wal, decode_snapshot


def pages(length, block):
    if length < 0 or block < 4:
        raise ValueError("bad physical geometry")
    return (length + block - 1) // block


def assign(values, operation):
    n = len(values)
    lo, hi, value = operation
    if not (0 <= lo < hi <= n and value in (0, 1)):
        raise ValueError("invalid range assign")
    out = list(values)
    out[lo:hi] = [value] * (hi - lo)
    return tuple(out)


def budget(values, block, alpha=4, beta=2, m_bits=0, gamma=0):
    if any(type(z) is not int or z < 0 for z in (alpha, beta, m_bits, gamma)):
        raise ValueError("nonnegative integer budgets required")
    return alpha * len(packed_image(values)) + beta * block + gamma * (m_bits + 7) // 8


def flat_update(before, operation, block, group, layout):
    if layout not in ("packed", "segmented"):
        raise ValueError("unknown flat layout")
    after = assign(before, operation)
    old = image_for(layout, before, group, block)
    new = image_for(layout, after, group, block)
    diff = page_difference(old, new, block)
    d0, d1 = pages(len(old), block) * block, pages(len(new), block) * block
    lo, hi, _ = operation
    read_pages = (pages(len(old), block) if layout == "packed" else
                  ((hi - 1) // group - lo // group + 1) *
                  pages(slot_capacity(group, block), block))
    return {
        "layout": layout, "state": after, "disk_bytes_before": d0,
        "disk_bytes_after": d1, "peak_bytes": max(d0, d1),
        "written_model_bytes": diff["changed_page_positions"] * block,
        "changed_page_images": diff["changed_page_positions"],
        "allocated_pages": diff["pages_added"],
        "retired_pages": diff["pages_removed"],
        "materialized_checkpoint_payload": 0, "persistent_aux_ram_bits": 0,
        "read_update_pages": read_pages,
        "max_point_query_pages": max(
            len(lookup_page_probe(layout, after, p, group, block)["page_indices"])
            for p in range(len(after))),
        "operation": "same_offset_overwrite",
    }


@dataclass(frozen=True)
class WalState:
    base: tuple
    frames: tuple  # Tuple[bytes] (exact RW CRC frames)
    latest: tuple


def initial_wal(values):
    values = tuple(values)
    if not values or any(v not in (0, 1) for v in values):
        raise ValueError("nonempty binary state")
    return WalState(values, (), values)


def wal_disk_bytes(state, block):
    log_length = sum(map(len, state.frames))
    return (pages(len(packed_image(state.base)), block) +
            pages(log_length, block) + 1) * block  # control page


def wal_lookup(state, pos, block):
    if not 0 <= pos < len(state.latest):
        raise ValueError("bad point query")
    # Control is a real persistent, consulted page (not an in-RAM directory).
    log_size = sum(map(len, state.frames))
    unique_reads = 1 + pages(log_size, block)
    seen = None
    for frame in state.frames:
        lo, hi, value = decode_wal(len(state.base), frame)
        if lo <= pos < hi:
            seen = value
    if seen is not None:
        return seen, unique_reads
    base_info = lookup_page_probe("packed", state.base, pos, min(8, len(state.base)), block)
    return base_info["value"], unique_reads + len(base_info["page_indices"])


def wal_step(state, operation, block=32, threshold=3):
    if type(threshold) is not int or threshold < 1:
        raise ValueError("threshold must be positive")
    updated = assign(state.latest, operation)
    old_d = wal_disk_bytes(state, block)
    if len(state.frames) + 1 >= threshold:
        # Two-generation checkpoint: new base allocated before old base/log GC.
        new_base_bytes = len(packed_image(updated))
        allocated = pages(new_base_bytes, block)
        result = initial_wal(updated)
        written = (allocated + 1) * block  # immutable new base + control
        peak = old_d + allocated * block
        retired = (pages(len(packed_image(state.base)), block) +
                   pages(sum(map(len, state.frames)), block))
        moved = new_base_bytes
        mode = "checkpoint"
        read_pages = 1 + pages(len(packed_image(state.base)), block) + pages(
            sum(map(len, state.frames)), block)
        xchanged = 0  # not comparable to same-offset page-difference X
    else:
        frame = encode_wal(len(state.base), *operation)
        if decode_wal(len(state.base), frame) != tuple(operation):
            raise AssertionError("WAL encode/decode mismatch")
        old_log = b"".join(state.frames)
        new_log = old_log + frame
        diff = page_difference(old_log, new_log, block)
        result = WalState(state.base, state.frames + (frame,), updated)
        # Whole page image rewrite of tail/log plus one control page.
        written = (diff["changed_page_positions"] + 1) * block
        allocated = diff["pages_added"]
        peak = wal_disk_bytes(result, block)
        retired = 0
        moved = 0
        mode = "wal_append"
        read_pages = 1 + int(bool(len(old_log) and len(old_log) % block))
        xchanged = diff["changed_page_positions"]
    new_d = wal_disk_bytes(result, block)
    max_q = max(wal_lookup(result, p, block)[1] for p in range(len(updated)))
    return result, {
        "layout": "wal", "operation": mode, "state": updated,
        "disk_bytes_before": old_d, "disk_bytes_after": new_d,
        "peak_bytes": max(old_d, new_d, peak),
        "written_model_bytes": written, "changed_page_images": xchanged,
        "allocated_pages": allocated, "retired_pages": retired,
        "materialized_checkpoint_payload": moved,
        "persistent_aux_ram_bits": 0, "read_update_pages": read_pages,
        "max_point_query_pages": max_q,
        "wal_frames_after": len(result.frames),
        "log_payload_bytes_after": sum(map(len, result.frames)),
    }


def compare_trace(initial, operations, block=32, group=8, threshold=3,
                  alpha=4, beta=2):
    initial = tuple(initial)
    if not initial or any(v not in (0, 1) for v in initial):
        raise ValueError("invalid initial state")
    if block < 4 or not (1 <= group <= len(initial)):
        raise ValueError("bad geometry")
    truth = initial
    wal = initial_wal(initial)
    rows = []
    for operation in operations:
        after = assign(truth, operation)
        results = [flat_update(truth, operation, block, group, layout)
                   for layout in ("packed", "segmented")]
        wal, log_result = wal_step(wal, operation, block, threshold)
        results.append(log_result)
        limit = budget(after, block, alpha, beta)
        for row in results:
            if row["state"] != after:
                raise AssertionError("dense oracle diverged")
            row["within_steady_budget"] = row["disk_bytes_after"] <= limit
            row["within_peak_budget"] = row["peak_bytes"] <= limit
            row["budget_bytes"] = limit
            row["state"] = "".join(map(str, row["state"]))
        for p, target in enumerate(after):
            value, _ = wal_lookup(wal, p, block)
            if value != target:
                raise AssertionError("last-write-wins WAL lookup incorrect")
        rows.append({"op": list(operation), "strategies": results})
        truth = after
    return rows



def bounded_epoch_limit(base, block, max_snapshot_bytes, min_frame_bytes,
                        alpha=4, beta=2, m_bits=0, gamma=0):
    """Exact upper bound on append count for THIS unindexed WAL policy.

    This is a necessary inequality only, not a sufficient schedule or a
    generic lower bound for competing dynamic structures.
    """
    if min_frame_bytes < 1 or max_snapshot_bytes < 0:
        raise ValueError("positive frame and nonnegative snapshot size needed")
    ceiling_budget = (alpha * max_snapshot_bytes + beta * block +
                      gamma * ((m_bits + 7) // 8))
    h = ceiling_budget // block - 1 - pages(len(packed_image(base)), block)
    return {"max_log_pages": h,
            "max_uncheckpointed_appends": max(-1, (h * block) // min_frame_bytes),
            "budget_upper_bytes": ceiling_budget}


def report():
    z = (0,) * 64
    observed = compare_trace(z, [(0, 1, 1), (0, 1, 0), (0, 1, 1),
                                 (0, 1, 0), (8, 56, 1), (8, 56, 0)],
                             block=32, group=8, threshold=3)
    slots = len(image_for("segmented", z, 8, 32))
    zero_s = len(packed_image(z))
    assert zero_s == 12 and slots == 256 and budget(z, 32) == 112
    assert not slots <= budget(z, 32)
    assert decode_snapshot(packed_image(z)) == z
    cap = bounded_epoch_limit(z, 32, 14, len(encode_wal(64, 0, 1, 1)))
    assert cap["max_log_pages"] == 1 and cap["max_uncheckpointed_appends"] == 3
    return {
        "schema": "mathlab.index001.g2b4c0.priced-wal.v1",
        "classification": "FINITE_COUNTERMODEL_RESTRICTED_FIXED_SLOT_SPACE_BOUND",
        "main_parent": "dd90dd634e4e600cea0d14e302b215b698758ec5",
        "no_nand_or_syscall_measurement": True,
        "zero64": {"packed_bytes": zero_s, "slots_bytes": slots,
                   "budget_bytes": budget(z, 32), "effective_hot_toggle_epoch_bound": cap},
        "trace": observed,
    }


if __name__ == "__main__":
    output = report()
    print(json.dumps({"schema": output["schema"],
                      "classification": output["classification"],
                      "zero64": output["zero64"],
                      "operations": [
                          {"op": r["op"],
                           "costs": {s["layout"]: {
                               "W": s["written_model_bytes"],
                               "D": s["disk_bytes_after"],
                               "P": s["peak_bytes"],
                               "Q": s["max_point_query_pages"],
                               "R_update": s["read_update_pages"],
                               "steady_ok": s["within_steady_budget"],
                               "peak_ok": s["within_peak_budget"],
                               "mode": s["operation"]}
                            for s in r["strategies"]}}
                          for r in output["trace"]]},
                     sort_keys=True, indent=2))
    print("INDEX001_G2B4C0_PRICED_WAL_PASS")
