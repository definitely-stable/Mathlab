"""AA4-W independent all-h original-full-global seven-GF5 transfer tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations
from math import comb,factorial
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import _K6_2factors
from hyp105_issue230_d6aa4u_source_forest_frechet import CELL_NAMES
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    TAGS, all_h_full_seven_one_global_map_transfer_probabilities,
    one_fixed_side_full_seven_ensemble,
    two_uniform_complete_global_maps_full_seven_expectation,
    genuine_W32_fixed_full_map_all_seven_transfer,
)

TRUE_SOURCE_UNIVERSE_32={
    "A/A":1566360,"A/B":1666980,"B/A":1666980,
    "A/C":6225,"C/A":6225,"B/C":5220,"C/B":5220,
    "B/B-overlap":910080,"B/B-disjoint":707580,
}


class OriginalFullSevenQuenchedKernelTests(unittest.TestCase):
    def test_001_all_h_rational_one_global_injection_source_transfer(self):
        for h in range(1,15):
            s=1<<h
            p=all_h_full_seven_one_global_map_transfer_probabilities(s)
            a,K=p["a"],p["K"]
            self.assertLess(comb(a-1,2),(s+1)*(s*s+1))
            self.assertGreaterEqual(K,(s+1)*(s*s+1))
            F=lambda n,k:factorial(n)//factorial(n-k)
            ph=Fraction(F(a,6),F(K,6))
            pa=70*ph
            pb=Fraction(K*3*comb(a-2,4)*24,F(K,5))
            pc=Fraction(F(a,6),8*F(K,3))
            self.assertEqual(
                (p["D6_position_matched_connected_H"],
                 p["A_any_connected_or_disconnected_physical_2factor"],
                 p["B_same_source_repeated_plus_physical_C4"],
                 p["C_three_source_repeats_physical_matching"]),
                (ph,pa,pb,pc))
            self.assertTrue(p["one_single_uniform_full_global_map_all_six_Q"])
            self.assertFalse(p["all_h_root_minimin_proved"])

    def test_002_independent_physical_K6_numerators_A_B_C_and_single_H(self):
        P=all_h_full_seven_one_global_map_transfer_probabilities(2)
        self.assertEqual(P["D6_position_matched_connected_H"],Fraction(1,5005))
        self.assertEqual(P["A_any_connected_or_disconnected_physical_2factor"],
                         Fraction(2,143))
        self.assertEqual(P["B_same_source_repeated_plus_physical_C4"],
                         Fraction(3,1001))
        self.assertEqual(P["C_three_source_repeats_physical_matching"],
                         Fraction(3,91))
        edges=tuple(combinations(range(6),2))
        # Direct physical K6 six-edge 2factor subsets, independently of
        # frozen 70 kernel: each distinct selected edge sextuple is 6!.
        A=[x for x in combinations(edges,6)
           if Counter(v for e in x for v in e)==Counter({v:2 for v in range(6)})]
        self.assertEqual(len(A),70)
        self.assertEqual(len(_K6_2factors()),70)
        self.assertEqual(Fraction(len(A)*factorial(6),factorial(15)//factorial(9)),
                         Fraction(2,143))
        # FIVE different source factors, one root B-label and four ordered
        # C4 edges within the complement of that one unordered pair.
        B=0
        for root in edges:
            rest=tuple(i for i in range(6) if i not in root)
            for assigned in permutations(
                tuple(e for e in edges if set(e).issubset(rest)),4):
                degree=Counter(v for e in assigned for v in e)
                if len(degree)==4 and set(degree.values())=={2}:
                    B+=1
        self.assertEqual(B,15*3*factorial(4))
        self.assertEqual(Fraction(B,factorial(15)//factorial(10)),Fraction(3,1001))
        # THREE distinct original factors: ordered pairwise disjoint
        # physical image pair labels, direct 15*14*13 enumeration.
        C=sum(1 for a,b,c in permutations(edges,3)
              if len(set(a+b+c))==6)
        self.assertEqual(C,90)
        self.assertEqual(Fraction(C,15*14*13),Fraction(3,91))

    def test_003_all_nine_source_forest_nonAA_and_51palette_exact_both_uniform(self):
        full=two_uniform_complete_global_maps_full_seven_expectation(
            2,TRUE_SOURCE_UNIVERSE_32)
        self.assertEqual(set(full["exact_tag_expectations"]),set(TAGS))
        self.assertEqual(full["exact_tag_expectations"]["D6"],
                         Fraction(3759264,1002001))
        self.assertEqual(full["exact_expected_seven_S"],
                         Fraction(165129984,1002001))
        self.assertGreater(full["exact_expected_seven_S"],160)
        self.assertLess(full["exact_expected_seven_S"],170)
        self.assertTrue(full["does_NOT_imply_all_f_g_lower"])
        for h in (1,2,3,4,5):
            z=two_uniform_complete_global_maps_full_seven_expectation(
                1<<h,TRUE_SOURCE_UNIVERSE_32)
            self.assertGreaterEqual(z["exact_expected_seven_S"],0)

    def test_004_true_original_S68_S72_lex_reverse_both_typed_fixed_ensembles(self):
        actual={"S68":68,"S72":72,"lex":259,"reverse":169}
        for scheme,score in actual.items():
            for fixed_side in (0,1):
                model=fixture(1,scheme)
                d=genuine_W32_fixed_full_map_all_seven_transfer(
                    model,fixed_side=fixed_side)
                self.assertEqual(d["actual_one_specified_global_pair_seven_S"],score)
                self.assertEqual(sum(d["true_FIXED_original_source_forest_half"].values())+
                                 d["genuine_fixed_one_half_source_Q_OUTSIDE_joint_nine_grid"],
                                 62370)
                self.assertEqual(set(d["expected_full_seven_tag_counts"]),set(TAGS))
                self.assertGreater(d["expected_full_seven_S"],0)
                self.assertGreater(d["expected_full_selected_51palette_numerator"],0)
                self.assertTrue(d["all_h_conditional_exact_full_seven_kernel"])
                self.assertFalse(d["uniform_all_h_adversarial_pair_lower_PROVED"])
                self.assertEqual(d["independent_true_global_pair_GF5_history"],"PASS")

    def test_005_one_fixed_original_type_same_image_random_others_does_not_change_mean(self):
        rng=random.Random(23000437)
        edges=list(combinations(range(6),2))
        baseline=fixture(1,"S68")
        a=genuine_W32_fixed_full_map_all_seven_transfer(
            baseline,fixed_side=0,independent_history=False)
        for _ in range(5):
            rng.shuffle(edges)
            m={**baseline,"right_labels":tuple(edges)}
            b=genuine_W32_fixed_full_map_all_seven_transfer(
                m,fixed_side=0,independent_history=False)
            self.assertEqual(a["expected_full_seven_tag_counts"],
                             b["expected_full_seven_tag_counts"])
            self.assertEqual(a["expected_full_seven_S"],b["expected_full_seven_S"])
            self.assertEqual(a["expected_full_selected_51palette_numerator"],
                             b["expected_full_selected_51palette_numerator"])
        # This is a conditional expectation; varying right g changes the
        # real full seven score but not its fixed-left one-global-g average.
        self.assertNotEqual(a["expected_full_seven_S"],
                            Fraction(a["actual_one_specified_global_pair_seven_S"]))

    def test_006_same_global_right_map_fixed_on_line_side_against_random_left(self):
        rng=random.Random(23000438)
        edges=list(combinations(range(6),2))
        baseline=fixture(1,"S72")
        a=genuine_W32_fixed_full_map_all_seven_transfer(
            baseline,fixed_side=1,independent_history=False)
        for _ in range(4):
            rng.shuffle(edges)
            m={**baseline,"left_labels":tuple(edges)}
            b=genuine_W32_fixed_full_map_all_seven_transfer(
                m,fixed_side=1,independent_history=False)
            self.assertEqual(a["expected_full_seven_tag_counts"],
                             b["expected_full_seven_tag_counts"])
            self.assertEqual(a["expected_full_seven_S"],b["expected_full_seven_S"])

    def test_007_zero_C_C_true_GQ_and_fail_closed_fake_source_or_noninjectivity(self):
        x=fixture(1,"lex")
        wrong={**x,"incidences":tuple((p,l) for l in range(15)
                                    for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            genuine_W32_fixed_full_map_all_seven_transfer(wrong)
        bad=list(x["left_labels"]);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            genuine_W32_fixed_full_map_all_seven_transfer(
                {**x,"left_labels":tuple(bad)})
        with self.assertRaises(ValueError):
            one_fixed_side_full_seven_ensemble(2,{"B/B-overlap":1},2)
        with self.assertRaises(ValueError):
            one_fixed_side_full_seven_ensemble(2,{"C/C":1},0)
        with self.assertRaises(ValueError):
            one_fixed_side_full_seven_ensemble(2,{},0,fixed_side=2)

    def test_008_seeded_complete_global_both_types_independent_oracles(self):
        rng=random.Random(23000439)
        edges=list(combinations(range(6),2))
        base=fixture(1,"lex")
        for _ in range(4):
            left=edges[:];right=edges[:]
            rng.shuffle(left);rng.shuffle(right)
            model={**base,"left_labels":tuple(left),"right_labels":tuple(right)}
            a=genuine_W32_fixed_full_map_all_seven_transfer(
                model,fixed_side=0)
            b=genuine_W32_fixed_full_map_all_seven_transfer(
                model,fixed_side=1)
            z=seven_census(model,independent_checks=False)
            self.assertEqual(a["actual_one_specified_global_pair_seven_S"],z["S_seven"])
            self.assertEqual(b["actual_one_specified_global_pair_seven_S"],z["S_seven"])
            self.assertEqual(
                a["actual_one_specified_global_pair_51palette_numerator"],
                z["GF5_seven_lower_numerator"])
            self.assertEqual(
                b["actual_one_specified_global_pair_51palette_numerator"],
                z["GF5_seven_lower_numerator"])
            self.assertTrue(a["random_other_side_single_complete_global_injection"]
                            if "random_other_side_single_complete_global_injection" in a
                            else a["all_h_conditional_exact_full_seven_kernel"])


if __name__=="__main__":
    unittest.main()
