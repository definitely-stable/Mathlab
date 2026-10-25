"""AA4-CU: independent TRUE ORIGINAL source matching and 3-minor oracles."""
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_BBo_exact_three_matching_transfer,
    original_nonincident_threepath,
    original_dual_model_immutable_source_Q,
)
from hyp105_issue230_d6aa4cu_exterior_matching_energy import (
    incidence_minor3_det,
    true_original_exterior_energy_parameters,
    original_source_anchor_exterior_energy,
)


def independent_all_three_source_flags(model):
    """Brute THREE independent genuine original flags, not any minors."""
    _,_,_,_,_,_,_= _validated_original(model)
    inc=model["incidences"]
    return sum(
        len({p for p,l in flags})==3 and len({l for p,l in flags})==3
        for flags in combinations(inc,3)
    )


def independent_gq_three_matching_from_ordered_two_flags(model):
    """GQ source walker; arithmetic third-edge availability for EVERY pair."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    flags=tuple(tuple(e) for e in model["incidences"])
    m=len(flags);d=s+1
    ordered=0
    crossing_sum=0
    for p,l in flags:
        for q,l0 in flags:
            if p==q or l==l0:
                continue
            cross=int(l0 in pl[p])+int(l in pl[q])
            if cross>1:
                raise AssertionError("genuine GQ has a forbidden source fourcycle")
            crossing_sum+=cross
            ordered+=m-4*d+2+cross
    if crossing_sum!=2*m*(d-1)**2:
        raise AssertionError("independent source adjacent-threepath cross tally invalid")
    if ordered%6:
        raise AssertionError("source 3match ordered/unordered factor")
    return ordered//6


def direct_permanent3(P,L,pl):
    return sum(all(l in pl[p] for p,l in zip(P,permutation))
               for permutation in permutations(L))


def independent_mmT_polynomial_spectrum(model):
    """Exact original incidence MM^T eigenvalue annihilator, no eigensolver."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    rows=[set(x) for x in pl]
    Q=[[len(rows[p]&rows[q]) for q in range(V)] for p in range(V)]
    def mm(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(V))
                 for j in range(V)] for i in range(V)]
    I=[[int(i==j) for j in range(V)] for i in range(V)]
    u=2*s;v=(s+1)**2
    A=[[Q[i][j]-u*I[i][j] for j in range(V)] for i in range(V)]
    B=[[Q[i][j]-v*I[i][j] for j in range(V)] for i in range(V)]
    product=mm(mm(Q,A),B)
    if any(z!=0 for row in product for z in row):
        raise AssertionError("genuine W3 incidence MM^T eigen polynomial false")
    if sum(Q[i][i] for i in range(V))!=V*(s+1):
        raise AssertionError("GQ degree/trace false")
    return True


