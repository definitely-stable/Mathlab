#!/usr/bin/env python3
"""UCT-005 G3-B2-C0: explicit, restricted 4KiB page-image and LRU oracle.

This is a mathematical *layout simulator* atop G3-B2-B logical references,
NOT real disk measurements, crash-safe file I/O, or a new asymptotic bound.
All page images (including underfull images) charge a whole page.
"""
from collections import OrderedDict
from dataclasses import dataclass
from math import ceil

from uct005_g3b2b_range_tree import Reader, TreeWriter, checked_query
from uct005_g3b2b_baselines import ReplicaWriter, SnapshotWriter


def _ceildiv(n, d):
    if type(n) is not int or n < 0 or type(d) is not int or d <= 0:
        raise ValueError("nonnegative numerator and positive divisor required")
    return (n + d - 1) // d


@dataclass(frozen=True)
class FrozenPages:
    page_bytes: int = 4096
    header_bytes: int = 64
    tree_record_bytes: int = 160
    root_directory_bytes: int = 48
    log_record_bytes: int = 13
    ram_pages: int = 1

    def __post_init__(self):
        fields = (self.page_bytes, self.header_bytes,
                  self.tree_record_bytes, self.root_directory_bytes,
                  self.log_record_bytes, self.ram_pages)
        if any(type(v) is not int for v in fields):
            raise ValueError("integer layout required")
        if (self.page_bytes < 128 or self.header_bytes < 0
                or self.tree_record_bytes < 1 or self.root_directory_bytes < 1
                or self.log_record_bytes < 1 or self.ram_pages < 0
                or max(self.tree_record_bytes, self.root_directory_bytes,
                       self.log_record_bytes) > self.payload_bytes):
            raise ValueError("invalid immutable page layout")

    @property
    def payload_bytes(self):
        return self.page_bytes - self.header_bytes

    @property
    def slots(self):
        return self.payload_bytes // self.tree_record_bytes


class ColdLRU:
    """Bounded per-operation server cache; cold at every independent operation.

    Capacity 0 causes a fault on each access, including a repeat within a page.
    No hidden RAM reuse across operations. Each fault reads the WHOLE page.
    """
    def __init__(self, capacity):
        if type(capacity) is not int or capacity < 0:
            raise ValueError("negative cache")
        self.capacity = capacity
        self.cache = OrderedDict()
        self.faults = 0
        self.accesses = []

    def touch(self, page):
        if type(page) is not int or page < 0:
            raise ValueError("invalid page address")
        self.accesses.append(page)
        if page in self.cache:
            self.cache.move_to_end(page)
            return
        self.faults += 1
        if self.capacity:
            self.cache[page] = None
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


def _all_nodes(root):
    yield root
    if root.left is not None:
        yield from _all_nodes(root.left)
        yield from _all_nodes(root.right)


def _path_nodes(root, n, index):
    lo, hi = 0, n - 1
    cur = root
    while True:
        yield cur
        if lo == hi:
            return
        mid = (lo + hi) // 2
        if index <= mid:
            cur = cur.left
            hi = mid
        else:
            cur = cur.right
            lo = mid + 1


def _frontier_nodes(root, lo, hi, left, right):
    yield root
    terminal = (right < lo or hi < left) or (left <= lo and hi <= right)
    if not terminal:
        mid = (lo + hi) // 2
        yield from _frontier_nodes(root.left, lo, mid, left, right)
        yield from _frontier_nodes(root.right, mid + 1, hi, left, right)


@dataclass(frozen=True)
class PhysicalTrace:
    protocol: str
    operation: str
    logical_node_reads: int
    logical_node_writes: int
    remote_page_reads: int
    remote_page_writes: int
    remote_read_bytes: int
    remote_write_bytes: int
    remote_response_bytes: int
    untrusted_request_bytes: int
    verifier_sha_calls: int
    verifier_xor_ops: int
    author_sha_calls: int
    anchor_request_bytes: int
    anchor_response_bytes: int
    anchor_publication_bytes: int
    trusted_checkpoint_bytes: int
    retained_remote_pages: int
    server_cache_bytes_cap: int


