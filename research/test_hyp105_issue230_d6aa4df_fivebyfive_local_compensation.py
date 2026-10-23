"""AA4-DF: finite independent TRUE-original 5+5 local compensation tests."""
from collections import Counter
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
    original_dual_model_immutable_source_Q,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4df_fivebyfive_local_compensation import (
    SUPPORTED_LOCAL_CLASSES,
    original_local_profile_sixflag,
    original_local_five_factor_physical_certificate,
    exact_original_local_fivebyfive_seven_census,
)


def genuine_source_anchors(model,count,cut=False):
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=frozenset(range(k)) if cut else None
    Y=frozenset(range(a-k,a)) if cut else None
    out=[]
    for p in range(V):
        if X is not None and not set(f[p])<=X:continue
        for l in range(V):
            if l in pl[p] or Y is not None and not set(g[l])<=Y:continue
            original=original_nonincident_threepath(p,l,pl,lp)
            q,l0=original[1][0],original[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            out.append((p,l))
            if len(out)>=count:return tuple(out)
    return tuple(out)


def independent_local_paired_C4_sixflag_oracle(model,anchors,cap=None):
    """SECOND independently ordered source original six-ID exhaustive oracle.

    Iterate ALL true SOURCE SIX-FLAG sets from original immutable
    incidence IDs inside point/line original factor reservoirs,
    BEFORE applying the physical criterion. No module census reused.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    inc=tuple(model["incidences"])
    pinv={tuple(sorted(e)):i for i,e in enumerate(f)}
    linv={tuple(sorted(e)):j for j,e in enumerate(g)}
    point_sources={}
    line_sources={}
    for p,l in anchors:
        original=original_nonincident_threepath(p,l,pl,lp)
        q,l0=original[1][0],original[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
        if (p,q) not in point_sources:
            pc=c4_completions_from_single_and_doubled(f[p],f[q],pinv,a)
            point_sources[p,q]=pc if cap is None else pc[:cap]
        if (l,l0) not in line_sources:
            lc=c4_completions_from_single_and_doubled(g[l],g[l0],linv,a)
            line_sources[l,l0]=lc if cap is None else lc[:cap]
    total=0;classes=Counter();no_positive=0;failmarked=0
    unique=set()
    for p,l in anchors:
        original=original_nonincident_threepath(p,l,pl,lp)
        q,l0=original[1][0],original[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
        for pt in point_sources[p,q]:
            for lt in line_sources[l,l0]:
                sources_point=frozenset((p,q,*pt))
                sources_line=frozenset((l,l0,*lt))
                flagidx=tuple(z for z,(ip,jl) in enumerate(inc)
                              if ip in sources_point and jl in sources_line)
                n=0
                for ids in combinations(flagidx,6):
                    # Independent historical all-seven oracle, actual source IDs
                    kind=classify_seven_all_a_original_Q(ids,f,g,inc)
                    if kind:
                        selfcheck=original_local_profile_sixflag(ids,inc,f,g)
                        if selfcheck!=kind:
                            raise AssertionError("independent historical and source original 5x5 oracle disagreement")
                        classes[kind]+=1;n+=1;unique.add(tuple(sorted(ids)))
                total+=1
                if not n:no_positive+=1
    return {"C4":total,"classes":dict(classes),"no_positive":no_positive,
            "distinct":len(unique)}


def independent_structural_BC_source_geometry(f,base,doubled,C4):
    """No seven-class oracle: brute every distinct 3-/5-source physical form.

    The SOURCE reservoir is a 4cycle of ACTUAL occupied pair images plus
    one disconnected doubled source edge. Count 2 physical C profile
    triples and 1 physical B repeated-source candidate, by brute 5.
    """
    ids=(base,doubled,*C4)
    def regular(physical_image_ids):
        deg=Counter(v for src in physical_image_ids for v in f[src])
        return len(deg)==6 and set(deg.values())=={2}
    C3={tuple(sorted(x)) for x in combinations(ids,3)
        if regular(tuple(src for y in x for src in (y,y)))}
    B5={rep for rep in ids if regular(ids+(rep,))}
    return C3,B5


class AA4DFTrueOriginalFiveByFive(unittest.TestCase):
    def test_01_exhaustive_K6_physical_cycle_plus_disjoint_edge_source_profiles(self):
        # One ACTUAL two-edge physical alphabet pattern; the SOURCE
        # structural identity is independent of how W3 source IDs are
        # assigned globally and independent of physical coordinate names.
        f=((0,1),(4,5),(0,2),(2,3),(3,1))
        structural=original_local_five_factor_physical_certificate(
            f,f,0,1,(2,3,4),0,1,(2,3,4))
        p=structural["POINT"]
        self.assertEqual(p["original_B_only_possible_repeated_source_factor"],1)
        self.assertEqual(set(p["original_C_possible_three_repeated_source_factor_sets"]),
                         {(0,1,3),(1,2,4)})
        C3,B5=independent_structural_BC_source_geometry(f,0,1,(2,3,4))
        self.assertEqual(C3,set(p["original_C_possible_three_repeated_source_factor_sets"]))
        self.assertEqual(B5,{1})
        # exhaust every source factor order on ONE occupied K6 4cycle
        # and every two choices of source-spoke centers from W32 images.
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        for p,l in genuine_source_anchors(model,8):
            tr=original_nonincident_threepath(p,l,pl,lp)
            q,l0=tr[1][0],tr[0][1]
            fp={tuple(sorted(e)):z for z,e in enumerate(f)}
            gl={tuple(sorted(e)):z for z,e in enumerate(g)}
            point=c4_completions_from_single_and_doubled(f[p],f[q],fp,a)
            line=c4_completions_from_single_and_doubled(g[l],g[l0],gl,a)
            for pc in point[:5]:
                for lc in line[:5]:
                    z=original_local_five_factor_physical_certificate(f,g,p,q,pc,l,l0,lc)
                    for labels,base,double,three,typ in (
                        (f,p,q,pc,"POINT"),(g,l,l0,lc,"LINE")
                    ):
                        C3,B5=independent_structural_BC_source_geometry(labels,base,double,three)
                        self.assertEqual(C3,set(
                            z[typ]["original_C_possible_three_repeated_source_factor_sets"]))
                        self.assertEqual(B5,{double})
        print("AA4DF_SOURCE_5X5_TWO_C_PROFILES_ONE_B_REPEATED_FACTOR_OK",flush=True)

    def test_02_true_original_W32_lex_S72_full_real_C4_local_GF5_oracle(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            anchors=genuine_source_anchors(model,12)
            z=exact_original_local_fivebyfive_seven_census(model,anchor_pairs=anchors)
            r=independent_local_paired_C4_sixflag_oracle(model,anchors)
            self.assertEqual(z["original_occupied_C4_pairs_checked"],r["C4"])
            self.assertEqual(z["local_accepted_historical_sevenclass_G5_multiset_by_label"],r["classes"])
            self.assertEqual(z["local_accepted_six_original_incidence_ID_sets_distinct_across_reservoirs"],r["distinct"])
            self.assertEqual(set(r["classes"])-SUPPORTED_LOCAL_CLASSES,set())
            self.assertGreater(z["true_original_marked_cofactor_Hall_failing_C4_pairs"],0)
            self.assertGreater(
                z["true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes"],0,
                "Need an ACTUAL ORIGINAL local Hall-marked zero-compensation witness")
            w=z["first_exact_genuine_original_Hall_marked_but_NO_LOCAL_positive_witness"]
            self.assertTrue(w["zero_accepted_local_sevenclass_G5_SOURCE_sixflags"])
            if len(w["all_genuine_original_source_incidence_IDs_inside_reservoir"])<6:
                self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            print("AA4DF_TRUE_ORIGINAL_W32_5X5_GF5_NO_LOCAL_RESCUE",
                  scheme,"C4pairs",r["C4"],"positive_class_multisets",r["classes"],
                  "failed_no_local_positive",
                  z["true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes"],
                  "first_source_witness",w,flush=True)

    def test_03_true_original_W32_point_line_dual_local_seven_class_invariance(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            anchors=genuine_source_anchors(model,8)
            dual=original_dual_model_immutable_source_Q(model)
            z=exact_original_local_fivebyfive_seven_census(model,anchor_pairs=anchors)
            w=exact_original_local_fivebyfive_seven_census(
                dual,anchor_pairs=tuple((l,p) for p,l in anchors))
            self.assertEqual(z["original_occupied_C4_pairs_checked"],
                             w["original_occupied_C4_pairs_checked"])
            self.assertEqual(z["local_accepted_historical_sevenclass_G5_multiset_by_label"],
                             w["local_accepted_historical_sevenclass_G5_multiset_by_label"])
            self.assertEqual(
                z["true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes"],
                w["true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes"])
            print("AA4DF_GENUINE_ORIGINAL_W32_DUAL_5X5_SEVEN_SOURCE_IDS",
                  scheme,z["local_accepted_historical_sevenclass_G5_multiset_by_label"],flush=True)

    def test_04_true_original_W34_lex_random_fixed_global_full_C4_local_GF5(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            anchors=genuine_source_anchors(model,8,cut=True)
            self.assertEqual(len(anchors),8)
            z=exact_original_local_fivebyfive_seven_census(model,anchor_pairs=anchors)
            r=independent_local_paired_C4_sixflag_oracle(model,anchors)
            self.assertEqual(z["original_occupied_C4_pairs_checked"],r["C4"])
            self.assertEqual(z["local_accepted_historical_sevenclass_G5_multiset_by_label"],r["classes"])
            self.assertEqual(z["local_accepted_six_original_incidence_ID_sets_distinct_across_reservoirs"],r["distinct"])
            self.assertGreater(z["true_original_marked_cofactor_Hall_failing_C4_pairs"],0)
            self.assertTrue(z["cannot_infer_ROOT_all_seven_global_S_from_local_reservoir"])
            print("AA4DF_TRUE_ORIGINAL_W34_COMPLETE_TYPED_MAPS",scheme,
                  "C4pairs",r["C4"],"local_Q",r["classes"],
                  "Hall_no_local_positive",z[
                      "true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes"],flush=True)

    def test_05_true_original_W38_explicitly_PARTIAL_C4_5X5_seven_classes(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            anchors=genuine_source_anchors(model,4)
            self.assertEqual(len(anchors),4)
            z=exact_original_local_fivebyfive_seven_census(
                model,anchor_pairs=anchors,max_triples_per_side=8)
            self.assertTrue(z["C4_cap_means_partial"])
            self.assertLessEqual(z["original_occupied_C4_pairs_checked"],4*8*8)
            self.assertEqual(set(z["local_accepted_historical_sevenclass_G5_multiset_by_label"])-SUPPORTED_LOCAL_CLASSES,set())
            print("AA4DF_TRUE_ORIGINAL_W38_PARTIAL_NOT_GLOBAL",scheme,
                  "C4pairs",z["original_occupied_C4_pairs_checked"],
                  "classes",z["local_accepted_historical_sevenclass_G5_multiset_by_label"],flush=True)

    def test_06_failclosed_forged_source_3path_labels_bad_C4_and_Q(self):
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        for ids in ((0,0,1,2,3,4),(0,1,2,3,4,V*(s+1)),(0,1,2,3,4,True)):
            with self.assertRaises(ValueError):
                original_local_profile_sixflag(ids,tuple(model["incidences"]),f,g)
        for cap in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                exact_original_local_fivebyfive_seven_census(
                    model,anchor_pairs=(),max_triples_per_side=cap)
        with self.assertRaises(ValueError):
            exact_original_local_fivebyfive_seven_census(model,anchor_pairs=None)
        with self.assertRaises(ValueError):
            original_local_five_factor_physical_certificate(
                f,g,0,0,(1,2,3),0,0,(1,2,3))
        bad=dict(model);labels=list(model["left_labels"]);labels[0]=labels[1]
        bad["left_labels"]=tuple(labels)
        with self.assertRaises(ValueError):
            exact_original_local_fivebyfive_seven_census(bad,anchor_pairs=())


if __name__=="__main__":unittest.main()
