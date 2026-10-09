"""UCT-004 G2-D exact finite PPZ + nonlinear proof-cover cross-checks.

These exhaustive oracles are falsification companions, NOT an all-n computer proof.
"""
from fractions import Fraction
from itertools import permutations, product
from math import ceil
import unittest


def parity(x):
    return x.bit_count() & 1


def clause_satisfied(x, clause):
    """Clause forbids matching an assignment on given support."""
    support, forbidden = clause
    return (x & support) != (forbidden & support)


def sat(cnf, n):
    return tuple(x for x in range(1 << n)
                 if all(clause_satisfied(x, c) for c in cnf))


def build_separating_cnf(n, p, honest):
    """Either return genuine width-p CNF for H, or None if not separable."""
    claim = parity(honest[0])
    assert all(parity(x) == claim for x in honest)
    clauses = []
    for y in range(1 << n):
        if parity(y) == claim:
            continue
        mask = next((s for s in range(1, 1 << n)
                     if s.bit_count() <= p
                     and all((x & s) != (y & s) for x in honest)), None)
        if mask is None:
            return None
        clauses.append((mask, y))
    return tuple(clauses)


def critical_supports(cnf, n, solution):
    assert solution in sat(cnf, n)
    supports = []
    for i in range(n):
        changed = solution ^ (1 << i)
        assert changed not in sat(cnf, n)
        eligible = [support for support, forbidden in cnf
                    if clause_satisfied(solution, (support, forbidden))
                    and not clause_satisfied(changed, (support, forbidden))]
        assert eligible
        supports.append(min(eligible, key=int.bit_count))
    return tuple(supports)


def ppz_exact_hit_probability(cnf, n, target):
    """Enumerate each permutation and all random decision tapes."""
    favorable, total = 0, 0
    for order in permutations(range(n)):
        for random_bits in range(1 << n):
            partial, assigned = 0, 0
            for i in order:
                decision = (random_bits >> i) & 1
                for support, forbidden in cnf:
                    # Is there a clause whose other literals already false?
                    remaining = support & ~assigned
                    if remaining != (1 << i):
                        continue
                    if (partial & (support & assigned)) == (
                            forbidden & (support & assigned)):
                        decision = 1 ^ ((forbidden >> i) & 1)
                        break
                partial |= decision << i
                assigned |= 1 << i
            total += 1
            favorable += partial == target
    return Fraction(favorable, total)


def block_masks(n, p):
    return tuple(sum(1 << i for i in range(start, min(start+p, n)))
                 for start in range(0, n, p))


class Uct004PpzAllNTests(unittest.TestCase):
    def test_all_small_nonlinear_fibers_embed_in_isolated_short_cnf(self):
        checked = 0
        for n in (1, 2, 3, 4):
            honest_candidates = [x for x in range(1 << n) if parity(x) == 0]
            for p in range(1, n+1):
                for bits in range(1, 1 << len(honest_candidates)):
                    H = tuple(honest_candidates[i]
                              for i in range(len(honest_candidates))
                              if bits & (1 << i))
                    cnf = build_separating_cnf(n, p, H)
                    if cnf is None:
                        continue
                    solutions = sat(cnf, n)
                    self.assertTrue(set(H).issubset(solutions))
                    self.assertTrue(all(parity(x) == 0 for x in solutions))
                    self.assertTrue(all(x ^ (1 << i) not in solutions
                                        for x in solutions for i in range(n)))
                    self.assertTrue(all(s.bit_count() <= p for s, _ in cnf))
                    # Exact integer reformulation of |SAT|<=2^(n-n/p).
                    self.assertLessEqual(len(solutions)**p, 2**(n*(p-1)))
                    checked += 1
        self.assertGreater(checked, 200)

    def test_ppz_critical_clauses_random_permutation_probability(self):
        # Strictly independent exact PPZ simulation on several CNFs that
        # represent fixed-parity blocks and admit isolated solutions.
        for n, p in ((1, 1), (2, 1), (3, 2), (4, 2)):
            blocks = block_masks(n, p)
            clauses = tuple((mask, value) for mask in blocks
                            for value in range(1 << n)
                            if parity(value & mask))
            for x in sat(clauses, n):
                crit = critical_supports(clauses, n, x)
                self.assertEqual(len(crit), n)
                self.assertTrue(all(v.bit_count() <= p for v in crit))
                probability = ppz_exact_hit_probability(clauses, n, x)
                # P(x)^p >= 2^(-n(p-1)) is exactly PPZ probability lower.
                self.assertGreaterEqual(probability**p,
                                        Fraction(1, 2**(n*(p-1))))

    def test_divisible_n_block_construction_attains_ppz_count(self):
        for n in range(1, 9):
            for p in range(1, n+1):
                if n % p:
                    continue
                blocks = block_masks(n, p)
                cnf = tuple((mask, forbidden)
                            for mask in blocks
                            for forbidden in range(1 << n)
                            if parity(forbidden & mask))
                good = sat(cnf, n)
                self.assertEqual(len(good), 2**(n - n//p))
                self.assertTrue(all(parity(x & mask) == 0
                                    for x in good for mask in blocks))
                self.assertTrue(all(x ^ (1 << i) not in good
                                    for x in good for i in range(n)))

    def test_all_n_ceil_proof_length_integer_frontier(self):
        for n in range(1, 129):
            for p in range(1, n+1):
                g = (n+p-1)//p
                b = g-1
                self.assertGreaterEqual(p*(b+1), n)
                if b>0:
                    self.assertLess(p*b, n)
                self.assertEqual(b, ceil(n/p)-1)
                self.assertLessEqual(len(block_masks(n, p)), b+1)

    def test_exact_kappa_lower_upper_do_not_imply_integer_closed_form(self):
        # Bounds on K, rather than b, differ when p does not divide n.
        n, p = 7, 2
        lower = next(k for k in range(1, 100)
                     if k**p >= 2**(n-p))
        upper = 2**(((n+p-1)//p)-1)
        self.assertEqual((lower, upper), (6, 8))
        self.assertTrue(lower < upper)
        # Yet all K in this allowable interval demand three proof bits.
        self.assertEqual({(k-1).bit_length() for k in range(lower, upper+1)},
                         {3})

    def test_nonlinear_six_state_fiber_satisfies_ppz_not_affine_cap(self):
        n, p = 4, 3
        H = tuple(x for x in range(1 << n) if x.bit_count() == 2)
        self.assertEqual(len(H), 6)
        self.assertGreater(len(H), 2**(n-((n+p-1)//p)))
        F = build_separating_cnf(n, p, H)
        self.assertIsNotNone(F)
        self.assertLessEqual(len(sat(F, n))**p, 2**(n*(p-1)))

    def test_false_witness_cost_and_fixed_soundness_not_conflated(self):
        for n in range(1, 12):
            for p in range(1, n+1):
                g = (n+p-1)//p
                soundness = Fraction(g-1, g)
                self.assertLess(soundness, 1)
                self.assertEqual(soundness, 0 if p == n
                                 else Fraction(g-1, g))
                self.assertGreaterEqual(p, Fraction(n, g))


if __name__ == "__main__":
    unittest.main()
