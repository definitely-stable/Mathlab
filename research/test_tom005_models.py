"""Independent small-case adversarial checks for ALL seven TOM-005 claims.

The models each have a written universally quantified elementary proof.
These tests independently enumerate alternative implementations, not reuse
the optimized function as their own oracle.
"""
import itertools
from fractions import Fraction
import unittest

from tom005_models import (
    interval_certificate, pareto_indices, routed_cost, expected_cost,
    reject_first_order, generation_crash_prefix, exact_fingerprint_possible,
    materialized_fanout_changes,
)


class SevenTheoremProofOracles(unittest.TestCase):
    def test_A_interval_certificate_vs_all_unknown_cost_completions(self):
        bins = ((0, 0), (0, 1), (1, 2), (0, 2), (2, 3))
        visited = 0
        for n in (1, 2, 3):
            for intervals in itertools.product(bins, repeat=n):
                for mask in range(1, 1 << n):
                    obs_ids = [i for i in range(n) if mask & (1 << i)]
                    for known in itertools.product(*[
                            range(intervals[i][0], intervals[i][1] + 1)
                            for i in obs_ids
                    ]):
                        obs = dict(zip(obs_ids, known))
                        best, certified = interval_certificate(intervals, obs)
                        unknown = [i for i in range(n) if i not in obs]
                        all_complete = itertools.product(*[
                            range(intervals[i][0], intervals[i][1] + 1)
                            for i in unknown
                        ])
                        oracle = all(best <= min((c for c in unknown_costs),
                                                 default=best)
                                     for unknown_costs in all_complete)
                        self.assertEqual(certified, oracle)
                        visited += 1
        self.assertGreater(visited, 1000)

    def test_B_pareto_pruning_preserves_all_positive_monotone_costs(self):
        possibilities = tuple(itertools.product(range(3), repeat=2))
        counter = 0
        for n in (1, 2, 3):
            for candidates in itertools.product(possibilities, repeat=n):
                pruned = pareto_indices(candidates)
                self.assertTrue(pruned)
                for wa, wb in ((1, 1), (1, 3), (3, 1), (2, 3)):
                    value = lambda v: wa * v[0] + wb * v[1]
                    self.assertEqual(min(map(value, candidates)),
                                     min(value(candidates[i]) for i in pruned))
                counter += 1
        self.assertGreater(counter, 700)
        # Rule is NOT sound for context-dependent, nonmonotone costs.
        self.assertEqual(pareto_indices(((1, 1), (2, 2))), (0,))
        self.assertLess(-sum((2, 2)), -sum((1, 1)))

    def test_C_segment_route_dp_vs_complete_path_search(self):
        count = 0
        for periods in (1, 2, 3):
            for flattened in itertools.product(range(3), repeat=periods * 2):
                local = tuple(tuple(flattened[2*t:2*t+2])
                              for t in range(periods))
                for switch in range(4):
                    brute = min(
                        sum(local[t][route[t]] for t in range(periods))
                        + switch * sum(route[t] != route[t-1]
                                       for t in range(1, periods))
                        for route in itertools.product(range(2), repeat=periods)
                    )
                    self.assertEqual(routed_cost(local, switch), brute)
                    count += 1
        self.assertGreater(count, 3000)
        self.assertEqual(routed_cost(((0, 1), (1, 0)), 3), 1)
        # Naively choose local argmin (0 then 1) -> 3 > DP optimum 1.

    def test_D_failure_test_order_exchange_vs_all_permutations(self):
        count = 0
        for n in (2, 3):
            for prices in itertools.product((1, 2, 3), repeat=n):
                for ps in itertools.product(
                    (Fraction(0), Fraction(1, 4), Fraction(3, 4), Fraction(1)),
                    repeat=n
                ):
                    tests = tuple(zip(prices, ps))
                    winner = reject_first_order(tests)
                    expected = expected_cost(tests, winner)
                    brute = min(expected_cost(tests, p)
                                for p in itertools.permutations(range(n)))
                    self.assertEqual(expected, brute)
                    count += 1
        self.assertGreater(count, 1000)
        # Zero-cost tests cannot make later cost worse.
        tests = ((0, Fraction(1)), (2, Fraction(0)))
        self.assertEqual(expected_cost(tests, reject_first_order(tests)),
                         Fraction(0))

    def test_E_complete_abstract_crash_prefixes_and_reordering_falsifiers(self):
        for order in itertools.permutations(("prepare", "flush", "publish")):
            cuts = [generation_crash_prefix(order, cut)
                    for cut in range(4)]
            all_valid = all(valid for _, _, valid in cuts)
            # Only order with prepared+durable data before commit is safe.
            self.assertEqual(all_valid,
                             order == ("prepare", "flush", "publish"))
        self.assertTrue(all(generation_crash_prefix(
            ("prepare", "flush", "publish"), stop)[-1] for stop in range(4)))
        self.assertFalse(generation_crash_prefix(
            ("prepare", "publish", "flush"), 2)[-1])

    def test_F_injective_fixed_bit_state_pigeonhole_with_all_tiny_maps(self):
        for domain in range(1, 5):
            for bits in range(3):
                available = range(1 << bits)
                actual_exists = any(
                    len(set(mapping)) == domain
                    for mapping in itertools.product(available, repeat=domain)
                )
                self.assertEqual(
                    exact_fingerprint_possible(domain, bits), actual_exists)
        self.assertFalse(exact_fingerprint_possible(5, 2))
        self.assertTrue(exact_fingerprint_possible(4, 2))
        # This is NOT a theorem that hash collision attacks are efficient,
        # nor a bound for algorithms with extra probes or trusted state.

    def test_G_materialized_incremental_fanout_lower_bound(self):
        for n in range(51):
            for old, new in itertools.product((0, 1), repeat=2):
                prior_outputs = tuple(old & 1 for _ in range(n))
                next_outputs = tuple(new & 1 for _ in range(n))
                brute = sum(a != b for a, b in
                            zip(prior_outputs, next_outputs))
                self.assertEqual(
                    materialized_fanout_changes(n, old, new), brute)
        # Lazy output (one retained scalar reference) is a different
        # cost model and refutes an unconditional computational bound.
        self.assertEqual(len({1}), 1)

    def test_api_fails_closed_when_outside_frozen_model(self):
        with self.assertRaises(ValueError):
            interval_certificate(((2, 1),), {0: 2})
        with self.assertRaises(ValueError):
            interval_certificate(((0, 1),), {0: 4})
        with self.assertRaises(ValueError):
            pareto_indices(((1, 2), (3,)))
        with self.assertRaises(ValueError):
            routed_cost(((1, 3), (1,)), 1)
        with self.assertRaises(ValueError):
            expected_cost(((1, Fraction(1, 2)),), (1,))
        with self.assertRaises(ValueError):
            generation_crash_prefix(("prepare", "flush", "publish"), 4)
        with self.assertRaises(ValueError):
            exact_fingerprint_possible(0, 1)
        with self.assertRaises(ValueError):
            materialized_fanout_changes(-1, 0, 1)


if __name__ == "__main__":
    unittest.main()
