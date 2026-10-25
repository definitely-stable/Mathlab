"""AA4-CS: independent true W3 point-to-line path double-disjointness auditors."""
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import (
    _validated_original, macro_path_cut,
)
from hyp105_issue230_d6aa4cs_uniform_disjoint_original_source_cut import (
    _minimal_a,
    dyadic_all_h_disjoint_macro_arithmetic,
    original_disjoint_3path_cut_certificate,
)


def four_real_physical_halfcuts(a):
    k=a//2
    return (
        (tuple(range(k)),tuple(range(a-k,a))),
        (tuple(range(a-k,a)),tuple(range(k))),
        (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))),
        (tuple(range(k)),tuple(range(1,k+1))),
    )


def independent_original_source_transpose_P3_disjointness(model,cert):
    """SECOND truly original GQ oracle, starts source LINE endpoint l first.

    Counts nonincident endpoints and the same path via the opposite
    middle incidence (q,l), then (q,l0), then (p,l0).
    Unlike product-degree bound, test explicitly enumerates every real
    source point-to-line threeflag sequence in the given true cut.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    t=left_bad=right_bad=both_bad=good=0
    X=frozenset(cert["physical_cut_X"])
    Y=frozenset(cert["physical_cut_Y"])
    for l in range(V):
        if not set(g[l])<=Y:continue
        for p in range(V):
            if not set(f[p])<=X or l in pl[p]:continue
            mids=[(q,l0) for q in lp[l]
                  for l0 in pl[q] if l0 in pl[p]]
            if len(mids)!=1:
                raise AssertionError("independent GQ source LINE-first unique P3 false")
            q,l0=mids[0]
            b0=bool(set(f[p])&set(f[q]))
            b1=bool(set(g[l])&set(g[l0]))
            t+=1;left_bad+=b0;right_bad+=b1;both_bad+=b0 and b1
            good+=not b0 and not b1
    if (t,left_bad,right_bad,both_bad,good)!=(
        cert["actual_original_nonincident_source_3paths_T"],
        cert["left_physical_disjointness_blocked_paths"],
        cert["right_physical_disjointness_blocked_paths"],
        cert["both_disjointness_blocked_paths"],
        cert["both_physically_disjoint_source_3paths"]):
        raise AssertionError("independent LINE-first original path enumeration differs")
    return True


class AA4CSUniformRealGQSourceThreepathDisjointness(unittest.TestCase):
    def _original_fixture(self,power,scheme):
        model=fixture(power,scheme)
        s,V,a,*_= _validated_original(model)
        for i,(X,Y) in enumerate(four_real_physical_halfcuts(a)):
            z=original_disjoint_3path_cut_certificate(model,X,Y)
            q=macro_path_cut(model,X,Y)
            self.assertEqual(z["actual_original_nonincident_source_3paths_T"],
                             q["unique_original_simple_3path_count"])
            self.assertEqual(z["true_original_incidence_edges_between_cuts"],
                             q["original_flag_edges_between_cuts"])
            self.assertTrue(independent_original_source_transpose_P3_disjointness(model,z))
            if i==0:
                frozen={
                    (2,"lex"):(8,1,4,6,3),
                    (2,"S72"):(7,0,6,4,3),
                    (4,"lex"):(299,123,96,106,26),
                    (4,"random"):(379,209,84,106,20),
                    (8,"lex"):(16893,12358,2318,2461,244),
                    (8,"random"):(17415,13832,1904,1895,216),
                }
                self.assertEqual((
                    z["actual_original_nonincident_source_3paths_T"],
                    z["both_physically_disjoint_source_3paths"],
                    z["left_physical_disjointness_blocked_paths"],
                    z["right_physical_disjointness_blocked_paths"],
                    z["both_disjointness_blocked_paths"],
                ),frozen[s,scheme])
            self.assertEqual(z["both_physically_disjoint_source_3paths"],
                z["actual_original_nonincident_source_3paths_T"]
                -z["left_physical_disjointness_blocked_paths"]
                -z["right_physical_disjointness_blocked_paths"]
                +z["both_disjointness_blocked_paths"])
            self.assertLessEqual(z["left_physical_disjointness_blocked_paths"],
                                 z["uniform_left_block_upper"])
            self.assertLessEqual(z["right_physical_disjointness_blocked_paths"],
                                 z["uniform_right_block_upper"])
            self.assertGreaterEqual(z["both_physically_disjoint_source_3paths"],
                                    z["actual_xy_source_degree_lower"])
            self.assertFalse(z["uniform_half_cut_disjoint_gate_h_ge_14"])
            if power==3:
                self.assertGreaterEqual(128*z["actual_original_nonincident_source_3paths_T"],V*V)
            print("AA4CS_REAL_ORIGINAL_CUT",s,scheme,"cut",i,
                  "source_paths",z["actual_original_nonincident_source_3paths_T"],
                  "physically_disjoint_both",z["both_physically_disjoint_source_3paths"],
                  "left_bad",z["left_physical_disjointness_blocked_paths"],
                  "right_bad",z["right_physical_disjointness_blocked_paths"],
                  "both_bad",z["both_disjointness_blocked_paths"],flush=True)

    def test_01_true_original_W32_lex_S72_four_cuts_and_independent_LINE_first(self):
        for scheme in ("lex","S72"):self._original_fixture(1,scheme)

    def test_02_true_original_W34_lex_random_four_cuts_and_independent_LINE_first(self):
        for scheme in ("lex","random"):self._original_fixture(2,scheme)

    def test_03_true_original_W38_lex_random_four_cuts_and_independent_LINE_first(self):
        for scheme in ("lex","random"):self._original_fixture(3,scheme)

    def test_04_exact_all_h_macro_disjointness_constant_arithmetic(self):
        for h in range(1,27):
            z=dyadic_all_h_disjoint_macro_arithmetic(h)
            s,V,a,m=z["s"],z["V"],z["a"],z["m"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertEqual(a,_minimal_a(V))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(m,comb(a//2,2)-z["H"])
            if h>=14:
                self.assertGreaterEqual(m,2*(s+1)+8*(a-2)*s)
                self.assertGreaterEqual(8*m,V)
                self.assertGreater(m*m*128,s**6*2)
                self.assertTrue(z["uniform_half_cut_disjoint_gate_h_ge_14"])
            else:
                self.assertFalse(z["uniform_half_cut_disjoint_gate_h_ge_14"])
            print("AA4CS_ALLH_INTEGER_ARITHMETIC",h,
                  "s",s,"a",a,"m",m,"threshold",z["sufficient_threshold_m_ge_2d_plus_4c"],
                  "margin",z["margin"],flush=True)

    def test_05_malformed_original_coordinate_cuts_and_model_fail_closed(self):
        model=fixture(1,"lex")
        for X,Y in (
            ((0,0,1),(3,4,5)),
            ((-1,0,1),(3,4,5)),
            ((0,1,6),(3,4,5)),
            ((0,1),(3,4,5)),
            ((0,1,2),(3,4,4)),
            ((False,1,2),(3,4,5))
        ):
            with self.assertRaises(ValueError):
                original_disjoint_3path_cut_certificate(model,X,Y)
        for h in (0,-1,2.5,True):
            with self.assertRaises(ValueError):
                dyadic_all_h_disjoint_macro_arithmetic(h)
        fake=dict(model)
        fake["incidences"]=tuple(model["incidences"][:-1])
        with self.assertRaises(ValueError):
            original_disjoint_3path_cut_certificate(fake)
        fake=dict(model)
        bad=list(model["left_labels"]);bad[1]=bad[0]
        fake["left_labels"]=tuple(bad)
        with self.assertRaises(ValueError):
            original_disjoint_3path_cut_certificate(fake)


if __name__=="__main__":
    unittest.main()
