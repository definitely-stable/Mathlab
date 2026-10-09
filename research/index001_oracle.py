"""INDEX-001 G1: exact logical run map, not a disk index or physical-cost model.

Runs are canonical maximal constant half-open ranges covering [0, size).
This is intentionally independent from the dense-array oracle in tests.
"""
from dataclasses import dataclass
from math import comb


def count_maps_with_k_runs(size: int, alphabet_size: int, runs: int) -> int:
    """Number of complete maps with exactly runs maximal constant intervals."""
    if not (size >= 1 and alphabet_size >= 2 and 1 <= runs <= size):
        raise ValueError("invalid size, alphabet or number of runs")
    return alphabet_size * (alphabet_size - 1) ** (runs - 1) * comb(size - 1, runs - 1)


def complete_encoding_lower_bits(size: int, alphabet_size: int, runs: int) -> int:
    """Information floor for a complete *standalone* encoding, NOT index RAM."""
    return (count_maps_with_k_runs(size, alphabet_size, runs) - 1).bit_length()


def canonicalize(segments):
    """Merge touching equal-valued intervals; reject gaps and overlaps."""
    result = []
    for lo, hi, value in segments:
        if not isinstance(lo, int) or not isinstance(hi, int) or lo < 0 or lo >= hi:
            raise ValueError("invalid segment")
        if result:
            last_lo, last_hi, last_val = result[-1]
            if lo != last_hi:
                raise ValueError("segments contain a gap or overlap")
            if last_val == value:
                result[-1] = (last_lo, hi, value)
                continue
        result.append((lo, hi, value))
    return tuple(result)


@dataclass(frozen=True)
class LogicalDelta:
    """Logical boundary edits, not physical bytes or writes."""
    boundaries_removed: frozenset
    boundaries_added: frozenset

    @property
    def recourse(self):
        return len(self.boundaries_removed) + len(self.boundaries_added)


@dataclass
class PhysicalWriteLedger:
    """Explicitly hypothetical event ledger; G1 makes no durability claims."""
    foreground_bytes: int = 0
    wal_bytes: int = 0
    compaction_bytes: int = 0
    other_bytes: int = 0

    def add(self, category: str, byte_count: int):
        if category not in ("foreground", "wal", "compaction", "other"):
            raise ValueError("unknown disjoint write category")
        if not isinstance(byte_count, int) or byte_count < 0:
            raise ValueError("negative or noninteger byte count")
        key = category + "_bytes"
        setattr(self, key, getattr(self, key) + byte_count)

    @property
    def total_physical_write_bytes(self):
        return (self.foreground_bytes + self.wal_bytes +
                self.compaction_bytes + self.other_bytes)


class ExactRangeMap:
    def __init__(self, size: int, initial_value=0):
        if not isinstance(size, int) or size < 1:
            raise ValueError("size must be positive")
        self.size = size
        self.runs = ((0, size, initial_value),)

    def _range_ok(self, lo: int, hi: int):
        if (not isinstance(lo, int) or not isinstance(hi, int)
                or not 0 <= lo <= hi <= self.size):
            raise ValueError("range must be within [0,size]")

    @property
    def boundaries(self):
        return frozenset(lo for lo, _, _ in self.runs[1:])

    def assign(self, lo: int, hi: int, value) -> LogicalDelta:
        self._range_ok(lo, hi)
        if lo == hi:
            return LogicalDelta(frozenset(), frozenset())
        old = self.boundaries
        pieces = []
        inserted = False
        for start, end, existing in self.runs:
            if end <= lo or start >= hi:
                if not inserted and start >= hi:
                    pieces.append((lo, hi, value))
                    inserted = True
                pieces.append((start, end, existing))
                continue
            if start < lo:
                pieces.append((start, lo, existing))
            if not inserted:
                pieces.append((lo, hi, value))
                inserted = True
            if end > hi:
                pieces.append((hi, end, existing))
        if not inserted:
            pieces.append((lo, hi, value))
        self.runs = canonicalize(pieces)
        assert self.runs[0][0] == 0 and self.runs[-1][1] == self.size
        now = self.boundaries
        return LogicalDelta(old - now, now - old)

    def lookup(self, pos: int):
        if not isinstance(pos, int) or not 0 <= pos < self.size:
            raise ValueError("point outside universe")
        for lo, hi, value in self.runs:
            if lo <= pos < hi:
                return value
        raise AssertionError("canonical map must cover every point")

    def scan(self, lo: int, hi: int):
        """Maximal clipped runs within [lo,hi); [] for empty intervals."""
        self._range_ok(lo, hi)
        if lo == hi:
            return ()
        pieces = []
        for start, end, value in self.runs:
            if end <= lo:
                continue
            if start >= hi:
                break
            pieces.append((max(start, lo), min(end, hi), value))
        return canonicalize(pieces)
