"""HYP-105 C12: independent physical graph orbit/stabilizer falsifiers."""
from fractions import Fraction
from itertools import combinations,permutations
from math import comb,factorial
import unittest

from hyp105_g5e2b3e1c5_common_bijection import (
    physical_occupied_target,fixed_map_overlap,
)
from hyp105_g5e2b3e1c12_physical_orbits import (
    physical_coordinate_actions, physical_prefix_orbits,
    conditional_shared_prefix_mean, full_physical_alphabet_one_pin_blindness,
    original_to_physical_action,genuine_W32_orbit_report,
    orbit_quotiented_shared_minimum_interval,
)


class PhysicalOrbitC12Tests(unittest.TestCase):
    def test_full_K6_physical_group_orbits_and_stabilizers(self):
        F=tuple(combinations(range(6),2))
        group=physical_coordinate_actions(6,F)
        self.assertEqual(group["physical_coordinate_automorphism_count"],720)
        self.assertEqual(group["induced_action_group_order"],720)
        self.assertEqual(group["coordinate_to_occupied_action_kernel_size"],1)
        for k,counts,orbit_count in (
                (0,1,1),(1,15,1),(2,210,2),(3,2730,9)):
            result=physical_prefix_orbits(6,F,tuple(range(k)))
            self.assertEqual(result["all_injective_prefixes"],counts)
            self.assertEqual(result["representative_prefixes"],orbit_count)
            self.assertEqual(sum(p["orbit_size"] for p in result["orbits"]),counts)
            for row in result["orbits"]:
                self.assertEqual(row["orbit_size"]*row["stabilizer_size"],720)
        self.assertEqual(factorial(15)//720,1816214400)

    def test_missing_K6_edges_automorphisms_and_occupied_target(self):
        full=tuple(combinations(range(6),2))
        for missing,expected_group,expected_t in (
          ({(0,1),(0,2)},12,21),
          ({(0,1),(2,3)},16,28),
        ):
            F=tuple(e for e in full if e not in missing)
            group=physical_coordinate_actions(6,F)
            self.assertEqual(group["physical_coordinate_automorphism_count"],
                             expected_group)
            self.assertEqual(group["induced_action_group_order"],expected_group)
            T=physical_occupied_target(6,F)
            self.assertEqual(len(T),expected_t)
            for action in group["distinct_occupied_edge_actions"]:
                self.assertEqual({frozenset(action[i] for i in R) for R in T},
                                 set(T))
            pins=physical_prefix_orbits(6,F,(0,1))
            self.assertEqual(sum(x["orbit_size"] for x in pins["orbits"]),
                             len(F)*(len(F)-1))
            self.assertGreater(pins["representative_prefixes"],1)

    def test_independent_physical_S6_all_720_full_map_BA_preserved(self):
        F=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,F)
        source={R:(i%5+1) for i,R in
                enumerate(map(frozenset,combinations(range(15),6)))
                if i%7==0}
        base=tuple(range(15))
        before=fixed_map_overlap(source,target,base)
        group=physical_coordinate_actions(6,F)
        for action in group["distinct_occupied_edge_actions"]:
            pi=original_to_physical_action(base,action)
            self.assertEqual(fixed_map_overlap(source,target,pi),before)

    def test_k2_conditional_mean_invariant_under_all_coordinate_actions(self):
        V=15
        F=tuple(combinations(range(6),2))
        tgt=physical_occupied_target(6,F)
        source={R:(i%4+1) for i,R in
                enumerate(map(frozenset,combinations(range(V),6)))
                if i%7==0}
        acts=physical_coordinate_actions(6,F)["distinct_occupied_edge_actions"]
        D=(0,1)
        fixed=conditional_shared_prefix_mean(source,tgt,V,{0:0,1:1})
        for a in acts:
            self.assertEqual(
                conditional_shared_prefix_mean(source,tgt,V,
                                               {0:a[0],1:a[1]}),fixed)

    def test_complete_physical_one_pin_blindness_independent_source(self):
        F=tuple(combinations(range(6),2))
        src={frozenset((0,1,2,3,4,5)):9,
             frozenset((0,6,7,8,9,10)):3}
        b=full_physical_alphabet_one_pin_blindness(src,6)
        T=physical_occupied_target(6,F)
        self.assertEqual(b["target_count"],70)
        self.assertEqual(b["target_edge_degree"],28)
        self.assertEqual(b["unconditional_one_map_mean"],Fraction(12*70,5005))
        for original in (0,1,7,14):
            for physical in range(15):
                self.assertEqual(conditional_shared_prefix_mean(
                    src,T,15,{original:physical}),b["unconditional_one_map_mean"])

    def test_full_K6_global_two_pin_orbit_certificate_exact_zero_toy(self):
        # A single weighted original sixset can always avoid the sparse
        # physical T(K6) target, by one genuine full map (not 15! search).
        F=tuple(combinations(range(6),2))
        source={frozenset(range(6)):1}
        result=orbit_quotiented_shared_minimum_interval(
            source,6,F,(0,1),max_prefixes=210)
        self.assertEqual(result["physical_prefix_orbits"],2)
        self.assertEqual(result["physical_prefix_assignments_exhausted"],210)
        self.assertEqual(result["certified_global_BA_minimum_lower"],0)
        self.assertEqual(result["existential_global_BA_minimum_upper"],0)
        self.assertEqual(result["exact_global_BA_minimum_if_equal"],0)
        self.assertEqual(result["unconditional_mean_recovered_by_exact_orbit_tower"],
                         Fraction(70,5005))
        self.assertTrue(result["all_right_completions_same_global_map"])

    def test_genuine_W32_source_same_map_seven_class_equivariance(self):
        r=genuine_W32_orbit_report()
        self.assertEqual(r["prefix_orbit_counts_k0_to_k3"],(1,1,2,9))
        self.assertEqual(r["prefix_assignment_counts_k0_to_k3"],(1,15,210,2730))
        self.assertTrue(r["physical_S6_equivariant_seven_class_count"])
        self.assertEqual(r["real_W32_24_joint_map_min"],56)
        self.assertEqual(r["real_W32_original_S_seven"],169)
        self.assertEqual(r["real_W32_BA_minimizer_S_seven"],141)
        self.assertEqual(r["real_W32_S_seven_change"],-28)
        self.assertEqual(r["real_W32_GF5_floor_numerator_before"],7627209)
        self.assertEqual(r["real_W32_GF5_floor_numerator_after"],6400556)
        self.assertEqual(r["real_W32_class_changes"]["B-left/A-right"],-21)
        self.assertEqual(r["same_11_pin_prefix_conditional_variance"],
                         r["transformed_11_pin_prefix_conditional_variance"])
        self.assertEqual(r["full_map_orbits_exact_quotient"],1816214400)
        self.assertGreaterEqual(r["W32_all_right_g_two_pin_orbit_global_lower"],0)
        self.assertLessEqual(r["W32_all_right_g_two_pin_orbit_global_lower"],56)
        self.assertLessEqual(r["W32_all_right_g_two_pin_orbit_existential_upper"],69)
        self.assertGreaterEqual(r["W32_all_right_g_two_pin_orbit_existential_upper"],
                                r["W32_all_right_g_two_pin_orbit_global_lower"])
        self.assertEqual(r["W32_two_pin_orbit_conditional_mean_tower"],"10000/143")
        self.assertFalse(r["all_15_factorial_orbits_enumerated"])

    def test_fail_closed_partial_group_and_budget(self):
        F=tuple(combinations(range(6),2))
        for invalid in ([(0,1)]*15, [(0,0)]*15, [(1,0)]*15):
            with self.assertRaises(ValueError):
                physical_coordinate_actions(6,invalid)
        with self.assertRaises(ValueError):
            physical_prefix_orbits(6,F,(0,1,2),max_prefixes=210)
        with self.assertRaises(ValueError):
            physical_coordinate_actions(9,
                 tuple(combinations(range(9),2)),max_coordinate_permutations=40000)
        with self.assertRaises(ValueError):
            physical_prefix_orbits(6,F,(0,0))
        R=frozenset(range(6))
        with self.assertRaises(ValueError):
            conditional_shared_prefix_mean({R:1},{R},15,{0:0,1:0})
        with self.assertRaises(ValueError):
            conditional_shared_prefix_mean({R:-1},{R},15,{0:0})


if __name__=="__main__":
    unittest.main()
