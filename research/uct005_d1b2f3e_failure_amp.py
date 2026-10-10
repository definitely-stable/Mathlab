#!/usr/bin/env python3
"""UCT-005 F3-E: adversarial bitmap failure costs on two accepted uppers.

No new root lower bound, no real fsync or Byzantine availability guarantee.
Every result comes from independent F2 and F3-C page-ledger executions.
"""
from __future__ import annotations

import json
from math import ceil

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1
from uct005_d1b2f3c_onepass_speculative_pin import OnePassStagedPinBitmapF1

CLASSIFICATION = "PREAUTH_FAILURE_STAGE_AMPLIFICATION_AND_NO_ALL_AXIS_PARETO"


def _state(model) -> dict:
    return {
        "online_bitmap_read_attempts":
            model.ledger["bitmap_remote_page_read_attempts"],
        "stage_page_writes":
            model.ledger["bitmap_stream_stage_page_writes"],
        "stage_upload_bytes": model.ledger["bitmap_remote_upload_bytes"],
        "abort_stage_drop_calls":
            model.ledger["bitmap_stream_stage_abort_drop_calls"],
        "abort_stage_drop_address_bytes":
            model.ledger["bitmap_stream_stage_abort_drop_request_bytes"],
        "trusted_root_publications":
            model.ledger["bitmap_trusted_root_publications"],
        "old_slot_retirement_calls":
            model.ledger["bitmap_stream_retired_bitmap_page_drop_calls"],
        "peak_remote_pages": model.ledger["peak_remote_pages"],
        "trusted_generation": model.bitmap_generation,
        "unpublished_stage_after_abort": model.bitmap_stage is not None,
        "trusted_local_reader_PIN_entries": sum(
            len(x) for x in model.readers.values()),
        "pin_epoch_after_abort": model.epoch,
    }


def _fault(model, kind: str, j: int | None):
    M = model.bitmap_pages
    if kind == "preexisting_wrong_SHA":
        img = bytearray(model.bitmap_store[0])
        img[0] ^= 1
        model.bitmap_store[0] = bytes(img)
    elif kind == "withheld_complete_page":
        if type(j) is not int or not 0 <= j < M:
            raise ValueError("withheld page must be within physical bitmap")
        del model.bitmap_store[j]
    elif kind == "noncanonical_last_page_padding":
        B,P = model.bitmap_payload_bytes, model.page_bytes
        if B == M*P:
            raise ValueError("bitmap has no padding to corrupt")
        img = bytearray(model.bitmap_store[M-1])
        img[-1] = 1
        model.bitmap_store[M-1] = bytes(img)
    else:
        raise ValueError("unrecognized failure class")


def compare_preverification_fault(*, C: int, P: int, kind: str,
                                   j: int | None = None) -> dict:
    if (type(C) is not int or not 4 <= C <= 65536
            or type(P) is not int or P < 1):
        raise ValueError("public PIN epoch capacity and page dimensions required")
    models = (
        ("two_pass", StreamedPinBitmapF1((0,1,0),P,C)),
        ("speculative_one_pass", OnePassStagedPinBitmapF1((0,1,0),P,C)),
    )
    M = ceil(ceil(2*C/8)/P)
    expected_stage = (M if kind == "preexisting_wrong_SHA" else
                      j if kind == "withheld_complete_page" else M-1)
    expected_reads = (j+1 if kind == "withheld_complete_page" else M)
    report = {}
    for name,model in models:
        trusted = (model.bitmap_generation, model.trusted_bitmap_digest,
                   model.epoch, tuple(sorted(model.readers[0].items())))
        baseline = model.remote_pages
        _fault(model,kind,j)
        try:
            model.pin_current(0)
        except Abort:
            pass
        else:
            raise AssertionError("untrusted invalid old page was accepted")
        observed = _state(model)
        if (model.bitmap_generation, model.trusted_bitmap_digest,
                model.epoch, tuple(sorted(model.readers[0].items()))) != trusted:
            raise AssertionError("unverified data changed trusted publication")
        if (observed["online_bitmap_read_attempts"] != expected_reads
                or observed["trusted_root_publications"] != 0
                or observed["unpublished_stage_after_abort"]
                or model.remote_pages != baseline):
            raise AssertionError("preverified bad source left trusted/remote effects")
        target = 0 if name == "two_pass" else expected_stage
        if (observed["stage_page_writes"] != target
                or observed["abort_stage_drop_calls"] != target
                or observed["stage_upload_bytes"] != target*P
                or observed["abort_stage_drop_address_bytes"] != target*8
                or observed["old_slot_retirement_calls"] != 0):
            raise AssertionError("failure-stage P-byte writes and 8-byte drops mispriced")
        report[name] = observed
    return {
        "classification":CLASSIFICATION,
        "root_novelty":"OPEN_UNPROVED",
        "C":C,"P":P,"M":M,"kind":kind,"fault_position":j,
        "two_pass":report["two_pass"],
        "one_pass":report["speculative_one_pass"],
        "additional_failure_side_stage_page_writes_due_to_speculation":
            expected_stage,
        "additional_failure_side_full_page_upload_bytes": expected_stage*P,
        "additional_failure_side_drop_address_bytes": expected_stage*8,
        "F2_has_zero_stage_writes_for_PREEXISTING_corruption_only": True,
        "F2_has_zero_stage_writes_for_ALL_possible_failures": False,
        "real_durable_cleanup_guarantee":False,
        "new_information_lower_bound":False,
    }


