#!/usr/bin/env python3
"""D1-B2-D: byte-conserving authenticated REMOTE PIN bitmap upper model.

The trusted PIN authority retains only a generation/digest (40 bytes), not a
state-dependent full bitmap. Clients independently retain their paid PIN
roots. Full remote bitmap reads, writes, hashing and page deletes are charged.
This is an HONEST-SERVER page-image reference with SHA binding assumed, not
a physical crash-safe storage system or a new joint lower-bound theorem.
"""
from __future__ import annotations

import hashlib
import itertools
import json

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference, validate_contract
from uct005_d1b2c_eager_pin_reclaim import EagerPinReclaim


class RemotePinBitmapF1(SnapshotF1Reference):
    """Two-client, bounded-epoch, remote bitset controlled by trusted digest."""

    _DOMAIN = b"Mathlab.D1.B2.D.remote-pin-bitmap.v1\0"
    _TRUSTED_ROOT_BYTES = 40  # u64 bitmap generation + SHA256 digest

    def __init__(self, bits: tuple[int, ...], page_bytes: int,
                 epoch_capacity: int):
        if not 2 <= epoch_capacity <= 65536:
            raise ValueError("bounded epoch capacity must be 2..65536")
        self.epoch_capacity = epoch_capacity
        super().__init__(bits, page_bytes)
        self.remote_pin_bitmap: bytes | None = bytes((2 * epoch_capacity + 7) // 8)
        self.bitmap_generation = 0
        self.trusted_bitmap_digest = self._bitmap_digest(0, self.remote_pin_bitmap)
        self.ledger["bitmap_setup_page_writes"] += self.bitmap_pages
        self.ledger["bitmap_setup_upload_bytes"] += self.bitmap_pages * self.page_bytes
        self.ledger["bitmap_setup_hashed_bytes"] += len(self._DOMAIN) + 8 + len(self.remote_pin_bitmap)
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages
        )

    @property
    def bitmap_payload_bytes(self) -> int:
        return (2 * self.epoch_capacity + 7) // 8

    @property
    def bitmap_pages(self) -> int:
        return (self.bitmap_payload_bytes + self.page_bytes - 1) // self.page_bytes

    @property
    def remote_pages(self) -> int:
        snapshot_pages = super().remote_pages
        return snapshot_pages + (self.bitmap_pages
                                 if hasattr(self, "remote_pin_bitmap") else 0)

    def _slot_start_page(self, epoch: int) -> int:
        # The remote PIN bitmap occupies physical pages [0, bitmap_pages).
        # PAGE-001 immutable epoch slots follow those pages with no overlap;
        # all addresses are public arithmetic, with no hidden object index.
        return self.bitmap_pages + epoch * self._pages_per_snapshot()

    @property
    def trusted_bits(self) -> int:
        # Unused inherited pin_registry dict must remain empty: otherwise
        # an unpriced authoritative copy would invalidate the comparison.
        if self.pin_registry:
            raise AssertionError("unexpected trusted replica of PIN bitmap")
        return super().trusted_bits + 8 * self._TRUSTED_ROOT_BYTES

    def _bitmap_digest(self, generation: int, bitmap: bytes) -> bytes:
        if not 0 <= generation < 1 << 64:
            raise ValueError("bitmap generation outside uint64")
        return hashlib.sha256(
            self._DOMAIN + generation.to_bytes(8, "big") + bitmap
        ).digest()

    def _read_verified_bitmap(self, audit: bool = False) -> bytes:
        # Test-only invariant checks must not inflate operational counters:
        # their own authenticating reads are still charged under audit_*.
        prefix = "bitmap_audit" if audit else "bitmap"
        self.ledger[prefix + "_trusted_root_reads"] += 1
        self.ledger[prefix + "_trusted_root_bytes_read"] += self._TRUSTED_ROOT_BYTES
        self.ledger[prefix + "_remote_page_read_attempts"] += self.bitmap_pages
        candidate = self.remote_pin_bitmap
        if candidate is None:
            raise Abort("withheld remote PIN bitmap")
        self.ledger[prefix + "_remote_payload_bytes"] += len(candidate)
        if len(candidate) != self.bitmap_payload_bytes:
            raise Abort("truncated or lengthened PIN bitmap")
        self.ledger[prefix + "_verifier_hashed_bytes"] += len(self._DOMAIN) + 8 + len(candidate)
        if self._bitmap_digest(self.bitmap_generation, candidate) != (
                self.trusted_bitmap_digest):
            raise Abort("stale/tampered remote PIN bitmap")
        return candidate

    def _publish_bitmap(self, image: bytes) -> None:
        if len(image) != self.bitmap_payload_bytes:
            raise ValueError("PIN bitmap has incorrect byte length")
        if self.bitmap_generation == (1 << 64) - 1:
            raise ValueError("PIN authority generation exhausted")
        # Ideal serialized authority commits remote image + trusted root.
        new_sequence = self.bitmap_generation + 1
        new_digest = self._bitmap_digest(new_sequence, image)
        self.remote_pin_bitmap = image
        self.bitmap_generation = new_sequence
        self.trusted_bitmap_digest = new_digest
        self.ledger["bitmap_remote_page_writes"] += self.bitmap_pages
        self.ledger["bitmap_remote_upload_bytes"] += self.bitmap_pages * self.page_bytes
        self.ledger["bitmap_author_hash_input_bytes"] += len(self._DOMAIN) + 8 + len(image)
        self.ledger["bitmap_trusted_root_publications"] += 1
        self.ledger["bitmap_trusted_root_publication_bytes"] += self._TRUSTED_ROOT_BYTES

    def _index(self, reader: int, epoch: int) -> int:
        if reader not in (0, 1) or not 0 <= epoch < self.epoch_capacity:
            raise ValueError("reader or epoch outside registered PIN contract")
        return 2 * epoch + reader

    @staticmethod
    def _set_bit(bitmap: bytes, index: int, value: bool) -> bytes:
        updated = bytearray(bitmap)
        if value:
            updated[index >> 3] |= 1 << (index & 7)
        else:
            updated[index >> 3] &= ~(1 << (index & 7))
        return bytes(updated)

    @staticmethod
    def _has_bit(bitmap: bytes, index: int) -> bool:
        return bool(bitmap[index >> 3] & (1 << (index & 7)))

    def _retire_epoch(self, epoch: int, verified_bitmap: bytes) -> int:
        self.ledger["bitmap_reclaim_trusted_latest_reads"] += 1
        self.ledger["bitmap_reclaim_trusted_latest_bytes_read"] += self.ROOT_BYTES
        if epoch == self.epoch:
            return 0
        # Scan the TWO bits for this epoch in an already authenticated
        # full bitmap; no free lookup into readers' local PIN dictionaries.
        first_pinned = self._has_bit(verified_bitmap, self._index(0, epoch))
        second_pinned = self._has_bit(verified_bitmap, self._index(1, epoch))
        self.ledger["bitmap_reclaim_bit_tests"] += 2
        if first_pinned or second_pinned:
            return 0
        pages = self._pages_per_snapshot()
        first = self._slot_start_page(epoch)
        if first + pages > 1 << 64:
            raise OverflowError("remote addressed-delete uint64 overflow")
        for page in range(first, first + pages):
            self.ledger["bitmap_remote_drop_page_calls"] += 1
            self.ledger["bitmap_remote_drop_request_bytes"] += 8
        # An honest remote page API executes DROP_PAGE. A malicious server
        # may refuse; this model does not assert Byzantine availability.
        self.remote.pop(epoch, None)
        self.remote_manifests.pop(epoch, None)
        self.ledger["bitmap_logical_pages_reclaimed"] += pages
        return pages

    def pin_current(self, reader: int) -> int:
        if reader not in self.readers:
            raise ValueError("unknown reader")
        epoch, root = self._read_anchor()
        authenticated = self._read_verified_bitmap()
        updated = self._set_bit(authenticated, self._index(reader, epoch), True)
        self._publish_bitmap(updated)
        # Locally held PIN root belongs to this reader; authority itself
        # owns only its 40-byte bitmap commitment.
        self.readers[reader][epoch] = root
        self.ledger["bitmap_pin_operations"] += 1
        return epoch

    def unpin(self, reader: int, epoch: int) -> None:
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise ValueError("no locally trusted PIN token")
        authenticated = self._read_verified_bitmap()
        index = self._index(reader, epoch)
        if not self._has_bit(authenticated, index):
            raise Abort("PIN registry contradicts locally trusted client token")
        updated = self._set_bit(authenticated, index, False)
        self._publish_bitmap(updated)
        del self.readers[reader][epoch]
        self.ledger["bitmap_unpin_operations"] += 1
        self._retire_epoch(epoch, updated)

    def set(self, i: int, value: int) -> int:
        if self.epoch + 1 >= self.epoch_capacity:
            raise ValueError("PIN bitmap epoch capacity exhausted")
        # Authenticate the old authoritative registry before committing a
        # new epoch. The same trusted serialized transaction ensures there
        # cannot be an interleaved PIN of the retired old latest.
        authenticated = self._read_verified_bitmap()
        old_latest = self.epoch
        result = super().set(i, value)
        self._retire_epoch(old_latest, authenticated)
        return result

    def gc(self) -> int:
        # Under honest serialized transitions, every unpinned old version
        # was reclaimed at SET or final UNPIN. Explicit GC costs one call,
        # with no remote historical manifest directory enumeration.
        self.ledger["bitmap_explicit_gc_calls"] += 1
        return 0

    def assert_live_invariant(self) -> None:
        image = self._read_verified_bitmap(audit=True)
        pinned = {
            e for e in range(self.epoch_capacity)
            if self._has_bit(image, 2 * e) or self._has_bit(image, 2 * e + 1)
        }
        expected = {self.epoch} | pinned
        if set(self.remote) != expected or set(self.remote_manifests) != expected:
            raise AssertionError("remote PIN bitmap and live snapshots disagree")
        for reader in (0, 1):
            local = set(self.readers[reader])
            remote = {
                e for e in range(self.epoch_capacity)
                if self._has_bit(image, self._index(reader, e))
            }
            if local != remote:
                raise AssertionError("PIN bitmap diverges from client trusted tokens")


