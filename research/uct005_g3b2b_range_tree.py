#!/usr/bin/env python3
"""UCT-005 G3-B2-B: explicit authenticated range-parity UPPER construction.

Stdlib-only research reference; SHA-256 domain-separated commitments are NOT
a cryptographic security theorem, and an ideal monotone trusted anchor is PAID.
The storage-node counters are logical, not physical page I/O measurements.
"""
from dataclasses import dataclass
from hashlib import sha256
import json


def _hash(data):
    return sha256(data).digest()


def _check_bit(bit):
    if type(bit) is not int or bit not in (0, 1):
        raise ValueError("non-binary bit")


def _commit(span, parity, payload):
    _check_bit(parity)
    if not 0 < span <= 2**32 - 1 or len(payload) != 32:
        raise ValueError("invalid commitment fields")
    return _hash(b"UCT005-G3B2B/NODE\0" + span.to_bytes(4, "big")
                 + bytes([parity]) + payload)


def _leaf(bit):
    _check_bit(bit)
    payload = _hash(b"UCT005-G3B2B/LEAF\0" + bytes([bit]))
    return TreeNode(1, bit, payload, _commit(1, bit, payload), None, None)


def _parent(left, right):
    parity = left.parity ^ right.parity
    payload = _hash(b"UCT005-G3B2B/PAIR\0" + left.digest + right.digest)
    span = left.span + right.span
    return TreeNode(span, parity, payload, _commit(span, parity, payload),
                    left, right)


@dataclass(frozen=True)
class TreeNode:
    span: int
    parity: int
    payload: bytes
    digest: bytes
    left: object
    right: object


@dataclass(frozen=True)
class AnchorValue:
    epoch: int
    digest: bytes

    def __post_init__(self):
        if type(self.epoch) is not int or not 0 <= self.epoch < 2**64:
            raise ValueError("epoch outside uint64")
        if not isinstance(self.digest, bytes) or len(self.digest) != 32:
            raise ValueError("expected 32-byte root")

    def wire(self):
        return self.epoch.to_bytes(8, "big") + self.digest


@dataclass(frozen=True)
class UpdateCost:
    remote_node_reads: int
    remote_node_writes: int
    hash_calls: int
    anchor_publications: int
    anchor_publication_bytes: int
    # Neither OS page writes, storage durability, nor network framing included.


@dataclass(frozen=True)
class QueryCost:
    untrusted_request_bytes: int
    untrusted_response_bytes: int
    anchor_request_bytes: int
    anchor_response_bytes: int
    anchor_calls: int
    server_node_reads: int
    verifier_hash_calls: int
    verifier_xor_ops: int
    trusted_checkpoint_bytes: int


@dataclass(frozen=True)
class QueryOutcome:
    status: str
    value: int | None
    epoch: int | None
    cost: QueryCost


@dataclass
class Reader:
    """Exactly one (epoch, digest) trusted persistent checkpoint, not n bits."""
    checkpoint: AnchorValue

    def __post_init__(self):
        if not isinstance(self.checkpoint, AnchorValue):
            raise ValueError("checkpoint required")


def _validate_bits(bits):
    bits = tuple(bits)
    if not bits or len(bits) >= 2**32:
        raise ValueError("nonempty n < 2**32 required")
    for bit in bits:
        _check_bit(bit)
    return bits


def _build(bits, lo, hi):
    if lo == hi:
        return _leaf(bits[lo])
    mid = (lo + hi) // 2
    return _parent(_build(bits, lo, mid), _build(bits, mid + 1, hi))


def _replace(node, lo, hi, index, bit):
    """Persistent path copying; counts node access, copies, and SHA invocations."""
    if lo == hi:
        return _leaf(bit), 1, 1, 2
    mid = (lo + hi) // 2
    if index <= mid:
        new_left, reads, writes, hashes = _replace(
            node.left, lo, mid, index, bit)
        result = _parent(new_left, node.right)
    else:
        new_right, reads, writes, hashes = _replace(
            node.right, mid + 1, hi, index, bit)
        result = _parent(node.left, new_right)
    return result, reads + 1, writes + 1, hashes + 2


def _proof(node, lo, hi, left, right):
    """Canonical interval frontier. No arbitrary prover-chosen query shape."""
    if (right < lo or hi < left) or (left <= lo and hi <= right):
        return {"t": "c", "p": node.parity, "d": node.payload.hex()}, 1
    mid = (lo + hi) // 2
    a, ac = _proof(node.left, lo, mid, left, right)
    b, bc = _proof(node.right, mid + 1, hi, left, right)
    return {"t": "s", "l": a, "r": b}, ac + bc + 1


def _verify_frontier(piece, lo, hi, left, right):
    """Return (commit, total parity, selected parity, SHA calls, XOR calls).

    Raises ValueError for any wrong type, noncanonical shape, or malformed hash.
    No external trust in claimed internal parity: parent recomputation binds it.
    """
    if not isinstance(piece, dict):
        raise ValueError("invalid proof node")
    terminal = (right < lo or hi < left) or (left <= lo and hi <= right)
    if terminal:
        if set(piece) != {"t", "p", "d"} or piece["t"] != "c":
            raise ValueError("noncanonical frontier leaf")
        parity, digest_hex = piece["p"], piece["d"]
        _check_bit(parity)
        if (not isinstance(digest_hex, str) or len(digest_hex) != 64
                or any(c not in "0123456789abcdef" for c in digest_hex)):
            raise ValueError("malformed digest")
        digest = _commit(hi - lo + 1, parity, bytes.fromhex(digest_hex))
        selected = parity if left <= lo and hi <= right else 0
        return digest, parity, selected, 1, 0
    if set(piece) != {"t", "l", "r"} or piece["t"] != "s":
        raise ValueError("noncanonical internal frontier")
    mid = (lo + hi) // 2
    ac, ap, av, ah, ax = _verify_frontier(piece["l"], lo, mid, left, right)
    bc, bp, bv, bh, bx = _verify_frontier(piece["r"], mid + 1, hi, left, right)
    parity = ap ^ bp
    payload = _hash(b"UCT005-G3B2B/PAIR\0" + ac + bc)
    digest = _commit(hi - lo + 1, parity, payload)
    return digest, parity, av ^ bv, ah + bh + 2, ax + bx + 2


