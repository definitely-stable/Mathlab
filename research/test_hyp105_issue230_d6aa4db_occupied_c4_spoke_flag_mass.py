"""Independent actual ORIGINAL W(3,s) C4 extension and sixflag nonimplications."""
from itertools import combinations
from math import comb,isqrt
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
    c4_completions_from_single_and_doubled,
)
from hyp105_issue230_d6aa4db_occupied_c4_spoke_flag_mass import (
    allh_original_occupied_c4_arithmetic,
    _physical_pair_holes_and_heavy,
    occupied_C4_completion_containing_original_SAFE_spoke,
    original_cut_occupied_c4_source_flag_certificate,
)


def independent_full_true_original_3path_original_flag_first_C4(model,X,Y,limit=None):
    """Different original ORIGINAL flag-first/canonical C4 triple referee.

    For each actual genuine source path, enumerate fully occupied
    physical C4 triple sets using the AA4-CR independent standard
    conversion, and ALL immutable original source incidences one by one.
    The source module's bespoke w-extension code is NOT reused.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    X,Y=set(X),set(Y)
    i_f={tuple(sorted(edge)):i for i,edge in enumerate(f)}
    i_g={tuple(sorted(edge)):i for i,edge in enumerate(g)}
    P=tuple(p for p in range(V) if set(f[p])<=X)
    L=tuple(l for l in range(V) if set(g[l])<=Y)
    flags=tuple(model["incidences"])
    safe=occupied=loss=positive=0
    checked=0
    for p in P:
        for l in L:
            if l in pl[p]:continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            checked+=1
            fp=c4_completions_from_single_and_doubled(f[p],f[q],i_f,a)
            gp=c4_completions_from_single_and_doubled(g[l],g[l0],i_g,a)
            # A source factor is one of two outer physical spokes of an
            # actual occupied 4cycle completion; physical center factor
            # alone does NOT qualify as a spoke.
            def eligible_spokes(completions,images,base):
                e=set(base)
                out=set()
                for triple in completions:
                    for i in triple:
                        out.update([i] if len(set(images[i])&e)==1 else [])
                return out
            fp_ids=eligible_spokes(fp,f,f[p])
            gp_ids=eligible_spokes(gp,g,g[l])
            x=y=0
            for i,j in flags:
                if i==p or j==l or not (
                    set(f[i])<=X and set(g[j])<=Y and
                    set(f[i])&set(f[p]) and set(g[j])&set(g[l]) and
                    not set(f[i])&set(f[q]) and not set(g[j])&set(g[l0])
                ):
                    continue
                x+=1
                if i in fp_ids and j in gp_ids:
                    y+=1
            safe+=x;occupied+=y;loss+=x-y;positive+=y>0
            if limit is not None and checked>=limit:
                return {"safe":safe,"occupied":occupied,"loss":loss,
                        "positive":positive,"checked":checked}
    return {"safe":safe,"occupied":occupied,"loss":loss,
            "positive":positive,"checked":checked}


class AA4DBTrueOriginalOccupiedC4(unittest.TestCase):
    def test_01_exact_dyadic_1_110_heavy_hole_and_occupied_C4_allh_bounds(self):
        for h in range(1,111):
            z=allh_original_occupied_c4_arithmetic(h)
            s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(z["H"],comb(a,2)-V)
            self.assertLessEqual(z["H"],a-2)
            self.assertEqual(
                z["raw_safe_to_both_occupied_C4_original_flag_mass_loss_upper"],
                128*(a-1)*k*k*d)
            if h>=96:
                self.assertTrue(z["allh_gate_h_ge_96"])
                self.assertLessEqual(4*z["H"],8*(a-5))
                self.assertLessEqual(32768*128*(a-1)*k*k*d,s**7)
                self.assertGreaterEqual(4*k*k,s**3)
                self.assertGreater(z["allh_both_occupied_c4_true_original_positive_P3_floor"],0)
            else:self.assertFalse(z["allh_gate_h_ge_96"])
            if h in (24,60,95,96,99,110):
                print("AA4DB_ORIGINAL_DYADIC_C4_GATE",h,
                      "s",s,"physical_holes",z["H"],
                      "full_original_factor_a",a,"physical_k",k,
                      "strong_true_original_nonincident_mass_threshold",
                      z["allh_both_occupied_c4_original_flag_mass_lower_numerator"]//(1<<15),
                      flush=True)

    def test_02_genuine_W32_original_complete_map_three_cuts_all_FLAGS_and_C4_triples(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,*_=_validated_original(model);k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))),
                  (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))))
            for ci,(X,Y) in enumerate(cuts):
                z=original_cut_occupied_c4_source_flag_certificate(model,X,Y)
                indep=independent_full_true_original_3path_original_flag_first_C4(model,X,Y)
                self.assertEqual(z["safe_actual_original_source_incidence_mass"],indep["safe"])
                self.assertEqual(z["both_occupied_physical_C4_TRUE_original_cross_source_flag_mass"],
                                 indep["occupied"])
                self.assertEqual(z["SAFE_to_occupied_C4_original_flag_mass_loss"],indep["loss"])
                self.assertEqual(z["original_both_occupied_C4_positive_nonincident_P3"],indep["positive"])
                self.assertEqual(z["real_original_nonincident_double_disjoint_3path_anchors"],indep["checked"])
                print("AA4DB_W32_INDEPENDENT_ORIGINAL_C4_FULL",scheme,ci,
                      indep,flush=True)

    def test_03_true_original_W34_independent_all_original_flags_all_C4_census(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,*_=_validated_original(model);k=a//2
            X,Y=tuple(range(k)),tuple(range(a-k,a))
            z=original_cut_occupied_c4_source_flag_certificate(model,X,Y)
            ind=independent_full_true_original_3path_original_flag_first_C4(model,X,Y)
            self.assertEqual(z["safe_actual_original_source_incidence_mass"],ind["safe"])
            self.assertEqual(z["both_occupied_physical_C4_TRUE_original_cross_source_flag_mass"],ind["occupied"])
            self.assertEqual(z["original_both_occupied_C4_positive_nonincident_P3"],ind["positive"])
            self.assertLessEqual(
                z["SAFE_to_occupied_C4_original_flag_mass_loss"],
                z["allh_original_SAFE_to_both_occupied_C4_loss_upper"])
            print("AA4DB_W34_INDEPENDENT_ORIGINAL_C4",scheme,
                  "safe",ind["safe"],"occupied",ind["occupied"],
                  "positive_source_anchors",ind["positive"],flush=True)

    def test_04_genuine_W38_occupied_C4_source_masses_and_direct_witness(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model);k=a//2
            X,Y=tuple(range(k)),tuple(range(a-k,a))
            z=original_cut_occupied_c4_source_flag_certificate(model,X,Y)
            self.assertLessEqual(
                z["SAFE_to_occupied_C4_original_flag_mass_loss"],
                z["allh_original_SAFE_to_both_occupied_C4_loss_upper"])
            w=z["first_real_original_cross_FLAG_with_both_occupied_C4_triplets"]
            if w:
                p,l,i,j,fp,gp=w
                self.assertIn(j,pl[i])
                self.assertEqual(len(set(fp)),3)
                self.assertEqual(len(set(gp)),3)
                path=original_nonincident_threepath(p,l,pl,lp)
                q,l0=path[1][0],path[0][1]
                point_inv={tuple(sorted(edge)):r for r,edge in enumerate(f)}
                line_inv={tuple(sorted(edge)):r for r,edge in enumerate(g)}
                self.assertIn(tuple(sorted(fp)),
                    c4_completions_from_single_and_doubled(f[p],f[q],point_inv,a))
                self.assertIn(tuple(sorted(gp)),
                    c4_completions_from_single_and_doubled(g[l],g[l0],line_inv,a))
            self.assertTrue(z["these_are_NOT_original_3x3_matching_flags"])
            print("AA4DB_W38_GENUINE_GQ_OCCUPIED_BOTH_C4",scheme,
                  "source_safe",z["safe_actual_original_source_incidence_mass"],
                  "with_two_occupied_C4",z["both_occupied_physical_C4_TRUE_original_cross_source_flag_mass"],
                  "lost",z["SAFE_to_occupied_C4_original_flag_mass_loss"],
                  "source_anchors",z["original_both_occupied_C4_positive_nonincident_P3"],
                  flush=True)

    def test_05_real_original_heavy_holes_and_local_extension_necessary_condition(self):
        for power,scheme in ((1,"lex"),(1,"S72"),(2,"lex"),(3,"lex")):
            model=fixture(power,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            for labels in (f,g):
                m=_physical_pair_holes_and_heavy(labels,a)
                self.assertEqual(m["H"],comb(a,2)-V)
                self.assertLessEqual(len(m["heavy_physical_coordinates"]),8)
                self.assertLessEqual(len(m["bad_original_source_factor_ids"]),8*(a-1))
                occupied=m["occupied"];deg=m["holes_by_coordinate"]
                inverse={tuple(sorted(edge)):i for i,edge in enumerate(labels)}
                count=0
                for i in range(min(V,120)):
                    for j in range(min(V,120)):
                        if i==j or set(labels[i])&set(labels[j]):continue
                        base=labels[i];double=labels[j]
                        for source_id in range(min(V,120)):
                            spoke=labels[source_id]
                            if not(set(spoke)&set(base)) or set(spoke)&set(double):
                                continue
                            w=occupied_C4_completion_containing_original_SAFE_spoke(
                                base,double,spoke,inverse,a)
                            if not w:
                                shared=set(spoke)&set(base)
                                u=next(iter(shared));v=next(iter(set(base)-{u}))
                                z=next(iter(set(spoke)-{u}))
                                self.assertGreaterEqual(deg[v]+deg[z],a-5)
                                self.assertTrue(v in m["heavy_physical_coordinates"] or
                                                z in m["heavy_physical_coordinates"])
                            count+=1
                            if count>=100:break
                        if count>=100:break
                    if count>=100:break
                print("AA4DB_ORIGINAL_HOLES_EXTENSION_FALSIFIER",s,scheme,
                      "heavy",len(m["heavy_physical_coordinates"]),
                      "tested_safe_spokes",count,flush=True)

    def test_06_failclosed_malformed_original_source_map_and_cuts(self):
        for h in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                allh_original_occupied_c4_arithmetic(h)
        model=fixture(1,"lex")
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(3,4,True))):
            with self.assertRaises(ValueError):
                original_cut_occupied_c4_source_flag_certificate(model,X,Y)
        broken=dict(model)
        f=list(model["left_labels"]);f[1]=f[0]
        broken["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            original_cut_occupied_c4_source_flag_certificate(broken)


if __name__=="__main__":
    unittest.main()
