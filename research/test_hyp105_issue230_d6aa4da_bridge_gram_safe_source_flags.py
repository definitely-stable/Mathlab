"""AA4-DA independently falsifies genuine original GQ BRIDGE-GRAM vs SAFE loss."""
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath
from hyp105_issue230_d6aa4da_bridge_gram_safe_source_flags import (
    allh_original_bridge_gram_safe_arithmetic,
    original_cut_bridge_gram_certificate,
)


def direct_original_source_safe_flag_census(model,X,Y):
    """Completely independent every TRUE ORIGINAL six-source path RAW/SAFE oracle."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    X,Y=set(X),set(Y)
    P=tuple(i for i in range(V) if set(f[i])<=X)
    L=tuple(j for j in range(V) if set(g[j])<=Y)
    immutable_flags=tuple(model["incidences"])
    raw=safe=loss=goodpositive=0
    for p in P:
        for l in L:
            if l in pl[p]:
                continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
                continue
            r=t=0
            for i,j in immutable_flags:
                if i==p or j==l or not(
                    set(f[i])<=X and set(g[j])<=Y and
                    set(f[i])&set(f[p]) and set(g[j])&set(g[l])
                ):
                    continue
                r+=1
                if not(set(f[i])&set(f[q]) or set(g[j])&set(g[l0])):
                    t+=1
            raw+=r;safe+=t;loss+=r-t;goodpositive+=t>0
    return {"raw":raw,"safe":safe,"loss":loss,"positive":goodpositive}


def direct_original_source_bridge_weight(model,X,Y,typed):
    """Different independent cube-iteration: original (p,q,i) flags via actual GQ.

    Enumerates ALL REAL original factor ids i (including unrelated source
    factors), does NOT rely on module's four physical-pair inverse candidates.
    For each source TRUE collinear ordered p,q and bridging physical i,
    directly enumerates actual opposite-typed original pencils and source
    physical K_a-edge adjacency, exactly K_g(q,i) or dual K_f(q,i).
    Restricted to genuine W32 and W34 in hosted tests for cost.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    if typed=="POINT":
        labels=f;source=pl;dual=lp;other=g;cut=set(Y)
    elif typed=="LINE":
        labels=g;source=lp;dual=pl;other=f;cut=set(X)
    else:raise ValueError("exact genuine typed POINT/LINE")
    total=triples=0
    for p in range(V):
        near=set()
        for z in source[p]:
            near.update(dual[z])
        near.discard(p)
        for q in near:
            if set(labels[p])&set(labels[q]):
                continue
            for i in range(V):
                if i==p or i==q or not(
                    set(labels[i])&set(labels[p]) and
                    set(labels[i])&set(labels[q])
                ):
                    continue
                triples+=1
                for l in source[q]:
                    if not set(other[l])<=cut:continue
                    for j in source[i]:
                        if j!=l and set(other[j])<=cut and set(other[l])&set(other[j]):
                            total+=1
    return {"triples":triples,"Gram":total}


