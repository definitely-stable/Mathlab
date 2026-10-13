"""Independent D6-O original GQ B/C joint covariance falsifiers.

Independent physical B templates are constructed as repeated edge +
four-vertex cycle, never via selected_left_six. Independent C templates
use three physical disjoint doubled original points. Both select TRUE
original GQ incident lines. All arithmetic exact integer/Fraction.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
import unittest

from hyp105_issue230_d6o_joint_ba_ca_covariance import (
    original_sixline_weights_BC,
    original_mixed_overlap_spectrum, _moments_one_pair,
    genuine_W32_joint_BC_report,
)
from hyp105_issue230_d6n_exact_correlated_ca_overlap import (
    exact_right_A_overlap_kernel, ca_original_line_weights,
    ca_correlation_moments, _is_right_physical_A,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)


def physical_four_cycles(vertices):
    pairs=tuple(combinations(vertices,2))
    return [
        cycle for cycle in combinations(pairs,4)
        if all(sum(u in edge for edge in cycle)==2 for u in vertices)
    ]


def brute_original_BC_from_physical_templates(model):
    """Independent incidence-level true GQ B and C sixset census."""
    incidence_lines=[set() for _ in model["left_labels"]]
    for p,l in model["incidences"]:
        incidence_lines[p].add(l)
    physical=[tuple(edge) for edge in model["left_labels"]]
    inverse={p:i for i,p in enumerate(physical)}
    if len(inverse)!=len(physical):
        raise AssertionError("original fixed left injection malformed")
    out={"B": Counter(),"C": Counter()}
    universe=set(range(model["a"]))
    for repeated_point,pair in enumerate(physical):
        remain=tuple(sorted(universe-set(pair)))
        if len(remain)!=4:
            raise ValueError("independent finite B enumerator requires physical K6")
        for cycle in physical_four_cycles(remain):
            others=[inverse[edge] for edge in cycle]
            for selected in combinations(sorted(incidence_lines[repeated_point]),2):
                for singles in product(*(sorted(incidence_lines[p]) for p in others)):
                    lines=tuple(sorted(selected+singles))
                    if len(set(lines))==6:
                        out["B"][lines]+=1
    for triple in combinations(range(len(physical)),3):
        if any(set(physical[p])&set(physical[q])
               for p,q in combinations(triple,2)):
            continue
        for pairs in product(*(combinations(sorted(incidence_lines[p]),2)
                               for p in triple)):
            lines=tuple(sorted(l for pair in pairs for l in pair))
            if len(set(lines))==6:
                out["C"][lines]+=1
    return out


def direct_pair_overlap_spectrum(x,y):
    out=[0]*7
    for left,weight_l in x.items():
        mask=set(left)
        for right,weight_r in y.items():
            out[len(mask&set(right))]+=weight_l*weight_r
    return out


class ExactJointBACACovarianceTests(unittest.TestCase):
    def test_true_original_W32_two_independent_BC_generators(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                from_selected=original_sixline_weights_BC(model)
                independent=brute_original_BC_from_physical_templates(model)
                self.assertEqual(from_selected, independent)
                self.assertEqual(from_selected["C"],ca_original_line_weights(model))
                self.assertGreater(sum(from_selected["B"].values()),0)

    def test_independent_direct_ordered_BC_overlap_vs_binomial_inverse(self):
        for scheme in ("lex","reverse","S68","S72"):
            model=fixture(1,scheme)
            weights=brute_original_BC_from_physical_templates(model)
            for left,right in (("B","C"),("C","C")):
                with self.subTest(scheme=scheme,pair=left+right):
                    fast=original_mixed_overlap_spectrum(
                        weights[left],weights[right],15)
                    direct=direct_pair_overlap_spectrum(weights[left],
                                                         weights[right])
                    self.assertEqual(fast["ordered_overlap_spectrum"],direct)
                    moments=fast["extension_binomial_moments"]
                    for r in range(7):
                        self.assertEqual(
                            moments[r],
                            sum(comb(k,r)*direct[k] for k in range(r,7)))
            if scheme=="lex":
                self.assertEqual(
                    original_mixed_overlap_spectrum(
                        weights["B"],weights["B"],15
                    )["ordered_overlap_spectrum"],
                    direct_pair_overlap_spectrum(weights["B"],weights["B"]))

    def test_true_fixed_right_against_seven_GF5_classifier(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                weights=brute_original_BC_from_physical_templates(model)
                row=_moments_one_pair(weights,model["right_labels"],model["a"])
                census=seven_census(model,independent_checks=False,witness_sets=True)
                observed={
                    t: sum(m for six,m in weights[t].items()
                           if _is_right_physical_A(six,model["right_labels"]))
                    for t in ("B","C")}
                self.assertEqual(row["B"]["actual_fixed_g_directional_sixsets"],
                                 observed["B"])
                self.assertEqual(row["C"]["actual_fixed_g_directional_sixsets"],
                                 observed["C"])
                self.assertEqual(observed["B"],
                    census["seven_class_motif_counts"]["B-left/A-right"])
                ca_reverse=0
                for ids,tag in census["sets"].items():
                    if tag!="C/A":
                        continue
                    points=[model["incidences"][i][0] for i in ids]
                    if len(set(points))==6:
                        ca_reverse+=1
                self.assertEqual(observed["C"]+ca_reverse,
                                 census["seven_class_motif_counts"]["C/A"])
                numer=45600*observed["B"]+43320*observed["C"]
                self.assertEqual(
                    numer,row["GF5_selected_numerator_actual_fixed_g"])
                self.assertLessEqual(numer,census["GF5_seven_lower_numerator"])

    def test_exact_covariance_variance_and_G5_weighted_identity(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                weights=original_sixline_weights_BC(model)
                row=_moments_one_pair(weights,model["right_labels"],model["a"])
                # This exact C variance is sourced from an entirely separate
                # one-direction D6-N implementation with direct O(n^2) oracles.
                old=ca_correlation_moments(
                    weights["C"],model["right_labels"],model["a"])
                self.assertEqual(row["C"]["right_random_mean"],
                                 old["right_random_exact_mean"])
                self.assertEqual(row["C"]["right_random_variance"],
                                 old["right_random_exact_variance"])
                p=exact_right_A_overlap_kernel(model["a"])[
                    "single_A_probability"]
                q=exact_right_A_overlap_kernel(model["a"])[
                    "joint_A_probability_by_common_original_line_count"]
                mixed=direct_pair_overlap_spectrum(weights["B"],weights["C"])
                cross=sum((mixed[k]*q[k] for k in range(7)),Fraction())
                mean_B=Fraction(row["B"]["right_random_mean"])
                mean_C=Fraction(row["C"]["right_random_mean"])
                self.assertEqual(Fraction(row["joint_BC_second_moment"]),cross)
                self.assertEqual(Fraction(row["joint_BC_covariance"]),
                                 cross-mean_B*mean_C)
                var_B=Fraction(row["B"]["right_random_variance"])
                var_C=Fraction(row["C"]["right_random_variance"])
                cov=Fraction(row["joint_BC_covariance"])
                self.assertEqual(
                    Fraction(row["B_plus_C_right_random_variance"]),
                    var_B+var_C+2*cov)
                PZ=Fraction(
                    row["B_plus_C_random_right_P_positive_Paley_Zygmund"])
                self.assertTrue(0<PZ<=1)
                wb=R3_CERTIFIED_FLOORS["B-left/A-right"]
                wc=R3_CERTIFIED_FLOORS["C/A"]
                self.assertEqual(
                    Fraction(row["GF5_selected_numerator_right_random_mean"]),
                    wb*mean_B+wc*mean_C)
                self.assertEqual(
                    Fraction(row["GF5_selected_numerator_right_random_variance"]),
                    wb*wb*var_B+wc*wc*var_C+2*wb*wc*cov)
                self.assertEqual(
                    Fraction(row["GF5_selected_R3_expected_lower"]),
                    (wb*mean_B+wc*mean_C)/51**6)
                self.assertEqual(
                    row["separate_right_random_events_are_not_independent"],True)
                self.assertEqual(row["Branch_A"],"OPEN")
                self.assertEqual(row["Branch_B"],"OPEN")

    def test_synthetic_repeated_original_sixline_support_and_bad_input(self):
        x={(0,1,2,3,4,5):2,(1,2,3,4,5,6):3}
        y={(0,1,2,3,4,5):1,(2,3,4,5,6,7):4}
        got=original_mixed_overlap_spectrum(x,y,8)
        self.assertEqual(got["ordered_overlap_spectrum"],
                         direct_pair_overlap_spectrum(x,y))
        labels=tuple(combinations(range(6),2))[:8]
        row=_moments_one_pair({"B":x,"C":y},labels,6)
        self.assertEqual(row["B"]["original_sixsets_with_distinct_right_lines"],5)
        self.assertEqual(row["C"]["original_sixsets_with_distinct_right_lines"],5)
        self.assertEqual(Fraction(row["B"]["right_random_mean"]),
                         5*Fraction(70,5005))
        with self.assertRaises(ValueError):
            original_mixed_overlap_spectrum({(0,0,2,3,4,5):1},y,8)
        with self.assertRaises(ValueError):
            original_mixed_overlap_spectrum({(0,1,2,3,4,5):0},y,8)
        with self.assertRaises(ValueError):
            original_mixed_overlap_spectrum(x,{(2,3,4,5,6,8):1},8)
        with self.assertRaises(ValueError):
            _moments_one_pair({"B":x,"C":y},(labels[0],)*8,6)

    def test_report_never_promotes_random_right_to_all_fixed_g(self):
        report=genuine_W32_joint_BC_report()
        self.assertEqual(report["theorem"],
                         "ALL-FINITE-H-EXACT-MIXED-COVARIANCE")
        self.assertEqual(report["Branch_A"],"OPEN")
        self.assertEqual(report["Branch_B"],"OPEN")
        self.assertEqual(report["complete_W34_W38_seven_S"],"NOT-CLAIMED")
        self.assertEqual(len(report["cases"]),4)
        for row in report["cases"]:
            self.assertLessEqual(row["B_plus_C_actual_fixed_g"],
                                 row["true_full_seven_S"])


if __name__ == "__main__":
    unittest.main()
