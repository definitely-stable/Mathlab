"""B3.2-E1-C0 independent weighted six-hypergraph intersection falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six,validated_small_model,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets,source_weighted_BA_hypergraph,
    exact_BA_overlap,random_injection_expectation,
    finite_W32_overlap_report,generic_mass_only_countermodel,
)


def independent_degree2_target_K6():
    """Enumerate *all* C(15,6)=5005 physical six-edge subsets."""
    result=set()
    for es in combinations(tuple(combinations(range(6),2)),6):
        d=Counter(v for e in es for v in e)
        if len(d)==6 and all(x==2 for x in d.values()):
            result.add(frozenset(es))
    return result


def independent_BA_brute_original_sixsets(model):
    """Classify original endpoints and physical coordinates without m_f or index.

    Source enumerator only furnishes accepted LEFT-valid unordered
    original sixsets. The independent validator checks original
    left multiplicity B and right physical 6x2 condition directly.
    """
    left,right,edges,_=validated_small_model(model)
    source=Counter()
    overlap=0
    generatedB=0
    for ids,kind in selected_left_six(model):
        if kind!="B":
            continue
        generatedB+=1
        points=[edges[i][0] for i in ids]
        if sorted(Counter(points).values())!=[1,1,1,1,2]:
            raise AssertionError("left B profile mismatch")
        lines=tuple(edges[i][1] for i in ids)
        if len(set(lines))!=6:
            continue
        R=frozenset(lines)
        source[R]+=1
        deg=Counter(c for l in lines for c in right[l])
        if len(deg)==6 and all(v==2 for v in deg.values()):
            overlap+=1
    return source,overlap,generatedB


class WeightedIntersectionTests(unittest.TestCase):
    def test_independent_exhaustive_target_K6(self):
        expected=independent_degree2_target_K6()
        actual=simple_six_2factor_targets(6)
        self.assertEqual(len(expected),70)
        self.assertEqual(actual,frozenset(expected))
        self.assertEqual(Fraction(len(actual),comb(15,6)),Fraction(2,143))

    def test_W32_both_controls_with_true_original_incidence(self):
        target=independent_degree2_target_K6()
        for scheme,expected in (("lex",98),("reverse-line",77)):
            model=pair_labeled_symplectic(1,scheme)
            source,full_count,generatedB=independent_BA_brute_original_sixsets(model)
            weights=source_weighted_BA_hypergraph(model)
            self.assertEqual(generatedB,10935)
            self.assertEqual(weights,source)
            self.assertEqual(exact_BA_overlap(weights,model["right_labels"],
                                              target=target),expected)
            self.assertEqual(full_count,expected)
            self.assertEqual(seven_census(model,independent_checks=False)
                             ["seven_class_motif_counts"]["B-left/A-right"],expected)
            self.assertEqual(random_injection_expectation(
                weights,a=6,original_vertices=15),
                Fraction(sum(weights.values())*2,143))
            self.assertGreater(len(source),0)

    def test_actual_correlated_pair_edge_swap_intersection(self):
        from hyp105_g5e2b3e1b1b_label_swaps import swap_line_pair_labels
        model=pair_labeled_symplectic(1,"reverse-line")
        weights=source_weighted_BA_hypergraph(model)
        target=independent_degree2_target_K6()
        swapped=swap_line_pair_labels(model,4,13)
        # LEFT f and ORIGINAL source weights must NOT change:
        self.assertEqual(source_weighted_BA_hypergraph(swapped),weights)
        self.assertEqual(exact_BA_overlap(weights,model["right_labels"],
                                          target=target),77)
        self.assertEqual(exact_BA_overlap(weights,swapped["right_labels"],
                                          target=target),57)
        self.assertEqual(random_injection_expectation(
            weights,a=6,original_vertices=15),
            random_injection_expectation(
                source_weighted_BA_hypergraph(swapped),a=6,
                original_vertices=15))

    def test_generic_mass_alone_gives_no_positive_minimum(self):
        for mass in (1,2,13,100_000_000):
            result=generic_mass_only_countermodel(mass)
            self.assertEqual(result["min_attained_overlap"],0)
            self.assertEqual(result["positive_random_mean"],
                             str(Fraction(2*mass,143)))
            self.assertTrue(result["does_NOT_model_actual_GQ_source"])
        with self.assertRaises(ValueError):
            generic_mass_only_countermodel(0)

    def test_scope_and_invalid_images(self):
        report=finite_W32_overlap_report()
        self.assertEqual(report["target_K6_six_edge_2factor_sets"],70)
        self.assertEqual(report["target_K6_sixset_universe"],5005)
        self.assertEqual(report["actual_BA_overlap"],77)
        self.assertFalse(report["all_right_permutations_minimum_computed"])
        self.assertFalse(report["all_h_universal_BA_minimum_lower_proved"])
        for value in (0,3,15,True):
            with self.assertRaises(ValueError):
                simple_six_2factor_targets(value)
        with self.assertRaises(ValueError):
            exact_BA_overlap({frozenset(range(6)):1},[(0,1)]*15)
        with self.assertRaises(ValueError):
            random_injection_expectation(
                {frozenset(range(6)):1},a=6,original_vertices=16)


if __name__=="__main__":
    unittest.main()
