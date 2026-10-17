"""Independent genuine-original both SOURCE-point-C historical GF5 proofs."""
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
from hyp105_issue230_d6aa4bx_weighted_POINT_C_sixcube import (
    weighted_POINT_C_all_h_certificate,
    historical_W32_POINT_C_two_class_sixcube,
)
from hyp105_issue230_d6aa4bw_CB_sixcube_lowdegree_rigidity import (
    original_CB_sixcube_fixed_f_source_tail,
)

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def independent_literal_GF5_point_C_class(Q,original,point_map,line_map):
    """Independent of historic classifier. Both true C/A/C/B orientations.

    Historical original C/A comprises source POINT C / LINE A AND
    source POINT A / LINE C. Similarly original C/B also comprises
    original POINT B / LINE C. The reverse orientation LINE C has
    only THREE distinct true original LINE factors, so it cannot
    contribute at Walsh order FOUR or more on disjoint LINE packets.
    However, it MUST remain present in ALL 64 raw SCORE vertices,
    zero mode and orders <=3. Physical 2-regularity is necessary
    and sufficient for both classes; a disconnected 2-factor is
    accepted here. Connected C6 is only additionally required for D6.
    """
    if len(Q)!=6 or len(set(Q))!=6:return None
    P=tuple(sorted(Counter(original[j][0] for j in Q).values()))
    L=tuple(sorted(Counter(original[j][1] for j in Q).values()))
    A=(1,1,1,1,1,1);B=(1,1,1,1,2);C=(2,2,2)
    if (P,L) in ((C,A),(A,C)):
        tag="C/A"
    elif (P,L) in ((C,B),(B,C)):
        tag="C/B"
    else:return None
    for side,lab in ((0,point_map),(1,line_map)):
        degrees=Counter(coord for j in Q for coord in lab[original[j][side]])
        if len(degrees)!=6 or set(degrees.values())!={2}:return None
    return tag

def independent_signed_walsh_64(values,T):
    return Fraction(sum(((-1 if (x&T).bit_count()%2 else 1)*values[x])
                        for x in range(64)),64)


