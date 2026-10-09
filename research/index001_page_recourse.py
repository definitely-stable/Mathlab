"""INDEX-001 G2-B4-B: logical page-image oracle, not physical SSD/NAND I/O.

Three exact binary lookup representations: one contiguous canonical RLE image,
fixed-position independently CRC-encoded RLE slots, and raw one-byte cells.
No file system, atomic write, crash, cache, or external-memory lower-bound claim.
"""
from dataclasses import dataclass
from itertools import product
import argparse
import json

from index001_variable_checkpoint import (
    encode_snapshot, decode_snapshot, parse_uvarint, uvarint,
)

def check_parameters(n, page_size, group):
    if type(n) is not int or n < 1 or type(page_size) is not int or page_size < 4:
        raise ValueError("N>=1 and B>=4 integers required")
    if type(group) is not int or not 1 <= group <= n:
        raise ValueError("group width must be in 1..N")


def runs_and_boundaries(values):
    values = tuple(values)
    if not values or any(type(x) is not int or x not in (0, 1) for x in values):
        raise ValueError("nonempty binary state required")
    return frozenset(i for i in range(1, len(values))
                     if values[i] != values[i-1])


def padded_pages(data, page_size):
    if type(page_size) is not int or page_size < 4:
        raise ValueError("invalid page size")
    return tuple(data[pos:pos+page_size].ljust(page_size, b"\x00")
                 for pos in range(0, len(data), page_size))


def page_difference(old, new, page_size):
    """Changed logical page *images*, NOT actual application write calls."""
    left, right = padded_pages(old, page_size), padded_pages(new, page_size)
    count = max(len(left), len(right))
    changed = tuple(i for i in range(count)
                    if (left[i] if i < len(left) else bytes(page_size)) !=
                       (right[i] if i < len(right) else bytes(page_size)))
    shared = tuple(i for i in changed if i < min(len(left), len(right)))
    return {
        "changed_page_indices": list(changed),
        "shared_changed_pages": len(shared),
        "changed_page_positions": len(changed),
        "modeled_page_image_bytes": len(changed) * page_size,
        "allocated_pages_before": len(left),
        "allocated_pages_after": len(right),
        "pages_added": max(0, len(right) - len(left)),
        "pages_removed": max(0, len(left) - len(right)),
    }


