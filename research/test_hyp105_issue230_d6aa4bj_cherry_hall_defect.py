"""AA4-BJ independent original W32/W34 source-cherry FIRST residual oracles."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bi_original_cherry_moment import (
    true_original_fixed_pair_source_cherry_fiber,
)
from hyp105_issue230_d6aa4bj_cherry_hall_defect import (
    cherry_unilateral_all_h_lower,actual_original_cherry_anchor,
    actual_original_W32_complete_cherry_defect,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def independent_literal_fourflag_source_completion(model,side,p,two_flags,vertices):
    """Brute all 4 distinct ORIGINAL remaining incidence IDs; no physical C4 enum.

    Restrict physical first-side pair coordinates to EXACTLY four values
    and verify the point/line physical degree two by literal degree
    counts. Opposite physical mask check is independent of the
    production optimized source-first kernel.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    root=(f,g)[side][p]
    labels=(f,g)[side]
    other=(g,f)[side]
    chosen=tuple(two_flags)
    vertices=set(vertices)
    avail=[
        j for j,(sp,sl) in enumerate(inc)
        if j not in chosen and inc[j][side]!=p and
        set(labels[inc[j][side]])<=vertices
    ]
    unilateral=both=0
    for picked in combinations(avail,4):
        degree=Counter(x for i in picked
                       for x in labels[inc[i][side]])
        if set(degree)!=vertices or any(t!=2 for t in degree.values()):
            continue
        unilateral+=1
        all_six=chosen+picked
        opposite=Counter(x for i in all_six
                         for x in other[inc[i][1-side]])
        if len(opposite)==6 and set(opposite.values())=={2}:
            both+=1
    return unilateral,both


