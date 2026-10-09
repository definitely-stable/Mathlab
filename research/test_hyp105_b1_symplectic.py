"""Independent falsification of W(3,2), W(3,4) algebraic incidence."""
import unittest
from itertools import combinations
from hyp105_b1_symplectic import (
    GF2Power, exact_gq_certificate, projective_points, symplectic,
    symplectic_gq, normalized, span_projective_line
)
from test_hyp105_g5b_graph_realization import (
    quadrangle_w32, shortest_cycle_bipartite
)


class G5C3B10SymplecticTests(unittest.TestCase):
    def test_extension_field_not_integer_mod_four(self):
        f = GF2Power(2)
        self.assertEqual(f.add(2, 2), 0)
        self.assertEqual(f.mul(2, 2), 3)
        self.assertEqual(f.mul(2, 3), 1)
        self.assertEqual(f.mul(3, 3), 2)
        self.assertEqual({f.mul(2, k) for k in (1, 2, 3)}, {1, 2, 3})
        for h in (1, 2, 3, 4):
            g = GF2Power(h)
            for a in range(1, g.q):
                self.assertEqual(g.mul(a, g.inv(a)), 1)
                self.assertEqual(g.mul(a, 0), 0)
                self.assertEqual(g.mul(a, 1), a)
                self.assertEqual(g.add(a, a), 0)
        for bad in (-1, 4, 100):
            with self.assertRaises(ValueError):
                f.mul(bad, 1)
        with self.assertRaises(ZeroDivisionError):
            f.inv(0)
        with self.assertRaises(ValueError):
            GF2Power(5)

    def test_projective_normalization_scalar_orbits_and_symplectic_axioms(self):
        for h in (1, 2):
            f = GF2Power(h)
            pts = projective_points(f)
            self.assertEqual(len(pts), (f.q + 1) * (f.q*f.q + 1))
            self.assertEqual(len(set(pts)), len(pts))
            for p in pts:
                self.assertEqual(next(x for x in p if x), 1)
                self.assertEqual(symplectic(p, p, f), 0)
                for k in range(1, f.q):
                    scalar = tuple(f.mul(x, k) for x in p)
                    self.assertEqual(normalized(scalar, f), p)
            for i, u in enumerate(pts[:25]):
                for v in pts[:25]:
                    self.assertEqual(symplectic(u, v, f),
                                     symplectic(v, u, f))
        with self.assertRaises(ValueError):
            normalized((0, 0, 0, 0), GF2Power(2))

    def test_classical_projective_gq_point_line_counts_and_girth(self):
        for h, expected in ((1, (15, 15, 45, 3)),
                            (2, (85, 85, 425, 5))):
            field, points, lines, edges = symplectic_gq(h)
            self.assertEqual((len(points), len(lines), len(edges), field.q + 1),
                             expected)
            self.assertEqual(len(set(lines)), len(lines))
            self.assertEqual(shortest_cycle_bipartite(edges), 8)
            self.assertEqual(exact_gq_certificate(h)["incidences"], expected[2])
            # Independent combinatorial projective GQ axiom: for a point
            # outside a line, exactly ONE point of the line is perpendicular.
            for u, p in enumerate(points):
                for line in lines:
                    if u not in line:
                        orthogonal = sum(symplectic(p, points[v], field) == 0
                                         for v in line)
                        self.assertEqual(orthogonal, 1, (h, u, line))

    def test_gf2_lines_match_independent_previous_w32_fixture(self):
        _, points, lines, _ = symplectic_gq(1)
        previous, previous_edges = quadrangle_w32()
        previous_set = set(map(frozenset, previous))
        our_set = {
            frozenset(sum(value << shift for shift, value
                          in enumerate(points[i]))
                      for i in line)
            for line in lines
        }
        self.assertEqual(previous_set, our_set)
        self.assertEqual(len(previous_edges), 45)

    def test_negative_nonisotropic_and_repeat_line_generators(self):
        field, points, _, _ = symplectic_gq(2)
        with self.assertRaises(ValueError):
            span_projective_line(points[0], points[0], field)
        pair = next((u, v) for u, v in combinations(points, 2)
                    if symplectic(u, v, field) != 0)
        with self.assertRaises(ValueError):
            span_projective_line(*pair, field)


if __name__ == "__main__":
    unittest.main()
