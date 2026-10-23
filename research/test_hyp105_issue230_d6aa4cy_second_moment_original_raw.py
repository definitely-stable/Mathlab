"""AA4-CY: independent real ORIGINAL GQ source flag FIRST/SECOND moments."""
from itertools import combinations
from math import comb,isqrt
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cy_second_moment_original_raw import (
    allh_raw_frobenius_arithmetic,original_cut_frobenius_second_moment,
)


def independent_direct_original_flag_census(model,X,Y):
    """Original immutable GQ FLAGS-first, every original cut anchor p,l.

    Neither optimized original AA4-CW source flag pushforward nor
    local second-moment module used here. No source labels are re-drawn.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    P=tuple(p for p in range(V) if set(f[p])<=set(X))
    L=tuple(l for l in range(V) if set(g[l])<=set(Y))
    original_flags=tuple(model["incidences"])
    values={}
    for p in P:
        for l in L:
            count=0
            for i,j in original_flags:
                count+=(i!=p and j!=l and
                         set(f[i])<=set(X) and set(g[j])<=set(Y) and
                         not set(f[i]).isdisjoint(f[p]) and
                         not set(g[j]).isdisjoint(g[l]))
            if count:values[p,l]=count
    return {
        "T":sum(values.values()),
        "Q":sum(x*x for x in values.values()),
        "positive":len(values),
        "nonincident":sum(l not in pl[p] for p,l in values),
        "incident":sum(l in pl[p] for p,l in values)
    }


def original_flag_pair_gram_census(model,X,Y):
    """INDEPENDENT exact 2-source-incidence-flag Gram formula.

    Double sum over *two genuine original immutable flag IDs*, not
    over physical source anchor pairs. Uses source endpoint reverse
    physical edge comparisons.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    P={p for p in range(V) if set(f[p])<=set(X)}
    L={l for l in range(V) if set(g[l])<=set(Y)}
    flags=[(i,j) for i,j in model["incidences"] if i in P and j in L]
    pf={i:frozenset(p for p in P if p!=i and
                    not set(f[p]).isdisjoint(f[i])) for i in P}
    gl={j:frozenset(l for l in L if l!=j and
                    not set(g[l]).isdisjoint(g[j])) for j in L}
    return sum(len(pf[i]&pf[ii])*len(gl[j]&gl[jj])
               for i,j in flags for ii,jj in flags)


