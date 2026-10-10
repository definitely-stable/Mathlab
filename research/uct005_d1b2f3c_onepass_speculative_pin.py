#!/usr/bin/env python3
"""UCT-005 D1-B2-F3-C: speculative single-pass staged remote PIN bitmap.

A counterconstruction against claiming two bitmap read passes are logically
necessary for O(P) payload scratch. It assumes the same ideal serialized
trusted digest authority and page-staging interface as D1-B2-F2; untrusted
speculative stage writes are permitted before old-image SHA validation,
but authoritative publication and client PIN changes are NOT.

All staged byte writes (including failed attempts) and their cleanup costs
are charged. No real fsync/barrier/durable-rollback or new UCT lower bound.
"""
from __future__ import annotations

import hashlib
import json
from itertools import product
from math import ceil

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference, validate_contract
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1

CLASSIFICATION = "SPECULATIVE_ONEPASS_STAGING_RESTRICTED_UPPER_AND_TWO_PASS_NECESSITY_FALSIFIER"


class OnePassStagedPinBitmapF1(StreamedPinBitmapF1):
    """Exactly one authenticated bitmap-read pass per PIN/UNPIN.

    Staging is an UNTRUSTED remote side effect, with its own fixed generation
    slot; the atomic trusted authority is changed only after all old pages'
    SHA digest is authenticated. Never claim a constant real Python RSS.
    """

    def _mutate(self, reader: int, epoch: int, value: bool,
                *, must_exist: bool = False) -> bool:
        if self.bitmap_generation >= (1 << 64) - 1:
            raise ValueError("bitmap generation exhausted")
        bit = self._index(reader, epoch)
        if self.bitmap_stage is not None:
            raise Abort("uncommitted bitmap stage already occupied")
        next_generation = self.bitmap_generation + 1
        # Read trusted root/generation ONCE, before speculative staging.
        expected_old_digest = self.trusted_bitmap_digest
        self.ledger["bitmap_stream_trusted_root_reads"] += 1
        self.ledger["bitmap_stream_trusted_root_read_bytes"] += self._TRUSTED_ROOT_BYTES
        old_hash = hashlib.sha256(
            self._DOMAIN + self.bitmap_generation.to_bytes(8, "big"))
        new_hash = hashlib.sha256(
            self._DOMAIN + next_generation.to_bytes(8, "big"))
        current_membership = None
        next_membership = None
        self.bitmap_stage = {}
        try:
            for page in range(self.bitmap_pages):
                # This page has NOT YET been SHA-verified when staged;
                # it cannot be served as authoritative while old root is active.
                old_page, valid = self._page(page, pass_name="speculative_onepass")
                old_hash.update(old_page[:valid])
                if (bit >> 3) // self.page_bytes == page:
                    byte_offset = (bit >> 3) % self.page_bytes
                    byte_mask = 1 << (bit & 7)
                    old_byte = old_page[byte_offset]
                    new_byte = ((old_byte | byte_mask) if value
                                else (old_byte & ~byte_mask))
                    mutated_page = (
                        old_page[:byte_offset] + bytes((new_byte,)) +
                        old_page[byte_offset + 1:])
                    shift = (2 * epoch) & 7
                    current_membership = (
                        bool(old_byte & (1 << shift)),
                        bool(old_byte & (1 << (shift + 1))))
                    next_membership = (
                        bool(new_byte & (1 << shift)),
                        bool(new_byte & (1 << (shift + 1))))
                else:
                    mutated_page = old_page
                self._peak_scratch(valid, two=True)
                new_hash.update(mutated_page[:valid])
                address = self._bitmap_page_address(page, next_generation)
                self.bitmap_stage[page] = mutated_page
                self.ledger["bitmap_stream_last_stage_page_offset"] = address
                self.ledger["bitmap_stream_stage_page_writes"] += 1
                self.ledger["bitmap_remote_page_writes"] += 1
                self.ledger["bitmap_remote_upload_bytes"] += self.page_bytes
                self.ledger["bitmap_stream_stage_address_bytes"] += 8
                self.ledger["bitmap_speculative_page_writes_before_authentication"] += 1
                self.ledger["peak_remote_pages"] = max(
                    self.ledger["peak_remote_pages"], self.remote_pages)
            full_hashed_bytes = (
                len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
            self.ledger["bitmap_stream_speculative_old_hash_input_bytes"] += (
                full_hashed_bytes)
            self.ledger["bitmap_stream_speculative_new_hash_input_bytes"] += (
                full_hashed_bytes)
            self.ledger["bitmap_verifier_hashed_bytes"] += full_hashed_bytes
            self.ledger["bitmap_author_hash_input_bytes"] += full_hashed_bytes
            # Abort *before* trusted publication if any read was malicious,
            # missing, truncated, stale or had noncanonical physical padding.
            if old_hash.digest() != expected_old_digest:
                raise Abort("speculative old bitmap digest did not authenticate")
            if current_membership is None or next_membership is None:
                raise AssertionError("selected epoch's physical page not visited")
            if must_exist and not current_membership[reader]:
                raise Abort("client's PIN token contradicts authenticated bit")
            # In the ideal atomic-root model, this is the ONLY point at which
            # the new remote pages become authoritative. After this point,
            # incomplete old-page retirement may leak pages but cannot replace
            # the independently committed new generation.
            old_slot = self.bitmap_store
            self.bitmap_store = self.bitmap_stage
            self.bitmap_stage = None
            self.bitmap_generation = next_generation
            self.trusted_bitmap_digest = new_hash.digest()
            self.ledger["bitmap_trusted_root_publications"] += 1
            self.ledger["bitmap_trusted_root_publication_bytes"] += (
                self._TRUSTED_ROOT_BYTES)
            for page in old_slot:
                address = self._bitmap_page_address(page, next_generation - 1)
                self.ledger["bitmap_stream_last_retired_page_offset"] = address
                self.ledger["bitmap_stream_retired_bitmap_page_drop_calls"] += 1
                self.ledger["bitmap_stream_retired_bitmap_drop_request_bytes"] += 8
            return any(next_membership)
        except Exception:
            # If trusted root was NOT published, the authoritative old image
            # survives. This drops the speculative, untrusted staging pages.
            self._discard_stage()
            raise


def same_history_onepass(bits: tuple[int,...], P: int, C: int=8) -> dict:
    validate_contract()
    if (not bits or any(type(x) is not int or x not in (0,1) for x in bits)
            or type(P) is not int or P<1
            or type(C) is not int or not 4<=C<=65536):
        raise ValueError("GF2 initial word, positive P, C>=4 required")
    bits=tuple(bits)
    one=OnePassStagedPinBitmapF1(bits,P,C)
    two=StreamedPinBitmapF1(bits,P,C)
    bulk=RemotePinBitmapF1(bits,P,C)
    n=len(bits)
    assert one.pin_current(0)==two.pin_current(0)==bulk.pin_current(0)==0
    trace=[bits]
    for j,position in enumerate((0,min(1,n-1),n-1),1):
        updated=list(trace[-1])
        if j != 2:
            updated[position] ^= 1
        trace.append(tuple(updated))
        if not (one.set(position,updated[position])==
                two.set(position,updated[position])==
                bulk.set(position,updated[position])==j):
            raise AssertionError("epoch semantics differ")
        if j==2:
            if not (one.pin_current(1)==two.pin_current(1)==bulk.pin_current(1)==2):
                raise AssertionError("PIN2 semantics differ")
    intervals=(tuple((a,b) for a in range(n) for b in range(a+1,n+1))
               if n<=6 else ((0,1),(0,n),(n-1,n)))
    for a,b in intervals:
        latest=sum(trace[3][a:b])&1
        old0=sum(trace[0][a:b])&1
        old2=sum(trace[2][a:b])&1
        for m in (one,two,bulk):
            if (any(m.latest(reader,a,b)!=latest for reader in (0,1))
                    or m.as_of(0,0,a,b)!=old0
                    or m.as_of(1,2,a,b)!=old2):
                raise AssertionError("wrong independently checked interval XOR")
    stage=[]
    for release in (None,(0,0),(1,2)):
        if release:
            for m in (one,two,bulk):
                m.unpin(*release)
        records=tuple((m.remote_pages,tuple(sorted(m.remote))) for m in (one,two,bulk))
        if len(set(records))!=1:
            raise AssertionError("one-pass/two-pass/bulk pinned remote pages differ")
        if one.bitmap_stage is not None:
            raise AssertionError("one-pass staging leaked after commit")
        stage.append(records[0][0])
    M=one.bitmap_pages
    S=one._pages_per_snapshot()
    # Four bitmap mutations (2 PIN + 2 UNPIN), three SET scans. This is
    # checked against the actual independent ledgers of all three references.
    if (one.ledger["bitmap_remote_page_read_attempts"] != 7*M
            or two.ledger["bitmap_remote_page_read_attempts"] != 11*M
            or bulk.ledger["bitmap_remote_page_read_attempts"] != 7*M):
        raise AssertionError("7M/11M/7M verified bitmap page read budget")
    for m in (one,two,bulk):
        if (m.ledger["bitmap_remote_page_writes"] != 4*M
                or m.ledger["bitmap_remote_upload_bytes"] != 4*M*P):
            raise AssertionError("four complete bitmap mutation writes")
    if (one.ledger["bitmap_stream_retired_bitmap_page_drop_calls"] != 4*M
            or one.ledger["bitmap_speculative_page_writes_before_authentication"] != 4*M
            or one.ledger["bitmap_stream_stage_abort_drop_calls"]):
        raise AssertionError("accepted staged image writes/retirement not conserved")
    if (one.ledger["peak_remote_pages"] != 3*S+2*M
            or two.ledger["peak_remote_pages"] != 3*S+2*M
            or bulk.ledger["peak_remote_pages"] != 3*S+M):
        raise AssertionError("peak including transient unpublished stage is wrong")
    if not (one.bitmap_peak_trusted_payload_buffers <=
            2*min(one.bitmap_payload_bytes,P)):
        raise AssertionError("one-pass conceptual payload scratch exceeded")
    return {
        "classification": CLASSIFICATION,
        "n":n,"P":P,"C":C,"M":M,"S":S,
        "same_F1_answers_verified":True,
        "remote_page_images_at_each_stage":stage,
        "online_bitmap_page_reads":{
            "bulk":bulk.ledger["bitmap_remote_page_read_attempts"],
            "two_pass_stream":two.ledger["bitmap_remote_page_read_attempts"],
            "speculative_one_pass":one.ledger["bitmap_remote_page_read_attempts"]},
        "onepass_saves_online_pages_vs_twopass":4*M,
        "onepass_speculative_full_page_writes_before_authentication":4*M,
        "onepass_failure_cleanup_is_additional_cost":True,
        "onepass_conceptual_payload_scratch_upper_bytes":
            2*min(one.bitmap_payload_bytes,P),
        "onepass_remote_peak_page_images":3*S+2*M,
        "logical_two_pass_is_NOT_required_under_speculative_untrusted_staging":True,
        "full_crash_or_powerloss_safety":False,
        "novel_joint_lower_bound":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def report()->dict:
    return {"status":CLASSIFICATION,
            "cases":[same_history_onepass((0,1),1),
                     same_history_onepass((0,1,1,0,1),2),
                     same_history_onepass(tuple(i&1 for i in range(33)),64,17)],
            "root_novelty":"OPEN_UNPROVED"}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
