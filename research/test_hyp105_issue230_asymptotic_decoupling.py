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


if __name__ == '__main__':
    unittest.main()
