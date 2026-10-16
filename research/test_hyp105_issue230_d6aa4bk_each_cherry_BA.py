"""AA4-BK: every ACTUAL original GQ cherry, one global opposite image, B/A."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations,product

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bk_each_cherry_BA import (
    physical_simple_twofactor_6_count,
    root_cherry_BA_quenched_all_h_lower,
    genuine_original_root_BA_source_pool,
)
from hyp105_issue230_d6aa4be_original_D6_pins import falling
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, classify_seven_prechecked,
)


def independent_original_brute_C4_root_Q(model,side,p,flags,coords):
    """Select four real ORIGINAL source incidence IDs, not physical 4-cycle patterns."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    root_phys=(f,g)[side][p]
    first=(f,g)[side]
    other=(g,f)[side]
    eligible=[j for j in range(len(inc))
              if j not in flags and inc[j][side]!=p
              and set(first[inc[j][side]])<=set(coords)]
    good=set()
    fixed_right=0
    for four in combinations(eligible,4):
        q=tuple(sorted(tuple(flags)+four))
        original_primary=tuple(inc[j][side] for j in four)
        original_opposite=tuple(inc[j][1-side] for j in q)
        if len(set(original_primary))!=4 or len(set(original_opposite))!=6:
            continue
        source_degree=Counter(u for j in four for u in first[inc[j][side]])
        if set(source_degree)!=set(coords) or any(x!=2 for x in source_degree.values()):
            continue
        good.add(q)
        opposite_degree=Counter(u for j in q for u in other[inc[j][1-side]])
        if len(opposite_degree)==6 and set(opposite_degree.values())=={2}:
            fixed_right+=1
    return len(good),fixed_right


def independent_all_K6_simple_six_templates():
    """Independent physical 6-edge-subset enumeration, not target 60+10 constructor."""
    ed=tuple(combinations(range(6),2))
    count=0
    for picked in combinations(ed,6):
        degrees=Counter(j for e in picked for j in e)
        if len(degrees)==6 and set(degrees.values())=={2}:
            count+=1
    return count