class AA4BJTrueOriginalSourceCherryHall(unittest.TestCase):
    def test_01_all_h_explicit_robust_C4_matching_missing_edge_loss(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            s=1<<h
            z=cherry_unilateral_all_h_lower(s)
            self.assertGreater(z["all_h_each_actual_original_cherry_unilateral_fourflag_lower"],0)
            self.assertGreater(z["both_types_unilateral_candidate_incidence_lower"],0)
            self.assertTrue(z["every_f_g_joint_same_Q_extension_lower_NOT_PROVED"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            if h==1:
                self.assertEqual(z["complete_physical_C4_count_on_complement"],3)
                self.assertEqual(z["all_h_each_actual_original_cherry_unilateral_fourflag_lower"],270)
                self.assertEqual(z["both_types_unilateral_candidate_incidence_lower"],24300)
            if h==2:
                self.assertEqual(z["a"],14)
                self.assertEqual(z["m"],6)
                self.assertEqual(z["occupied_physical_C4_per_root_lower"],945)
                self.assertEqual(z["occupied_disjoint_physical_two_edge_matching_per_root_lower"],1215)
                self.assertEqual(z["all_h_each_actual_original_cherry_unilateral_fourflag_lower"],
                                 625*945+100*1215)
            if h>=5:
                self.assertGreaterEqual(z["occupied_physical_C4_per_root_lower"]*100,
                                        z["complete_physical_C4_count_on_complement"]*96)

    def test_02_all_five_true_W32_90_original_source_cherries_against_independent_M1(self):
        models=[("dual_zero",zero_split_original_W32())]+[
            (n,fixture(1,n)) for n in ("lex","reverse","S68","S72")]
        expected={"dual_zero":142,"lex":295,"reverse":184,"S68":71,"S72":79}
        for name,model in models:
            new=actual_original_W32_complete_cherry_defect(model)
            self.assertEqual(new["true_original_cherry_anchor_count"],90)
            self.assertEqual(new["one_sided_original_sixflag_reservoir_total"],24300)
            self.assertEqual(new["two_sided_original_sevenGF5_nonAA_first_cherry_moment"],
                             expected[name])
            self.assertEqual(new["original_cherry_Hall_failures_total"],
                             24300-expected[name])
            old=true_original_fixed_pair_source_cherry_fiber(
                model,tuple(range(6)))["sectors"][tuple(range(6))]
            self.assertEqual(new["two_sided_original_sevenGF5_nonAA_first_cherry_moment"],
                             old["source_cherry_binomial_moments_M1_to_M4"][0])
            self.assertGreater(new["fully_nonextendible_actual_original_cherries"],0)
            self.assertEqual(
                sum(new["root_anchored_success_histogram"].values()),90)
            self.assertEqual(sum(new["original_two_sided_joint_by_root_type"].values()),
                             expected[name])
            print("AA4BJ_TRUE_W32",name,"M1",expected[name],
                  "failed",new["original_cherry_Hall_failures_total"],
                  "zero_anchor",new["fully_nonextendible_actual_original_cherries"])
        # Every actual full map has ALL one-sided source anchored
        # candidates, yet little of that reservoir survives same-source-Q
        # original two-type Hall. Finite evidence, not asymptotic counterfamily.

    def test_03_independent_real_W34_nonto_4coordinate_C4_or_2double_shapes(self):
        checked=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side in (0,1):
                p=0
                root=(f,g)[side][p]
                vertices=tuple(j for j in range(a) if j not in root)[:4]
                by=(byP,byL)[side]
                flags=tuple(by[p][:2])
                got=actual_original_cherry_anchor(
                    model,side,p,flags,vertex_foursets=(vertices,))
                brute=independent_literal_fourflag_source_completion(
                    model,side,p,flags,vertices)
                self.assertEqual((
                    got["exact_one_side_original_sixflag_extensions"],
                    got["exact_both_sides_same_original_sixflag_accepted_nonAA"]
                ),brute)
                self.assertFalse(got["all_complement_foursets_covered"])
                self.assertEqual(got["physical_fourcoordinate_subsets_checked"],1)
                self.assertGreaterEqual(got["exact_one_side_original_sixflag_extensions"],0)
                checked+=1
        self.assertEqual(checked,4)

    def test_04_true_W32_exact_each_anchor_B_C_shape_and_source_injection(self):
        for name in ("lex","S68"):
            model=fixture(1,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            for side,by in ((0,byP),(1,byL)):
                for p in (0,7,14):
                    flags=tuple(by[p][:2])
                    z=actual_original_cherry_anchor(model,side,p,flags)
                    self.assertEqual(z["source_original_occupied_C4_residuals"],3)
                    self.assertEqual(z["source_original_occupied_double_matching_residuals"],3)
                    self.assertEqual(z["exact_one_side_original_sixflag_extensions"],270)
                    self.assertGreaterEqual(z["exact_one_side_to_opposite_side_Hall_failures"],0)
                    for Q in z["example_actual_original_sixflag_Q"]:
                        self.assertEqual(len(set(Q)),6)
                        self.assertTrue(set(flags)<=set(Q))
                        for i in Q:
                            self.assertIn(inc[i][side],range(15))

    def test_05_dual_original_physical_coordinate_gauge_preserves_cherry(self):
        m=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(m)
        z0=actual_original_cherry_anchor(m,0,0,byP[0][:2])
        swapped=dict(m,
          left_labels=tuple(tuple(sorted(((i+2)%6 for i in e))) for e in m["left_labels"]),
          right_labels=tuple(tuple(sorted(((5-i)%6 for i in e))) for e in m["right_labels"]))
        z1=actual_original_cherry_anchor(swapped,0,0,byP[0][:2])
        for key in ("source_original_occupied_C4_residuals",
                    "source_original_occupied_double_matching_residuals",
                    "exact_one_side_original_sixflag_extensions",
                    "exact_both_sides_same_original_sixflag_accepted_nonAA",
                    "exact_one_side_to_opposite_side_Hall_failures"):
            self.assertEqual(z0[key],z1[key])

    def test_06_strict_original_source_model_flags_and_physical_input_rejection(self):
        model=fixture(1,"lex")
        _,_,_,_,_,_,byP,byL=_original_source(model)
        for invalid in ((0,0),(-1,1),(0,30),(True,1)):
            with self.assertRaises(ValueError):
                actual_original_cherry_anchor(model,0,0,invalid)
        for bad in (2,3,True,-1):
            with self.assertRaises(ValueError):
                actual_original_cherry_anchor(model,bad,0,byP[0][:2])
        for invalid in (((0,1,2,3),(0,1,2,3)),
                        ((0,1,2,3),), ((0,1,2,6),)):
            with self.assertRaises(ValueError):
                actual_original_cherry_anchor(model,0,0,byP[0][:2],
                                               vertex_foursets=invalid)
        for bad in (0,3,33,-4,True):
            with self.assertRaises(ValueError):
                cherry_unilateral_all_h_lower(bad)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                actual_original_W32_complete_cherry_defect(bad)
        with self.assertRaises(ValueError):
            actual_original_W32_complete_cherry_defect(fixture(2,"lex"))

if __name__=="__main__":
    unittest.main()
