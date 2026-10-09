"""G1-B: independent finite branching information and online syndrome tests."""
import itertools
import unittest

from dag002_g1a_frontier import remote_state_volume
from dag002_g1b_adaptive import (
    potential_query_addresses, visible_remote_cells, adaptive_probe_local_bits,
    all_potential_tree_addresses, evaluate_tree,
    fixed_binary_one_probe_programs, remote_binary_states,
    output_vectors_for_programs, GF2SyndromeDynamic,
    independent_parity_syndrome, independent_column_requirements,
)


class G1BFiniteTests(unittest.TestCase):
    def test_exact_decision_tree_address_expansion_and_limits(self):
        for bits in (1, 2, 3):
            for probes in range(5):
                expected = sum((1 << bits) ** d for d in range(probes))
                self.assertEqual(potential_query_addresses(bits, probes), expected)
                self.assertEqual(visible_remote_cells(2, 100, bits, probes),
                                 min(100, 2 * expected))
        # Two adaptive binary probes, three potentially distinct addresses.
        branch = (0, (1, 0, 1), (2, 1, 0))
        self.assertEqual(all_potential_tree_addresses(branch), {0, 1, 2})
        for word in itertools.product((0, 1), repeat=3):
            result, reads = evaluate_tree(branch, word, 2)
            self.assertEqual(reads, 2)
            self.assertEqual(result, word[1] if word[0] == 0 else 1 - word[2])
            with self.assertRaises(ValueError):
                evaluate_tree(branch, word, 1)
        with self.assertRaises(ValueError):
            potential_query_addresses(0, 2)
        with self.assertRaises(ValueError):
            adaptive_probe_local_bits(2, 2, 4, 1, 5, 1)

    def test_exact_all_one_probe_boolean_decoders_with_written_cell_masks(self):
        # Independent enumeration of every possible read/negate/constant query
        # pair: no assumption of coordinate XOR or disjoint address use.
        for cells in range(0, 5):
            programs = fixed_binary_one_probe_programs(cells)
            for w in range(cells + 1):
                m = visible_remote_cells(2, cells, 1, 1)
                upper = remote_state_volume(m, 1, min(w, m))
                for first in programs:
                    for second in programs:
                        observed = set(output_vectors_for_programs(
                            (first, second), cells, w, 1))
                        self.assertLessEqual(len(observed), upper)
        # More remote *addresses* do not make P=1/W=1 sufficient
        # for all 4 two-bit answer vectors without local metadata.
        self.assertEqual(adaptive_probe_local_bits(4, 2, 3, 1, 1, 1), 1)
        self.assertEqual(adaptive_probe_local_bits(4, 2, 30, 1, 1, 1), 1)
        # The G1-A bound with N=3, W=1 permits B=0; G1-B refutes that.
        self.assertEqual(remote_state_volume(3, 1, 1), 4)

    def test_zero_remote_probes_and_narrow_legal_successor_alphabet(self):
        for n in range(1, 7):
            self.assertEqual(adaptive_probe_local_bits(1 << n, n, 200, 1, 0, 0), n)
            self.assertEqual(adaptive_probe_local_bits(1 << n, n, 200, 1, 20, 0), n)
            self.assertEqual(adaptive_probe_local_bits(n, n, 0, 1, 0, 0),
                             (n - 1).bit_length())
            self.assertEqual(adaptive_probe_local_bits(1 << n, n, 200, 1, 1, 1),
                             ( ( ((1 << n) + (n + 1) - 1) // (n + 1)) - 1).bit_length())

    def test_maintained_single_flip_linear_syndrome_all_small_update_sequences(self):
        # Independent source-state oracle; all 4^4 and 8^3 update histories.
        for n, history in ((1, 5), (2, 4), (3, 3), (4, 2)):
            for targets in itertools.product(range(1 << n), repeat=history):
                store = GF2SyndromeDynamic(n)
                writes = 0
                for target in targets:
                    before = store.memory
                    cost = store.update(target)
                    writes += cost
                    self.assertLessEqual(cost, 1)
                    self.assertEqual((before ^ store.memory).bit_count(), cost)
                    self.assertEqual(independent_parity_syndrome(store.memory, n),
                                     target)
                    self.assertEqual(tuple(store.query(i)[0] for i in range(n)),
                                     tuple((target >> i) & 1 for i in range(n)))
                    self.assertTrue(all(store.query(i)[1] == 1 << (n - 1)
                                        for i in range(n)))
                self.assertEqual(store.actual_writes, writes)

    def test_linear_single_flip_necessary_nonzero_columns_and_row_support(self):
        for n in range(1, 6):
            columns = tuple(range(1, 1 << n))
            result = independent_column_requirements(n, columns)
            self.assertTrue(result["covers_all_nonzero_deltas"])
            self.assertEqual(result["num_unique_required"], (1 << n) - 1)
            self.assertEqual(result["row_ones"], (1 << (n - 1),) * n)
            for omitted in columns:
                bad = independent_column_requirements(n,
                            tuple(x for x in columns if x != omitted))
                self.assertFalse(bad["covers_all_nonzero_deltas"])
        # Exhaust all 1-3 physical columns over 2 output bits.
        for size in range(4):
            for columns in itertools.product(range(4), repeat=size):
                r = independent_column_requirements(2, columns)
                if r["covers_all_nonzero_deltas"]:
                    self.assertGreaterEqual(size, 3)
                    self.assertGreaterEqual(min(r["row_ones"]), 2)

    def test_dynamic_two_outputs_strict_probe_separation(self):
        # n=2, N=3, W=1, B=G=0, P=2 achieves all 4 logical
        # states from *every history*; P=1 cannot cover all successors.
        self.assertEqual(adaptive_probe_local_bits(4, 2, 3, 1, 1, 2), 0)
        self.assertEqual(adaptive_probe_local_bits(4, 2, 3, 1, 1, 1), 1)
        for remote in range(1 << 3):
            store = GF2SyndromeDynamic(2, remote)
            for desired in range(4):
                copy = GF2SyndromeDynamic(2, store.memory)
                self.assertLessEqual(copy.update(desired), 1)
                self.assertEqual(copy.observe(), desired)
                self.assertEqual(independent_parity_syndrome(copy.memory, 2), desired)

    def test_no_claim_of_general_amortized_physical_write_complexity(self):
        # Each update performs no more than one logical cell toggle; this
        # says nothing about page rewrites, WAL, crashes or metadata layout.
        s = GF2SyndromeDynamic(2)
        seq = (3, 2, 1, 0, 0, 3, 1, 3)
        costs = [s.update(v) for v in seq]
        self.assertEqual(costs, [1, 1, 1, 1, 0, 1, 1, 1])
        self.assertEqual(s.actual_writes, 7)


if __name__ == "__main__":
    unittest.main()
