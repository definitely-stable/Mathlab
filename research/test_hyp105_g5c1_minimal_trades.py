"""HYP-105 G5-C1: minimal signed-trade localization and split-pair circuits.

Exact finite examples and independent finite oracles; no asymptotic exponent
claim. The mathematical arguments are in docs/research/HYP-105-G5-C1-TRADES.md.
Only prime fields are used in this stdlib harness.
"""
import itertools
import unittest

from test_hyp105_g5c_signed_oracles import (direct_aset_collision, signed_trade, rank_mod_q)


def all_signed_relations(columns, prime=5, activity=3):
    """Oracle 1: physical disjoint positive/negative subset enumeration."""
    n = len(columns)
    m = len(columns[0]) if n else 0
    for left_size in range(activity + 1):
        for right_size in range(activity + 1):
            if left_size + right_size == 0 or left_size + right_size > n:
                continue
            for plus in itertools.combinations(range(n), left_size):
                available = tuple(i for i in range(n) if i not in plus)
                for minus in itertools.combinations(available, right_size):
                    if all(
                        (sum(columns[i][j] for i in plus) -
                         sum(columns[i][j] for i in minus)) % prime == 0
                        for j in range(m)
                    ):
                        yield plus, minus


def support_incidence(columns, selected):
    """Count support degrees, independently of field arithmetic."""
    result = {}
    for i in selected:
        for j, value in enumerate(columns[i]):
            if value:
                result[j] = result.get(j, 0) + 1
    return result


def incidence_components(columns, selected):
    """Bipartite column/coordinate support graph: component column IDs."""
    selected = set(selected)
    remaining = set(selected)
    coords = {i: {j for j, x in enumerate(columns[i]) if x} for i in selected}
    result = []
    while remaining:
        start = min(remaining)
        seen_cols = {start}
        seen_coords = set(coords[start])
        changed = True
        while changed:
            changed = False
            for idx in sorted(remaining - seen_cols):
                if coords[idx] & seen_coords:
                    seen_cols.add(idx)
                    seen_coords.update(coords[idx])
                    changed = True
        result.append(tuple(sorted(seen_cols)))
        remaining -= seen_cols
    return tuple(result)


def is_minimal_trade(columns, plus, minus, prime=5, activity=3):
    """Oracle 2: explicit proper-relation subpattern search, no rank argument.

    A trade with a proper nonzero subset that itself sums to zero cannot be
    support-minimal, even if that subpattern uses different +/- signs.
    """
    selected = tuple(sorted(set(plus) | set(minus)))
    if len(selected) == 0 or set(plus) & set(minus):
        return False
    m = len(columns[0]) if columns else 0
    if any((sum(columns[i][j] for i in plus) -
            sum(columns[i][j] for i in minus)) % prime
           for j in range(m)):
        return False
    for size in range(1, len(selected)):
        for sub in itertools.combinations(selected, size):
            subcols = tuple(columns[i] for i in sub)
            if direct_aset_collision(subcols, prime, activity) is not None:
                return False
    return True


def pair_projection_circuits(columns, plus, minus, coords):
    """A combinatorial (NOT modular-algebra) exact alternating circuit cover.

    All selected columns must be 0/1, with exactly two ones in the given
    coordinates. Balanced endpoints pair +ports to -ports. Each halfedge
    gets a partner, and the resulting 2-regular multigraph on column-edges
    decomposes into alternating circuits of length 2,4,6 if <=3 on each side.
    Returns None if the projection cannot satisfy integer degree balance.
    """
    selected = tuple(sorted(set(plus) | set(minus)))
    if not selected or set(plus) & set(minus):
        return None
    plus = set(plus)
    minus = set(minus)
    coords = tuple(coords)
    pairs = {}
    pos = {v: [] for v in coords}
    neg = {v: [] for v in coords}
    for idx in selected:
        vec = columns[idx]
        if any(vec[j] not in (0, 1) for j in coords):
            raise ValueError("unit input required for pair circuit oracle")
        edge = tuple(v for v in coords if vec[v])
        if len(edge) != 2:
            raise ValueError("exactly two nonzero projection coordinates needed")
        pairs[idx] = edge
        target = pos if idx in plus else neg
        for v in edge:
            target[v].append(idx)
    partner = {}
    for v in coords:
        if len(pos[v]) != len(neg[v]):
            return None
        for red, blue in zip(sorted(pos[v]), sorted(neg[v])):
            partner[red, v] = blue
            partner[blue, v] = red

    remaining = set(selected)
    circuits = []
    while remaining:
        start = min(remaining)
        entered = pairs[start][0]
        idx = start
        cycle = []
        while True:
            assert idx in remaining, ("port pairing reused edge", idx)
            remaining.remove(idx)
            cycle.append(idx)
            a, b = pairs[idx]
            exit_vertex = b if entered == a else a
            following = partner[idx, exit_vertex]
            if following == start:
                assert exit_vertex == pairs[start][0]
                break
            entered = exit_vertex
            idx = following
        assert len(cycle) % 2 == 0
        assert all((cycle[k] in plus) != (cycle[(k + 1) % len(cycle)] in plus)
                   for k in range(len(cycle)))
        circuits.append(tuple(cycle))
    return tuple(circuits)