class TreePageLedger:
    """Concrete immutable node records, append-only COW pages + epoch directory.

    Each record is fixed-width and packs a node commitment, parity, length,
    two child pointers and child digests into 160 bytes. Pointer offsets and
    verification CPU beyond B2-B are outside this abstract page-image model.
    Initial nodes are preorder-packed; each SET's new root-to-leaf nodes are
    packed in *fresh* pages and followed by a fresh root-directory page.
    Every epoch is retained; no compaction/GC, no dedup, no hidden free pages.
    """
    def __init__(self, bits, layout=FrozenPages()):
        self.layout = layout
        self.writer = TreeWriter(bits)
        self.addresses = {}
        self.next_page = 0
        initial = tuple(_all_nodes(self.writer.roots[0]))
        for offset, node in enumerate(initial):
            self.addresses[id(node)] = offset // layout.slots
        self.next_page = _ceildiv(len(initial), layout.slots)
        self.setup_data_pages = self.next_page
        self.epoch_directory = [self._new_page()]
        self.setup_write_pages = self.setup_data_pages + 1

    def _new_page(self):
        page = self.next_page
        self.next_page += 1
        return page

    def update(self, index, bit):
        old = self.writer.roots[-1]
        old_nodes = tuple(_path_nodes(old, self.writer.n, index))
        cache = ColdLRU(self.layout.ram_pages)
        cache.touch(self.epoch_directory[-1])
        for node in old_nodes:
            cache.touch(self.addresses[id(node)])
        logical = self.writer.set(index, bit)
        new_nodes = tuple(_path_nodes(self.writer.roots[-1],
                                      self.writer.n, index))
        if logical.remote_node_reads != len(old_nodes):
            raise AssertionError("G3-B2-B update-read seam changed")
        if logical.remote_node_writes != len(new_nodes):
            raise AssertionError("G3-B2-B update-write seam changed")
        new_data_pages = _ceildiv(len(new_nodes), self.layout.slots)
        first_new_page = self.next_page
        for i, node in enumerate(new_nodes):
            if id(node) in self.addresses:
                raise AssertionError("persistent COW node must be new")
            self.addresses[id(node)] = first_new_page + i // self.layout.slots
        self.next_page += new_data_pages
        self.epoch_directory.append(self._new_page())
        writes = new_data_pages + 1
        return self._trace("SET", len(old_nodes), len(new_nodes),
                           cache.faults, writes, 0, 0, 0, 0,
                           logical.hash_calls, 0, 0, 40)

    def query(self, epoch, left, right):
        if type(epoch) is not int or not 0 <= epoch < len(self.writer.roots):
            raise ValueError("invalid epoch")
        response, expected_nodes = self.writer.serve(epoch, left, right)
        root = self.writer.roots[epoch]
        nodes = tuple(_frontier_nodes(root, 0, self.writer.n - 1,
                                      left, right))
        if len(nodes) != expected_nodes:
            raise AssertionError("G3-B2-B query-read seam changed")
        cache = ColdLRU(self.layout.ram_pages)
        cache.touch(self.epoch_directory[epoch])
        for node in nodes:
            cache.touch(self.addresses[id(node)])
        verifier = checked_query(
            Reader(self.writer.epochs[0]), self.writer.n, left, right,
            response, len(nodes), self.writer.anchor)
        # A historical epoch may be rejected by current anchor. The physical
        # response nevertheless consumed pages and transfer bytes.
        return self._trace("RANGE_PARITY", len(nodes), 0,
                           cache.faults, 0, len(response),
                           verifier.cost.untrusted_request_bytes,
                           verifier.cost.verifier_hash_calls,
                           verifier.cost.verifier_xor_ops, 0, 1, 40, 0)

    def _trace(self, name, reads, writes, page_reads, page_writes, wire,
               request, hashes, xors, author_hashes, anchor_req, anchor_resp, anchor_pub):
        p = self.layout.page_bytes
        return PhysicalTrace(
            "T", name, reads, writes,
            page_reads, page_writes, page_reads * p, page_writes * p,
            wire, request, hashes, xors, author_hashes, anchor_req, anchor_resp,
            anchor_pub, 40, self.next_page, self.layout.ram_pages * p)


def snapshot_page_cost(n, layout=FrozenPages()):
    """Cold full immutable bitmap COW: full snapshot every committed SET.

    Hash input in current B2-B Python implementation is n BYTES, not n/8.
    Physical serialized bitmap is bit-packed; these are different resources.
    One root-directory page is allocated per epoch. No shared-page overwrite.
    """
    if type(n) is not int or n < 1 or n >= 2**32:
        raise ValueError("invalid n")
    data_pages = _ceildiv(_ceildiv(n, 8), layout.payload_bytes)
    return {
        "protocol": "S",
        "initial_data_pages": data_pages,
        "update_remote_page_reads": data_pages + 1,
        "update_remote_page_writes": data_pages + 1,
        "query_remote_page_reads": data_pages + 1,
        "sha_input_bytes_per_set": n,
        "trusted_checkpoint_bytes": 40,
        "anchor_publication_bytes": 40,
        "anchor_request_bytes": 1,
        "anchor_response_bytes": 40,
        "note": "cold full immutable bitmap COW plus new root-directory page",
    }


