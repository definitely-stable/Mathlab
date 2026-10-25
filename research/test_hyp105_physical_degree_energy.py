"""AA4-DEG source-spectrum-to-physical-degree independent falsifiers."""
import json
import os
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_weighted_variance_transfer import (
    _physical_adj, witness_maps, w32_weighted_census,
)
from hyp105_physical_degree_energy import (
    minimal_alphabet, physical_degree_energy,
    source_spectral_projector_identity,
)


class TestPhysicalDegreeEnergy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(__file__)
        with open(os.path.join(here, "hyp105_w34_adversarial_certificate.json"),
                  encoding="utf-8") as stream:
            cls.w34 = json.load(stream)

    def test_all_h_minimal_alphabet_integer_only(self):
        for h in (1, 2, 3, 4, 12, 36, 80, 300):
            s = 1 << h
            v = (s+1)*(s*s+1)
            a = minimal_alphabet(v)
            self.assertLess((a-1)*(a-2)//2, v)
            self.assertGreaterEqual(a*(a-1)//2, v)

    def test_exact_gq_centered_spectral_projector_polynomial(self):
        # Independent exact-integer matrix certificate, no floating eigenvalues.
        for h in (1, 2):
            s = 1 << h
            _, points, lines, flags = symplectic_gq(h)
            cert = source_spectral_projector_identity(s, flags)
            v = (s+1)*(s*s+1)
            self.assertEqual(cert["V"], len(points))
            self.assertEqual(cert["V"], len(lines))
            self.assertTrue(cert["spectral_identity_verified"])
            # rank of the nontrivial positive 2s eigenspace:
            # Tr(X)=2sV * (s(s+1)^2/2).
            rank = s*(s+1)**2 // 2
            self.assertEqual(cert["tr_projector_times_2sV"], 2*s*v*rank)

    def test_true_w32_graph_degrees_against_independent_physical_adjacency(self):
        _, _, _, flags = symplectic_gq(1)
        for seed in (41, 91):
            f, g = witness_maps(seed)
            audit = physical_degree_energy(2, f, g, flags, verify_spectral=True)
            adj = _physical_adj(f, g, flags)
            for u in range(6):
                for x in range(6):
                    self.assertEqual(audit["degree_matrix"][u][x],
                                     len(adj.get((u,x), ())))
            self.assertEqual(audit["degree_sum"], 4*45)
            self.assertGreater(audit["residual_energy_upper_num_over_V2"],
                               audit["residual_energy_num_over_V2"])
            self.assertGreaterEqual(audit["pointwise_min_slack"], 0)
            self.assertLessEqual(w32_weighted_census(f, g)["P"],
                                 audit["all_three_walk_upper"])
            self.assertFalse(audit["path_chi_square_bound_proved"])

    def test_true_w34_graph_degrees_against_direct_original_flags(self):
        _, _, _, flags = symplectic_gq(2)
        f, g = self.w34["f"], self.w34["g"]
        audit = physical_degree_energy(4, f, g, flags, verify_spectral=True)
        # Independent direct physical edge-by-edge degree construction.
        direct = [[0]*14 for _ in range(14)]
        for p, l in flags:
            u, v = f[p]
            x, y = g[l]
            for a, b in (((u, x), (v, y)), ((u, y), (v, x))):
                direct[a[0]][a[1]] += 1
                direct[b[0]][b[1]] += 1
        self.assertEqual(tuple(tuple(row) for row in direct),
                         audit["degree_matrix"])
        self.assertEqual(audit["degree_sum"], 1700)
        self.assertGreaterEqual(audit["residual_energy_upper_num_over_V2"],
                                audit["residual_energy_num_over_V2"])
        self.assertGreaterEqual(audit["pointwise_min_slack"], 0)
        self.assertGreaterEqual(audit["all_three_walk_upper"], 58730)
        self.assertFalse(audit["all_h_sixth_order_bound_proved"])

    def test_physical_edge_injection_and_original_flags_fail_closed(self):
        _, _, _, flags = symplectic_gq(1)
        f, g = witness_maps(41)
        damaged_f = list(f)
        damaged_f[0] = damaged_f[1]
        with self.assertRaises(ValueError):
            physical_degree_energy(2, damaged_f, g, flags)
        with self.assertRaises(ValueError):
            physical_degree_energy(2, f, g, flags[:-1])
        with self.assertRaises(ValueError):
            physical_degree_energy(3, f, g, flags)
        with self.assertRaises(ValueError):
            physical_degree_energy(2, f, g, tuple(flags[:-1])+(flags[0],))
        with self.assertRaises(ValueError):
            minimal_alphabet(0)

    def test_independent_coordinate_permutations_preserve_centered_energy(self):
        _, _, _, flags = symplectic_gq(1)
        f, g = witness_maps(41)
        before = physical_degree_energy(2, f, g, flags)
        after_f = [tuple(sorted(((5*x+1)%6, (5*y+1)%6))) for x, y in f]
        after_g = [tuple(sorted(((5*x+2)%6, (5*y+2)%6))) for x, y in g]
        after = physical_degree_energy(2, after_f, after_g, flags)
        for k in ("residual_energy_num_over_V2",
                  "residual_energy_upper_num_over_V2",
                  "degree_square_sum", "max_corner_degree", "pointwise_min_slack",
                  "all_three_walk_upper"):
            self.assertEqual(after[k], before[k])


if __name__ == "__main__":
    unittest.main()
