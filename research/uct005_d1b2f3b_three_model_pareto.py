#!/usr/bin/env python3
"""UCT-005 D1-B2-F3-B: three upper constructions, one F1 PIN/GC trace.

Reference-only, fully paid PAGE-IMAGE comparisons. F2 streaming is a pending
research dependency until exact-head CI and accepted merge. Nothing here
establishes a new information lower bound or a complete Pareto frontier.
"""
from __future__ import annotations

from math import ceil
import json

from uct005_d1b0_f1_reference import Abort, validate_contract
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1
from uct005_d1b2f3a_joint_retention import compare_joint_trace

CLASSIFICATION = "THREE_SAME_F1_TRACE_PARTIAL_PARETO_WITH_PAID_OFFLINE_PIN_AUDIT"
UNKNOWN = (
    "end_to_end_trusted_process_peak_RSS",
    "full_client_server_wire_and_retry_traffic",
    "SHA_security_reduction_as_lambda_grows",
    "whole_system_verifier_and_prover_CPU",
    "powerloss_fsync_and_root_authority_recovery",
    "real_SSD_erase_and_compaction_amplification",
)


def authenticated_streamed_PIN_audit(stream: StreamedPinBitmapF1) -> dict:
    """Authenticate every epoch with the accepted F2 SHA page scan.

    O(C*M) *paid* remote page reads. This deliberately does NOT use the
    forbidden bulk bitmap getter, the empty trusted PIN registry, or a free
    untrusted dict of historical membership. Its collection of PIN epochs is
    offline diagnostic RAM, NOT part of the O(P) bitmap-buffer claim.
    """
    if type(stream) is not StreamedPinBitmapF1:
        raise TypeError("only frozen F2 reference")
    C = stream.epoch_capacity
    M = stream.bitmap_pages
    P = stream.page_bytes
    B = stream.bitmap_payload_bytes
    original_reads = stream.ledger["bitmap_remote_page_read_attempts"]
    original_hash = stream.ledger["bitmap_verifier_hashed_bytes"]
    original_authority = stream.ledger["bitmap_stream_trusted_root_reads"]
    per_reader = {0:set(), 1:set()}
    for epoch in range(C):
        bits = stream._scan(pass_name="F3B_offline_audit",
                            inspect_epoch=epoch, audit=True)
        if bits is None:
            raise AssertionError("bounded epoch scan failed to return membership")
        for reader in (0,1):
            if bits[reader]:
                per_reader[reader].add(epoch)
    for reader in (0,1):
        if per_reader[reader] != set(stream.readers[reader]):
            raise Abort("authenticated remote bitmap and independently held PIN disagree")
    all_roots = {stream.epoch} | per_reader[0] | per_reader[1]
    S = stream._pages_per_snapshot()
    page_reads = 0
    snapshot_hash_input = 0
    for epoch in sorted(all_roots):
        page_reads += S
        img = stream.remote.get(epoch)
        manifest = stream.remote_manifests.get(epoch)
        expected = (stream.latest_root if epoch == stream.epoch else
                    next(stream.readers[r][epoch] for r in (0,1)
                         if epoch in stream.readers[r]))
        if (type(img) is not bytes or type(manifest) is not bytes
                or len(img) != ceil(stream.n/8)
                or len(manifest) != stream.MANIFEST_BYTES):
            raise Abort("missing or malformed pinned snapshot image")
        if stream._digest(epoch, img) != expected or stream._manifest(epoch, img) != manifest:
            raise Abort("pinned snapshot/root/manifest authenticity failed")
        snapshot_hash_input += 2*(len(b"mathlab.F1.snapshot.v1\0") + 16 + len(img))
    reads = stream.ledger["bitmap_remote_page_read_attempts"]-original_reads
    hashed = stream.ledger["bitmap_verifier_hashed_bytes"]-original_hash
    trusted = stream.ledger["bitmap_stream_trusted_root_reads"]-original_authority
    H = len(stream._DOMAIN)+8+B
    if reads != C*M or hashed != C*H or trusted != C:
        raise AssertionError("all remote PIN epoch checks must be fully charged")
    kept = len(all_roots)*S+M
    return {
        "PIN_epochs": tuple(sorted(all_roots-{stream.epoch})),
        "PIN_entries": sum(map(len,per_reader.values())),
        "live_authenticated_page_images": kept,
        "extra_PIN_page_images": (len(all_roots)-1)*S,
        "offline_PIN_scan_pages": reads,
        "offline_PIN_scan_full_page_response_bytes": reads*P,
        "offline_PIN_scan_request_address_bytes": reads*8,
        "offline_PIN_SHA_input_bytes": hashed,
        "offline_trusted_root_reads": trusted,
        "offline_snapshot_read_pages": page_reads,
        "offline_snapshot_full_page_response_bytes": page_reads*P,
        "offline_snapshot_request_address_bytes": 8*len(all_roots),
        "offline_snapshot_SHA_input_bytes": snapshot_hash_input,
        "offline_diagnostic_PIN_epoch_list_bytes_at_u64_width":
            8*sum(map(len,per_reader.values())),
        "offline_diagnostic_excluded_from_bitmap_scratch_upper": True,
        "audit_is_free_online_operation": False,
    }


