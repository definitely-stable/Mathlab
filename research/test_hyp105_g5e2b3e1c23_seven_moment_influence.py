"""C23 exact all-h physical twofactor templates, source means and swap."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import comb, perm, factorial
import unittest

from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c23_seven_moment_influence import (
    six_coordinate_multifactor_templates,
    local_pair_template_incidence_census,
    all_h_seven_global_right_swap_influence_upper,
    physical_right_shape_counts,
    exact_original_W32_static_seven_source,
    expected_common_global_right_seven_from_source,
    genuine_W32_C23_report,
)


class C23SevenMeanInfluenceTests(unittest.TestCase):
    def test_130_K6_multigraph_templates_independent_full_multiset_census(self):
        templates=six_coordinate_multifactor_templates()
        self.assertEqual({k:len(v) for k,v in templates.items()},
                         {"A":70,"B":45,"C":15})
        oracle=Counter()
        for six in combinations_with_replacement(PAIRS,6):
            degree=Counter(v for pair in six for v in pair)
            if len(degree)!=6 or set(degree.values())!={2}:
                continue
            profile=tuple(sorted(Counter(six).values(),reverse=True))
            category={(1,1,1,1,1,1):"A",(2,1,1,1,1):"B",
                      (2,2,2):"C"}.get(profile)
            self.assertIsNotNone(category)
            oracle[category]+=1
        self.assertEqual(oracle,{"A":70,"B":45,"C":15})
        self.assertEqual(local_pair_template_incidence_census()[
            "per_fixed_physical_pair_singleton"],40)
        self.assertEqual(local_pair_template_incidence_census()[
            "per_fixed_physical_pair_doubled"],6)

    def test_all_h_exact_source_upper_and_GF5_lipschitz(self):
        for s in (2,4,8,16,32,64,128):
            d=s+1
            info=all_h_seven_global_right_swap_influence_upper(s)
            a=info["a"]
            self.assertEqual(
                info["complete_physical_alphabet_all_left_source_upper"],
                comb(a,6)*(70*d**6+45*comb(d,2)*d**4+
                           15*comb(d,2)**3))
            self.assertEqual(
                info["two_swapped_original_right_lines_source_touched_upper"],
                2*comb(a-2,4)*(46*d**6-6*d**5))
            self.assertLessEqual(
                info["abs_global_right_swap_S_seven_delta_upper"],
                info["complete_physical_alphabet_all_left_source_upper"])
            self.assertEqual(
                info["abs_global_right_swap_GF5_seven_necessary_numerator_delta_upper"],
                info["abs_global_right_swap_S_seven_delta_upper"]*
                max(R3_CERTIFIED_FLOORS.values()))
            self.assertTrue(info["not_all_g_seven_lower"])
        self.assertEqual(
            all_h_seven_global_right_swap_influence_upper(2)[
                "complete_physical_alphabet_all_left_source_upper"],62370)
        for invalid in (0,1,3,True,9,"4"):
            with self.assertRaises(ValueError):
                all_h_seven_global_right_swap_influence_upper(invalid)

    def test_full_K6_physical_targets_and_GF4_missing_edge_gate(self):
        info=physical_right_shape_counts(6,PAIRS)
        self.assertEqual(tuple(info[k] for k in (
            "T_A_simple","T_B_one_double_C4",
            "T_C_three_doubled_matching","C6_simple")),(70,45,15,60))
        for edge in PAIRS[:5]:
            reduced=physical_right_shape_counts(
                6,[e for e in PAIRS if e!=edge])
            self.assertLess(reduced["T_A_simple"],70)
            self.assertLess(reduced["T_B_one_double_C4"],45)
            self.assertLess(reduced["T_C_three_doubled_matching"],15)
            self.assertLess(reduced["C6_simple"],60)
        from hyp105_g5e2b3e1c20_global_left_c6 import all_h_global_left_c6_lower
        s4=all_h_global_left_c6_lower(4)
        self.assertEqual(s4["minimal_physical_coordinates"],14)
        with self.assertRaises(ValueError):
            physical_right_shape_counts(15,tuple(combinations(range(15),2)))
        with self.assertRaises(ValueError):
            physical_right_shape_counts(6,PAIRS+PAIRS[:1])
        with self.assertRaises(ValueError):
            physical_right_shape_counts(6,[(1,0)])
        with self.assertRaises(ValueError):
            physical_right_shape_counts(6,PAIRS,max_six_coordinate_subsets=0)

    def test_uniform_global_right_class_probabilities_exact_independent(self):
        targets=physical_right_shape_counts(6,PAIRS)
        source={
            ("D6","A"):1,
            ("B-left/A-right","A"):1,
            ("A-left/B-right","B"):1,
            ("C/A","C"):1,
        }
        result=expected_common_global_right_seven_from_source(
            15,source,targets)
        p=result["probabilities_by_original_right_profile"]
        self.assertEqual(Fraction(p["D6"]),Fraction(1,5005))
        self.assertEqual(Fraction(p["A"]),Fraction(70,5005))
        self.assertEqual(Fraction(p["B"]),Fraction(3,1001))
        self.assertEqual(Fraction(p["C"]),Fraction(3,91))
        expected=sum((Fraction(p[k]) for k in ("D6","A","B","C")),
                     Fraction(0))
        self.assertEqual(
            Fraction(result["one_common_uniform_global_right_expected_seven_S"]),
            expected)
        self.assertTrue(result["one_common_global_g_linearity_not_witness_independence"])
        with self.assertRaises(ValueError):
            expected_common_global_right_seven_from_source(
                14,source,targets)
        with self.assertRaises(ValueError):
            expected_common_global_right_seven_from_source(
                15,{("D6","B"):1},targets)
        with self.assertRaises(ValueError):
            expected_common_global_right_seven_from_source(
                15,{("D6","A"):-1},targets)

    def test_genuine_W32_complete_true_original_seven_mean_and_weighted(self):
        src=exact_original_W32_static_seven_source()
        counts=src["source_by_seven_class_and_original_right_multiplicity"]
        self.assertEqual(src["original_six_incidence_source"],62370)
        self.assertEqual(src["eligible_six_incidence_source"],52309)
        self.assertEqual(sum(counts.values()),52309)
        report=genuine_W32_C23_report()
        mean=report["exact_mean"]
        probs=mean["probabilities_by_original_right_profile"]
        self.assertEqual(Fraction(probs["D6"]),Fraction(1,5005))
        expected_count=Fraction(0)
        expected_numerator=Fraction(0)
        for (tag,kind),n in counts.items():
            p=Fraction(probs["D6" if tag=="D6" else kind])
            expected_count+=n*p
            expected_numerator+=R3_CERTIFIED_FLOORS[tag]*n*p
        self.assertEqual(
            Fraction(mean["one_common_uniform_global_right_expected_seven_S"]),
            expected_count)
        self.assertEqual(
            Fraction(mean["one_common_uniform_global_right_GF5_necessary_numerator_mean"]),
            expected_numerator)
        self.assertGreaterEqual(
            expected_count,
            Fraction(report["C21_BA_plus_D6_uniform_lower"]))

    def test_right_target_probabilities_are_single_named_injection_not_6factorial_fluff(self):
        # Independent target direct injection for one original right-C
        # source: three named original lines each appearing twice.
        a=PAIRS
        total=0
        for ordered in permutations(range(15),3):
            deg=Counter(x for k in ordered for _ in (0,1) for x in a[k])
            total+=int(len(deg)==6 and set(deg.values())=={2})
        self.assertEqual(total,90)
        self.assertEqual(Fraction(total,perm(15,3)),Fraction(3,91))


if __name__=="__main__":
    unittest.main()
