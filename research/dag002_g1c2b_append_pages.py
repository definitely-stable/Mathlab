#!/usr/bin/env python3
"""G1-C2-B: append-only DAG transitive-closure page reference.

Exact application-level full-page transfer accounting, no durability, allocator,
cryptographic freshness, OS/NAND I/O or source-codebook-space lower bound.
"""
from dataclasses import dataclass


def pages_for(bits, page_bytes):
    if (type(bits) is not int or bits < 0 or type(page_bytes) is not int
            or page_bytes < 1):
        raise ValueError('nonnegative bits and positive page bytes required')
    return (bits + 8 * page_bytes - 1) // (8 * page_bytes)


@dataclass(frozen=True)
class Ledger:
    vertices: int
    input_parent_bits: int
    update_read_pages: int
    update_write_pages: int
    query_read_pages: int
    update_read_bytes: int
    update_write_bytes: int
    query_read_bytes: int
    new_label_one_bits: int


class PagedAppendClosure:
    """Immutable per-vertex closure pages in a public, virtual (v,page) namespace.

    Parent payload is a *charged* v-bit incidence vector at append(v). Pages
    are allocated in an ideal key-addressed namespace: real allocator/root,
    namespace metadata and crash/GC costs are OUTSIDE the scoped model.
    Each stored page is fully transferred even when mostly zero-filled.
    """
    def __init__(self, page_bytes=1):
        if type(page_bytes) is not int or page_bytes < 1 or page_bytes > 4096:
            raise ValueError('invalid page bytes')
        self.page_bytes = page_bytes
        self.parents = []
        self.pages = {}
        self.input_parent_bits = 0
        self.update_read_pages = 0
        self.update_write_pages = 0
        self.query_read_pages = 0
        self.new_label_one_bits = 0

    def _page(self, vertex, page_index):
        raw = self.pages[(vertex, page_index)]
        if type(raw) is not bytes or len(raw) != self.page_bytes:
            raise ValueError('invalid stored page image')
        return raw

    def append(self, parents=()):
        vertex = len(self.parents)
        selected = tuple(parents)
        if any(type(p) is not int or not 0 <= p < vertex for p in selected):
            raise ValueError('parent must be an already published vertex')
        if len(set(selected)) != len(selected):
            raise ValueError('duplicate parents')
        mask = 0
        for p in selected:
            mask |= 1 << p
            for k in range(pages_for(p, self.page_bytes)):
                raw = self._page(p, k)
                self.update_read_pages += 1
                mask |= int.from_bytes(raw, 'little') << (8 * self.page_bytes * k)
        self.input_parent_bits += vertex
        page_limit = pages_for(vertex, self.page_bytes)
        for k in range(page_limit):
            portion = (mask >> (8 * self.page_bytes * k)) & ((1 << (8 * self.page_bytes)) - 1)
            self.pages[(vertex, k)] = portion.to_bytes(self.page_bytes, 'little')
            self.update_write_pages += 1
        self.new_label_one_bits += mask.bit_count()
        self.parents.append(tuple(sorted(selected)))
        return vertex

    def query(self, ancestor, target):
        total = len(self.parents)
        if (type(ancestor) is not int or type(target) is not int
                or not 0 <= ancestor < total or not 0 <= target < total):
            raise ValueError('invalid query vertex')
        if ancestor == target:
            return True  # Reflexive path has zero length.
        if ancestor > target:
            return False  # Every append edge goes from old to new.
        page_index = ancestor // (8 * self.page_bytes)
        image = self._page(target, page_index)
        self.query_read_pages += 1
        return bool(image[(ancestor // 8) % self.page_bytes] & (1 << (ancestor % 8)))

    def ledger(self):
        P = self.page_bytes
        return Ledger(len(self.parents), self.input_parent_bits,
                      self.update_read_pages, self.update_write_pages,
                      self.query_read_pages, self.update_read_pages * P,
                      self.update_write_pages * P, self.query_read_pages * P,
                      self.new_label_one_bits)

    def snapshot(self):
        return dict(self.pages)


def reachable_from_adjacency(parents, source, sink):
    """Independent path search; does NOT consult transitive closure pages."""
    todo = [sink]
    seen = set()
    while todo:
        v = todo.pop()
        if v == source:
            return True
        if v not in seen:
            seen.add(v)
            todo.extend(parents[v])
    return False


def path_parity(parents, source, sink):
    """Parity of directed walks, NOT Boolean reachability (diamond killer)."""
    if source > sink:
        return 0
    count = [0] * (sink + 1)
    for v in range(source, sink + 1):
        count[v] = int(v == source) ^ (0 if v == source else
                                     (sum(count[p] for p in parents[v]) & 1))
    return count[sink]


def direct_parent_bit(parents, ancestor, target):
    """Incorrect as a transitive reachability query beyond an antichain."""
    return ancestor == target or ancestor in parents[target]


def report():
    store = PagedAppendClosure(1)
    for pr in ((), (0,), (0,), (1, 2)):
        store.append(pr)
    assert store.query(0, 3)
    assert path_parity(store.parents, 0, 3) == 0
    assert not direct_parent_bit(store.parents, 0, 3)
    assert store.ledger().update_write_pages == 3
    print('DAG_G1C2B_ALL_SOURCE_MODELS_DISTINCT_PASS')
    print('DAG_G1C2B_DIAMOND_BOOLEAN_VS_GF2_PASS')
    print('DAG_G1C2B_PAGE_TRANSFER_REFERENCE_PASS')
    print('NOVELTY_UNPROVED_APPEND_ONLY_BASELINE')


if __name__ == '__main__':
    report()
