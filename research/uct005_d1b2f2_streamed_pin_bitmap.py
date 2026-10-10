#!/usr/bin/env python3
"""D1-B2-F2: streamed authenticated remote PIN bitmap with paid staging.

Conditional byte/page-image reference. Ideal serialized trusted authority,
honest remotely addressed page storage, and SHA-256 collision resistance are
assumptions. This is NOT real crash safety or a cryptographic security proof.
"""
from __future__ import annotations

import hashlib
import json

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference, validate_contract
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1


class StreamedPinBitmapF1(RemotePinBitmapF1):
    """Peak algorithmic bitmap payload buffers <= 2*min(B,P) bytes.

    self.bitmap_store and self.bitmap_stage are explicitly UNTRUSTED REMOTE
    page-image dictionaries. No runtime/RSS bound is asserted for Python's
    emulation or SHA/network/stack/control buffers; the bound is the
    algorithm's conceptual retained bitmap payload buffers only.

    Two reserved fixed bitmap slots, alternating by trusted generation parity,
    precede immutable snapshot epoch slots. Free slots have no live page
    allocation. All bitmap page read/write/drop requests are charged.
    """

    def __init__(self, bits: tuple[int, ...], page_bytes: int,
                 epoch_capacity: int):
        if type(epoch_capacity) is not int or not 2 <= epoch_capacity <= 65536:
            raise ValueError("bounded capacity must be 2..65536")
        self.epoch_capacity = epoch_capacity
        # Avoid RemotePinBitmapF1.__init__: it constructs a full B-byte
        # trusted mutation buffer, violating the streamed setup gate.
        SnapshotF1Reference.__init__(self, bits, page_bytes)
        self.bitmap_generation = 0
        self.remote_pin_bitmap = None  # deliberately NOT a cached bitmap
        self.bitmap_store: dict[int, bytes] = {}
        self.bitmap_stage: dict[int, bytes] | None = None
        self.bitmap_peak_trusted_payload_buffers = 0
        digest = hashlib.sha256(self._DOMAIN + bytes(8))
        remaining = self.bitmap_payload_bytes
        for page in range(self.bitmap_pages):
            valid = min(remaining, self.page_bytes)
            payload = bytes(self.page_bytes)  # remote fixed complete page
            self.bitmap_store[page] = payload
            digest.update(payload[:valid])
            remaining -= valid
            self._peak_scratch(valid)
        assert remaining == 0
        self.trusted_bitmap_digest = digest.digest()
        self.ledger["bitmap_setup_page_writes"] += self.bitmap_pages
        self.ledger["bitmap_setup_upload_bytes"] += self.bitmap_pages * self.page_bytes
        self.ledger["bitmap_setup_hashed_bytes"] += len(self._DOMAIN) + 8 + self.bitmap_payload_bytes
        self.ledger["bitmap_stream_setup_page_writes"] += self.bitmap_pages
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages)

    def _slot_start_page(self, epoch: int) -> int:
        # Two physical (active + staging) bitmap slots; snapshot address
        # cannot overlap either, even when the second slot is logically free.
        return 2 * self.bitmap_pages + epoch * self._pages_per_snapshot()

    @property
    def remote_pages(self) -> int:
        baseline = super().remote_pages
        return baseline + (len(self.bitmap_stage)
                           if getattr(self, "bitmap_stage", None) is not None else 0)

    def _peak_scratch(self, count: int, two: bool = False):
        self.bitmap_peak_trusted_payload_buffers = max(
            self.bitmap_peak_trusted_payload_buffers, count * (2 if two else 1))
        self.ledger["bitmap_stream_peak_payload_buffer_bytes"] = (
            self.bitmap_peak_trusted_payload_buffers)

    def _page(self, page: int, *, pass_name: str) -> tuple[bytes, int]:
        if not 0 <= page < self.bitmap_pages:
            raise Abort("bitmap address outside issued physical slot")
        self.ledger["bitmap_stream_" + pass_name + "_page_read_attempts"] += 1
        self.ledger["bitmap_remote_page_read_attempts"] += 1
        self.ledger["bitmap_remote_page_request_bytes"] += 8
        self.ledger["bitmap_remote_page_read_transfer_bytes"] += self.page_bytes
        image = self.bitmap_store.get(page)
        if type(image) is not bytes or len(image) != self.page_bytes:
            raise Abort("withheld/truncated remote complete bitmap page")
        valid = min(self.page_bytes, self.bitmap_payload_bytes - page * self.page_bytes)
        if image[valid:] != bytes(self.page_bytes - valid):
            raise Abort("noncanonical nonzero bitmap padding")
        self._peak_scratch(valid)
        return image, valid

    def _scan(self, *, pass_name: str, inspect_epoch: int | None = None,
              audit: bool = False) -> tuple[bool, bool] | None:
        self.ledger["bitmap_stream_trusted_root_reads"] += 1
        self.ledger["bitmap_stream_trusted_root_read_bytes"] += self._TRUSTED_ROOT_BYTES
        root = self.trusted_bitmap_digest
        digest = hashlib.sha256(
            self._DOMAIN + self.bitmap_generation.to_bytes(8, "big"))
        found = None
        if inspect_epoch is not None and not 0 <= inspect_epoch < self.epoch_capacity:
            raise ValueError("epoch outside PIN bitmap")
        for page in range(self.bitmap_pages):
            image, valid = self._page(page, pass_name=pass_name)
            digest.update(image[:valid])
            if inspect_epoch is not None:
                byte_idx = (2 * inspect_epoch) >> 3
                if byte_idx // self.page_bytes == page:
                    byte = image[byte_idx % self.page_bytes]
                    shift = (2 * inspect_epoch) & 7
                    found = (bool(byte & (1 << shift)),
                             bool(byte & (1 << (shift + 1))))
        self.ledger["bitmap_stream_" + pass_name + "_hash_input_bytes"] += (
            len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
        self.ledger["bitmap_verifier_hashed_bytes"] += (
            len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
        if digest.digest() != root:
            raise Abort("tampered/stale remote PIN bitmap")
        if inspect_epoch is None:
            return None
        if found is None:
            raise AssertionError("no physical page for valid epoch")
        return found

    def _discard_stage(self) -> None:
        if self.bitmap_stage is not None:
            for page in sorted(self.bitmap_stage):
                self.ledger["bitmap_stream_stage_abort_drop_calls"] += 1
                self.ledger["bitmap_stream_stage_abort_drop_request_bytes"] += 8
            self.bitmap_stage = None

    def _mutate(self, reader: int, epoch: int, value: bool,
                *, must_exist: bool = False) -> bool:
        if self.bitmap_generation >= (1 << 64) - 1:
            raise ValueError("PIN authority generation exhausted")
        bit = self._index(reader, epoch)
        before = self._scan(pass_name="pass1", inspect_epoch=epoch)
        if must_exist and not before[reader]:
            raise Abort("trusted PIN token contradicts authenticated remote bit")
        # Only one serialized PIN/UNPIN may stage at a time.
        if self.bitmap_stage is not None:
            raise Abort("bitmap authority stage already occupied")
        self.bitmap_stage = {}
        previous = hashlib.sha256(
            self._DOMAIN + self.bitmap_generation.to_bytes(8, "big"))
        next_generation = self.bitmap_generation + 1
        next_digest = hashlib.sha256(
            self._DOMAIN + next_generation.to_bytes(8, "big"))
        after_bits = None
        try:
            for page in range(self.bitmap_pages):
                image, valid = self._page(page, pass_name="pass2")
                previous.update(image[:valid])
                # Only one old and one new bitmap payload page coexist in
                # trusted algorithmic scratch at any iteration.
                new_page = bytearray(image)
                if (bit >> 3) // self.page_bytes == page:
                    index_in_page = (bit >> 3) % self.page_bytes
                    if value:
                        new_page[index_in_page] |= 1 << (bit & 7)
                    else:
                        new_page[index_in_page] &= ~(1 << (bit & 7))
                    shift = (2 * epoch) & 7
                    byte = new_page[index_in_page]
                    # Both reader bits occupy one byte for any epoch.
                    after_bits = (bool(byte & (1 << shift)),
                                  bool(byte & (1 << (shift + 1))))
                new_image = bytes(new_page)
                self._peak_scratch(valid, two=True)
                next_digest.update(new_image[:valid])
                self.bitmap_stage[page] = new_image
                self.ledger["bitmap_stream_stage_page_writes"] += 1
                self.ledger["bitmap_remote_page_writes"] += 1
                self.ledger["bitmap_remote_upload_bytes"] += self.page_bytes
                self.ledger["bitmap_stream_stage_address_bytes"] += 8
                self.ledger["peak_remote_pages"] = max(
                    self.ledger["peak_remote_pages"], self.remote_pages)
            self.ledger["bitmap_stream_pass2_old_hash_input_bytes"] += (
                len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
            self.ledger["bitmap_stream_stage_new_hash_input_bytes"] += (
                len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
            self.ledger["bitmap_author_hash_input_bytes"] += (
                len(self._DOMAIN) + 8 + self.bitmap_payload_bytes)
            if previous.digest() != self.trusted_bitmap_digest:
                raise Abort("bitmap mutated between authenticated pass1/pass2")
            if after_bits is None:
                raise AssertionError("mutated bit not found")
            # Ideal server stage copy + trusted root publication are
            # serialized. No crash/power-loss atomicity follows.
            old = self.bitmap_store
            self.bitmap_store = self.bitmap_stage
            self.bitmap_stage = None
            self.bitmap_generation = next_generation
            self.trusted_bitmap_digest = next_digest.digest()
            self.ledger["bitmap_trusted_root_publications"] += 1
            self.ledger["bitmap_trusted_root_publication_bytes"] += self._TRUSTED_ROOT_BYTES
            self.ledger["bitmap_stream_retired_bitmap_page_drop_calls"] += len(old)
            self.ledger["bitmap_stream_retired_bitmap_drop_request_bytes"] += len(old) * 8
            return any(after_bits)
        except Exception:
            self._discard_stage()
            raise

    def _retire_if_unpinned(self, epoch: int, *, pinned: bool) -> int:
        self.ledger["bitmap_reclaim_trusted_latest_reads"] += 1
        self.ledger["bitmap_reclaim_trusted_latest_bytes_read"] += self.ROOT_BYTES
        self.ledger["bitmap_reclaim_bit_tests"] += 2
        if epoch == self.epoch or pinned:
            return 0
        pages = self._pages_per_snapshot()
        first = self._slot_start_page(epoch)
        if first + pages > (1 << 64):
            raise OverflowError("remote addressed-delete uint64 overflow")
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
        self._mutate(reader, epoch, True)
        self.readers[reader][epoch] = root
        self.ledger["bitmap_pin_operations"] += 1
        return epoch

    def unpin(self, reader: int, epoch: int) -> None:
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise ValueError("no locally trusted PIN token")
        pinned_after = self._mutate(reader, epoch, False, must_exist=True)
        del self.readers[reader][epoch]
        self.ledger["bitmap_unpin_operations"] += 1
        self._retire_if_unpinned(epoch, pinned=pinned_after)

    def set(self, i: int, value: int) -> int:
        if self.epoch + 1 >= self.epoch_capacity:
            raise ValueError("PIN bitmap epoch capacity exhausted")
        old = self.epoch
        pins = self._scan(pass_name="set_scan", inspect_epoch=old)
        result = SnapshotF1Reference.set(self, i, value)
        self._retire_if_unpinned(old, pinned=any(pins))
        return result

    def gc(self) -> int:
        self.ledger["bitmap_explicit_gc_calls"] += 1
        return 0

    def assert_live_invariant(self) -> None:
        # Offline audit: deliberately separately labeled 2C scans and C
        # independently charged authenticated page read passes. Never
        # confused with one online F1 membership lookup.
        pinned = set()
        for epoch in range(self.epoch_capacity):
            bits = self._scan(pass_name="audit", inspect_epoch=epoch, audit=True)
            if any(bits):
                pinned.add(epoch)
            for reader in (0, 1):
                if (epoch in self.readers[reader]) != bits[reader]:
                    raise AssertionError("reader PIN token != bitmap")
        expected = {self.epoch} | pinned
        if set(self.remote) != expected or set(self.remote_manifests) != expected:
            raise AssertionError("remote PIN history and snapshot live set mismatch")
        if self.bitmap_stage is not None:
            raise AssertionError("unpublished remote bitmap stage remains live")


def compare_streamed_history(initial: tuple[int, ...], page_bytes: int, cap: int = 8):
    validate_contract()
    streamed = StreamedPinBitmapF1(initial, page_bytes, cap)
    bulk = RemotePinBitmapF1(initial, page_bytes, cap)
    truth = [tuple(initial)]
    assert streamed.pin_current(0) == bulk.pin_current(0) == 0
    operations = ((0, initial[0] ^ 1), (0, initial[0] ^ 1), (len(initial) - 1, None))
    for k, (i, b) in enumerate(operations):
        w = list(truth[-1])
        w[i] = w[i] ^ 1 if b is None else b
        truth.append(tuple(w))
        assert streamed.set(i, w[i]) == bulk.set(i, w[i]) == k + 1
        if k == 1:
            assert streamed.pin_current(1) == bulk.pin_current(1) == 2
    for lo in range(len(initial)):
        for hi in range(lo + 1, len(initial) + 1):
            v = sum(truth[-1][lo:hi]) & 1
            assert streamed.latest(0, lo, hi) == bulk.latest(0, lo, hi) == v
            assert streamed.latest(1, lo, hi) == bulk.latest(1, lo, hi) == v
            assert streamed.as_of(0, 0, lo, hi) == bulk.as_of(0, 0, lo, hi) == (
                sum(truth[0][lo:hi]) & 1)
            assert streamed.as_of(1, 2, lo, hi) == bulk.as_of(1, 2, lo, hi) == (
                sum(truth[2][lo:hi]) & 1)
    for reader, epoch in ((0, 0), (1, 2)):
        streamed.unpin(reader, epoch)
        bulk.unpin(reader, epoch)
        assert set(streamed.remote) == set(bulk.remote)
    streamed.assert_live_invariant()
    assert streamed.bitmap_peak_trusted_payload_buffers <= 2 * min(
        streamed.bitmap_payload_bytes, page_bytes)
    assert streamed.ledger["bitmap_stream_stage_page_writes"] == (
        streamed.ledger["bitmap_remote_page_writes"])
    return {
        "n": len(initial), "P": page_bytes, "C": cap,
        "bitmap_bytes": streamed.bitmap_payload_bytes,
        "bitmap_pages": streamed.bitmap_pages,
        "peak_trusted_bitmap_payload_buffer_bytes":
            streamed.bitmap_peak_trusted_payload_buffers,
        "bound": 2 * min(streamed.bitmap_payload_bytes, page_bytes),
        "stream_bitmap_page_reads": streamed.ledger["bitmap_remote_page_read_attempts"],
        "bulk_bitmap_page_reads": bulk.ledger["bitmap_remote_page_read_attempts"],
        "stream_stage_page_writes": streamed.ledger["bitmap_stream_stage_page_writes"],
        "stream_bitmap_peak_remote_pages": streamed.ledger["peak_remote_pages"],
        "bulk_bitmap_peak_remote_pages": bulk.ledger["peak_remote_pages"],
        "root_novelty": "OPEN_UNPROVED",
        "pareto": "UNDECIDABLE_PARTIAL_RESOURCE_VECTOR",
    }


def report():
    return {
        "classification": "CONDITIONAL_STREAMED_PIN_BITMAP_PAGE_IMAGE_UPPER_ONLY",
        "cases": [
            compare_streamed_history((0, 1, 0), 1),
            compare_streamed_history((0, 1, 0, 1, 1), 2),
            compare_streamed_history(tuple((i & 1) for i in range(33)), 64, 17),
        ],
        "full_runtime_RSS_or_crash_safety_proof": False,
        "novel_information_lower_bound": False,
        "root_novelty": "OPEN_UNPROVED",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
