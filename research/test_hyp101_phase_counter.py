"""HYP-101 G1: purely structural canonical chunk-input reuse experiments.

NO BLAKE3 implementation; keys include counter and byte payload, not digest.
No claim of unrestricted compression-query lower bounds or any security result.
"""
import itertools
import unittest


def canonical_leaf_inputs(data: bytes, chunk_len: int) -> set[tuple[int, bytes]]:
    if not isinstance(data, bytes) or not isinstance(chunk_len, int) or chunk_len < 1:
        raise ValueError("expected bytes and positive chunk_len")
    return {(index, data[pos:pos + chunk_len])
            for index, pos in enumerate(range(0, len(data), chunk_len))}


def exact_strict_cache_misses(old: bytes, new: bytes, chunk_len: int) -> int:
    return len(canonical_leaf_inputs(new, chunk_len)
               - canonical_leaf_inputs(old, chunk_len))


def independent_scan_misses(old: bytes, new: bytes, chunk_len: int) -> int:
    """Independent algorithm: compare same-index new/old chunks by slicing."""
    count = 0
    for j, start in enumerate(range(0, len(new), chunk_len)):
        new_chunk = new[start:start + chunk_len]
        if start >= len(old) or new_chunk != old[start:start + chunk_len]:
            count += 1
    return count


def insert(old: bytes, pos: int, payload: bytes) -> bytes:
    return old[:pos] + payload + old[pos:]


def delete(old: bytes, pos: int, length: int) -> bytes:
    return old[:pos] + old[pos + length:]


class CanonicalLeafInputAudits(unittest.TestCase):
    def test_exhaustive_binary_strings_insertions_deletions_and_overwrites(self):
        visits = 0
        for n in range(7):
            for bits in itertools.product((0, 1), repeat=n):
                old = bytes(bits)
                for size in (1, 2, 3, 4):
                    variants = {old}
                    for pos in range(n + 1):
                        variants.add(insert(old, pos, b"\x00"))
                        variants.add(insert(old, pos, b"\x01"))
                        for length in range(n - pos + 1):
                            variants.add(delete(old, pos, length))
                    for pos in range(n):
                        variants.add(old[:pos] + bytes([1 - old[pos]]) + old[pos + 1:])
                    for new in variants:
                        self.assertEqual(
                            exact_strict_cache_misses(old, new, size),
                            independent_scan_misses(old, new, size))
                        visits += 1
        self.assertGreater(visits, 3000)

    def test_proved_aligned_whole_chunk_insertion_distinct_neighbors(self):
        for size in (1, 2, 3, 4):
            for m in range(2, 8):
                # Distinct neighboring full chunks, no C_j==C_(j+1).
                old_chunks = tuple(bytes([j + 1]) * size for j in range(m))
                old = b"".join(old_chunks)
                inserted = bytes([253]) * size
                for k in range(m + 1):
                    new = insert(old, k * size, inserted)
                    expected = m - k + 1
                    self.assertEqual(exact_strict_cache_misses(old, new, size),
                                     expected)

    def test_high_periodicity_reuses_all_existing_same_index_keys(self):
        for m in (2, 3, 5, 9):
            for size in (1, 2, 4, 7):
                old = b"a" * (m * size)
                for k in range(m + 1):
                    new = insert(old, k * size, b"a" * size)
                    self.assertEqual(exact_strict_cache_misses(old, new, size), 1)

    def test_single_byte_edit_same_target_many_positions(self):
        for size in (1, 2, 4, 8):
            old = b"a" * (4 * size)
            outputs = {insert(old, k, b"a") for k in range(len(old) + 1)}
            self.assertEqual(len(outputs), 1)
            self.assertEqual(exact_strict_cache_misses(old, outputs.pop(), size), 1)

    def test_position_counter_is_part_of_identity(self):
        size = 2
        old = b"abcdefgh"
        new = insert(old, 0, b"ZZ")
        old_inputs = canonical_leaf_inputs(old, size)
        new_inputs = canonical_leaf_inputs(new, size)
        self.assertIn((0, b"ab"), old_inputs)
        self.assertIn((1, b"ab"), new_inputs)
        self.assertNotIn((1, b"ab"), old_inputs)
        self.assertEqual(exact_strict_cache_misses(old, new, size), 5)
        # A payload-only lookup would misleadingly re-use old b'ab'
        # for new counter 1; the canonical input is (counter, bytes).

    def test_no_hash_collision_or_unrestricted_lower_bound_claim(self):
        self.assertEqual(exact_strict_cache_misses(b"abc", b"abc", 2), 0)
        with self.assertRaises(ValueError):
            canonical_leaf_inputs(b"abc", 0)


if __name__ == "__main__":
    unittest.main()
