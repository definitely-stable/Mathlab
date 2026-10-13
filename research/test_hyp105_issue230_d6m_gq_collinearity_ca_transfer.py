"""Independent ORIGINAL GF5 C/A expectation oracles; NO transport solver."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from random import Random
import unittest

from hyp105_issue230_d6m_gq_collinearity_ca_transfer import (
    exact_three_point_phi, exact_right_A_probability,
    universal_fixed_left_CA_expectation, exact_fixed_left_CA_profile,
    _collinearity_type,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def independent_original_point_line_sets(model):
    by_point=[set() for _ in model["left_labels"]]
    for p,l in model["incidences"]:
        by_point[p].add(l)
    return by_point


def independent_choose_two_per_point(point_line_sets, triple):
    """Enumerate actual original six-edge sets in the GQ, no Phi formula."""
    pools=[tuple(combinations(sorted(point_line_sets[p]),2)) for p in triple]
    result=0
    for chosen in product(*pools):
        distinct=set(x for pair in chosen for x in pair)
        if len(distinct)==6:
            result+=1
    return result


def independent_right_two_factor_count(a):
    """Count physical six-edge A 2-factors by unrelated brute K_a scan."""
    physical_pairs=tuple(combinations(range(a),2))
    if a!=6:
        raise ValueError("small independent A verifier only a=6")
    yes=0
    for six in combinations(physical_pairs,6):
        counts=Counter(v for pair in six for v in pair)
        if len(counts)==6 and set(counts.values())=={2}:
            yes+=1
    return yes,len(tuple(combinations(physical_pairs,6)))


def independent_finite_W32_class_C_A(model):
    """Full left C candidate scan, independent of main seven classifier."""
    by_point=independent_original_point_line_sets(model)
    incidence=model["incidences"]
    left=model["left_labels"]
    right=model["right_labels"]
    left_C=0
    right_distinct=0
    ca_directed_left_C_right_A=0
    ca_reverse_left_A_right_C=0
    for ids,tag in selected_left_six(model):
        if tag not in ("A","C"):
            continue
        ps=[incidence[i][0] for i in ids]
        rs=[incidence[i][1] for i in ids]
        if tag=="C":
            left_C+=1
            if len(set(ps))!=3 or set(Counter(ps).values())!={2}:
                raise AssertionError("selected_left_six C pattern violated")
            if len(set(rs))==6:
                right_distinct+=1
                degrees=Counter(v for i in ids for v in right[incidence[i][1]])
                if len(degrees)==6 and set(degrees.values())=={2}:
                    ca_directed_left_C_right_A+=1
        elif len(set(rs))==3 and set(Counter(rs).values())=={2}:
            physical=tuple(right[j] for j in set(rs))
            if len({v for pair in physical for v in pair})==6:
                ca_reverse_left_A_right_C+=1
    return (left_C,right_distinct,ca_directed_left_C_right_A,
            ca_reverse_left_A_right_C)


class ExactOriginalGQCollinearityTransferTests(unittest.TestCase):
    def test_independent_four_orbit_line_choice_exhaustion(self):
        for power in (1,2):
            model=fixture(power,"lex")
            by_point=independent_original_point_line_sets(model)
            formula=exact_three_point_phi(2**power)
            grouped={}
            n=len(by_point)
            for trio in combinations(range(n),3):
                typ=_collinearity_type(tuple(map(frozenset,by_point)),trio)
                grouped.setdefault(typ,trio)
                if len(grouped)==4:
                    break
            self.assertEqual(len(grouped),4)
            for typ,trio in grouped.items():
                with self.subTest(power=power,typ=typ):
                    brute=independent_choose_two_per_point(by_point,trio)
                    self.assertEqual(
                        brute,formula[
                          "six_distinct_right_original_lines_by_type"][typ])

    def test_right_A_probability_true_all_six_symbol_two_factors(self):
        yes,total=independent_right_two_factor_count(6)
        self.assertEqual(yes,70)
        self.assertEqual(total,5005)
        self.assertEqual(exact_right_A_probability(2),
                         Fraction(70,5005))

    def test_exact_C_A_true_original_W32_two_independent_oracles(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                profile=exact_fixed_left_CA_profile(model)
                left_C,right_distinct,leftC_rightA,leftA_rightC=(
                    independent_finite_W32_class_C_A(model))
                all_seven=seven_census(
                    model,independent_checks=False,witness_sets=True)
                self.assertEqual(left_C,405)
                self.assertEqual(left_C,
                                 profile["physical_left_C_matching_point_triples"]*27)
                self.assertEqual(right_distinct,
                    profile["exact_left_C_sixsets_with_six_distinct_original_right_lines"])
                self.assertEqual(
                    leftC_rightA+leftA_rightC,
                    all_seven["seven_class_motif_counts"]["C/A"])
                self.assertLessEqual(
                    leftC_rightA,all_seven["seven_class_motif_counts"]["C/A"])
                self.assertEqual(
                    profile["exact_expected_g_random_CA"],
                    str(Fraction(right_distinct)*Fraction(70,5005)))
                self.assertEqual(profile["s"],2)

    def test_true_original_W34_collinearity_profile_and_all_left_bounds(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                profile=exact_fixed_left_CA_profile(model)
                bound=universal_fixed_left_CA_expectation(4)
                count=profile["physical_left_C_matching_point_triples"]
                self.assertGreaterEqual(
                    count,bound["uniform_lower_physical_C_templates"])
                self.assertLessEqual(
                    count,bound["full_physical_C_templates"])
                expected=Fraction(profile["exact_expected_g_random_CA"])
                self.assertGreaterEqual(
                    expected,Fraction(bound["uniform_expected_CA_lower"]))
                self.assertLessEqual(
                    expected,Fraction(bound["uniform_expected_CA_upper"]))
                self.assertEqual(profile["original_GQ_incidences"],425)
                # This is an expectation over right g. Actual complete
                # seven-positive W34 target pool remains unknown.
                self.assertIsNone(profile["actual_fixed_global_right_g_CA"])
                # Independently sample actual W34 original point triples:
                # the exact Phi must not depend on physical labels.
                by_point=independent_original_point_line_sets(model)
                rng=Random(23062)
                for _ in range(10):
                    triple=tuple(sorted(rng.sample(range(len(by_point)),3)))
                    typ=_collinearity_type(
                        tuple(map(frozenset,by_point)),triple)
                    brute=independent_choose_two_per_point(by_point,triple)
                    self.assertEqual(
                        brute,exact_three_point_phi(4)[
                            "six_distinct_right_original_lines_by_type"][typ])

    def test_all_h_symbolic_bound_and_invalid_triangles(self):
        for s in (2,4,8,16,32,64,128,256):
            case=universal_fixed_left_CA_expectation(s)
            phi=exact_three_point_phi(s)
            self.assertEqual(
                case["phi"]["phi_min_all_original_GQ_point_triples"],
                phi["phi_min_all_original_GQ_point_triples"])
            self.assertGreater(
                Fraction(case["uniform_expected_CA_lower"]),0)
            self.assertLessEqual(
                Fraction(case["uniform_expected_CA_lower"]),
                Fraction(case["uniform_expected_CA_upper"]))
            self.assertFalse(case["all_g_or_root_Branch_A_proved"])
            self.assertEqual(case[
                "new_asymptotic_fixed_left_C_A_mean_coefficient"],"35/3")
        with self.assertRaises(ValueError):
            exact_three_point_phi(3)
        # Fake 6-cycle of point-line incidence would be a NON-GQ
        # triangle; the theorem rejects it rather than misclassifying.
        bad=({0,1},{0,2},{1,2})
        with self.assertRaises(AssertionError):
            _collinearity_type(tuple(map(frozenset,bad)),(0,1,2))


if __name__=="__main__":
    unittest.main()
