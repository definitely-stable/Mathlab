"""AA4-CW: independent genuine ORIGINAL GQ source-flag and physical-spoke tests."""
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage import (
    minimal_a, exact_dyadic_cut_leakage_arithmetic,
    original_cut_spoke_leakage_certificate,
)


def _cuts(a):
    k=a//2
    return (
        (tuple(range(k)),tuple(range(a-k,a))),
        (tuple(range(a-k,a)),tuple(range(k))),
        (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))),
        (tuple(range(k)),tuple(range(1,k+1))),
    )


def _independent_actual_flag_first_mass(model,X,Y):
    """Sum ACTUAL original immutable incidence IDs, no source walk/oracle reuse."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    P=tuple(p for p in range(V) if set(f[p])<=set(X))
    L=tuple(l for l in range(V) if set(g[l])<=set(Y))
    # Reversed complete factor-image sets enumerate source witnesses.
    point_spoke_degree={i:sum(i!=p and bool(set(f[i])&set(f[p]))
                               for p in P) for i in P}
    line_spoke_degree={j:sum(j!=l and bool(set(g[j])&set(g[l]))
                              for l in L) for j in L}
    return sum(point_spoke_degree[p]*line_spoke_degree[l]
               for p,l in model["incidences"]
               if p in point_spoke_degree and l in line_spoke_degree)


def _independent_cut_anchor_direct(model,X,Y):
    """Explicit SOURCE flag-by-flag brute test for each genuine p,l anchor."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    P=tuple(p for p in range(V) if set(f[p])<=set(X))
    L=tuple(l for l in range(V) if set(g[l])<=set(Y))
    results={}
    for p in P:
        for l in L:
            # This second oracle iterates the IMMUTABLE original source
            # flags without constructing the CW optimized spoke graph.
            count=sum(
                i!=p and j!=l and set(f[i])<=set(X)
                and set(g[j])<=set(Y)
                and bool(set(f[p])&set(f[i]))
                and bool(set(g[l])&set(g[j]))
                for i,j in model["incidences"]
            )
            results[p,l]=count
    return results


