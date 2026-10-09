#!/usr/bin/env python3
"""DAG-002 × ALG-001 G1-B: adaptive cell-probe counting and persistent GF(2) syndrome.

Finite, deterministic, fixed-code observers only. The finite counting lemma
and linear parity constructions are classical. No novelty/performance claim.
"""
from dataclasses import dataclass
from itertools import combinations

from dag002_g1a_frontier import necessary_local_bits, remote_state_volume


def potential_query_addresses(cell_bits, probes):
    """Maximum number of probe nodes in a c-bit branching tree of depth P."""
    if (not isinstance(cell_bits, int) or isinstance(cell_bits, bool)
            or cell_bits < 1 or not isinstance(probes, int)
            or isinstance(probes, bool) or probes < 0):
        raise ValueError("positive cell bits, nonnegative probe count required")
    return sum((1 << (cell_bits * d)) for d in range(probes))


def visible_remote_cells(queries, cells, cell_bits, probes):
    """n query decision trees expose at most n * sum((2**c)**d) cells."""
    if (not isinstance(queries, int) or isinstance(queries, bool)
            or not isinstance(cells, int) or isinstance(cells, bool)
            or queries < 0 or cells < 0):
        raise ValueError("invalid query count or remote cell count")
    return min(cells, queries * potential_query_addresses(cell_bits, probes))


def adaptive_probe_local_bits(distinct_outputs, queries, cells,
                              cell_bits, changed_cells, probes):
    """Necessary, NOT sufficient: conditional exact per-step local state bits.

    Counts at most sum binom(M,j)*(2^c-1)^j reachable remote projections,
    M = min(N, queries*(1+2^c+...+(2^c)^(P-1))). All pre-update state,
    public IDs and immutable historical labels must be FIXED while
    enumerating the distinct successor output vectors.
    """
    visible = visible_remote_cells(queries, cells, cell_bits, probes)
    if (not isinstance(changed_cells, int) or isinstance(changed_cells, bool)
            or changed_cells < 0 or changed_cells > cells):
        raise ValueError("invalid net write budget")
    return necessary_local_bits(distinct_outputs, visible, cell_bits,
                                min(changed_cells, visible))


def evaluate_tree(tree, memory, max_probes):
    """Generic binary adaptive decision tree: int leaf or (address, zero, one)."""
    traversed = 0
    node = tree
    while isinstance(node, tuple):
        if len(node) != 3:
            raise ValueError("malformed probe node")
        address, left, right = node
        if (not isinstance(address, int) or isinstance(address, bool)
                or not 0 <= address < len(memory)):
            raise ValueError("invalid address")
        if traversed >= max_probes:
            raise ValueError("probe budget exceeded")
        traversed += 1
        val = memory[address]
        if val not in (0, 1):
            raise ValueError("binary oracle expects bits")
        node = right if val else left
    if node not in (0, 1):
        raise ValueError("invalid output bit")
    return node, traversed


def all_potential_tree_addresses(tree):
    """Structural oracle: gather union of addresses on all possible paths."""
    if not isinstance(tree, tuple):
        return frozenset()
    address, left, right = tree
    return frozenset((address,)) | all_potential_tree_addresses(left) | all_potential_tree_addresses(right)


def fixed_binary_one_probe_programs(cells):
    """All distinct 0/1 constants or a cell bit, optionally negated."""
    if not isinstance(cells, int) or cells < 0:
        raise ValueError("invalid cell count")
    return (0, 1) + tuple((address, 0, 1) for address in range(cells)) + tuple(
        (address, 1, 0) for address in range(cells)
    )


def remote_binary_states(cells, max_changed):
    """All 0/1 remote words with <=W net writes relative to zeros."""
    if not 0 <= max_changed <= cells:
        raise ValueError("invalid write budget")
    for weight in range(max_changed + 1):
        for positions in combinations(range(cells), weight):
            remote = [0] * cells
            for i in positions:
                remote[i] = 1
            yield tuple(remote)


def output_vectors_for_programs(programs, cells, max_changed, probe_bound):
    for remote in remote_binary_states(cells, max_changed):
        yield tuple(evaluate_tree(tree, remote, probe_bound)[0] for tree in programs)


@dataclass
class GF2SyndromeDynamic:
    """Hamming parity-check-column store; exactly one toggle per nonzero delta.

    No changing local manifest. Code/column listing is fixed public metadata,
    assumed free in G1-B finite model and MUST be priced in any real system.
    Query_i is XOR over ALL physical bits with column i = 1; exactly
    2**(n-1) cells are accessed for every i.
    """
    outputs: int
    memory: int = 0
    actual_writes: int = 0

    def __post_init__(self):
        if (not isinstance(self.outputs, int) or isinstance(self.outputs, bool)
                or self.outputs < 1 or self.outputs > 8):
            raise ValueError("finite exact oracle supports 1 <= n <= 8")
        if (not isinstance(self.memory, int) or self.memory < 0
                or self.memory >= (1 << ((1 << self.outputs) - 1))):
            raise ValueError("remote word outside physical cell count")

    @property
    def cell_count(self):
        return (1 << self.outputs) - 1

    @property
    def parity_read_count(self):
        return 1 << (self.outputs - 1)

    def query(self, i):
        if not isinstance(i, int) or not 0 <= i < self.outputs:
            raise ValueError("query outside logical output dimension")
        result = 0
        reads = 0
        for column in range(1, 1 << self.outputs):
            if (column >> i) & 1:
                reads += 1
                result ^= (self.memory >> (column - 1)) & 1
        assert reads == self.parity_read_count
        return result, reads

    def observe(self):
        return sum(self.query(i)[0] << i for i in range(self.outputs))

    def update(self, target):
        if (not isinstance(target, int) or isinstance(target, bool)
                or not 0 <= target < (1 << self.outputs)):
            raise ValueError("target out of range")
        previous = self.observe()
        delta = previous ^ target
        if delta:
            # The column with value delta is at *fixed public address* delta-1.
            self.memory ^= 1 << (delta - 1)
            self.actual_writes += 1
        if self.observe() != target:
            raise AssertionError("syndrome update failure")
        return int(bool(delta))


def independent_parity_syndrome(memory, outputs):
    """Second oracle sums selected generator columns, not GF2SyndromeDynamic.query."""
    result = 0
    for bit_position in range((1 << outputs) - 1):
        if memory & (1 << bit_position):
            result ^= bit_position + 1
    return result


def independent_column_requirements(outputs, columns):
    """Necessary universal one-bit-toggle image alphabet under parity reader."""
    if outputs < 1 or any(not 0 <= column < (1 << outputs) for column in columns):
        raise ValueError("bad columns")
    required = set(range(1, 1 << outputs))
    distinct = set(columns)
    return {
        "covers_all_nonzero_deltas": required.issubset(distinct),
        "num_unique_required": len(required & distinct),
        "row_ones": tuple(sum((column >> i) & 1 for column in columns)
                          for i in range(outputs)),
    }
