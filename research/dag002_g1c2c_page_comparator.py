#!/usr/bin/env python3
"""G1-C2-C: honest append-only DAG page-image comparator, not a theorem.

Two frozen reference codecs with identical public virtual page keys, immutable
per-vertex records and an overwritable remote manifest. Application-level
page/address bytes are NOT hardware or authenticated I/O.
"""
from dataclasses import dataclass


def pages_for_bytes(length, page_bytes):
    if type(length) is not int or type(page_bytes) is not int or length < 0 or page_bytes < 8:
        raise ValueError("invalid record length or P<8")
    return (length + page_bytes - 1) // page_bytes


def independent_dfs(graph, ancestor, target):
    todo, seen = [target], set()
    while todo:
        v = todo.pop()
        if v == ancestor:
            return True
        if v not in seen:
            seen.add(v)
            todo.extend(graph[v])
    return False


@dataclass(frozen=True)
class Counters:
    update_reads: int
    update_writes: int
    query_reads: int
    metadata_reads: int
    metadata_writes: int
    address_bytes: int
    parent_bits: int
    label_pages: int
    metadata_pages: int
    max_workspace_bytes: int
    update_read_bytes: int
    update_write_bytes: int
    query_read_bytes: int


class PagedIndex:
    """Bitmap or first-compatible chain-top codec with equally priced keys.

    Immutable records: (label,v,page). Mutable manifest: (manifest,0,page).
    Fixed-width IDs are derived from a frozen horizon. No durability, GC,
    allocator, directory, cache, Merkle proof or device-byte inference.
    """
    def __init__(self, kind, horizon, page_bytes=16, ram_limit=1 << 20):
        if kind not in ("bitmap", "chain"):
            raise ValueError("unknown index kind")
        if type(horizon) is not int or not 1 <= horizon <= 1024:
            raise ValueError("invalid frozen vertex horizon")
        if type(page_bytes) is not int or not 8 <= page_bytes <= 4096:
            raise ValueError("invalid page bytes")
        if type(ram_limit) is not int or ram_limit < 0:
            raise ValueError("invalid RAM cap")
        self.kind, self.horizon, self.P, self.ram_limit = kind, horizon, page_bytes, ram_limit
        self.w = max(1, ((horizon - 1).bit_length() + 7) // 8)
        self.pages = {}
        self.parents = []  # Only for independently replayable traces; never query path.
        self.up_reads = self.up_writes = self.q_reads = 0
        self.meta_reads = self.meta_writes = self.addr_bytes = self.parent_bits = 0
        self.max_workspace = 0
        self._write_blob(("manifest", 0), self._manifest_bytes(0, ()), "init")

    def _ensure_workspace(self, required):
        if required > self.ram_limit:
            raise MemoryError(f"working set {required} exceeds cap {self.ram_limit}")
        self.max_workspace = max(self.max_workspace, required)

    def _addr(self):
        self.addr_bytes += 1 + 2 * self.w

    def _read_page(self, base, k, role):
        self._addr()
        item = self.pages[(base[0], base[1], k)]
        if role == "update":
            self.up_reads += 1
        elif role == "query":
            self.q_reads += 1
        elif role == "metadata":
            self.meta_reads += 1
        else:
            raise AssertionError("bad read role")
        return item

    def _write_blob(self, base, raw, role):
        for k in range(pages_for_bytes(len(raw), self.P)):
            self._addr()
            chunk = raw[k * self.P:(k + 1) * self.P].ljust(self.P, b'\0')
            self.pages[(base[0], base[1], k)] = chunk
            if role == "label":
                self.up_writes += 1
            elif role in ("metadata", "init"):
                if role == "metadata":
                    self.meta_writes += 1
            else:
                raise AssertionError("bad write role")

    def _uint(self, x):
        if not 0 <= x < 1 << (8 * self.w):
            raise ValueError("out of horizon")
        return x.to_bytes(self.w, 'little')

    def _manifest_bytes(self, count, heads):
        if self.kind == "bitmap":
            return count.to_bytes(4, 'little')
        return (count.to_bytes(4, 'little') + len(heads).to_bytes(4, 'little') +
                b''.join(self._uint(x) for x in heads))

    def _read_manifest(self):
        first = self._read_page(("manifest", 0), 0, "metadata")
        n = int.from_bytes(first[:4], 'little')
        if self.kind == "bitmap":
            return n, ()
        chains = int.from_bytes(first[4:8], 'little')
        count = pages_for_bytes(8 + chains * self.w, self.P)
        raw = first + b''.join(self._read_page(("manifest", 0), k, "metadata")
                               for k in range(1, count))
        heads = tuple(int.from_bytes(raw[8 + j*self.w:8 + (j+1)*self.w], 'little')
                      for j in range(chains))
        self._ensure_workspace(len(raw) + self.P)
        return n, heads

    def _read_chain_record(self, vertex, role):
        first = self._read_page(("label", vertex), 0, role)
        count = int.from_bytes(first[:4], 'little')
        length = 4 + self.w + 2*self.w*count
        raw = first + b''.join(self._read_page(("label", vertex), k, role)
                               for k in range(1, pages_for_bytes(length, self.P)))
        self._ensure_workspace(len(raw) + self.P)
        chain = int.from_bytes(raw[4:4+self.w], 'little')
        tops = {}
        pos = 4 + self.w
        for _ in range(count):
            ch = int.from_bytes(raw[pos:pos+self.w], 'little')
            top = int.from_bytes(raw[pos+self.w:pos+2*self.w], 'little')
            if ch in tops:
                raise ValueError("noncanonical duplicate chain")
            tops[ch] = top
            pos += 2*self.w
        return chain, tops

    def _encode_chain(self, chain, tops):
        ordered = sorted(tops.items())
        return (len(ordered).to_bytes(4, 'little') + self._uint(chain) +
                b''.join(self._uint(ch) + self._uint(top) for ch, top in ordered))

    def append(self, parents=()):
        v = len(self.parents)
        if v >= self.horizon:
            raise ValueError("frozen horizon exhausted")
        selected = tuple(parents)
        if any(type(p) is not int or p < 0 or p >= v for p in selected):
            raise ValueError("parent must be an older vertex")
        if len(set(selected)) != len(selected):
            raise ValueError("duplicate parent")
        n, heads = self._read_manifest()
        if n != v:
            raise AssertionError("unexpected manifest epoch")
        if self.kind == "bitmap":
            self._ensure_workspace(2*self.P)
            output = []
            for k in range(pages_for_bytes((v+7)//8, self.P)):
                val = 0
                for p in selected:
                    if k < pages_for_bytes((p+7)//8, self.P):
                        val |= int.from_bytes(self._read_page(("label", p), k, "update"), 'little')
                    if p // (8*self.P) == k:
                        val |= 1 << (p % (8*self.P))
                output.append(val.to_bytes(self.P, 'little'))
            data = b''.join(output)
            next_heads = ()
        else:
            tops = {}
            max_parent_bytes = 0
            for p in selected:
                _, prior = self._read_chain_record(p, "update")
                max_parent_bytes = max(max_parent_bytes, 4+self.w+2*self.w*len(prior))
                for chain, top in prior.items():
                    tops[chain] = max(top, tops.get(chain, -1))
            chosen = next((i for i, head in enumerate(heads) if tops.get(i) == head), None)
            next_heads = list(heads)
            if chosen is None:
                chosen = len(heads)
                next_heads.append(v)
            else:
                next_heads[chosen] = v
            tops[chosen] = v
            data = self._encode_chain(chosen, tops)
            self._ensure_workspace(max(len(data), max_parent_bytes) +
                                   3*self.P + 2*self.w*len(next_heads))
            next_heads = tuple(next_heads)
        self._ensure_workspace(max(self.P, len(data)+2*self.P if self.kind == "bitmap"
                                   else len(data)+self.P))
        self._write_blob(("label", v), data, "label")
        self._write_blob(("manifest", 0), self._manifest_bytes(v+1, next_heads), "metadata")
        self.parent_bits += v
        self.parents.append(tuple(sorted(selected)))
        return v

    def query(self, ancestor, target):
        n = len(self.parents)
        if (type(ancestor) is not int or type(target) is not int or
                not (0 <= ancestor < n and 0 <= target < n)):
            raise ValueError("invalid query IDs")
        if ancestor == target:
            return True
        if ancestor > target:
            return False
        if self.kind == "bitmap":
            self._ensure_workspace(self.P)
            k = ancestor // (8*self.P)
            image = self._read_page(("label", target), k, "query")
            return bool(image[(ancestor//8) % self.P] & (1 << (ancestor % 8)))
        source = self._read_page(("label", ancestor), 0, "query")
        chain = int.from_bytes(source[4:4+self.w], 'little')
        _, tops = self._read_chain_record(target, "query")
        return ancestor <= tops.get(chain, -1)

    def counters(self):
        labels = sum(1 for key in self.pages if key[0] == "label")
        metadata = sum(1 for key in self.pages if key[0] == "manifest")
        return Counters(self.up_reads, self.up_writes, self.q_reads,
                        self.meta_reads, self.meta_writes, self.addr_bytes,
                        self.parent_bits, labels, metadata, self.max_workspace,
                        self.up_reads*self.P, self.up_writes*self.P,
                        self.q_reads*self.P)


def run_family(kind, graph, page_bytes=16, ram_limit=1<<20, query_pairs=()):
    idx = PagedIndex(kind, len(graph), page_bytes, ram_limit)
    for parents in graph:
        idx.append(parents)
    for u, v in query_pairs:
        assert idx.query(u, v) == independent_dfs(graph, u, v)
    return idx.counters()


def report():
    for family in (tuple(() for _ in range(24)),
                   ((),) + tuple((i-1,) for i in range(1,24)),
                   tuple(tuple(range(i)) for i in range(24))):
        for codec in ('bitmap', 'chain'):
            c = run_family(codec, family, 16,
                           query_pairs=((0,23), (5,19), (22,23)))
            print(codec, 'n=24', 'label_pages=', c.label_pages,
                  'manifest_rw=', c.metadata_reads+c.metadata_writes,
                  'query_pages=', c.query_reads)
    print('DAG_G1C2C_TYPED_PAGE_COMPARISON_PASS')
    print('NOVELTY_UNPROVED_CLASSICAL_INDEX_COMPARISON')


if __name__ == '__main__':
    report()
