"""HYP-105 AA4-S independent all-h root-conditioned Frechet and true W32 oracles."""
from collections import Counter
from itertools import combinations
from math import comb, prod, isqrt
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4s_root_conditional_frechet import (
    minimal_physical_a, all_h_root_conditional_frechet_no_go,
    original_B_A_point_root, exact_true_W32_B_A_source_universe_by_root,
    real_W32_root_marginal_and_joint_audit,
)


class GenuineOriginalRootConditionedNoGoTests(unittest.TestCase):
    def test_001_minimal_Ka_unordered_pair_alphabet_all_h(self):
        for h in range(1,14):
            s=1<<h
            a=minimal_physical_a(s)
            V=(s+1)*(s*s+1)
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)

    def test_002_all_h_integer_strict_root_frechet_gap(self):
        for h in range(1,14):
            s=1<<h
            z=all_h_root_conditional_frechet_no_go(s)
            self.assertGreater(z["strict_universe_minus_both_marginal_caps"],0)
            self.assertEqual(z["best_possible_root_conditional_Frechet_lower"],0)
            self.assertEqual(
                z["strict_universe_minus_both_marginal_caps"],
                z["minimum_true_original_B_A_source_universe_per_root"]-
                z["maximum_left_physical_B_original_root_half"]-
                z["maximum_right_physical_A_global_half"])
            self.assertTrue(z["dual_A_left_B_right_same_no_go"])
            self.assertFalse(z["all_h_seven_S_omega_s6_PROVED"])

    def test_003_small_h_exact_constants_and_large_uniform_algebra(self):
        known={2:(6,58320,729,51030),
               4:(14,10127000000,9281250,3284531250)}
        for s,(a,n,l,r) in known.items():
            z=all_h_root_conditional_frechet_no_go(s)
            self.assertEqual((z["a"],
                z["minimum_true_original_B_A_source_universe_per_root"],
                z["maximum_left_physical_B_original_root_half"],
                z["maximum_right_physical_A_global_half"]), (a,n,l,r))
        for h in range(5,13):
            s=1<<h
            z=all_h_root_conditional_frechet_no_go(s)
            self.assertEqual(z["proof_mode"],"symbolic_uniform_s_ge_32")
            self.assertLessEqual(z["a"]**2,4*s**3)
            # Rigorous rational inequality used in the independent proof:
            self.assertGreater(48*s**3,1015625)
            self.assertGreaterEqual(
                768*z["minimum_true_original_B_A_source_universe_per_root"],
                s**18)

    def test_004_reject_incorrect_source_orders(self):
        for s in (1,3,5,0,-2,2.0,"4",True):
            with self.assertRaises(ValueError):
                minimal_physical_a(s)
        for s in (1,3,0,6,False):
            with self.assertRaises(ValueError):
                all_h_root_conditional_frechet_no_go(s)

    def test_005_exact_source_only_W32_universe_each_real_point_root(self):
        m=fixture(1,"lex")
        inc=tuple(tuple(e) for e in m["incidences"])
        universe=exact_true_W32_B_A_source_universe_by_root(inc)
        floor=all_h_root_conditional_frechet_no_go(2)[
            "minimum_true_original_B_A_source_universe_per_root"]
        self.assertEqual(len(universe),15)
        self.assertGreaterEqual(min(universe),floor)
        self.assertEqual(len(set(universe)),1) # actual true W32 point transitivity
        self.assertGreater(universe[0],floor)

    def test_006_independent_root_conditioned_join_on_historical_true_maps(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            result=real_W32_root_marginal_and_joint_audit(m)
            legacy=seven_census(m,independent_checks=False,witness_sets=True)
            joint=exact_two_sided_original_seven_join(m,independent_history=False)
            self.assertTrue(result["all_15_root_frechet_floors_zero"])
            self.assertEqual(result["actual_total_B_left_A_right"],
                             legacy["seven_class_motif_counts"]["B-left/A-right"])
            self.assertEqual(result["actual_total_B_left_A_right"],
                             joint["physical_projection_source_3x3_joint_matrix"]["B/A"])
            self.assertGreater(result["actual_total_B_left_A_right"],0)
            for record in result["per_true_original_root"].values():
                self.assertEqual(record["root_conditional_Frechet_lower"],0)
                self.assertGreater(
                    record["true_source_universe_BA_root"],
                    record["actual_left_B_source_root_margin"]+
                    record["actual_right_A_source_B_root_margin"])

    def test_007_global_complete_both_type_random_permutations_not_local_fake(self):
        edges=tuple(combinations(range(6),2))
        rng=random.Random(23000448)
        original=fixture(1,"S68")
        for _ in range(3):
            pl=list(edges);gl=list(edges)
            rng.shuffle(pl);rng.shuffle(gl)
            actual={**original,"left_labels":tuple(pl),"right_labels":tuple(gl)}
            z=real_W32_root_marginal_and_joint_audit(actual,exact_universe=False)
            joint=exact_two_sided_original_seven_join(actual,independent_history=False)
            self.assertTrue(z["all_15_root_frechet_floors_zero"])
            self.assertEqual(z["actual_total_B_left_A_right"],
                             joint["physical_projection_source_3x3_joint_matrix"]["B/A"])

    def test_008_falsifier_original_source_row_malformed(self):
        with self.assertRaises(ValueError):
            exact_true_W32_B_A_source_universe_by_root(((0,0),)*45)
        m=fixture(1,"S72")
        labels=list(m["left_labels"])
        labels[0]=labels[1]
        with self.assertRaises(ValueError):
            real_W32_root_marginal_and_joint_audit(
                {**m,"left_labels":tuple(labels)},exact_universe=False)

    def test_009_original_B_A_repeat_root_signature_is_unambiguous(self):
        m=fixture(1,"lex")
        inc=tuple(tuple(e) for e in m["incidences"])
        root=0
        js=[i for i,(p,l) in enumerate(inc) if p==root]
        self.assertEqual(len(js),3)
        self.assertIsNone(original_B_A_point_root(tuple(js),inc))
        some=[i for i,e in enumerate(inc) if e[0]!=root]
        exemplar=None
        for i,j in combinations(js,2):
            for Q4 in combinations(some,4):
                Q=tuple(sorted((i,j)+Q4))
                if original_B_A_point_root(Q,inc)==root:
                    exemplar=Q
                    break
            if exemplar is not None:
                break
        self.assertIsNotNone(exemplar)
        self.assertEqual(original_B_A_point_root(exemplar,inc),root)


if __name__=="__main__":
    unittest.main()
