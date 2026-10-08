"""UCT-003 fixed-q certificate falsifier. Exact small parse DP, not a novelty proof."""
from math import ceil
import unittest


def pair(r, m):
    if r < 1 or m < 1:
        raise ValueError("positive r,m required")
    base = "ab" * r + "b" * (2 * m) + "ab" * r
    target = "ab" * m
    return base, target


def absent_q_positions(base, target, q):
    return tuple(i for i in range(max(0, len(target) - q + 1))
                 if target[i:i + q] not in base)


def exact_source_only_cost(base, target):
    """Exact min K=L+#ADD instructions+2*COPY over all nonempty instructions."""
    n = len(target)
    best = [0] * (n + 1)
    # For an input suffix, try every legal nonempty ADD phrase or COPY phrase.
    for i in range(n - 1, -1, -1):
        options = []
        for k in range(1, n - i + 1):
            suffix = best[i + k]
            options.append(k + 1 + suffix)  # independent literal ADD length k
            if target[i:i + k] in base:
                options.append(2 + suffix)  # source substring COPY
        best[i] = min(options)
    return best[0]


class Uct003FixedQTests(unittest.TestCase):
    def test_all_short_windows_present_and_structural_lengths(self):
        for r in range(1, 7):
            for m in range(1, 13):
                base, target = pair(r, m)
                self.assertEqual(len(base), 2*m + 4*r)
                self.assertEqual(len(target), 2*m)
                for q in range(1, 2*r + 1):
                    self.assertEqual(absent_q_positions(base, target, q), ())
                # Exact relaxation candidate L=0,C=1 is feasible by
                # the *relaxed numeric constraints*, not by an actual parse.
                self.assertGreaterEqual(len(base), len(target))

    def test_exact_small_parse_dp_and_diverging_gap(self):
        for r in range(1, 5):
            for m in range(1, 14):
                base, target = pair(r, m)
                exact = exact_source_only_cost(base, target)
                self.assertGreaterEqual(exact*(2*r + 1), 4*m)
                self.assertLessEqual(exact, 2*ceil(m/r))
                # All q<=2r have U_q=0, giving optimistic relaxed floor 2.
                self.assertEqual(absent_q_positions(base, target, 2*r), ())
                self.assertGreaterEqual(exact, 2)
        # Arbitrary finite cutoff Qmax handled by r=ceil(Qmax/2).
        for max_q in range(1, 11):
            r = ceil(max_q/2)
            base, target = pair(r, 100)
            self.assertTrue(all(not absent_q_positions(base, target, q)
                                for q in range(1, max_q+1)))
            self.assertGreater(2*100/(2*r+1), 10)

    def test_actual_one_copy_impossible_at_long_lengths(self):
        for r in range(1, 5):
            base, target = pair(r, r + 2)
            self.assertNotIn(target, base)
            self.assertEqual(absent_q_positions(base, target, 2*r), ())
            self.assertGreater(exact_source_only_cost(base, target), 2)


if __name__ == "__main__":
    unittest.main()