class AA4CYOriginalRawFrobeniusTests(unittest.TestCase):
    def test_01_allh_big_int_threshold_s11_half_original_source(self):
        for h in range(1,35):
            z=allh_raw_frobenius_arithmetic(h)
            s,V,k,d=z["s"],z["V"],z["k"],z["d"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertLess(comb(z["a"]-1,2),V)
            self.assertGreaterEqual(comb(z["a"],2),V)
            if h>=24:
                self.assertTrue(z["allh_gate_h_ge_24"])
                self.assertLess(4*k,s*s)
                self.assertLessEqual(d*d*k,s*V)
                self.assertGreaterEqual(k*s,(1<<25)*d)
                self.assertGreater(4*k*k,s**3)
                self.assertGreater(
                     (s*k*V//(1<<25))**2*(1<<52),s**11)
                self.assertGreater(z["raw_positive_integer_floor_at_least"],0)
            else:
                self.assertFalse(z["allh_gate_h_ge_24"])
            if h in (16,23,24,30,34):
                print("AA4CY_ALLH_EXACT_GATE",h,"s",s,
                      "V",V,"k",k,"s11half_floor",
                      z["raw_positive_integer_floor_at_least"],flush=True)

    def test_02_true_W32_all_original_cut_anchors_three_independent_referees(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,*_=_validated_original(model)
            k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))),
                  (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))))
            for ci,(X,Y) in enumerate(cuts):
                x=original_cut_frobenius_second_moment(model,X,Y,True)
                y=independent_direct_original_flag_census(model,X,Y)
                q=original_flag_pair_gram_census(model,X,Y)
                self.assertEqual(x["original_raw_spoke_first_moment_T"],y["T"])
                self.assertEqual(x["original_raw_spoke_second_moment_Q"],y["Q"])
                self.assertEqual(x["independent_original_source_flag_pair_Gram_Q"],q)
                self.assertEqual(q,y["Q"])
                self.assertEqual(x["raw_spoke_positive_original_NONINCIDENT_P3"],y["nonincident"])
                self.assertEqual(x["raw_spoke_positive_original_INCIDENT_pairs"],y["incident"])
                self.assertEqual(x["raw_spoke_positive_original_endpoint_pairs"],y["positive"])
                print("AA4CY_ORIGINAL_W32",scheme,ci,"T",y["T"],"Q",y["Q"],
                      "nonincident",y["nonincident"],"independentGram",q,flush=True)

    def test_03_true_W34_W38_original_second_moment_vs_flagpair_gram(self):
        for power,schemes in ((2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,*_=_validated_original(model);k=a//2
                cuts=((tuple(range(k)),tuple(range(a-k,a))),
                      (tuple(range(a-k,a)),tuple(range(k)))) if power==2 else (
                      (tuple(range(k)),tuple(range(a-k,a))),)
                for ci,(X,Y) in enumerate(cuts):
                    x=original_cut_frobenius_second_moment(model,X,Y,True)
                    q=original_flag_pair_gram_census(model,X,Y)
                    self.assertEqual(x["original_raw_spoke_second_moment_Q"],q)
                    self.assertEqual(x["independent_original_source_flag_pair_Gram_Q"],q)
                    self.assertGreaterEqual(
                        x["raw_spoke_positive_original_endpoint_pairs"] *
                        x["original_raw_spoke_second_moment_Q"],
                        x["original_raw_spoke_first_moment_T"]**2)
                    self.assertLessEqual(
                        x["original_raw_spoke_second_moment_Q"],
                        x["source_spectral_absolute_Frobenius_Q_upper"])
                    print("AA4CY_GENUINE_ORIGINAL_GQ",s,scheme,ci,
                          "T",x["original_raw_spoke_first_moment_T"],
                          "Q",q,"nonincident",
                          x["raw_spoke_positive_original_NONINCIDENT_P3"],
                          "all_original_flagpairs",
                          x["genuine_original_flags_between_two_cut_factor_sets"],flush=True)

    def test_04_true_original_full_moment_spectrum_and_strict_nonimplication(self):
        for power,scheme in ((1,"lex"),(1,"S72"),(2,"lex"),(3,"lex")):
            model=fixture(power,scheme)
            s,V,a,*_=_validated_original(model)
            z=original_cut_frobenius_second_moment(model)
            T=z["original_raw_spoke_first_moment_T"]
            Q=z["original_raw_spoke_second_moment_Q"]
            N=z["raw_spoke_positive_original_endpoint_pairs"]
            self.assertGreaterEqual(N,
                z["Cauchy_positive_support_necessary_ceiling"])
            self.assertEqual(T==0,Q==0)
            self.assertTrue(z["actual_original_second_moment_support_no_GF5_transfer"])
            # Recorded true ORIGINAL W32 no-go from prior CW: lex cut
            # can have RAW original spoke interactions but none produce
            # the 6-flag matching in one physical 2x2 C4 completion.
            if power==1 and scheme=="lex":
                self.assertEqual(
                    z["raw_spoke_positive_original_NONINCIDENT_P3"],4)
            print("AA4CY_FROBENIUS_SOURCE_BOUND",s,scheme,
                  "T",T,"Q",Q,
                  "spectralQcap",z["source_spectral_absolute_Frobenius_Q_upper"],
                  flush=True)

    def test_05_reject_malformed_dyadic_and_noninjective_original_map_cut(self):
        for h in (0,-1,1.5,True):
            with self.assertRaises(ValueError):
                allh_raw_frobenius_arithmetic(h)
        model=fixture(1,"lex")
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(3,4,True))):
            with self.assertRaises(ValueError):
                original_cut_frobenius_second_moment(model,X,Y)
        dup=dict(model);f=list(model["left_labels"]);f[0]=f[1]
        dup["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            original_cut_frobenius_second_moment(dup)


if __name__=="__main__":unittest.main()
