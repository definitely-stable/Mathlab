"""HYP-105 G5-B: graph-only relaxation versus genuine ASET sum collisions.

Stdlib-only finite proof oracles. Infinite GQ existence comes from cited
classical geometry, NOT from finite enumeration; no original theorem claim.
"""
import collections
import itertools
import unittest


def canonical_pair_embedding(edges, left_vertices, right_vertices, left_coords, right_coords):
    """Map any finite bipartite graph to 2+2 all-one sparse vectors.

    Isolated graph vertices do not appear in the factor graph of the columns.
    Edges are pairs of 0-based graph vertex labels.
    """
    left_pairs = tuple(itertools.combinations(range(left_coords), 2))
    right_pairs = tuple(itertools.combinations(
        range(left_coords, left_coords + right_coords), 2))
    if left_vertices > len(left_pairs) or right_vertices > len(right_pairs):
        raise ValueError("not enough coordinate pairs for graph vertices")
    if len(set(edges)) != len(edges):
        raise ValueError("expected a simple bipartite graph")
    for x, y in edges:
        if not (0 <= x < left_vertices and 0 <= y < right_vertices):
            raise ValueError("edge vertex outside graph's bipartition")
    columns = tuple(tuple(sorted(left_pairs[x] + right_pairs[y]))
                    for x, y in edges)
    return columns


def recovered_factor_edges(columns):
    """Independent reconstruction of canonical first/last two signatures."""
    return {(tuple(support[:2]), tuple(support[2:])) for support in columns}


def symplectic_4(a, b):
    """Standard alternating symplectic GF(2)^4 form, 4-bit bitset encoding."""
    return (((a & 1) * ((b >> 2) & 1))
            ^ (((a >> 2) & 1) * (b & 1))
            ^ (((a >> 1) & 1) * ((b >> 3) & 1))
            ^ (((a >> 3) & 1) * ((b >> 1) & 1))) & 1


def quadrangle_w32():
    """Fifteen GF(2)^4 points and 15 isotropic projective lines."""
    lines = {
        tuple(sorted((a, b, a ^ b)))
        for a in range(1, 16) for b in range(a + 1, 16)
        if symplectic_4(a, b) == 0
    }
    # Deliberately freeze a readable, deterministic line order so the
    # four-column signed-trade fixture can be pinned by coordinates.
    lines = tuple(sorted(lines, key=lambda triple: ",".join(map(str, triple))))
    if len(lines) != 15:
        raise AssertionError("incorrect symplectic quadrangle line count")
    # L-part identifies point index 0..14; R-part a line index 0..14.
    edges = tuple((p - 1, line_index) for line_index, line in enumerate(lines)
                  for p in line)
    return lines, edges


def shortest_cycle_bipartite(edges):
    """Independent BFS girth oracle on graph labels L:x and R:y."""
    graph = collections.defaultdict(set)
    for x, y in edges:
        l, r = ("L", x), ("R", y)
        graph[l].add(r)
        graph[r].add(l)
    girth = float("inf")
    for source in graph:
        distances = {source: 0}
        parent = {source: None}
        queue = collections.deque([source])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in distances:
                    distances[nxt] = distances[node] + 1
                    parent[nxt] = node
                    queue.append(nxt)
                elif parent[node] != nxt:
                    girth = min(girth, distances[node] + distances[nxt] + 1)
    return girth


def direct_count_sum(columns, selected, modulus, coordinate_count):
    """First oracle: coordinate-by-coordinate vector construction."""
    answer = [0] * coordinate_count
    for idx in selected:
        for coord in columns[idx]:
            answer[coord] = (answer[coord] + 1) % modulus
    return tuple(answer)


def find_direct_three_sum_collision(columns, modulus, coordinate_count):
    seen = {}
    for size in range(4):
        for selected in itertools.combinations(range(len(columns)), size):
            signature = direct_count_sum(columns, selected, modulus,
                                         coordinate_count)
            if signature in seen:
                return seen[signature], selected
            seen[signature] = selected
    return None


