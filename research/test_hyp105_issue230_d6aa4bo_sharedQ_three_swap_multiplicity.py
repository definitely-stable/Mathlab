"""Independent original source W32/W34 and h>=22 shared Q 3-swap tests."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bo_sharedQ_three_swap_multiplicity import (
    all_h_shared_original_Q_three_swap_multiplicity,
    enumerate_same_Q_three_swap_repairs,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def independent_exact_physical_C6_with_three_pins(edges,physical_pin_edges):
    """Independent physical sixedge SET oracle; no rooted C6 ordering.

    For genuine W32 K6 this is exactly all 5005 six-edge physical
    subsets. Count only simple connected cycles, not two triangles.
    """
    E=tuple(edges)
    pins=set(physical_pin_edges)
    output=set()
    for six in combinations(E,6):
        if not pins<=set(six):
            continue
        d=Counter(v for edge in six for v in edge)
        if len(d)!=6 or set(d.values())!={2}:
            continue
        adj={}
        for u,v in six:
            adj.setdefault(u,set()).add(v)
            adj.setdefault(v,set()).add(u)
        reached=set()
        to_visit=[next(iter(d))]
        while to_visit:
            u=to_visit.pop()
            if u in reached:continue
            reached.add(u)
            to_visit.extend(adj[u]-reached)
        if len(reached)!=6:continue
        output.add(tuple(sorted(six)))
    return output


def independent_complete_source_swap_replay(before,path,fixed):
    state=list(before)
    seen=[tuple(state)]
    for j,k in path:
        state[j],state[k]=state[k],state[j]
        assert len(set(state))==len(state)
        assert set(state)==set(before)
        for original_id in fixed:
            assert state[original_id]==before[original_id]
        seen.append(tuple(state))
    return tuple(seen)


class AA4BOGenuineOriginalSharedQMultiplicity(unittest.TestCase):
    def test_01_all_h_gq_same_Q_pigeonhole_three_image_pins(self):
        for h in tuple(range(22,37))+(40,48,64,80):
            z=all_h_shared_original_Q_three_swap_multiplicity(1<<h)
            target=(z["a"]-5+3)//4
            self.assertEqual(
                z["uniform_same_Q_same_three_LINE_pins_distinct_global_three_swap_maps_lower"],
                target)
            self.assertGreaterEqual(z["incidence_pigeonhole_same_one_good_original_LINE_image_adjacent"],target)
            self.assertGreaterEqual(z["incidence_pigeonhole_same_one_good_original_LINE_image_disjoint"],target)
            self.assertGreater(z["minimum_distinct_C6_targets_surviving_bad_original_line_images_adjacent"],0)
            self.assertGreater(z["minimum_distinct_C6_targets_surviving_bad_original_line_images_disjoint"],0)
            self.assertTrue(z["true_original_source_six_ID_Q_common_to_ALL_repaired_maps"])
            self.assertTrue(z["unmodified_original_f_g_positive_lower_NOT_PROVED"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_five_true_W32_every_actual_source_cherry_shared_Q_many_maps(self):
        samples=[("dual_zero",zero_split_original_W32())]+[
            (n,fixture(1,n)) for n in ("lex","reverse","S68","S72")]
        seen_total=0
        groups_with_two=0
        for name,model in samples:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            counts=Counter()
            for side,by in ((0,byP),(1,byL)):
                for p in range(V):
                    for flags in combinations(by[p],2):
                        z=enumerate_same_Q_three_swap_repairs(
                            model,side,p,flags,verify=True)
                        self.assertIsNotNone(z)
                        Q=z["SAME_six_actual_original_incidence_IDs_Q_for_every_map"]
                        self.assertEqual(len(Q),6)
                        self.assertEqual(len(set(Q)),6)
                        self.assertTrue(set(flags)<=set(Q))
                        fixes=z["three_unmodified_real_original_opposite_source_factor_IDs"]
                        self.assertEqual(len(fixes),3)
                        maps=z["different_COMPLETE_repaired_original_opposite_global_maps"]
                        self.assertEqual(len(set(maps)),len(maps))
                        self.assertEqual(len(maps),len(z["all_distinct_physical_occupied_root_C6_targets"]))
                        self.assertEqual(len(maps),len(z["each_complete_repair_swaps"]))
                        if len(maps)>=2:groups_with_two+=1
                        for after,path in zip(maps,z["each_complete_repair_swaps"]):
                            self.assertLessEqual(len(path),3)
                            timeline=independent_complete_source_swap_replay(
                                z["original_complete_opposite_global_map"],path,fixes)
                            self.assertEqual(timeline[-1],after)
                            for fixed in fixes:
                                self.assertEqual(after[fixed],
                                                 z["original_complete_opposite_global_map"][fixed])
                        if p==0 and counts[side]==0:
                            rebuilt=dict(model)
                            rebuilt["right_labels" if side==0 else "left_labels"]=maps[0]
                            old=seven_census(rebuilt,independent_checks=False,witness_sets=True)
                            self.assertEqual(old["sets"][Q],
                                "B-left/A-right" if side==0 else "A-left/B-right")
                        counts[side]+=1
            self.assertEqual(counts[0],45)
            self.assertEqual(counts[1],45)
            seen_total+=sum(counts.values())
            print("AA4BO_TRUE_W32",name,"source_roots",sum(counts.values()),
                  "distinct repaired fixed-Q maps sample", len(maps))
        self.assertEqual(seen_total,450)
        self.assertGreater(groups_with_two,350)

    def test_03_real_W34_nonto_and_independent_original_class(self):
        seen=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                for p in (0,7,37):
                    flags=tuple(by[p][:2])
                    z=enumerate_same_Q_three_swap_repairs(
                        model,side,p,flags,verify=True)
                    self.assertIsNotNone(z)
                    self.assertGreater(z["distinct_GLOBAL_repaired_maps_with_SAME_Q_AND_three_pins"],1)
                    Q=z["SAME_six_actual_original_incidence_IDs_Q_for_every_map"]
                    for after in z["different_COMPLETE_repaired_original_opposite_global_maps"][:4]:
                        rebuilt=dict(model)
                        rebuilt["right_labels" if side==0 else "left_labels"]=after
                        cls=independent_joint_classify(
                            Q,"B" if side==0 else "A","A" if side==0 else "B",
                            inc,rebuilt["left_labels"],rebuilt["right_labels"])
                        self.assertEqual(cls,"B-left/A-right" if side==0 else "A-left/B-right")
                    seen+=1
        self.assertEqual(seen,12)

    def test_04_independent_physical_K6_C6_fixed_THREE_owners(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        for side,by in ((0,byP),(1,byL)):
            for p in (0,7,14):
                flags=tuple(by[p][:2])
                z=enumerate_same_Q_three_swap_repairs(model,side,p,flags)
                pins=tuple(z["original_complete_opposite_global_map"][i]
                           for i in z["three_unmodified_real_original_opposite_source_factor_IDs"])
                independent=independent_exact_physical_C6_with_three_pins(
                    z["original_complete_opposite_global_map"],pins)
                self.assertTrue(set(z["all_distinct_physical_occupied_root_C6_targets"])<=independent)
                # The AA4-BL canonical DISJOINT-pin cycle family
                # deliberately omits connected C6s with both original
                # pins consecutive along the cycle. Only subset is
                # asserted for disjoint pins, not equality to all C6.
                original_pins=tuple(z["original_complete_opposite_global_map"][inc[j][1-side]]
                                    for j in flags)
                if len(set(original_pins[0]+original_pins[1]))==3:
                    self.assertEqual(len(independent),len(z["all_distinct_physical_occupied_root_C6_targets"]))
                else:
                    self.assertGreaterEqual(len(independent),len(z["all_distinct_physical_occupied_root_C6_targets"]))

    def test_05_original_source_and_wrong_h_rejection(self):
        for s in (0,2,4,16,32,2**21,2**22+1,True,-1):
            with self.assertRaises(ValueError):
                all_h_shared_original_Q_three_swap_multiplicity(s)
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        for bad_side in (2,-1,True):
            with self.assertRaises(ValueError):
                enumerate_same_Q_three_swap_repairs(model,bad_side,0,byP[0][:2])
        for bad_flags in ((byP[0][0],)*2,(99,byP[0][1]),(True,byP[0][0])):
            with self.assertRaises(ValueError):
                enumerate_same_Q_three_swap_repairs(model,0,0,bad_flags)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                enumerate_same_Q_three_swap_repairs(bad,0,0,byP[0][:2])

    def test_06_fixed_source_six_Q_is_identical_across_TARGETS_not_extra_claim(self):
        model=fixture(1,"S68")
        _,V,a,inc,f,g,byP,byL=_original_source(model)
        for p in (0,7,14):
            z=enumerate_same_Q_three_swap_repairs(
                model,0,p,tuple(byP[p][:2]))
            Q=z["SAME_six_actual_original_incidence_IDs_Q_for_every_map"]
            self.assertEqual(len(Q),6)
            self.assertGreaterEqual(len(z["different_COMPLETE_repaired_original_opposite_global_maps"]),1)
            fixed=z["three_unmodified_real_original_opposite_source_factor_IDs"]
            self.assertEqual(len(fixed),3)
            for after in z["different_COMPLETE_repaired_original_opposite_global_maps"]:
                self.assertEqual(
                    {after[i] for i in set(inc[j][1] for j in Q)},
                    set(z["all_distinct_physical_occupied_root_C6_targets"][z[
                        "different_COMPLETE_repaired_original_opposite_global_maps"].index(after)]))
            self.assertTrue(z["one_map_simultaneously_for_all_roots_NOT_PROVED"])
            self.assertTrue(z["original_f_g_UNCHANGED_positive_NOT_PROVED"])

if __name__=="__main__":
    unittest.main()
