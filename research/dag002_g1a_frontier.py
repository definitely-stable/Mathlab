#!/usr/bin/env python3
"""DAG-002×ALG-001 G1-A: exact *one-shot* remote-cell/bit accounting.

Immutable prefix and input-independent baseline. Covers elementary Hamming
injection and a STRICTLY RESTRICTED coordinate-addressed XOR-delta coding
family (classical covering codes). No generic cell-probe novelty claimed.
"""
from dataclasses import dataclass
from itertools import combinations
from math import comb

from dag002_oracle import min_fixed_bits_for_states


def remote_state_volume(cells, cell_bits, net_changed):
    """Number of c-bit N-cell states differing from fixed baseline in <=W cells."""
    if any(not isinstance(x, int) or isinstance(x, bool)
           for x in (cells, cell_bits, net_changed)):
        raise ValueError("integer parameters required")
    if cells < 0 or cell_bits < 1 or net_changed < 0 or net_changed > cells:
        raise ValueError("invalid remote state configuration")
    alternatives = (1 << cell_bits) - 1
    return sum(comb(cells, j) * alternatives ** j
               for j in range(net_changed + 1))


def necessary_local_bits(distinct_outputs, cells, cell_bits, net_changed):
    """Universal *necessary* bit count for fixed snapshot, any decoder/P."""
    if (not isinstance(distinct_outputs, int) or isinstance(distinct_outputs, bool)
            or distinct_outputs < 1):
        raise ValueError("distinct_outputs must be >= 1")
    volume = remote_state_volume(cells, cell_bits, net_changed)
    local_variants = (distinct_outputs + volume - 1) // volume
    return min_fixed_bits_for_states(local_variants)


def hamming_ball(center, dimension, radius):
    if (not isinstance(dimension, int) or not isinstance(center, int)
            or not isinstance(radius, int) or dimension < 0
            or radius < 0 or radius > dimension or
            not 0 <= center < (1 << dimension)):
        raise ValueError("bad binary Hamming ball")
    return frozenset(x for x in range(1 << dimension)
                     if (x ^ center).bit_count() <= radius)


def covering_radius(centers, dimension):
    if not centers:
        raise ValueError("at least one center required")
    if any(not isinstance(c, int) or c < 0 or c >= (1 << dimension)
           for c in centers):
        raise ValueError("center out of range")
    return max(min((v ^ c).bit_count() for c in centers)
               for v in range(1 << dimension))


def minimum_covering_centers(dimension, radius):
    """Brute exact set-cover search for n<=4, no precomputed K(n,R) table."""
    if (not isinstance(dimension, int) or isinstance(dimension, bool)
            or dimension < 0 or dimension > 4 or not isinstance(radius, int)
            or radius < 0 or radius > dimension):
        raise ValueError("exhaustive oracle restricted to n<=4")
    universe = 1 << dimension
    balls = [sum(1 << x for x in hamming_ball(c, dimension, radius))
             for c in range(universe)]
    all_values = (1 << universe) - 1
    for k in range(1, universe + 1):
        for code in combinations(range(universe), k):
            joined = 0
            for center in code:
                joined |= balls[center]
            if joined == all_values:
                return code
    raise AssertionError("singletons always cover")


@dataclass(frozen=True)
class SparseRemoteRecord:
    center_id: int
    remote_delta: int
    net_changed_cells: int


class CoordinateXorDeltaScheme:
    """Label chooses one public center; P=1 reads public remote cell i."""
    def __init__(self, dimension, max_changed, centers):
        if (not isinstance(dimension, int) or dimension < 0
                or not isinstance(max_changed, int) or
                max_changed < 0 or max_changed > dimension):
            raise ValueError("invalid n, W")
        self.dimension = dimension
        self.max_changed = max_changed
        self.centers = tuple(centers)
        if covering_radius(self.centers, dimension) > max_changed:
            raise ValueError("centers do not cover target state family")
        self.label_bits = min_fixed_bits_for_states(len(self.centers))

    def encode(self, mask):
        if not isinstance(mask, int) or not 0 <= mask < (1 << self.dimension):
            raise ValueError("mask out of range")
        for index, center in enumerate(self.centers):
            delta = mask ^ center
            if delta.bit_count() <= self.max_changed:
                return SparseRemoteRecord(index, delta, delta.bit_count())
        raise AssertionError("inconsistent covering radius")

    def query(self, record, position):
        if not isinstance(position, int) or not 0 <= position < self.dimension:
            raise ValueError("query index out of range")
        if not 0 <= record.center_id < len(self.centers):
            raise ValueError("unknown center")
        # Exactly one remote bit probe at public address 'position'.
        remote_bit = (record.remote_delta >> position) & 1
        local_center_bit = (self.centers[record.center_id] >> position) & 1
        return local_center_bit ^ remote_bit

    def transition_changed_cells(self, first, second):
        """Actual final-state changes between records, not a W guarantee."""
        return (first.remote_delta ^ second.remote_delta).bit_count()


def independent_source_probe(mask, coordinate, dimension):
    """Out-of-model source graph bit-array: one probe, B+G=0."""
    if not 0 <= mask < (1 << dimension) or not 0 <= coordinate < dimension:
        raise ValueError("invalid query")
    source_bits = tuple((mask >> i) & 1 for i in range(dimension))
    return source_bits[coordinate]


def broadcast_changed_cell(bit_value, dimension):
    """Arbitrary decoder: all queries probe SAME cell. Refutes Hamming transfer."""
    if bit_value not in (0, 1) or dimension < 1:
        raise ValueError("invalid input")
    return tuple(bit_value for _ in range(dimension))