class GirthRelaxationProofChecks(unittest.TestCase):
    def test_every_graph_on_three_by_three_vertices_is_realizable(self):
        """Exhaustive over all 512 simple bipartite graphs on 3+3 vertices."""
        universe = tuple(itertools.product(range(3), repeat=2))
        left_pairs = tuple(itertools.combinations(range(3), 2))
        right_pairs = tuple(itertools.combinations(range(3, 6), 2))
        for mask in range(1 << len(universe)):
            selected = tuple(edge for i, edge in enumerate(universe)
                             if mask & (1 << i))
            columns = canonical_pair_embedding(selected, 3, 3, 3, 3)
            self.assertEqual(len(set(columns)), len(columns))
            self.assertTrue(all(len(set(column)) == 4 for column in columns))
            graph = recovered_factor_edges(columns)
            expected = {(left_pairs[x], right_pairs[y]) for x, y in selected}
            self.assertEqual(graph, expected, (mask, selected))

    def test_w32_source_geometry_and_girth(self):
        lines, edges = quadrangle_w32()
        self.assertEqual((len(lines), len(edges)), (15, 45))
        self.assertEqual(len(set(lines)), 15)
        self.assertEqual(len(set(edges)), 45)
        self.assertTrue(all(len(set(line)) == 3 for line in lines))
        self.assertTrue(all(symplectic_4(line[0], line[1]) == 0
                            for line in lines))
        self.assertEqual({sum(x == i for x, _ in edges) for i in range(15)},
                         {3})
        self.assertEqual({sum(y == j for _, y in edges) for j in range(15)},
                         {3})
        self.assertEqual(shortest_cycle_bipartite(edges), 8)

    def test_gq_factor_graph_exactness_and_explicit_2_vs_2_trade(self):
        _, edges = quadrangle_w32()
        columns = canonical_pair_embedding(edges, 15, 15, 6, 6)
        self.assertEqual(len(columns), 45)
        self.assertEqual(len(set(columns)), 45)
        self.assertEqual(shortest_cycle_bipartite(edges), 8)
        left_pairs = tuple(itertools.combinations(range(6), 2))
        right_pairs = tuple(itertools.combinations(range(6, 12), 2))
        self.assertEqual(recovered_factor_edges(columns),
                         {(left_pairs[x], right_pairs[y]) for x, y in edges})
        self.assertFalse(any(len(set(c)) != 4 for c in columns))

        a = (2, 3, 6, 7)
        b = (0, 5, 8, 9)
        c = (0, 2, 6, 8)
        d = (3, 5, 7, 9)
        for witness in (a, b, c, d):
            self.assertIn(witness, columns)
        ia, ib, ic, id_ = tuple(columns.index(e) for e in (a, b, c, d))
        self.assertEqual(len({ia, ib, ic, id_}), 4)
        for p in (2, 3, 5, 7, 11):
            lhs = direct_count_sum(columns, (ia, ib), p, 12)
            rhs = direct_count_sum(columns, (ic, id_), p, 12)
            self.assertEqual(lhs, rhs)
            self.assertIsNotNone(find_direct_three_sum_collision(columns, p, 12))

    def test_distinct_direct_collision_vs_separate_base_five_oracle(self):
        # Both zero/one edge signatures are positive; at most three chosen
        # columns means base-five arithmetic is exact without digit carries.
        _, edges = quadrangle_w32()
        columns = canonical_pair_embedding(edges, 15, 15, 6, 6)
        radix = tuple(5 ** i for i in range(12))
        hashes = [sum(radix[coord] for coord in column) for column in columns]
        seen = {}
        found = None
        for k in range(4):
            for selection in itertools.combinations(range(len(columns)), k):
                digest = sum(hashes[i] for i in selection)
                if digest in seen:
                    found = (seen[digest], selection)
                    break
                seen[digest] = selection
            if found:
                break
        self.assertIsNotNone(found)
        self.assertEqual(
            direct_count_sum(columns, found[0], 5, 12),
            direct_count_sum(columns, found[1], 5, 12))
        self.assertEqual(
            bool(find_direct_three_sum_collision(columns, 5, 12)), True)


if __name__ == "__main__":
    unittest.main()
