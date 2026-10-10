#!/usr/bin/env python3
"""D1-C2 — PIN old-root versus LATEST freshness, F1 page-image witness.

Only a classical, conditional two-world indistinguishability lemma plus
accepted ideal-authority F1 reference. No cryptographic proof, full page
lower bound, Byzantine availability or original nonfactorizing UCT theorem.
"""
from __future__ import annotations

from itertools import product
from math import ceil
import json

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference, validate_contract

CLASSIFICATION = "CLASSICAL_TWO_WORLD_FRESHNESS_SEPARATOR_F1_UPPER_NO_ROOT_NOVELTY"


def parity(word: tuple[int,...], a: int, b: int) -> int:
    if not word or not 0<=a<b<=len(word):
        raise ValueError("invalid half-open interval")
    return sum(word[a:b])&1


def two_world_without_fresh_authority(word: tuple[int,...], i: int,
                                      P: int) -> dict:
    """A replay-capable remote returns the SAME old authenticated snapshot.

    A no-anchor reader accepting the old parity as LATEST is wrong in W1.
    The old tuple is still a sound AS_OF witness in BOTH worlds. The client
    may abort, so no Byzantine liveness or worst-case accepted-error bound.
    """
    if (not word or any(type(bit) is not int or bit not in (0,1)
                         for bit in word)
            or type(i) is not int or not 0<=i<len(word)
            or type(P) is not int or P<1):
        raise ValueError("finite two-world inputs")
    w0=SnapshotF1Reference(word,P)
    w1=SnapshotF1Reference(word,P)
    self0=w0.pin_current(0)
    self1=w1.pin_current(0)
    old_authority=(w0.readers[0][self0],w0.remote[0],w0.remote_manifests[0])
    if self0!=self1 or old_authority!=(
            w1.readers[0][self1],w1.remote[0],w1.remote_manifests[0]):
        raise AssertionError("worlds differ before the trusted anchor update")
    changed=list(word)
    changed[i]^=1
    w1.set(i,changed[i])  # accepted and committed BEFORE the LATEST call
    if w0.latest_root==w1.latest_root or w0.epoch==w1.epoch:
        raise AssertionError("worlds must have different current commitments")
    old_parity=parity(word,i,i+1)
    new_parity=parity(tuple(changed),i,i+1)
    if old_parity==new_parity:
        raise AssertionError("hard query must separate the worlds")
    # Both adversarial remote responses, WITHOUT a trusted anchor query,
    # may be old canonical full images and the SAME already pinned SHA root.
    no_anchor_transcript=(self0,old_authority,
                          old_parity)
    if no_anchor_transcript!=(self1,(
            w1.readers[0][self1],w1.remote[0],w1.remote_manifests[0]),
            w1.as_of(0,self1,i,i+1)):
        raise AssertionError("replayed old proof should still verify AS_OF")
    before=w1.ledger["anchor_read_calls"]
    try:
        w1.latest(0,i,i+1,presented_epoch=0)
    except Abort:
        pass
    else:
        raise AssertionError("LATEST accepted replayed old epoch image")
    if w1.ledger["anchor_read_calls"]!=before+1:
        raise AssertionError("fresh LATEST failed to pay trusted anchor request")
    if w0.as_of(0,self0,i,i+1)!=old_parity:
        raise AssertionError("stale proof incorrectly rejected for AS_OF")
    return {
        "model":"F1_FIXED_ANCHOR_LINEARIZATION_WITH_BYZANTINE_REPLAY",
        "n":len(word),"P":P,"changed_coordinate":i,
        "W0_current_epoch":w0.epoch,"W1_current_epoch":w1.epoch,
        "same_preanchor_reader_state_and_replayed_old_snapshot":True,
        "old_pinned_parity":old_parity,
        "new_latest_parity":new_parity,
        "one_common_accepted_answer_must_be_wrong_in_one_world":True,
        "equal_worlds_any_common_randomized_output_error_at_least_half":True,
        "latest_with_authority_rejects_old_epoch_replay":True,
        "as_of_old_pinned_root_remains_valid":True,
        "Byzantine_availability_proved":False,
        "new_joint_F1_lower_proved":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def two_reader_paid_trace(word: tuple[int,...], i: int, new_bit: int,
                          P: int) -> dict:
    if (not word or any(type(x) is not int or x not in (0,1) for x in word)
            or type(i) is not int or not 0<=i<len(word)
            or type(new_bit) is not int or new_bit not in (0,1)
            or type(P) is not int or P<1):
        raise ValueError("invalid finite F1 transcript")
    validate_contract()
    m=SnapshotF1Reference(word,P)
    n=len(word)
    initial=m.pin_current(0)  # independently trusted reader0 root
    prior_anchor_reads=m.ledger["anchor_read_calls"]
    epoch=m.set(i,new_bit)
    now=list(word)
    now[i]=new_bit
    m.pin_current(1)  # independent reader1 gets latest root after SET
    if (initial,epoch)!=(0,1):
        raise AssertionError("no-op SET still must publish new epoch")
    if m.ledger["anchor_read_calls"]!=prior_anchor_reads+1:
        raise AssertionError("PIN_CURRENT must pay anchor")
    before_gc=m.remote_pages
    freed=m.gc()
    if freed!=0 or m.remote_pages!=before_gc:
        raise AssertionError("old epoch0 protected by registered reader0 PIN")
    S=ceil(ceil(n/8)/P)+ceil(48/P)
    if (m.remote_pages,m.retained_pinned_pages)!=(2*S,S):
        raise AssertionError("snapshot page/manifest capacity not paid")
    check=0
    for a in range(n):
        for b in range(a+1,n+1):
            count_before=m.ledger["anchor_read_calls"]
            v0=m.as_of(0,0,a,b)
            v1=m.as_of(1,1,a,b)
            if v0!=parity(word,a,b) or v1!=parity(tuple(now),a,b):
                raise AssertionError("offline immutable version parity disagrees")
            if m.ledger["anchor_read_calls"]!=count_before:
                raise AssertionError("AS_OF PIN used uncharged latest authority")
            latest=m.latest(0,a,b)
            if latest!=parity(tuple(now),a,b):
                raise AssertionError("LATEST parity disagrees after SET")
            if m.ledger["anchor_read_calls"]!=count_before+1:
                raise AssertionError("LATEST must use current anchor exactly once")
            check+=1
    if m.readers[0][0]==m.readers[1][1]:
        raise AssertionError("even a no-op SET must bind new epoch in SHA")
    if (m.ledger["query_full_page_reads"]!=3*check*S
            or m.ledger["query_remote_payload_bytes"]!=3*check*(48+ceil(n/8))
            or m.ledger["query_remote_request_bytes"]!=3*check*8):
        raise AssertionError("all three SHA-checked page/wire reads must be paid")
    if (m.ledger["pin_registry_bytes"]!=2*41
            or m.ledger["pin_control_full_page_writes"]!=2*ceil(41/P)
            or m.ledger["anchor_read_calls"]!=2+check
            or m.ledger["anchor_read_response_bytes"]!=40*(2+check)):
        raise AssertionError("PIN authority and freshness control plane not paid")
    return {
        "model":"F1_IDEAL_SERIALIZED_AUTHORITY_PAGE_IMAGE",
        "n":n,"P":P,"epoch_after_SET":epoch,
        "set_was_noop":word[i]==new_bit,
        "query_ranges":check,
        "old_PIN_anchor_reads_per_AS_OF":0,
        "LATEST_anchor_reads_per_query":1,
        "latest_anchor_reads_total_including_two_PIN":m.ledger["anchor_read_calls"],
        "remote_pages_per_snapshot":S,
        "retained_remote_history_pages":S,
        "live_remote_pages":m.remote_pages,
        "query_full_page_reads":m.ledger["query_full_page_reads"],
        "query_remote_payload_bytes":m.ledger["query_remote_payload_bytes"],
        "reader_and_authoritative_PIN_record_bytes":m.ledger["pin_registry_bytes"],
        "trusted_bits_including_writer_and_reader_roots":m.trusted_bits,
        "manifest_bytes_each_version":48,
        "complete_cryptographic_SUNDR_or_VC_theorem_transfer":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def duplicate_PIN_authority_GC(P: int) -> dict:
    if type(P) is not int or P<1:
        raise ValueError("positive physical P")
    m=SnapshotF1Reference((0,1,1),P)
    e0=m.pin_current(0)
    m.pin_current(1)  # both independent reader tokens same epoch
    m.set(0,1)
    S=ceil(ceil(3/8)/P)+ceil(48/P)
    first=m.gc()
    if first!=0 or m.retained_pinned_pages!=S:
        raise AssertionError("two readers should retain a single old snapshot")
    m.unpin(0,e0)
    middle=m.gc()
    if middle!=0 or m.retained_pinned_pages!=S:
        raise AssertionError("reader1 still retains same historic snapshot")
    if m.as_of(1,e0,0,3)!=0:
        raise AssertionError("old pinned reader1 parity incorrect")
    m.unpin(1,e0)
    last=m.gc()
    if last!=S or m.retained_pinned_pages!=0:
        raise AssertionError("revoking both PIN tokens must permit one GC image")
    try:
        m.as_of(1,e0,0,3)
    except Abort:
        pass
    else:
        raise AssertionError("AS_OF without PIN after GC succeeded")
    if (m.ledger["pin_registry_revocations"]!=2
            or m.ledger["pin_control_full_page_writes"]!=4*ceil(41/P)):
        raise AssertionError("trusted PIN revocation pages were free")
    return {
        "P":P,
        "PIN_entries_at_old_epoch":2,
        "distinct_old_epoch_pages_retained":S,
        "freed_after_first_UNPIN":0,
        "freed_after_second_UNPIN":last,
        "trusted_PIN_control_full_page_writes":m.ledger["pin_control_full_page_writes"],
        "GC_directory_full_page_reads":m.ledger["gc_directory_page_reads"],
        "historic_as_of_after_last_UNPIN_aborts":True,
        "root_implies_availability":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def report() -> dict:
    return {
        "classification":CLASSIFICATION,
        "root_novelty":"OPEN_UNPROVED",
        "two_world_replay":two_world_without_fresh_authority((0,1,0),0,2),
        "F1_page_image_two_reader":two_reader_paid_trace((0,1,0),0,1,2),
        "GC_two_reader":duplicate_PIN_authority_GC(2),
        "root_nonfactorizing_theorem_proved":False,
        "FULL_VC_2026_REDUCTION":None,
        "full_crypto_binding_reduction":None,
        "real_fsync_powerloss":None,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
