"""HYP-105 G5-C0: genuinely weighted GF(5) ASET versus six-wise independence.

Two *algorithmically independent* ASET decision paths:
  1. hash all actual subset sums of cardinality 0..3;
  2. enumerate bounded signed {-1,0,+1} annihilators without hashing subsets.
Two independent linear-dependence paths:
  1. modular Gaussian rank;
  2. exhaustive arbitrary GF(q) coefficient search for small N.
Finite tests do NOT establish an asymptotic exponent or a novel theorem.
"""
import itertools
import unittest


def admissible(columns, q, m):
    return (q in (2, 3, 5, 7, 11)
            and len(columns) == len(set(columns))
            and all(len(c) == m
                    and 1 <= sum(x % q != 0 for x in c) <= 4
                    and all(isinstance(x, int) and 0 <= x < q for x in c)
                    for c in columns))


def direct_aset_collision(columns, q, d=3):
    """Oracle A: enumerate physical subset sums, including empty/cross-size."""
    m = len(columns[0]) if columns else 0
    seen = {}
    for size in range(min(d, len(columns)) + 1):
        for indices in itertools.combinations(range(len(columns)), size):
            total = [0] * m
            for index in indices:
                for j, x in enumerate(columns[index]):
                    total[j] = (total[j] + x) % q
            signature = tuple(total)
            if signature in seen:
                return seen[signature], indices
            seen[signature] = indices
    return None


def signed_trade(columns, q, d=3):
    """Oracle B: ternary signed kernel; independent of subset-sum hashing."""
    n = len(columns)
    m = len(columns[0]) if n else 0
    for pattern in itertools.product((-1, 0, 1), repeat=n):
        plus = sum(x == 1 for x in pattern)
        minus = sum(x == -1 for x in pattern)
        if not (0 < plus + minus <= 2 * d and plus <= d and minus <= d):
            continue
        residual = []
        for j in range(m):
            value = 0
            for i in range(n):
                value += pattern[i] * columns[i][j]
            residual.append(value % q)
        if not any(residual):
            return tuple(i for i, x in enumerate(pattern) if x == 1), tuple(
                i for i, x in enumerate(pattern) if x == -1)
    return None


def rank_mod_q(columns, q):
    """Oracle C: modular row elimination; no exhaustive coefficient loop."""
    if not columns:
        return 0
    data = [list(row) for row in zip(*columns)]
    rows, cols = len(data), len(columns)
    pivot_count = 0
    for j in range(cols):
        pivot = next((i for i in range(pivot_count, rows)
                      if data[i][j] % q), None)
        if pivot is None:
            continue
        data[pivot_count], data[pivot] = data[pivot], data[pivot_count]
        factor = pow(data[pivot_count][j], -1, q)
        data[pivot_count] = [(x * factor) % q for x in data[pivot_count]]
        for i in range(rows):
            if i != pivot_count and data[i][j]:
                f = data[i][j]
                data[i] = [(x - f * y) % q for x, y in zip(
                    data[i], data[pivot_count])]
        pivot_count += 1
        if pivot_count == rows:
            break
    return pivot_count


def arbitrary_dependence_bruteforce(columns, q):
    """Oracle D: independent exhaustive GF(q)^N nonzero coefficient witness."""
    n = len(columns)
    m = len(columns[0]) if columns else 0
    for coeffs in itertools.product(range(q), repeat=n):
        if not any(coeffs):
            continue
        if all(sum(coeffs[i] * columns[i][j]
                   for i in range(n)) % q == 0 for j in range(m)):
            return coeffs
    return None


def dependent_at_most_six(columns, q):
    for size in range(1, min(6, len(columns)) + 1):
        for subset in itertools.combinations(columns, size):
            if rank_mod_q(subset, q) < size:
                return True
    return False


