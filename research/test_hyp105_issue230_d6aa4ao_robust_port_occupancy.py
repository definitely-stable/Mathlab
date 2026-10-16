"""AA4-AO: global-original physical port robust theorem and falsifiers."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4ao_robust_port_occupancy import (
    physical_P5_robust_certificate,all_h_robust_original_D_port_physical_theorem,
    genuine_original_D_pair_robust_occupation,
    independent_abstract_isolated_port_sharpness)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    _strict_occupied_half_patterns)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index,exact_W32_original_seven_pair_extension_certificate)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    exact_true_original_W32_D_funnel_census)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independent_physical_literal_P5_oracle(ports,a,occupied):
    """Completely distinct physical P5 mechanism via all-H pattern oracle."""
    inv={tuple(edge):i for i,edge in enumerate(occupied)}
    entries,formal,occ=_strict_occupied_half_patterns(ports,a,inv)
    return occ.get("P5",0),occ


class RobustOriginalDPortPhysical(unittest.TestCase):
    def test_01_all_h_exact_integer_missing_palette_thresholds(self):
        for h in (1,2,3,4,5,6,7,8,10,12,14,18,19,25,50):
            s=1<<h
            z=all_h_robust_original_D_port_physical_theorem(s)
            n=z["auxiliary_coordinates"]
            m=z["global_physical_missing_edges_per_type"]
            self.assertLessEqual(m,n+1)
            self.assertEqual(z["each_original_D_pair_typed_occupied_P5_lower"],
                             max(0,(n-m)*(n-1)*(n-2)))
            if m<=n-1:
                self.assertTrue(z[
                    "unconditional_typed_P5_positive_for_every_original_D"])
                self.assertGreater(z[
                    "each_original_D_pair_two_side_occupied_P5_P5_lower"],0)
            if h>=2 and m<=n:
                self.assertTrue(z[
                    "unconditional_some_typed_physical_pattern_for_every_original_D"])
            if h>=3:
                self.assertEqual(z["conditional_typed_good_P5_lower"],
                                 n*(n-1)*(n-2)/2)
                self.assertEqual(z["conditional_two_side_good_P5_P5_lower"],
                                 (n*(n-1)*(n-2)/2)**2)
            self.assertTrue(z["accepted_original_Hall_Q_positive_NOT_PROVED"])
            self.assertTrue(z["number_of_good_D_pairs_lower_NOT_PROVED"])
        for bad in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_robust_original_D_port_physical_theorem(bad)

    def test_02_independent_literal_missing_edge_oracle_K8_K9(self):
        for a in (8,9):
            all_edges=frozenset(combinations(range(a),2))
            center,p,q=0,1,2
            msets=[
                set(), {(3,4)}, {(1,3),(1,4)}, {(2,3),(4,5)},
                {(1,2),(3,4),(3,5),(4,5)},
                {(1,t) for t in range(3,a)},
                {(1,t) for t in range(2,a)},
            ]
            for missing in msets:
                occupied=all_edges-set(missing)
                z=physical_P5_robust_certificate((center,p,q),a,occupied)
                direct,all_types=independent_physical_literal_P5_oracle(
                    (center,p,q),a,occupied)
                self.assertEqual(z["actual_occupied_P5"],direct)
                self.assertGreaterEqual(z["actual_occupied_P5"],
                                        z["exact_union_bound_P5"])
                self.assertGreaterEqual(z["exact_union_bound_P5"],
                                        z["universal_m_only_bound_P5"])
                self.assertLessEqual(z["actual_occupied_P5"],z["formal_P5"])
                if not missing:
                    self.assertEqual(direct,(a-3)*(a-4)*(a-5))

    def test_03_every_genuine_original_W32_D_pair_all_five_maps_exact(self):
        for name,m in [("dual_zero",zero_split_original_W32())]+[
            (s,fixture(1,s)) for s in ("lex","reverse","S68","S72")]:
            D=original_D_pair_index(m)
            n=0
            for pair in sorted(D):
                z=genuine_original_D_pair_robust_occupation(m,pair)
                self.assertEqual(z["original_point_physical"]["actual_occupied_P5"],6)
                self.assertEqual(z["original_line_physical"]["actual_occupied_P5"],6)
                self.assertEqual(z["occupied_two_side_P5_P5_physical_template_count"],36)
                self.assertEqual(z["theorem"][
                    "each_original_D_pair_typed_occupied_P5_lower"],6)
                n+=1
            self.assertEqual(n,{
                "dual_zero":277,"lex":307,"reverse":300,"S68":257,"S72":261}[name])
            print("AA4AO_REAL_W32",name,"source_original_D_pairs",n,
                  "occupied_P5_P5_templates_PER_D",36)
            if name=="S68":
                full=exact_true_original_W32_D_funnel_census(m)
                self.assertEqual(full["D_pair_stage_partition"],{
                    "no_original_Hall_six_Q":50,
                    "original_six_Q_only_unaligned_AA":143,
                    "has_seven_positive_original_six_Q":64})
                self.assertEqual(full[
                    "total_occupied_both_side_physical_template_pair_incidence"],25700)

    def test_04_true_original_W34_global_injection_6_holes_both_sides(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            D=sorted(original_D_pair_index(m))
            self.assertGreater(len(D),1000)
            n=0
            for pair in D[:8]+D[-8:]:
                z=genuine_original_D_pair_robust_occupation(m,pair)
                self.assertEqual(z["theorem"]["a"],14)
                self.assertEqual(z["theorem"][
                    "global_physical_missing_edges_per_type"],6)
                self.assertGreaterEqual(z["original_point_physical"][
                    "actual_occupied_P5"],(11-6)*10*9)
                self.assertGreaterEqual(z["original_line_physical"][
                    "actual_occupied_P5"],(11-6)*10*9)
                self.assertGreaterEqual(z[
                    "occupied_two_side_P5_P5_physical_template_count"],450**2)
                n+=1
            self.assertEqual(n,16)
            print("AA4AO_REAL_W34",scheme,"checked_16_real_D_pairs",
                  "per_typed_P5_universal_floor",450)

    def test_05_good_physical_ports_conditional_W38_real_global_labels(self):
        # True source W(3,8) fixture model is costly; instantiate nothing
        # of that size here. The power h3 bound is symbolic, exact, and
        # the physical deletion inequality is independently enumerated
        # for a=35 globally injected images, not fake source incidences.
        s=8
        z=all_h_robust_original_D_port_physical_theorem(s)
        a,n=z["a"],z["auxiliary_coordinates"]
        self.assertEqual((a,n),(35,32))
        self.assertEqual(z["global_physical_missing_edges_per_type"],10)
        occupied=set(combinations(range(a),2))
        # Concentrate missing edges away from the two genuine physical
        # pinned port vertices: all 10 deleted edges are U-U.
        missing=set(combinations(range(3,a),2))
        deleted=set(sorted(missing)[:10])
        occupied-=deleted
        q=physical_P5_robust_certificate((0,1,2),a,occupied)
        self.assertTrue(q["physical_good_ports"])
        self.assertGreaterEqual(q["actual_occupied_P5"],
                                z["conditional_typed_good_P5_lower"])
        self.assertGreater(q["exact_union_bound_P5"],0)

    def test_06_sharp_abstract_port_isolation_and_original_six_Q_nonlift(self):
        for a in (8,14,35):
            z=independent_abstract_isolated_port_sharpness(a)
            self.assertEqual(z["missing_physical_edges"],a-2)
            self.assertEqual(z["occupied_residual_patterns"],0)
            self.assertTrue(z["physical_only_not_a_real_symplectic_GQ"])
        # The genuine original W32 S68 has EVERY physical pattern
        # occupied (100 per source D), yet most of its genuine original
        # two-flag pairs are NOT extended into any selected sevenclass Q.
        m=fixture(1,"S68")
        v=exact_W32_original_seven_pair_extension_certificate(m)
        self.assertEqual(v["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],193)
        for bad in ((0,1,1),(0,1,2,3),(-1,1,2)):
            with self.assertRaises((ValueError,TypeError)):
                physical_P5_robust_certificate(bad,8,
                    set(combinations(range(8),2)))


if __name__=="__main__":
    unittest.main()
