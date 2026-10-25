"""Genuine W3 original source Hall-vacancy 4-type dual invariant tests."""
from collections import Counter
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_dual_model_immutable_source_Q,
    original_nonincident_threepath,
    original_BBo_exact_three_matching_transfer,
)
from hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit import (
    exact_original_C4_marked_cofactor_energy,
)
from hyp105_issue230_d6aa4dd_dual_hall_vacancy import (
    DENOMINATOR,SOURCE_VACANCY_CLASSES,
    original_marked_true_source_vacancy_certificate,
    allh_original_vacancy_dichotomy_arithmetic,
    exact_original_C4_source_vacancy_energy,
)


def independent_two_by_two_residual_original_vacancies(B,i,j):
    """Independent source-matrix four-rank brute from actual adjacency."""
    rs=tuple(r for r in range(3) if r!=i)
    cs=tuple(c for c in range(3) if c!=j)
    count=sum(all(B[r][c] for r,c in zip(rs,p))
              for p in permutations(cs))
    vacancies=set()
    if count==0:
        for r in rs:
            if all(B[r][c]==0 for c in cs):
                vacancies.add("POINT_other_spoke" if r!=2 else "POINT_center")
        for c in cs:
            if all(B[r][c]==0 for r in rs):
                vacancies.add("LINE_other_spoke" if c!=2 else "LINE_center")
    return count,vacancies


def sample_original_cut_anchors(model,n,physical_halfcut=True):
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X,Y=(frozenset(range(k)),frozenset(range(a-k,a))) if physical_halfcut else (None,None)
    out=[]
    for p in range(V):
        if X is not None and not set(f[p])<=X:continue
        for l in range(V):
            if l in pl[p] or (Y is not None and not set(g[l])<=Y):continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            out.append((p,l))
            if len(out)>=n:return tuple(out)
    return tuple(out)