class AA4CUOriginalGQExteriorEnergy(unittest.TestCase):
    def test_01_original_W32_every_threeflags_and_all_3x3_minors(self):
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        params=true_original_exterior_energy_parameters(s)
        count=independent_all_three_source_flags(model)
        self.assertEqual(count,10560)
        self.assertEqual(count,params["global_exterior3_frobenius_squared"])
        self.assertEqual(count,independent_gq_three_matching_from_ordered_two_flags(model))
        self.assertTrue(independent_mmT_polynomial_spectrum(model))
        point_sets=tuple(combinations(range(V),3))
        line_sets=tuple(combinations(range(V),3))
        sq=positive=negative=0
        for P in point_sets:
            for L in line_sets:
                det=incidence_minor3_det(P,L,pl)
                self.assertIn(det,(-1,0,1))
                sq+=det*det
                positive+=det>0
                negative+=det<0
                if det:
                    self.assertEqual(direct_permanent3(P,L,pl),1)
        self.assertEqual(sq,count)
        self.assertEqual(positive+negative,count)
        print("AA4CU_W32_ALL_3X3_SQUARED_MINORS",sq,
              "signed_positive",positive,"signed_negative",negative,flush=True)

    def test_02_original_W34_unrestricted_energy_independent_edge_walker(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            params=true_original_exterior_energy_parameters(4)
            self.assertEqual(params["global_exterior3_frobenius_squared"],11995200)
            self.assertEqual(params["global_exterior3_frobenius_squared"],
                             independent_gq_three_matching_from_ordered_two_flags(model))
            self.assertTrue(independent_mmT_polynomial_spectrum(model))
            print("AA4CU_W34_SOURCE_ALL_MATCHINGS",scheme,
                  params["global_exterior3_frobenius_squared"],flush=True)

    def test_03_W32_full_real_historical_BBo_oracle_and_true_zero_cut(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            anchors=tuple((p,l) for p in range(V) for l in range(V)
                          if l not in pl[p])
            new=original_source_anchor_exterior_energy(model,anchors)
            old=original_BBo_exact_three_matching_transfer(model,collect_original_Q=False)
            self.assertEqual(new["historical_original_BBo_sixflag_count"],
                             old["historical_accepted_original_BBo_sixflag_Q"])
            self.assertEqual(new["all_anchored_occupied_physical_C4_pairs"],
                             old["paired_two_sided_C4_templates"])
            self.assertEqual(new["historical_original_BBo_sixflag_count"],
                             8 if scheme=="lex" else 1)
            self.assertEqual(new["determinant_abs_sum_check"],
                             new["compressed_exterior3_original_squared_energy"])
            # The true W32 lex X=012/Y=345 cut has ONE original double
            # physically disjoint 3path, K6 is FULL, 2x2 physical C4,
            # but ALL four TRUE GQ 3x3 incidence minors are zero.
            if scheme=="lex":
                X,Y={0,1,2},{3,4,5}
                cut=tuple((p,l) for p,l in anchors
                          if set(f[p])<=X and set(g[l])<=Y)
                cert=original_source_anchor_exterior_energy(model,cut,collect_zero=True)
                good=[x for x in cert["anchor_details"]
                      if x["both_physical_C4_candidate_pairs"]]
                self.assertEqual(len(cut),8)
                self.assertEqual(len(good),1)
                witness=good[0]
                self.assertEqual(witness["left_occupied_C4_source_triples"],2)
                self.assertEqual(witness["right_occupied_C4_source_triples"],2)
                self.assertEqual(witness["both_physical_C4_candidate_pairs"],4)
                self.assertEqual(witness["exterior3_compressed_squared_Frobenius"],0)
                self.assertIsNotNone(witness["one_original_zero_witness"])
                self.assertEqual(direct_permanent3(*witness["one_original_zero_witness"],pl),0)
                print("AA4CU_TRUE_GQ_FULL_PHYSICAL_K6_BUT_ZERO_3MATCH",
                      witness["original_anchor"],"four_C4_pairs",4,flush=True)
            print("AA4CU_W32_FULL_BBO",scheme,
                  "C4pairs",new["all_anchored_occupied_physical_C4_pairs"],
                  "accepted",new["historical_original_BBo_sixflag_count"],flush=True)

    def test_04_real_W34_and_W38_anchored_original_exterior_vs_matching(self):
        cases=((2,"lex",72),(2,"random",72),(3,"lex",1))
        for power,scheme,budget in cases:
            model=fixture(power,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            if power==3:
                anchors=((0,74),)
            else:
                anchors=tuple((p,l) for p in range(min(V,12))
                              for l in range(min(V,12))
                              if l not in pl[p])[:budget]
            new=original_source_anchor_exterior_energy(model,anchors)
            old=original_BBo_exact_three_matching_transfer(
                model,anchor_pairs=anchors,collect_original_Q=False)
            self.assertEqual(new["historical_original_BBo_sixflag_count"],
                             old["historical_accepted_original_BBo_sixflag_Q"])
            self.assertEqual(new["all_anchored_occupied_physical_C4_pairs"],
                             old["paired_two_sided_C4_templates"])
            self.assertEqual(new["positive_signed_det_count"]+
                             new["negative_signed_det_count"],
                             old["three_by_three_source_PERMANENT_one"])
            if power==3:
                self.assertEqual(new["all_anchored_occupied_physical_C4_pairs"],828100)
                self.assertEqual(new["historical_original_BBo_sixflag_count"],23)
            print("AA4CU_HIGHER_TRUE_ORIGINAL_SOURCE",s,scheme,
                  "C4pairs",new["all_anchored_occupied_physical_C4_pairs"],
                  "accepted",new["historical_original_BBo_sixflag_count"],flush=True)

    def test_05_all_dyadic_orders_exact_symbolic_arithmetic_independent(self):
        for h in range(1,27):
            s=1<<h
            z=true_original_exterior_energy_parameters(s)
            E=z["original_incidence_flags"];d=z["source_degree"]
            m=(E*(E-2*d+1)*(E-4*d+2)+2*E*(d-1)**2)//6
            self.assertEqual(z["global_exterior3_frobenius_squared"],m)
            self.assertEqual(z["incidence_matrix_rank"],1+s*(s+1)**2//2)
            self.assertLessEqual(z["global_exterior3_frobenius_squared"],comb(E,3))
        print("AA4CU_ALLH_EXACT_SOURCE_COUNTS",26,"ORDERS_PASS",flush=True)

    def test_06_fail_closed_nonoriginal_or_illtyped_factors(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            original_source_anchor_exterior_energy(model,())
        with self.assertRaises(ValueError):
            original_source_anchor_exterior_energy(model,((0,0),(0,0)))
        with self.assertRaises(ValueError):
            original_source_anchor_exterior_energy(model,((-1,0),))
        s,V,a,f,g,pl,lp=_validated_original(model)
        p,l=next((p,l) for p in range(V) for l in pl[p])
        with self.assertRaises(ValueError):
            original_source_anchor_exterior_energy(model,((p,l),))
        with self.assertRaises(ValueError):
            incidence_minor3_det((0,0,1),(0,1,2),pl)
        for bad in (1,0,-1,2.5,True):
            with self.assertRaises(ValueError):
                true_original_exterior_energy_parameters(bad)
        fake=dict(model);lbl=list(model["right_labels"]);lbl[1]=lbl[0]
        fake["right_labels"]=tuple(lbl)
        with self.assertRaises(ValueError):
            original_source_anchor_exterior_energy(fake,((0,3),))


if __name__=="__main__":unittest.main()
