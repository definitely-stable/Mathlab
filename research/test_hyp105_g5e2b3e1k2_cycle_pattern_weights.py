"""Independent K2 falsifiers.

GF5 weights are recomputed by a 3+3 meet-in-the-middle palette count that
does not use the Fourier oracle; walk patterns are recounted by brute force
over all colourings; the D2 identity is checked on dense random graphs.
"""
from collections import Counter
from itertools import combinations, product
import random
import unittest

from hyp105_g5e2b3d_joint_risk import closed_form_c4_GF5_flow_weight
from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, labeled_model
from hyp105_g5e2b3e1k2_cycle_pattern_weights import (
    classify_four_cycle_patterns, classify_six_cycle_patterns, column_supports,
    cyclic_walk_patterns, edge_pair_identity, kikuchi_r3_witness,
    pattern_columns,
)

PALETTE = [t for t in product(range(1, 5), repeat=4) if sum(t) % 5 == 4]
PAIRS6 = tuple(combinations(range(6), 2))


def mitm_six(supports, signs=(1, -1, 1, -1, 1, -1)):
    """Count palette assignments with signed coordinate sums zero (3+3 split)."""
    coords = sorted({c for col in supports for c in col})
    pos = {c: i for i, c in enumerate(coords)}

    def side(ids):
        acc = Counter({(0,) * len(coords): 1})
        for i in ids:
            nxt = Counter()
            for vec, n in acc.items():
                for t in PALETTE:
                    v = list(vec)
                    for c, w in zip(supports[i], t):
                        v[pos[c]] = (v[pos[c]] + signs[i] * w) % 5
                    nxt[tuple(v)] += n
            acc = nxt
        return acc

    first = side((0, 1, 2))
    second = side((3, 4, 5))
    return sum(n * second[tuple((-x) % 5 for x in vec)] for vec, n in first.items())


def brute_four(supports, signs=(1, -1, 1, -1)):
    """Enumerate three columns, solve the fourth exactly."""
    coords = sorted({c for col in supports for c in col})
    pos = {c: i for i, c in enumerate(coords)}
    palette = set(PALETTE)
    total = 0
    for t0, t1, t2 in product(PALETTE, repeat=3):
        v = [0] * len(coords)
        for col, t, sg in zip(supports[:3], (t0, t1, t2), signs[:3]):
            for c, w in zip(col, t):
                v[pos[c]] = (v[pos[c]] + sg * w) % 5
        need = [(-v[pos[c]] * signs[3]) % 5 for c in supports[3]]
        if any(v[i] for c, i in pos.items() if c not in supports[3]):
            continue
        if tuple(need) in palette:
            total += 1
    return total


def canonical_count(length):
    seen = set()
    for seq in product(range(length), repeat=length):
        if any(seq[i] == seq[(i + 1) % length] for i in range(length)):
            continue
        relabel = {}
        canon = tuple(relabel.setdefault(c, len(relabel)) for c in seq)
        seen.add(canon)
    return len(seen)


class PatternTests(unittest.TestCase):
    def test_walk_pattern_counts_by_brute_force(self):
        self.assertEqual(len(cyclic_walk_patterns(6)), canonical_count(6))
        self.assertEqual(len(cyclic_walk_patterns(4)), canonical_count(4))
        self.assertEqual(len(cyclic_walk_patterns(6)), 41)

    def test_six_cycle_classification_and_independent_weights(self):
        six = classify_six_cycle_patterns()
        self.assertEqual(six["distinct_column_patterns"], 879)
        self.assertEqual(six["degenerate_repeated_column_patterns"], 50)
        self.assertEqual(six["global_min_weight"], 5643)
        self.assertTrue(six["min_attained_only_by_proper"])
        self.assertEqual(six["max_cycles_per_six_column_set"], 4)
        weights = six["weights"]
        rng = random.Random(230)
        keys = sorted(weights)
        sample = [((0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))]
        sample += [k for k in keys if (len(set(k[0])), len(set(k[1]))) in ((6, 5), (5, 6))][:3]
        sample += rng.sample(keys, 4)
        for xs, ys in sample:
            sup = column_supports(pattern_columns(xs, ys))
            self.assertEqual(mitm_six(sup), weights[(xs, ys)], (xs, ys))

    def test_four_cycle_classification_and_brute_force(self):
        four = classify_four_cycle_patterns()
        self.assertEqual(four["cycle_patterns"], 9)
        self.assertEqual(four["proper_weight"], closed_form_c4_GF5_flow_weight())
        self.assertEqual(four["global_min_weight"], 531)
        self.assertEqual(four["max_cycles_per_four_column_set"], 2)
        for (xs, ys), w in four["weights"].items():
            sup = column_supports(pattern_columns(xs, ys))
            self.assertEqual(brute_four(sup), w, (xs, ys))


class IdentityAndWitnessTests(unittest.TestCase):
    def test_d2_identity_on_random_graphs(self):
        rng = random.Random(4)
        for _ in range(25):
            n = rng.randint(6, 10)
            rows = [set() for _ in range(n)]
            for u, v in combinations(range(n), 2):
                if rng.random() < rng.choice((0.4, 0.7)):
                    rows[u].add(v)
                    rows[v].add(u)
            out = edge_pair_identity(tuple(frozenset(r) for r in rows))
            self.assertEqual(out["sum_edge_C4_pairs"],
                             out["edge_only_pairs"] + out["book_pairs"]
                             + out["degenerate_pairs"])

    def test_theorem_k_prime_on_w32_bijections_and_s4(self):
        rng = random.Random(366)
        base = gq_pair_model(1, "lex")
        for _ in range(4):
            left = list(PAIRS6)
            right = list(PAIRS6)
            rng.shuffle(left)
            rng.shuffle(right)
            model = labeled_model(2, 6, base["incidences"], left, right)
            out = kikuchi_r3_witness(model)
            self.assertLessEqual(out["max_cycles_per_set"], 4)
        out = kikuchi_r3_witness(gq_pair_model(2, "random", 20261011))
        self.assertGreater(out["distinct_six_sets"], 0)

    def test_fail_closed(self):
        with self.assertRaises(ValueError):
            cyclic_walk_patterns(2)
        with self.assertRaises(RuntimeError):
            kikuchi_r3_witness(gq_pair_model(1, "lex"), max_cycles=3)


if __name__ == "__main__":
    unittest.main()
