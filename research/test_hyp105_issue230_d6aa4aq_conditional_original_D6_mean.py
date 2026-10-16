"""AA4-AQ: genuine original conditional D6 mean and all-h robust-support lower."""
import unittest
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports)
from hyp105_issue230_d6aa4ap_unique_original_D6_path_kernel import (
    occupied_oriented_original_P5_paths,
    true_original_W32_all_D6_source_path_census)
from hyp105_issue230_d6aa4aq_conditional_original_D6_mean import (
    _falling,minimal_physical_GQ_parameters,six_cycle_image_lower,
    all_h_one_side_permutation_D6_theorem,
    independent_occupied_C6_cycle_census,
    true_original_six_line_SDR_count,
    _original_six_line_SDR_by_distinct_permutation,
    exact_true_original_W32_conditional_D6_mean,
    independent_W32_original_source_sixpoint_first_mean)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def source_sixpoints_from_actual_D_P5(model):
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    for e0 in range(len(inc)):
        p0,l0=inc[e0]
        for e1 in range(e0+1,len(inc)):
            p1,l1=inc[e1]
            if p0==p1 or l0==l1:continue
            if not(set(f[p0])&set(f[p1]) and set(g[l0])&set(g[l1])):
                continue
            ports=true_original_D_physical_ports(inc,f,g,(e0,e1))
            paths=occupied_oriented_original_P5_paths(ports[0],f,a)
            if paths:
                rest=next(iter(paths))
                assert len({p0,p1,*rest})==6
                return tuple((p0,p1)+rest)
    raise AssertionError("genuine source D port has no globally occupied original P5")


