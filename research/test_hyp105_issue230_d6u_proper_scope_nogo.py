"""D6-U: independent combinatorics, adversarial pins, real W32 seven-GF5."""
import unittest
from itertools import combinations, product
from collections import Counter

from hyp105_issue230_d6u_proper_scope_nogo import (
    free_site_bad_projection, physical_two_regular,
    original_sixset_forest_scope, proper_scope_zero_witness, report,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six, validated_small_model
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    _signature_for_original_sixset, cylinder_seven_class, R3_CERTIFIED_FLOORS,
)


def canonical_partitions_of_six():
    """Independent restricted-growth words: Bell(6)=203."""
    for p in product(range(6), repeat=6):
        if p[0] or any(p[i] > 1 + max(p[:i]) for i in range(1, 6)):
            continue
        yield p


def independent_bad_projection(ends, pairs):
    degrees = Counter(u for orig in ends for u in pairs[orig])
    return len(degrees) != 6 or any(d != 2 for d in degrees.values())


def independently_no_short_cycle(edges):
    adjacency = {}
    for p, l in edges:
        u, v = ("P", p), ("L", l)
        adjacency.setdefault(u, set()).add(v)
        adjacency.setdefault(v, set()).add(u)
    for start in adjacency:
        pending = [(start, (start,))]
        while pending:
            node, path = pending.pop()
            for nxt in adjacency[node]:
                if nxt == start and len(path) in (4, 6):
                    return False
                if nxt not in path and len(path) < 6:
                    pending.append((nxt, path + (nxt,)))
    return True


