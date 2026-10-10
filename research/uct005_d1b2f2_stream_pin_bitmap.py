#!/usr/bin/env python3
"""UCT-005 D1-B2-F2: two-pass streamed authenticated PIN membership updates.

Exact PAGE-001 / D1-B2-D page-image F1 service under the SAME trusted atomic
authority. Streaming SHA256 validation and second-pass authenticated staging
bound the protocol's trusted BITMAP chunk buffers by 2*min(B,P) bytes. This is
NOT measured CPython RSS, all trusted scratch, or a crash-safe transaction.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference, validate_contract
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1

STATUS = "STREAMED_AUTH_BITMAP_CONDITIONAL_REFERENCE_UPPER_ONLY"


class StreamedRemotePinBitmapF1(RemotePinBitmapF1):
    """Bounded chunk buffers, remote staging, second-pass anti-TOCTOU hash."""

    def _buffer_mark(self, number: int) -> None:
        if not isinstance(number, int) or number < 0:
            raise ValueError("invalid trusted bitmap-buffer residency")
        self.ledger["stream_peak_trusted_bitmap_buffer_bytes"] = max(
            self.ledger["stream_peak_trusted_bitmap_buffer_bytes"], number)

    def _stream_verify(self, epoch: int | None = None) -> tuple[bool, bool]:
        """One authenticated full-remote-image pass with <= P chunk residence."""
        self.ledger["bitmap_trusted_root_reads"] += 1
        self.ledger["bitmap_trusted_root_bytes_read"] += self._TRUSTED_ROOT_BYTES
        self.ledger["bitmap_remote_page_read_attempts"] += self.bitmap_pages
        source = self.remote_pin_bitmap
        if not isinstance(source, bytes) or len(source) != self.bitmap_payload_bytes:
            raise Abort("withheld or malformed remote PIN bitmap")
        digest = hashlib.sha256()
        digest.update(self._DOMAIN + self.bitmap_generation.to_bytes(8, "big"))
        flags = [False, False]
        a = 2 * epoch if epoch is not None else -1
        for start in range(0, self.bitmap_payload_bytes, self.page_bytes):
            end = min(start + self.page_bytes, self.bitmap_payload_bytes)
            # This page is materialized into the TRUSTED authority; source
            # remains a separately modeled UNTRUSTED remote object.
            page = bytes(memoryview(source)[start:end])
            self._buffer_mark(len(page))
            digest.update(page)
            if epoch is not None:
                for reader in (0, 1):
                    loc = (a + reader) >> 3
                    if start <= loc < end:
                        flags[reader] = bool(
                            page[loc - start] & (1 << ((a + reader) & 7)))
        self.ledger["bitmap_remote_payload_bytes"] += len(source)
        self.ledger["bitmap_verifier_hashed_bytes"] += (
            len(self._DOMAIN) + 8 + len(source))
        self.ledger["stream_first_pass_page_reads"] += self.bitmap_pages
        if digest.digest() != self.trusted_bitmap_digest:
            raise Abort("untrusted PIN bitmap SHA mismatch or stale replay")
        return flags[0], flags[1]

    def _stream_mutation(self, epoch: int, reader: int,
                         value: bool) -> tuple[bool, bool]:
        """Verify, read again, stage immutable remote image and then publish.

        The second scan hashes the *old* data again before trusting the staged
        mutation; this detects changes between the two read passes before
        publication. Page staging is REMOTE and must pay its allocated pages.
        """
        bit_index = self._index(reader, epoch)
        old_flags = self._stream_verify(epoch)
        if not value and not old_flags[reader]:
            raise Abort("PIN registry contradicts local revoke token")
        generation = self.bitmap_generation
        if generation >= (1 << 64) - 1:
            raise ValueError("PIN bitmap generation exhausted")
        prefix = self._DOMAIN + generation.to_bytes(8, "big")
        next_generation = generation + 1
        old_hash, updated_hash = hashlib.sha256(), hashlib.sha256()
        old_hash.update(prefix)
        updated_hash.update(
            self._DOMAIN + next_generation.to_bytes(8, "big"))
        # Staged bitmap is the UNTRUSTED remote storage object. The trusted
        # authority never constructs a full-size updated bitmap.
        remote_staging = bytearray(self.bitmap_payload_bytes)
        # The old source is NOT cached after pass 1: fetch each page from
        # the live untrusted server in pass 2, so mid-pass substitution is
        # detected by independently recomputing the old-image digest.
        self.ledger["stream_peak_extra_remote_bitmap_pages"] = max(
            self.ledger["stream_peak_extra_remote_bitmap_pages"],
            self.bitmap_pages)
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages + self.bitmap_pages)
        changed_flags = list(old_flags)
        for start in range(0, self.bitmap_payload_bytes, self.page_bytes):
            end = min(start + self.page_bytes, self.bitmap_payload_bytes)
            candidate = self.remote_pin_bitmap
            if not isinstance(candidate, bytes) or len(candidate) != self.bitmap_payload_bytes:
                self.ledger["stream_aborted_unpublished_staging_pages"] += self.bitmap_pages
                raise Abort("remote PIN bitmap withheld/truncated during staging")
            old_page = bytes(memoryview(candidate)[start:end])
            updated_page = bytearray(old_page)
            self._buffer_mark(len(old_page) + len(updated_page))
            if start <= (bit_index >> 3) < end:
                i = (bit_index >> 3) - start
                bit = 1 << (bit_index & 7)
                if value:
                    updated_page[i] |= bit
                else:
                    updated_page[i] &= ~bit
                changed_flags[reader] = value
            old_hash.update(old_page)
            updated_hash.update(updated_page)
            remote_staging[start:end] = updated_page
        self.ledger["stream_second_pass_page_reads"] += self.bitmap_pages
        self.ledger["bitmap_remote_page_read_attempts"] += self.bitmap_pages
        self.ledger["bitmap_remote_payload_bytes"] += len(source)
        self.ledger["stream_second_pass_old_hash_input_bytes"] += (
            len(self._DOMAIN) + 8 + len(source))
        self.ledger["bitmap_author_hash_input_bytes"] += (
            len(self._DOMAIN) + 8 + len(source))
        if old_hash.digest() != self.trusted_bitmap_digest:
            self.ledger["stream_aborted_unpublished_staging_pages"] += self.bitmap_pages
            raise Abort("PIN bitmap changed between authenticated read passes")
        # Atomic trusted publication + installation of the authenticated
        # remote image are ABSTRACT; no disk fsync or distributed transaction.
        self.remote_pin_bitmap = bytes(remote_staging)
        self.bitmap_generation = next_generation
        self.trusted_bitmap_digest = updated_hash.digest()
        self.ledger["bitmap_remote_page_writes"] += self.bitmap_pages
        self.ledger["bitmap_remote_upload_bytes"] += (
            self.bitmap_pages * self.page_bytes)
        self.ledger["stream_staged_remote_bitmap_page_writes"] += self.bitmap_pages
        self.ledger["bitmap_trusted_root_publications"] += 1
        self.ledger["bitmap_trusted_root_publication_bytes"] += (
            self._TRUSTED_ROOT_BYTES)
        return bool(changed_flags[0]), bool(changed_flags[1])

    def _retire_checked(self, epoch: int, pinned: tuple[bool, bool]) -> int:
        self.ledger["bitmap_reclaim_trusted_latest_reads"] += 1
        self.ledger["bitmap_reclaim_trusted_latest_bytes_read"] += self.ROOT_BYTES
        self.ledger["bitmap_reclaim_bit_tests"] += 2
        if epoch == self.epoch or pinned[0] or pinned[1]:
            return 0
        pages = self._pages_per_snapshot()
        start = self._slot_start_page(epoch)
        if start + pages > (1 << 64):
            raise OverflowError("DROP_PAGE remote u64 address overflow")
        # No unpriced remote existence lookup: one addressed delete per page.
        for _ in range(pages):
            self.ledger["bitmap_remote_drop_page_calls"] += 1
            self.ledger["bitmap_remote_drop_request_bytes"] += 8
        self.remote.pop(epoch, None)
        self.remote_manifests.pop(epoch, None)
        self.ledger["bitmap_logical_pages_reclaimed"] += pages
        return pages

    def pin_current(self, reader: int) -> int:
        if reader not in self.readers:
            raise ValueError("unknown reader")
        epoch, root = self._read_anchor()
        self._stream_mutation(epoch, reader, True)
        self.readers[reader][epoch] = root
        self.ledger["bitmap_pin_operations"] += 1
        return epoch

    def unpin(self, reader: int, epoch: int) -> None:
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise ValueError("UNPIN without trusted local token")
        flags = self._stream_mutation(epoch, reader, False)
        del self.readers[reader][epoch]
        self.ledger["bitmap_unpin_operations"] += 1
        self._retire_checked(epoch, flags)

    def set(self, i: int, value: int) -> int:
        if not 0 <= i < self.n or type(value) is not int or value not in (0, 1):
            raise ValueError("invalid SET")
        if self.epoch + 1 >= self.epoch_capacity:
            raise ValueError("public PIN epoch capacity exhausted")
        old = self.epoch
        verified_flags = self._stream_verify(epoch=old)
        # Jump over the bulk-only reference set(), preserving identical data
        # snapshot storage, publication and PAGE-001 accounting.
        newest = SnapshotF1Reference.set(self, i, value)
        self._retire_checked(old, verified_flags)
        return newest

    def assert_streamed_live_set(self) -> None:
        """Test-only audit is separately charged; not an online F1 operation."""
        bitmap = super()._read_verified_bitmap(audit=True)
        self.ledger["stream_diagnostic_audits"] += 1
        # This explicit TEST-ONLY materializing audit uses the parent's
        # bitmap_audit_* ledger instead of online stream_* resource counters.
        active = {e for e in range(self.epoch_capacity)
                  if (bitmap[(2*e)>>3] & (1 << ((2*e)&7))
                      or bitmap[(2*e+1)>>3] & (1 << ((2*e+1)&7)))}
        if set(self.remote) != ({self.epoch} | active):
            raise AssertionError("PIN bitmap live-set invariant failed")


def compare(bits: tuple[int, ...], page_bytes: int, epoch_capacity: int) -> dict:
    validate_contract()
    if not bits or any(type(v) is not int or v not in (0, 1) for v in bits):
        raise ValueError("nonempty binary GF2 input expected")
    if type(page_bytes) is not int or page_bytes <= 0 or epoch_capacity < 4:
        raise ValueError("positive page and capacity>=4 required")
    streamed = StreamedRemotePinBitmapF1(bits, page_bytes, epoch_capacity)
    bulk = RemotePinBitmapF1(bits, page_bytes, epoch_capacity)
    states = [tuple(bits)]
    for m in (streamed, bulk):
        assert m.pin_current(0) == 0
    for k, (pos, typ) in enumerate([(0, "flip"),
                                    (min(1, len(bits)-1), "noop"),
                                    (len(bits)-1, "flip")]):
        next_state = list(states[-1])
        next_state[pos] = (next_state[pos] ^ 1
                           if typ == "flip" else next_state[pos])
        states.append(tuple(next_state))
        for m in (streamed, bulk):
            assert m.set(pos, next_state[pos]) == k+1
        if k == 1:
            for m in (streamed, bulk):
                assert m.pin_current(1) == 2
    for left in range(len(bits)):
        for right in range(left+1, len(bits)+1):
            for model in (streamed, bulk):
                assert model.latest(0,left,right)==(sum(states[3][left:right])&1)
                assert model.latest(1,left,right)==(sum(states[3][left:right])&1)
                assert model.as_of(0,0,left,right)==(sum(states[0][left:right])&1)
                assert model.as_of(1,2,left,right)==(sum(states[2][left:right])&1)
    before={label:m.remote_pages for label,m in (("streamed",streamed),("bulk",bulk))}
    for reader,ep in ((0,0),(1,2)):
        for m in (streamed,bulk):
            m.unpin(reader,ep)
    for m in (streamed,bulk):
        assert m.gc()==0 and set(m.remote)=={3}
    B=streamed.bitmap_payload_bytes
    M=streamed.bitmap_pages
    input_chunk=min(B,page_bytes)
    if streamed.ledger["stream_peak_trusted_bitmap_buffer_bytes"]!=2*input_chunk:
        raise AssertionError("bounded buffered reference memory contract broken")
    if streamed.ledger["bitmap_remote_page_read_attempts"]-bulk.ledger[
            "bitmap_remote_page_read_attempts"] != 4*M:
        raise AssertionError("extra second authenticated pass cost wrong")
    if streamed.ledger["bitmap_remote_page_writes"]!=bulk.ledger[
            "bitmap_remote_page_writes"]:
        raise AssertionError("bitmap versions rewritten differently")
    return {
        "classification":STATUS, "n":len(bits),"P":page_bytes,"epoch_capacity":epoch_capacity,
        "bitmap_bytes":B,"bitmap_pages":M,
        "trusted_persistent_bits_same":streamed.trusted_bits==bulk.trusted_bits,
        "stream_protocol_peak_trusted_bitmap_buffer_bytes":
            streamed.ledger["stream_peak_trusted_bitmap_buffer_bytes"],
        "bulk_abstract_three_resident_bitmap_images_bytes":3*B,
        "stream_second_pass_extra_bitmap_page_reads":4*M,
        "stream_remote_staging_peak_additional_pages":
            streamed.ledger["stream_peak_extra_remote_bitmap_pages"],
        "bulk_bitmap_page_reads":bulk.ledger["bitmap_remote_page_read_attempts"],
        "stream_bitmap_page_reads":streamed.ledger["bitmap_remote_page_read_attempts"],
        "stream_bitmap_page_writes":streamed.ledger["bitmap_remote_page_writes"],
        "bulk_bitmap_page_writes":bulk.ledger["bitmap_remote_page_writes"],
        "stream_remote_page_peak":streamed.ledger["peak_remote_pages"],
        "bulk_remote_page_peak":bulk.ledger["peak_remote_pages"],
        "same_live_pages_with_two_PINS":before["streamed"]==before["bulk"],
        "same_all_honest_answers":True,
        "total_peak_trust_state_bound":"UNKNOWN_CRYPTO_AND_OTHER_TRANSIENT_SCRATCH",
        "crash_consistent_durability":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def report():
    return {"status":STATUS,"cases":[compare(tuple(i&1 for i in range(n)),p,C)
                                     for n,p,C in ((1,1,8),(8,2,64),
                                                   (33,2,4096),(65,64,256))],
            "new_joint_lower_bound":False,"root_novelty":"OPEN_UNPROVED"}


if __name__ == "__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
