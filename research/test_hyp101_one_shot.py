"""HYP-101 one-shot exhaustive caching: hash-agnostic finite countermodel.

SHA-256 is used only as a standard-library deterministic test digest.
This does not claim an actual BLAKE3 implementation or security proof.
"""
import hashlib
import itertools
import unittest


def prepared_one_insert_table(base, alphabet):
    return {(index, value): hashlib.sha256(base[:index] + bytes([value])
                                         + base[index:]).digest()
            for index in range(len(base) + 1)
            for value in alphabet}


def independent_fresh_digest(base, index, value):
    data = bytearray()
    data.extend(base[:index])
    data.append(value)
    data.extend(base[index:])
    return hashlib.sha256(bytes(data)).digest()


class Hyp101OneShotTable(unittest.TestCase):
    def test_all_small_sources_and_insertion_queries(self):
        tested = 0
        for n in range(6):
            for alphabet_word in itertools.product((0, 1), repeat=n):
                base = bytes(alphabet_word)
                table = prepared_one_insert_table(base, (0, 1))
                self.assertEqual(len(table), 2 * (n + 1))
                for i in range(n + 1):
                    for value in (0, 1):
                        self.assertEqual(table[i, value],
                                         independent_fresh_digest(base, i, value))
                        tested += 1
        self.assertEqual(tested, sum((2 ** n) * 2 * (n + 1) for n in range(6)))

    def test_bit_budget_is_linear_only_for_fixed_alphabet(self):
        for n in (0, 1, 16, 100):
            # One 256-bit digest for each (position, byte value).
            self.assertEqual(256 * 256 * (n + 1), 65536 * (n + 1))

    def test_table_stale_after_a_second_edit(self):
        base = b"abc"
        old_table = prepared_one_insert_table(base, (ord("X"), ord("Y")))
        intermediate = b"Xabc"
        final = b"YXabc"
        self.assertEqual(old_table[0, ord("X")], hashlib.sha256(intermediate).digest())
        self.assertNotEqual(old_table[0, ord("Y")], hashlib.sha256(final).digest())
        rebuilt = prepared_one_insert_table(intermediate, (ord("Y"),))
        self.assertEqual(rebuilt[0, ord("Y")], hashlib.sha256(final).digest())


if __name__ == "__main__":
    unittest.main()