def between_pass_F2_mutation(C: int, P: int, page: int | None = None) -> dict:
    if (type(C) is not int or C < 4 or C > 65536
            or type(P) is not int or P < 1):
        raise ValueError("invalid C or P")
    M=ceil(ceil(2*C/8)/P)
    target=M-1 if page is None else page
    if type(target) is not int or not 0<=target<M:
        raise ValueError("second-pass switch page outside bitmap")
    class SwitchedSecondPage(StreamedPinBitmapF1):
        def _page(self, current, *, pass_name):
            if pass_name=="pass2" and current==target:
                # A syntactically valid full P-byte old page changes between
                # SHA scans, so the SECOND old digest fails at the end.
                img=bytearray(self.bitmap_store[current])
                img[0]^=1
                self.bitmap_store[current]=bytes(img)
            return super()._page(current,pass_name=pass_name)
    m=SwitchedSecondPage((1,0,0),P,C)
    trusted=(m.bitmap_generation,m.trusted_bitmap_digest,m.epoch)
    try:
        m.pin_current(0)
    except Abort:
        pass
    else:
        raise AssertionError("second-pass changed page cannot be trusted")
    z=_state(m)
    if (z["online_bitmap_read_attempts"]!=2*M
            or z["stage_page_writes"]!=M
            or z["abort_stage_drop_calls"]!=M
            or z["stage_upload_bytes"]!=M*P
            or z["trusted_root_publications"]!=0
            or z["unpublished_stage_after_abort"]
            or (m.bitmap_generation,m.trusted_bitmap_digest,m.epoch)!=trusted):
        raise AssertionError("F2 second-pass changed-page abort cost not conserved")
    return {
        "classification":"F2_CAN_ALSO_WRITE_FAILED_SPECULATIVE_STAGE_AFTER_PASS1",
        "C":C,"P":P,"M":M,"changed_second_pass_page":target,
        "F2_after_pass1_failure_cost":z,
        "new_information_lower_bound":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def post_publication_availability_attack(C: int, P: int) -> dict:
    """Tamper active remote PIN page AFTER ideal trusted root publishes."""
    if (type(C) is not int or not 4<=C<=65536
            or type(P) is not int or P<1):
        raise ValueError("invalid C or P")
    states={}
    for name,typ in (
        ("two_pass", StreamedPinBitmapF1),
        ("speculative_one_pass", OnePassStagedPinBitmapF1),
    ):
        m=typ((0,1,0),P,C)
        if m.pin_current(0)!=0:
            raise AssertionError("honest first PIN did not publish")
        before=(m.epoch,m.bitmap_generation,m.trusted_bitmap_digest,
                tuple(sorted(m.readers[0].items())))
        img=bytearray(m.bitmap_store[0])
        img[0]^=1
        m.bitmap_store[0]=bytes(img)
        try:
            m.set(0,1)
        except Abort:
            pass
        else:
            raise AssertionError("malicious remote bitmap accepted after publication")
        after=(m.epoch,m.bitmap_generation,m.trusted_bitmap_digest,
               tuple(sorted(m.readers[0].items())))
        if before!=after or m.ledger["bitmap_trusted_root_publications"]!=1:
            raise AssertionError("remote tamper may never force new trust publication")
        states[name]={
            "old_trusted_root_unchanged":before==after,
            "pin_epoch_0_remains_trusted_to_reader":0 in m.readers[0],
            "tampered_remote_page_caused_fail_closed_next_SET":True,
            "trusted_root_publication_count":1,
            "availability_guarantee":False,
        }
    return {
        "classification":"REMOTE_SERVER_LIVENESS_DOES_NOT_FOLLOW_FROM_SHA",
        "C":C,"P":P,"models":states,
        "real_fsync_or_powerloss_proof":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def repeated_failed_attempts(C: int, P: int, attempts: int) -> dict:
    if type(attempts) is not int or not 1<=attempts<=20:
        raise ValueError("bounded intentional retry census 1..20 only")
    m=OnePassStagedPinBitmapF1((0,1,0),P,C)
    first=bytearray(m.bitmap_store[0])
    first[0]^=1
    m.bitmap_store[0]=bytes(first)
    old_digest=m.trusted_bitmap_digest
    for _ in range(attempts):
        try:
            m.pin_current(0)
        except Abort:
            pass
        else:
            raise AssertionError("SHA invalid old page accepted on retry")
    M=m.bitmap_pages
    if (m.ledger["bitmap_remote_page_read_attempts"] != attempts*M
            or m.ledger["bitmap_stream_stage_page_writes"] != attempts*M
            or m.ledger["bitmap_stream_stage_abort_drop_calls"]!=attempts*M
            or m.ledger["bitmap_trusted_root_publications"]!=0
            or m.trusted_bitmap_digest!=old_digest
            or m.bitmap_generation!=0 or m.bitmap_stage is not None):
        raise AssertionError("adversarial retry amplification not fully charged")
    return {
        "attempts":attempts,"C":C,"P":P,"M":M,
        "full_page_speculative_uploads":attempts*M,
        "full_page_speculative_upload_bytes":attempts*M*P,
        "charged_cleanup_drop_request_bytes":attempts*M*8,
        "no_trusted_publication":True,
        "unbounded_failure_side_cost_if_attempts_are_unbounded":True,
        "root_novelty":"OPEN_UNPROVED",
    }


def report():
    return {
        "classification":CLASSIFICATION,"root_novelty":"OPEN_UNPROVED",
        "cases":[
            compare_preverification_fault(C=17,P=1,kind="preexisting_wrong_SHA"),
            compare_preverification_fault(C=17,P=2,kind="withheld_complete_page",j=1),
            compare_preverification_fault(C=17,P=64,kind="noncanonical_last_page_padding"),
        ],
        "f2_second_pass_fault":between_pass_F2_mutation(17,2),
        "remote_liveness":post_publication_availability_attack(8,1),
        "repeat_attack":repeated_failed_attempts(17,1,3),
        "full_pareto":None,
        "new_joint_lower_bound":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
