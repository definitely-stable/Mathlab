"""UCT-004 G2-5: independent exact GF(2) local parity proof length oracles.

Deterministic finite checks support a self-contained classical proof, not novelty.
"""
from itertools import combinations
from math import ceil
from fractions import Fraction
import unittest


def parity(x):
    return x.bit_count() & 1


def span(rows):
    values = {0}
    for row in rows:
        values |= {x ^ row for x in tuple(values)}
    return values


def linear_rank(rows):
    return len(span(rows)).bit_length() - 1


def block_sizes(n, cap):
    return [min(cap, n-i) for i in range(0, n, cap)]


def block_masks(n, cap):
    chunks = []
    for start in range(0, n, cap):
        end = min(n, start + cap)
        chunks.append(sum(1 << i for i in range(start, end)))
    return chunks


def block_witness(actual, n, cap):
    blocks = block_masks(n, cap)
    return tuple(parity(actual & s) for s in blocks[:-1])


def block_assertions(claim, alleged_witness, n, cap):
    blocks = block_masks(n, cap)
    last = claim
    for x in alleged_witness:
        last ^= x
    return tuple(alleged_witness) + (last,)


def block_accept_chance(actual, claim, witness, n, cap):
    blocks = block_masks(n, cap)
    alleged = block_assertions(claim, witness, n, cap)
    accepted = sum(parity(actual & mask) == bit
                   for mask, bit in zip(blocks, alleged))
    return Fraction(accepted, len(blocks))


class Uct004LinearLocalProofTests(unittest.TestCase):
    def test_short_row_basis_cannot_span_full_parity(self):
        # Exhaustive all SETS of fewer than ceil(n/p) independent check
        # candidates for all n<=5, even when check blocks overlap.
        attempts = 0
        for n in range(1, 6):
            full = (1 << n) - 1
            for p in range(1, n+1):
                g = ceil(n / p)
                candidates = tuple(mask for mask in range(1, 1 << n)
                                   if mask.bit_count() <= p)
                for rank_cap in range(g):
                    for selected in combinations(candidates, rank_cap):
                        self.assertNotIn(full, span(selected))
                        attempts += 1
        self.assertGreater(attempts, 100)

    def test_any_claim_parity_affine_fiber_has_at_most_2_to_n_minus_g(self):
        # For every small set of rows that spans the full parity,
        # number of possible input states meeting a *consistent*
        # parity-check right hand side equals 2^(n-rank).
        checked = 0
        for n in range(1, 5):
            full = (1 << n)-1
            for cap in range(1, n+1):
                g = ceil(n/cap)
                candidates = [m for m in range(1, 1 << n)
                              if m.bit_count() <= cap]
                for size in range(g, min(len(candidates), 3)+1):
                    for rows in combinations(candidates, size):
                        if full not in span(rows):
                            continue
                        rank = linear_rank(rows)
                        self.assertGreaterEqual(rank, g)
                        for base in range(1 << n):
                            rhs = tuple(parity(base & row) for row in rows)
                            fiber = [x for x in range(1 << n)
                                     if tuple(parity(x & row) for row in rows)
                                     == rhs]
                            self.assertEqual(len(fiber), 1 << (n-rank))
                            self.assertLessEqual(len(fiber), 1 << (n-g))
                            self.assertTrue(all(parity(x) == parity(base)
                                                for x in fiber))
                            checked += 1
        self.assertGreater(checked, 100)

    def test_block_protocol_all_honest_claims_perfect(self):
        for n in range(1, 8):
            for p in range(1, n+1):
                blocks = block_masks(n, p)
                self.assertEqual(len(blocks), ceil(n/p))
                self.assertTrue(all(mask.bit_count() <= p for mask in blocks))
                for x in range(1 << n):
                    pi = block_witness(x, n, p)
                    self.assertEqual(len(pi), len(blocks)-1)
                    self.assertEqual(block_accept_chance(
                        x, parity(x), pi, n, p), 1)

    def test_block_protocol_all_false_claims_and_all_witnesses(self):
        # All inputs and every forged b-bit message, no Monte Carlo.
        for n in range(1, 8):
            for p in range(1, n+1):
                g = ceil(n/p)
                max_soundness = Fraction(g-1, g)
                observed_worst = Fraction(0)
                for x in range(1 << n):
                    wrong_claim = parity(x) ^ 1
                    for raw in range(1 << (g-1)):
                        witness = tuple((raw >> i) & 1 for i in range(g-1))
                        chance = block_accept_chance(x, wrong_claim,
                                                     witness, n, p)
                        self.assertLessEqual(chance, max_soundness)
                        observed_worst = max(observed_worst, chance)
                self.assertEqual(observed_worst, max_soundness)

    def test_witness_count_lower_bound_even_with_variable_length(self):
        for n in range(1, 32):
            for p in range(1, n+1):
                g = ceil(n/p)
                states_same_parity = 1 << (n-1)
                states_per_witness_cap = 1 << (n-g)
                required = (states_same_parity + states_per_witness_cap - 1) // states_per_witness_cap
                self.assertEqual(required, 1 << (g-1))
                if g >= 2:
                    all_binary_messages_of_length_at_most_g_minus_2 = (1 << (g-1)) - 1
                    self.assertLess(all_binary_messages_of_length_at_most_g_minus_2,
                                    required)

    def test_one_probe_protocol_uses_n_minus_one_witness_bits(self):
        for n in range(1, 8):
            self.assertEqual(len(block_witness(0, n, 1)), n-1)
            for x in range(1 << n):
                pi = block_witness(x, n, 1)
                self.assertEqual(block_accept_chance(x, parity(x), pi,
                                                     n, 1), 1)
                if n > 1:
                    self.assertEqual(block_accept_chance(
                        x, parity(x) ^ 1, pi, n, 1),
                        Fraction(n-1, n))


if __name__ == "__main__":
    unittest.main()