class AA4CWTrueOriginalManyAnchorLeakage(unittest.TestCase):
    def test_01_exact_allh_integer_feasibility_and_real_exponent(self):
        for h in range(1,31):
            a=exact_dyadic_cut_leakage_arithmetic(h)
            s,V,k,d=a["s"],a["V"],a["k"],a["d"]
            self.assertEqual(a["a"],minimal_a(V))
            self.assertLess(comb(a["a"]-1,2),V)
            self.assertGreaterEqual(comb(a["a"],2),V)
            if h>=24:
                self.assertGreaterEqual(k,2048*d)
                self.assertGreaterEqual(V,128*(a["a"]-2))
                self.assertGreaterEqual(d*d,2048*s)
                self.assertGreaterEqual(8*a["m"],V)
                self.assertGreater(4*k*k,s*s*s)
                self.assertTrue(a["allh_gate_h_ge_24"])
            else:self.assertFalse(a["allh_gate_h_ge_24"])
            if h in (14,20,23,24,30):
                print("AA4CW_GENUINE_DYADIC_INTEGER_GATE",
                      h,"s",s,"a",a["a"],"k",k,"degree",d,
                      "nonincident_lower_Vk_div2048",
                      V*k//2048,flush=True)

    def test_02_all_W32_original_source_flags_all_cut_anchors_independent_brute(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,*_= _validated_original(model)
            for cut,X_Y in enumerate(_cuts(a)):
                X,Y=X_Y
                z=original_cut_spoke_leakage_certificate(model,X,Y)
                d=_independent_cut_anchor_direct(model,X,Y)
                self.assertEqual(sum(d.values()),
                                 z["true_original_flag_mass_through_incut_physical_spokes"])
                self.assertEqual(sum(bool(value) for (p,l),value in d.items()
                                     if l not in {j for pp,j in model["incidences"] if pp==p}),
                                 z["positive_spoke_NONINCIDENT_P3_anchors"])
                self.assertEqual(sum(1 for v in d.values() if v),
                                 z["positive_spoke_anchors_including_incident"])
                self.assertEqual(z["independent_flag_first_source_mass"],
                                 _independent_actual_flag_first_mass(model,X,Y))
                self.assertEqual(z["source_original_incident_pairs"]+
                                 z["source_original_nonincident_P3_anchors"],len(d))
                self.assertTrue(z["does_NOT_imply_matching_or_GF5"])
                print("AA4CW_TRUE_ORIGINAL_W32",scheme,"cut",cut,
                      "nonincident_P3",z["source_original_nonincident_P3_anchors"],
                      "raw_spoke_positive",z["positive_spoke_NONINCIDENT_P3_anchors"],
                      "source_flags_weighted",sum(d.values()),flush=True)

    def test_03_real_W34_W38_two_full_correlated_original_maps_each(self):
        for power,schemes in ((2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,*_= _validated_original(model)
                for cut,(X,Y) in enumerate(_cuts(a)):
                    z=original_cut_spoke_leakage_certificate(model,X,Y)
                    self.assertEqual(z["true_original_flag_mass_through_incut_physical_spokes"],
                                     _independent_actual_flag_first_mass(model,X,Y))
                    self.assertLessEqual(z["positive_spoke_NONINCIDENT_P3_anchors"],
                                         z["source_original_nonincident_P3_anchors"])
                    self.assertTrue(z["max_original_spoke_cross_incidence_at_one_anchor"]
                                    <=2*(a//2-2)*(s+1))
                    self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
                    self.assertFalse(s>=1<<24)
                    print("AA4CW_REAL_ORIGINAL_W3",s,scheme,"cut",cut,
                          "nonincident",z["source_original_nonincident_P3_anchors"],
                          "positive_spoke_nonincident",
                          z["positive_spoke_NONINCIDENT_P3_anchors"],
                          "genuine_source_spoke_flags",
                          z["true_original_flag_mass_through_incut_physical_spokes"],
                          flush=True)

    def test_04_nonincidence_paths_and_CV_no_go_nonimplication(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            X,Y=_cuts(a)[0]
            result=original_cut_spoke_leakage_certificate(model,X,Y)
            P=[p for p in range(V) if set(f[p])<=set(X)]
            L=[l for l in range(V) if set(g[l])<=set(Y)]
            count=sum(l not in pl[p] for p in P for l in L)
            self.assertEqual(result["source_original_nonincident_P3_anchors"],count)
            for p in P:
                for l in L:
                    if l not in pl[p]:
                        path=original_nonincident_threepath(p,l,pl,lp)
                        self.assertEqual(len(set(path)),3)
            # Raw source spoke crossing can use original factors whose
            # physical pair contains the doubled endpoint coordinate.
            # We intentionally refuse to promote it to valid C4 or GF5.
            self.assertTrue(result["not_the_doubled_factor_avoiding_C4_completion"])
            self.assertTrue(result["does_NOT_imply_matching_or_GF5"])

    def test_05_invalid_physical_cut_and_duplicated_full_original_map_fail_closed(self):
        model=fixture(1,"lex")
        a=_validated_original(model)[2]
        for X,Y in (((0,0,1),(3,4,5)),
                    ((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),
                    ((0,1,2),(3,3,4)),
                    ((False,1,2),(3,4,5))):
            with self.assertRaises(ValueError):
                original_cut_spoke_leakage_certificate(model,X,Y)
        for h in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                exact_dyadic_cut_leakage_arithmetic(h)
        broken=dict(model)
        m=list(model["left_labels"])
        m[1]=m[0]
        broken["left_labels"]=tuple(m)
        with self.assertRaises(ValueError):
            original_cut_spoke_leakage_certificate(broken)


if __name__=="__main__":unittest.main()