def replica_log_page_cost(n, missed, layout=FrozenPages()):
    """Intentionally conservative append-only one-entry-per-page log.

    Each SET gets one durable log page AND a separate epoch-directory page;
    no implicit in-place modification of already-published pages. Rejoining
    client must read every missed record. It stores n trusted bits plus root.
    No crash-atomic client disk protocol is asserted.
    """
    if type(n) is not int or n < 1 or n >= 2**32:
        raise ValueError("invalid n")
    if type(missed) is not int or missed < 0:
        raise ValueError("invalid missing-update count")
    return {
        "protocol": "R",
        "log_record_bytes": layout.log_record_bytes,
        "update_remote_page_writes": 2,
        "query_remote_page_reads": missed + int(missed > 0),
        "trusted_checkpoint_bytes": 40 + _ceildiv(n, 8),
        "local_update_digest_calls": missed,
        "anchor_publication_bytes": 40,
        "anchor_request_bytes": 1,
        "anchor_response_bytes": 40,
        "note": "one page per log entry; read all missed entries, paid n-bit replica",
    }


@dataclass(frozen=True)
class CrashCut:
    steps_completed: int
    new_anchor_visible: bool
    data_durable: bool
    directory_durable: bool
    safe: bool
    orphaned_new_data: bool


# An ideal storage contract: full-page atomicity and FLUSH as persistence
# barriers. A real filesystem/SSD does not automatically provide this model.
ORDERED_COMMIT = (
    "WRITE_DATA", "FLUSH_DATA", "WRITE_DIRECTORY",
    "FLUSH_DIRECTORY", "PUBLISH_ANCHOR", "ACK_COMMIT",
)


def crash_cuts(order=ORDERED_COMMIT):
    """Enumerate every crash prefix, detecting unsafe visibility order."""
    allowed = set(ORDERED_COMMIT)
    if len(order) != len(ORDERED_COMMIT) or set(order) != allowed:
        raise ValueError("exact commit event permutation required")
    results = []
    for prefix in range(len(order) + 1):
        seen = set(order[:prefix])
        data = ("FLUSH_DATA" in seen and "WRITE_DATA" in seen
                and order.index("WRITE_DATA") < order.index("FLUSH_DATA"))
        directory = ("FLUSH_DIRECTORY" in seen
                     and "WRITE_DIRECTORY" in seen
                     and order.index("WRITE_DIRECTORY") < order.index("FLUSH_DIRECTORY"))
        visible = "PUBLISH_ANCHOR" in seen
        results.append(CrashCut(
            prefix, visible, data, directory,
            not visible or (data and directory),
            ("WRITE_DATA" in seen and not visible),
        ))
    return tuple(results)


def novelty_falsifiers(n=256, layout=FrozenPages()):
    """Explicit countermodels, NOT proof of a new UCT lower bound."""
    if type(n) is not int or n < 2:
        raise ValueError("n >= 2")
    tree = TreePageLedger((0,) * n, layout)
    update = tree.update(0, 1)
    full_range = tree.query(1, 0, n - 1)
    return {
        "n": n,
        "slots": layout.slots,
        "tree_logical_writes": update.logical_node_writes,
        "tree_physical_page_writes": update.remote_page_writes,
        "full_range_tree_query_page_reads": full_range.remote_page_reads,
        "full_range_tree_query_logical_reads": full_range.logical_node_reads,
        "replica_zero_backlog_page_reads": replica_log_page_cost(n, 0, layout)[
            "query_remote_page_reads"],
        "candidate_page_writes_at_least_logical_writes_rejected":
            update.remote_page_writes < update.logical_node_writes,
        "candidate_every_range_requires_log_pages_rejected":
            full_range.remote_page_reads < update.logical_node_writes,
        "candidate_universal_positive_remote_query_io_rejected":
            replica_log_page_cost(n, 0, layout)["query_remote_page_reads"] == 0,
    }


def main():
    import json
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 256
    print(json.dumps({
        "page_model": "fixed-image COW; no actual disk IO",
        "falsifiers": novelty_falsifiers(n),
        "snapshot": snapshot_page_cost(n),
        "replica_no_backlog": replica_log_page_cost(n, 0),
        "safe_crash_prefixes": all(c.safe for c in crash_cuts()),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
