"""UCT-003 classical operational influence bounds, independently falsified on finite models.

No proof of novelty, probabilistic security, or multi-probe asymptotic lower bounds.
"""
from itertools import product
from math import log2
import unittest


def states(n):
    return tuple(range(1 << n))


def bit(x, i):
    return (x >> i) & 1


def prefix(x, k):
    return (x & ((1 << k) - 1)).bit_count() & 1


def direct_mem(x, n):
    return tuple(bit(x, i) for i in range(n))


def prefix_mem(x, n):
    return tuple(prefix(x, k) for k in range(1, n + 1))


def hamming_support(left, right):
    return frozenset(i for i, (a, b) in enumerate(zip(left, right)) if a != b)


def exact_transversal(read_sets, m):
    if not read_sets:
        return 0
    for mask in range(1 << m):
        if all(any(mask & (1 << idx) for idx in group) for group in read_sets):
            return mask.bit_count()
    raise AssertionError("empty read path for changed output")


def adaptive_two_probe(mem, first, second_by_first, truth_table):
    """Tree is selected by public query; next address depends on first bit."""
    path = [first]
    observed = mem[first]
    next_addr = second_by_first[observed]
    path.append(next_addr)
    second = mem[next_addr]
    output = (truth_table >> (2*observed + second)) & 1
    return output, frozenset(path)


def enum_boolean_function_values(n, mask):
    return tuple((mask >> x) & 1 for x in states(n))


def function_classes(bit_tables, state_count):
    """Independent equivalence partition under f~g or f~not g."""
    all_ones = (1 << state_count) - 1
    classes = set()
    for table in bit_tables:
        if table not in (0, all_ones):
            classes.add(min(table, all_ones ^ table))
    return classes


class Uct003InfluenceTests(unittest.TestCase):
    def test_exhaustive_adaptive_depth_two_influence_hits_actual_writes(self):
        # Exhaustive 2-bit stored function pairs (16*16), 128 adaptive
        # two-probe trees, and 4 hypercube-state edges (both directions).
        checked = 0
        for c0, c1 in product(range(16), repeat=2):
            memories = [((c0 >> x) & 1, (c1 >> x) & 1) for x in range(4)]
            for first in range(2):
                for second in product(range(2), repeat=2):
                    for output_table in range(16):
                        observations = [
                            adaptive_two_probe(mem, first, second, output_table)
                            for mem in memories
                        ]
                        for x in range(4):
                            for i in range(2):
                                y = x ^ (1 << i)
                                if observations[x][0] != observations[y][0]:
                                    writes = hamming_support(memories[x], memories[y])
                                    self.assertTrue(writes & observations[x][1])
                                checked += 1
        self.assertEqual(checked, 256*2*4*16*4*2)

    def test_exact_hitting_set_on_all_two_bit_state_update_edges(self):
        # Queries have both direct and combined parity read paths.
        queries = [
            lambda x: (bit(x, 0), {0}),
            lambda x: (bit(x, 1), {1}),
            lambda x: (prefix(x, 2), {0, 1}),
            lambda x: (1 ^ prefix(x, 2), {0, 1}),
        ]
        for x in range(4):
            for y in range(4):
                before = direct_mem(x, 2)
                after = direct_mem(y, 2)
                writes = hamming_support(before, after)
                changed_paths = []
                for query in queries:
                    old_result, old_path = query(x)
                    new_result, _ = query(y)
                    if old_result != new_result:
                        changed_paths.append(old_path)
                self.assertLessEqual(exact_transversal(changed_paths, 2),
                                     len(writes))

    def test_one_probe_minimal_functions_and_exact_writes_exhaustive(self):
        # All families of 3 Boolean functions on all 2-bit states.
        # Constants require 0 probes. Complements may reuse a cell.
        for family in product(range(16), repeat=3):
            classes = function_classes(family, 4)
            representatives = sorted(classes)
            encoded = [
                tuple((mask >> x) & 1 for mask in representatives)
                for x in range(4)
            ]
            for x in range(4):
                for i in range(2):
                    y = x ^ (1 << i)
                    expected = sum(
                        ((table >> x) & 1) != ((table >> y) & 1)
                        for table in representatives
                    )
                    self.assertEqual(
                        len(hamming_support(encoded[x], encoded[y])),
                        expected
                    )
            # Every nonconstant function must equal or complement one
            # directly stored bit. The explicit construction has one bit
            # for each class and meets the lower bound exactly.
            all_one = 15
            for table in family:
                if table in (0, all_one):
                    continue
                self.assertTrue(
                    any(table == rep or table == (all_one ^ rep)
                        for rep in representatives)
                )

    def test_prefix_parity_one_probe_exact_n_write_barrier(self):
        for n in range(1, 8):
            prefixes = [
                sum(prefix(x, k) << x for x in states(n))
                for k in range(1, n+1)
            ]
            self.assertEqual(len(function_classes(prefixes, 1 << n)), n)
            for x in states(n):
                code = prefix_mem(x, n)
                self.assertEqual(code, tuple(prefix(x, k)
                                             for k in range(1, n+1)))
                for i in range(n):
                    updated = prefix_mem(x ^ (1 << i), n)
                    changed = hamming_support(code, updated)
                    self.assertEqual(len(changed), n-i)
            # Exact sharp update-by-public-index, no hidden old input.
            self.assertEqual(len(prefix_mem(0, n)), n)

    def test_fenwick_escapes_false_write_times_probe_ge_n(self):
        def make_tree(bits):
            n = len(bits)
            tree = [0] * (n + 1)
            for i, val in enumerate(bits, 1):
                j = i
                while j <= n:
                    tree[j] ^= val
                    j += j & -j
            return tree

        def lookup(tree, k):
            visited, result = [], 0
            while k > 0:
                visited.append(k)
                result ^= tree[k]
                k -= k & -k
            return result, len(visited)

        for n in (1, 2, 3, 4, 8, 16, 32, 256):
            maximum_update = maximum_read = 0
            sample = range(1 << n) if n <= 4 else (0, 1, 3, (1 << n)-1)
            for x in sample:
                original = [bit(x, i) for i in range(n)]
                tree = make_tree(original)
                for k in range(1, n+1):
                    answer, reads = lookup(tree, k)
                    self.assertEqual(answer, prefix(x, k))
                    maximum_read = max(maximum_read, reads)
                for i in range(n):
                    new = original.copy()
                    new[i] ^= 1
                    newer = make_tree(new)
                    writes = len(hamming_support(tree, newer))
                    # one toggle influences one Fenwick chain
                    self.assertGreaterEqual(writes, 1)
                    maximum_update = max(maximum_update, writes)
                    self.assertEqual(lookup(newer, n)[0],
                                     prefix(x ^ (1 << i), n))
            self.assertLessEqual(maximum_read, n.bit_length())
            self.assertLessEqual(maximum_update, n.bit_length())
            if n == 256:
                self.assertLess(maximum_read * maximum_update, n)

    def test_free_external_old_root_breaks_read_write_model(self):
        # n prefix functions can be read from an uncharged external helper.
        # Raw-input representation changes one bit, but all n answers
        # change for input 0: the physical read set is then OUTSIDE memory.
        for n in range(2, 8):
            x, y = 0, 1
            self.assertEqual(len(hamming_support(direct_mem(x, n),
                                                 direct_mem(y, n))), 1)
            external_old = tuple(prefix(x, k) for k in range(1, n+1))
            external_new = tuple(prefix(y, k) for k in range(1, n+1))
            self.assertEqual(sum(a != b for a,b in zip(external_old,
                                                        external_new)), n)


if __name__ == "__main__":
    unittest.main()