def future_pin_signature_count(horizon: int, eligible: tuple[int, ...]) -> int:
    """Independent enumeration of observable subsets at eligible epochs."""
    if horizon < 0 or len(set(eligible)) != len(eligible) or any(
            t < 0 or t >= horizon for t in eligible):
        raise ValueError("invalid set of eligible historic PIN epochs")
    return len({
        tuple(int(i in subset) for i in range(horizon))
        for k in range(len(eligible) + 1)
        for subset in itertools.combinations(eligible, k)
    })


def compare_history(bits: tuple[int, ...], page_bytes: int) -> dict:
    validate_contract()
    n = len(bits)
    if n < 1 or any(type(x) is not int or x not in (0, 1) for x in bits):
        raise ValueError("nonempty binary word required")
    if page_bytes < 1:
        raise ValueError("page size must be positive")
    remote = RemotePinBitmapF1(bits, page_bytes, epoch_capacity=8)
    trusted = EagerPinReclaim(bits, page_bytes)
    truth = [bits]
    p0 = remote.pin_current(0)
    assert p0 == trusted.pin_current(0) == 0
    ops = ((0, bits[0] ^ 1),
           (0, bits[0] ^ 1),
           (n - 1, None))
    for index, (pos, desired) in enumerate(ops):
        previous = list(truth[-1])
        value = previous[pos] ^ 1 if desired is None else desired
        previous[pos] = value
        truth.append(tuple(previous))
        assert remote.set(pos, value) == trusted.set(pos, value) == index + 1
        if index == 1:
            assert remote.pin_current(1) == trusted.pin_current(1) == 2
    remote.assert_live_invariant()
    assert set(remote.remote) == set(trusted.remote) == {0, 2, 3}
    for left in range(n):
        for right in range(left + 1, n + 1):
            current = sum(truth[-1][left:right]) & 1
            historic0 = sum(truth[0][left:right]) & 1
            historic2 = sum(truth[2][left:right]) & 1
            for reader in (0, 1):
                assert remote.latest(reader, left, right) == current
                assert trusted.latest(reader, left, right) == current
            assert remote.as_of(0, 0, left, right) == historic0
            assert trusted.as_of(0, 0, left, right) == historic0
            assert remote.as_of(1, 2, left, right) == historic2
            assert trusted.as_of(1, 2, left, right) == historic2
    remote.unpin(0, 0)
    trusted.unpin(0, 0)
    remote.assert_live_invariant()
    remote.unpin(1, 2)
    trusted.unpin(1, 2)
    remote.assert_live_invariant()
    assert set(remote.remote) == set(trusted.remote) == {3}
    return {
        "status": "CLASSICAL_REMOTE_AUTH_PIN_BITMAP_UPPER_NOT_NEW_LOWER_BOUND",
        "n": n, "P": page_bytes,
        "remote_bitmap_bytes": remote.bitmap_payload_bytes,
        "remote_bitmap_pages": remote.bitmap_pages,
        "trusted_registry_commitment_bytes": 40,
        "bitmap_remote_page_read_attempts": remote.ledger["bitmap_remote_page_read_attempts"],
        "bitmap_remote_page_writes": remote.ledger["bitmap_remote_page_writes"],
        "bitmap_author_hash_input_bytes": remote.ledger["bitmap_author_hash_input_bytes"],
        "bitmap_verifier_hashed_bytes": remote.ledger["bitmap_verifier_hashed_bytes"],
        "bitmap_trusted_root_bytes_read": remote.ledger["bitmap_trusted_root_bytes_read"],
        "bitmap_trusted_root_publication_bytes": remote.ledger["bitmap_trusted_root_publication_bytes"],
        "bitmap_remote_drop_page_calls": remote.ledger["bitmap_remote_drop_page_calls"],
        "trusted_eager_pin_record_page_reads": trusted.ledger["eager_authority_pin_record_page_reads"],
        "remote_pin_registry_local_trusted_bytes_excluding_reader_roots": 40,
        "trusted_eager_pin_registry_active_record_bytes": 0,
        "latest_snapshot_only": True,
        "root_novelty": "OPEN_UNPROVED",
        "cost_frontier": "PARTIAL_NO_FULL_PARETO",
    }


def report() -> dict:
    return {
        "classification": "CLASSICAL_FINITE_HISTORY_INFO_AND_AUTHENTICATED_REMOTE_BITMAP",
        "five_epoch_pin_signatures": future_pin_signature_count(5, tuple(range(5))),
        "cases": [compare_history(tuple(i & 1 for i in range(n)), p)
                  for n, p in ((1, 1), (3, 2), (8, 8), (33, 2))],
        "cryptographic_theorem": False,
        "physical_durability_proof": False,
        "root_novelty": "OPEN_UNPROVED",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
