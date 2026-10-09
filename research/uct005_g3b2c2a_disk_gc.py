#!/usr/bin/env python3
"""UCT-005 G3-B2-C2-A: disk-file GC with constant PAGE-BUFFER workspace.

All graph/page-address sets and the BFS queue live in temporary files. This
models explicit full-image seek/read/write operations, NOT raw device I/O or a
verified filesystem/atomic pin journal. Python runtime RSS is not bounded.
Only collector algorithm page-buffer count is bounded independently of n,H.
"""
from dataclasses import dataclass
import struct
import tempfile

from uct005_g3b2b_range_tree import _commit, _hash, _leaf

NULL = 2**64 - 1
NODE = struct.Struct("<QQIB32s32s")
ROOT = struct.Struct("<Q32s")
PIN = struct.Struct("<QQ32s")


@dataclass(frozen=True)
class Cost:
    page_reads: int
    page_writes: int
    queue_pages_read: int
    queue_pages_written: int
    node_pages_read: int
    bitmap_pages_read: int
    bitmap_pages_written: int
    root_pin_pages_read: int
    metadata_init_writes: int
    logical_trim_commands: int
    freed_nodes: int
    live_nodes: int
    total_nodes: int
    gc_sha256_calls: int
    page_size: int
    max_collector_page_buffers: int

    @property
    def read_bytes(self):
        return self.page_reads * self.page_size

    @property
    def write_bytes(self):
        return self.page_writes * self.page_size


class Account:
    def __init__(self):
        self.counts = dict.fromkeys((
            "page_reads", "page_writes", "queue_pages_read",
            "queue_pages_written", "node_pages_read", "bitmap_pages_read",
            "bitmap_pages_written", "root_pin_pages_read",
            "metadata_init_writes", "logical_trim_commands"), 0)

    def count(self, key):
        self.counts[key] += 1

    def read(self, file, page, size, kind):
        if type(page) is not int or page < 0:
            raise ValueError("invalid physical page")
        file.seek(page * size)
        result = file.read(size)
        if len(result) != size:
            raise ValueError("truncated disk-backed page")
        self.count("page_reads")
        self.count(kind)
        return result

    def write(self, file, page, payload, size, kind):
        if len(payload) != size:
            raise ValueError("partial page image")
        file.seek(page * size)
        if file.write(payload) != size:
            raise OSError("short file-image write")
        self.count("page_writes")
        self.count(kind)


