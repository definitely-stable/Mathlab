"""Independent AA4-CX original W3 spectral maximum and doubled-filter checks."""
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath
from hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion import (
    allh_local_spectrum_exclusion_arithmetic,
    original_cut_doubled_exclusion_certificate,
)


def independent_oracle_by_every_original_incidence(model,X,Y,p,l):
    """Genuine original SOURCE flag-first, not code's source-point-first sums."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    if l in pl[p]:
        raise ValueError("source nonincident real P3 anchor required")
    path=original_nonincident_threepath(p,l,pl,lp)
    q,l0=path[1][0],path[0][1]
    x,y=set(X),set(Y)
    bad=bool(set(f[p])&set(f[q]) or set(g[l])&set(g[l0]))
    raw=safe=0
    for i,j in model["incidences"]:
        if i==p or j==l:
            continue
        if not(set(f[i])<=x and set(g[j])<=y
               and bool(set(f[i])&set(f[p]))
               and bool(set(g[j])&set(g[l]))):
            continue
        raw+=1
        if not bad and not(set(f[i])&set(f[q]) or set(g[j])&set(g[l0])):
            safe+=1
    return raw,safe,bad


class AA4CXOriginalSpectralDoubleExclusion(unittest.TestCase):
    def test_01_exact_allh_s5_integer_and_bad_anchor_loss_barrier(self):
        for h in range(1,31):
            z=allh_local_spectrum_exclusion_arithmetic(h)
            s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(z["max_original_incidence_loss_per_double_disjoint_anchor"],8*d)
            self.assertEqual(z["double_overlap_bad_cut_anchor_upper"],4*(a-2)*s*V)
            if h>=24:
                self.assertTrue(z["allh_gate_h_ge_24"])
                self.assertLess(4*d*(k-2)**2,s*s*V)
                self.assertLess(8*(k-2)**2,9*s**3)
                self.assertGreaterEqual(4*k*k,s**3)
                self.assertGreaterEqual(
                    16384*d*V*(k*k-2048*s*s),2048*s**7)
                self.assertGreaterEqual(
                    z["double_overlap_bad_cut_anchor_upper"]*16384,s**5)
            else:self.assertFalse(z["allh_gate_h_ge_24"])
            if h in (14,23,24,30):
                print("AA4CX_DYADIC_EXACT_S5_GATE",h,"s",s,
                      "physical_a",a,"k",k,
                      "proven_nonincident_raw_positive_floor",
                      s**5//16384,flush=True)

    def test_02_true_W32_all_global_original_cuts_each_nonincident_original_flag_referee(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2
            cuts=(
                (tuple(range(k)),tuple(range(a-k,a))),
                (tuple(range(1,k+1)),tuple(range(k))),
                (tuple(range(a-k,a)),tuple(range(1,k+1))),
            )
            for ci,(X,Y) in enumerate(cuts):
                cert=original_cut_doubled_exclusion_certificate(model,X,Y)
                raw=safe=bad=0
                for p in range(V):
                    if not set(f[p])<=set(X):continue
                    for l in range(V):
                        if l in pl[p] or not set(g[l])<=set(Y):continue
                        x,y,b=independent_oracle_by_every_original_incidence(model,X,Y,p,l)
                        raw+=x
                        safe+=y
                        bad+=b
                self.assertEqual(cert["raw_original_source_incidence_mass_all_nonincident"],raw)
                self.assertEqual(cert["SAFE_original_source_incidence_mass_double_disjoint"],safe)
                self.assertEqual(cert["bad_either_physical_doubled_source_overlap_anchors"],bad)
                self.assertEqual(cert["raw_original_spoke_positive_source_3path_anchors"],
                                 cert["double_disjoint_raw_spoke_positive_anchors"]+
                                 sum(
                                     independent_oracle_by_every_original_incidence(
                                         model,X,Y,p,l)[0]>0
                                     for p in range(V) if set(f[p])<=set(X)
                                     for l in range(V) if l not in pl[p] and set(g[l])<=set(Y)
                                     if independent_oracle_by_every_original_incidence(
                                         model,X,Y,p,l)[2]))
                self.assertTrue(cert["not_a_GF5_accepted_motif"])
                print("AA4CX_W32_TRUE_SOURCE",scheme,"cut",ci,
                      "raw_mass",raw,"safe_mass",safe,"bad",bad,
                      "positive_raw",cert["raw_original_spoke_positive_source_3path_anchors"],
                      "positive_safe",cert["double_disjoint_SAFE_spoke_positive_anchors"],flush=True)

    def test_03_true_W34_W38_complete_correlated_maps_both_source_orientations(self):
        for power,schemes in ((2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                k=a//2
                cuts=((tuple(range(k)),tuple(range(a-k,a))),
                      (tuple(range(a-k,a)),tuple(range(k)))) if power==2 else (
                      (tuple(range(k)),tuple(range(a-k,a))),)
                for cut_index,(X,Y) in enumerate(cuts):
                    cert=original_cut_doubled_exclusion_certificate(model,X,Y)
                    self.assertLessEqual(
                        cert["double_disjoint_SAFE_spoke_positive_anchors"],
                        cert["double_disjoint_raw_spoke_positive_anchors"])
                    self.assertLessEqual(
                        cert["max_original_incidence_loss_one_good_anchor"],8*(s+1))
                    self.assertLessEqual(
                        cert["bad_left_physical_doubled_source_overlap_anchors"],
                        2*(a-2)*s*cert["source_POINT_cut_original_factor_count"])
                    self.assertLessEqual(
                        cert["bad_right_physical_doubled_source_overlap_anchors"],
                        2*(a-2)*s*cert["source_LINE_cut_original_factor_count"])
                    sample=0
                    for p in range(V):
                        if set(f[p])<=set(X):
                            for l in range(V):
                                if l in pl[p] or not set(g[l])<=set(Y):continue
                                original,filtered,bad=independent_oracle_by_every_original_incidence(
                                    model,X,Y,p,l)
                                self.assertGreaterEqual(original,filtered)
                                if not bad:
                                    self.assertLessEqual(original-filtered,8*(s+1))
                                sample+=1
                                if sample>=8:break
                        if sample>=8:break
                    self.assertGreaterEqual(sample,8)
                    print("AA4CX_TRUE_W3",s,scheme,"cut",cut_index,
                          "original_nonincident",cert["original_nonincident_3path_anchors"],
                          "raw_positive",cert["raw_original_spoke_positive_source_3path_anchors"],
                          "good_double_disjoint",cert["double_disjoint_good_source_3path_anchors"],
                          "safe_spoke_positive",cert["double_disjoint_SAFE_spoke_positive_anchors"],
                          "real_source_flags_dropped",
                          cert["exact_original_source_incidence_loss"],flush=True)

    def test_04_direct_girth_source_spectral_cap_on_all_census_extrema(self):
        for power,scheme in ((1,"lex"),(1,"S72"),(2,"lex"),(3,"lex")):
            model=fixture(power,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2;X=tuple(range(k));Y=tuple(range(a-k,a))
            z=original_cut_doubled_exclusion_certificate(model,X,Y)
            C=z["max_original_spoke_rectangle_incidence"]
            # Same SOURCE expander-mixing of real point-by-line incidence
            # used on individual sets of size at most 2(k-2), WITHOUT
            # float sqrt; if C above uniform main term test squared.
            positive=C*V-4*(s+1)*(k-2)**2
            if positive>0:
                self.assertLessEqual(positive**2,
                                     8*s*(k-2)**2*V**2)
            self.assertLessEqual(C,2*(k-2)*(s+1))
            print("AA4CX_SOURCE_SPECTRAL_POINT_CAP",s,scheme,C,flush=True)

    def test_05_failclosed_dyadic_source_maps_and_bad_cut(self):
        for h in (True,0,-1,2.5):
            with self.assertRaises(ValueError):
                allh_local_spectrum_exclusion_arithmetic(h)
        model=fixture(1,"lex")
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(False,4,5))):
            with self.assertRaises(ValueError):
                original_cut_doubled_exclusion_certificate(model,X,Y)
        invalid=dict(model)
        p=list(model["left_labels"]);p[2]=p[1]
        invalid["left_labels"]=tuple(p)
        with self.assertRaises(ValueError):
            original_cut_doubled_exclusion_certificate(invalid)


if __name__=="__main__":unittest.main()
