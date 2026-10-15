"""AA4-U: independently falsifiable TRUE ORIGINAL nine-forest joint lower."""
import random
import unittest
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    A,B,C,SOURCE_SHAPES, original_sixset_source_cell,
    independent_true_source_component_lengths,
    all_h_original_gq_six_forest_theorem,
    exact_W32_source_six_forest_universe, exact_W32_forest_stratified_frechet
)


class OriginalSixForestTransportationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=fixture(1,"lex")
        cls.inc=tuple(tuple(x) for x in cls.m["incidences"])
        cls.source=exact_W32_source_six_forest_universe(cls.m)

    def test_001_all_h_true_original_six_edge_forest_and_no_C_C(self):
        for h in range(1,15):
            s=1<<h
            z=all_h_original_gq_six_forest_theorem(s)
            self.assertEqual(z["actual_original_incidence_ids"],
                             (s+1)**2*(s*s+1))
            self.assertTrue(z["source_C_C_impossible"])
            self.assertTrue(z["any_six_distinct_gq_incidence_ids_induce_acyclic_source_forest"])
            self.assertEqual(len(z["nine_actual_source_forest_cells"]),9)
            self.assertFalse(z["full_seven_GF5_minimum_PROVED"])

    def test_002_independent_true_W32_universe_full_45_choose_6(self):
        z=self.source
        self.assertEqual(z["total_original_45_choose_6"],comb(45,6))
        self.assertEqual(len(z["original_source_forest_universe"]),9)
        self.assertEqual(set(z["original_source_forest_universe"]),set(SOURCE_SHAPES))
        expected={"A":comb(15,6)*3**6,
                  "B":15*comb(14,4)*comb(3,2)*3**4,
                  "C":comb(15,3)*comb(3,2)**3}
        self.assertEqual(z["left_source_A_B_C_universe"],expected)
        self.assertEqual(z["right_source_A_B_C_universe"],expected)
        self.assertTrue(all(x>0 for x in z["original_source_forest_universe"].values()))
        self.assertLess(sum(z["original_source_forest_universe"].values()),
                        z["total_original_45_choose_6"])
        self.assertTrue(z["independent_of_physical_f_g"])

    def test_003_independent_source_path_component_oracle(self):
        rng=random.Random(23000419)
        indexes=tuple(range(45))
        # Source-only paths, independent of f and g, checked against a
        # separate actual-incidence six-edge connectivity enumerator.
        sizes=Counter()
        checked=0
        for _ in range(3500):
            Q=tuple(sorted(rng.sample(indexes,6)))
            cell=original_sixset_source_cell(Q,self.inc)
            if cell is None:
                continue
            actual=independent_true_source_component_lengths(Q,self.inc)
            self.assertEqual(actual,SOURCE_SHAPES[cell])
            sizes[cell]+=1
            checked+=1
        self.assertGreater(checked,2000)
        self.assertGreaterEqual(len(sizes),7)

    def test_004_all_four_true_W32_global_map_seven_GF5_reconstruction(self):
        known={"S68":68,"S72":72,"lex":259,"reverse":169}
        for scheme,s in known.items():
            m=fixture(1,scheme)
            z=exact_W32_forest_stratified_frechet(
                m,source_universe=self.source,component_crosscheck=True)
            self.assertEqual(z["actual_full_seven_GF5_S"],s)
            self.assertEqual(z["source_population_from_all_45_choose_6"],comb(45,6))
            self.assertEqual(len(z["forest_cells"]),9)
            self.assertGreater(z["source_path_component_crosschecks"],100)
            self.assertEqual(
                sum(c["actual_global_two_side_join"] for c in z["forest_cells"].values()),
                z["actual_accepted_non_A_A_seven"]+
                z["actual_nonaligned_A_A_joint"]+
                z["actual_genuine_D6"])
            self.assertTrue(z["all_h_geometric_forest_partition_PROVED"])
            self.assertFalse(z["forest_conditioned_frechet_proves_all_h_S_omega_s6"])
            self.assertFalse(z["true_GLOBAL_injection_realising_relaxed_empty_intersection_PROVED"])
            history=seven_census(m,independent_checks=False)
            self.assertEqual(z["selected_GF5_51palette_certified_numerator"],
                             history["GF5_seven_lower_numerator"])

    def test_005_two_global_injected_type_maps_random_and_real(self):
        m=fixture(1,"lex")
        edges=tuple(combinations(range(6),2))
        rng=random.Random(23000427)
        for _ in range(3):
            left=list(edges);right=list(edges)
            rng.shuffle(left);rng.shuffle(right)
            x={**m,"left_labels":tuple(left),"right_labels":tuple(right)}
            z=exact_W32_forest_stratified_frechet(
                x,source_universe=self.source,independent_historical=True)
            self.assertEqual(sum(c["point_physical_half_in_source_cell"]
                                 for c in z["forest_cells"].values())+
                             z["point_physical_half_outside_joint_source_grid"],62370)
            self.assertEqual(sum(c["line_physical_half_in_source_cell"]
                                 for c in z["forest_cells"].values())+
                             z["line_physical_half_outside_joint_source_grid"],62370)
            self.assertEqual(z["source_population_from_all_45_choose_6"],comb(45,6))
            for c in z["forest_cells"].values():
                self.assertLessEqual(c["sharp_abstract_subset_Frechet_lower"],
                                     c["actual_global_two_side_join"])

    def test_006_negative_fake_original_source_C6_fails_before_census(self):
        actual=fixture(1,"lex")
        fake={**actual,"incidences":tuple((p,l)
                 for l in range(15)
                 for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            exact_W32_source_six_forest_universe(fake)
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            exact_W32_forest_stratified_frechet(fake,source_universe=self.source)

    def test_007_strict_injection_and_non_source_sixset_rejection(self):
        inc=self.inc
        with self.assertRaises(ValueError):
            original_sixset_source_cell((0,0,1,2,3,4),inc)
        with self.assertRaises(ValueError):
            original_sixset_source_cell((0,1,2),inc)
        malformed=fixture(1,"lex")
        dup=list(malformed["left_labels"]);dup[0]=dup[1]
        with self.assertRaises(ValueError):
            exact_W32_forest_stratified_frechet(
                {**malformed,"left_labels":tuple(dup)},source_universe=self.source)

    def test_008_no_independent_per_Q_source_universe_calibration(self):
        # The source universe census is independent of the physical
        # mapping: relabel BOTH complete physical types and check that
        # every exact source-forest N remains fixed and all margins
        # obey their common genuine-original reservoir capacity.
        for scheme in ("S68","reverse"):
            z=exact_W32_forest_stratified_frechet(
                fixture(1,scheme),source_universe=self.source)
            for cell,datum in z["forest_cells"].items():
                self.assertEqual(datum["true_original_source_universe"],
                                 self.source["original_source_forest_universe"][cell])
                self.assertLessEqual(
                    datum["point_physical_half_in_source_cell"]+
                    datum["line_physical_half_in_source_cell"]-
                    datum["actual_global_two_side_join"],
                    datum["true_original_source_universe"])


if __name__=="__main__":
    unittest.main()