class TrueOriginalConditionalD6Mean(unittest.TestCase):
    def test_01_all_h_exact_robust_occupied_C6_and_conditional_lower_2thirds(self):
        for h in range(1,81):
            s=1<<h
            z=all_h_one_side_permutation_D6_theorem(s)
            V,d,a,m=z["V"],z["d"],z["a"],z["m"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertLessEqual(m,a-2)
            self.assertEqual(z["complete_Ka_undirected_C6"],_falling(a,6)//12)
            self.assertEqual(z["each_missing_physical_edge_C6_deletion_max"],
                             _falling(a-2,4))
            self.assertGreaterEqual(z["minimum_globally_occupied_C6_by_union_bound"],0)
            self.assertTrue(z["requires_random_GLOBAL_line_source_factor_assignment"])
            self.assertTrue(z["does_NOT_hold_for_EACH_FIXED_GLOBAL_f_g"])
            self.assertTrue(z["root_issue230_A_B_C_OPEN"])
            self.assertLessEqual(
                z["any_fixed_point_global_f_and_any_fixed_line_occupied_image_expectation_lower"],
                z["any_fixed_global_f_line_support_conditional_mean_upper"])
            self.assertTrue(z[
                "all_GLOBAL_fixed_f_supports_conditional_mean_sandwiched_to_16_over_3_s6_as_h_grows"])
            if s>=4:
                self.assertGreaterEqual(z[
                  "any_fixed_point_global_f_and_any_fixed_line_occupied_image_expectation_lower"
                  ],Fraction(2,3)*s**6)
                self.assertTrue(z[
                    "all_complete_original_two_typed_supports_one_sided_mean_at_least_two_thirds_s6"])
            else:
                self.assertFalse(z[
                    "all_complete_original_two_typed_supports_one_sided_mean_at_least_two_thirds_s6"])
            if s>=8:
                self.assertGreaterEqual(z["relative_to_s6_uniform_lower"],
                                        Fraction(1408,2025))

    def test_02_full_original_W32_5_maps_TWO_independent_source_major_mean_oracles(self):
        for name,m in [("zero",zero_split_original_W32()),
                       ("lex",fixture(1,"lex")),("reverse",fixture(1,"reverse")),
                       ("S68",fixture(1,"S68")),("S72",fixture(1,"S72"))]:
            point_cycle=exact_true_original_W32_conditional_D6_mean(
                m,direct_source_check=True)
            point_subset=independent_W32_original_source_sixpoint_first_mean(m)
            self.assertEqual(point_cycle["point_global_physically_occupied_C6"],
                             point_subset["point_six_source_subset_first_connected_C6"])
            self.assertEqual(point_cycle[
                "original_source_six_points_six_distinct_line_Flag_matchings_given_f"],
                point_subset["source_original_six_distinct_line_flag_matchings"])
            self.assertEqual(point_cycle[
                "exact_conditional_D6_six_original_FLAG_Q_expectation"],
                point_subset["conditional_D6_expectation_original_point_subset_first"])
            self.assertEqual(point_cycle["point_global_physically_occupied_C6"],60)
            self.assertEqual(point_cycle["line_FIXED_global_image_physically_occupied_C6"],60)
            th=all_h_one_side_permutation_D6_theorem(2)
            self.assertLessEqual(
                point_cycle["exact_conditional_D6_six_original_FLAG_Q_expectation"],
                th["any_fixed_global_f_line_support_conditional_mean_upper"])
            self.assertEqual(point_cycle[
                "exact_probability_random_SINGLE_global_line_source_perm_gives_ALIGNED_D6"],
                Fraction(720,_falling(15,6)))
            print("AA4AQ TRUE ORIGINAL W32",name,
                  "source_sixmatchings",point_cycle[
                      "original_source_six_points_six_distinct_line_Flag_matchings_given_f"],
                  "conditional_exact_D6_mean",point_cycle[
                      "exact_conditional_D6_six_original_FLAG_Q_expectation"])

    def test_03_genuine_W32_favorable_randomization_is_not_current_fixed_g_D6(self):
        # Full true-original W32 S68/S72 currently have D6=ZERO
        # even though the average over a new ONE globally fixed
        # permutation of original line factor images is positive.
        for name in ("S68","S72"):
            m=fixture(1,name)
            prior=true_original_W32_all_D6_source_path_census(
                m,independent_physical=False,historical_Q_first=True)
            self.assertEqual(prior["exact_D6_unique_true_original_six_Q"],0)
            positive_mean=exact_true_original_W32_conditional_D6_mean(
                m,direct_source_check=False)
            self.assertGreater(positive_mean[
                "exact_conditional_D6_six_original_FLAG_Q_expectation"],0)

    def test_04_genuine_original_W34_W38_source_neighbor_6SDR_stronger_lower(self):
        for h in (2,3):
            s=2**h
            q=(s+1)**4*((s+1)**2-15)
            for scheme in ("lex","random"):
                m=fixture(h,scheme)
                s0,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
                self.assertEqual(s0,s)
                ps=source_sixpoints_from_actual_D_P5(m)
                brute=true_original_six_line_SDR_count(ps,np)
                self.assertGreaterEqual(brute,q)
                self.assertGreater(brute,0)
                if h==2:
                    independent=_original_six_line_SDR_by_distinct_permutation(ps,np)
                    self.assertEqual(independent,brute)
                self.assertLessEqual(
                    six_cycle_image_lower(s)[
                        "minimum_globally_occupied_C6_by_union_bound"],
                    _falling(a,6)//12)
                print("AA4AQ true original GQ SDR",s,scheme,"six-matchings",brute,
                      "source_GQ_pairwise_collision_floor",q)

    def test_05_independent_K6_physically_occupied_cycles_and_per_fixed_dual_probability(self):
        m=fixture(1,"lex")
        z=independent_occupied_C6_cycle_census(m["right_labels"],6)
        self.assertEqual(len(z),60)
        # Independent abstract graph enumeration for K6, each undirected
        # 6-cycle accounts for exactly 12 physical edge-to-flag cyclic
        # positional isomorphisms fixing all six original source columns.
        cycles=set()
        for perm in permutations(range(6)):
            ed=tuple(sorted(tuple(sorted((perm[i],perm[(i+1)%6])))
                            for i in range(6)))
            cycles.add(ed)
        self.assertEqual(len(cycles),60)
        self.assertEqual(set(cycles),set(z))
        self.assertEqual(len(z)*12,720)
        self.assertEqual(_falling(15,6),3603600)

    def test_06_true_original_symplectic_source_automorphism_and_typed_physical_invariance(self):
        m=zero_split_original_W32()
        old=exact_true_original_W32_conditional_D6_mean(
            m,direct_source_check=False)
        pt,ln=symplectic_transvection_source(m,1)
        a=m["a"]
        changed=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((v+2)%a for v in range(a)))
        new=exact_true_original_W32_conditional_D6_mean(
            changed,direct_source_check=False)
        for fld in (
            "point_global_physically_occupied_C6",
            "line_FIXED_global_image_physically_occupied_C6",
            "original_source_six_points_six_distinct_line_Flag_matchings_given_f",
            "exact_probability_random_SINGLE_global_line_source_perm_gives_ALIGNED_D6",
            "exact_conditional_D6_six_original_FLAG_Q_expectation"):
            self.assertEqual(old[fld],new[fld])

    def test_07_negative_fake_original_source_and_noninjective_global_maps_fail(self):
        m=fixture(1,"lex")
        for bad in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=tuple(m["incidences"])[:-1])):
            with self.assertRaises(ValueError):
                exact_true_original_W32_conditional_D6_mean(bad)
        with self.assertRaises(ValueError):
            all_h_one_side_permutation_D6_theorem(12)
        with self.assertRaises(ValueError):
            independent_occupied_C6_cycle_census(m["left_labels"],7,limit_a=6)
        with self.assertRaises(ValueError):
            true_original_six_line_SDR_count((0,0,1,2,3,4),tuple(() for _ in range(15)))


if __name__=="__main__":unittest.main()