class AA4DATrueOriginalBridgeGram(unittest.TestCase):
    def test_01_exact_allh_h1_110_analytic_SAFE_gates_and_finite_root_boundary(self):
        for h in range(1,111):
            x=allh_original_bridge_gram_safe_arithmetic(h)
            s,V,a,k,d=(x[z] for z in ("s","V","a","k","d"))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(x["typed_bridge_triplet_number_bound_exact"],4*V*s*d)
            self.assertEqual(x["typed_bridge_multiplicity_square_sum_upper"],4*V*s*d*(a-2))
            if h>=96:
                self.assertTrue(x["allh_gate_h_ge_96"])
                self.assertLessEqual((a-2)**2,4*s**3)
                self.assertGreaterEqual(4*k*k,s**3)
                self.assertLessEqual(4*V*s*d*(a-2),32*s**6*(s**(1/2) if False else __import__("math").isqrt(s)))
                self.assertGreaterEqual(s,(384*16384)**4)
                self.assertGreater(x["allh_SAFE_positive_nonincident_double_disjoint_P3_floor_integer"],0)
            else:self.assertFalse(x["allh_gate_h_ge_96"])
            if h in (60,80,95,96,98,110):
                print("AA4DA_ANALYTIC_GQ_SAFE_GATE",h,"s",s,"a",a,
                      "k",k,"lower_safe_mass",
                      x["allh_global_SAFE_original_flag_mass_lower_numerator"]//16384,
                      "positive_SAFE_source_P3_floor",
                      x["allh_SAFE_positive_nonincident_double_disjoint_P3_floor_integer"],
                      flush=True)

    def test_02_genuine_W32_every_original_nonincident_source_p3_and_immutable_crossflags(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))),
                  (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))))
            for ci,(X,Y) in enumerate(cuts):
                cert=original_cut_bridge_gram_certificate(model,X,Y)
                direct=direct_original_source_safe_flag_census(model,X,Y)
                self.assertEqual(cert["true_original_double_disjoint_RAW_incidence_mass"],direct["raw"])
                self.assertEqual(cert["true_original_double_disjoint_SAFE_incidence_mass"],direct["safe"])
                self.assertEqual(cert["exact_original_RAW_to_SAFE_flag_loss"],direct["loss"])
                self.assertEqual(cert["original_safe_positive_double_disjoint_nonincident_P3"],direct["positive"])
                self.assertGreaterEqual(cert["total_true_original_bridge_Gram_loss_majorant"],direct["loss"])
                print("AA4DA_TRUE_ORIGINAL_W32_SAFE",scheme,ci,
                      "raw",direct["raw"],"safe",direct["safe"],
                      "loss",direct["loss"],
                      "bridgeGram",
                      cert["total_true_original_bridge_Gram_loss_majorant"],flush=True)

    def test_03_all_original_W32_W34_full_cube_independent_bridge_gram_source_referee(self):
        for power,schemes in ((1,("lex","S72")),(2,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,*_=_validated_original(model)
                k=a//2
                X,Y=tuple(range(k)),tuple(range(a-k,a))
                cert=original_cut_bridge_gram_certificate(model,X,Y)
                for typed,key in (
                    ("POINT","independent_original_left_bridge_Gram"),
                    ("LINE","independent_original_right_bridge_Gram")
                ):
                    direct=direct_original_source_bridge_weight(model,X,Y,typed)
                    self.assertEqual(
                        direct["triples"],cert[key]["real_source_typed_bridge_triples"])
                    self.assertEqual(
                        direct["Gram"],cert[key]["original_MAgMt_or_dual_MtAfM_Gram_exact_weighted_majorant"])
                    self.assertLessEqual(
                        cert[key]["bridge_multiplicity_squared_sum"],
                        (a-2)*cert[key]["real_source_typed_bridge_triples"])
                    print("AA4DA_GENUINE_ORIGINAL_BRIDGE_TRIPLE_GRAM",s,scheme,typed,
                          "true_original_bridge_triples",direct["triples"],
                          "actual_original_weighted_GQ_Gram",direct["Gram"],flush=True)

    def test_04_genuine_W34_W38_frozen_complete_global_maps_and_SAFE_source_flags(self):
        for power,schemes in ((2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,*_=_validated_original(model)
                k=a//2
                cuts=((tuple(range(k)),tuple(range(a-k,a))),
                      (tuple(range(a-k,a)),tuple(range(k)))) if power==2 else (
                      (tuple(range(k)),tuple(range(a-k,a))),)
                for ci,(X,Y) in enumerate(cuts):
                    z=original_cut_bridge_gram_certificate(model,X,Y)
                    self.assertLessEqual(
                        z["exact_original_RAW_to_SAFE_flag_loss"],
                        z["total_true_original_bridge_Gram_loss_majorant"])
                    self.assertGreaterEqual(z["true_original_double_disjoint_SAFE_incidence_mass"],0)
                    self.assertGreaterEqual(z["original_safe_positive_double_disjoint_nonincident_P3"],0)
                    self.assertTrue(z["original_3x3_perfect_matching_NOT_DEDUCED"])
                    self.assertTrue(z["original_historical_GF5_sixflag_NOT_DEDUCED"])
                    self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
                    print("AA4DA_GENUINE_SOURCE_BRIDGE_MASS",s,scheme,ci,
                          "RAW",z["true_original_double_disjoint_RAW_incidence_mass"],
                          "SAFE",z["true_original_double_disjoint_SAFE_incidence_mass"],
                          "RAW_to_SAFE_loss",z["exact_original_RAW_to_SAFE_flag_loss"],
                          "bridge_GQ_Gram_upper",
                          z["total_true_original_bridge_Gram_loss_majorant"],
                          "genuine_SAFEpositive_nonincident",
                          z["original_safe_positive_double_disjoint_nonincident_P3"],
                          flush=True)

    def test_05_failclosed_original_typed_source_labels_and_coordinate_cuts(self):
        for h in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                allh_original_bridge_gram_safe_arithmetic(h)
        model=fixture(1,"lex")
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(3,4,True))):
            with self.assertRaises(ValueError):
                original_cut_bridge_gram_certificate(model,X,Y)
        bad=dict(model);labels=list(model["left_labels"]);labels[1]=labels[0]
        bad["left_labels"]=tuple(labels)
        with self.assertRaises(ValueError):
            original_cut_bridge_gram_certificate(bad)


if __name__=="__main__":
    unittest.main()
