"""C8 independent finite tests: full permutations, fiber combinatorics, GQ."""
from collections import defaultdict
from itertools import combinations, permutations
from math import comb
import unittest

from hyp105_g5e2b3e1c5_common_bijection import fixed_map_overlap
from hyp105_g5e2b3e1c7_adversarial_minimum import exact_adversarial_minimum
from hyp105_g5e2b3e1c8_fiber_rearrangement import (
    frozen_fiber_rearrangement, universal_k_pin_lower, finite_minimum_interval,
    W32_fiber_report,
)


def direct_relaxed_fiber_min(source, target, V, D, p):
    """Independent oracle: enumerate every possible target-cell subset.

    Does NOT use C8 sorted marginal buckets or sixset-capacity identity.
    Safe on V=7, with a single pin and at most 6-sixset fibers.
    """
    allsets = tuple(map(frozenset, combinations(range(V), 6)))
    total = 0
    for A in (frozenset(), frozenset(D)):
        orig = [R for R in allsets if R.intersection(D) == A]
        mapped = frozenset(p[D.index(i)] for i in A)
        t = sum(1 for Q in target if Q.intersection(p) == mapped)
        weights = [source.get(R, 0) for R in orig]
        total += min(sum(weights[j] for j in ix)
                     for ix in combinations(range(len(orig)), t))
    return total


class FiberRearrangementC8Tests(unittest.TestCase):
    def test_star_strict_positive_single_pin_certificate_all_eight_images(self):
        V = 8
        star = {frozenset(set(range(V)) - {0, j}) for j in range(1, V)}
        src = {R: 1 for R in star}
        c = universal_k_pin_lower(src, star, V, (0,))
        self.assertEqual(c["unconditioned_rearrangement_lower"], 0)
        self.assertEqual(c["minimum_fiber_lower"], 1)
        self.assertEqual(c["enumerated_injective_prefixes"], 8)
        for j in range(V):
            self.assertEqual(frozen_fiber_rearrangement(
                src, star, V, (0,), (j,)), 7 if j == 0 else 1)
        self.assertEqual(exact_adversarial_minimum(src, star, V)["exact_minimum"], 1)

    def test_star_mean_upper_meets_one_pin_lower_exactly(self):
        V=8
        star={frozenset(set(range(V))-{0,j}) for j in range(1,V)}
        source={R:1 for R in star}
        loose=finite_minimum_interval(source, star, V)
        sharp=finite_minimum_interval(source, star, V, (0,))
        self.assertEqual((loose["certified_minimum_lower"],
                          loose["existential_mean_minimum_upper"]), (0,1))
        self.assertEqual((sharp["certified_minimum_lower"],
                          sharp["existential_mean_minimum_upper"]), (1,1))
        self.assertTrue(sharp["minimum_exact"])
        self.assertEqual(sharp["exact_minimum_if_equal"], 1)
        self.assertFalse(sharp["explicit_upper_witness"])

    def test_independent_direct_subset_relaxation_V7(self):
        V = 7
        edges = tuple(map(frozenset, combinations(range(V), 6)))
        src = {R: 1 + i % 3 for i, R in enumerate(edges) if i != 2}
        tgt = {edges[0], edges[3], edges[5]}
        for d in range(V):
            for j in range(V):
                self.assertEqual(frozen_fiber_rearrangement(
                    src, tgt, V, (d,), (j,)),
                    direct_relaxed_fiber_min(src, tgt, V, (d,), (j,)))

    def test_all_eight_factorial_conditional_fiber_lower_is_sound(self):
        V = 8
        edges = tuple(map(frozenset, combinations(range(V), 6)))
        src = {R: i%4+1 for i, R in enumerate(edges) if i%3!=0}
        target = {R for i,R in enumerate(edges) if i%4!=0}
        D = (0, 3)
        exact_cond = defaultdict(lambda: None)
        global_best = None
        for p in permutations(range(V)):
            val = fixed_map_overlap(src, target, p)
            key = (p[0], p[3])
            previous = exact_cond[key]
            exact_cond[key] = val if previous is None else min(previous, val)
            global_best = val if global_best is None else min(global_best, val)
        self.assertEqual(len(exact_cond), V*(V-1))
        for key, optimum in exact_cond.items():
            rel = frozen_fiber_rearrangement(src, target, V, D, key)
            self.assertLessEqual(rel, optimum)
        gate = universal_k_pin_lower(src, target, V, D)
        self.assertEqual(gate["minimum_fiber_lower"], min(
            frozen_fiber_rearrangement(src, target, V, D, p)
            for p in permutations(range(V), len(D))))
        self.assertLessEqual(gate["minimum_fiber_lower"], global_best)
        self.assertGreaterEqual(gate["minimum_fiber_lower"],
                                gate["unconditioned_rearrangement_lower"])

    def test_nested_prefix_monotonicity_for_each_full_map(self):
        V = 8
        sets = tuple(map(frozenset, combinations(range(V), 6)))
        source = {R: 2 + i%3 for i,R in enumerate(sets) if i%4 != 0}
        target = {R for i,R in enumerate(sets) if i%3 == 1}
        for p in list(permutations(range(V)))[:400]:
            l0 = frozen_fiber_rearrangement(source, target, V)
            l1 = frozen_fiber_rearrangement(source, target, V, (0,), (p[0],))
            l2 = frozen_fiber_rearrangement(source, target, V,
                                            (0, 1), (p[0], p[1]))
            actual = fixed_map_overlap(source, target, p)
            self.assertLessEqual(l0, l1)
            self.assertLessEqual(l1, l2)
            self.assertLessEqual(l2, actual)

    def test_genuine_W32_source_target_consistency(self):
        r = W32_fiber_report()
        self.assertEqual(r["lex"]["actual_original_right_g_overlap"], 98)
        self.assertEqual(r["reverse-line"]["actual_original_right_g_overlap"], 77)
        for x in r.values():
            self.assertEqual(x["V"], 15)
            self.assertEqual(x["one_pin_prefixes"], 15)
            self.assertEqual(x["two_pin_prefixes"], 210)
            self.assertLessEqual(x["unconditional_lower"], x["one_pin_universal_lower"])
            self.assertLessEqual(x["one_pin_universal_lower"], x["two_pin_universal_lower"])
            self.assertLessEqual(x["two_pin_universal_lower"], x["actual_original_right_g_overlap"])
            self.assertEqual(x["existential_mean_upper"], 69)
            self.assertFalse(x["f_and_F_minimum_proved"])

    def test_fail_closed_bad_pins_and_budget(self):
        R = frozenset(range(6))
        with self.assertRaises(ValueError):
            frozen_fiber_rearrangement({R:1}, {R}, 7, (0,0), (1,2))
        with self.assertRaises(ValueError):
            frozen_fiber_rearrangement({R:1}, {R}, 7, (0,1), (2,2))
        with self.assertRaises(ValueError):
            frozen_fiber_rearrangement({R:1}, {R}, 7, (0,), ())
        with self.assertRaises(ValueError):
            frozen_fiber_rearrangement({R:-1}, {R}, 7)
        with self.assertRaises(ValueError):
            universal_k_pin_lower({R:1}, {R}, 8, (0,1), max_prefixes=8)


if __name__ == "__main__":
    unittest.main()
