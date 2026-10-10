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
    physical_target_two_point_design,one_degree_source_overlap_invariant,
    two_marginal_blind_cube_trade,physical_target_three_point_orbits,
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

    def test_independent_K6_and_K9_target_two_point_signature(self):
        for a in (6,9):
            T=simple_six_2factor_targets(a)
            edges=tuple(combinations(range(a),2))
            d=Counter()
            adjacent=Counter()
            disjoint=Counter()
            for six in T:
                for e in six:
                    d[e]+=1
                for e,f in combinations(sorted(six),2):
                    (adjacent if len(set(e)&set(f)) else disjoint)[(e,f)]+=1
            expected=physical_target_two_point_design(a)
            self.assertEqual(len(T),
                             expected["physical_six_2factor_target_size"])
            self.assertEqual(set(d.values()),
                             {expected["target_degree_each_pair_label"]})
            for e,f in combinations(edges,2):
                key=tuple(sorted((e,f)))
                observed=(adjacent if set(e)&set(f) else disjoint)[key]
                oracle=(expected["pair_codegree_adjacent_physical_labels"]
                        if set(e)&set(f) else
                        expected["pair_codegree_disjoint_physical_labels"])
                self.assertEqual(observed,oracle)
            self.assertEqual(expected["target_is_two_design"],a==9)

    def test_K14_nontrivial_two_orbit_second_component(self):
        values=physical_target_two_point_design(14)
        self.assertEqual(values["a"],14)
        self.assertTrue(values["target_is_one_design"])
        self.assertFalse(values["target_is_two_design"])
        self.assertTrue(values["uniform_target_component_W1_zero"])
        self.assertEqual(values["target_degree_each_pair_label"],
                         28*comb(12,4))
        self.assertEqual(values["pair_codegree_adjacent_physical_labels"],
                         7*comb(11,3))
        self.assertEqual(values["pair_codegree_disjoint_physical_labels"],
                         14*comb(10,2))

    def test_full_physical_third_orbit_census_K6_and_K9(self):
        """Complete 455 K6 and 7140 K9 physical three-edge subsets."""
        for a in (6,9):
            target=simple_six_2factor_targets(a)
            palette=tuple(combinations(range(a),2))
            observed=Counter()
            for physical_six in target:
                for triplet in combinations(sorted(physical_six),3):
                    observed[triplet]+=1
            data=physical_target_three_point_orbits(a)
            orbit_counts=Counter()
            for tr in combinations(palette,3):
                degrees=Counter(v for e in tr for v in e)
                n=len(degrees)
                signature=tuple(sorted(degrees.values(),reverse=True))
                if n==3 and signature==(2,2,2):
                    kind="triangle"
                elif n==4 and signature==(2,2,1,1):
                    kind="path_P4"
                elif n==4 and signature==(3,1,1,1):
                    kind="star_K1_3"
                elif n==5 and signature==(2,1,1,1,1):
                    kind="path_P3_plus_edge"
                elif n==6 and signature==(1,1,1,1,1,1):
                    kind="matching_3"
                else:
                    self.fail("unknown three-physical-pair orbit")
                orbit_counts[kind]+=1
                ids=tuple(palette.index(e) for e in tr)
                self.assertEqual(observed[ids],
                                 data["target_triple_label_orbits"][kind]["codegree"])
            self.assertEqual(
                dict(orbit_counts),
                {k:v["orbit_cardinality"]
                 for k,v in data["target_triple_label_orbits"].items()})
            self.assertEqual(sum(observed.values()),20*len(target))
        # Host a=14 from W(3,4), large arithmetic only; no complete
        # physical 6set scan with 3e6 target hyperedges required.
        target14=physical_target_three_point_orbits(14)
        self.assertTrue(target14["exact_all_a_census_proved"])
        self.assertFalse(target14["all_correlated_right_min_lower_proved"])
        for bad in (0,5,True):
            with self.assertRaises(ValueError):
                physical_target_three_point_orbits(bad)

    def test_exact_degree_one_source_permutation_invariance_K6(self):
        a=6
        edges=tuple(combinations(range(a),2))
        T=independent_degree2_target_K6()
        K=len(edges)
        coeff=tuple((i*17)%29 for i in range(K))
        constant=9
        expected=one_degree_source_overlap_invariant(a,constant,coeff)
        for mapping in (
            tuple(range(K)),
            tuple(reversed(range(K))),
            tuple((i+7)%K for i in range(K)),
        ):
            observed=0
            for R in combinations(range(K),6):
                weight=constant+sum(coeff[i] for i in R)
                if frozenset(edges[mapping[i]] for i in R) in T:
                    observed+=weight
            self.assertEqual(observed,expected)
        self.assertEqual(expected,constant*70+28*sum(coeff))

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

    def test_pair_marginals_cannot_determine_exact_target_overlap(self):
        """Independent 8-corner K6 trade and exact 0,1,2 marginals."""
        palette=tuple(combinations(range(6),2))
        T=independent_degree2_target_K6()
        shared=(0,1,6)
        flip=((2,11),(3,12),(13,14))
        corners={}
        for mask in range(8):
            R=frozenset(shared+tuple(flip[j][(mask>>j)&1]
                                     for j in range(3)))
            corners[R]=mask
        self.assertEqual(len(corners),8)
        for scale in (1,17,1_000_000):
            m_even={R:scale for R,mask in corners.items()
                    if not mask.bit_count()%2}
            m_odd={R:scale for R,mask in corners.items()
                   if mask.bit_count()%2}
            for k in (0,1,2):
                def marginal(source):
                    out=Counter()
                    for R,w in source.items():
                        for subset in combinations(sorted(R),k):
                            out[subset]+=w
                    return out
                self.assertEqual(marginal(m_even),marginal(m_odd))
            self.assertEqual(sum(m_even.values()),4*scale)
            self.assertEqual(sum(m_odd.values()),4*scale)
            self.assertEqual(exact_BA_overlap(m_even,palette,target=T),0)
            self.assertEqual(exact_BA_overlap(m_odd,palette,target=T),scale)
            self.assertEqual(random_injection_expectation(
                m_even,a=6,original_vertices=15),
                random_injection_expectation(
                    m_odd,a=6,original_vertices=15))
            report=two_marginal_blind_cube_trade(scale)
            self.assertEqual(report["overlap_gap"],scale)
            self.assertFalse(report["actual_W3s_incidence_source"])
        with self.assertRaises(ValueError):
            two_marginal_blind_cube_trade(False)

    def test_actual_correlated_pair_edge_swap_intersection(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        weights=source_weighted_BA_hypergraph(model)
        target=independent_degree2_target_K6()
        # Self-contained real ORIGINAL right-factor reassignment; no
        # import from not-yet-merged PR #242.
        r=list(model["right_labels"])
        r[4],r[13]=r[13],r[4]
        swapped=dict(model)
        swapped["right_labels"]=tuple(r)
        a=model["a"]
        swapped["supports"]=tuple(tuple(sorted(
            model["left_labels"][p]+tuple(a+v for v in r[l])))
            for p,l in model["incidences"])
        # LEFT f and ORIGINAL source weights must NOT change:
        self.assertEqual(source_weighted_BA_hypergraph(swapped),weights)
        self.assertEqual(exact_BA_overlap(weights,model["right_labels"],
                                          target=target),77)
        self.assertEqual(exact_BA_overlap(weights,swapped["right_labels"],
                                          target=target),57)
        self.assertEqual(seven_census(swapped,independent_checks=False)
                         ["seven_class_motif_counts"]["B-left/A-right"],57)
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
