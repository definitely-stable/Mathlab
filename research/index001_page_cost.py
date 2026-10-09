"""INDEX-001 G2-A deterministic *simulated* cold-page metadata comparators.

No real files, WAL durability, OS page cache, fsync, payload GC or device timings.
The model deliberately overcharges one full-page append write per range record.
"""
from dataclasses import dataclass

from index001_oracle import ExactRangeMap, PhysicalWriteLedger


def pages_for_records(records: int, records_per_page: int) -> int:
    if records < 0 or records_per_page <= 0:
        raise ValueError("invalid record/page count")
    return (records + records_per_page - 1) // records_per_page


@dataclass
class ComparatorCounters:
    read_pages: int = 0
    metadata_probes: int = 0
    compact_read_pages: int = 0
    compactions: int = 0
    logical_blocks_assigned: int = 0


class DirectArrayComparator:
    """Each assigned cell is materialized; each touched page is rewritten."""
    def __init__(self, size: int, blocks_per_page: int, initial=0):
        if not (isinstance(size, int) and size >= 1 and
                isinstance(blocks_per_page, int) and blocks_per_page >= 1):
            raise ValueError("invalid direct-array dimensions")
        self.size = size
        self.blocks_per_page = blocks_per_page
        self.cells = [initial] * size
        self.page_reads = 0
        self.page_writes = 0

    def _check(self, lo, hi):
        if not (isinstance(lo, int) and isinstance(hi, int)
                and 0 <= lo <= hi <= self.size):
            raise ValueError("outside block universe")

    def assign(self, lo, hi, value):
        self._check(lo, hi)
        for i in range(lo, hi):
            self.cells[i] = value
        if hi > lo:
            self.page_writes += (hi - 1) // self.blocks_per_page - lo // self.blocks_per_page + 1

    def lookup(self, pos):
        self._check(pos, pos + 1)
        self.page_reads += 1
        return self.cells[pos]

    def scan(self, lo, hi):
        self._check(lo, hi)
        if lo == hi:
            return ()
        self.page_reads += (hi - 1) // self.blocks_per_page - lo // self.blocks_per_page + 1
        result = []
        at = lo
        for pos in range(lo + 1, hi + 1):
            if pos == hi or self.cells[pos] != self.cells[at]:
                result.append((at, pos, self.cells[at]))
                at = pos
        return tuple(result)


class OverlayPageComparator:
    """Range log + canonical base with exact semantics and synthetic cost."""
    def __init__(self, size: int, page_bytes: int = 4096,
                 record_bytes: int = 32, max_pending: int = 8, initial=0):
        if not (isinstance(page_bytes, int) and
                isinstance(record_bytes, int) and 0 < record_bytes <= page_bytes and
                page_bytes % record_bytes == 0):
            raise ValueError("record must evenly divide metadata page")
        if not isinstance(max_pending, int) or max_pending <= 0:
            raise ValueError("max_pending must be positive")
        self.base = ExactRangeMap(size, initial)
        self.size = size
        self.page_bytes = page_bytes
        self.records_per_page = page_bytes // record_bytes
        self.max_pending = max_pending
        self.pending = []
        self.counters = ComparatorCounters()
        self.writes = PhysicalWriteLedger()

    @property
    def metadata_page_footprint(self):
        return (pages_for_records(len(self.base.runs), self.records_per_page) +
                pages_for_records(len(self.pending), self.records_per_page))

    def assign(self, lo, hi, value):
        self.base._range_ok(lo, hi)
        if lo == hi:
            return
        self.counters.logical_blocks_assigned += hi - lo
        self.pending.append((lo, hi, value))
        # Conservative one-page append journal: NOT an observed disk write.
        self.writes.add("wal", self.page_bytes)
        if len(self.pending) >= self.max_pending:
            self.compact()

    def lookup(self, pos):
        self.base._range_ok(pos, pos + 1)
        pages = set()
        for i in range(len(self.pending) - 1, -1, -1):
            self.counters.metadata_probes += 1
            pages.add(("log", i // self.records_per_page))
            lo, hi, value = self.pending[i]
            if lo <= pos < hi:
                self.counters.read_pages += len(pages)
                return value
        for i, (lo, hi, value) in enumerate(self.base.runs):
            self.counters.metadata_probes += 1
            pages.add(("base", i // self.records_per_page))
            if lo <= pos < hi:
                self.counters.read_pages += len(pages)
                return value
        raise AssertionError("complete base has a run covering every point")

    def _materialize(self):
        tmp = ExactRangeMap(self.size)
        tmp.runs = tuple(self.base.runs)
        for lo, hi, v in self.pending:
            tmp.assign(lo, hi, v)
        return tmp

    def scan(self, lo, hi):
        self.base._range_ok(lo, hi)
        if lo == hi:
            return ()
        # Conservative cold full metadata scan, whether or not a range is narrow.
        self.counters.metadata_probes += len(self.base.runs) + len(self.pending)
        self.counters.read_pages += self.metadata_page_footprint
        return self._materialize().scan(lo, hi)

    def compact(self):
        if not self.pending:
            return
        read = self.metadata_page_footprint
        self.counters.compact_read_pages += read
        self.counters.read_pages += read
        self.counters.metadata_probes += len(self.base.runs) + len(self.pending)
        updated = self._materialize()
        out_pages = pages_for_records(len(updated.runs), self.records_per_page)
        self.writes.add("compaction", out_pages * self.page_bytes)
        self.counters.compactions += 1
        self.base = updated
        self.pending.clear()

    @property
    def total_metadata_written_bytes(self):
        return self.writes.total_physical_write_bytes

    @property
    def metadata_cold_read_bytes(self):
        return self.counters.read_pages * self.page_bytes
