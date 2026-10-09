#!/usr/bin/env python3
"""UCT-005 G3-B2-B: two more F1 upper constructions, same SET/RANGE_PARITY task.

All three constructions use an independently trusted, paid monotone epoch+32B
digest. SHA-256 is assumed collision resistant for conditional soundness.
These are not signature implementations, crash-safe stores, or proof systems.
"""
from dataclasses import dataclass
from hashlib import sha256
import json

from uct005_g3b2b_range_tree import (
    AnchorValue, Reader, QueryCost, QueryOutcome, _check_bit, _check_range,
    _validate_bits, _wire,
)


def _snapshot_digest(bits):
    return sha256(b"UCT005-G3B2B/SNAPSHOT\0"
                  + len(bits).to_bytes(4, "big") + bytes(bits)).digest()


def _initial_log_digest(bits):
    return sha256(b"UCT005-G3B2B/LOG-GENESIS\0"
                  + len(bits).to_bytes(4, "big") + bytes(bits)).digest()


def _advance_log(digest, epoch, index, bit):
    return sha256(b"UCT005-G3B2B/LOG-SET\0" + digest
                  + epoch.to_bytes(8, "big")
                  + index.to_bytes(4, "big") + bytes([bit])).digest()


class SnapshotWriter:
    """O(n) rehash per SET, one remote bit modified, full response per query."""
    def __init__(self, bits):
        self.bits = _validate_bits(bits)
        self.n = len(self.bits)
        self.history = [self.bits]
        self.anchor = AnchorValue(0, _snapshot_digest(self.bits))

    def set(self, index, bit):
        if type(index) is not int or not 0 <= index < self.n:
            raise ValueError("invalid index")
        _check_bit(bit)
        if self.anchor.epoch == 2**64 - 1:
            raise ValueError("epoch overflow")
        next_bits = list(self.bits)
        next_bits[index] = bit
        self.bits = tuple(next_bits)
        self.history.append(self.bits)
        self.anchor = AnchorValue(self.anchor.epoch + 1,
                                  _snapshot_digest(self.bits))
        # Full-state SHA reads n bits, even if SET is idempotent.
        return {"remote_bit_reads_for_hash": self.n,
                "remote_bit_writes": 1, "sha256_calls": 1,
                "anchor_publication_bytes": 40}

    def serve(self, epoch):
        if type(epoch) is not int or not 0 <= epoch < len(self.history):
            raise ValueError("unavailable epoch")
        return _wire({"e": epoch, "bits": list(self.history[epoch])})


def snapshot_query(reader, writer, left, right, epoch=None,
                   anchor_available=True, response=None):
    _check_range(writer.n, left, right)
    if not isinstance(reader, Reader):
        raise ValueError("Reader required")
    if epoch is None:
        epoch = writer.anchor.epoch
    anchor = writer.anchor if anchor_available else None
    delivered = b"" if anchor is None else (
        writer.serve(epoch) if response is None else response)
    if not isinstance(delivered, bytes):
        raise ValueError("response bytes required")
    cost = QueryCost(
        untrusted_request_bytes=len(_wire({"a": left, "b": right}))
                                   if anchor is not None else 0,
        untrusted_response_bytes=len(delivered),
        anchor_request_bytes=1, anchor_response_bytes=40 if anchor else 0,
        anchor_calls=1,
        server_node_reads=writer.n if anchor else 0,
        verifier_hash_calls=0, verifier_xor_ops=0,
        trusted_checkpoint_bytes=40,
    )
    def answer(status, value=None, hashes=0, xors=0):
        from dataclasses import replace
        return QueryOutcome(status, value,
                            anchor.epoch if status == "ACCEPT" else None,
                            replace(cost, verifier_hash_calls=hashes,
                                    verifier_xor_ops=xors))
    if anchor is None:
        return answer("NO_TRUSTED_ANCHOR")
    if (anchor.epoch < reader.checkpoint.epoch or
            (anchor.epoch == reader.checkpoint.epoch and
             anchor.digest != reader.checkpoint.digest)):
        return answer("ANCHOR_ROLLBACK_OR_FORK")
    try:
        obj = json.loads(delivered.decode("ascii"))
        if not isinstance(obj, dict) or _wire(obj) != delivered or set(obj) != {"e", "bits"}:
            raise ValueError("invalid framing")
        if type(obj["e"]) is not int or obj["e"] != anchor.epoch:
            return answer("STALE_OR_EQUIVOCATING_ROOT")
        bits = tuple(obj["bits"])
        if len(bits) != writer.n or any(type(b) is not int or b not in (0, 1)
                                       for b in bits):
            raise ValueError("invalid signed state")
        digest = _snapshot_digest(bits)
        if digest != anchor.digest:
            return answer("INVALID_PROOF", hashes=1)
    except (ValueError, TypeError, UnicodeError, OverflowError, KeyError):
        return answer("INVALID_PROOF")
    reader.checkpoint = anchor
    value = 0
    for bit in bits[left:right + 1]:
        value ^= bit
    return answer("ACCEPT", value, hashes=1, xors=right - left + 1)


