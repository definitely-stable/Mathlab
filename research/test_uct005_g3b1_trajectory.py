"""Independent UCT-005 G3-B1 temporal-walk/tube falsification oracles."""
from itertools import product
from math import comb
import unittest

from uct005_g3b1_trajectory import (
    ball_volume, adaptive_tree_support, trajectory_capacity_bound,
    independent_epoch_capacity_product, enumerate_walks,
    exact_max_temporal_tube_packing, hamming,
)


def direct_ball(q, s, e):
    words = tuple(product(range(q), repeat=s))
    return tuple(x for x in words if sum(v != 0 for v in x) <= e)


def brute_tube(path, q, e):
    alphabet = tuple(product(range(q), repeat=len(path[0])))
    return set(product(*(tuple(z for z in alphabet
                               if hamming(z, x) <= e) for x in path)))


def brute_max_clique(paths, q, e):
    """Literally enumerate all subsets of <=9 trajectories (independent)."""
    if len(paths) > 9:
        raise ValueError("small-only independent clique oracle")
    tubes = [brute_tube(p, q, e) for p in paths]
    best = 0
    for mask in range(1 << len(paths)):
        chosen = [i for i in range(len(paths)) if mask & (1 << i)]
        if len(chosen) <= best:
            continue
        if all(tubes[i].isdisjoint(tubes[j])
               for i in chosen for j in chosen if i < j):
            best = len(chosen)
    return best


class TrajectoryCapacityTests(unittest.TestCase):
    def test_volume_versus_independent_enumeration(self):
        for q in (2, 3):
            for s in range(5):
                for r in range(s + 2):
                    self.assertEqual(ball_volume(q, s, r),
                                     len(direct_ball(q, s, r)))

    def test_adaptive_support_counts_all_possible_branches(self):
        self.assertEqual(adaptive_tree_support(2, 0), 0)
        self.assertEqual(adaptive_tree_support(2, 1), 1)
        self.assertEqual(adaptive_tree_support(2, 2), 3)
        self.assertEqual(adaptive_tree_support(3, 3), 13)
        bound = trajectory_capacity_bound(q=2, cells=20, epochs=2,
                                          changed=1, errors=0, trusted_bits=0,
                                          query_count=1, probes=2)
        self.assertEqual(bound["accessible_symbols"], 6)
        self.assertLessEqual(bound["maximizing_support"], 6)

    def test_exact_walk_counts_for_every_2x2_case(self):
        for q, s, d in ((2, 2, 2), (2, 3, 2), (3, 1, 2),
                        (2, 0, 3), (3, 2, 1)):
            for w in range(min(2, s) + 1):
                paths = enumerate_walks(q, s, d, w)
                self.assertEqual(len(paths), len(direct_ball(q, s, w)) ** d)
                self.assertEqual(len(paths), len(set(paths)))

    def test_independent_error_tubes_and_exact_tiny_packing(self):
        for q, s, d in ((2, 2, 2), (3, 1, 2), (2, 1, 2)):
            paths = enumerate_walks(q, s, d, 1)
            for e in (0, 1):
                actual = exact_max_temporal_tube_packing(paths, e)
                separate = brute_max_clique(paths, q, e)
                self.assertEqual(actual, separate)
                bound = trajectory_capacity_bound(q=q, cells=s, epochs=d,
                    changed=1, errors=e, trusted_bits=0,
                    query_count=max(1, s), probes=1)
                self.assertGreaterEqual(bound["bound"], actual)
                if not e:
                    self.assertEqual(actual, len(paths))
                    self.assertEqual(bound["bound"], len(paths))
                # No double-counting: equal corruptions of all time slots
                # occur exactly when all slot-wise distances are <= 2e.
                for a in paths:
                    for b in paths:
                        common = not brute_tube(a, q, e).isdisjoint(brute_tube(b, q, e))
                        expected = all(hamming(x, y) <= 2 * e for x, y in zip(a, b))
                        self.assertEqual(common, expected)

    def test_temporal_tube_strict_finite_gain_over_independent_epochs(self):
        args = dict(q=2, cells=6, epochs=3, changed=1,
                    errors=1, trusted_bits=0, query_count=6, probes=1)
        report = trajectory_capacity_bound(**args)
        self.assertEqual(report["accessible_symbols"], 6)
        self.assertEqual(report["bound"], 113)
        self.assertEqual(independent_epoch_capacity_product(
            2, 6, 3, 1, 1, 0), 144)
        self.assertLess(report["bound"], 144)
        self.assertEqual(report["per_support"][-1]["walks"], 343)
        self.assertEqual(report["per_support"][-1]["tube"], 113)

    def test_zero_probes_and_zero_writes_cannot_hide_information(self):
        for h in range(3):
            report = trajectory_capacity_bound(
                q=2, cells=5, epochs=3, changed=3, errors=2,
                trusted_bits=h, query_count=5, probes=0)
            self.assertEqual(report["accessible_symbols"], 0)
            self.assertEqual(report["bound"], 2 ** (h * 3))
        report = trajectory_capacity_bound(
            q=2, cells=5, epochs=3, changed=0, errors=2,
            trusted_bits=0, query_count=5, probes=1)
        self.assertEqual(report["bound"], 1)

    def test_epoch_one_matches_single_epoch_classical_ball_bound(self):
        for q in (2, 3):
            for s in range(5):
                for w in (0, 1, 2):
                    for e in (0, 1):
                        result = trajectory_capacity_bound(
                            q=q, cells=s, epochs=1, changed=w,
                            errors=e, trusted_bits=0,
                            query_count=max(1, s), probes=1)
                        single = min(ball_volume(q, s, w),
                            ball_volume(q, s, w+e)//ball_volume(q, s, e))
                        self.assertEqual(result["bound"], single)

    def test_immutable_inputs_explicitly_rejected(self):
        invalid = [
            dict(q=1), dict(epochs=0), dict(changed=-1),
            dict(errors=-1), dict(trusted_bits=-1),
            dict(query_count=0), dict(probes=-1),
        ]
        good = dict(q=2, cells=2, epochs=2, changed=1, errors=1,
                    trusted_bits=0, query_count=2, probes=1)
        for delta in invalid:
            with self.assertRaises(ValueError):
                trajectory_capacity_bound(**(good | delta))


if __name__ == "__main__":
    unittest.main()
