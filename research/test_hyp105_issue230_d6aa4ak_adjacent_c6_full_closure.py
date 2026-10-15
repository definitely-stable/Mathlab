"""AA4-AK independent original-symplectic and physical finite falsifiers."""
import unittest
from itertools import combinations
from collections import Counter
from math import comb

from hyp105_issue230_d6aa4ak_adjacent_c6_full_closure import (
    adjacent_pin_endpoints, adjacent_path_physical_count,
    adjacent_complete_capacity, exact_original_adjacent_C6_transfer,
    independent_adjacent_C6_original_oracle, original_connected_full_join,
    original_internal_link_prehall_floor,
)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32, classify_physical_A_twofactor,
    single_original_A_sector_permanent, full_original_W32_sector_certificate,
)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors,
)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    pinned_twofactor_completions,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source, transform_model,
)


class AdjacentC6TrueOriginal(unittest.TestCase):
    def test_01_exhaustive_complete_adjacent_K6_K7_K8(self):
        for a in (6, 7, 8):
            physical = set(combinations(range(a),2))
            edges = tuple(sorted(physical))
            for pins in combinations(edges,2):
                if adjacent_pin_endpoints(*pins) is None:
                    continue
                paths = adjacent_path_physical_count(a, pins, physical)
                brute = sum(classify_physical_A_twofactor(H,pins)=="connected_C6"
                            for H in pinned_twofactor_completions(*pins,a))
                self.assertEqual(paths, brute)
                self.assertEqual(paths, adjacent_complete_capacity(a))

    def test_02_independent_holes_on_all_simple_adjacent_patterns(self):
        for a in (6,7,8):
            pins=((0,1),(1,2))
            all_edges=set(combinations(range(a),2))
            for holes in ((),((2,3),),((2,3),(3,4)),
                          ((0,3),(2,4),(3,5))):
                occupancy=all_edges-set(holes)
                literal=adjacent_path_physical_count(a,pins,occupancy)
                brute=sum(
                    classify_physical_A_twofactor(H,pins)=="connected_C6"
                    and all(e in occupancy for e in H)
                    for H in pinned_twofactor_completions(*pins,a))
                self.assertEqual(literal,brute)

    def test_03_full_true_original_W32_global_zero_split_both_orientations(self):
        model=zero_split_original_W32()
        for side in (0,1):
            source=physical=adjacent_cohorts=0
            for root in range(15):
                Cs=occupied_root_C4_source_factors(model,side=side,root=root)
                self.assertEqual(len(Cs),3)
                for pair_offset in range(3):
                    for four in Cs:
                        full=original_connected_full_join(
                            model,side=side,root=root,pair_offset=pair_offset,
                            four=four,independent=True)
                        source+=full["adjacent_original"]
                        # Reconstruct adjacent physical count independently
                        single=exact_original_adjacent_C6_transfer(
                            model,side=side,root=root,pair_offset=pair_offset,
                            four=four,independent=True)
                        physical+=single["occupied_adjacent_connected_C6_H"]
                        adjacent_cohorts+=int(single["pinned_physical_adjacent"])
            self.assertGreater(adjacent_cohorts,0)
            self.assertEqual(source,(23,17)[side])
            self.assertEqual(physical,(558,432)[side])
            old=full_original_W32_sector_certificate(model,side=side)
            self.assertEqual(old["original_GF5_A_accepted_by_sector"]["connected_C6"],
                             (40,58)[side])
            self.assertEqual(old["occupied_opposite_A_physical_H_by_sector"]["connected_C6"],
                             (1062,1188)[side])

    def test_04_existing_original_W32_lex_S68_S72_completeness(self):
        for scheme in ("lex","S68","S72"):
            model=fixture(1,scheme)
            for side in (0,1):
                combined=0
                adjacent=0
                disjoint=0
                for root in range(15):
                    for off in range(3):
                        for four in occupied_root_C4_source_factors(
                                model,side=side,root=root):
                            z=original_connected_full_join(
                                model,side=side,root=root,pair_offset=off,
                                four=four,independent=True)
                            combined+=z["accepted_original_full_C6_Q"]
                            adjacent+=z["adjacent_original"]
                            disjoint+=z["disjoint_original"]
                complete=full_original_W32_sector_certificate(model,side=side)
                self.assertEqual(combined,complete[
                    "original_GF5_A_accepted_by_sector"]["connected_C6"])
                self.assertEqual(combined,adjacent+disjoint)

    def test_05_genuine_original_W34_with_holes_both_types(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            self.assertEqual(comb(model["a"],2)-len(model["right_labels"]),6)
            for side in (0,1):
                for root,off in ((0,0),(1,1),(3,2)):
                    fours=occupied_root_C4_source_factors(
                        model,side=side,root=root)
                    for four in fours[:2]:
                        actual=original_connected_full_join(
                            model,side=side,root=root,pair_offset=off,
                            four=four,independent=True)
                        self.assertTrue(actual[
                            "all_pin_relations_genuine_original_C6_EXACT"])
                        self.assertTrue(actual[
                            "all_global_maps_Hall_lower_NOT_PROVED"])

    def test_06_true_original_source_symmetry_and_separate_coordinate_perms(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        perm=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        def totals(model,side):
            return tuple(sum(
                exact_original_adjacent_C6_transfer(
                    model,side=side,root=root,pair_offset=off,
                    four=four,independent=False)[key]
                for root in range(15) for off in range(3)
                for four in occupied_root_C4_source_factors(
                    model,side=side,root=root))
                for key in ("accepted_original_adjacent_connected_C6_Q",
                            "occupied_adjacent_connected_C6_H"))
        for side in (0,1):
            self.assertEqual(totals(m,side),totals(perm,side))

    def test_07_integer_global_internal_link_all_powers_and_exceptions(self):
        for h in range(1,43):
            s=1<<h
            z=original_internal_link_prehall_floor(s)
            self.assertEqual(z["original_rootpairs_total"],
                z["V"]*comb(s+1,2))
            self.assertTrue(z["accepted_original_Hall_positive_lower_NOT_PROVED"])
            if h>=4:
                self.assertTrue(z[
                    "original_internal_link_preHall_s14_over384_PROVED"])
                self.assertGreaterEqual(384*z[
                    "all_map_indexed_internal_link_preHall_lower"],s**14)
                self.assertGreater(z[
                    "safe_with_at_least_one_occupied_cross_lower"],0)
            else:
                self.assertFalse(z[
                    "original_internal_link_preHall_s14_over384_PROVED"])
        self.assertEqual([original_internal_link_prehall_floor(s)[
            "safe_with_at_least_one_occupied_cross_lower"] for s in (16,32,64)],
            [187866,4022933,224930885])

    def test_08_domains_no_fake_original_or_Hall_promotion(self):
        for bad in (3,0,-1,16.0,True):
            with self.assertRaises(ValueError):
                original_internal_link_prehall_floor(bad)
        for bad in (0,5,6.0,True):
            with self.assertRaises(ValueError):
                adjacent_complete_capacity(bad)
        self.assertIsNone(adjacent_pin_endpoints((0,1),(2,3)))
        m=zero_split_original_W32()
        good=occupied_root_C4_source_factors(m,side=0,root=0)[0]
        for params in ({"side":2},{"root":15},{"pair_offset":3},
                       {"four":(0,1,2,3)}):
            kwargs={"side":0,"root":0,"pair_offset":0,"four":good}
            kwargs.update(params)
            with self.assertRaises(ValueError):
                exact_original_adjacent_C6_transfer(m,**kwargs)
        with self.assertRaises(ValueError):
            exact_original_adjacent_C6_transfer(
                dict(m,right_labels=((0,1),)*15),
                side=0,root=0,pair_offset=0,four=good)


if __name__=="__main__":
    unittest.main()