def compare_all_three(bits: tuple[int,...], P: int, C: int=8) -> dict:
    validate_contract()
    if (not bits or any(type(x) is not int or x not in (0,1) for x in bits)
            or type(P) is not int or P < 1
            or type(C) is not int or not 4 <= C <= 65536):
        raise ValueError("nonempty binary word, positive P, C>=4 required")
    frozen = compare_joint_trace(bits,P,C)  # independently verified R + COW
    streamed = StreamedPinBitmapF1(tuple(bits),P,C)
    n = len(bits)
    M = streamed.bitmap_pages
    S = streamed._pages_per_snapshot()
    B = streamed.bitmap_payload_bytes
    words = [tuple(bits)]
    indexes = (0,min(1,n-1),n-1)
    if streamed.pin_current(0) != 0:
        raise AssertionError("stream PIN0 epoch wrong")
    for j,position in enumerate(indexes, start=1):
        successor = list(words[-1])
        if j != 2:  # same deliberate no-op epoch e2 as F3-A
            successor[position] ^= 1
        words.append(tuple(successor))
        if streamed.set(position,successor[position]) != j:
            raise AssertionError("stream SET epoch disagrees")
        if j == 2 and streamed.pin_current(1) != 2:
            raise AssertionError("stream PIN2 epoch wrong")
    intervals = (tuple((i,j) for i in range(n)
                       for j in range(i+1,n+1)) if n<=6
                 else ((0,1),(0,n),(n-1,n)))
    for lo,hi in intervals:
        truth = sum(words[-1][lo:hi]) & 1
        if any(streamed.latest(reader,lo,hi)!=truth for reader in (0,1)):
            raise AssertionError("stream LATEST != independent GF2 truth")
        if (streamed.as_of(0,0,lo,hi)!=(sum(words[0][lo:hi])&1)
                or streamed.as_of(1,2,lo,hi)!=(sum(words[2][lo:hi])&1)):
            raise AssertionError("stream AS_OF != independent GF2 truth")
    # Online bitmap scans: PIN0,PIN2,UNPIN0,UNPIN2 each need two verified
    # full passes. Three SETs need one authenticated pass each, no staging.
    expected_online_bitmap_reads = (4*2+3)*M
    original_bitmap_pages_before_audits = streamed.ledger[
        "bitmap_remote_page_read_attempts"]
    rows=[]
    offline_extra=0
    for stage,release,comparator in zip(
        ("PIN0_PIN2","PIN2_ONLY","LATEST_ONLY"),
        (None,(0,0),(1,2)), frozen["stages"]
    ):
        if release:
            streamed.unpin(*release)
        offline = authenticated_streamed_PIN_audit(streamed)
        offline_extra += offline["offline_PIN_scan_pages"]
        if streamed.gc()!=0:
            raise AssertionError("F2 eager deletion should make explicit GC a no-op")
        if (streamed.remote_pages != offline["live_authenticated_page_images"]
                or streamed.bitmap_stage is not None):
            raise AssertionError("streamed live full pages or unpublished stage mismatch")
        if (comparator["stage"] != stage
                or comparator["PIN_epochs"] != offline["PIN_epochs"]
                or comparator["PIN_entries"] != offline["PIN_entries"]
                or comparator["bulk_live_remote_pages"] != streamed.remote_pages
                or comparator["bulk_PIN_extra_pages"] != offline["extra_PIN_page_images"]):
            raise AssertionError("three upper constructions disagree on exact history")
        if (streamed.trusted_bits != n + 8*80 + 8*40*offline["PIN_entries"]):
            raise AssertionError("trusted writer/anchor/bitmap/client roots not charged")
        rows.append({
            "stage": stage,
            "remote_PIN_epochs": offline["PIN_epochs"],
            "retained_remote_snapshot_pages_bulk_and_stream":
                comparator["bulk_live_remote_pages"],
            "retained_segmented_COW_pages": comparator["cow_live_remote_pages"],
            "stream_PIN_bitmap_extra_page_images":
                offline["extra_PIN_page_images"],
            "COW_PIN_extra_page_images": comparator["cow_PIN_extra_pages"],
            "bulk_offline_PIN_audit": comparator["bulk_offline_audit"],
            "stream_offline_PIN_audit": offline,
            "cow_offline_authenticated_root_audit": comparator["cow_offline_audit"],
            "persistent_trusted_stream_bits": streamed.trusted_bits,
        })
    online_read_attempts = (streamed.ledger["bitmap_remote_page_read_attempts"]
                            - offline_extra)
    if online_read_attempts != expected_online_bitmap_reads:
        raise AssertionError("offline PIN scan must not be mistaken for free online reads")
    if original_bitmap_pages_before_audits != (2*2+3)*M:
        raise AssertionError("three SET and two initial PIN transactions must match")
    if (streamed.ledger["bitmap_stream_stage_page_writes"] != 4*M
            or streamed.ledger["bitmap_stream_retired_bitmap_page_drop_calls"] != 4*M
            or streamed.ledger["bitmap_stream_stage_abort_drop_calls"]):
        raise AssertionError("remote staging and retirement count mismatch")
    bulk_reference_reads = (4+3)*M
    if online_read_attempts-bulk_reference_reads != 4*M:
        raise AssertionError("second validation pass is not paid")
    if streamed.bitmap_peak_trusted_payload_buffers > 2*min(B,P):
        raise AssertionError("F2 bitmap payload buffer upper violated")
    if streamed.ledger["peak_remote_pages"] != 3*S+2*M:
        raise AssertionError("F2 remote staging peak must include old+new bitmap regions")
    if (streamed.ledger["bitmap_remote_upload_bytes"] != 4*M*P
            or streamed.ledger["bitmap_stream_retired_bitmap_drop_request_bytes"]
                != 4*M*8):
        raise AssertionError("full stage upload and address bytes not conserved")
    return {
        "classification": CLASSIFICATION,
        "root_novelty": "OPEN_UNPROVED",
        "n": n, "P": P, "C": C, "B": B, "M": M,
        "three_models_one_frozen_logical_F1_transcript": True,
        "no_op_creates_epoch": True,
        "history_stages": rows,
        "known_F2_additional_online_bitmap_full_page_reads_vs_bulk": 4*M,
        "known_F2_total_online_bitmap_read_pages": online_read_attempts,
        "known_F2_offline_authentication_bitmap_read_pages": offline_extra,
        "known_F2_staged_full_page_writes": 4*M,
        "known_F2_staged_full_page_upload_bytes": 4*M*P,
        "known_F2_retire_address_bytes": 4*M*8,
        "known_F2_remote_peak_pages_with_double_slot": 3*S+2*M,
        "known_bulk_remote_peak_pages_without_double_slot": 3*S+M,
        "known_F2_conceptual_bitmap_payload_scratch_upper_bytes": 2*min(B,P),
        "chosen_bulk_three_image_conceptual_scratch_upper_bytes": 3*B,
        "bulk_three_image_bound_is_NOT_a_universal_lower": True,
        "unknown_resource_axes": {key:None for key in UNKNOWN},
        "all_axis_pareto_order": None,
        "novel_joint_lower_bound": False,
        "real_crash_durability_proof": False,
    }


def report()->dict:
    return {
        "root_novelty":"OPEN_UNPROVED",
        "cases":[
            compare_all_three((0,1,0),1),
            compare_all_three((1,0,1,1,0),2),
            compare_all_three(tuple(i&1 for i in range(33)),64,17),
        ],
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
