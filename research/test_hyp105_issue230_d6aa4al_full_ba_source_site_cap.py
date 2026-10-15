"""AA4-AL: stricter ALL genuine original four-A-sector GF5 Hall/source cap."""
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,full_original_W32_sector_certificate,
    single_original_A_sector_permanent)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors)
from hyp105_issue230_d6aa4al_full_ba_source_site_cap import (
    original_cross_spoke_site_injection_witnesses,
    exact_original_adjacent_same_triangle,
    sharp_all_h_original_full_BA_upper,
    sharp_true_original_complete_BA_cohort)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def real_physical_pin_pair(model,side,adjacent):
    source=tuple(model["incidences"])
    labels=tuple(model["right_labels" if side==0 else "left_labels"])
    for root in range(len(model["left_labels"])):
        neighbors=sorted(x[1-side] for x in source if x[side]==root)
        for pair_offset,(i,j) in enumerate(combinations(neighbors,2)):
            if bool(set(labels[i])&set(labels[j]))==adjacent:
                return root,pair_offset
    raise AssertionError("real GQ global f,g must support this observed physical case")


class OriginalAllFourASectorsTighterSiteDegree(unittest.TestCase):
    def test_01_all_h_new_strictly_improved_source_degree_cap_exact(self):
        for h in range(1,44):
            s=1<<h
            r=sharp_all_h_original_full_BA_upper(s)
            d=s+1
            self.assertEqual(r["disjoint_all_true_original_A_sectors_cap_NEW"],
                             18*d*d+192*d)
            self.assertEqual(r["adjacent_all_true_original_A_sectors_cap_NEW"],
                             48*d*d)
            self.assertEqual(r["all_fixed_actual_original_B_C4_cohort_cap_NEW"],
                             max(18*d*d+192*d,48*d*d))
            self.assertLess(r["all_fixed_actual_original_B_C4_cohort_cap_NEW"],
                            r["OLD_parallel_AK_full_cohort_cap"])
            self.assertTrue(r["for_every_full_global_f_g_true_original_W3s_PROVED"])
            self.assertTrue(r["NO_positive_all_maps_GF5_lower"])
            if s>=8:
                self.assertEqual(
                    r["all_fixed_actual_original_B_C4_cohort_cap_NEW"],48*d*d)
            else:
                self.assertGreater(18*d*d+192*d,48*d*d)

    def test_02_independent_true_W32_all_5_global_pair_maps_all_135_cohorts(self):
        schemes=[("zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        for name,m in schemes:
            for side in (0,1):
                total=0
                classes={"adjacent":0,"disjoint":0}
                for root in range(15):
                    physical_C4=occupied_root_C4_source_factors(
                        m,side=side,root=root)
                    self.assertEqual(len(physical_C4),3)
                    for pair_offset in range(3):
                        for four in physical_C4:
                            z=sharp_true_original_complete_BA_cohort(
                                m,side=side,root=root,pair_offset=pair_offset,
                                four=four,independent_brute=True)
                            self.assertLessEqual(
                                z["exact_accepted_true_original_six_ID_GF5"],
                                z["new_true_original_upper_for_this_sector"])
                            total+=z["exact_accepted_true_original_six_ID_GF5"]
                            classes["adjacent" if z["pinned_physical_adjacent"]
                                    else "disjoint"]+=1
                prior=full_original_W32_sector_certificate(m,side=side)
                self.assertEqual(total,prior["full_original_BA_or_AB_accepted"])
                self.assertEqual(classes["adjacent"]+classes["disjoint"],135)
                if name=="zero":
                    self.assertEqual(total,(46,61)[side])

    def test_03_true_W34_partial_K14_and_separate_source_witnesses(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            for side in (0,1):
                for adjacent in (False,True):
                    root,offset=real_physical_pin_pair(m,side,adjacent)
                    for four in occupied_root_C4_source_factors(
                            m,side=side,root=root)[:3]:
                        z=sharp_true_original_complete_BA_cohort(
                            m,side=side,root=root,pair_offset=offset,
                            four=four,independent_brute=True)
                        self.assertEqual(z["pinned_physical_adjacent"],adjacent)
                        if not adjacent:
                            for w in z["crossed_spoke_real_neighbor_site_injections"]:
                                self.assertLessEqual(
                                    w["accepted_genuine_original_six_Q"],6*25)
                                self.assertTrue(all(y<=5 for y in w["source_site_set_Y"]))
                                self.assertTrue(all(y<=5 for y in w["source_site_set_Z"]))

    def test_04_real_W38_globally_injected_not_onto_K35(self):
        for scheme in ("lex","random"):
            m=fixture(3,scheme)
            self.assertEqual(len(m["left_labels"]),585)
            self.assertEqual(len(m["right_labels"]),585)
            for side in (0,1):
                for adjacent in (False,True):
                    root,offset=real_physical_pin_pair(m,side,adjacent)
                    four=occupied_root_C4_source_factors(
                        m,side=side,root=root)[0]
                    z=sharp_true_original_complete_BA_cohort(
                        m,side=side,root=root,pair_offset=offset,
                        four=four,independent_brute=True)
                    self.assertLessEqual(z["exact_accepted_true_original_six_ID_GF5"],
                                         z["new_uniform_all_A_source_upper"])

    def test_05_same_triangle_all_source_channels_vs_true_permanent(self):
        for scheme,m in (("zero",zero_split_original_W32()),
                         ("lex",fixture(1,"lex")),
                         ("random",fixture(2,"random"))):
            for side in (0,1):
                root,offset=real_physical_pin_pair(m,side,True)
                for four in occupied_root_C4_source_factors(
                        m,side=side,root=root)[:4]:
                    ans=exact_original_adjacent_same_triangle(
                        m,side=side,root=root,pair_offset=offset,four=four)
                    prior=single_original_A_sector_permanent(
                        m,side=side,root=root,pair_offset=offset,four=four)
                    self.assertEqual(ans["accepted_original_same_two_triangles"],
                                     prior["accepted"]["same_triangle_pins"])
                    self.assertLessEqual(ans["accepted_original_same_two_triangles"],
                                         24*(m["s"]+1)**2)

    def test_06_genuine_source_automorphism_and_global_physical_relabels(self):
        m=zero_split_original_W32()
        pt,ln=symplectic_transvection_source(m,1)
        a=m["a"]
        changed=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((i+2)%a for i in range(a)))
        for side in (0,1):
            root,offset=real_physical_pin_pair(m,side,False)
            source=tuple(m["incidences"])
            nbs=sorted(e[1-side] for e in source if e[side]==root)
            pinned=tuple(combinations(nbs,2))[offset]
            trans=pt if side==0 else ln
            other=ln if side==0 else pt
            newroot=trans[root]
            movedpin=tuple(sorted(other[x] for x in pinned))
            updated=tuple(changed["incidences"])
            movednbs=sorted(e[1-side] for e in updated if e[side]==newroot)
            newoffset=tuple(combinations(movednbs,2)).index(movedpin)
            four=occupied_root_C4_source_factors(m,side=side,root=root)[0]
            post=tuple(trans[q] for q in four)
            old=sharp_true_original_complete_BA_cohort(
                m,side=side,root=root,pair_offset=offset,four=four,
                independent_brute=True)
            new=sharp_true_original_complete_BA_cohort(
                changed,side=side,root=newroot,pair_offset=newoffset,
                four=post,independent_brute=True)
            self.assertEqual(old["exact_accepted_true_original_six_ID_GF5"],
                             new["exact_accepted_true_original_six_ID_GF5"])

    def test_07_invalid_global_original_injection_source_and_power_rejected(self):
        m=fixture(1,"lex")
        root,offset=real_physical_pin_pair(m,0,False)
        four=occupied_root_C4_source_factors(m,side=0,root=root)[0]
        with self.assertRaises(ValueError):
            sharp_all_h_original_full_BA_upper(12)
        with self.assertRaises(ValueError):
            sharp_true_original_complete_BA_cohort(
                m,side=0,root=root,pair_offset=offset,four=None)
        with self.assertRaises(ValueError):
            sharp_true_original_complete_BA_cohort(
                m,side=0,root=root,pair_offset=offset,four=(root,)*4)
        with self.assertRaises(ValueError):
            sharp_true_original_complete_BA_cohort(
                dict(m,right_labels=((0,1),)*15),
                side=0,root=root,pair_offset=offset,four=four)
        with self.assertRaises(ValueError):
            sharp_true_original_complete_BA_cohort(
                dict(m,incidences=tuple(m["incidences"])[:-1]),
                side=0,root=root,pair_offset=offset,four=four)

if __name__=="__main__":
    unittest.main()
