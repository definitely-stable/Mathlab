"""HYP-105 G5-A: graph girth necessary but not sufficient for 3-sums.

Two truly distinct oracles: direct all-subsets sums vs constrained signed
projection kernels; no externally downloaded deps, stdlib-only and deterministic.
"""
import itertools
import unittest


def doubled_six_cycle():
    # Six columns on 12 disjoint-coordinate halves.
    return tuple(tuple(sorted((i, (i+1) % 6, 6+i, 6+(i+1) % 6)))
                 for i in range(6))


def direct_sums(columns, indices, modulus, m):
    vec = [0] * m
    for i in indices:
        for coord in columns[i]:
            vec[coord] = (vec[coord] + 1) % modulus
    return tuple(vec)


def direct_collision(columns, modulus, activity, m):
    known = {}
    for d in range(min(activity, len(columns)) + 1):
        for subset in itertools.combinations(range(len(columns)), d):
            value = direct_sums(columns, subset, modulus, m)
            if value in known:
                return known[value], subset
            known[value] = subset
    return None


def factor_graph_edges(columns):
    # Canonical two smallest/two largest coordinates, all weights=1.
    return tuple((tuple(c[:2]), tuple(c[2:])) for c in columns)


def has_graph_cycle(edges):
    # Independent bipartite DFS cycle detector, tags keep left/right apart.
    nbr = {}
    for left, right in edges:
        u, v = ("L", left), ("R", right)
        nbr.setdefault(u, set()).add(v)
        nbr.setdefault(v, set()).add(u)
    for start in nbr:
        visited = set()
        def walk(v, parent):
            visited.add(v)
            for x in nbr[v]:
                if x == parent:
                    continue
                if x in visited or walk(x, v):
                    return True
            return False
        if start not in visited and walk(start, None):
            return True
    return False


def projected_trade_overlap(columns, modulus, activity, cut, m):
    # Independent +/-1 kernel search: the left and right sums must both vanish.
    n = len(columns)
    for signs in itertools.product((-1, 0, 1), repeat=n):
        if not any(signs):
            continue
        if signs.count(1) > activity or signs.count(-1) > activity:
            continue
        left = [0] * cut
        right = [0] * (m-cut)
        for i, sign in enumerate(signs):
            if not sign:
                continue
            for j in columns[i]:
                if j < cut:
                    left[j] = (left[j] + sign) % modulus
                else:
                    right[j-cut] = (right[j-cut] + sign) % modulus
        if not any(left) and not any(right):
            return True
    return False


def distinct_unions(columns, activity):
    known = set()
    for r in range(min(activity, len(columns)) + 1):
        for indices in itertools.combinations(range(len(columns)), r):
            key = frozenset(k for i in indices for k in columns[i])
            if key in known:
                return False
            known.add(key)
    return True


class TradeIntersectionTests(unittest.TestCase):
    def test_matching_factor_graph_still_collides_in_every_field(self):
        cols = doubled_six_cycle()
        self.assertEqual(len(cols), 6)
        self.assertEqual(len(set(cols)), 6)
        self.assertTrue(all(len(set(c)) == 4 for c in cols))
        self.assertTrue(all(len(c[:2]) == 2 and max(c[:2]) < 6
                            and min(c[2:]) >= 6 for c in cols))
        factor = factor_graph_edges(cols)
        self.assertEqual(len(set(x for x, _ in factor)), 6)
        self.assertEqual(len(set(y for _, y in factor)), 6)
        self.assertFalse(has_graph_cycle(factor))
        for p in (2, 3, 5, 7, 11):
            self.assertEqual(
                direct_sums(cols, (0, 2, 4), p, 12),
                direct_sums(cols, (1, 3, 5), p, 12))
            self.assertEqual(direct_sums(cols, (0, 2, 4), p, 12),
                             (1,) * 12)
            self.assertIsNotNone(direct_collision(cols, p, 3, 12))
            self.assertTrue(projected_trade_overlap(cols, p, 3, 6, 12))

    def test_exhaustive_separated_projection_criterion(self):
        # Forty-five local cases on two disjoint 4-coordinate blocks.
        # Vary size 0..4, direct all-subsets independently from signs.
        pairs = tuple(itertools.combinations(range(4), 2))
        right_pairs = tuple(tuple(x+4 for x in p) for p in pairs)
        pool = tuple(tuple(a+b) for a in pairs[:3] for b in right_pairs[:3])
        self.assertEqual(len(pool), 9)
        runs = 0
        for n in range(5):
            for selection in itertools.combinations(pool, n):
                for p in (2, 3, 5, 7):
                    truth = direct_collision(selection, p, 3, 8) is not None
                    kernel = projected_trade_overlap(selection, p, 3, 4, 8)
                    self.assertEqual(truth, kernel, (selection, p))
                    runs += 1
        self.assertGreater(runs, 1000)

    def test_four_uniform_triangle_is_aset_but_not_union_free(self):
        cols = ((0, 1, 3, 4), (1, 2, 3, 4), (0, 2, 3, 4))
        self.assertTrue(all(len(c) == 4 for c in cols))
        self.assertIsNone(direct_collision(cols, 5, 3, 5))
        self.assertFalse(distinct_unions(cols, 3))
        unions = [frozenset(cols[i]).union(cols[j])
                  for i, j in itertools.combinations(range(3), 2)]
        self.assertEqual(len(set(unions)), 1)
        self.assertEqual(unions[0], frozenset(range(5)))

    def test_graph_cycle_witness_is_detected_by_both_oracles(self):
        # Two factor-graph cycles with independent left/right pair coordinates.
        for h in (2, 3):
            left = [(2*i, 2*i+1) for i in range(h)]
            right = [(2*h+2*i, 2*h+2*i+1) for i in range(h)]
            cols = tuple(tuple(sorted(left[i] + right[i]))
                         for i in range(h)) + tuple(
                             tuple(sorted(left[(i+1) % h] + right[i]))
                             for i in range(h))
            factor = factor_graph_edges(cols)
            self.assertTrue(has_graph_cycle(factor))
            for p in (2, 3, 5):
                self.assertIsNotNone(direct_collision(cols, p, h, 4*h))
                self.assertTrue(projected_trade_overlap(cols, p, h,
                                                        2*h, 4*h))


if __name__ == "__main__":
    unittest.main()