@dataclass
class ReplicaReader:
    """n trusted durable bits + 40-byte checkpoint (not low-memory)."""
    bits: tuple
    checkpoint: AnchorValue

    def __post_init__(self):
        self.bits = _validate_bits(self.bits)
        if not isinstance(self.checkpoint, AnchorValue):
            raise ValueError("anchor checkpoint required")


class ReplicaWriter:
    """Append-only SET event log, digest independently anchored each epoch."""
    def __init__(self, bits):
        self.bits = _validate_bits(bits)
        self.n = len(self.bits)
        self.log = []
        self.anchor = AnchorValue(0, _initial_log_digest(self.bits))
        self.genesis = self.anchor

    def set(self, index, bit):
        if type(index) is not int or not 0 <= index < self.n:
            raise ValueError("invalid index")
        _check_bit(bit)
        if self.anchor.epoch == 2**64 - 1:
            raise ValueError("epoch overflow")
        bits = list(self.bits)
        bits[index] = bit
        self.bits = tuple(bits)
        epoch = self.anchor.epoch + 1
        self.log.append({"e": epoch, "i": index, "b": bit})
        self.anchor = AnchorValue(
            epoch, _advance_log(self.anchor.digest, epoch, index, bit))
        return {"author_bit_writes": 1, "sha256_calls": 1,
                "anchor_publication_bytes": 40}

    def serve(self, since_epoch):
        if type(since_epoch) is not int or not 0 <= since_epoch <= self.anchor.epoch:
            raise ValueError("invalid checkpoint")
        return _wire({"updates": self.log[since_epoch:]})


def replica_query(reader, writer, left, right, anchor_available=True,
                  response=None):
    if not isinstance(reader, ReplicaReader):
        raise ValueError("ReplicaReader required")
    _check_range(len(reader.bits), left, right)
    if len(reader.bits) != writer.n:
        raise ValueError("incompatible array")
    anchor = writer.anchor if anchor_available else None
    delivered = b"" if anchor is None else (
        writer.serve(reader.checkpoint.epoch) if response is None else response)
    if not isinstance(delivered, bytes):
        raise ValueError("response must be bytes")
    # Actual canonical JSON response bytes; trusted n bits are paid explicitly.
    cost = QueryCost(
        untrusted_request_bytes=(len(_wire({"a": left, "b": right,
                                           "since": reader.checkpoint.epoch}))
                                 if anchor is not None else 0),
        untrusted_response_bytes=len(delivered),
        anchor_request_bytes=1, anchor_response_bytes=40 if anchor else 0,
        anchor_calls=1,
        server_node_reads=0 if anchor is None else len(writer.log) -
                          min(reader.checkpoint.epoch, len(writer.log)),
        verifier_hash_calls=0, verifier_xor_ops=0,
        trusted_checkpoint_bytes=40 + (len(reader.bits) + 7) // 8,
    )
    def answer(status, value=None, hashes=0, xors=0):
        from dataclasses import replace
        return QueryOutcome(status, value,
                            anchor.epoch if status == "ACCEPT" else None,
                            replace(cost, verifier_hash_calls=hashes,
                                    verifier_xor_ops=xors))
    if anchor is None:
        return answer("NO_TRUSTED_ANCHOR")
    if (anchor.epoch < reader.checkpoint.epoch or
            (anchor.epoch == reader.checkpoint.epoch and
             anchor.digest != reader.checkpoint.digest)):
        return answer("ANCHOR_ROLLBACK_OR_FORK")
    bits = list(reader.bits)
    digest = reader.checkpoint.digest
    epoch = reader.checkpoint.epoch
    calls = 0
    try:
        obj = json.loads(delivered.decode("ascii"))
        if not isinstance(obj, dict) or _wire(obj) != delivered or set(obj) != {"updates"}:
            raise ValueError("invalid log response")
        updates = obj["updates"]
        if not isinstance(updates, list):
            raise ValueError("invalid updates")
        for op in updates:
            if not isinstance(op, dict) or set(op) != {"e", "i", "b"}:
                raise ValueError("invalid operation")
            ne, idx, bit = op["e"], op["i"], op["b"]
            if (type(ne) is not int or ne != epoch + 1 or
                    type(idx) is not int or not 0 <= idx < len(bits)):
                raise ValueError("untrusted epoch or index")
            _check_bit(bit)
            digest = _advance_log(digest, ne, idx, bit)
            bits[idx] = bit
            epoch = ne
            calls += 1
        if epoch != anchor.epoch or digest != anchor.digest:
            return answer("STALE_OR_EQUIVOCATING_LOG", hashes=calls)
    except (ValueError, TypeError, UnicodeError, OverflowError, KeyError):
        return answer("INVALID_PROOF", hashes=calls)
    # All-or-nothing durable checkpoint; cannot claim crash atomicity.
    reader.bits = tuple(bits)
    reader.checkpoint = anchor
    value = 0
    for bit in bits[left:right + 1]:
        value ^= bit
    return answer("ACCEPT", value, hashes=calls,
                  xors=right - left + 1)