class DiskGcArena:
    """Immutable forest exported from authentic B2-B roots; collector O(1) pages.

    Each graph NODE uses a full physical page; this is a NEW upper construction,
    not a claim that one page holds only a node under C0's 25-slot packing.
    Immutable root records each use a full separate page; each reader pin is
    one fixed on-disk page slot. The index and pins are NOT crash-durable.
    No in-memory graph IDs, live-ID set, mark set or queue after export.
    """
    BUFFER_LIMIT = 6

    def __init__(self, page_bytes=4096, clients=2):
        if type(page_bytes) is not int or page_bytes < max(256, NODE.size, PIN.size):
            raise ValueError("page must fit records")
        if type(clients) is not int or clients < 1:
            raise ValueError("positive number of reader slots")
        self.page_bytes = page_bytes
        self.clients = clients
        self.nodes = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.roots = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.pins = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.alive = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.count = 0
        self.epochs = 0
        self.latest_trusted_checkpoint = None
        self._has_reclaimed = False
        self._build_writes = 0
        for client in range(clients):
            self.pins.write(bytes(page_bytes))
            self._build_writes += 1

    @classmethod
    def from_writer(cls, writer, page_bytes=4096, clients=2):
        obj = cls(page_bytes, clients)
        # SETUP ONLY: allocation-map uses unbounded Python RAM to export a
        # completed forest; it is discarded. Collector itself never uses it.
        ids = {}
        def export(node):
            key = id(node)
            if key in ids:
                return ids[key]
            left = export(node.left) if node.left is not None else NULL
            right = export(node.right) if node.right is not None else NULL
            index = obj.count
            raw = NODE.pack(left, right, node.span, node.parity,
                            node.payload, node.digest)
            obj.nodes.seek(index * page_bytes)
            obj.nodes.write(raw.ljust(page_bytes, b"\0"))
            obj.count += 1
            obj._build_writes += 1
            ids[key] = index
            return index
        obj._root_span_limit = writer.n
        obj.latest_trusted_checkpoint = writer.anchor
        for epoch, root in enumerate(writer.roots):
            index = export(root)
            expected = writer.epochs[epoch]
            if expected.digest != root.digest:
                raise ValueError("writer epoch root mismatch")
            obj.roots.write(ROOT.pack(index, root.digest).ljust(page_bytes, b"\0"))
            obj._build_writes += 1
            obj.epochs += 1
        blocks = (obj.count + page_bytes - 1) // page_bytes
        for start in range(blocks):
            used = min(page_bytes, obj.count - start*page_bytes)
            obj.alive.write((b"\x01" * used).ljust(page_bytes, b"\0"))
            obj._build_writes += 1
        return obj

    @property
    def latest(self):
        return self.epochs - 1

    @property
    def setup_page_writes(self):
        return self._build_writes

    def _page(self, file, index):
        file.seek(index*self.page_bytes)
        raw = file.read(self.page_bytes)
        if len(raw) != self.page_bytes:
            raise ValueError("missing root or pin page")
        return raw

    def _root(self, epoch):
        if type(epoch) is not int or not 0 <= epoch < self.epochs:
            raise ValueError("invalid root epoch")
        return ROOT.unpack_from(self._page(self.roots, epoch))

    def _live(self, index):
        if type(index) is not int or not 0 <= index < self.count:
            raise ValueError("invalid node index")
        page = self._page(self.alive, index // self.page_bytes)
        return bool(page[index % self.page_bytes])

    def _node(self, index):
        if not self._live(index):
            raise ValueError("remote node was logically reclaimed")
        return NODE.unpack_from(self._page(self.nodes, index))

    def pin_epoch(self, client, epoch, checkpoint):
        """Authenticated pin BEFORE first GC, or to current latest after GC.

        An old epoch can be pinned after forest export but only before the
        first reclamation. This avoids impossible resurrection while charging
        all authenticated input and explicit root-index lookup. No crash log.
        """
        if type(client) is not int or not 0 <= client < self.clients:
            raise ValueError("client slot out of range")
        if type(epoch) is not int or not 0 <= epoch <= self.latest:
            raise ValueError("invalid pin epoch")
        if self._has_reclaimed and epoch != self.latest:
            raise ValueError("cannot revive past epoch after GC")
        root, digest = self._root(epoch)
        if checkpoint.epoch != epoch or checkpoint.digest != digest:
            raise ValueError("unauthenticated historical checkpoint")
        if not self._live(root):
            raise ValueError("cannot pin reclaimed root")
        self.pins.seek(client*self.page_bytes)
        self.pins.write(PIN.pack(epoch, root, digest).ljust(self.page_bytes, b"\0"))
        # One root image READ and one pin image WRITE; checkpoint already
        # acquired over a separately paid independent trust channel.
        return {"root_page_reads": 1, "pin_page_writes": 1,
                "read_bytes": self.page_bytes, "write_bytes": self.page_bytes,
                "trusted_checkpoint_bytes": 40}

    def release(self, client):
        if type(client) is not int or not 0 <= client < self.clients:
            raise ValueError("client slot out of range")
        epoch, root, digest = PIN.unpack_from(self._page(self.pins, client))
        if digest == bytes(32):
            raise ValueError("slot not pinned")
        self.pins.seek(client*self.page_bytes)
        self.pins.write(bytes(self.page_bytes))
        return {"pin_page_reads": 1, "pin_page_writes": 1,
                "read_bytes": self.page_bytes, "write_bytes": self.page_bytes}

    def _pin_epoch(self, client):
        e, root, digest = PIN.unpack_from(self._page(self.pins, client))
        return None if digest == bytes(32) else (e, root, digest)

    def verify_range(self, epoch, left, right, checkpoint):
        """Full-tree reference verifier; query workspace NOT O(1) pages.

        Hash reconstruction uses the B2-B domain separation. This independent
        verifier is deliberately O(n) reads; only COLLECTOR is page-bounded.
        """
        if type(left) is not int or type(right) is not int:
            raise ValueError("range indices required")
        root, root_digest = self._root(epoch)
        if checkpoint.epoch != epoch or checkpoint.digest != root_digest:
            raise ValueError("no authentic checkpoint for requested epoch")
        if epoch != self.latest and not any(
            (p := self._pin_epoch(i)) is not None and p[0] == epoch
            for i in range(self.clients)
        ):
            raise ValueError("old epoch not pinned")
        def visit(page, lo, depth=0):
            if depth > (self._root_span_limit-1).bit_length():
                raise ValueError("noncanonical tree depth or forged cycle")
            a, b, span, bit, payload, digest = self._node(page)
            if span == 1:
                if a != NULL or b != NULL:
                    raise ValueError("malformed leaf")
                expected = _leaf(bit)
                if payload != expected.payload or digest != expected.digest:
                    raise ValueError("leaf corruption")
                chosen = bit if left <= lo <= right else 0
                return digest, span, bit, chosen
            if a == NULL or b == NULL or a >= self.count or b >= self.count:
                raise ValueError("malformed internal node")
            lc, ls, lp, lv = visit(a, lo, depth+1)
            rc, rs, rp, rv = visit(b, lo+ls, depth+1)
            computed = _hash(b"UCT005-G3B2B/PAIR\0" + lc + rc)
            if payload != computed or span != ls+rs or bit != (lp ^ rp):
                raise ValueError("corrupt node structure")
            if digest != _commit(span, bit, computed):
                raise ValueError("corrupt node commitment")
            return digest, span, bit, lv ^ rv
        digest, span, _, value = visit(root, 0)
        if not 0 <= left <= right < span or digest != root_digest:
            raise ValueError("wrong range or authenticated root")
        return value

    def collect(self, expected_epoch, interrupt_after_trims=None):
        """Disk FIFO + page bitmap + alive bitmap: O(6) page buffers.

        Logical TRIM only flips durable-model alive bit. Freed data bytes still
        exist in the tempfile; actual sparse file punching is NOT claimed.
        Pins and latest epoch MUST remain frozen throughout this operation.
        A simulated crash after k flips is recoverable by a NEW mark/sweep
        under the same frozen root/pin configuration; not a general fsync proof.
        """
        if type(expected_epoch) is not int or expected_epoch != self.latest:
            raise ValueError("stale or invalid collection epoch")
        if interrupt_after_trims is not None and (
            type(interrupt_after_trims) is not int or interrupt_after_trims < 0
        ):
            raise ValueError("invalid crash cut")
        size = self.page_bytes
        counts = Account()
        mark = tempfile.TemporaryFile(mode="w+b", buffering=0)
        queue = tempfile.TemporaryFile(mode="w+b", buffering=0)
        try:
            blocks = (self.count+size-1)//size
            for block in range(blocks):
                counts.write(mark, block, bytes(size), size, "metadata_init_writes")
            appended = 0
            popped = 0
            def append(page_id):
                nonlocal appended
                counts.write(queue, appended,
                             struct.pack("<Q", page_id).ljust(size, b"\0"),
                             size, "queue_pages_written")
                appended += 1
            latest = counts.read(self.roots, self.latest, size,
                                 "root_pin_pages_read")
            newest_node, newest_digest = ROOT.unpack_from(latest)
            del latest
            if (self.latest_trusted_checkpoint.epoch != self.latest
                    or newest_digest != self.latest_trusted_checkpoint.digest):
                raise ValueError("untrusted latest root conflicts with trusted anchor")
            latest_node = counts.read(self.nodes, newest_node, size,
                                      "node_pages_read")
            if NODE.unpack_from(latest_node)[-1] != newest_digest:
                raise ValueError("latest pointer does not match trusted root")
            del latest_node
            append(newest_node)
            for i in range(self.clients):
                pin = counts.read(self.pins, i, size, "root_pin_pages_read")
                epoch, node, digest = PIN.unpack_from(pin)
                del pin
                if digest != bytes(32):
                    expected = counts.read(self.roots, epoch, size,
                                           "root_pin_pages_read")
                    rid, authentic = ROOT.unpack_from(expected)
                    del expected
                    if node != rid or digest != authentic:
                        raise ValueError("pin does not match stored epoch root")
                    pinned_node = counts.read(self.nodes, node, size,
                                              "node_pages_read")
                    if NODE.unpack_from(pinned_node)[-1] != digest:
                        raise ValueError("pinned node does not match checkpoint")
                    del pinned_node
                    append(node)
            # Queue lives entirely on a FILE, not a Python list/deque.
            hash_calls = 0
            while popped < appended:
                entry = counts.read(queue, popped, size, "queue_pages_read")
                page_id, = struct.unpack_from("<Q", entry)
                del entry
                popped += 1
                if page_id >= self.count:
                    raise ValueError("child references invalid page")
                block, offset = divmod(page_id, size)
                image = counts.read(mark, block, size, "bitmap_pages_read")
                if image[offset]:
                    del image
                    continue
                changed = bytearray(image)
                del image
                changed[offset] = 1
                counts.write(mark, block, changed, size, "bitmap_pages_written")
                del changed
                live = counts.read(self.alive, block, size,
                                   "bitmap_pages_read")
                if not live[offset]:
                    raise ValueError("required retained node already freed")
                del live
                node_image = counts.read(self.nodes, page_id, size,
                                         "node_pages_read")
                a, b, span, bit, payload, digest = NODE.unpack_from(node_image)
                del node_image
                if (a == NULL) != (b == NULL):
                    raise ValueError("invalid child pair")
                if a == NULL:
                    if span != 1:
                        raise ValueError("non-leaf or bad length")
                    leaf = _leaf(bit)
                    hash_calls += 2
                    if payload != leaf.payload or digest != leaf.digest:
                        raise ValueError("malformed authenticated leaf")
                else:
                    if a >= self.count or b >= self.count:
                        raise ValueError("out-of-bounds child pointer")
                    child_l = counts.read(self.nodes, a, size, "node_pages_read")
                    child_r = counts.read(self.nodes, b, size, "node_pages_read")
                    _, _, la, lp, _, ld = NODE.unpack_from(child_l)
                    del child_l
                    _, _, ra, rp, _, rd = NODE.unpack_from(child_r)
                    del child_r
                    expected_payload = _hash(b"UCT005-G3B2B/PAIR\0" + ld + rd)
                    expected_digest = _commit(span, bit, expected_payload)
                    hash_calls += 2
                    if (la+ra != span or lp ^ rp != bit
                            or payload != expected_payload
                            or digest != expected_digest):
                        raise ValueError("untrusted child link changed")
                    append(a)
                    append(b)
            freed = 0
            living = 0
            for page_id in range(self.count):
                block, off = divmod(page_id, size)
                marked = counts.read(mark, block, size, "bitmap_pages_read")
                exists = counts.read(self.alive, block, size, "bitmap_pages_read")
                if not exists[off]:
                    del marked, exists
                    continue
                if marked[off]:
                    living += 1
                    del marked, exists
                    continue
                changed = bytearray(exists)
                del marked, exists
                changed[off] = 0
                counts.write(self.alive, block, changed, size,
                             "bitmap_pages_written")
                del changed
                freed += 1
                self._has_reclaimed = True
                counts.count("logical_trim_commands")
                if interrupt_after_trims is not None and freed >= interrupt_after_trims:
                    raise RuntimeError("injected power-loss AFTER complete mark phase")
            # Count previously freed nodes as not live; no uncharged set.
            living = self._alive_total(counts)
            return Cost(
                **counts.counts, freed_nodes=freed, live_nodes=living,
                gc_sha256_calls=hash_calls,
                total_nodes=self.count, page_size=size,
                max_collector_page_buffers=self.BUFFER_LIMIT,
            )
        finally:
            mark.close()
            queue.close()

    def _alive_total(self, counts):
        """Scan living bitmap on disk and charge every final census read."""
        total = 0
        for block in range((self.count+self.page_bytes-1)//self.page_bytes):
            raw = counts.read(self.alive, block, self.page_bytes, "bitmap_pages_read")
            total += raw.count(1)
        return total

    def close(self):
        for f in (self.nodes, self.roots, self.pins, self.alive):
            f.close()


def main():
    import json
    from uct005_g3b2b_range_tree import TreeWriter
    writer = TreeWriter((0,)*16)
    forest = None
    writer.set(0, 1)
    writer.set(2, 1)
    try:
        forest = DiskGcArena.from_writer(writer, clients=2)
        forest.pin_epoch(0, forest.latest, writer.anchor)
        charge = forest.collect(forest.latest)
        print(json.dumps({
            "research": "C2-A disk-queue page-bounded GC, NOT production I/O",
            "retained_latest_parity": forest.verify_range(
                forest.latest, 0, 15, writer.anchor),
            "cost": charge.__dict__,
            "read_bytes": charge.read_bytes,
            "write_bytes": charge.write_bytes,
        }, indent=2, sort_keys=True))
    finally:
        if forest is not None:
            forest.close()


if __name__ == "__main__":
    main()