class AA4DDGenuineSourceDualHallVacancy(unittest.TestCase):
    def test_01_independent_all_512_original_GQ_girth_acyclic_source_matrices(self):
        valid=nonzero=deficient=multivacant=source_dual=0
        mass=Counter()
        for bits in range(1<<9):
            B=tuple(tuple((bits>>(3*i+j))&1 for j in range(3))
                    for i in range(3))
            if any(sum(B[i][j]*B[ii][j] for j in range(3))>=2
                   for i,ii in combinations(range(3),2)):
                continue
            if sum(all(B[i][p[i]] for i in range(3)) for p in permutations(range(3)))>1:
                continue
            valid+=1
            Bt=tuple(tuple(B[j][i] for j in range(3)) for i in range(3))
            for i in (0,1):
                for j in (0,1):
                    if not B[i][j]:continue
                    nonzero+=1
                    z=original_marked_true_source_vacancy_certificate(B,i,j)
                    c,expected=independent_two_by_two_residual_original_vacancies(B,i,j)
                    self.assertEqual(c,z["source_original_2x2_cofactor"])
                    self.assertEqual(expected,set(z["original_SOURCE_zero_row_or_column_witnesses"]))
                    self.assertEqual(sum(z["dual_symmetric_vacancy_credits_in_twelfths"].values()),
                                     DENOMINATOR*(c==0))
                    if c==0:
                        deficient+=1
                        multivacant+=len(expected)>1
                    w=original_marked_true_source_vacancy_certificate(Bt,j,i)
                    self.assertEqual(c,w["source_original_2x2_cofactor"])
                    for src,dst in (
                        ("POINT_other_spoke","LINE_other_spoke"),
                        ("POINT_center","LINE_center"),
                        ("LINE_other_spoke","POINT_other_spoke"),
                        ("LINE_center","POINT_center")
                    ):
                        self.assertEqual(
                            z["dual_symmetric_vacancy_credits_in_twelfths"][src],
                            w["dual_symmetric_vacancy_credits_in_twelfths"][dst])
                    source_dual+=1
                    for t,v in z["dual_symmetric_vacancy_credits_in_twelfths"].items():
                        mass[t]+=v
        self.assertEqual(valid,328)
        self.assertGreater(nonzero,0)
        self.assertGreater(deficient,0)
        self.assertGreater(multivacant,0)
        self.assertEqual(sum(mass.values()),12*deficient)
        print("AA4DD_ALL_512_BINARY_SOURCE_FORESTS","valid",valid,
              "original_marked",nonzero,"unextendible",deficient,
              "multi_vacancy",multivacant,"dual",source_dual,
              "weighted_Hall_classes",dict(mass),flush=True)

    def test_02_exact_h1_110_allh_true_original_BBo_or_four_vacancy(self):
        for h in range(1,111):
            z=allh_original_vacancy_dichotomy_arithmetic(h)
            s,V,a=z["s"],z["V"],z["a"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(z["source_fractional_Hall_vacancy_common_denominator"],12)
            self.assertEqual(z["source_vacancy_class_count"],4)
            if h>=96:
                self.assertTrue(z["allh_gate_h_ge_96"])
                self.assertEqual(z["either_historical_original_BBo_lower_denominator"],1<<17)
                self.assertEqual(z["or_ONE_true_original_vacancy_class_lower_denominator"],1<<18)
            else:self.assertFalse(z["allh_gate_h_ge_96"])
            self.assertTrue(z["does_NOT_resolve_root_230"])
            if h in (60,95,96,100,110):
                print("AA4DD_DYADIC_TRUE_ORIGINAL_HALL_VACANCY",h,
                      "U_BBo_or_true_original_typed_vacancy","UNRESOLVED",
                      "s7",s**7,flush=True)

    def test_03_W32_complete_original_point_LINE_dual_invariance_and_BBo(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            anchors=sample_original_cut_anchors(model,12,physical_halfcut=False)
            self.assertGreater(len(anchors),0)
            z=exact_original_C4_source_vacancy_energy(model,anchor_pairs=anchors)
            dual=original_dual_model_immutable_source_Q(model)
            w=exact_original_C4_source_vacancy_energy(dual,
                anchor_pairs=tuple((l,p) for p,l in anchors))
            self.assertEqual(z["actual_original_marked_spoke_incidence_T"],
                             w["actual_original_marked_spoke_incidence_T"])
            self.assertEqual(z["actual_original_unextendible_source_cofactor_D"],
                             w["actual_original_unextendible_source_cofactor_D"])
            self.assertEqual(z["actual_historical_original_BBo_sixflag_U"],
                             w["actual_historical_original_BBo_sixflag_U"])
            self.assertEqual(z["actual_original_extendible_marked_E"],
                             w["actual_original_extendible_marked_E"])
            a=z["source_Hall_fractional_vacancy_credits_in_twelfths"]
            b=w["source_Hall_fractional_vacancy_credits_in_twelfths"]
            self.assertEqual(a["POINT_other_spoke"],b["LINE_other_spoke"])
            self.assertEqual(a["POINT_center"],b["LINE_center"])
            self.assertEqual(a["LINE_other_spoke"],b["POINT_other_spoke"])
            self.assertEqual(a["LINE_center"],b["POINT_center"])
            canonical=original_BBo_exact_three_matching_transfer(
                model,anchor_pairs=anchors,collect_original_Q=False)
            self.assertEqual(z["actual_historical_original_BBo_sixflag_U"],
                             canonical["historical_accepted_original_BBo_sixflag_Q"])
            self.assertEqual(sum(a.values()),12*z["actual_original_unextendible_source_cofactor_D"])
            print("AA4DD_GENUINE_W32_DUAL",scheme,"anchors",len(anchors),
                  "marked_T",z["actual_original_marked_spoke_incidence_T"],
                  "defect_D",z["actual_original_unextendible_source_cofactor_D"],
                  "BBo_U",z["actual_historical_original_BBo_sixflag_U"],
                  "class_credits_12",a,flush=True)

    def test_04_W34_actual_original_full_C4_permutation_and_fractional_Hall(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            anchors=sample_original_cut_anchors(model,8,physical_halfcut=True)
            self.assertEqual(len(anchors),8)
            X,Y=tuple(range(a//2)),tuple(range(a-a//2,a))
            z=exact_original_C4_source_vacancy_energy(
                model,anchor_pairs=anchors,point_cut=X,line_cut=Y)
            dc=exact_original_C4_marked_cofactor_energy(
                model,anchor_pairs=anchors,point_cut=X,line_cut=Y)
            self.assertFalse(z["quantities_are_partial_if_capped"])
            for left,right in (
                ("actual_original_marked_spoke_incidence_T","source_occupied_C4_source_cross_flag_mark_mass_T"),
                ("actual_original_extendible_marked_E","source_2x2_cofactor_extendible_flag_mass_E"),
                ("actual_original_unextendible_source_cofactor_D","source_Hall_defective_C4_spoke_flag_mass_D"),
                ("actual_historical_original_BBo_sixflag_U","source_original_3x3_perfect_matching_BBo_U"),
                ("actual_occupied_source_C4_pairs","C4_pairs_examined")
            ):
                self.assertEqual(z[left],dc[right])
            credits=z["source_Hall_fractional_vacancy_credits_in_twelfths"]
            self.assertEqual(sum(credits.values()),12*z["actual_original_unextendible_source_cofactor_D"])
            for t in SOURCE_VACANCY_CLASSES:
                self.assertGreater(credits[t],0)
                self.assertIn(t,z["first_true_original_vacancy_witness_by_type"])
            print("AA4DD_GENUINE_W34_ORIGINAL_HALL_CLASSES",scheme,
                  "anchors",len(anchors),"T",z["actual_original_marked_spoke_incidence_T"],
                  "D",z["actual_original_unextendible_source_cofactor_D"],
                  "U",z["actual_historical_original_BBo_sixflag_U"],
                  "classes_in_12ths",credits,flush=True)

    def test_05_W38_explicitly_partial_original_four_anchor_C4_census(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            anchors=sample_original_cut_anchors(model,4,physical_halfcut=False)
            self.assertEqual(len(anchors),4)
            z=exact_original_C4_source_vacancy_energy(
                model,anchor_pairs=anchors,max_triples_per_side=8)
            dc=exact_original_C4_marked_cofactor_energy(
                model,anchor_pairs=anchors,max_triples_per_side=8)
            self.assertTrue(z["quantities_are_partial_if_capped"])
            self.assertEqual(z["actual_occupied_source_C4_pairs"],256)
            self.assertEqual(z["actual_original_marked_spoke_incidence_T"],
                             dc["source_occupied_C4_source_cross_flag_mark_mass_T"])
            self.assertEqual(z["actual_original_unextendible_source_cofactor_D"],
                             dc["source_Hall_defective_C4_spoke_flag_mass_D"])
            self.assertEqual(sum(z["source_Hall_fractional_vacancy_credits_in_twelfths"].values()),
                             12*z["actual_original_unextendible_source_cofactor_D"])
            print("AA4DD_TRUE_W38_PARTIAL_HALL",scheme,
                  "C4pair_count",z["actual_occupied_source_C4_pairs"],
                  "T",z["actual_original_marked_spoke_incidence_T"],
                  "D",z["actual_original_unextendible_source_cofactor_D"],
                  "types",z["source_Hall_fractional_vacancy_credits_in_twelfths"],flush=True)

    def test_06_original_input_and_source_matrix_forgery_failclosed(self):
        badmatrices=(((1,0),(0,0)),((1,0,0),(0,1,0),(0,0,2)),
                     ((True,0,0),(0,0,0),(0,0,0)),
                     ((1,1,0),(1,1,0),(0,0,0)))
        for B in badmatrices:
            with self.assertRaises(ValueError):
                original_marked_true_source_vacancy_certificate(B,0,0)
        for ij in ((2,0),(0,2),(-1,1),(True,0),(0,False)):
            with self.assertRaises(ValueError):
                original_marked_true_source_vacancy_certificate(
                    ((1,0,0),(0,1,0),(0,0,1)),*ij)
        with self.assertRaises(ValueError):
            original_marked_true_source_vacancy_certificate(
                ((0,0,0),(0,1,0),(0,0,1)),0,0)
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            exact_original_C4_source_vacancy_energy(model,anchor_pairs=None)
        for val in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                exact_original_C4_source_vacancy_energy(model,anchor_pairs=(),
                                                         max_triples_per_side=val)
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1,2),(False,4,5))):
            with self.assertRaises(ValueError):
                exact_original_C4_source_vacancy_energy(
                    model,anchor_pairs=(),point_cut=X,line_cut=Y)
        broken=dict(model)
        f=list(model["left_labels"]);f[1]=f[0];broken["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            exact_original_C4_source_vacancy_energy(broken,anchor_pairs=())


if __name__=="__main__":
    unittest.main()
