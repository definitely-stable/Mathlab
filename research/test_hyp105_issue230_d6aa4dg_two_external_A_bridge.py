"""AA4-DG: independent K6 8-template and genuine original W32/W34/W38 GF5."""

from collections import Counter
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4dg_two_external_A_bridge import (
    A_SIDE_POSITIVE_CLASSES,_physical_original_A_six_edges,
    original_two_external_A_completion_catalogue,
    original_two_external_A_anchor_certificate,
)


def independent_two_external_original_factor_brute(labels,base,doubled,C4):
    """Completely separate all physical 6-factor subsets enumeration."""
    labels=tuple(labels);local={base,doubled,*C4}
    candidates=set()
    for four in combinations(sorted(local),4):
        for ext in combinations(tuple(i for i in range(len(labels)) if i not in local),2):
            six=tuple(sorted((*four,*ext)))
            degree=Counter(v for src in six for v in labels[src])
            if len(degree)==6 and set(degree.values())=={2}:
                candidates.add(six)
    return candidates


def original_sample_real_P3(model,num):
    s,V,a,f,g,pl,lp=_validated_original(model)
    out=[]
    for p in range(V):
        for l in range(V):
            if l in pl[p]:continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            out.append((p,l))
            if len(out)>=num:return tuple(out)
    return tuple(out)


