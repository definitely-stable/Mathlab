"""Independent exact true-original C/B degree-3 six-cube rigidity tests."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4bw_CB_sixcube_lowdegree_rigidity import (
    original_CB_sixcube_uniform_certificate,
    original_CB_sixcube_fixed_f_source_tail,
    original_true_W32_CB_sixcube_polynomial,
    _fwt_integer,
)

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def independent_literal_original_CB(Q,inc,point_map,line_map):
    """No historical classifier, no Walsh routine, no GQ intersection oracle.

    The necessary and sufficient true-original selected C/B properties:
    three doubled ORIGINAL source point factors; one doubled source
    LINE factor, four singleton original lines; BOTH physical degree2
    on SIX distinct coordinates, using SAME six immutable source flags.
    """
    if len(Q)!=6 or len(set(Q))!=6:return False
    P=Counter(inc[j][0] for j in Q)
    L=Counter(inc[j][1] for j in Q)
    if tuple(sorted(P.values()))!=(2,2,2):return False
    if tuple(sorted(L.values()))!=(1,1,1,1,2):return False
    for side,labels in ((0,point_map),(1,line_map)):
        d=Counter(u for j in Q for u in labels[inc[j][side]])
        if len(d)!=6 or set(d.values())!={2}:return False
    return True


def independent_direct_walsh(scores,T):
    """Literal 64-term signed average, independent of production FWT."""
    return Fraction(sum((-1 if (x&T).bit_count()%2 else 1)*scores[x]
                        for x in range(64)),64)


class OriginalCBTrueGQSixcubeRemainder(unittest.TestCase):
    def test_01_all_dyadic_h_exact_analytic_original_CB_sixcube_degree3(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h
            z=original_CB_sixcube_uniform_certificate(s)
            d=s+1
            n4=960+96*d+192*(2*d-1)*(d-1)
            self.assertEqual(z["max_fourth_true_original_C_B_sixflag_source_cap"],n4)
            self.assertEqual(z["max_fifth_true_original_C_B_sixflag_source_cap"],960)
            self.assertEqual(z["all_h_uniform_degree_gt3_absolute_remainder_cap"],
                             Fraction(15*n4+6*960,2))
            self.assertTrue(z["original_C_B_sixth_order_Walsh_exactly_zero"])
            self.assertTrue(z["uniform_o_s6_analytic_since_degree2_in_s"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertLess(original_CB_sixcube_uniform_certificate(1<<24)[
            "relative_to_six_scale_exact"],Fraction(1,10**12))

    def test_02_true_original_W32_all64_complete_maps_GQ_CB_source_tail(self):
        results={}
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            z=original_true_W32_CB_sixcube_polynomial(model,PACKETS)
            self.assertEqual(z["64_complete_GLOBAL_original_LINE_maps_on_same_support"],64)
            self.assertEqual(len(z["historical_C_B_acceptance_at_each_complete_map"]),64)
            self.assertEqual(z["zero_mode_original_C_B_average"],
                Fraction(sum(z["historical_C_B_acceptance_at_each_complete_map"]),64))
            self.assertEqual(z["unchanged_initial_original_C_B_score"],
                z["historical_C_B_acceptance_at_each_complete_map"][0])
            self.assertEqual(z["exact_fourier_coefficients"][63],0)
            self.assertLessEqual(z["max_actual_tail_absolute"],
                z["source_geometry_fixed_f_certificate"][
                    "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"])
            self.assertLessEqual(z["max_actual_tail_absolute"],
                z["all_h_uniform_source_bound"])
            for mask in (0,1,15,42,63):
                self.assertEqual(
                    Fraction(z["historical_C_B_acceptance_at_each_complete_map"][mask]),
                    z["exact_degree3_projection_at_all_complete_maps"][mask]+
                    z["exact_degree4_and_5_tail_at_all_complete_maps"][mask])
            pinned={
                "lex":{"center":1,"mean":Fraction(19,32),
                       "max_tail":Fraction(3,16),"fixed_f":Fraction(79)},
                "S72":{"center":0,"mean":Fraction(1,16),
                       "max_tail":Fraction(1,16),"fixed_f":Fraction(63,2)}
            }[scheme]
            self.assertEqual(z["unchanged_initial_original_C_B_score"],pinned["center"])
            self.assertEqual(z["zero_mode_original_C_B_average"],pinned["mean"])
            self.assertEqual(z["max_actual_tail_absolute"],pinned["max_tail"])
            self.assertEqual(z["source_geometry_fixed_f_certificate"][
                "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],pinned["fixed_f"])
            results[scheme]=z
            print("AA4BW_W32",scheme,
                  "score0",z["unchanged_initial_original_C_B_score"],
                  "zero-mode",z["zero_mode_original_C_B_average"],
                  "max-tail",z["max_actual_tail_absolute"],
                  "fixed-f-bound",z["source_geometry_fixed_f_certificate"][
                    "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],
                  flush=True)
        self.assertEqual(set(results),{"lex","S72"})

    def test_03_true_W32_independent_direct_64_Walsh_all_subsets(self):
        for scheme in ("lex","S72"):
            values=original_true_W32_CB_sixcube_polynomial(
                fixture(1,scheme),PACKETS)
            vals=values["historical_C_B_acceptance_at_each_complete_map"]
            for T in range(64):
                self.assertEqual(values["exact_fourier_coefficients"][T],
                    independent_direct_walsh(vals,T))
                if T.bit_count()==6:
                    self.assertEqual(values["exact_fourier_coefficients"][T],0)
                if T.bit_count()>=4:
                    cap=values["source_geometry_fixed_f_certificate"]
                    ids=tuple(j for j in range(6) if T>>j&1)
                    if len(ids)==4:
                        n=cap["fourth_source_C_B_left_physical_eligible_by_T"][ids]
                    elif len(ids)==5:
                        n=cap["fifth_source_C_B_left_physical_eligible_by_T"][ids]
                    else:n=0
                    self.assertLessEqual(abs(values["exact_fourier_coefficients"][T]),
                                         Fraction(n,2))
            for x in range(64):
                low=sum(((-1 if (x&T).bit_count()%2 else 1)*
                         values["exact_fourier_coefficients"][T])
                        for T in range(64) if T.bit_count()<=3)
                self.assertEqual(low,values[
                    "exact_degree3_projection_at_all_complete_maps"][x])

    def test_04_true_original_W32_literal_SOURCE_64_map_all_Q_oracle(self):
        model=fixture(1,"S72")
        s,V,a,inc,f,g,_,_=_original_source(model)
        Qs=tuple(Q for Q,_ in selected_left_six(model))
        self.assertEqual(len(Qs),62370)
        actual=original_true_W32_CB_sixcube_polynomial(model,PACKETS)
        # Deliberately no historical class classifier, no source
        # packet filter, no use of the production C/B six-Q subset.
        # Loop entire historically left-eligible ORIGINAL six-Q census
        # against every COMPLETE globally injected right swap map.
        for mask in range(64):
            state=apply_disjoint_factor_swaps(
                g,PACKETS,tuple(i for i in range(6) if mask>>i&1))
            independent=sum(independent_literal_original_CB(Q,inc,f,state)
                            for Q in Qs)
            self.assertEqual(independent,
                actual["historical_C_B_acceptance_at_each_complete_map"][mask])
        self.assertEqual(len(set(Qs)),62370)

    def test_05_original_W34_NONONTO_geometry_refined_right_g_independence(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            z=original_CB_sixcube_fixed_f_source_tail(model,PACKETS)
            self.assertEqual((z["s"],z["a"]),(4,14))
            self.assertEqual(len(z["fourth_source_C_B_left_physical_eligible_by_T"]),15)
            self.assertEqual(len(z["fifth_source_C_B_left_physical_eligible_by_T"]),6)
            self.assertLessEqual(z["fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],
                z["all_h_universal_tail_cap"])
            varied=dict(model,right_labels=tuple(reversed(model["right_labels"])))
            q=original_CB_sixcube_fixed_f_source_tail(varied,PACKETS)
            self.assertEqual(z["fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],
                             q["fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"])
            self.assertEqual(z["fourth_source_C_B_left_physical_eligible_by_T"],
                             q["fourth_source_C_B_left_physical_eligible_by_T"])
            self.assertEqual(z["fifth_source_C_B_left_physical_eligible_by_T"],
                             q["fifth_source_C_B_left_physical_eligible_by_T"])

    def test_06_source_input_and_whole_LINE_packet_guards(self):
        for s in (0,-2,1,3,5,True):
            with self.assertRaises(ValueError):
                original_CB_sixcube_uniform_certificate(s)
        model=fixture(1,"lex")
        for bad in (PACKETS[:5],((0,1),(1,2),(3,4),(5,6),(7,8),(9,10))):
            with self.assertRaises(ValueError):
                original_CB_sixcube_fixed_f_source_tail(model,bad)
            with self.assertRaises(ValueError):
                original_true_W32_CB_sixcube_polynomial(model,bad)
        with self.assertRaises(ValueError):
            original_true_W32_CB_sixcube_polynomial(fixture(2,"lex"),PACKETS)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                original_CB_sixcube_fixed_f_source_tail(bad,PACKETS)
        with self.assertRaises(ValueError):
            _fwt_integer((0,1,2))

    def test_07_method_no_go_zero_center_despite_zero_high_order(self):
        """Only an ABSTRACT warning, NOT an actual W3 GF5 counterfamily."""
        score=tuple((x&1)+((x>>1)&1) for x in range(64))
        hat=_fwt_integer(score)
        self.assertEqual(score[0],0)
        self.assertGreater(Fraction(hat[0],64),0)
        self.assertTrue(all(z==0 for i,z in enumerate(hat) if i.bit_count()>=2))
        self.assertTrue(all(v>=0 for v in score))
        # This only falsifies 'low-degree + positive MEAN
        # automatically gives positive ORIGINAL CENTER', an abstract
        # already-understood methodological no-go; no Branch B claim.

if __name__=="__main__":
    unittest.main()
