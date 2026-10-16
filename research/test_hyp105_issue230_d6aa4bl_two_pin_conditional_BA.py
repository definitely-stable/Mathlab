"""AA4-BL independent exact global 2-pinned original source-root B/A checks."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4be_original_D6_pins import falling
from hyp105_issue230_d6aa4bk_each_cherry_BA import (
    genuine_original_root_BA_source_pool,
)
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    occupied_A_six_two_pinned_edges,
    true_original_two_pin_root_conditional_mean,
    robust_all_h_two_root_pin_BA_floor,
    abstract_extreme_holes_two_pin_no_go,
)


def independent_unordered_K6_A_target_count_with_pins(E,pin1,pin2):
    """Completely unrelated brute of 6-PHYSICAL-EDGES SUBSETS.

    Does NOT use 6-coordinate cycle generation / any preexisting
    historical original six-source-flag GF5 classifier.
    """
    good=0
    for t in combinations(E,6):
        if pin1 not in t or pin2 not in t:continue
        cnt=Counter(v for edge in t for v in edge)
        if len(cnt)==6 and set(cnt.values())=={2}:
            good+=1
    return good


def independent_ordered_four_maps_prob(E,pin1,pin2):
    """All (V-2)_4 ordered opposite physical images under ONE bijection."""
    rem=tuple(e for e in E if e!=pin1 and e!=pin2)
    success=0
    total=0
    for tup in permutations(rem,4):
        degrees=Counter(v for e in (pin1,pin2)+tup for v in e)
        success+=int(len(degrees)==6 and set(degrees.values())=={2})
        total+=1
    return Fraction(success,total),success,total


def brute_physical_A_templates_from_sixcoords(E,a,pin1,pin2):
    """Independent 6-coordinate *set* and 70 abstract 2factor options.

    Avoid generating C6 vertex orders: enumerate simple 6-edge
    subsets of the induced 15 local K6 edges for each sixsite set.
    For physical a=14 large C(15,6)*C(14,6) cost too high, so
    restrict to physical 6-coordinate sets containing pin endpoints
    and prefilter missing edges via a lightweight 70 graph kernel.
    """
    support=set(E)
    pins={pin1,pin2}
    fixed=set(pin1+pin2)
    ans=0
    for vertices in combinations(range(a),6):
        if not fixed<=set(vertices):continue
        # Generate 10 triangle partitions and 60 connected C6 through
        # independent HAMILTONIAN path DFS permutations. Crosscheck
        # results against the production 6site/positional method.
        base=vertices[0]
        for v in permutations(vertices[1:]):
            order=(base,)+v
            if order[1]>order[5]:continue
            ed={tuple(sorted((order[i],order[(i+1)%6]))) for i in range(6)}
            ans+=int(pins<=ed and ed<=support)
        for pair in combinations(vertices[1:],2):
            t1=set((base,)+pair)
            t2=set(vertices)-t1
            edges={tuple(sorted(edge)) for part in (t1,t2)
                   for edge in combinations(sorted(part),2)}
            ans+=int(pins<=edges and edges<=support)
    return ans


class AA4BLTwoPinnedRootImages(unittest.TestCase):
    def test_01_all_dyadic_h5_to80_conditional_four_d_no_fake_source(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            cert=robust_all_h_two_root_pin_BA_floor(s)
            self.assertGreaterEqual(
                cert["exact_one_complete_globally_coherent_conditional_mean_floor"],
                4*(s+1))
            self.assertGreaterEqual(cert["adjacent_pinned_physical_connected_C6_survivor_floor"]*2,
                (cert["a"]-3)*(cert["a"]-4)*(cert["a"]-5))
            self.assertGreaterEqual(cert["disjoint_pinned_physical_connected_C6_survivor_floor"]*2,
                (cert["a"]-4)*(cert["a"]-5))
            self.assertTrue(cert["explicit_extra_max_missing_degree_assumption_REQUIRED"])
            self.assertTrue(cert["all_fully_fixed_correlated_f_g_positive_NOT_PROVED"])
        small=robust_all_h_two_root_pin_BA_floor(32,missing_max_degree=0)
        strong=robust_all_h_two_root_pin_BA_floor(32)
        self.assertGreaterEqual(small["exact_one_complete_globally_coherent_conditional_mean_floor"],
                                strong["exact_one_complete_globally_coherent_conditional_mean_floor"])

    def test_02_K6_both_adjacency_types_full_4factor_global_marginal_oracle(self):
        E=tuple(combinations(range(6),2))
        tests=[((0,1),(1,2),7),((0,1),(2,3),14)]
        for e1,e2,expected in tests:
            z=occupied_A_six_two_pinned_edges(E,6,e1,e2)
            self.assertEqual(z["occupied_physical_A_six_twofactor_with_both_pins"],expected)
            self.assertEqual(independent_unordered_K6_A_target_count_with_pins(E,e1,e2),
                             expected)
            p,count,total=independent_ordered_four_maps_prob(E,e1,e2)
            self.assertEqual(count,24*expected)
            self.assertEqual(total,falling(13,4))
            self.assertEqual(p,Fraction(24*expected,falling(13,4)))
        self.assertEqual(Fraction(120*7+90*14,210)*Fraction(24,falling(13,4)),
                         Fraction(2,143))

    def test_03_true_original_W32_all_90_roots_each_scheme_two_pin_expectations(self):
        schemes=[("dual_zero",zero_split_original_W32())]+[
            (n,fixture(1,n)) for n in ("lex","reverse","S68","S72")]
        E=tuple(combinations(range(6),2))
        pinned=(((0,1),(1,2)),((0,1),(2,3)))
        for name,model in schemes:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            count=0
            for side,by in ((0,byP),(1,byL)):
                for source in range(V):
                    for flags in combinations(by[source],2):
                        original=genuine_original_root_BA_source_pool(
                            model,side,source,flags)
                        N=original["original_six_distinct_incidence_and_opposite_source_factor_Q_count"]
                        for e1,e2 in pinned:
                            z=true_original_two_pin_root_conditional_mean(
                                model,side,source,flags,e1,e2)
                            expected=Fraction(N*24*(7 if len(set(e1+e2))==3 else 14),
                                              falling(13,4))
                            self.assertEqual(
                                z["exact_ONE_whole_global_opposite_completion_expected_BA"],
                                expected)
                            self.assertEqual(
                                z["source_sixdistinct_incidence_opposite_factor_Q_pool"],N)
                            self.assertTrue(
                                z["six_actual_original_flag_IDs_always_shared_between_both_sides"])
                        count+=1
            self.assertEqual(count,90)
            print("AA4BL_W32",name,"ninety actual original pinned source roots verified")

    def test_04_actual_original_W34_nonto_two_fixed_pins_and_independent_physical(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                E=tuple((g,f)[side])
                adjacent=next((x,y) for x in E for y in E
                              if x!=y and len(set(x+y))==3)
                disjoint=next((x,y) for x in E for y in E
                              if x!=y and len(set(x+y))==4)
                for e1,e2 in (adjacent,disjoint):
                    p=0
                    coords=tuple(v for v in range(a) if v not in (f,g)[side][p])[:4]
                    root=tuple(by[p][:2])
                    z=true_original_two_pin_root_conditional_mean(
                        model,side,p,root,e1,e2,vertex_foursets=(coords,))
                    independent=brute_physical_A_templates_from_sixcoords(E,a,e1,e2)
                    self.assertEqual(z["right_physical_A_two_pin_templates"][
                        "occupied_physical_A_six_twofactor_with_both_pins"],independent)
                    self.assertEqual(z["exact_ONE_whole_global_opposite_completion_expected_BA"],
                        Fraction(24*independent,falling(V-2,4))*
                        z["source_sixdistinct_incidence_opposite_factor_Q_pool"])

    def test_05_physical_pendant_no_go_explicitly_not_dyadic_W3_family(self):
        for a in (6,7,8,10):
            x=abstract_extreme_holes_two_pin_no_go(a)
            self.assertEqual(x["physical_missing_pairs"],a-2)
            self.assertEqual(x["V_abstract"],comb(a-1,2)+1)
            self.assertEqual(x["all_A_physical_2factors_with_two_pins"],0)
            self.assertTrue(x["is_NOT_a_proven_dyadic_true_W3_physical_support"])
            self.assertEqual(x["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        # A hole budget "m<=a-2" ALONE is NOT a sufficient
        # per-root-pinned conditional positivity hypothesis.

    def test_06_reject_bad_pinned_edges_incomplete_source_and_false_h(self):
        E=tuple(combinations(range(6),2))
        for e1,e2 in (((0,1),(0,1)),((0,1),(0,6)),((0,1),(2,2))):
            with self.assertRaises(ValueError):
                occupied_A_six_two_pinned_edges(E,6,e1,e2)
        with self.assertRaises(ValueError):
            occupied_A_six_two_pinned_edges(E[:-1]+(E[0],),6,(0,1),(2,3))
        for s in (2,4,8,16,33,48,0,True):
            with self.assertRaises(ValueError):
                robust_all_h_two_root_pin_BA_floor(s)
        for val in (-1,33,True):
            with self.assertRaises(ValueError):
                robust_all_h_two_root_pin_BA_floor(32,missing_max_degree=val)
        model=fixture(1,"lex")
        _,_,_,_,_,_,byP,_=_original_source(model)
        for flags in ((byP[0][0],)*2,(99,byP[0][1])):
            with self.assertRaises(ValueError):
                true_original_two_pin_root_conditional_mean(
                    model,0,0,flags,(0,1),(2,3))
        self.assertTrue(
            true_original_two_pin_root_conditional_mean(
                model,0,0,tuple(byP[0][:2]),(0,1),(2,3))[
                "every_fully_fixed_g_nonzero_NOT_PROVED"])

if __name__=="__main__":
    unittest.main()
