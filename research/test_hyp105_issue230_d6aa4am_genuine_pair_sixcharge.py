"""AA4-AM true-original full seven-GF5 six-Q to two-original-flag extension."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    all_h_seven_class_anchor_capacity,
    exact_W32_original_seven_pair_extension_certificate,
    independent_W32_pair_anchor_referee,original_D_pair_index,
    six_Q_anchored_D_pairs,_projection_source_type)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,_source_cohort,
    single_original_A_sector_permanent)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    exact_original_global_transport,_actual_strict_original_transport)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independent_true_original_W34_selected_local_BA(model,side,root,off,four):
    """Literal original Hall matching, no AA4-AK channel or pair formulas."""
    a,inc,N,pins_original,inv,pins_phys,four=_source_cohort(
        model,side=side,root=root,pair_offset=off,src_four=four)
    ix={tuple(flag):i for i,flag in enumerate(inc)}
    result=set()
    for H in pinned_twofactor_completions(*pins_phys,a):
        rest=tuple(e for e in H if e not in pins_phys)
        if any(e not in inv for e in rest):continue
        opp=tuple(inv[e] for e in rest)
        for matching in permutations(opp):
            if not all(matching[i] in N[four[i]] for i in range(4)):
                continue
            if side==0:
                flags=[(root,pins_original[0]),(root,pins_original[1])]
                flags.extend((four[i],matching[i]) for i in range(4))
            else:
                flags=[(pins_original[0],root),(pins_original[1],root)]
                flags.extend((matching[i],four[i]) for i in range(4))
            Q=tuple(sorted(ix[q] for q in flags))
            if len(set(Q))!=6:raise AssertionError("faked ORIGINAL six flags")
            if Q in result:raise AssertionError("duplicate true original six Q")
            result.add(Q)
    return result


class GenuineOriginalPairSixcharge(unittest.TestCase):
    def test_01_all_h_source_pattern_capacities_and_unanchored_C(self):
        x=all_h_seven_class_anchor_capacity()
        self.assertEqual(x[
            "accepted_true_original_seven_GF5_tag_max_D_two_flag_anchors"],{
              "D6":6,"B-left/A-right":3,"A-left/B-right":3,
              "C/A":0,"C/B":0,"B/B-overlap":2,"B/B-disjoint":1})
        self.assertEqual(x["true_original_D6_Q_anchors_EXACT"],6)
        self.assertTrue(x["all_complete_global_label_maps_all_h_structural_theorem"])
        self.assertTrue(x["seven_class_S_omega_s6_NOT_PROVED"])

    def test_02_W32_exact_5_maps_full_seven_selected_source_extension(self):
        maps=[("dual_zero",zero_split_original_W32())]+[
            (scheme,fixture(1,scheme))
            for scheme in ("lex","reverse","S68","S72")]
        # Independently frozen exact ORIGINAL source Q -> true D-pair
        # extension witness values from first 4/4-success hosted run.
        # Columns: D, S, E, U, covered D, uncovered D.
        totals={"dual_zero":(277,123,164,17,115,162),
                "lex":(307,259,517,23,212,95),
                "reverse":(300,169,246,23,166,134),
                "S68":(257,68,79,10,64,193),
                "S72":(261,72,75,16,59,202)}
        for scheme,m in maps:
            z=exact_W32_original_seven_pair_extension_certificate(
                m,independent_oracle=scheme in ("dual_zero","S68"))
            D,S,E,U,C,uncovered=totals[scheme]
            self.assertEqual(z["D_unordered_actual_original_bilateral_two_flag_pairs"],D)
            self.assertEqual(z["S_selected_original_seven_GF5_sixsets"],S)
            self.assertEqual(z["E_original_extension_incidences"],E)
            self.assertEqual(z["U_selected_sixsets_with_ZERO_original_D_pair_anchors"],U)
            self.assertEqual(z["D_covered_by_at_least_one_selected_original_six_Q"],C)
            self.assertEqual(z["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],uncovered)
            self.assertGreater(uncovered,0)
            self.assertGreater(U,0)
            self.assertEqual(z["seven_original_S_by_tag"],
                seven_census(m,independent_checks=False)["seven_class_motif_counts"])
            self.assertEqual(z["D_covered_by_at_least_one_selected_original_six_Q"]+
                z["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],D)
            self.assertEqual(
                z["E_original_extension_incidences"],
                sum(i*n for i,n in z["selected_six_Q_anchored_D_pair_histogram"].items()))
            self.assertEqual(
                z["E_original_extension_incidences"],
                sum(z["seven_original_D_extension_E_by_tag"].values()))
            self.assertEqual(
                z["S_selected_original_seven_GF5_sixsets"],
                z["U_selected_sixsets_with_ZERO_original_D_pair_anchors"]+
                z["S_with_positive_D_anchor"])
            self.assertLessEqual(
                z["exact_energy_anchor_sandwich_lower"],
                z["S_selected_original_seven_GF5_sixsets"])
            self.assertLessEqual(
                z["S_selected_original_seven_GF5_sixsets"],
                z["exact_energy_anchor_sandwich_upper"])
            self.assertLessEqual(z["E_original_extension_incidences"],
                                 z["all_h_tag_weighted_original_extension_E_upper"])
            self.assertEqual(z["all_h_tag_weighted_original_extension_E_upper"],
                  sum(all_h_seven_class_anchor_capacity()[
                      "accepted_true_original_seven_GF5_tag_max_D_two_flag_anchors"][tag]*n
                      for tag,n in z["seven_original_S_by_tag"].items()))
            self.assertEqual(z["seven_original_D_extension_E_by_tag"]["C/A"],0)
            self.assertEqual(z["seven_original_D_extension_E_by_tag"]["C/B"],0)
            self.assertEqual(
                z["seven_original_D_extension_E_by_tag"]["D6"],
                6*z["seven_original_S_by_tag"]["D6"])
            self.assertLessEqual(
                z["D_covered_by_at_least_one_selected_original_six_Q"],
                z["E_original_extension_incidences"])
            print("AA4AM_W32",scheme,"D",D,"S",z["S_selected_original_seven_GF5_sixsets"],
                  "E",z["E_original_extension_incidences"],
                  "U",z["U_selected_sixsets_with_ZERO_original_D_pair_anchors"],
                  "covered_D",z["D_covered_by_at_least_one_selected_original_six_Q"],
                  "uncovered_D",z["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],
                  "tagsE",z["seven_original_D_extension_E_by_tag"],
                  "tagsU",z["seven_original_zero_D_anchor_U_by_tag"],
                  "weightedEcap",z["all_h_tag_weighted_original_extension_E_upper"],
                  "kHist",z["selected_six_Q_anchored_D_pair_histogram"])

    def test_03_direct_TRUE_original_D_first_independent_seven_sixQ_referee(self):
        for scheme,m in (("dual_zero",zero_split_original_W32()),
                         ("lex",fixture(1,"lex")),("S72",fixture(1,"S72"))):
            selected=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
            z=exact_W32_original_seven_pair_extension_certificate(m)
            independent=independent_W32_pair_anchor_referee(m,selected)
            self.assertEqual(z["E_original_extension_incidences"],
                             independent["E_from_D_major_oracle"])
            self.assertEqual(z["D_covered_by_at_least_one_selected_original_six_Q"],
                             independent["covered_from_D_major_oracle"])
            self.assertEqual(z["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],
                             independent["uncovered_from_D_major_oracle"])
            self.assertEqual(z["positive_extension_degree_histogram"],
                             independent["degree_histogram_from_D_major_oracle"])

    def test_04_same_complete_original_W32_symplectic_and_typed_physical_relabels(self):
        m=zero_split_original_W32()
        original=exact_W32_original_seven_pair_extension_certificate(m)
        p,l=symplectic_transvection_source(m,1)
        updated=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        other=exact_W32_original_seven_pair_extension_certificate(updated)
        for key in ("D_unordered_actual_original_bilateral_two_flag_pairs",
                    "S_selected_original_seven_GF5_sixsets",
                    "E_original_extension_incidences",
                    "U_selected_sixsets_with_ZERO_original_D_pair_anchors",
                    "D_covered_by_at_least_one_selected_original_six_Q",
                    "D_UNCOVERED_by_ALL_SEVEN_selected_six_Q",
                    "selected_six_Q_anchored_D_pair_histogram",
                    "seven_original_D_extension_E_by_tag"):
            self.assertEqual(original[key],other[key])

    def test_05_actual_original_W34_partial_global_hole_local_BA_A_B_Q(self):
        # No full W34 seven-GF5 census claim. Only a selection of ACTUAL
        # source B/A anchored original 6-Q under one global physical
        # f,g, each obtained by independent literal true source rook.
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            _,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(m)
            self.assertEqual((V,d,a),(85,5,14))
            D=original_D_pair_index(m)
            count=0
            for side in (0,1):
                for root,off in ((0,0),(1,1),(5,2)):
                    for four in occupied_root_C4_source_factors(
                            m,side=side,root=root)[:2]:
                        Qs=independent_true_original_W34_selected_local_BA(
                            m,side,root,off,four)
                        old=single_original_A_sector_permanent(
                            m,side=side,root=root,pair_offset=off,four=four)
                        self.assertEqual(len(Qs),sum(old["accepted"].values()))
                        for Q in Qs:
                            self.assertEqual(_projection_source_type(Q,inc,side),"B")
                            self.assertEqual(_projection_source_type(Q,inc,1-side),"A")
                            k=six_Q_anchored_D_pairs(Q,inc,left,right)
                            self.assertTrue(k.issubset(D))
                            self.assertLessEqual(len(k),3)
                        count+=len(Qs)
            print("AA4AM_W34_LOCAL",scheme,"selected_original_BA_AB_Q",count,
                  "D_all_original_two_flag_pairs",len(D))
            self.assertGreater(count,0)

    def test_06_original_six_Q_rejects_fabrications_and_wrong_scope(self):
        m=zero_split_original_W32()
        r=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
        Q=next(iter(r))
        inc=tuple(m["incidences"])
        left,right=m["left_labels"],m["right_labels"]
        for wrong in ((0,)*6,(-1,)+Q[1:],tuple(range(5)),tuple(range(6,8))):
            with self.assertRaises(ValueError):
                six_Q_anchored_D_pairs(wrong,inc,left,right)
        for invalid in (dict(m,left_labels=((0,1),)*15),
                        dict(m,right_labels=((0,1),)*15),
                        dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                exact_W32_original_seven_pair_extension_certificate(invalid)
        with self.assertRaises(ValueError):
            exact_W32_original_seven_pair_extension_certificate(fixture(2,"lex"))

    def test_07_positivity_of_D_does_not_force_split_triangle_sixsets(self):
        m=zero_split_original_W32()
        z=exact_W32_original_seven_pair_extension_certificate(m)
        self.assertEqual(z["D_unordered_actual_original_bilateral_two_flag_pairs"],277)
        from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
            full_original_W32_sector_certificate)
        for side in (0,1):
            v=full_original_W32_sector_certificate(m,side=side)
            self.assertEqual(v["original_GF5_A_accepted_by_sector"][
                "split_two_triangles"],0)
        self.assertEqual(z["S_selected_original_seven_GF5_sixsets"],123)
        self.assertTrue(z["model_equivalent_charge_frontier_not_Branch_A_B"])


if __name__=="__main__":
    unittest.main()