class AA4BKEachTrueOriginalCherryQuenchedBA(unittest.TestCase):
    def test_01_all_h_uniform_every_cherry_72d_strict_exact_rational(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            z=root_cherry_BA_quenched_all_h_lower(s)
            self.assertEqual(z["h"],h)
            self.assertGreaterEqual(
                z["one_global_complete_opposite_map_accepted_original_BA_mean_lower"],
                72*(s+1))
            self.assertGreaterEqual(z["physical_root_complement_C4_min"],
                                    Fraction(z["a"]**4,10))
            self.assertGreaterEqual(z["physical_occupied_right_C6_min"],
                                    Fraction(z["a"]**6,16))
            self.assertTrue(
                z["every_individually_fixed_full_original_f_g_bound_NOT_PROVED"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_5_real_W32_ALL_90_roots_exact_BA_global_first_moment_and_historical(self):
        K6_right=independent_all_K6_simple_six_templates()
        self.assertEqual(K6_right,70)
        pA=Fraction(720*70,falling(15,6))
        self.assertEqual(pA,Fraction(2,143))
        models=[("dual_zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        for name,model in models:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            total_fixed=[0,0]
            total_ensemble=[Fraction(),Fraction()]
            total_src=[0,0]
            total_cherries=0
            for side,by in ((0,byP),(1,byL)):
                for root in range(V):
                    for flags in combinations(by[root],2):
                        z=genuine_original_root_BA_source_pool(model,side,root,flags)
                        self.assertEqual(z["physical_C4_root_residuals"],3)
                        self.assertEqual(
                            z["occupied_opposite_physical_simple_twofactor_counts"][
                                "right_simple_twofactor_A_total"],70)
                        self.assertEqual(
                            z["one_globally_uniform_opposite_map_exact_BA_probability_for_each_true_original_Q"],
                            pA)
                        self.assertEqual(
                            z["ONE_global_opposite_map_expected_original_BA_accepted_count"],
                            z["original_six_distinct_incidence_and_opposite_source_factor_Q_count"]*pA)
                        total_fixed[side]+=z["fixed_pair_original_BA_accepted_count"]
                        total_ensemble[side]+=z["ONE_global_opposite_map_expected_original_BA_accepted_count"]
                        total_src[side]+=z["original_six_distinct_incidence_and_opposite_source_factor_Q_count"]
                        total_cherries+=1
            self.assertEqual(total_cherries,90)
            historic=seven_census(model,independent_checks=False)
            cls=historic["seven_class_motif_counts"]
            self.assertEqual(total_fixed[0],cls["B-left/A-right"])
            self.assertEqual(total_fixed[1],cls["A-left/B-right"])
            self.assertGreater(total_src[0],0)
            self.assertGreater(total_src[1],0)
            self.assertEqual(total_ensemble[0],total_src[0]*pA)
            self.assertEqual(total_ensemble[1],total_src[1]*pA)
            self.assertTrue(all(q>0 for q in total_ensemble))
            print("AA4BK_W32",name,"true_root_BA",tuple(total_fixed),
                  "random_global_right_expected",tuple(map(str,total_ensemble)))

    def test_03_independent_real_W34_both_typed_and_two_schemes_partial_root(self):
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                p=0
                coords=tuple(v for v in range(a)
                             if v not in (f,g)[side][p])[:4]
                flags=tuple(by[p][:2])
                z=genuine_original_root_BA_source_pool(
                    model,side,p,flags,vertex_foursets=(coords,))
                independent=independent_original_brute_C4_root_Q(
                    model,side,p,flags,coords)
                self.assertEqual((
                    z["original_six_distinct_incidence_and_opposite_source_factor_Q_count"],
                    z["fixed_pair_original_BA_accepted_count"]),independent)
                self.assertGreater(
                    z["occupied_opposite_physical_simple_twofactor_counts"][
                        "right_simple_twofactor_A_total"],0)
                self.assertGreaterEqual(
                    z["ONE_global_opposite_map_expected_original_BA_accepted_count"],0)
                self.assertTrue(z["retains_true_same_six_original_source_incidence_IDs"])

    def test_04_exact_K6_global_injection_probability_and_typed_coordinate_gauge(self):
        assert independent_all_K6_simple_six_templates()==70
        base=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(base)
        root,flags=0,tuple(byP[0][:2])
        c0=genuine_original_root_BA_source_pool(base,0,root,flags)
        remapped=dict(base,
            left_labels=tuple(tuple(sorted(((i+2)%6 for i in e))) for e in base["left_labels"]),
            right_labels=tuple(tuple(sorted(((5-i)%6 for i in e))) for e in base["right_labels"]))
        c1=genuine_original_root_BA_source_pool(remapped,0,root,flags)
        for key in (
            "original_six_distinct_incidence_and_opposite_source_factor_Q_count",
            "fixed_pair_original_BA_accepted_count",
            "ONE_global_opposite_map_expected_original_BA_accepted_count",
        ):
            self.assertEqual(c0[key],c1[key])

    def test_05_true_W32_independent_root_original_GF5_class_positional_check(self):
        model=fixture(1,"S68")
        _,V,a,inc,f,g,byP,byL=_original_source(model)
        root=0;flags=tuple(byP[root][:2])
        z=genuine_original_root_BA_source_pool(model,0,root,flags)
        brute=independent_original_brute_C4_root_Q(
            model,0,root,flags,tuple(j for j in range(a) if j not in f[root]))
        self.assertEqual(
            (z["original_six_distinct_incidence_and_opposite_source_factor_Q_count"],
             z["fixed_pair_original_BA_accepted_count"]),brute)
        self.assertTrue(z["same_given_fully_fixed_opposite_map_is_NOT_guaranteed_positive"])
        self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_06_fake_genuine_original_input_and_bad_quantifiers_reject(self):
        for s in (0,2,4,8,16,24,33,48,True):
            with self.assertRaises(ValueError):
                root_cherry_BA_quenched_all_h_lower(s)
        model=fixture(1,"lex")
        _,V,a,inc,f,g,byP,byL=_original_source(model)
        for kwargs in (
            dict(side=2,source_factor=0,source_flag_ids=tuple(byP[0][:2])),
            dict(side=0,source_factor=V,source_flag_ids=tuple(byP[0][:2])),
            dict(side=0,source_factor=0,source_flag_ids=(byP[0][0],)*2),
            dict(side=0,source_factor=0,source_flag_ids=(0,999)),
            dict(side=0,source_factor=0,source_flag_ids=tuple(byP[0][:2]),
                 vertex_foursets=((0,1,2,3),)),
        ):
            with self.assertRaises(ValueError):
                genuine_original_root_BA_source_pool(model,**kwargs)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                genuine_original_root_BA_source_pool(bad,0,0,tuple(byP[0][:2]))

if __name__=="__main__":
    unittest.main()
