"""HYP-105 G1: finite independent quadrangle and signed-sum oracles.

Does NOT independently prove infinite generalized-quadrangle existence or a new
asymptotic theorem. Mathlab-only, deterministic and stdlib-only.
"""
import itertools
import collections
import unittest


def symplectic_dot(a, b):
    # Alternating, non-degenerate bilinear form on GF(2)^4.
    return (((a >> 0 & 1) * (b >> 2 & 1)
             ^ (a >> 2 & 1) * (b >> 0 & 1)
             ^ (a >> 1 & 1) * (b >> 3 & 1)
             ^ (a >> 3 & 1) * (b >> 1 & 1)) & 1)


def w32_quadrangle_edges():
    """W(3,2): 15 points, 15 totally isotropic 2D projective lines."""
    points = range(1, 16)
    lines = sorted({tuple(sorted((a, b, a ^ b)))
                    for a in points for b in points
                    if a < b and symplectic_dot(a, b) == 0})
    assert len(lines) == 15 and all(len(set(line)) == 3 for line in lines)
    # The row indices 0..14 are points; rows 15..29 are lines.
    edges = [(p - 1, 15 + i) for i, line in enumerate(lines) for p in line]
    return 30, tuple(edges)


def graph_girth(n, edges):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    best = float("inf")
    for start in range(n):
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        queue = collections.deque([start])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if dist[v] == -1:
                    dist[v], parent[v] = dist[u] + 1, u
                    queue.append(v)
                elif v != parent[u]:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def oriented_incidence_signature(n, edges, chosen, modulus):
    values = [0] * n
    for i in chosen:
        u, v = edges[i]
        values[u] = (values[u] + 1) % modulus
        values[v] = (values[v] - 1) % modulus
    return tuple(values)


def two_part_coefficients(n, edges, chosen, modulus, left_size):
    values = [0] * n
    for i in chosen:
        u, v = edges[i]
        assert u < left_size and v >= left_size
        values[u] = (values[u] + 1) % modulus
        values[v] = (values[v] + 2) % modulus
    return tuple(values)


class Hyp105GirthTests(unittest.TestCase):
    def test_w32_girth_eight_30_nodes_45_edges(self):
        n, edges = w32_quadrangle_edges()
        self.assertEqual(n, 30)
        self.assertEqual(len(edges), 45)
        self.assertEqual(len(set(edges)), 45)
        degree = [0] * n
        for u, v in edges:
            self.assertLess(u, 15)
            self.assertGreaterEqual(v, 15)
            degree[u] += 1
            degree[v] += 1
        self.assertEqual(set(degree), {3})
        self.assertEqual(graph_girth(n, edges), 8)

    def test_all_small_active_sets_have_distinct_gf5_sums(self):
        n, edges = w32_quadrangle_edges()
        seen = {}
        for k in range(4):
            for subset in itertools.combinations(range(len(edges)), k):
                sig = oriented_incidence_signature(n, edges, subset, 5)
                self.assertNotIn(sig, seen, (subset, seen.get(sig)))
                seen[sig] = subset
        self.assertEqual(len(seen), 1 + 45 + 990 + 14190)

    def test_all_small_active_sets_have_distinct_gf2_sums(self):
        n, edges = w32_quadrangle_edges()
        seen = set()
        for k in range(4):
            for subset in itertools.combinations(range(len(edges)), k):
                sig = oriented_incidence_signature(n, edges, subset, 2)
                self.assertNotIn(sig, seen)
                seen.add(sig)

    def test_bipartite_4_6_cycles_force_same_sum(self):
        for h in (2, 3):
            # Cycle on left L_i and right R_i, alternated matchings.
            edges = []
            for i in range(h):
                edges.extend(((i, h + i), ((i + 1) % h, h + i)))
            self.assertEqual(graph_girth(2 * h, edges), 2 * h)
            first = range(0, 2 * h, 2)
            second = range(1, 2 * h, 2)
            for q in (3, 5, 7):
                self.assertEqual(two_part_coefficients(2 * h, edges, first, q, h),
                                 two_part_coefficients(2 * h, edges, second, q, h))

    def test_five_field_one_sparse_capacity_exact(self):
        for m in range(1, 5):
            columns = tuple((i, coeff) for i in range(m) for coeff in (1, 2))
            seen = set()
            for bits in itertools.product((0, 1), repeat=len(columns)):
                vec = [0] * m
                for use, (i, coeff) in zip(bits, columns):
                    if use:
                        vec[i] = (vec[i] + coeff) % 5
                sig = tuple(vec)
                self.assertNotIn(sig, seen)
                seen.add(sig)
            self.assertEqual(len(seen), 4 ** m)
        # Three scalar columns on one axis force a collision because 2^3 > 5.
        for coeffs in itertools.combinations((1, 2, 3, 4), 3):
            self.assertLess(len({sum(s) % 5 for r in range(4)
                                 for s in itertools.combinations(coeffs, r)}), 8)


if __name__ == "__main__":
    unittest.main()
