#!/usr/bin/env python3
"""UCT-005 D1-B2-B: page-rounded immutable authenticated COW XOR tree.

A finite research reference, not a filesystem, power-loss proof, or novel
cryptographic theorem. Trusts an ideal globally linearizable, separately paid
epoch/root+PIN authority. Nodes and root manifests live on a Byzantine
remote page-image machine with public fixed-stride addresses.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import struct

ZERO = bytes(32)
NODE = struct.Struct(">4sBIBQQ32s32s")  # 90-byte authenticated prefix
ROOT = struct.Struct(">QQ32s")  # 48-byte remote epoch -> (node-id, digest)
NODE_BYTES = NODE.size + 32  # exactly 122 bytes
ROOT_BYTES = ROOT.size       # exactly 48 bytes
ANCHOR_BYTES = 40           # trusted u64 epoch + SHA256 root
PIN_RECORD_BYTES = 41       # trusted reader u8 + anchor
DOMAIN = b"mathlab.uct005.d1b2b.pagecow.node.v1\0"


class Abort(RuntimeError):
    """Unsafe or unavailable remote data is never accepted."""


def _ceil(x: int, p: int) -> int:
    return (x + p - 1) // p


def _check_bit(b):
    if type(b) is not int or b not in (0, 1):
        raise ValueError("GF2 bit required")


def _decode(raw: bytes) -> dict:
    if not isinstance(raw, bytes) or len(raw) != NODE_BYTES:
        raise Abort("truncated or malformed complete node")
    prefix, digest = raw[:NODE.size], raw[NODE.size:]
    if sha256(DOMAIN + prefix).digest() != digest:
        raise Abort("tampered node hash")
    magic, kind, span, parity, left, right, ld, rd = NODE.unpack(prefix)
    if magic != b"UCTN" or kind not in (0, 1) or span < 1 or parity not in (0, 1):
        raise Abort("bad node grammar")
    if kind == 0:
        if span != 1 or left or right or ld != ZERO or rd != ZERO:
            raise Abort("bad leaf grammar")
    elif left == 0 or right == 0 or ld == ZERO or rd == ZERO:
        raise Abort("bad internal node grammar")
    return dict(kind=kind, span=span, parity=parity, left=left, right=right,
                ld=ld, rd=rd, digest=digest)


def _encode(kind: int, span: int, parity: int, left: int = 0, right: int = 0,
            ld: bytes = ZERO, rd: bytes = ZERO) -> bytes:
    _check_bit(parity)
    if not 1 <= span < 2**32 or not 0 <= left < 2**64 or not 0 <= right < 2**64:
        raise ValueError("node exceeds frozen wire grammar")
    prefix = NODE.pack(b"UCTN", kind, span, parity, left, right, ld, rd)
    raw = prefix + sha256(DOMAIN + prefix).digest()
    _decode(raw)
    return raw


class PageCowTree:
    """Two-reader linearized F1 reference with exact page-image accounting.

    The Python node/root dictionaries are SIMULATED UNTRUSTED FIXED-ADDRESS
    pages. No trusted n-bit writer copy, cached root directory, or free
    epoch->root index is maintained. A public monotone node ID determines
    node page offset; a public epoch determines root slot offset.
    """

    def __init__(self, bits, page_bytes=64):
        bits = tuple(bits)
        if not bits or len(bits) >= 2**32 or any(type(x) is not int or x not in (0, 1) for x in bits):
            raise ValueError("nonempty GF2 word of n<2^32")
        if type(page_bytes) is not int or not 1 <= page_bytes <= 2**32:
            raise ValueError("positive byte page size")
        self.n = len(bits)
        self.P = page_bytes
        self.ledger = Counter()
        self.nodes: dict[int, bytes] = {}
        self.roots: dict[int, bytes] = {}
        self.next_id = 1
        self.epoch = 0
        self.readers: dict[int, dict[int, bytes]] = {0: {}, 1: {}}
        self.authority_pins: dict[tuple[int, int], bytes] = {}
        self.generation = 0
        root_id, digest, _ = self._build(bits, 0, self.n)
        self.latest_digest = digest
        self.roots[0] = ROOT.pack(0, root_id, digest)
        self.ledger["setup_root_page_writes"] += self.root_pages
        self.ledger["setup_remote_upload_bytes"] += self.root_pages * self.P
        self.ledger["setup_anchor_publications"] += 1
        self.ledger["setup_anchor_bytes"] += ANCHOR_BYTES
        self.ledger["setup_bitmap_page_writes"] += self.bitmap_pages
        self.ledger["setup_bitmap_upload_bytes"] += self.bitmap_pages * self.P
        self.ledger["setup_remote_upload_bytes"] += self.bitmap_pages * self.P
        self.ledger["peak_remote_pages"] = self.remote_pages

    @property
    def node_pages(self):
        return _ceil(NODE_BYTES, self.P)

    @property
    def root_pages(self):
        return _ceil(ROOT_BYTES, self.P)

    @property
    def bitmap_pages(self):
        # Persistent allocated/deleted bitmap, 1 bit per issued ID and epoch.
        return _ceil(_ceil(self.next_id + self.epoch + 1, 8), self.P)

    @property
    def remote_pages(self):
        return (len(self.nodes) * self.node_pages
                + len(self.roots) * self.root_pages + self.bitmap_pages)

    @property
    def trusted_bits(self):
        # Latest epoch/root, n, page size, next id, serialized generation,
        # two independent trusted reader-token copies and PIN-authority
        # records. No plaintext writer replica or trusted root lookup table.
        return 8 * (ANCHOR_BYTES + 8 * 4
                    + ANCHOR_BYTES * sum(map(len, self.readers.values()))
                    + PIN_RECORD_BYTES * len(self.authority_pins))

    def _alloc(self, raw: bytes, phase: str) -> tuple[int, bytes]:
        if self.next_id >= 2**64:
            raise ValueError("node-ID overflow")
        node = _decode(raw)
        i = self.next_id
        self.next_id += 1
        self.nodes[i] = raw
        self.ledger[f"{phase}_node_page_writes"] += self.node_pages
        self.ledger[f"{phase}_remote_upload_bytes"] += self.node_pages * self.P
        self.ledger[f"{phase}_hash_calls"] += 1
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages)
        return i, node["digest"]

    def _build(self, bits, lo, hi):
        if hi - lo == 1:
            return (*self._alloc(_encode(0, 1, bits[lo]), "setup"), bits[lo])
        mid = (lo + hi) // 2
        lid, ld, lp = self._build(bits, lo, mid)
        rid, rd, rp = self._build(bits, mid, hi)
        parity = lp ^ rp
        return (*self._alloc(_encode(1, hi - lo, parity, lid, rid, ld, rd), "setup"), parity)

    def _read_node(self, nid: int, expected: bytes, span: int, phase: str) -> dict:
        if type(nid) is not int or nid <= 0 or nid >= self.next_id:
            raise Abort("bad immutable node pointer")
        # Node page offset = (nid-1) * node_pages, independently of all
        # remote dictionaries and of deleted physical-page holes.
        self.ledger[f"{phase}_last_node_page_offset"] = (nid - 1) * self.node_pages
        self.ledger[f"{phase}_node_page_reads"] += self.node_pages
        raw = self.nodes.get(nid)
        if raw is None:
            raise Abort("remote node omitted/reclaimed")
        result = _decode(raw)
        self.ledger[f"{phase}_hash_calls"] += 1
        if result["span"] != span or result["digest"] != expected:
            raise Abort("node hash/span mismatch")
        return result

    def _root(self, epoch: int, expected: bytes, phase: str,
              presented: bytes | None = None) -> int:
        if type(epoch) is not int or not 0 <= epoch <= self.epoch:
            raise Abort("invalid root epoch")
        # Epoch manifest page offset = epoch * root_pages, including holes.
        self.ledger[f"{phase}_last_root_page_offset"] = epoch * self.root_pages
        self.ledger[f"{phase}_root_page_reads"] += self.root_pages
        raw = self.roots.get(epoch) if presented is None else presented
        if not isinstance(raw, bytes) or len(raw) != ROOT_BYTES:
            raise Abort("root page missing/truncated")
        claimed_epoch, nid, digest = ROOT.unpack(raw)
        if claimed_epoch != epoch or digest != expected or not 1 <= nid < self.next_id:
            raise Abort("stale/forged root slot")
        return nid

    def _rewrite(self, nid, digest, lo, hi, index, bit):
        old = self._read_node(nid, digest, hi - lo, "set")
        if hi - lo == 1:
            id2, h2 = self._alloc(_encode(0, 1, bit), "set")
            return id2, h2, old["parity"], bit
        if old["kind"] != 1:
            raise Abort("internal node missing")
        mid = (lo + hi) // 2
        if index < mid:
            left, ld, was, now = self._rewrite(old["left"], old["ld"], lo, mid, index, bit)
            right, rd = old["right"], old["rd"]
        else:
            right, rd, was, now = self._rewrite(old["right"], old["rd"], mid, hi, index, bit)
            left, ld = old["left"], old["ld"]
        newparity = old["parity"] ^ was ^ now
        id2, h2 = self._alloc(_encode(1, hi - lo, newparity,
                                    left, right, ld, rd), "set")
        return id2, h2, old["parity"], newparity

    def set(self, index: int, bit: int) -> int:
        if type(index) is not int or not 0 <= index < self.n:
            raise ValueError("bad SET index")
        _check_bit(bit)
        if self.epoch >= 2**64 - 1:
            raise ValueError("epoch overflow")
        root_id = self._root(self.epoch, self.latest_digest, "set")
        new_id, digest, oldparity, newparity = self._rewrite(
            root_id, self.latest_digest, 0, self.n, index, bit)
        next_epoch = self.epoch + 1
        self.roots[next_epoch] = ROOT.pack(next_epoch, new_id, digest)
        self.epoch = next_epoch
        self.latest_digest = digest
        self.generation += 1
        self.ledger["set_changed_logical_bits"] += int(oldparity != newparity)
        self.ledger["set_root_page_writes"] += self.root_pages
        self.ledger["set_remote_upload_bytes"] += self.root_pages * self.P
        self.ledger["set_anchor_publications"] += 1
        self.ledger["set_anchor_publication_bytes"] += ANCHOR_BYTES
        # Bitmap is stored, not a free allocation/deallocation oracle.
        self.ledger["set_bitmap_page_writes"] += self.bitmap_pages
        self.ledger["set_bitmap_upload_bytes"] += self.bitmap_pages * self.P
        self.ledger["set_remote_upload_bytes"] += self.bitmap_pages * self.P
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages)
        return self.epoch

    def _read_anchor(self):
        self.ledger["anchor_read_calls"] += 1
        self.ledger["anchor_request_bytes"] += 1
        self.ledger["anchor_response_bytes"] += ANCHOR_BYTES
        return self.epoch, self.latest_digest

    def pin_current(self, reader: int):
        if reader not in self.readers:
            raise ValueError("reader must be 0 or 1")
        epoch, digest = self._read_anchor()
        self.readers[reader][epoch] = digest
        self.authority_pins[(reader, epoch)] = digest
        self.generation += 1
        self.ledger["authority_pin_page_writes"] += _ceil(PIN_RECORD_BYTES, self.P)
        self.ledger["authority_pin_bytes"] += PIN_RECORD_BYTES
        return epoch

    def unpin(self, reader: int, epoch: int):
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise ValueError("no such active historical PIN")
        del self.readers[reader][epoch]
        del self.authority_pins[(reader, epoch)]
        self.generation += 1
        self.ledger["authority_pin_page_writes"] += _ceil(PIN_RECORD_BYTES, self.P)
        self.ledger["authority_pin_bytes"] += PIN_RECORD_BYTES

    def make_proof(self, epoch: int, left: int, right: int):
        """Server frontier of raw complete node records; no trusted index."""
        if not 0 <= left < right <= self.n:
            raise ValueError("half-open interval")
        root = self.roots.get(epoch)
        if not isinstance(root, bytes) or len(root) != ROOT_BYTES:
            raise Abort("withheld remote epoch slot")
        _, nid, digest = ROOT.unpack(root)
        out = []
        def visit(i, d, lo, hi):
            rec = self._read_node(i, d, hi - lo, "query")
            out.append(self.nodes[i])
            if right <= lo or hi <= left or (left <= lo and hi <= right):
                return
            if rec["kind"] != 1:
                raise Abort("invalid frontier shape")
            mid = (lo + hi) // 2
            visit(rec["left"], rec["ld"], lo, mid)
            visit(rec["right"], rec["rd"], mid, hi)
        visit(nid, digest, 0, self.n)
        return root, tuple(out)

    def _verify_proof(self, expected: bytes, root_id: int, left: int,
                      right: int, records: tuple[bytes, ...]) -> int:
        pos = 0
        def visit(lo, hi, digest):
            nonlocal pos
            if pos >= len(records):
                raise Abort("truncated frontier proof")
            rec = _decode(records[pos])
            pos += 1
            self.ledger["verify_hash_calls"] += 1
            self.ledger["verify_hash_input_bytes"] += NODE.size + len(DOMAIN)
            if rec["digest"] != digest or rec["span"] != hi - lo:
                raise Abort("wrong frontier node/digest/span")
            if right <= lo or hi <= left:
                return 0, rec["parity"]
            if left <= lo and hi <= right:
                return rec["parity"], rec["parity"]
            if rec["kind"] != 1:
                raise Abort("partial-range internal node missing")
            mid = (lo + hi) // 2
            a, ap = visit(lo, mid, rec["ld"])
            b, bp = visit(mid, hi, rec["rd"])
            if rec["parity"] != (ap ^ bp):
                raise Abort("wrong XOR aggregate")
            return a ^ b, rec["parity"]
        result, _ = visit(0, self.n, expected)
        if pos != len(records):
            raise Abort("noncanonical trailing proof records")
        return result

    def query(self, reader: int, left: int, right: int,
              as_of: int | None = None, *, presented_root: bytes | None = None,
              presented_records: tuple[bytes, ...] | None = None,
              presented_epoch: int | None = None, anchor_available=True):
        if reader not in self.readers or not 0 <= left < right <= self.n:
            raise ValueError("bad reader or half-open interval")
        if as_of is None:
            if not anchor_available:
                self.ledger["anchor_read_calls"] += 1
                self.ledger["anchor_request_bytes"] += 1
                raise Abort("trusted latest anchor withheld")
            epoch, digest = self._read_anchor()
        else:
            if as_of not in self.readers[reader]:
                raise Abort("no independently trusted historical PIN")
            epoch, digest = as_of, self.readers[reader][as_of]
        remote_epoch = epoch if presented_epoch is None else presented_epoch
        # Byzantine replay of an unissued or reclaimed epoch MUST NOT turn
        # a missing Python dict entry into "None -> fetch current root".
        # The attempted remote root-slot read is still charged.
        if type(remote_epoch) is not int or remote_epoch != epoch:
            self.ledger["query_root_page_reads"] += self.root_pages
            raise Abort("stale or invalid server epoch")
        # Each query must read a complete remote 48-byte root slot; it may
        # NOT use a free Python root index or silently skip manifest I/O.
        remote_root = self.roots.get(remote_epoch) if presented_root is None else presented_root
        if remote_root is None:
            self.ledger["query_root_page_reads"] += self.root_pages
            raise Abort("missing remote root slot")
        nid = self._root(epoch, digest, "query", remote_root)
        if presented_records is None:
            _, records = self.make_proof(epoch, left, right)
        else:
            records = presented_records
            # Supplied Byzantine wire records still consume charged server
            # page fetches when materialized from their fixed-stride IDs;
            # a malformed transport must not make reads appear free.
            if isinstance(records, tuple):
                self.ledger["query_node_page_reads"] += len(records) * self.node_pages
        if not isinstance(records, tuple) or any(not isinstance(r, bytes) for r in records):
            raise Abort("malformed proof transport")
        self.ledger["query_remote_request_bytes"] += 8 + 8 + 8
        self.ledger["query_proof_payload_bytes"] += ROOT_BYTES + sum(map(len, records))
        return self._verify_proof(digest, nid, left, right, records)

    def _mark(self, nid, digest, lo, hi, reachable: set[int]):
        if nid in reachable:
            return
        node = self._read_node(nid, digest, hi - lo, "gc")
        reachable.add(nid)
        if hi - lo > 1:
            if node["kind"] != 1:
                raise Abort("invalid live tree shape during GC")
            mid = (lo + hi) // 2
            self._mark(node["left"], node["ld"], lo, mid, reachable)
            self._mark(node["right"], node["rd"], mid, hi, reachable)
        elif node["kind"] != 0:
            raise Abort("invalid live leaf during GC")

    def gc(self, expected_generation: int | None = None) -> int:
        if expected_generation is not None and expected_generation != self.generation:
            raise Abort("stale PIN/GC generation")
        # Entire mark pass verifies pinned roots BEFORE any remote deletion.
        roots = {self.epoch: self.latest_digest}
        for (_, e), digest in self.authority_pins.items():
            if e in roots and roots[e] != digest:
                raise Abort("conflicting trusted roots")
            roots[e] = digest
        reachable = set()
        for e, digest in sorted(roots.items()):
            nid = self._root(e, digest, "gc")
            self._mark(nid, digest, 0, self.n, reachable)
        # Physically inspect entire public address span including holes.
        self.ledger["gc_node_slot_scan_page_reads"] += (
            (self.next_id - 1) * self.node_pages)
        self.ledger["gc_root_slot_scan_page_reads"] += (
            (self.epoch + 1) * self.root_pages)
        dead_nodes = [i for i in range(1, self.next_id) if i in self.nodes and i not in reachable]
        dead_epochs = [e for e in range(self.epoch + 1) if e in self.roots and e not in roots]
        for i in dead_nodes:
            del self.nodes[i]
        for e in dead_epochs:
            del self.roots[e]
        freed = len(dead_nodes) * self.node_pages + len(dead_epochs) * self.root_pages
        self.ledger["gc_logical_pages_freed"] += freed
        self.ledger["gc_bitmap_page_writes"] += self.bitmap_pages
        self.ledger["gc_bitmap_upload_bytes"] += self.bitmap_pages * self.P
        self.ledger["gc_remote_free_calls"] += len(dead_nodes) + len(dead_epochs)
        self.generation += 1
        return freed


def report():
    x = PageCowTree((0, 1, 0, 1, 1), page_bytes=2)
    e0 = x.pin_current(0)
    x.set(0, 1)
    x.set(1, 1)  # no-op but new epoch and COW path
    e2 = x.pin_current(1)
    x.set(4, 0)
    answers = {
        "pinned0": x.query(0, 0, 5, as_of=e0),
        "pinned2": x.query(1, 0, 5, as_of=e2),
        "latest": x.query(0, 0, 5),
    }
    freed = x.gc()
    return {"classification":"CONDITIONAL_PAGE_IMAGE_UPPER_NO_SECURITY_OR_SSD_PROOF",
            "node_record_bytes": NODE_BYTES, "root_slot_bytes": ROOT_BYTES,
            "n":x.n, "P":x.P, "answers":answers,
            "first_gc_freed_pages":freed, "live_remote_pages":x.remote_pages,
            "trusted_bits":x.trusted_bits, "ledger":dict(x.ledger),
            "root_novelty":"OPEN_UNPROVED"}


if __name__ == "__main__":
    import json
    print(json.dumps(report(), indent=2))
