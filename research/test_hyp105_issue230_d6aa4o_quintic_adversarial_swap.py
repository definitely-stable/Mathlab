"""D6-AA4-O original five-source tensor and exact swap adversarial tests."""
import random
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4n_quenched_right_transfer import (
    original_W32_fixed_g_right_A_counter)
from hyp105_issue230_d6aa4o_quintic_adversarial_swap import (
    true_original_W32_fixed_g_weighted_tensor,
    exact_original_BA_energy,exact_swap_gradient,
    exhaustive_one_swap_frontier,descend_true_original_W32,
    true_W32_quintic_swap_report,
)


class TrueOriginalQuinticSwapTests(unittest.TestCase):
    def test_001_true_W32_all_four_fixed_right_g_tensor_coefficients(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            t=true_original_W32_fixed_g_weighted_tensor(m)
            right=original_W32_fixed_g_right_A_counter(m)
            self.assertEqual(sum(w for x,w in t["terms"]),right[
                "right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"])
            self.assertEqual(t["total_original_BA_true_right_A_internal_Q_T_g"],
                             sum(w for x,w in t["terms"]))
            self.assertEqual(len(t["incident_term_indices"]),15)
            self.assertEqual(t["positive_probability_full_left_B"],"3/1001")
            self.assertGreater(t["five_point_support_count"],0)
            self.assertGreater(t["max_original_Q_multiplicity_per_five_point_support"],0)
            self.assertEqual(sum(len(set(x))==5 for x,w in t["terms"]),len(t["terms"]))
            self.assertEqual(sum(len(ix) for ix in t["incident_term_indices"]),
                             5*len(t["terms"]))

    def test_002_all_105_transpositions_exact_brute_score_difference(self):
        rng=random.Random(2300471)
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            t=true_original_W32_fixed_g_weighted_tensor(m)
            for _ in range(2):
                labels=list(m["left_labels"])
                rng.shuffle(labels)
                labels=tuple(labels)
                initial=exact_original_BA_energy(t,labels)
                for u,v in combinations(range(15),2):
                    delta=exact_swap_gradient(t,labels,u,v)
                    swapped=list(labels)
                    swapped[u],swapped[v]=swapped[v],swapped[u]
                    self.assertEqual(
                        exact_original_BA_energy(t,swapped)-initial,
                        delta)
                f=exhaustive_one_swap_frontier(t,labels)
                self.assertEqual(f["all_original_complete_map_pair_swaps"],105)
                self.assertTrue(f["exact_swaps_preserve_global_source_injectivity"])

    def test_003_steepest_adversarial_swaps_preserve_TRUE_original_seven_GF5(self):
        for scheme in ("S68","S72"):
            r=true_W32_quintic_swap_report(scheme,random_starts=0)
            self.assertEqual(r["scheme"],scheme)
            self.assertTrue(r["not_a_global_minimum_certificate"])
            self.assertTrue(r["one_true_complete_fixed_original_line_mapping"])
            self.assertTrue(r["all_15_global_source_point_labels_are_distinct"])
            self.assertEqual(len(r["search_results"]),1)
            z=r["search_results"][0]
            self.assertLessEqual(z["final_real_BA_charge"],z["initial_real_BA_charge"])
            self.assertTrue(z["all_105_original_point_pair_label_swap_gradient_nonnegative"])
            self.assertGreaterEqual(z["certified_final_minimum_exact_swap_delta"],0)
            self.assertEqual(
                z["independent_historical_full_original_GF5_final_internal_charge"],
                z["final_real_BA_charge"])
            self.assertEqual(z["independent_62370_original_sixsets_before_after"],"PASS")
            self.assertEqual(len(set(tuple(x) for x in z[
                "final_globally_injective_point_labels"])),15)
            self.assertTrue(z["not_claimed_globally_optimal"])
            self.assertTrue(z["not_claimed_all_h_charge_zero"])

    def test_004_real_original_BASELINE_GF5_seven_census_from_weighted_tensor(self):
        from collections import Counter
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            t=true_original_W32_fixed_g_weighted_tensor(m)
            full=seven_census(m,independent_checks=False,witness_sets=True)
            expected=0
            for Q,tag in full["sets"].items():
                if tag!="B-left/A-right":continue
                pair=tuple(m["incidences"][k] for k in Q)
                roots=Counter(p for p,l in pair)
                p=next(p for p,n in roots.items() if n==2)
                lines=tuple(l for u,l in pair if u==p)
                expected+=not(set(m["right_labels"][lines[0]])&
                              set(m["right_labels"][lines[1]]))
            self.assertEqual(expected,exact_original_BA_energy(t,m["left_labels"]))
            self.assertLessEqual(expected,full["S_seven"])

    def test_005_global_random_complete_maps_same_g_energy_nonnegative(self):
        rng=random.Random(2300472)
        m=fixture(1,"S72")
        t=true_original_W32_fixed_g_weighted_tensor(m)
        labels=list(m["left_labels"])
        for _ in range(7):
            rng.shuffle(labels)
            e=exact_original_BA_energy(t,labels)
            self.assertGreaterEqual(e,0)
            self.assertLessEqual(e,t["total_original_BA_true_right_A_internal_Q_T_g"])
            self.assertEqual(len(set(tuple(x) for x in labels)),15)

    def test_006_fail_closed_source_identity_and_nonbijective_labels(self):
        m=fixture(1,"S68")
        t=true_original_W32_fixed_g_weighted_tensor(m)
        with self.assertRaises(ValueError):
            true_original_W32_fixed_g_weighted_tensor({**m,"s":4})
        with self.assertRaises(ValueError):
            true_original_W32_fixed_g_weighted_tensor(
                {**m,"right_labels":tuple(m["right_labels"])[:-1]})
        with self.assertRaises(ValueError):
            exact_original_BA_energy(t,m["left_labels"][:-1])
        with self.assertRaises(ValueError):
            exact_original_BA_energy(t,
                tuple(m["left_labels"])[:-1]+(m["left_labels"][0],))
        for u,v in ((-1,2),(0,0),(0,15),(1,True)):
            with self.assertRaises(ValueError):
                exact_swap_gradient(t,m["left_labels"],u,v)
        with self.assertRaises(ValueError):
            descend_true_original_W32(t,m["left_labels"],max_steps=0)

    def test_007_real_W32_S72_one_swap_stationarity_not_GLOBAL_minimum(self):
        """A rigorous ACTUAL ORIGINAL seven-GF5 counterexample to swap optimality."""
        r=true_W32_quintic_swap_report("S72",random_starts=2)
        base,_,better=r["search_results"]
        self.assertEqual(base["initial_real_BA_charge"],23)
        self.assertEqual(base["final_real_BA_charge"],23)
        self.assertEqual(base["strictly_decreasing_steps"],0)
        self.assertGreaterEqual(base["certified_final_minimum_exact_swap_delta"],0)
        self.assertEqual(base["full_historical_final_original_positive_seven_Q"],72)
        self.assertEqual(better["final_real_BA_charge"],14)
        self.assertEqual(better["full_historical_final_original_positive_seven_Q"],102)
        self.assertLess(better["final_real_BA_charge"],base["final_real_BA_charge"])
        self.assertEqual(better["independent_62370_original_sixsets_before_after"],"PASS")
        self.assertTrue(better["not_claimed_globally_optimal"])
        self.assertTrue(r["not_a_global_minimum_certificate"])


if __name__=="__main__":
    unittest.main()
