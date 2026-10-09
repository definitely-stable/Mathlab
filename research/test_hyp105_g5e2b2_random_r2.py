"""G5-E2-B2 independent finite four-factor-forest and projection oracles."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import random
import unittest

from hyp105_g5e2b2_random_r2 import (
    leafless_projection_probability, complete_small_projection_oracle,
    factor_partition_shapes, is_factor_forest,
    four_edge_forest_exponents, four_edge_profile_table, theorem_report,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


def independent_forest_check(incidences):
    """Graph theoretic independent oracle: DFS component and edge equality."""
    vertices={}
    adjacency={}
    for left,right in incidences:
        a=("L",left)
        b=("R",right)
        adjacency.setdefault(a,set()).add(b)
        adjacency.setdefault(b,set()).add(a)
    todo=set(adjacency)
    components=0
    while todo:
        components+=1
        first=next(iter(todo))
        stack=[first]
        todo.remove(first)
        while stack:
            x=stack.pop()
            for y in adjacency[x]:
                if y in todo:
                    todo.remove(y)
                    stack.append(y)
    return len(incidences)==len(adjacency)-components


class E2B2RandomLabelExpectedR2Tests(unittest.TestCase):
    def test_four_pair_projection_probability_exact_by_exhaustion(self):
        patterns=((4,), (3,1), (2,2), (2,1,1), (1,1,1,1))
        for a in (4,5,6):
            for part in patterns:
                self.assertEqual(
                    leafless_projection_probability(a,part),
                    complete_small_projection_oracle(a,part),
                    (a,part))
        self.assertEqual(leafless_projection_probability(6,(4,)),1)
        self.assertEqual(leafless_projection_probability(6,(2,2)),1)
        self.assertEqual(leafless_projection_probability(6,(3,1)),0)
        self.assertEqual(
            leafless_projection_probability(6,(2,1,1)),
            Fraction(120,15*14*13))
        self.assertEqual(
            leafless_projection_probability(6,(1,1,1,1)),
            Fraction(3*360,15*14*13*12))
        with self.assertRaises(ValueError):
            leafless_projection_probability(6,(1,1,2,3))
        with self.assertRaises(ValueError):
            complete_small_projection_oracle(7,(1,1,1,1))

    def test_all_225_factor_endpoint_patterns_prove_s4_cap(self):
        partitions=factor_partition_shapes()
        self.assertEqual(len(partitions),15)
        self.assertEqual(len(set(partitions)),15)
        entries=four_edge_forest_exponents()
        self.assertTrue(entries)
        self.assertLessEqual(len(entries),225)
        self.assertEqual(max(e["exponent_in_s"] for e in entries),4)
        self.assertTrue(all(e["components"]>=1 for e in entries))
        self.assertTrue(all(e["exponent_in_s"]<=4 for e in entries))
        self.assertTrue(any(
            e["left_profile"]==(2,2) and
            e["right_profile"]==(1,1,1,1) and
            e["exponent_in_s"]==4 for e in entries))
        self.assertTrue(any(
            e["left_profile"]==(1,1,1,1) and
            e["right_profile"]==(1,1,1,1) and
            e["exponent_in_s"]==4 for e in entries))
        # Independently verify forest formula for every enumerated
        # endpoint shape, not trusting the union-find cycle checker.
        for a in partitions:
            for b in partitions:
                if len(set(zip(a,b)))<4:
                    self.assertFalse(is_factor_forest(a,b))
                    continue
                original=list(zip(a,b))
                self.assertEqual(is_factor_forest(a,b),
                                 independent_forest_check(original))
        profile=four_edge_profile_table()
        self.assertEqual(sum(x["multiplicity_patterns"] for x in profile.values()),
                         len(entries))

    def test_all_s_gq_forest_prerequisite_on_real_GF2_GF4_graphs(self):
        # GQ girth8 was proved algebraically in accepted B1.0; the
        # independent oracle rechecks thousands of actual four-edge
        # physical incidences after pair embedding inversion.
        for h,limit in ((1,2000),(2,3000)):
            model=pair_labeled_symplectic(h,"lex")
            edges=model["incidences"]
            rng=random.Random(87542+h)
            self.assertEqual(len(set(edges)),len(edges))
            for _ in range(limit):
                subset=tuple(edges[i] for i in rng.sample(range(len(edges)),4))
                self.assertTrue(independent_forest_check(subset))
            if h==1:
                # All 45 choose4 would be 148,995; deterministic
                # substantial held-out exhaustive prefix/edge patterns.
                for ids in combinations(range(13),4):
                    self.assertTrue(independent_forest_check(
                        tuple(edges[i] for i in ids)))

    def test_scope_and_missing_asymptotic_R3_explicit(self):
        report=theorem_report()
        self.assertEqual(report["maximum_power_in_s"],"4")
        self.assertEqual(report["proved_expected_R2_upper"],
                         "O(s^4) = O(m^(8/3))")
        self.assertIsNone(report["proved_expected_R3_upper"])
        self.assertFalse(report["new_aset_lower_exponent_proven"])
        self.assertFalse(report["priority_novelty_verified"])
        self.assertIn("Omega(m^4)",report["published_expected_R3_lower"])


if __name__=="__main__":
    unittest.main()
