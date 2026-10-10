#!/usr/bin/env python3
"""UCT-005 D1-B2-F3-A: identical-transcript PIN retention resource comparator.

Compare accepted D1-B2-D authenticated-remote-bitmap immutable snapshots
against accepted D1-B2-B1 segmented authenticated COW, including the merged
F1 independently CHARGED offline retained-page audit.

No transfers from the pending F2 streaming code, no claimed full Pareto
vector, new joint lower bound, adversarial crash safety or measured SSD I/O.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
from math import ceil
import json

from uct005_d1b0_f1_reference import Abort, validate_contract
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1
from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree
from uct005_d1b2f1_pin_retention import (
    retention_audit, exact_retained_node_excess,
)

CLASSIFICATION = "SAME_TRANSCRIPT_TWO_AUTHENTICATED_UPPERS_PARTIAL_VECTOR"
UNKNOWN_AXES = (
    "complete_peak_trusted_RSS_bytes",
    "writer_network_framing_and_retries",
    "full_prover_CPU",
    "uniform_asymptotic_SHA_security",
    "durable_rollback_and_crash_recovery",
    "physical_SSD_erase_write_amplification",
)


def _original_words(bits: tuple[int, ...]):
    n = len(bits)
    indexes = (0, min(1, n - 1), n - 1)
    words = [bits]
    for i, position in enumerate(indexes):
        next_word = list(words[-1])
        if i != 1:  # no-op middle SET still emits a new authenticated epoch
            next_word[position] ^= 1
        words.append(tuple(next_word))
    return indexes, tuple(words)


def bulk_authenticated_retention_audit(m: RemotePinBitmapF1) -> dict:
    """Reconstruct live epochs from SHA-verified remote bitset, NOT PIN registry.

    D1-B2-F1's SnapshotF1Reference PIN registry deliberately remains EMPTY
    in this model. Applying its snapshot audit directly would silently miss
    ALL historically pinned epochs, so the remote PIN bitmap is authenticated
    and queried explicitly. Auditor's costs are separated and nonzero.
    """
    if type(m) is not RemotePinBitmapF1:
        raise TypeError("only the accepted bulk remote PIN reference")
    before = Counter({k:v for k,v in m.ledger.items()
                      if k.startswith("bitmap_audit_")})
    bitmap = m._read_verified_bitmap(audit=True)
    p = m.page_bytes
    B = m.bitmap_payload_bytes
    if len(bitmap) != B:
        raise Abort("bad authenticated PIN bitmap byte count")
    remote_pins = {reader: set() for reader in (0, 1)}
    for epoch in range(m.epoch_capacity):
        for reader in (0, 1):
            bit = m._index(reader, epoch)
            if bitmap[bit >> 3] & (1 << (bit & 7)):
                remote_pins[reader].add(epoch)
    for reader in (0, 1):
        if remote_pins[reader] != set(m.readers[reader]):
            raise Abort("remote bitset contradicts independently trusted reader PIN")
    retained = {m.epoch} | remote_pins[0] | remote_pins[1]
    snapshot_pages = m._pages_per_snapshot()
    snapshot_reads = 0
    hash_bytes = 0
    for epoch in sorted(retained):
        snapshot_reads += snapshot_pages
        image = m.remote.get(epoch)
        manifest = m.remote_manifests.get(epoch)
        expected = (m.latest_root if epoch == m.epoch else
                    next(m.readers[r][epoch] for r in (0, 1)
                         if epoch in m.readers[r]))
        if (type(image) is not bytes or type(manifest) is not bytes
                or len(image) != ceil(m.n / 8)
                or len(manifest) != m.MANIFEST_BYTES):
            raise Abort("withheld or malformed authenticated pinned snapshot")
        if (m._digest(epoch, image) != expected
                or m._manifest(epoch, image) != manifest):
            raise Abort("retained epoch failed independent SHA/root check")
        hash_bytes += 2*(len(b"mathlab.F1.snapshot.v1\0") + 16 + len(image))
    after = Counter({k:v for k,v in m.ledger.items()
                     if k.startswith("bitmap_audit_")})
    bitmap_delta = after - before
    if bitmap_delta["bitmap_audit_remote_page_read_attempts"] != m.bitmap_pages:
        raise AssertionError("remote bitmap audit must read all pages")
    if bitmap_delta["bitmap_audit_verifier_hashed_bytes"] != (
            len(m._DOMAIN)+8+B):
        raise AssertionError("remote bitmap digest input accounting mismatch")
    paid = {
        "bitmap_verified_page_reads": m.bitmap_pages,
        "bitmap_verified_full_response_bytes": m.bitmap_pages * p,
        "bitmap_verified_request_address_bytes": 8 * m.bitmap_pages,
        "bitmap_verified_hash_input_bytes":
            bitmap_delta["bitmap_audit_verifier_hashed_bytes"],
        "bitmap_trusted_root_reads":
            bitmap_delta["bitmap_audit_trusted_root_reads"],
        "snapshot_verified_page_reads": snapshot_reads,
        "snapshot_verified_full_response_bytes": snapshot_reads * p,
        "snapshot_verified_request_address_bytes": 8 * len(retained),
        "snapshot_verified_hash_input_bytes": hash_bytes,
    }
    remote_pages = len(retained) * snapshot_pages + m.bitmap_pages
    return {
        "root_novelty": "OPEN_UNPROVED",
        "source": "D1-B2-D authenticated bulk remote PIN bitmap",
        "distinct_PIN_epochs": tuple(sorted(retained - {m.epoch})),
        "PIN_entries": sum(len(a) for a in remote_pins.values()),
        "latest_only_pages": snapshot_pages + m.bitmap_pages,
        "authenticated_kept_pages": remote_pages,
        "PIN_incremental_pages": (len(retained)-1) * snapshot_pages,
        "PIN_remote_bitmap_pages": m.bitmap_pages,
        "paid_OFFLINE_audit": paid,
        "offline_audit_not_online_cost": True,
        "full_Pareto": False,
    }


def compare_joint_trace(bits: tuple[int, ...], page_bytes: int,
                        capacity: int = 8) -> dict:
    validate_contract()
    if (not bits or any(type(x) is not int or x not in (0, 1) for x in bits)
            or type(page_bytes) is not int or page_bytes < 1
            or type(capacity) is not int or capacity < 4
            or capacity > 65536):
        raise ValueError("invalid frozen F1 word/page/capacity")
    bitword = tuple(bits)
    n = len(bits)
    indexes, words = _original_words(bitword)
    bulk = RemotePinBitmapF1(bitword, page_bytes, capacity)
    cow = SegmentedPageCowTree(bitword, page_bytes)
    assert bulk.pin_current(0) == cow.pin_current(0) == 0
    for j, position in enumerate(indexes, start=1):
        bit = words[j][position]
        assert bulk.set(position, bit) == cow.set(position, bit) == j
        if j == 2:
            assert bulk.pin_current(1) == cow.pin_current(1) == 2
    intervals = (tuple((i, j) for i in range(n)
                       for j in range(i+1, n+1)) if n <= 6
                 else ((0, 1), (0, n), (n-1, n)))
    for lo, hi in intervals:
        current = sum(words[-1][lo:hi]) & 1
        old0 = sum(words[0][lo:hi]) & 1
        old2 = sum(words[2][lo:hi]) & 1
        for r in (0, 1):
            if (bulk.latest(r,lo,hi) != current or
                    cow.query(r,lo,hi) != current):
                raise AssertionError("LATEST mismatch on common transcript")
        if (bulk.as_of(0,0,lo,hi) != old0 or
                cow.query(0,lo,hi,as_of=0) != old0 or
                bulk.as_of(1,2,lo,hi) != old2 or
                cow.query(1,lo,hi,as_of=2) != old2):
            raise AssertionError("AS_OF mismatch on common transcript")

    records = []
    for tag, release, selected in (
        ("PIN0_PIN2", None, (0, 2, 3)),
        ("PIN2_ONLY", (0, 0), (2, 3)),
        ("LATEST_ONLY", (1, 2), (3,)),
    ):
        if release:
            bulk.unpin(*release)
            cow.unpin(*release)
        # Both audits happen before their explicitly charged GC step.
        a = bulk_authenticated_retention_audit(bulk)
        b = retention_audit(cow)
        before_cow = cow.remote_pages
        before_bulk = bulk.remote_pages
        cow_freed = cow.gc()
        bulk_freed = bulk.gc()
        if (cow_freed != before_cow-cow.remote_pages
                or bulk_freed != before_bulk-bulk.remote_pages):
            raise AssertionError("collector logical freed pages mismatch")
        if (a["authenticated_kept_pages"] != bulk.remote_pages
                or b["authenticated_kept_remote_pages_including_metadata"] !=
                cow.remote_pages):
            raise AssertionError("actual post-GC physical kept pages mismatch")
        expected_extra = exact_retained_node_excess(n,indexes,selected)
        measured_extra = (b["union_reachable_COW_nodes"] -
                          b["latest_reachable_COW_nodes"])
        if measured_extra != expected_extra:
            raise AssertionError("independent COW retained node identity failure")
        expected_cow_PIN = (expected_extra*cow.node_pages +
                            (len(selected)-1)*cow.root_pages)
        if b["incremental_PIN_remote_pages_over_latest"] != expected_cow_PIN:
            raise AssertionError("COW exact PIN page image decomposition failure")
        if set(a["distinct_PIN_epochs"]) != set(b["distinct_pinned_epochs"]):
            raise AssertionError("distinct historical PIN roots mismatch")
        records.append({
            "stage": tag,
            "PIN_epochs": a["distinct_PIN_epochs"],
            "PIN_entries": a["PIN_entries"],
            "bulk_live_remote_pages": bulk.remote_pages,
            "cow_live_remote_pages": cow.remote_pages,
            "bulk_PIN_extra_pages": a["PIN_incremental_pages"],
            "cow_PIN_extra_pages": expected_cow_PIN,
            "cow_extra_historical_node_IDs": expected_extra,
            "cow_bitmap_pages": b["bitmap_remote_pages_charged"],
            "bulk_bitmap_pages": a["PIN_remote_bitmap_pages"],
            "bulk_offline_audit": a["paid_OFFLINE_audit"],
            "cow_offline_audit": b["offline_audit_charged"],
            "distinct_models_no_unpriced_transfer": True,
        })
    if any(r["bulk_PIN_extra_pages"] < 0 or
           r["cow_PIN_extra_pages"] < 0 for r in records):
        raise AssertionError("negative PIN storage impossible")
    if records[-1]["bulk_PIN_extra_pages"] or records[-1]["cow_PIN_extra_pages"]:
        raise AssertionError("no historical PIN remains after final UNPIN")
    return {
        "classification": CLASSIFICATION,
        "n": n, "P": page_bytes, "capacity": capacity,
        "common_original_update_indices": indexes,
        "same_three_SET_noop_PIN_and_all_applicable_range_answers": True,
        "query_profile": "all_intervals" if n <= 6 else "representative",
        "stages": tuple(records),
        "resource_vector": {axis: None for axis in UNKNOWN_AXES},
        "strict_Pareto_dominance": None,
        "new_joint_lower_bound": False,
        "root_novelty": "OPEN_UNPROVED",
    }


def report() -> dict:
    return {
        "root_novelty": "OPEN_UNPROVED",
        "cases": [
            compare_joint_trace((0,1),1),
            compare_joint_trace((0,1,0,1,0),2),
            compare_joint_trace(tuple(i & 1 for i in range(33)),64,17),
        ],
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