class G5CSignedAndLinearTests(unittest.TestCase):
    def test_exact_support_four_aset_not_three_wise_linear_independence(self):
        # Every column has 4 nonzero coordinates, not a degenerate weight-1 case.
        # Cardinality is encoded by last 3 unit "hub" coordinates (0..3 < 5).
        # At a fixed cardinality the first-coordinate sums of {1,2,3} differ.
        columns = ((1, 1, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1))
        self.assertTrue(admissible(columns, 5, 4))
        self.assertIsNone(direct_aset_collision(columns, 5))
        self.assertIsNone(signed_trade(columns, 5))
        self.assertEqual(rank_mod_q(columns, 5), 2)
        self.assertEqual(arbitrary_dependence_bruteforce(columns, 5) is not None, True)
        # One explicit non-signed dependence: a - 2*b + c = 0 (mod 5).
        self.assertEqual(tuple((columns[0][j] - 2 * columns[1][j]
                                + columns[2][j]) % 5 for j in range(4)),
                         (0,) * 4)
        self.assertTrue(dependent_at_most_six(columns, 5))

    def test_all_activity_sizes_are_needed(self):
        # Even an unbalanced 2-vs-1 trade must be detected, not only 2+2/3+3.
        examples = [
            ((1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0)),
            ((1, 0, 0, 0), (4, 0, 0, 0)),
            ((1, 0, 0, 0), (1, 0, 0, 0)),
        ]
        for columns in examples:
            self.assertIsNotNone(direct_aset_collision(columns, 5))
            self.assertIsNotNone(signed_trade(columns, 5))

    def test_independent_oracle_agreement_weighted_cases(self):
        # Enumerate a deterministic pool with repeated supports but distinct
        # *weighted* signatures; q=5 includes non-{0,1} coefficients.
        pool = ((1, 1, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1),
                (1, 2, 1, 1), (1, 3, 1, 1), (1, 1, 2, 1),
                (1, 1, 3, 1))
        cases = 0
        for count in range(6):
            for columns in itertools.combinations(pool, count):
                self.assertTrue(admissible(columns, 5, 4))
                a = direct_aset_collision(columns, 5)
                b = signed_trade(columns, 5)
                self.assertEqual(a is None, b is None, columns)
                if a is not None:
                    self.assertNotEqual(a[0], a[1])
                if b is not None:
                    self.assertLessEqual(len(b[0]), 3)
                    self.assertLessEqual(len(b[1]), 3)
                    self.assertFalse(set(b[0]) & set(b[1]))
                cases += 1
        self.assertEqual(cases, 120)

    def test_independent_linear_oracles_on_held_out_fields(self):
        # Unlike signed kernel enumeration, this searches all q-ary scalars.
        families = (
            ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)),
            ((1, 1, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1)),
            ((1, 2, 0, 0), (2, 4, 0, 0), (0, 0, 1, 0)),
            ((1, 1, 0, 0), (1, 0, 1, 0), (0, 1, 1, 0)),
        )
        for q in (5, 7, 11):
            for base in families:
                columns = tuple(tuple(x % q for x in row) for row in base)
                dependent = rank_mod_q(columns, q) < len(columns)
                brute = arbitrary_dependence_bruteforce(columns, q) is not None
                self.assertEqual(dependent, brute, (q, base))

    def test_four_column_two_vs_two_collision_nonzero_weights(self):
        # Characteristic-independent coordinate trade, but q-ary weighted.
        a, b = (1, 2, 1, 2), (2, 1, 2, 1)
        c, d = (1, 1, 2, 2), (2, 2, 1, 1)
        columns = (a, b, c, d)
        for q in (5, 7, 11):
            self.assertTrue(admissible(columns, q, 4))
            self.assertIsNotNone(direct_aset_collision(columns, q))
            self.assertIsNotNone(signed_trade(columns, q))
            self.assertEqual(tuple((a[j] + b[j] - c[j] - d[j]) % q
                                   for j in range(4)), (0,) * 4)


if __name__ == "__main__":
    unittest.main()
