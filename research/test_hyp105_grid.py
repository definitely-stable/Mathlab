"""HYP-105 G2: finite independent grid vs 3-sum injectivity oracles.

For linear 3-uniform hypergraphs and characteristic >=5 only.
Published infinite dense grid-free construction is NOT proved by these tests.
"""
from itertools import combinations
import unittest


def ag23():
    """Twelve affine lines on 9 points, computed from GF(3)^2 coordinates."""
    lines = set()
    directions = ((1, 0), (0, 1), (1, 1), (1, 2))
    for dx, dy in directions:
        for x in range(3):
            for y in range(3):
                line = frozenset((3 * ((x + t * dx) % 3)
                                   + ((y + t * dy) % 3)) for t in range(3))
                lines.add(tuple(sorted(line)))
    return tuple(sorted(lines))


def linearm3(lines):
    return all(len(set(a) & set(b)) <= 1
               for a, b in combinations(lines, 2))


def grid_trade_masks(lines):
    """Independent structural grid oracle, not based on subset sums."""
    all_masks = set()
    for left in combinations(range(len(lines)), 3):
        if not all(set(lines[i]).isdisjoint(lines[j])
                   for i, j in combinations(left, 2)):
            continue
        others = [i for i in range(len(lines)) if i not in left]
        for right in combinations(others, 3):
            if not all(set(lines[i]).isdisjoint(lines[j])
                       for i, j in combinations(right, 2)):
                continue
            if all(len(set(lines[i]) & set(lines[j])) == 1
                   for i in left for j in right):
                all_masks.add(sum(1 << k for k in (*left, *right)))
    return tuple(sorted(all_masks))


def sum_signature(edges, indices, modulus, n=9):
    """Fresh count array reduced in GF(modulus), entirely separate from grid."""
    vec = [0] * n
    for i in indices:
        for point in edges[i]:
            vec[point] = (vec[point] + 1) % modulus
    return tuple(vec)


def has_sum_collision(edges, selected, modulus):
    """Independent direct subset-sum algorithm incl. all cardinalities 0..3."""
    seen = set()
    for k in range(min(3, len(selected)) + 1):
        for subset in combinations(selected, k):
            val = sum_signature(edges, subset, modulus)
            if val in seen:
                return True
            seen.add(val)
    return False


def fast_sum_collision_gf5(edges, selected):
    """Independent radix-5 count packing, valid for <=3 unit triples."""
    power = [5**j for j in range(9)]
    code = [sum(power[k] for k in e) for e in edges]
    seen = {0}
    for k in range(1, min(3, len(selected)) + 1):
        for subset in combinations(selected, k):
            value = sum(code[i] for i in subset)
            if value in seen:
                return True
            seen.add(value)
    return False


class GridThreeSums(unittest.TestCase):
    def test_affine_plane_linear_and_four_parallel_classes(self):
        edges = ag23()
        self.assertEqual(len(edges), 12)
        self.assertTrue(linearm3(edges))
        self.assertEqual(len(set(e for e in edges)), 12)
        point_degrees = [sum(j in e for e in edges) for j in range(9)]
        self.assertEqual(point_degrees, [4] * 9)
        self.assertEqual(len(grid_trade_masks(edges)), 6)

    def test_every_4096_subfamily_grid_iff_sum_collision_in_gf5(self):
        edges = ag23()
        grid_masks = grid_trade_masks(edges)
        self.assertEqual(len(grid_masks), 6)
        for mask in range(1 << 12):
            selected = tuple(i for i in range(12) if mask & (1 << i))
            structural = any((mask & grid) == grid for grid in grid_masks)
            numeric = fast_sum_collision_gf5(edges, selected)
            self.assertEqual(numeric, structural, (mask, structural, numeric))
        for mask in (0, (1 << 12) - 1, grid_masks[0]):
            selected = tuple(i for i in range(12) if mask & (1 << i))
            self.assertEqual(has_sum_collision(edges, selected, 5),
                             fast_sum_collision_gf5(edges, selected))

    def test_concrete_six_column_signed_grid_trade(self):
        edges = ag23()
        mask = grid_trade_masks(edges)[0]
        included = [i for i in range(12) if mask & (1 << i)]
        left = right = None
        for combo in combinations(included, 3):
            remaining = [i for i in included if i not in combo]
            if all(set(edges[i]).isdisjoint(edges[j])
                   for i, j in combinations(combo, 2)):
                if all(set(edges[i]).isdisjoint(edges[j])
                       for i, j in combinations(remaining, 2)):
                    left, right = combo, remaining
                    break
        self.assertIsNotNone(left)
        self.assertEqual(sum_signature(edges, left, 5),
                         sum_signature(edges, right, 5))
        self.assertEqual(sum_signature(edges, left, 5), (1,) * 9)

    def test_characteristic_three_grid_free_five_edge_counterexample(self):
        # Choose three distinct lines through point 0; their other six
        # points are the union of two parallel lines avoiding the fourth
        # through-0 line. In GF(3) three copies of center=0 vanish.
        edges = ag23()
        origin_lines = [i for i, e in enumerate(edges) if 0 in e]
        self.assertEqual(len(origin_lines), 4)
        self.assertEqual(len(grid_trade_masks(edges)), 6)
        found = None
        for centers in combinations(origin_lines, 3):
            exposed = {p for i in centers for p in edges[i]} - {0}
            for rhs in combinations(range(12), 2):
                if any(0 in edges[i] for i in rhs):
                    continue
                if set(edges[rhs[0]]) | set(edges[rhs[1]]) == exposed:
                    found = (*centers, *rhs)
                    break
            if found:
                break
        self.assertIsNotNone(found)
        self.assertEqual(len(set(found)), 5)
        chosen = tuple(found)
        self.assertFalse(any((sum(1 << i for i in chosen) & g) == g
                             for g in grid_trade_masks(edges)))
        self.assertEqual(sum_signature(edges, chosen[:3], 3),
                         sum_signature(edges, chosen[3:], 3))
        self.assertNotEqual(sum_signature(edges, chosen[:3], 5),
                            sum_signature(edges, chosen[3:], 5))

    def test_fano_7_point_plane_grid_free_gf5_aset(self):
        # Seven lines of Fano plane: (a,b,a XOR b) over GF(2)^3.
        edges = tuple(sorted({tuple(sorted((a-1, b-1, (a^b)-1)))
                              for a in range(1, 8) for b in range(a+1, 8)}))
        self.assertEqual(len(edges), 7)
        self.assertTrue(linearm3(edges))
        self.assertEqual(grid_trade_masks(edges), ())
        # The general reference array method supports 7 vertices.
        self.assertFalse(has_sum_collision(edges, tuple(range(7)), 5))


if __name__ == "__main__":
    unittest.main()
