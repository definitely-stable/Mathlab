"""AA4-AK: exact all-h TRUE original adjacent C6 / triangles / COMPLETE B/A."""
import unittest
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4ak_adjacent_full_a_hall import (
    exact_original_adjacent_A_transfer,full_original_A_Hall_cohort,
    all_h_true_original_full_BA_cohort_upper)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,single_original_A_sector_permanent,
    full_original_W32_sector_certificate,classify_physical_A_twofactor)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    _valid_original_model,transform_model,symplectic_transvection_source)
from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
    exact_original_connected_C6_transfer)


class AdjacentGenuineOriginalFullA(unittest.TestCase):
    def test_01_every_K6_K7_K8_adjacent_pins_topological_exhaustion(self):
        for a in (6,7,8):
            E=tuple(combinations(range(a),2))
            for e0,e1 in combinations(E,2):
                if not (set(e0)&set(e1)):continue
                h=Counter()
                for H in pinned_twofactor_completions(e0,e1,a):
                    tag=classify_physical_A_twofactor(H,(e0,e1))
                    self.assertNotEqual(tag,"split_two_triangles")
                    h[tag]+=1
                self.assertEqual(h["same_triangle_pins"],comb(a-3,3))
                self.assertEqual(h["connected_C6"],6*comb(a-3,3))
                self.assertEqual(sum(h.values()),7*comb(a-3,3))

    def test_02_original_W32_all_five_global_maps_full_135_cohorts_per_side(self):
        maps=[("dual_zero",zero_split_original_W32())]+[
            (scheme,fixture(1,scheme))
            for scheme in ("lex","reverse","S68","S72")]
        expected_total={"dual_zero":(46,61),"lex":(98,110),
                        "reverse":(77,74),"S68":(44,21),"S72":(36,31)}
        for name,m in maps:
            for side in (0,1):
                total=Counter()
                n=0
                for root in range(15):
                    foursets=occupied_root_C4_source_factors(m,side=side,root=root)
                    self.assertEqual(len(foursets),3)
                    for off in range(3):
                        for four in foursets:
                            n+=1
                            z=full_original_A_Hall_cohort(
                                m,side=side,root=root,pair_offset=off,four=four)
                            independently=single_original_A_sector_permanent(
                                m,side=side,root=root,pair_offset=off,four=four)
                            self.assertEqual(
                                z["accepted_full_true_original_BA_or_AB_Q"],
                                sum(independently["accepted"].values()))
                            self.assertEqual(
                                z["accepted_split_two_triangles_original_Q"],
                                independently["accepted"]["split_two_triangles"])
                            self.assertEqual(
                                z["accepted_same_triangle_original_Q"],
                                independently["accepted"]["same_triangle_pins"])
                            self.assertEqual(
                                z["accepted_disjoint_pins_C6_original_Q"]+
                                z["accepted_adjacent_pins_C6_original_Q"],
                                independently["accepted"]["connected_C6"])
                            total["split"]+=z["accepted_split_two_triangles_original_Q"]
                            total["same"]+=z["accepted_same_triangle_original_Q"]
                            total["C6_adj"]+=z["accepted_adjacent_pins_C6_original_Q"]
                            total["C6_dis"]+=z["accepted_disjoint_pins_C6_original_Q"]
                self.assertEqual(n,135)
                prev=full_original_W32_sector_certificate(m,side=side)
                self.assertEqual(total["split"],prev[
                    "original_GF5_A_accepted_by_sector"]["split_two_triangles"])
                self.assertEqual(total["same"],prev[
                    "original_GF5_A_accepted_by_sector"]["same_triangle_pins"])
                self.assertEqual(total["C6_adj"]+total["C6_dis"],prev[
                    "original_GF5_A_accepted_by_sector"]["connected_C6"])
                self.assertEqual(sum(total.values()),expected_total[name][side])
                if name=="dual_zero":
                    self.assertEqual(dict(total),{
                        "split":0,"same":(6,3)[side],
                        "C6_adj":(23,17)[side],
                        "C6_dis":(17,41)[side]})
                print("AA4AK_FULL_TRUE_ORIGINAL_W32",name,side,dict(total))

    def test_03_true_original_W34_actual_global_holes_both_typed_sides(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            self.assertEqual(comb(m["a"],2)-len(m["left_labels"]),6)
            self.assertEqual(comb(m["a"],2)-len(m["right_labels"]),6)
            for side in (0,1):
                for root,off in ((0,0),(1,1),(5,2)):
                    foursets=occupied_root_C4_source_factors(m,side=side,root=root)
                    for four in foursets[:3]:
                        z=full_original_A_Hall_cohort(
                            m,side=side,root=root,pair_offset=off,four=four)
                        old=single_original_A_sector_permanent(
                            m,side=side,root=root,pair_offset=off,four=four)
                        self.assertEqual(
                            z["accepted_full_true_original_BA_or_AB_Q"],
                            sum(old["accepted"].values()))
                        self.assertEqual(
                            z["accepted_same_triangle_original_Q"],
                            old["accepted"]["same_triangle_pins"])
                        self.assertEqual(
                            z["accepted_disjoint_pins_C6_original_Q"]+
                            z["accepted_adjacent_pins_C6_original_Q"],
                            old["accepted"]["connected_C6"])
                        self.assertEqual(
                            z["accepted_split_two_triangles_original_Q"],
                            old["accepted"]["split_two_triangles"])

    def test_04_genuine_W32_original_symplectic_and_independent_physical_relabels(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        other=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        for side in (0,1):
            totals=[]
            for model in (m,other):
                count=Counter()
                for root in range(15):
                    for off in range(3):
                        for four in occupied_root_C4_source_factors(model,side=side,root=root):
                            z=full_original_A_Hall_cohort(
                                model,side=side,root=root,pair_offset=off,four=four)
                            count["split"]+=z["accepted_split_two_triangles_original_Q"]
                            count["same"]+=z["accepted_same_triangle_original_Q"]
                            count["C6_adj"]+=z["accepted_adjacent_pins_C6_original_Q"]
                            count["C6_dis"]+=z["accepted_disjoint_pins_C6_original_Q"]
                totals.append(dict(count))
            self.assertEqual(totals[0],totals[1])
            self.assertEqual(sum(totals[0].values()),(46,61)[side])

    def test_05_all_h_real_gq_source_upper_and_adjacent_zero_domain(self):
        for h in (1,2,3,8,18,19,20,25):
            s=1<<h;d=s+1
            c=all_h_true_original_full_BA_cohort_upper(s)
            self.assertEqual(c["adjacent_pinned_source_Q_upper"],72*d*d)
            self.assertEqual(c["disjoint_pinned_source_Q_upper"],72*d*d+192*d)
            self.assertEqual(c["all_original_BA_cohort_source_Q_upper"],
                             72*d*d+192*d)
            self.assertTrue(c["all_global_complete_injections"])
            self.assertTrue(c["original_S_lower_NOT_PROVED"])
        m=zero_split_original_W32()
        tested_adj=tested_dis=0
        for root in range(15):
            four=occupied_root_C4_source_factors(m,side=0,root=root)[0]
            for off in range(3):
                z=exact_original_adjacent_A_transfer(
                    m,side=0,root=root,pair_offset=off,four=four)
                if z["pinned_physical_adjacent"]:
                    tested_adj+=1
                else:
                    tested_dis+=1
                    self.assertEqual(z["accepted_adjacent_A_original_Q"],0)
                self.assertLessEqual(z["accepted_adjacent_A_original_Q"],
                                     72*(m["s"]+1)**2)
        self.assertGreater(tested_adj,0)
        self.assertGreater(tested_dis,0)

    def test_06_negative_original_graph_and_physical_domains(self):
        m=zero_split_original_W32()
        four=occupied_root_C4_source_factors(m,side=0,root=0)[0]
        for kwargs in ({},{"four":None},{"side":2,"four":four},
                       {"root":15,"four":four},{"pair_offset":3,"four":four},
                       {"four":(0,1,2,3)}):
            with self.assertRaises(ValueError):
                full_original_A_Hall_cohort(m,**kwargs)
            with self.assertRaises(ValueError):
                exact_original_adjacent_A_transfer(m,**kwargs)
        with self.assertRaises(ValueError):
            full_original_A_Hall_cohort(
                dict(m,right_labels=((0,1),)*15),four=four)
        for s in (0,3,True,-4):
            with self.assertRaises(ValueError):
                all_h_true_original_full_BA_cohort_upper(s)


if __name__=="__main__":
    unittest.main()
