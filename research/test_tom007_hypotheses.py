"""Finite falsification oracles for TOM-007 research scouting.

These tests are NOT proofs of asymptotic hypotheses, BLAKE3 security, or
originality. All logic is dependency-free and does not alter production.
"""
import itertools
import unittest


def truth_table(function_bits, a, b):
    """Two-input Boolean function selected by its four truth-table bits."""
    return (function_bits >> (2 * a + b)) & 1


def independent_truth_table(function_bits, a, b):
    """Independent truth-table representation via base-2 binary vector."""
    bitset = tuple(int(v) for v in format(function_bits, "04b")[::-1])
    return bitset[2 * a + b]


def batch_singleton_claims(function_bits, a, b):
    """Naively assert batch no-effect if both individual edits preserve output."""
    old = truth_table(function_bits, a, b)
    return (truth_table(function_bits, 1 - a, b) == old
            and truth_table(function_bits, a, 1 - b) == old)


def exhaustive_subset_signature(columns, field, max_active):
    """Whether all subsets up to max_active have distinct finite-field sums."""
    dimension = len(columns[0])
    signatures = set()
    for used in range(min(max_active, len(columns)) + 1):
        for subset in itertools.combinations(columns, used):
            sig = tuple(sum(v[i] for v in subset) % field for i in range(dimension))
            if sig in signatures:
                return False
            signatures.add(sig)
    return True


def independent_small_column_free(columns, field, max_support):
    """No nonzero coefficient vector with support <= max_support sums to zero."""
    dimension = len(columns[0])
    for coeffs in itertools.product(range(field), repeat=len(columns)):
        if all(v == 0 for v in coeffs):
            continue
        if sum(v != 0 for v in coeffs) > max_support:
            continue
        if all(sum(c * v[i] for c, v in zip(coeffs, columns)) % field == 0
               for i in range(dimension)):
            return False
    return True


def reference_chunk_inputs(content, size):
    if size < 1:
        raise ValueError("size must be positive")
    return tuple(content[i:i + size] for i in range(0, len(content), size))


def independently_rebuild_blocks(content, size):
    """Another enumeration strategy for the *toy* fixed-alignment inputs."""
    if size < 1:
        raise ValueError("invalid block size")
    chunks = []
    offset = 0
    while offset < len(content):
        chunks.append(bytes(content[offset:min(len(content), offset + size)]))
        offset += size
    return tuple(chunks)


def shared_content_count(snapshots):
    """Abstract perfect cross-snapshot sharing; NOT pack-level compaction."""
    return len(set().union(*snapshots)) if snapshots else 0


class Tom007Falsification(unittest.TestCase):
    def test_hyp103_boolean_conjunction_not_sound(self):
        witness = None
        total = 0
        for f in range(16):
            for a, b in itertools.product((0, 1), repeat=2):
                self.assertEqual(truth_table(f, a, b),
                                 independent_truth_table(f, a, b))
                naive = batch_singleton_claims(f, a, b)
                joint = truth_table(f, a, b) == truth_table(f, 1-a, 1-b)
                if naive and not joint:
                    witness = (f, a, b)
                    total += 1
        self.assertGreater(total, 0)
        self.assertTrue(batch_singleton_claims(8, 0, 0))  # AND
        self.assertNotEqual(truth_table(8, 0, 0), truth_table(8, 1, 1))
        self.assertIsNotNone(witness)

    def test_hyp105_finite_not_asymptotic_GF5(self):
        columns = ((1,), (2,))
        self.assertTrue(exhaustive_subset_signature(columns, 5, 3))
        self.assertFalse(independent_small_column_free(columns, 5, 6))
        self.assertEqual({0, 1, 2, 3},
                         {sum(columns[i][0] for i in s) % 5
                          for r in range(3)
                          for s in itertools.combinations(range(2), r)})
        # Characteristic-three example is not a substitute for odd-q>=5 witness.
        self.assertFalse(exhaustive_subset_signature(columns, 3, 3))

    def test_hyp101_fixed_block_input_invalidation_not_digest_lower_bound(self):
        for size in (2, 3, 4):
            for old in (bytes(range(1, 17)), b"a" * 16):
                for position in (0, 1, len(old) // 2, len(old)):
                    new = old[:position] + b"Z" + old[position:]
                    before = reference_chunk_inputs(old, size)
                    after = reference_chunk_inputs(new, size)
                    self.assertEqual(after, independently_rebuild_blocks(new, size))
                    changed = sum(i >= len(before) or chunk != before[i]
                                  for i, chunk in enumerate(after))
                    self.assertGreaterEqual(changed, 1)
        # The number of changed leaves depends on actual content, even
        # for the same insert position and block width.
        def changed(old, size):
            before = reference_chunk_inputs(old, size)
            after = reference_chunk_inputs(b"Z" + old, size)
            return sum(i >= len(before) or x != before[i]
                       for i, x in enumerate(after))
        self.assertGreater(changed(bytes(range(1, 17)), 4),
                           changed(b"a" * 16, 4))

    def test_hyp104_snapshot_count_not_diversity(self):
        base = frozenset((1, 2, 3))
        for pins in (1, 2, 8, 32):
            self.assertEqual(shared_content_count([base] * pins), 3)
        self.assertEqual(shared_content_count([base, frozenset((4,))]), 4)

    def test_input_rejection(self):
        with self.assertRaises(ValueError):
            reference_chunk_inputs(b"abc", 0)
        with self.assertRaises(ValueError):
            independently_rebuild_blocks(b"abc", -1)


if __name__ == "__main__":
    unittest.main()
