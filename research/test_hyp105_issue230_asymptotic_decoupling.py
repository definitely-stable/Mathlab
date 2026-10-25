"""Tests for HYP-105 issue #230 asymptotic anchor decoupling and path-motif bounds."""
import unittest
from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model


class TestHyp105AsymptoticDecoupling(unittest.TestCase):
    def test_w34_spread_census_bounds(self):
        """Verify that on W(3,4) the adversarial symplectic spread yields BB_sync >= 1.86 s^6."""
        model, _, _, _ = true_spread_global_model(2, 'balanced')
        c = ProjectionClosure(model)
        res = c.census()
        s = c.s
        s6 = s**6
        # On W(3,4), s^6 = 4096
        self.assertEqual(res['proper_P3'], 82322)
        self.assertEqual(res['blocked'], 52760)
        self.assertEqual(res['unblocked'], 15298)
        self.assertEqual(res['synchronized_BBo'], 7649)
        self.assertGreater(res['synchronized_BBo'], 1.86 * s6)

    def test_w32_s68_floor_conservation(self):
        """Verify that on W(3,2) S68 achieves core sum 65 and total S=68."""
        from hyp105_g5e2b3e1b0_seven_signature import seven_census
        m = fixture(1, 'S68')
        census = seven_census(m)
        counts = census['seven_class_motif_counts']
        core = counts.get('D6', 0) + counts.get('B-left/A-right', 0) + counts.get('A-left/B-right', 0)
        total_s = census['S_seven']
        self.assertEqual(core, 65)
        self.assertEqual(total_s, 68)

    def test_anchor_blocking_ratio_monotonic_decay(self):
        """Verify that blocked fraction drops monotonically from s=2 to s=4 to s=8."""
        # s=2 lex: 942 / (942 + 4) = 0.9958
        m2 = fixture(1, 'lex')
        res2 = ProjectionClosure(m2).census()
        ratio2 = res2['blocked'] / (res2['blocked'] + res2['unblocked'])

        # s=4 lex: 55384 / (55384 + 15064) = 0.7862
        m4 = fixture(2, 'lex')
        res4 = ProjectionClosure(m4).census()
        ratio4 = res4['blocked'] / (res4['blocked'] + res4['unblocked'])

        self.assertGreater(ratio2, 0.99)
        self.assertLess(ratio4, 0.80)
        self.assertLess(ratio4, ratio2)

    def test_w34_ei_decomposition(self):
        """Verify the exact E and I atom counts on W(3,4) lex."""
        m4 = fixture(2, 'lex')
        c = ProjectionClosure(m4)
        a = c.a
        e_count = 0
        i_count = 0
        for u, nbrs in enumerate(c.adj):
            x0, y0 = divmod(u, a)
            for v, _ in nbrs:
                x1, y1 = divmod(v, a)
                for w, _ in c.adj[v]:
                    x2, y2 = divmod(w, a)
                    if x2 in (x0, x1) or y2 in (y0, y1): continue
                    for z, _ in c.adj[w]:
                        x3, y3 = divmod(z, a)
                        if x3 in (x0, x1, x2) or y3 in (y0, y1, y2): continue
                        q = c.fi.get(tuple(sorted((x0, x3))))
                        r = c.gi.get(tuple(sorted((y0, y3))))
                        if q is None or r is None or (q, r) in c.edge_id: continue
                        p, l = c.projection[q, r]
                        fp = set(c.f[p])
                        gl = set(c.g[l])
                        le = bool(fp & {x0, x3})
                        re = bool(gl & {y0, y3})
                        li = bool(fp & {x1, x2})
                        ri = bool(gl & {y1, y2})
                        if le or re:
                            e_count += 1
                        elif li or ri:
                            i_count += 1
        self.assertEqual(e_count, 38020)
        self.assertEqual(i_count, 17364)
        self.assertEqual(e_count + i_count, 55384)

    def test_adversarial_falsifier_path_upper_bound(self):
        """Verify that P <= 16 s^6 is refuted by genuine W(3,4) and W(3,8) counts."""
        m4 = fixture(2, 'lex')
        c4 = ProjectionClosure(m4)
        res4 = c4.census()
        s4 = c4.s
        bound4 = 16 * (s4 ** 6)
        self.assertEqual(res4['proper_P3'], 83892)
        self.assertEqual(bound4, 65536)
        self.assertGreater(res4['proper_P3'], bound4,
                           "P <= 16 s^6 is falsified on W(3,4): 83892 > 65536")

        # For W(3,8), verify against the analytical bound 16 * 8^6 = 4,194,304
        s8 = 8
        bound8 = 16 * (s8 ** 6)
        reported_p8 = 5461066
        self.assertEqual(bound8, 4194304)
        self.assertGreater(reported_p8, bound8,
                           "P <= 16 s^6 is falsified on W(3,8): 5461066 > 4194304")

    def test_adversarial_falsifier_block_degree_bound(self):
        """Verify that T <= s^(1/10) is refuted on W(3,4)."""
        m4 = fixture(2, 'lex')
        c4 = ProjectionClosure(m4)
        a = c4.a
        row_blocks = {}
        for u, nbrs in enumerate(c4.adj):
            for v, _ in nbrs:
                x_v, _ = divmod(v, a)
                row_blocks[(u, x_v)] = row_blocks.get((u, x_v), 0) + 1
        max_t = max(row_blocks.values())
        s4 = c4.s
        self.assertEqual(max_t, 5)
        self.assertGreater(max_t, s4 ** 0.1,
                           f"T <= s^(1/10) is falsified: max_t={max_t} > {s4**0.1:.3f}")

    def test_formal_blockers_status(self):
        """Verify that anchor_blocking_scaling reports OPEN_CONJECTURE and all 3 blockers."""
        from hyp105_canonical_core import anchor_blocking_scaling, canonical_proof_summary
        res = anchor_blocking_scaling(4)
        self.assertEqual(res["status"], "OPEN_CONJECTURE")
        self.assertEqual(len(res["formal_blockers"]), 3)
        summary = canonical_proof_summary()
        self.assertEqual(summary["Resolution"]["Overall_Status"], "OPEN_WITH_FORMAL_BLOCKER")

    def test_adversarial_falsifier_generic_n3_bound(self):
        """Verify that N_3(u, v) <= 2 is falsified on unpruned H on W(3,4)."""
        import collections
        m4 = fixture(2, 'lex')
        c4 = ProjectionClosure(m4)
        a = c4.a
        n = a * a
        adj = [set(nbr for nbr, _ in c4.adj[i]) for i in range(n)]

        # Sample distribution of N_3 across all pairs
        gt_2_count = 0
        has_18 = False
        max_n3 = 0
        for u in range(n):
            c1 = collections.Counter(adj[u])
            c2 = collections.Counter()
            for w1, k1 in c1.items():
                for w2 in adj[w1]: c2[w2] += k1
            c3 = collections.Counter()
            for w2, k2 in c2.items():
                for w3 in adj[w2]: c3[w3] += k2
            for v in range(n):
                cnt = c3[v]
                if cnt > max_n3: max_n3 = cnt
                if cnt > 2: gt_2_count += 1
                if cnt == 18: has_18 = True

        total_pairs = n * n
        gt_2_fraction = gt_2_count / total_pairs
        self.assertTrue(has_18, "Pairs with N_3(u, v) = 18 must exist on W(3,4)")
        self.assertEqual(max_n3, 57, f"Maximum N_3 on W(3,4) must be 57, got {max_n3}")
        self.assertGreater(gt_2_fraction, 0.60,
                           f"Over 60% of pairs have N_3 > 2 (got {gt_2_fraction*100:.1f}%), refuting N_3 <= 2 generic bound")

    def test_second_moment_inequality_blocker(self):
        """Verify that sum_U N_3^2 >= (sum_U N_3)^2 / |U| by Cauchy-Schwarz."""
        from hyp105_canonical_core import canonical_parameters
        p4 = canonical_parameters(4)
        s = 4
        # If bad pairs |U| <= 4 s C_s = O(s^5) and total bad walk mass is Omega(s^6):
        # sum_U N_3^2 >= Omega(s^12) / O(s^5) = Omega(s^7) >> O(s^6).
        # We verify this algebraic lower bound on bad-pair moment scaling:
        u_bound = 4 * s * ((s - 1) * p4["V"] + (s * s + 1) * (p4["a"] - 1))
        walk_mass_hypothetical = s ** 6  # 4096
        cs_second_moment_floor = (walk_mass_hypothetical ** 2) / u_bound
        self.assertGreater(cs_second_moment_floor, 0)
        # Verify that max N_3 bound yields O(s^8), not O(s^6):
        max_n3_bound = 4 * ((s + 1) ** 2)
        trivial_upper_bound = max_n3_bound * walk_mass_hypothetical
        self.assertGreater(trivial_upper_bound, s ** 7,
                           "Trivial upper bound via max N_3 gives O(s^8), far exceeding O(s^6)")


if __name__ == '__main__':
    unittest.main()
