"""HYP-105 G4: uniformity/characteristic boundary and GF(3) signed obstructions.

All checks are finite independent input oracles, not a new cryptographic
algorithm or a proof of an asymptotic Turan density theorem.
"""
import itertools
import unittest

from hyp105_minor import core_patterns, is_grid


def linear_uniform(edges, size):
    return all(len(set(e)) == size for e in edges) and all(
        len(set(a) & set(b)) <= 1
        for a, b in itertools.combinations(edges, 2)
    )


def unit_sum(edges, chosen, field, vertices):
    vector = [0] * vertices
    for index in chosen:
        for v in edges[index]:
            vector[v] = (vector[v] + 1) % field
    return tuple(vector)


def colliding_subsets(edges, field, activity, vertices):
    """Oracle A: actual vector sums across all sets of sizes 0..activity."""
    previous = {}
    for k in range(min(activity, len(edges)) + 1):
        for indices in itertools.combinations(range(len(edges)), k):
            signature = unit_sum(edges, indices, field, vertices)
            if signature in previous:
                return previous[signature], indices
            previous[signature] = indices
    return None


def coned_grid(prime):
    """Linear (p+1)-uniform hypergraph: p rows, p cols, two hubs."""
    grid = prime * prime
    edges = []
    for i in range(prime):
        edges.append(tuple(sorted((grid,) + tuple(
            i * prime + j for j in range(prime)))))
    for j in range(prime):
        edges.append(tuple(sorted((grid + 1,) + tuple(
            i * prime + j for i in range(prime)))))
    return grid + 2, tuple(edges)


def binary_four_uniform():
    """K6 minus a perfect matching, vertices become size-four edges."""
    removed = {(0, 1), (2, 3), (4, 5)}
    auxiliary = [
        (i, j) for i in range(6) for j in range(i + 1, 6)
        if (i, j) not in removed
    ]
    assert len(auxiliary) == 12
    original_edges = tuple(
        tuple(index for index, pair in enumerate(auxiliary) if i in pair)
        for i in range(6)
    )
    return 12, original_edges


def four_partite_affine(order):
    """For order=3, four mutually orthogonal coordinate expressions."""
    edges = []
    for x in range(order):
        for y in range(order):
            edges.append((
                x, order + y,
                2 * order + (x + y) % order,
                3 * order + (x + 2 * y) % order,
            ))
    return 4 * order, tuple(edges)


def signed_assignments(rows, count, prime, max_side=3):
    """Oracle B: exact +/-1 balanced witness, independent of integer minors."""
    assignments = []
    for mask in range(1 << count):
        plus = mask.bit_count()
        minus = count - plus
        if plus > max_side or minus > max_side:
            continue
        if all(sum(1 if mask & (1 << i) else -1
                   for i in range(count) if row & (1 << i)) % prime == 0
               for row in rows):
            assignments.append(mask)
    return tuple(assignments)


def direct_sums_on_core(rows, count, prime):
    """Oracle C: direct subset-sum enumeration independent of +/-1 assignments."""
    cols = [
        tuple(v for v, mask in enumerate(rows) if mask & (1 << i))
        for i in range(count)
    ]
    return colliding_subsets(cols, prime, 3, len(rows)) is not None


class UniformityAndCharacteristicTests(unittest.TestCase):
    def test_universal_coned_grid_witness_all_small_prime_fields(self):
        for p in (2, 3, 5):
            vertices, edges = coned_grid(p)
            self.assertTrue(linear_uniform(edges, p + 1))
            left = tuple(range(p))
            right = tuple(range(p, 2 * p))
            self.assertEqual(
                unit_sum(edges, left, p, vertices),
                unit_sum(edges, right, p, vertices))
            self.assertIsNotNone(colliding_subsets(edges, p, p, vertices))

    def test_gf3_coned_grid_is_safe_in_characteristic_five_at_activity_three(self):
        v, edges = coned_grid(3)
        self.assertEqual(v, 11)
        self.assertEqual(len(edges), 6)
        self.assertTrue(linear_uniform(edges, 4))
        self.assertIsNotNone(colliding_subsets(edges, 3, 3, v))
        for p in (5, 7, 11):
            self.assertIsNone(colliding_subsets(edges, p, 3, v))

    def test_gf2_six_column_four_uniform_collision(self):
        v, edges = binary_four_uniform()
        self.assertEqual((v, len(edges)), (12, 6))
        self.assertTrue(linear_uniform(edges, 4))
        self.assertEqual(unit_sum(edges, (0, 1, 2), 2, v),
                         unit_sum(edges, (3, 4, 5), 2, v))
        for p in (5, 7):
            self.assertIsNone(colliding_subsets(edges, p, 3, v))

    def test_affine_four_partite_linear_family_under_all_odd_large_characteristics(self):
        vertices, edges = four_partite_affine(3)
        self.assertEqual((vertices, len(edges)), (12, 9))
        self.assertTrue(linear_uniform(edges, 4))
        for p in (5, 7, 11):
            self.assertIsNone(colliding_subsets(edges, p, 3, vertices))

    def test_gf3_five_edge_three_against_two_without_grid(self):
        edges = ((0, 1, 2), (0, 3, 4), (1, 3, 5),
                 (2, 3, 6), (4, 5, 6))
        self.assertTrue(linear_uniform(edges, 3))
        self.assertEqual(unit_sum(edges, (0, 4), 3, 7),
                         unit_sum(edges, (1, 2, 3), 3, 7))
        self.assertIsNotNone(colliding_subsets(edges, 3, 3, 7))
        self.assertIsNone(colliding_subsets(edges, 5, 3, 7))

    def test_complete_gf3_signed_core_census_and_independent_direct_oracle(self):
        hist = {}
        grids = 0
        for t in range(1, 7):
            ncores = 0
            signed = 0
            for rows in core_patterns(t):
                signs = signed_assignments(rows, t, 3)
                direct = direct_sums_on_core(rows, t, 3)
                self.assertEqual(bool(signs), direct, (t, rows, signs))
                self.assertEqual(len(signs), 2 if signs else 0)
                if signs:
                    signed += 1
                if t == 6 and is_grid(rows, t):
                    grids += 1
                    self.assertTrue(signs)
                ncores += 1
            hist[t] = (ncores, signed)
        self.assertEqual(hist, {
            1: (0, 0), 2: (0, 0), 3: (0, 0),
            4: (1, 0), 5: (10, 10), 6: (520, 70),
        })
        self.assertEqual(grids, 10)


if __name__ == "__main__":
    unittest.main()