def double_cycle_fixture(length):
    """Unit exact-weight-4 global split: two identical L/R even cycles."""
    if length not in (4, 6):
        raise ValueError(length)
    m = 2 * length
    columns = []
    for i in range(length):
        col = [0] * m
        for j in (i, (i + 1) % length, length + i,
                  length + (i + 1) % length):
            col[j] = 1
        columns.append(tuple(col))
    return tuple(columns)


def weighted_unbalanced_fixture():
    """Exact weight4 GF5 trade 1-versus-2, maximally six live coordinates."""
    a = (1, 1, 1, 1, 0, 0)
    b = (1, 1, 0, 0, 1, 1)
    c = (0, 0, 1, 1, 4, 4)
    return a, b, c


def uniform_one_family_has_only_balanced_trades(columns, prime=5):
    """Checks every disjoint exact relation, including unequal sizes."""
    for plus, minus in all_signed_relations(columns, prime):
        if len(plus) != len(minus):
            return False
    return True


class HYP105G5C1TradeLocality(unittest.TestCase):
    def test_exact_four_support_unbalanced_trade_maximal_union_six(self):
        columns = weighted_unbalanced_fixture()
        self.assertEqual(tuple(sum(x != 0 for x in c) for c in columns),
                         (4, 4, 4))
        self.assertEqual(
            tuple((columns[1][j] + columns[2][j] - columns[0][j]) % 5
                  for j in range(6)), (0,) * 6)
        self.assertEqual(set(support_incidence(columns, range(3)).values()), {2})
        self.assertEqual(len(support_incidence(columns, range(3))), 6)
        self.assertTrue(is_minimal_trade(columns, (0,), (1, 2)))
        self.assertEqual(len(incidence_components(columns, range(3))), 1)
        self.assertIsNotNone(direct_aset_collision(columns, 5))
        self.assertIsNotNone(signed_trade(columns, 5))

    def test_gf5_minimal_three_vs_two_full_weight_four(self):
        # The four initial columns span F5^4. The fifth column creates
        # the unique (up to scalar) 5-column linear circuit a+b+c-d-e=0.
        # Thus this is a truly MINIMAL 3-vs-2 weighted obstruction,
        # not a 3-vs-2 superposition of a smaller 1-vs-2 trade.
        columns = (
            (3, 1, 1, 1),
            (1, 3, 1, 1),
            (1, 1, 3, 1),
            (1, 1, 1, 4),
            (4, 4, 4, 4),
        )
        self.assertEqual(rank_mod_q(columns[:4], 5), 4)
        self.assertEqual(rank_mod_q(columns, 5), 4)
        self.assertEqual(len(set(columns)), 5)
        self.assertTrue(all(all(x for x in row) for row in columns))
        self.assertEqual(
            tuple(sum(columns[i][j] for i in range(3)) % 5 for j in range(4)),
            tuple(sum(columns[i][j] for i in (3, 4)) % 5 for j in range(4)))
        self.assertTrue(is_minimal_trade(columns, (0, 1, 2), (3, 4)))
        self.assertEqual(incidence_components(columns, range(5)),
                         (tuple(range(5)),))
        self.assertIsNotNone(direct_aset_collision(columns, 5))
        self.assertIsNotNone(signed_trade(columns, 5))
        relations = set(all_signed_relations(columns, 5))
        self.assertEqual(relations,
                         {((0, 1, 2), (3, 4)), ((3, 4), (0, 1, 2))})

    def test_exact_minimal_2v2_and_3v3_sharp_localization(self):
        for length in (4, 6):
            columns = double_cycle_fixture(length)
            plus = tuple(range(0, length, 2))
            minus = tuple(range(1, length, 2))
            degree = support_incidence(columns, range(length))
            self.assertEqual(len(degree), 2 * length)
            self.assertEqual(set(degree.values()), {2})
            self.assertEqual(incidence_components(columns, range(length)),
                             (tuple(range(length)),))
            self.assertTrue(is_minimal_trade(columns, plus, minus),
                            (length, tuple(all_signed_relations(columns))))
            self.assertEqual(
                tuple(sum(columns[i][j] for i in plus) % 5
                      for j in range(2 * length)),
                tuple(sum(columns[i][j] for i in minus) % 5
                      for j in range(2 * length)))
            left = pair_projection_circuits(
                columns, plus, minus, range(length))
            right = pair_projection_circuits(
                columns, plus, minus, range(length, 2 * length))
            self.assertEqual(left is not None, True)
            self.assertEqual(right is not None, True)
            self.assertEqual(sorted(map(len, left)), [length])
            self.assertEqual(sorted(map(len, right)), [length])
            # The canonical weighted pair *factor graph* is only a matching.
            edgepairs = {(tuple(j for j in range(length) if col[j]),
                          tuple(j for j in range(length, 2 * length) if col[j]))
                         for col in columns}
            self.assertEqual(len(edgepairs), length)

    def test_signed_trade_singleton_free_and_connected_if_minimal(self):
        # All 0/1 supports of length 4, 2/3-element families over GF5.
        # Exhaustively check the claimed implications for small tiny cases.
        pool = tuple(tuple(1 if j in subset else 0 for j in range(4))
                     for r in range(1, 5)
                     for subset in itertools.combinations(range(4), r))
        checked = 0
        for length in range(2, 4):
            for columns in itertools.combinations(pool, length):
                for plus, minus in all_signed_relations(columns):
                    selected = set(plus) | set(minus)
                    degree = support_incidence(columns, selected)
                    self.assertTrue(all(d >= 2 for d in degree.values()))
                    self.assertLessEqual(len(degree), 2 * len(selected))
                    if is_minimal_trade(columns, plus, minus):
                        self.assertEqual(
                            len(incidence_components(columns, selected)), 1)
                    checked += 1
        self.assertGreater(checked, 0)

    def test_all_one_exact_four_balanced_but_weighted_not(self):
        weighted = weighted_unbalanced_fixture()
        self.assertIn(((0,), (1, 2)), set(all_signed_relations(weighted, 5)))
        for n in (4, 6):
            family = double_cycle_fixture(n)
            self.assertTrue(uniform_one_family_has_only_balanced_trades(family))
            # Characteristic 3 no longer distinguishes sizes differing by 3:
            # three disjoint all-one columns can sum to zero in GF3
            # if their supports are identical -- distinctness is irrelevant
            # for demonstrating why the counting proof needs p>3.
        # Separate direct modular cardinality identity for each size.
        self.assertTrue(all((4 * a - 4 * b) % 5 != 0
                            for a in range(4) for b in range(4) if a != b))
        self.assertEqual((4 * 3) % 3, 0)

    def test_split_circuit_cover_agrees_with_actual_unit_projection_sum(self):
        # Independently compare integer full projection vector equality
        # against graph half-edge alternating-circuit decomposition.
        pool = []
        left_pairs = tuple(itertools.combinations(range(4), 2))
        right_pairs = tuple(itertools.combinations(range(4, 8), 2))
        for l in left_pairs[:4]:
            for r in right_pairs[:3]:
                vec = [0] * 8
                for j in l + r:
                    vec[j] = 1
                pool.append(tuple(vec))
        pool = tuple(pool)
        runs = 0
        for idxs in itertools.combinations(range(len(pool)), 4):
            cols = tuple(pool[i] for i in idxs)
            for plus in itertools.combinations(range(4), 2):
                minus = tuple(i for i in range(4) if i not in plus)
                for coords in (range(4), range(4, 8)):
                    direct = all(
                        sum(cols[i][j] for i in plus) ==
                        sum(cols[i][j] for i in minus)
                        for j in coords)
                    circuits = pair_projection_circuits(
                        cols, plus, minus, coords)
                    self.assertEqual(circuits is not None, direct)
                    if circuits is not None:
                        self.assertTrue(all(len(c) in (2, 4)
                                            for c in circuits))
                    runs += 1
        self.assertGreater(runs, 900)

    def test_separate_pair_projections_required(self):
        # A valid alternating circuit in P does not imply an equal sum in Q.
        cols = double_cycle_fixture(4)
        cols = tuple(
            tuple(list(vec[:4]) + list(vec[4:])) if i != 3 else
            tuple(list(vec[:4]) + [1, 1, 0, 0])
            for i, vec in enumerate(cols)
        )
        plus, minus = (0, 2), (1, 3)
        self.assertIsNotNone(pair_projection_circuits(cols, plus, minus, range(4)))
        self.assertIsNone(pair_projection_circuits(cols, plus, minus, range(4, 8)))
        self.assertNotEqual(
            tuple(sum(cols[i][j] for i in plus) for j in range(8)),
            tuple(sum(cols[i][j] for i in minus) for j in range(8)))


if __name__ == "__main__":
    unittest.main()