class ProperScopeZeroTests(unittest.TestCase):
    def test_exhaustive_203_endpoint_multiplicity_types_adversarial_pins(self):
        n = 0
        for ends in canonical_partitions_of_six():
            ordered = tuple(dict.fromkeys(ends))
            for a in (6, 14, 35):
                alphabet = tuple(combinations(range(a), 2))
                for k in range(len(ordered)):
                    for direction in (0, 1):
                        selected = ordered[:k] if direction == 0 else ordered[len(ordered)-k:]
                        labels = alphabet[:k] if direction == 0 else alphabet[-k:]
                        pinned = dict(zip(selected, labels))
                        w = free_site_bad_projection(ends, pinned, a)
                        result = w["labels"]
                        self.assertTrue(all(result[v] == e for v, e in pinned.items()))
                        self.assertEqual(len(set(result.values())), len(ordered))
                        self.assertTrue(independently_bad_projection(ends, result))
                        self.assertFalse(physical_two_regular(ends, result))
                        self.assertLessEqual(w["candidates_tested"], 2)
                        n += 1
        self.assertEqual(sum(1 for _ in canonical_partitions_of_six()), 203)
        self.assertGreater(n, 2000)

    def test_fully_fixed_positive_class_cannot_be_claimed_zero(self):
        edges = ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2))
        L, R = original_sixset_forest_scope(edges)
        all_pairs = list(combinations(range(6), 2))
        with self.assertRaises(ValueError):
            proper_scope_zero_witness(
                edges, 6, dict(zip(L, all_pairs[:len(L)])),
                dict(zip(R, all_pairs[:len(R)])))
        with self.assertRaises(ValueError):
            free_site_bad_projection((0, 1, 2, 3, 4, 5),
                                     {i: all_pairs[i] for i in range(6)}, 6)
        with self.assertRaises(ValueError):
            free_site_bad_projection((0, 1, 2, 3, 4, 5), {0: (1, 0)}, 6)
        with self.assertRaises(ValueError):
            free_site_bad_projection((0, 1, 2, 3, 4, 5),
                                     {0: (0, 1), 1: (0, 1)}, 6)
        with self.assertRaises(ValueError):
            original_sixset_forest_scope(
                ((0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0)))

    def test_independent_full_original_W32_girth_8(self):
        model = fixture(1, "lex")
        edges = tuple(tuple(e) for e in model["incidences"])
        self.assertEqual(len(edges), 45)
        self.assertEqual(len(set(edges)), 45)
        self.assertEqual(len(set(p for p, _ in edges)), 15)
        self.assertEqual(len(set(l for _, l in edges)), 15)
        self.assertTrue(independently_no_short_cycle(edges))
        for subset in (edges[:6], edges[6:12], edges[12:18],
                       tuple(edges[i] for i in (0, 2, 6, 11, 19, 43))):
            L, R = original_sixset_forest_scope(subset)
            self.assertGreaterEqual(len(L)+len(R), 7)

    def test_true_W32_positive_GF5_seven_class_evaporates_on_all_sixsite_pins(self):
        # Original distinct six-incidence sets, NOT synthetic physical 6-cycles.
        for scheme in ("S68", "S72"):
            model = fixture(1, scheme)
            left, right, incidences, _ = validated_small_model(model)
            examples = {}
            positive = None
            for ids, kind in selected_left_six(model):
                if kind not in examples:
                    examples[kind] = ids
                if positive is None:
                    sig = _signature_for_original_sixset(ids, kind, incidences, left)
                    klass = cylinder_seven_class(sig, right)
                    if klass is not None:
                        positive = (ids, klass)
                if len(examples) == 3 and positive is not None:
                    break
            self.assertEqual(set(examples), {"A", "B", "C"})
            self.assertIsNotNone(positive)
            positive_ids, positive_klass = positive
            self.assertGreater(R3_CERTIFIED_FLOORS[positive_klass], 0)
            examples["positive"] = positive_ids
            for tag, ids in examples.items():
                Q = tuple(incidences[i] for i in ids)
                L, R = original_sixset_forest_scope(Q)
                scope = tuple(("L", i) for i in L) + tuple(("R", i) for i in R)
                self.assertGreaterEqual(len(scope), 7)
                for k in range(7):
                    for selected in (scope[:k], scope[len(scope)-k:]):
                        fixed_L = {v: left[v] for t, v in selected if t == "L"}
                        fixed_R = {v: right[v] for t, v in selected if t == "R"}
                        for a in (6, 14):
                            # For a=14 the W32 actual labels still sit inside K_6.
                            w = proper_scope_zero_witness(Q, a, fixed_L, fixed_R)
                            self.assertEqual(w["prescribed_size"], k)
                            self.assertFalse(w["left_two_regular"] and w["right_two_regular"])
                            self.assertEqual(w["seven_GF5_positive_indicator"], 0)
                            self.assertEqual(w["selected_nonnegative_GF5_weight"], 0)

    def test_critical_proper_subset_r_minus_one_cannot_survive(self):
        # 6 of 7 ORIGINAL typed sites pinned: at least one side can be invalidated.
        Q = ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2))
        L, R = original_sixset_forest_scope(Q)
        scope = tuple(("L", v) for v in L) + tuple(("R", v) for v in R)
        self.assertEqual(len(scope), 7)
        images = tuple(combinations(range(6), 2))
        for omitted in scope:
            remain = [z for z in scope if z != omitted]
            f = {v: images[i] for i, (t, v) in enumerate(z for z in remain if z[0] == "L")}
            g = {v: images[i] for i, (t, v) in enumerate(z for z in remain if z[0] == "R")}
            w = proper_scope_zero_witness(Q, 6, f, g)
            self.assertEqual(w["prescribed_size"], 6)
            self.assertFalse(w["left_two_regular"] and w["right_two_regular"])

    def test_machine_report_keeps_global_root_open(self):
        x = report()
        self.assertEqual(x["theorem"], "ALL-H-EVERY-PROPER-LOCAL-SCOPE-GF5-MINIMUM-ZERO")
        self.assertEqual(x["all_conditional_minima_for_k_le_6"], "ZERO")
        self.assertEqual(x["stronger_every_proper_scope_minimum"], "ZERO")
        self.assertFalse(x["general_Sherali_Adams_no_go"])
        self.assertEqual((x["Branch_A"], x["Branch_B"]), ("OPEN", "OPEN"))


if __name__ == "__main__":
    unittest.main()
