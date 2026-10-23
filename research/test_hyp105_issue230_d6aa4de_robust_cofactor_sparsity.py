"""Independent AA4-DE genuine-original light-Hall cofactor loss NO-GO tests."""
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,c4_completions_from_single_and_doubled,
)
from hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit import (
    exact_original_C4_marked_cofactor_energy,
)
from hyp105_issue230_d6aa4de_robust_cofactor_sparsity import (
    allh_original_robust_defect_arithmetic,
    _original_heavy_pair_sources,
    original_light_crossflag_robust_defect_certificate,
)


def original_selected_anchors(model,n,halfcut=False):
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X,Y=(set(range(k)),set(range(a-k,a))) if halfcut else (None,None)
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


def independent_genuine_original_SOURCE_light_c4_marks(model,anchors,X=None,Y=None,cap=None):
    """Independent BBo canonical C4-pair-first source incidence cofactor oracle.

    Unlike main source module, loops ALL actual canonical source C4
    triple pairs first, then scans TRUE ORIGINAL spoke-spoke source
    flags, no per-mark pre-index, no claimed GF5 compensation.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    pbad=_original_heavy_pair_sources(f,a)["bad_original_source_factor_ids"]
    lbad=_original_heavy_pair_sources(g,a)["bad_original_source_factor_ids"]
    invp={tuple(sorted(e)):i for i,e in enumerate(f)}
    invl={tuple(sorted(e)):j for j,e in enumerate(g)}
    X=None if X is None else set(X);Y=None if Y is None else set(Y)
    T=E=D=0
    successes=0
    positive_candidates=set()
    max_per_fixed=0
    for p,l in anchors:
        path=original_nonincident_threepath(p,l,pl,lp)
        q,l0=path[1][0],path[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
        if p in pbad or l in lbad:continue
        ps=c4_completions_from_single_and_doubled(f[p],f[q],invp,a)
        ls=c4_completions_from_single_and_doubled(g[l],g[l0],invl,a)
        if cap is not None:ps=ps[:cap];ls=ls[:cap]
        for px in ps:
            pspokes=[v for v in px if len(set(f[v])&set(f[p]))==1]
            centerp=next(v for v in px if v not in pspokes)
            for lx in ls:
                lspokes=[v for v in lx if len(set(g[v])&set(g[l]))==1]
                centerl=next(v for v in lx if v not in lspokes)
                for i in pspokes:
                    if i in pbad or X is not None and not set(f[i])<=X:continue
                    otherp=next(v for v in pspokes if v!=i)
                    for j in lspokes:
                        if j in lbad or Y is not None and not set(g[j])<=Y or j not in pl[i]:
                            continue
                        otherl=next(v for v in lspokes if v!=j)
                        positive_candidates.add((p,l,i,j))
                        T+=1
                        rows=(otherp,centerp);cols=(otherl,centerl)
                        c=sum(all(ol in pl[ip] for ip,ol in zip(rows,order))
                              for order in permutations(cols))
                        self_girth=c<=1
                        if not self_girth:raise AssertionError("genuine original 2x2 source violates GQ girth8")
                        E+=c;D+=1-c
                        successes+=c
    return {"T":T,"E":E,"D":D,"source_crossflags":len(positive_candidates)}


class AA4DEOriginalLightHallNoGo(unittest.TestCase):
    def test_01_exact_allh_h1_110_universal_s10_lower_and_not_original_GF5(self):
        for h in range(1,111):
            z=allh_original_robust_defect_arithmetic(h)
            s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(z["missing_original_physical_pair_images_H"],comb(a,2)-V)
            self.assertEqual(z["max_true_original_SAFE_crossflag_light_filter_loss"],256*(a-1)*k*k*d)
            self.assertEqual(z["max_heavy_coordinates_per_original_typed_map"],16)
            if h>=96:
                self.assertTrue(z["allh_gate_h_ge_96"])
                self.assertLessEqual(32768*256*(a-1)*k*k*d,s**7)
                self.assertGreaterEqual((a-5)**2,s**3)
                self.assertGreaterEqual(4*z["least_occupied_C4_completions_per_original_LIGHT_marked_spoke"]**2,s**3)
                self.assertGreaterEqual(z["least_occupied_C4_completions_per_original_LIGHT_marked_spoke"],4*d)
                self.assertEqual(z["original_LIGHT_C4_pair_unextendible_cofactor_defect_floor_denominator"],1<<18)
            else:self.assertFalse(z["allh_gate_h_ge_96"])
            self.assertTrue(z["NO_proven_other_GF5_class_compensation"])
            if h in (24,60,95,96,100,110):
                print("AA4DE_EXACT_GENUINE_W3_BIGINT_NO_GO",h,"s",s,
                      "a",a,"min_C4_per_light_spoke",
                      z["least_occupied_C4_completions_per_original_LIGHT_marked_spoke"],
                      "guaranteed_D_completion_multiplicity",
                      z["original_LIGHT_C4_pair_unextendible_cofactor_defect_floor_numerator"]//(1<<18),flush=True)

    def test_02_original_W32_TRUE_SOURCE_dual_lex_S72_full_immutable_c4_cofactor_referee(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,*_=_validated_original(model)
            anchors=original_selected_anchors(model,12)
            self.assertGreaterEqual(len(anchors),4)
            z=original_light_crossflag_robust_defect_certificate(model,anchor_pairs=anchors)
            ref=independent_genuine_original_SOURCE_light_c4_marks(model,anchors)
            self.assertEqual(z["light_original_occupied_C4_pair_mark_mass_T"],ref["T"])
            self.assertEqual(z["light_original_2x2_cofactor_extendible_mark_mass_E"],ref["E"])
            self.assertEqual(z["light_original_2x2_cofactor_Hall_defect_mark_mass_D"],ref["D"])
            self.assertEqual(z["light_original_anchor_crossflag_count"],ref["source_crossflags"])
            allc=exact_original_C4_marked_cofactor_energy(model,anchor_pairs=anchors)
            self.assertLessEqual(ref["D"],allc["source_Hall_defective_C4_spoke_flag_mass_D"])
            self.assertLessEqual(ref["E"],allc["source_2x2_cofactor_extendible_flag_mass_E"])
            self.assertEqual(sum(z["light_source_four_vacancy_Hall_credits_in_twelfths"].values()),12*ref["D"])
            print("AA4DE_TRUE_W32_INDEPENDENT_C4_MARKS",scheme,"anchors",len(anchors),
                  "light_T",ref["T"],"light_E",ref["E"],"light_D",ref["D"],
                  "all_D",allc["source_Hall_defective_C4_spoke_flag_mass_D"],flush=True)

    def test_03_original_W34_lex_random_FULL_true_original_C4_source_cofactor_counts(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2;X,Y=tuple(range(k)),tuple(range(a-k,a))
            anchors=original_selected_anchors(model,8,halfcut=True)
            self.assertEqual(len(anchors),8)
            z=original_light_crossflag_robust_defect_certificate(
                model,anchor_pairs=anchors,point_cut=X,line_cut=Y)
            ref=independent_genuine_original_SOURCE_light_c4_marks(
                model,anchors,X=X,Y=Y)
            for key,value in (
                ("light_original_occupied_C4_pair_mark_mass_T","T"),
                ("light_original_2x2_cofactor_extendible_mark_mass_E","E"),
                ("light_original_2x2_cofactor_Hall_defect_mark_mass_D","D"),
                ("light_original_anchor_crossflag_count","source_crossflags")
            ):
                self.assertEqual(z[key],ref[value])
            self.assertEqual(ref["T"],ref["E"]+ref["D"])
            full=exact_original_C4_marked_cofactor_energy(
                model,anchor_pairs=anchors,point_cut=X,line_cut=Y)
            self.assertLessEqual(ref["T"],full["source_occupied_C4_source_cross_flag_mark_mass_T"])
            self.assertLessEqual(ref["D"],full["source_Hall_defective_C4_spoke_flag_mass_D"])
            if ref["T"]:
                self.assertLessEqual(
                    z["max_actual_original_line_ext_per_one_POINT_C4"],2*(s+1))
            print("AA4DE_TRUE_W34_COMPLETE_MAPS",scheme,"light_T",ref["T"],
                  "light_D",ref["D"],"light_E",ref["E"],
                  "full_D",full["source_Hall_defective_C4_spoke_flag_mass_D"],
                  "light_line_C4_min",z["actual_min_LINE_C4_completions_per_light_original_spoke"],flush=True)

    def test_04_real_W38_explicitly_PARTIAL_original_anchors_eight_C4_lanes(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            anchors=original_selected_anchors(model,4)
            self.assertEqual(len(anchors),4)
            z=original_light_crossflag_robust_defect_certificate(
                model,anchor_pairs=anchors,max_triples_per_side=8)
            ref=independent_genuine_original_SOURCE_light_c4_marks(
                model,anchors,cap=8)
            self.assertTrue(z["is_explicitly_PARTIAL_if_capped"])
            self.assertEqual(z["light_original_occupied_C4_pair_mark_mass_T"],ref["T"])
            self.assertEqual(z["light_original_2x2_cofactor_extendible_mark_mass_E"],ref["E"])
            self.assertEqual(z["light_original_2x2_cofactor_Hall_defect_mark_mass_D"],ref["D"])
            print("AA4DE_REAL_ORIGINAL_W38_SAMPLED_NOT_A_GLOBAL_THEOREM",
                  scheme,ref,flush=True)

    def test_05_original_physical_hole_stars_are_genuine_source_factor_images(self):
        for power,schemes in ((1,("lex","S72")),(2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                for labels in (f,g):
                    data=_original_heavy_pair_sources(labels,a)
                    missing=[sum(tuple(sorted((u,v))) not in set(labels) for v in range(a) if v!=u)
                             for u in range(a)]
                    self.assertEqual(data["physical_missing_degree"],tuple(missing))
                    self.assertLessEqual(len(data["heavy_physical_coordinates"]),16)
                    self.assertLessEqual(len(data["bad_original_source_factor_ids"]),16*(a-1))
                print("AA4DE_FULL_TRUE_ORIGINAL_HOLE_STARS",s,scheme,
                      "a",a,flush=True)

    def test_06_bad_source_typed_maps_anchors_cuts_caps_failclosed(self):
        for h in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                allh_original_robust_defect_arithmetic(h)
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            original_light_crossflag_robust_defect_certificate(model,anchor_pairs=None)
        for val in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                original_light_crossflag_robust_defect_certificate(
                    model,anchor_pairs=(),max_triples_per_side=val)
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1,2),(False,4,5))):
            with self.assertRaises(ValueError):
                original_light_crossflag_robust_defect_certificate(
                    model,anchor_pairs=(),point_cut=X,line_cut=Y)
        bad=dict(model);f=list(model["left_labels"]);f[0]=f[1]
        bad["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            original_light_crossflag_robust_defect_certificate(bad,anchor_pairs=())


if __name__=="__main__":
    unittest.main()