def independent_original_A_sixflag_C4pair_oracle(model,p,l,PT,LT):
    """Independent 6-ID-first historical source-Q audit of ONE real C4 pair.

    Uses brute SOURCE factor 6sets with 4 local + 2 external on A,
    not eight-template catalogue nor source module's anchored
    enumeration routine; accepted 7GF5 historical original source
    oracle called on EXACT immutable six original IDs.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    path=original_nonincident_threepath(p,l,pl,lp)
    q,l0=path[1][0],path[0][1]
    p5=tuple(sorted({p,q,*PT}));l5=tuple(sorted({l,l0,*LT}))
    ap=independent_two_external_original_factor_brute(f,p,q,PT)
    al=independent_two_external_original_factor_brute(g,l,l0,LT)
    inc=tuple(model["incidences"])
    fl={(i,j):k for k,(i,j) in enumerate(inc)}
    cases=[((P,l5) for P in ap),
           ((p5,L) for L in al),
           ((P,L) for P in ap for L in al)]
    Qs=set();cls=Counter()
    for pairs in cases:
        for P,L in pairs:
            real_ids=tuple(fl[i,j] for i in P for j in L if (i,j) in fl)
            for six in combinations(real_ids,6):
                Q=tuple(sorted(six))
                if Q in Qs:continue
                kind=classify_seven_all_a_original_Q(Q,f,g,inc)
                if kind in A_SIDE_POSITIVE_CLASSES:
                    Qs.add(Q);cls[kind]+=1
    return {"classes":dict(cls),"distinct":len(Qs),
            "A_point":len(ap),"A_line":len(al)}


class AA4DGTwoExternalOriginalBridge(unittest.TestCase):
    def test_01_canonical_K6_exhaustive_ALL_6_factor_sets_eight_templates(self):
        labels=tuple(combinations(range(6),2))
        inv={e:i for i,e in enumerate(labels)}
        base,doubled=inv[0,1],inv[4,5]
        C4=tuple(inv[e] for e in ((0,2),(2,3),(1,3)))
        actual=original_two_external_A_completion_catalogue(labels,base,doubled,C4)
        independent=independent_two_external_original_factor_brute(labels,base,doubled,C4)
        self.assertEqual(set(actual),independent)
        self.assertEqual(len(actual),8)
        for six in actual:
            self.assertEqual(len(set(six)-{base,doubled,*C4}),2)
            self.assertIn(doubled,six)
            self.assertEqual(len({base,*C4}&set(six)),3)
            self.assertTrue(_physical_original_A_six_edges(labels,six))
        # All six-ORIGINAL-factor K6 physical 2factors with >=5 from
        # the original 4cycle+disjoint doubled physical 5 factors:
        # NONE. An A-type cannot leave this source factor reservoir
        # via only one new typed original factor.
        for ext in range(len(labels)):
            if ext in {base,doubled,*C4}:continue
            six=tuple(sorted((base,doubled,*C4,ext)))
            self.assertFalse(_physical_original_A_six_edges(labels,six))
        print("AA4DG_CANONICAL_PHYSICAL_4CYCLE_DOUBLED_SOURCE_K6",
              "exact_two_external_templates",len(actual),
              "one_external_A_impossible",True,flush=True)

    def test_02_true_original_W32_W34_independent_full_6factor_A_source_brute(self):
        for power,schemes,num in ((1,("lex","S72"),8),
                                  (2,("lex","random"),2)):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                anchors=original_sample_real_P3(model,num)
                got=0
                pinv={e:i for i,e in enumerate(f)}
                linv={e:i for i,e in enumerate(g)}
                for p,l in anchors:
                    path=original_nonincident_threepath(p,l,pl,lp)
                    q,l0=path[1][0],path[0][1]
                    P=c4_completions_from_single_and_doubled(f[p],f[q],pinv,a)
                    L=c4_completions_from_single_and_doubled(g[l],g[l0],linv,a)
                    for side,base,double,comp in (
                        (f,p,q,P[:2]),(g,l,l0,L[:2])):
                        for C4 in comp:
                            fast=original_two_external_A_completion_catalogue(
                                side,base,double,C4)
                            brute=independent_two_external_original_factor_brute(
                                side,base,double,C4)
                            self.assertEqual(set(fast),brute)
                            self.assertLessEqual(len(fast),8)
                            got+=1
                self.assertGreater(got,0)
                print("AA4DG_TRUE_ORIGINAL_COMPLETE_GLOBAL_TWO_EXTERNAL_A_GATES",
                      s,scheme,"true_original_P3s",len(anchors),
                      "actual_source_C4_sides_bruted",got,flush=True)

    def test_03_true_original_W32_hist_seven_A_side_two_external_ID_referee(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            anchors=original_sample_real_P3(model,4)
            z=original_two_external_A_anchor_certificate(
                model,anchor_pairs=anchors,max_C4_pairs=8)
            s,V,a,f,g,pl,lp=_validated_original(model)
            pinv={e:i for i,e in enumerate(f)}
            linv={e:i for i,e in enumerate(g)}
            checked=0;classes=Counter();Q_distinct=set()
            for p,l in anchors:
                path=original_nonincident_threepath(p,l,pl,lp)
                q,l0=path[1][0],path[0][1]
                for PT in c4_completions_from_single_and_doubled(f[p],f[q],pinv,a):
                    for LT in c4_completions_from_single_and_doubled(g[l],g[l0],linv,a):
                        if checked>=8:break
                        x=independent_original_A_sixflag_C4pair_oracle(
                            model,p,l,PT,LT)
                        classes.update(x["classes"])
                        checked+=1
                    if checked>=8:break
                if checked>=8:break
            self.assertEqual(checked,z["physical_original_C4_pair_reservoirs_checked"])
            self.assertEqual(dict(classes),
                             {k:v for k,v in z[
                                "historical_A_side_original_sixflag_C4_pair_multiplicities"].items()
                              if v})
            self.assertTrue(z["explicitly_PARTIAL_if_C4_capped"])
            self.assertLessEqual(
                z["historical_A_side_original_sixflag_distinct_Q_count"],
                z["historical_A_side_original_sixflag_C4_pair_multiplicity_total"])
            print("AA4DG_REAL_W32_A_CLASS_IMMUTABLE_SIXFLAGS",scheme,
                  "C4pairs",checked,"historical_A_side",dict(classes),flush=True)

    def test_04_true_original_W34_actual_nonlocal_historical_G5_two_external(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            anchors=original_sample_real_P3(model,2)
            z=original_two_external_A_anchor_certificate(
                model,anchor_pairs=anchors,max_C4_pairs=3)
            s,V,a,f,g,pl,lp=_validated_original(model)
            invf={e:i for i,e in enumerate(f)}
            invg={e:i for i,e in enumerate(g)}
            p,l=anchors[0]
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            pts=c4_completions_from_single_and_doubled(f[p],f[q],invf,a)
            lns=c4_completions_from_single_and_doubled(g[l],g[l0],invg,a)
            direct=Counter()
            for pt in pts[:1]:
                for lt in lns[:3]:
                    direct.update(independent_original_A_sixflag_C4pair_oracle(
                        model,p,l,pt,lt)["classes"])
            self.assertEqual(z["physical_original_C4_pair_reservoirs_checked"],3)
            self.assertEqual({k:v for k,v in z[
                "historical_A_side_original_sixflag_C4_pair_multiplicities"].items() if v},
                             dict(direct))
            print("AA4DG_W34_TRUE_SOURCE_NONLOCAL_FROZEN_CORRELATED_GF5",scheme,
                  "source_C4_pair_count",3,
                  "two_source_external_A_original_sixflag_Q_classes",
                  dict(direct),flush=True)

    def test_05_TRUE_original_W38_strict_PARTIAL_nonlocal_A_bridge(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            anchors=original_sample_real_P3(model,1)
            z=original_two_external_A_anchor_certificate(
                model,anchor_pairs=anchors,max_C4_pairs=2)
            self.assertEqual(z["physical_original_C4_pair_reservoirs_checked"],2)
            self.assertTrue(z["explicitly_PARTIAL_if_C4_capped"])
            self.assertLessEqual(z["historical_A_side_original_sixflag_distinct_Q_count"],
                                 z["historical_A_side_original_sixflag_C4_pair_multiplicity_total"])
            print("AA4DG_W38_SOURCE_SMALL_SAMPLE_NOT_ALLH_COMPENSATION",
                  scheme,"POINT_A_templates",
                  z["physical_occupied_POINT_two_external_A_templates"],
                  "LINE_A_templates",
                  z["physical_occupied_LINE_two_external_A_templates"],flush=True)

    def test_06_invalid_TRUE_original_anchors_source_C4_duplicate_images_failclosed(self):
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        for cap in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                original_two_external_A_anchor_certificate(
                    model,anchor_pairs=(),max_C4_pairs=cap)
        with self.assertRaises(ValueError):
            original_two_external_A_anchor_certificate(model,anchor_pairs=None)
        for triple in ((1,1,2),(1,2),(True,1,2),(V,1,2)):
            with self.assertRaises(ValueError):
                original_two_external_A_completion_catalogue(f,0,10,triple)
        forged=list(f);forged[0]=forged[1]
        with self.assertRaises(ValueError):
            original_two_external_A_completion_catalogue(forged,0,10,(1,2,3))
        bad=dict(model);bad["left_labels"]=tuple(forged)
        with self.assertRaises(ValueError):
            original_two_external_A_anchor_certificate(bad,anchor_pairs=())
        with self.assertRaises(ValueError):
            original_two_external_A_anchor_certificate(model,anchor_pairs=((0,0),))


if __name__=="__main__":unittest.main()
