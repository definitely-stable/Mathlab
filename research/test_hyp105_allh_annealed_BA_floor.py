"""Independent finite checks for the AA4-ANNBA all-h algebraic proof."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_allh_annealed_BA_floor import (
    annealed_original_BA_floor,
    exact_twofactor_count,
    exact_W32_original_B_source_distinct_line_count,
    falling,
    validate_typed_pairs,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


class TestAllHUniformAnnealedBA(unittest.TestCase):
    def test_independent_complete_K6_K7_twofactors_and_28_incidence_oracle(self):
        for a in (6,7):
            with self.subTest(a=a):
                full=exact_twofactor_count(a)
                self.assertEqual(full["2factor_count_unrestricted"],
                                 70*comb(a,6))
                self.assertEqual(full["allowed_2factor_edge_sets"],
                                 70*comb(a,6))
                self.assertEqual(
                    set(full["per_edge_2factor_counts"]),
                    set(combinations(range(a),2)))
                for edge in combinations(range(a),2):
                    self.assertEqual(full["per_edge_2factor_counts"][edge],
                                     28*comb(a-2,4))
                    remaining=exact_twofactor_count(a,(edge,))
                    self.assertEqual(
                        remaining["allowed_2factor_edge_sets"],
                        70*comb(a,6)-28*comb(a-2,4))
                # Two independently forbidden physical edges: union bound
                # must never exceed the exact small-alphabet surviving count.
                E=tuple(combinations(range(a),2))
                for F in (E[:2],(E[0],E[-1])):
                    x=exact_twofactor_count(a,F)
                    self.assertGreaterEqual(
                        x["allowed_2factor_edge_sets"],
                        max(0,70*comb(a,6)-len(F)*28*comb(a-2,4)))

    def test_C4_missing_edge_union_bound_independent_graph_oracle(self):
        # The proof applies to ANY globally injective f occupancy. We use
        # genuinely arbitrary missing-edge sets on K8, not GQ-specific f.
        a=8
        all_pairs=set(combinations(range(a),2))
        for missing in (
            set(),
            {(2,3)},
            {(2,3),(3,4)},
            {(0,2),(3,4),(5,6)},
        ):
            occupied=all_pairs-missing
            p=(0,1)
            self.assertIn(p,occupied)
            other=[x for x in range(a) if x not in p]
            actual=0
            for four in combinations(other,4):
                choices=tuple(combinations(four,2))
                for edges in combinations(choices,4):
                    deg={x:0 for x in four}
                    for x,y in edges:
                        deg[x]+=1;deg[y]+=1
                    if all(z==2 for z in deg.values()) and set(edges)<=occupied:
                        actual+=1
            lower=max(0,3*comb(a-2,4)-2*len(missing)*comb(a-4,2))
            self.assertGreaterEqual(actual,lower)

    def test_uniform_all_h_BA_asymptotic_and_frozen_source_cases(self):
        # Exact big integers: no regression fits, floating tolerance,
        # numerically evaluated singular value assumptions or randomness.
        for s in (2,4,8,16,32,64,128,256,512,1024):
            x=annealed_original_BA_floor(s)
            self.assertFalse(x["root_BRANCH_A_or_B_or_C_proved"])
            self.assertTrue(x["uniform_in_fixed_f_and_frozen_gJ"])
            self.assertEqual(
                x["conditional_expected_original_B_left_A_right_floor"],
                x["source_distinct_line_B_sixsets_floor"] *
                x["right_A_injection_probability_floor"])
            self.assertGreaterEqual(x["scaled_floor_over_s6"],0)
            if s>=8:
                self.assertGreater(x["scaled_floor_over_s6"],0)
        self.assertGreater(
            annealed_original_BA_floor(256)["scaled_floor_over_s6"],130)
        self.assertGreater(
            annealed_original_BA_floor(1024)["scaled_floor_over_s6"],138)
        self.assertEqual(annealed_original_BA_floor(4)["scaled_floor_over_s6"],
                         Fraction(0))
        self.assertEqual(
            annealed_original_BA_floor(16,frozen_count=12)[
                "scaled_floor_over_s6"],Fraction(0))
        self.assertGreater(
            annealed_original_BA_floor(32,frozen_count=12)[
                "scaled_floor_over_s6"],Fraction(0))
        self.assertGreater(
            annealed_original_BA_floor(1024,frozen_count=12)[
                "scaled_floor_over_s6"],130)

    def test_true_W32_lex_reverse_source_line_distinct_exact_expectation(self):
        # New all-h LOWER bound can be zero at s=2 (d=3), but the exact
        # conditional expectation is still independently accessible from
        # the historical complete 62,370 original sixset enumerator.
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                model=pair_labeled_symplectic(1,scheme)
                a=model["a"]
                M=comb(a,2)
                count=exact_W32_original_B_source_distinct_line_count(model)
                self.assertGreater(count[
                    "original_B_source_sixsets_all_distinct_unfrozen_lines"],0)
                self.assertLessEqual(count[
                    "original_B_source_sixsets_all_distinct_unfrozen_lines"],10935)
                r=exact_twofactor_count(a)
                p=Fraction(720*r["allowed_2factor_edge_sets"],
                           falling(M,6))
                expected=count[
                    "original_B_source_sixsets_all_distinct_unfrozen_lines"]*p
                self.assertGreater(expected,0)
                self.assertGreaterEqual(expected,
                    annealed_original_BA_floor(
                        2,point_labels=model["left_labels"])[
                            "conditional_expected_original_B_left_A_right_floor"])
                J=(0,)
                restricted=exact_W32_original_B_source_distinct_line_count(
                    model,J)
                F=(model["right_labels"][0],)
                a_oracle=exact_twofactor_count(a,F)
                exact_restricted_expectation=(
                    Fraction(720*a_oracle["allowed_2factor_edge_sets"],
                             falling(M-1,6)) *
                    restricted[
                        "original_B_source_sixsets_all_distinct_unfrozen_lines"]
                )
                self.assertGreaterEqual(exact_restricted_expectation,
                    annealed_original_BA_floor(
                        2,frozen_count=1,
                        point_labels=model["left_labels"],
                        frozen_labels=F)[
                            "conditional_expected_original_B_left_A_right_floor"])
                self.assertLessEqual(restricted[
                    "original_B_source_sixsets_all_distinct_unfrozen_lines"],
                    count["original_B_source_sixsets_all_distinct_unfrozen_lines"])

    def test_validation_fail_closed(self):
        model=pair_labeled_symplectic(1,"lex")
        with self.assertRaises(ValueError):
            annealed_original_BA_floor(3)
        with self.assertRaises(ValueError):
            annealed_original_BA_floor(2,frozen_count=-1)
        with self.assertRaises(ValueError):
            annealed_original_BA_floor(2,frozen_count=16)
        with self.assertRaises(ValueError):
            annealed_original_BA_floor(2,frozen_count=2,
                                      frozen_labels=((0,1),))
        with self.assertRaises(ValueError):
            validate_typed_pairs(2,[model["left_labels"][0]]*15)
        with self.assertRaises(ValueError):
            validate_typed_pairs(2,((0,1),(0,1)),partial=True)
        with self.assertRaises(ValueError):
            validate_typed_pairs(2,((0,6),),partial=True)


if __name__ == "__main__":
    unittest.main()
