"""Tests for HYP-105 issue #230 conditioned layer density of internal anchor blocking on W(3,4)."""
import statistics
import unittest
from collections import Counter

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model


def _compute_conditioned_density(model):
    c = ProjectionClosure(model)
    a = c.a
    w3 = Counter()
    i_cnt = Counter()
    w3_good = Counter()
    i_good = Counter()

    for u, nbrs in enumerate(c.adj):
        x0, y0 = divmod(u, a)
        for v, _ in nbrs:
            x1, y1 = divmod(v, a)
            for w, _ in c.adj[v]:
                x2, y2 = divmod(w, a)
                if x2 in (x0, x1) or y2 in (y0, y1):
                    continue
                for z, _ in c.adj[w]:
                    x3, y3 = divmod(z, a)
                    if x3 in (x0, x1, x2) or y3 in (y0, y1, y2):
                        continue
                    q = c.fi.get(tuple(sorted((x0, x3))))
                    r = c.gi.get(tuple(sorted((y0, y3))))
                    if q is None or r is None or (q, r) in c.edge_id:
                        continue
                    p, l = c.projection[q, r]
                    fp = set(c.f[p])
                    gl = set(c.g[l])
                    le = bool(fp & {x0, x3})
                    re = bool(gl & {y0, y3})
                    li = bool(fp & {x1, x2})
                    ri = bool(gl & {y1, y2})
                    w3[p] += 1
                    if li or ri:
                        i_cnt[p] += 1
                    if not (le or re):
                        w3_good[p] += 1
                        if li or ri:
                            i_good[p] += 1

    rhos = [i_cnt[p] / w3[p] for p in range(85)]
    rhos_good = [i_good[p] / w3_good[p] for p in range(85) if w3_good[p] > 0]
    return {
        'w3': w3,
        'i': i_cnt,
        'rhos': rhos,
        'w3_good': w3_good,
        'i_good': i_good,
        'rhos_good': rhos_good,
    }


class TestHyp105ConditionedDensity(unittest.TestCase):
    def test_w34_lex_conditioned_density(self):
        """Verify conditioned density statistics on W(3,4) lex."""
        data = _compute_conditioned_density(fixture(2, 'lex'))
        self.assertEqual(sum(data['w3'].values()), 70448)
        self.assertEqual(sum(data['i'].values()), 33328)
        self.assertEqual(sum(data['w3_good'].values()), 32428)
        self.assertEqual(sum(data['i_good'].values()), 17364)

        rhos = data['rhos']
        self.assertEqual(len(rhos), 85)
        self.assertAlmostEqual(statistics.mean(rhos), 0.472331, places=5)
        self.assertAlmostEqual(statistics.pvariance(rhos), 0.002220, places=5)
        self.assertAlmostEqual(min(rhos), 0.354523, places=5)
        self.assertAlmostEqual(max(rhos), 0.572779, places=5)

        # No pathological points: max < 0.60 << 1.0
        self.assertLess(max(rhos), 0.58)
        self.assertGreater(min(rhos), 0.35)

    def test_w34_spread_conditioned_density(self):
        """Verify conditioned density statistics on W(3,4) spread."""
        model, _, _, _ = true_spread_global_model(2, 'balanced')
        data = _compute_conditioned_density(model)
        self.assertEqual(sum(data['w3'].values()), 68058)
        self.assertEqual(sum(data['i'].values()), 31904)
        self.assertEqual(sum(data['w3_good'].values()), 32868)
        self.assertEqual(sum(data['i_good'].values()), 17570)

        rhos = data['rhos']
        self.assertEqual(len(rhos), 85)
        self.assertAlmostEqual(statistics.mean(rhos), 0.468980, places=5)
        self.assertAlmostEqual(statistics.pvariance(rhos), 0.001953, places=5)
        self.assertAlmostEqual(min(rhos), 0.368812, places=5)
        self.assertAlmostEqual(max(rhos), 0.568306, places=5)

        # No pathological points: max < 0.60 << 1.0
        self.assertLess(max(rhos), 0.57)
        self.assertGreater(min(rhos), 0.36)

    def test_conditioned_density_tight_concentration(self):
        """Verify that rho(p) concentrates tightly around 2/s = 0.50 across both schemes."""
        for model in (fixture(2, 'lex'), true_spread_global_model(2, 'balanced')[0]):
            data = _compute_conditioned_density(model)
            rhos = data['rhos']
            mean = statistics.mean(rhos)
            std = statistics.pstdev(rhos)
            # All 85 points lie within 2.6 standard deviations
            for r in rhos:
                self.assertLess(abs(r - mean), 2.6 * std)
                self.assertLess(r, 0.60)
                self.assertGreater(r, 0.30)


if __name__ == '__main__':
    unittest.main()