class BXSixcubeTrueOriginalWeightedPointC(unittest.TestCase):
    def test_01_all_h_genuine_point_C_two_class_weighted_cubic_bound(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h
            z=weighted_POINT_C_all_h_certificate(s)
            V=(s+1)*(s*s+1);d=s+1
            n4ca=96*d*d*(d-1)**2+48*(V-2)*comb(d,2)
            n5ca=480*d*(d-1)
            self.assertEqual(z["SOURCE_point_C_original_class_C_A_fourth_upper"],n4ca)
            self.assertEqual(z["SOURCE_point_C_original_class_C_A_fifth_upper"],n5ca)
            self.assertEqual(z["SOURCE_point_C_original_class_C_A_sixth_upper"],960)
            self.assertEqual(z["SOURCE_point_C_original_class_C_B_sixth_upper"],0)
            cb4=960+96*d+192*(2*d-1)*(d-1)
            e_ca=Fraction(15*n4ca+6*n5ca+960,2)
            e_cb=Fraction(15*cb4+6*960,2)
            self.assertEqual(z["uniform_CA_cubic_remainder"],e_ca)
            self.assertEqual(z["uniform_CB_cubic_remainder"],e_cb)
            self.assertEqual(z["uniform_WEIGHTED_point_C_cubic_remainder"],
                             43320*e_ca+49050*e_cb)
            self.assertTrue(z["weighted_C_cubic_remainder_o_s6_proved_by_degree5"])
            self.assertTrue(z["weight_combination_is_NOT_all_seven_classes"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertLess(weighted_POINT_C_all_h_certificate(1<<40)[
            "normalized_by_s6_exact"],Fraction(1,1000))

    def test_02_real_original_W32_64_global_maps_TWO_CLASS_weighted_projection(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            z=historical_W32_POINT_C_two_class_sixcube(model,PACKETS)
            self.assertEqual(z["64_globally_injected_original_right_maps"],64)
            self.assertEqual(len(z["original_selected_necessary_GF5_weighted_POINT_C_values"]),64)
            self.assertEqual(len(z["exact_original_WEIGHTED_point_C_Walsh"]),64)
            self.assertEqual(z["initial_unchanged_weighted_POINT_C_score"],
                             z["original_selected_necessary_GF5_weighted_POINT_C_values"][0])
            self.assertGreaterEqual(z["original_POINT_C_WEIGHTED_zero_mode"],0)
            self.assertLessEqual(z["max_actual_weighted_tail"],
                z["g_independent_original_f_refined_WEIGHTED_error"])
            self.assertLessEqual(z["g_independent_original_f_refined_WEIGHTED_error"],
                z["all_h_uniform_WEIGHTED_point_C_error"])
            self.assertEqual(z["exact_original_class_Walsh"]["C/B"][63],0)
            for x in range(64):
                self.assertEqual(
                    Fraction(z["original_selected_necessary_GF5_weighted_POINT_C_values"][x]),
                    z["exact_degree3_weighted_projection"][x]+
                    z["exact_weighted_point_C_high_order_tail"][x])
            pinned={
                "lex":{
                    "center":612210,"mean":Fraction(5664375,16),
                    "quartic":Fraction(-5415),
                    "tail":Fraction(284445,8),"f_cap":Fraction(12798870)},
                "S72":{
                    "center":86640,"mean":Fraction(1075035,8),
                    "quartic":Fraction(13695,8),
                    "tail":Fraction(197805,8),"f_cap":Fraction(12288435)}
            }[scheme]
            self.assertEqual(z["initial_unchanged_weighted_POINT_C_score"],
                             pinned["center"])
            self.assertEqual(z["original_POINT_C_WEIGHTED_zero_mode"],
                             pinned["mean"])
            self.assertEqual(z["four_packet_point_C_weighted_signed_coefficient"],
                             pinned["quartic"])
            self.assertEqual(z["max_actual_weighted_tail"],pinned["tail"])
            self.assertEqual(z["g_independent_original_f_refined_WEIGHTED_error"],
                             pinned["f_cap"])
            print("AA4BX_W32",scheme,
                  "center",z["initial_unchanged_weighted_POINT_C_score"],
                  "mean",z["original_POINT_C_WEIGHTED_zero_mode"],
                  "fourth",z["four_packet_point_C_weighted_signed_coefficient"],
                  "actual-tail",z["max_actual_weighted_tail"],
                  "f-cap",z["g_independent_original_f_refined_WEIGHTED_error"],flush=True)

    def test_03_independent_direct_signed_Walsh_and_real_opposite_quartic_signs(self):
        out={}
        for scheme in ("lex","S72"):
            z=historical_W32_POINT_C_two_class_sixcube(fixture(1,scheme),PACKETS)
            values=z["original_selected_necessary_GF5_weighted_POINT_C_values"]
            for T in range(64):
                self.assertEqual(z["exact_original_WEIGHTED_point_C_Walsh"][T],
                    independent_signed_walsh_64(values,T))
                if T.bit_count()>=4:
                    self.assertLessEqual(abs(z["exact_original_WEIGHTED_point_C_Walsh"][T]),
                        z["g_independent_original_f_refined_WEIGHTED_error"])
            # First four packet indices; based on separate genuine #594
            # and sibling #595 fourth coefficient evidence.
            # On the SIX-cube, hat(T=first4) AVERAGES the original
            # fourth difference over the OTHER TWO swap bits. Sibling
            # #595's standalone four-cube S72=0 is not the sixcube
            # marginal coefficient (which here is -1/32).
            self.assertEqual(z["exact_original_class_Walsh"]["C/A"][15],
                             {"lex":Fraction(-1,8),"S72":Fraction(-1,32)}[scheme])
            self.assertEqual(z["exact_original_class_Walsh"]["C/B"][15],
                             {"lex":Fraction(0),"S72":Fraction(1,16)}[scheme])
            out[scheme]=z["four_packet_point_C_weighted_signed_coefficient"]
        self.assertEqual(out["lex"],Fraction(-43320,8))
        self.assertEqual(out["S72"],
                         Fraction(-43320,32)+Fraction(49050,16))
        self.assertLess(out["lex"],0)
        self.assertGreater(out["S72"],0)

    def test_04_independent_real_original_W32_full_62370_source_all64_literal_GF5(self):
        model=fixture(1,"S72")
        s,V,a,inc,f,g,_,_=_original_source(model)
        universe=tuple(Q for Q,_ in selected_left_six(model))
        self.assertEqual(len(universe),62370)
        z=historical_W32_POINT_C_two_class_sixcube(model,PACKETS)
        for mask in range(64):
            right=apply_disjoint_factor_swaps(g,PACKETS,
                tuple(j for j in range(6) if mask>>j&1))
            counts=Counter()
            for Q in universe:
                tag=independent_literal_GF5_point_C_class(Q,inc,f,right)
                if tag is not None:counts[tag]+=1
            self.assertEqual(counts["C/A"],
                z["historical_GF5_C_A_and_C_B_counts"]["C/A"][mask])
            self.assertEqual(counts["C/B"],
                z["historical_GF5_C_A_and_C_B_counts"]["C/B"][mask])
            self.assertEqual(43320*counts["C/A"]+49050*counts["C/B"],
                z["original_selected_necessary_GF5_weighted_POINT_C_values"][mask])

    def test_05_real_original_W34_nononto_K14_CB_geometry_and_weight_cap(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            cap=weighted_POINT_C_all_h_certificate(s)
            self.assertGreater(cap["uniform_WEIGHTED_point_C_cubic_remainder"],0)
            cb=original_CB_sixcube_fixed_f_source_tail(model,PACKETS)
            self.assertLessEqual(49050*cb[
                "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],
                cap["uniform_WEIGHTED_point_C_cubic_remainder"])
            changed=dict(model,right_labels=tuple(reversed(g)))
            cb_new=original_CB_sixcube_fixed_f_source_tail(changed,PACKETS)
            self.assertEqual(cb[
                "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"],
                cb_new["fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"])

    def test_06_bad_original_source_injections_and_overlapping_packets_fail_closed(self):
        for s in (0,-2,1,3,5,True):
            with self.assertRaises(ValueError):
                weighted_POINT_C_all_h_certificate(s)
        model=fixture(1,"lex")
        for pairs in (PACKETS[:5],((0,1),(1,2),(3,4),(5,6),(7,8),(9,10))):
            with self.assertRaises(ValueError):
                historical_W32_POINT_C_two_class_sixcube(model,pairs)
        with self.assertRaises(ValueError):
            historical_W32_POINT_C_two_class_sixcube(fixture(2,"lex"),PACKETS)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                historical_W32_POINT_C_two_class_sixcube(bad,PACKETS)

    def test_07_abstract_lowdegree_SIGN_method_blocker_not_true_W3(self):
        values=tuple(1 if x&1 else 0 for x in range(64))
        self.assertEqual(values[0],0)
        self.assertEqual(independent_signed_walsh_64(values,0),Fraction(1,2))
        self.assertTrue(all(independent_signed_walsh_64(values,T)==0
             for T in range(64) if T.bit_count()>=2))
        # This is deliberately NON-W3, not a Branch B counterfamily.
        # The TRUE original W32 sign change in test_03 is stronger.

if __name__=="__main__":
    unittest.main()
