"""Independent all-h actual ORIGINAL GQ two-rook source site/degree cap."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4aj_original_source_site_cap import (
    all_h_original_site_cap_certificate,
    _pairwise_source_site_witnesses,
    independently_check_genuine_original_hall_site_cap,
    constructed_SHARP_genuine_W34_original_site_witness,
)
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
    independent_common_neighbors,
)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source, transform_model,
)


def actual_disjoint_rootpair(model,side):
    """Enumerate real source flag IDs; never substitute physical K_a pairs."""
    original=tuple(tuple(z) for z in model["incidences"])
    labels=tuple(model["right_labels" if side==0 else "left_labels"])
    V=len(model["left_labels"])
    for root in range(V):
        fl=tuple(k for k,e in enumerate(original) if e[side]==root)
        for offset,two in enumerate(combinations(fl,2)):
            e0,e1=(labels[original[j][1-side]] for j in two)
            if not(set(e0)&set(e1)):
                return root,offset
    raise AssertionError("genuine global original model has no opposite disjoint rootpair")


class GenuineOriginalHallSiteCapTests(unittest.TestCase):
    def test_01_all_h_exact_fraction_upper_and_strict_rejection(self):
        for h in range(1,44):
            s=1<<h
            c=all_h_original_site_cap_certificate(s)
            self.assertEqual(c["each_channel_site_set_cap_actual_original_degree"],s+1)
            self.assertEqual(c["each_fixed_actual_rootpair_B_C4_accepted_split_GF5_upper"],
                             6*(s+1)**2)
            self.assertLessEqual(
                Fraction(c["simpler_all_h_fraction_ceiling_24d2_over_a2"]),
                Fraction(c["simpler_real_GQ_fraction_ceiling_12d_over_s2plus1"]))
            self.assertTrue(c["each_true_source_channel_site_injection_for_ALL_global_maps"])
            self.assertFalse(c["positive_Hall_mass_for_all_global_maps_NOT_PROVED"] is False)
            if s>=16:
                self.assertTrue(c["uniform_strict_Hall_rejection_fraction_for_s_ge16_PROVED"])
                self.assertLess(
                    6*(s+1)**2,
                    c["each_SAFE_fixed_rootpair_C4_physical_two_triangle_floor"])
                self.assertLess(Fraction(c["simpler_real_GQ_fraction_ceiling_12d_over_s2plus1"]),1)
            else:
                self.assertFalse(c["uniform_strict_Hall_rejection_fraction_for_s_ge16_PROVED"])

    def test_02_explicit_first_order_strict_rejection_fractions(self):
        z16=all_h_original_site_cap_certificate(16)
        self.assertEqual(z16["a"],94)
        self.assertEqual(z16["each_fixed_actual_rootpair_B_C4_accepted_split_GF5_upper"],1734)
        self.assertEqual(z16["each_SAFE_fixed_rootpair_C4_physical_two_triangle_floor"],2209)
        self.assertEqual(z16["each_SAFE_C4_true_original_Hall_rejected_physical_lower"],475)
        for s in (16,32,64,128,256,512):
            c=all_h_original_site_cap_certificate(s)
            R=Fraction(c["MAX_true_original_Hall_positive_fraction_of_SAFE_2triangles"])
            self.assertLess(R,1)
            self.assertGreaterEqual(1-R,1-Fraction(12*(s+1),s*s+1))

    def test_03_genuine_original_W32_global_4_schemes_both_typed_sides(self):
        for scheme in ("S68","S72","lex","reverse"):
            model=fixture(1,scheme)
            for side in (0,1):
                root,offset=actual_disjoint_rootpair(model,side)
                c=independently_check_genuine_original_hall_site_cap(
                    model,side=side,root=root,pair_offset=offset,max_C4=3)
                self.assertTrue(c["disjoint_pinned_original_root_pair_physical"])
                self.assertEqual(c["source_cohorts_tested"],3)
                self.assertEqual(c["actual_all_six_ORIGINAL_GF5_accepted_Q"],
                                 c["expected_preexisting_AH_original_cohort_total"])
                for cohort in c["per_realized_original_B_C4_verification"]:
                    self.assertLessEqual(cohort["accepted_original_Q"],54)
                    for channel in cohort["channel_site_sets"]:
                        self.assertLessEqual(channel["left_site_count"],3)
                        self.assertLessEqual(channel["right_site_count"],3)
                        self.assertEqual(
                            len(set(channel["left_actual_ORIGINAL_source_line_factor_IDs"])),
                            channel["left_site_count"])

    def test_04_TRUE_W34_sharp_site_five_source_flag_realization(self):
        witness=constructed_SHARP_genuine_W34_original_site_witness()
        self.assertEqual(witness["sharp_site_degree"],5)
        self.assertTrue(witness["actual_source_points_noncollinear"])
        model=witness["model"]
        root=witness["root"]
        selected=witness["four_distinct_actual_original_B_source_factors"]
        self.assertEqual(len(set(model["left_labels"])),85)
        self.assertEqual(len(set(model["right_labels"])),85)
        cert=witness["certificate"]
        self.assertTrue(cert["disjoint"])
        pair=next(x for x in cert["channel_site_sets"]
                  if x["real_original_row_pair"]==(0,1))
        self.assertEqual(pair["left_site_count"],5)
        self.assertEqual(len(pair["physical_auxiliary_sites_left"]),5)
        self.assertEqual(
            len(set(pair["left_actual_ORIGINAL_source_line_factor_IDs"])),5)
        original=tuple(model["incidences"])
        for t in pair["left_actual_ORIGINAL_source_line_factor_IDs"]:
            self.assertIn((selected[0],t),original)
        self.assertLessEqual(cert["accepted_original_Q"],150)

    def test_05_TRUE_W34_global_lex_random_two_types_and_exact_AH(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            for side in (0,1):
                root,offset=actual_disjoint_rootpair(model,side)
                c=independently_check_genuine_original_hall_site_cap(
                    model,side=side,root=root,pair_offset=offset,max_C4=3)
                self.assertTrue(c["six_source_channels_degree_capped_all_tested"])
                self.assertEqual(
                    c["actual_all_six_ORIGINAL_GF5_accepted_Q"],
                    c["expected_preexisting_AH_original_cohort_total"])
                for one in c["per_realized_original_B_C4_verification"]:
                    self.assertLessEqual(one["accepted_original_Q"],6*25)

    def test_06_TRUE_W38_global_lex_random_two_typed_maps(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            for side in (0,1):
                root,offset=actual_disjoint_rootpair(model,side)
                c=independently_check_genuine_original_hall_site_cap(
                    model,side=side,root=root,pair_offset=offset,max_C4=2)
                self.assertLessEqual(
                    c["actual_all_six_ORIGINAL_GF5_accepted_Q"],2*6*81)
                self.assertEqual(c["actual_all_six_ORIGINAL_GF5_accepted_Q"],
                                 c["expected_preexisting_AH_original_cohort_total"])
                for v in c["per_realized_original_B_C4_verification"]:
                    for ch in v["channel_site_sets"]:
                        self.assertLessEqual(ch["left_site_count"],9)
                        self.assertLessEqual(ch["right_site_count"],9)

    def test_07_real_source_symplectic_and_independent_physical_coordinate_invariance(self):
        model=fixture(2,"lex")
        root,offset=actual_disjoint_rootpair(model,0)
        transP,transL=symplectic_transvection_source(model,1)
        a=model["a"]
        changed=transform_model(
            model,point_sources=transP,line_sources=transL,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((i+3)%a for i in range(a)))
        original=independently_check_genuine_original_hall_site_cap(
            model,side=0,root=root,pair_offset=offset,max_C4=1)
        # Pinned-flags' original source indexing is permuted; find the
        # mapped pair offset exactly, do not assume unchanged numbering.
        inc=tuple(model["incidences"])
        oldflags=tuple(i for i,e in enumerate(inc) if e[0]==root)
        pinned=tuple(combinations(oldflags,2))[offset]
        mapped=frozenset((transP[inc[i][0]],transL[inc[i][1]]) for i in pinned)
        altered=tuple(changed["incidences"])
        mapped_ids=frozenset(altered.index(x) for x in mapped)
        dest=transP[root]
        flags2=tuple(i for i,e in enumerate(altered) if e[0]==dest)
        newoffset=next(i for i,p in enumerate(combinations(flags2,2))
                       if frozenset(p)==mapped_ids)
        post=independently_check_genuine_original_hall_site_cap(
            changed,side=0,root=dest,pair_offset=newoffset,max_C4=1)
        self.assertEqual(original["disjoint_pinned_original_root_pair_physical"],
                         post["disjoint_pinned_original_root_pair_physical"])
        self.assertEqual(
            original["per_realized_original_B_C4_verification"][0][
                "accepted_original_Q"],
            post["per_realized_original_B_C4_verification"][0][
                "accepted_original_Q"])

    def test_08_negative_fake_original_and_invalid_selected_source_C4(self):
        model=fixture(1,"S68")
        root,offset=actual_disjoint_rootpair(model,0)
        src=occupied_root_C4_source_factors(model,side=0,root=root)
        with self.assertRaises(ValueError):
            _pairwise_source_site_witnesses(
                model,side=0,root=root,pair_offset=offset,
                four_sources=(root,)+src[0][1:])
        with self.assertRaises(ValueError):
            _pairwise_source_site_witnesses(
                model,side=0,root=root,pair_offset=offset,
                four_sources=(src[0][0],)*4)
        with self.assertRaises(ValueError):
            independently_check_genuine_original_hall_site_cap(
                model,side=0,root=root,pair_offset=offset,max_C4=0)
        with self.assertRaises(ValueError):
            independently_check_genuine_original_hall_site_cap(
                dict(model,right_labels=((0,1),)*15),
                side=0,root=root,pair_offset=offset,max_C4=1)
        with self.assertRaises(ValueError):
            independently_check_genuine_original_hall_site_cap(
                dict(model,incidences=model["incidences"][:-1]),
                side=0,root=root,pair_offset=offset,max_C4=1)


if __name__=="__main__":
    unittest.main()