def slot_capacity(group, page_size):
    if type(group) is not int or group < 1:
        raise ValueError("invalid group")
    if type(page_size) is not int or page_size < 4:
        raise ValueError("invalid page")
    v = len(uvarint(group))
    bound = 8 + 2*v + group*(v+1)
    return ((bound + page_size - 1)//page_size)*page_size


def packed_image(values):
    return encode_snapshot(tuple(values))


def segmented_image(values, group, page_size):
    """Concatenate fixed-slot independently encoded IXR1 blocks.

    Length of each used frame is derivable by scanning its canonical run
    payload, so it is not persisted in an auxiliary in-RAM directory.
    """
    values = tuple(values)
    n = len(values)
    check_parameters(n, page_size, group)
    capacity = slot_capacity(group, page_size)
    out = bytearray()
    for lo in range(0, n, group):
        part = values[lo:lo+group]
        frame = encode_snapshot(part)
        if len(frame) > capacity:
            raise AssertionError("conservative slot capacity overflow")
        out.extend(frame)
        out.extend(b"\x00"*(capacity-len(frame)))
    return bytes(out)


def raw_image(values):
    return bytes(tuple(values))


def image_for(layout, values, group, page_size):
    if layout == "packed":
        return packed_image(values)
    if layout == "segmented":
        return segmented_image(values, group, page_size)
    if layout == "raw":
        return raw_image(values)
    raise ValueError("unknown layout")


def _prefix_lookup(frame, local_index):
    """Read-only *unchecked CRC* prefix parser.

    Returns (value, bytes-touched-in-frame); integrity of the file is a
    prerequisite. No global out-of-band boundary cache or full CRC check.
    """
    if not frame.startswith(b"IXR1"):
        raise ValueError("bad frame magic")
    n, pos = parse_uvarint(frame, 4)
    k, pos = parse_uvarint(frame, pos)
    if not 0 <= local_index < n or not 1 <= k <= n:
        raise ValueError("invalid lookup")
    reached = 0
    previous = None
    for _ in range(k):
        length, pos = parse_uvarint(frame, pos)
        if length < 1 or pos >= len(frame):
            raise ValueError("malformed prefix")
        value = frame[pos]
        pos += 1
        if value not in (0,1) or value == previous or reached+length > n:
            raise ValueError("malformed run")
        if local_index < reached+length:
            return value, pos
        reached += length
        previous = value
    raise ValueError("run length mismatch")


def lookup_page_probe(layout, values, pos, group, page_size):
    """Return exact bit and unique physical-page positions visited by parser."""
    values = tuple(values)
    n = len(values)
    check_parameters(n, page_size, group)
    if type(pos) is not int or not 0 <= pos < n:
        raise ValueError("position outside universe")
    if layout == "raw":
        return {"value": values[pos], "page_indices": [pos//page_size],
                "prefix_bytes": 1, "verified_crc": False}
    if layout == "packed":
        encoded = packed_image(values)
        value, consumed = _prefix_lookup(encoded, pos)
        base = 0
    elif layout == "segmented":
        encoded = segmented_image(values, group, page_size)
        capacity = slot_capacity(group, page_size)
        block_id, local = divmod(pos, group)
        base = block_id*capacity
        value, consumed = _prefix_lookup(encoded[base:base+capacity], local)
    else:
        raise ValueError("unknown layout")
    first = base // page_size
    last = (base+consumed-1)//page_size
    return {"value": value, "page_indices": list(range(first,last+1)),
            "prefix_bytes": consumed, "verified_crc": False}


def verified_snapshot_pages(layout, values, group, page_size):
    """Physical pages required by full independent per-frame CRC validation.

    For segmented, full validation of the *queried slot* is possible
    without reading all slots, unlike packed's global snapshot CRC.
    """
    values = tuple(values)
    check_parameters(len(values), page_size, group)
    if layout == "packed":
        frame = packed_image(values)
        if decode_snapshot(frame) != values:
            raise AssertionError("global CRC mismatch")
        return (len(frame)+page_size-1)//page_size
    if layout == "segmented":
        maximum = 0
        cap = slot_capacity(group, page_size)
        encoded = segmented_image(values, group, page_size)
        for block_id, lo in enumerate(range(0,len(values),group)):
            part=values[lo:lo+group]
            data=encoded[block_id*cap:(block_id+1)*cap]
            frame=encode_snapshot(part)
            if decode_snapshot(data[:len(frame)]) != part:
                raise AssertionError("slot CRC mismatch")
            maximum=max(maximum,(len(frame)+page_size-1)//page_size)
        return maximum
    if layout == "raw":
        return 1  # no CRC; a one-page physical point read, NOT integrity proof
    raise ValueError("unknown layout")


def analyze_transition(before, after, page_size=32, group=8):
    before, after = tuple(before), tuple(after)
    if len(before)!=len(after):
        raise ValueError("the universe must stay fixed")
    check_parameters(len(before), page_size, group)
    old_b = runs_and_boundaries(before)
    new_b = runs_and_boundaries(after)
    out = {
        "universe": len(before), "page_size": page_size, "group": group,
        "logical_boundary_edits": len(old_b.symmetric_difference(new_b)),
        "strategies": {},
    }
    for layout in ("packed","segmented","raw"):
        old = image_for(layout,before,group,page_size)
        new = image_for(layout,after,group,page_size)
        diff = page_difference(old,new,page_size)
        out["strategies"][layout] = {
            "disk_bytes_before": len(old), "disk_bytes_after": len(new),
            "global_snapshot_bytes_before": len(packed_image(before)),
            "global_snapshot_bytes_after": len(packed_image(after)),
            **diff,
            "max_point_query_prefix_pages_after": max(
                len(lookup_page_probe(layout,after,p,group,page_size)["page_indices"])
                for p in range(len(after))),
            "max_crc_verified_frame_pages_after": verified_snapshot_pages(
                layout, after,group,page_size) if layout!="raw" else None,
        }
    return out


def alternating_flip_witness(n, page_size=32, group=8):
    if type(n) is not int or n<3 or n%2==0:
        raise ValueError("odd N>=3 required")
    if len(uvarint(n))!=len(uvarint(n-1)):
        raise ValueError("run-count varint width transition excluded")
    before=tuple(i%2 for i in range(n))
    after=(1,)+before[1:]
    row=analyze_transition(before,after,page_size,min(n,group))
    width=len(uvarint(n))
    header=4+2*width
    # Number of FULL pages contained in the suffix of phase-shifted run pairs.
    left=header+2
    right=header+2*n-2
    lower=max(0,right//page_size - (left+page_size-1)//page_size)
    if row["logical_boundary_edits"]!=1:
        raise AssertionError("adversary should delete exactly one boundary")
    if row["strategies"]["packed"]["shared_changed_pages"]<lower:
        raise AssertionError("full-page phase-shift lower bound falsified")
    row["full_suffix_pages_lower_bound"]=lower
    row["pre_run_count"]=n
    row["post_run_count"]=n-1
    return row


def build_report():
    witnesses=[alternating_flip_witness(n,32,8) for n in (3,5,31,129,511)]
    cases={}
    for label,state,update in (
        ("zero_to_one",(0,)*64,(0,1,1)),
        ("nested_overwrite",tuple((i//4)%2 for i in range(64)),(8,56,0)),
        ("hot_singleton",tuple(i%2 for i in range(64)),(3,4,0)),
    ):
        after=list(state)
        lo,hi,v=update
        after[lo:hi]=[v]*(hi-lo)
        cases[label]=analyze_transition(state,tuple(after),32,8)
    return {
        "schema":"mathlab.index001.g2b4b.page-recourse.v1",
        "classification":"CONTIGUOUS_LAYOUT_RESTRICTED_LOWER_BOUND_NOT_UNIVERSAL",
        "physical_nand_bytes":"NOT_MEASURED",
        "actual_syscalls":"NOT_MEASURED",
        "crc_prefix_queries":"NOT_VERIFIED_PER_QUERY",
        "witnesses":witnesses,
        "controls":cases,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    report=build_report()
    if args.json:
        print(json.dumps(report,sort_keys=True,indent=2))
    else:
        for r in report["witnesses"]:
            packed=r["strategies"]["packed"]
            slot=r["strategies"]["segmented"]
            print(f"N={r['universe']} L={r['logical_boundary_edits']} "
                  f"packed_changed={packed['shared_changed_pages']} "
                  f"suffix_lower={r['full_suffix_pages_lower_bound']} "
                  f"slot_changed={slot['changed_page_positions']} "
                  f"packed_bytes={packed['disk_bytes_before']} "
                  f"slots_bytes={slot['disk_bytes_before']}")
        print("INDEX001_G2B4B_PAGE_IMAGE_RECOURSE_PASS")