def _wire(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


class TreeWriter:
    """One honest author; every SET creates a new epoch including no-ops.

    "anchor" represents a separate ideal atomic monotone root publication,
    NOT merely the newest untrusted server record.
    """
    def __init__(self, bits):
        bits = _validate_bits(bits)
        self.n = len(bits)
        self.roots = [_build(bits, 0, self.n - 1)]
        self.epochs = [AnchorValue(0, self.roots[0].digest)]
        self.anchor = self.epochs[0]
        self.update_costs = []
        self.setup_nodes = 2 * self.n - 1
        self.setup_hash_calls = 2 * self.setup_nodes

    def set(self, index, bit):
        if type(index) is not int or not 0 <= index < self.n:
            raise ValueError("invalid update index")
        _check_bit(bit)
        if self.anchor.epoch >= 2**64 - 1:
            raise ValueError("epoch overflow")
        root, reads, writes, hashes = _replace(
            self.roots[-1], 0, self.n - 1, index, bit)
        value = AnchorValue(self.anchor.epoch + 1, root.digest)
        self.roots.append(root)
        self.epochs.append(value)
        self.anchor = value
        cost = UpdateCost(reads, writes, hashes, 1, len(value.wire()))
        self.update_costs.append(cost)
        return cost

    def serve(self, epoch, left, right):
        """Untrusted server may choose stale epoch; anchor is separate."""
        _check_range(self.n, left, right)
        if type(epoch) is not int or not 0 <= epoch < len(self.roots):
            raise ValueError("unknown server version")
        frontier, visits = _proof(self.roots[epoch], 0, self.n - 1,
                                  left, right)
        return _wire({"e": epoch, "proof": frontier}), visits


def _check_range(n, left, right):
    if (type(left) is not int or type(right) is not int
            or not 0 <= left <= right < n):
        raise ValueError("invalid inclusive range")


def checked_query(reader, n, left, right, response, server_reads,
                  trusted_anchor, anchor_available=True):
    """F1 verifier. Claim LATEST only as of trusted anchor-read instant.

    Cost counts canonical request/reply bytes and ideal anchor traffic.
    User-supplied server_reads is a REPORT, not cryptographically trusted.
    The anchor is read before any remote request; unavailable -> no response.
    """
    _check_range(n, left, right)
    if not isinstance(reader, Reader):
        raise ValueError("reader required")
    if not isinstance(response, bytes):
        raise ValueError("byte response required")
    if type(server_reads) is not int or server_reads < 0:
        raise ValueError("nonnegative node reads required")
    anchor_ok = anchor_available and isinstance(trusted_anchor, AnchorValue)
    request_bytes = len(_wire({"a": left, "b": right})) if anchor_ok else 0
    cost = QueryCost(
        untrusted_request_bytes=request_bytes,
        untrusted_response_bytes=len(response) if anchor_ok else 0,
        anchor_request_bytes=1,
        anchor_response_bytes=40 if anchor_ok else 0,
        anchor_calls=1,
        server_node_reads=server_reads if anchor_ok else 0,
        verifier_hash_calls=0,
        verifier_xor_ops=0,
        trusted_checkpoint_bytes=40,
    )

    def done(status, answer=None, epoch=None, hashes=0, xors=0):
        from dataclasses import replace
        return QueryOutcome(status, answer, epoch,
                            replace(cost, verifier_hash_calls=hashes,
                                    verifier_xor_ops=xors))

    if not anchor_ok:
        return done("NO_TRUSTED_ANCHOR")
    if (trusted_anchor.epoch < reader.checkpoint.epoch or
            (trusted_anchor.epoch == reader.checkpoint.epoch
             and trusted_anchor.digest != reader.checkpoint.digest)):
        return done("ANCHOR_ROLLBACK_OR_FORK")
    try:
        message = json.loads(response.decode("ascii"))
        if _wire(message) != response or not isinstance(message, dict):
            raise ValueError("noncanonical wire")
        if set(message) != {"e", "proof"}:
            raise ValueError("wrong response fields")
        epoch = message["e"]
        if type(epoch) is not int or not 0 <= epoch < 2**64:
            raise ValueError("invalid epoch")
        if epoch != trusted_anchor.epoch:
            return done("STALE_OR_EQUIVOCATING_ROOT")
        digest, _, value, hashes, xors = _verify_frontier(
            message["proof"], 0, n - 1, left, right)
        if digest != trusted_anchor.digest:
            return done("INVALID_PROOF", hashes=hashes, xors=xors)
    except (UnicodeError, ValueError, TypeError, KeyError, RecursionError,
            OverflowError):
        return done("INVALID_PROOF")
    reader.checkpoint = trusted_anchor
    return done("ACCEPT", value, epoch, hashes, xors)


def query_writer(writer, reader, epoch, left, right, anchor_available=True):
    """Honest server delivery with separately supplied trusted writer anchor."""
    if not anchor_available:
        return checked_query(reader, writer.n, left, right, b"", 0,
                             None, anchor_available=False)
    response, reads = writer.serve(epoch, left, right)
    return checked_query(reader, writer.n, left, right, response, reads,
                         writer.anchor)
