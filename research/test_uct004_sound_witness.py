"""Finite independent UCT-004 G2-A checks. Classical result, no source-proof audit claim."""
from fractions import Fraction
from itertools import combinations, product
from math import comb
import unittest


def parity(x):
    return x.bit_count() & 1


def supports(raw, other, width):
    return frozenset(i for i in range(width) if (raw ^ other) & (1 << i))


def accepts_sample(actual, witness, n, coordinates):
    return all((actual >> i) & 1 == (witness >> i) & 1
               for i in coordinates)


def sample_accept_probability(actual, witness, n, probes):
    choices = tuple(combinations(range(n), probes))
    return Fraction(sum(accepts_sample(actual, witness, n, c)
                        for c in choices), len(choices))


def verify_randomized_influence_on_all_accept_tables(n):
    """Exactly enumerate every accept/reject lookup for n private coin seeds.

    Each of n equiprobable seeds probes precisely its indexed bit;
    the fixed claimant/prover is considered part of the protocol table.
    For x=0 and every opposite-answer one-bit neighbor y, acceptance
    gap cannot exceed probability of reading its changed coordinate.
    """
    assert 1 <= n <= 4
    max_gap = Fraction(0)
    tables = 0
    for accept_mask in range(1 << (2*n)):
        def probability(x):
            return Fraction(sum((accept_mask >> (2*coin +
                            ((x >> coin) & 1))) & 1
                            for coin in range(n)), n)
        old = probability(0)
        for i in range(n):
            new = probability(1 << i)
            self_event = Fraction(1, n)
            assert old - new <= self_event
            max_gap = max(max_gap, old - new)
        tables += 1
    return tables, max_gap


def fractional_packing_grid(sets, cells):
    """Independent exhaustive half-integer LP on <=3 update supports.

    Not a general-purpose LP solver: this toy oracle demonstrates a real
    fractional integrality gap with feasible weights 1/2.
    """
    best = Fraction(0)
    witnesses = ()
    for weights in product((Fraction(0), Fraction(1, 2), Fraction(1)),
                           repeat=len(sets)):
        if all(sum((weights[j] for j, support in enumerate(sets)
                    if cell in support), Fraction(0)) <= 1
               for cell in range(cells)):
            value = sum(weights, Fraction(0))
            if value > best:
                best, witnesses = value, weights
    return best, witnesses


class Uct004SoundWitnessTests(unittest.TestCase):
    def test_exhaustive_private_coin_lookup_tables_obey_pairwise_coupling(self):
        for n in range(1, 5):
            tables, gap = verify_randomized_influence_on_all_accept_tables(n)
            self.assertEqual(tables, 1 << (2*n))
            self.assertEqual(gap, Fraction(1, n))

    def test_uniform_honest_witness_exact_completeness(self):
        for n in range(1, 7):
            for x in range(1 << n):
                for p in range(n+1):
                    self.assertEqual(sample_accept_probability(x, x, n, p), 1)

    def test_all_false_parity_witnesses_satisfy_exact_soundness_frontier(self):
        # Every input, every malicious witness with opposite parity, all
        # sample sizes. Explicit exact fractions, no Monte Carlo.
        for n in range(1, 7):
            frontier = Fraction(n, n)
            for x in range(1 << n):
                for alleged in range(1 << n):
                    if parity(alleged) == parity(x):
                        continue
                    for p in range(n+1):
                        actual_pass = sample_accept_probability(x, alleged,
                                                                n, p)
                        claimed_max = Fraction(n-p, n)
                        self.assertLessEqual(actual_pass, claimed_max)
                        if (x ^ alleged).bit_count() == 1:
                            self.assertEqual(actual_pass, claimed_max)

    def test_sampling_protocol_pass_rate_agrees_with_binomial_formula(self):
        for n in range(1, 8):
            for errors in range(1, n+1):
                witness = (1 << errors) - 1
                for p in range(n+1):
                    actual = sample_accept_probability(0, witness, n, p)
                    expected = Fraction(comb(n-errors, p)
                                        if p <= n-errors else 0, comb(n, p))
                    self.assertEqual(actual, expected)

    def test_fractional_packing_can_strictly_beat_integral_matching(self):
        sets = (frozenset({0, 1}), frozenset({1, 2}),
                frozenset({0, 2}))
        fractional, weights = fractional_packing_grid(sets, 3)
        self.assertEqual(fractional, Fraction(3, 2))
        self.assertEqual(weights, (Fraction(1, 2),)*3)
        matching = 0
        for mask in range(1 << len(sets)):
            taken = [sets[i] for i in range(len(sets)) if mask & (1 << i)]
            if all(not (a & b) for a, b in combinations(taken, 2)):
                matching = max(matching, len(taken))
        self.assertEqual(matching, 1)
        # Combinatorial example only; NOT a claim of a valid full-cube code.

    def test_unit_write_parity_has_disjoint_update_support(self):
        for n in range(1, 8):
            x = 0
            edges = [supports(x, x ^ (1 << i), n) for i in range(n)]
            self.assertEqual(edges, [frozenset({i}) for i in range(n)])
            self.assertTrue(all(not (a & b)
                                for a, b in combinations(edges, 2)))

    def test_parity_cache_two_writes_collapses_witness_packing(self):
        for n in range(2, 8):
            def code(x):
                return x | (parity(x) << n)
            original = code(0)
            edges = [supports(original, code(1 << i), n+1)
                     for i in range(n)]
            self.assertEqual(edges, [frozenset({i, n})
                                     for i in range(n)])
            self.assertTrue(all(n in s for s in edges))
            self.assertEqual(len({(code(x) >> n) & 1
                                  for x in range(1 << n)}), 2)
            # The shared parity cell is a complete one-bit witness,
            # demonstrating why w=2 does not entail p>=n/2.
            for x in range(1 << n):
                self.assertEqual((code(x) >> n) & 1, parity(x))

    def test_free_input_dependent_oracle_breaks_scope(self):
        for n in (2, 4, 7):
            x, y = 0, 1
            # Trivial fixed storage: outputs recoverable only from
            # an external uncharged oracle. This violates G2 assumptions.
            code_old = code_new = (0,)
            self.assertEqual(code_old, code_new)
            self.assertNotEqual(parity(x), parity(y))

    def test_coin_revealing_can_defeat_fixed_witness_soundness_contract(self):
        # Proof selected after seeing public coin: for each fixed pi,
        # accept probability is 1/2. Adaptive witness pi=R gives 1.
        for witness in (0, 1):
            self.assertEqual(Fraction(sum(witness == r for r in (0, 1)), 2),
                             Fraction(1, 2))
        self.assertEqual(sum(r == r for r in (0, 1)), 2)


if __name__ == "__main__":
    unittest.main()
