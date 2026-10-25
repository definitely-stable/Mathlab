"""Independent D6-AA4-F exact source factor separator tests; no W34 full scan."""
import random
import unittest
from itertools import permutations, product

from hyp105_issue230_d6aa4f_three_factor_separator import (
    PAIRS, permutation_states, separator_hierarchy, triangle_gap)


class ThreeSourceSeparatorTests(unittest.TestCase):
    def test_triangle_pairs_believe_zero_but_global_triple_cost_one(self):
        result = triangle_gap()
        self.assertEqual(result["globally_coherent_states"], 6)
        self.assertEqual(
            (result["independent_Q_lower"],result["pairwise_source_coherent_lower"],
             result["three_source_joint_exact_minimum"]), (0,0,1))
        self.assertEqual(result["pair_to_triple_gap"], 1)
        self.assertEqual(sum(result["pair_groups_minima"].values()), 0)
        self.assertEqual(sorted(result["all_global_state_scores"]), [1,1,1,2,2,2])

    def test_pure_and_mixed_images_independently_injective(self):
        for types in (("P","P","P"),("P","P","L"),("P","L","L"),("L","L","L")):
            n = {t:types.count(t) for t in ("P","L")}
            base = tuple((types[i], i) for i in range(3))
            states = permutation_states(types, base)
            self.assertEqual(len(states), __import__("math").factorial(n["P"]) *
                             __import__("math").factorial(n["L"]))
            self.assertEqual(len(set(states)),len(states))
            for state in states:
                for t in ("P","L"):
                    used = [state[i] for i in range(3) if types[i] == t]
                    self.assertEqual(len(used),len(set(used)))
        # Opposite typed factors CAN reuse the same physical pair.
        mixed = permutation_states(("P","P","L"), (0,1,0))
        self.assertEqual(len(mixed), 2)
        self.assertTrue(any(s[0] == s[2] for s in mixed))
        with self.assertRaises(ValueError):
            permutation_states(("P","P","L"), (0,0,0))

    def test_strict_source_dependency_rejection(self):
        states = permutation_states(("P","P","P"), (0,1,2))
        # Cost of original factor 2 illegally described as depending on 0.
        with self.assertRaises(AssertionError):
            separator_hierarchy(("P","P","P"), states, [
                ((0,), tuple(int(s[2] == 0) for s in states))])
        with self.assertRaises(ValueError):
            separator_hierarchy(("P","P","P"), states[:-1], [])
        with self.assertRaises(ValueError):
            separator_hierarchy(("P","P","P"), states, [((0,0),(0,)*6)])
        with self.assertRaises(ValueError):
            separator_hierarchy(("P","P","P"), states, [((0,),(-1,)*6)])
        with self.assertRaises(ValueError):
            separator_hierarchy(("P","P","P"), states, [((4,),(0,)*6)])

    def test_random_complete_local_original_support_hierarchy_sound(self):
        rng = random.Random(230)
        for types in (("P","P","P"),("P","P","L"),("P","L","L")):
            states = permutation_states(types, tuple(range(3)))
            for _ in range(60):
                motifs = []
                for j in range(8):
                    scope = tuple(i for i in range(3) if rng.randrange(2))
                    # Exact locally consistent, typed-injective partial
                    # assignment cost table; no independent per-state fiction.
                    partials = {tuple(s[i] for i in scope) for s in states}
                    table = {k: rng.randrange(5) for k in partials}
                    motifs.append((scope, tuple(table[tuple(s[i] for i in scope)]
                                                 for s in states)))
                result = separator_hierarchy(types, states, motifs)
                raw = [sum(row[k] for _, row in motifs)
                       for k in range(len(states))]
                self.assertEqual(result["three_source_joint_exact_minimum"], min(raw))
                self.assertLessEqual(result["independent_Q_lower"],
                                     result["pairwise_source_coherent_lower"])
                self.assertLessEqual(result["pairwise_source_coherent_lower"], min(raw))
                self.assertEqual(result["all_global_state_scores"], tuple(raw))

    def test_true_three_way_motifs_not_false_pairwise_localized(self):
        states = permutation_states(("P","P","P"), (0,1,2))
        three = (tuple(range(3)), tuple(int(s == (0,1,2)) for s in states))
        bound = separator_hierarchy(("P","P","P"), states, [three])
        self.assertEqual(bound["true_three_factor_scope_motifs"],1)
        self.assertEqual(bound["three_source_joint_exact_minimum"],0)
        self.assertEqual(bound["pairwise_source_coherent_lower"],0)

    def test_constant_original_sixsets_preserved_in_all_scopes(self):
        states = permutation_states(("P","L","L"), (0,0,1))
        bound = separator_hierarchy(("P","L","L"), states, [
            ((),(7,7)),
            ((0,),(1,1)),
            ((1,2),(0,1))])
        self.assertEqual(bound["independent_Q_lower"],8)
        self.assertEqual(bound["pairwise_source_coherent_lower"],8)
        self.assertEqual(bound["three_source_joint_exact_minimum"],8)


if __name__=="__main__":
    unittest.main()
