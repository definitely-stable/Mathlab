"""AA4-CD independent original signed seven-GF5 one-sided geometry bounds."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cb_original_parity_affine_center import (
    genuine_original_Q_parity_sixcube,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,
)
from hyp105_issue230_d6aa4cd_one_sided_original_center import (
    one_sided_signed_support_certificate,
    true_original_W32_one_sided_f_g_seven_center,
    true_original_W32_signed_seven_center_lower,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,R3_CERTIFIED_FLOORS,
)

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def independent_unrestricted_sign_bound(support,k,center):
    """Literal sum and exact supportwise indicator extrema, not new helper."""
    K=high_degree_boolean_kernel(k)
    signed=(K[center^y] for y in support)
    pos=0;neg=0
    for v in signed:
        if v>0:pos+=v
        if v<0:neg-=v
    return Fraction(neg,1<<k),Fraction(pos,1<<k)


class TrueOriginalGF5OneSidedCenter(unittest.TestCase):
    def test_01_exact_support_signed_bounds_exhaustive_4bit_boolean(self):
        k=4
        for support_mask in range(1<<16):
            support=tuple(i for i in range(16) if support_mask>>i&1)
            for center in (0,7,15):
                z=one_sided_signed_support_certificate(support,k,center)
                neg,pos=independent_unrestricted_sign_bound(support,k,center)
                self.assertEqual((z["minus"],z["plus"]),(neg,pos))
        for k in (5,6):
            K=high_degree_boolean_kernel(k)
            supports=(
                tuple(),
                tuple(range(1<<k)),
                tuple(i for i in range(1<<k) if i.bit_count()%2==0),
                tuple(i for i in range(1<<k) if K[i]<0),
                tuple(i for i in range(1<<k) if K[i]>0),
            )
            for S in supports:
                for x in range(1<<k):
                    a=one_sided_signed_support_certificate(S,k,x)
                    self.assertEqual((a["minus"],a["plus"]),
                                     independent_unrestricted_sign_bound(S,k,x))
        for k in range(4):
            self.assertEqual(one_sided_signed_support_certificate(
                (),k,0)["minus"],0)

    def test_02_actual_original_W32_Q_historical_signed_indicator_inside_screen(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            seen=0;nonzero=0
            for Q,_ in selected_left_six(model):
                if seen>=24:break
                data=genuine_original_Q_parity_sixcube(
                    model,Q,PACKETS,verify_historical=True)
                k=len(data["touched_original_LINE_packet_indices"])
                if k<4:continue
                used=data["touched_original_LINE_packet_indices"]
                for key in ("parity_zero_affine_coset",
                            "physical_right_2regular_states"):
                    S=data[key]
                    for center in range(1<<k):
                        en=one_sided_signed_support_certificate(S,k,center)
                        K=high_degree_boolean_kernel(k)
                        accepted=data["historically_accepted_original_GF5_states"]
                        actual=Fraction(sum(K[center^y] for y in accepted),1<<k)
                        self.assertLessEqual(-en["minus"],actual)
                        self.assertLessEqual(actual,en["plus"])
                if data["historically_accepted_original_GF5_states"]:
                    nonzero+=1
                seen+=1
            self.assertEqual(seen,24)

    def test_03_original_W32_all_seven_one_sided_f_g_errors(self):
        for scheme in ("lex","S72"):
            x=true_original_W32_one_sided_f_g_seven_center(
                fixture(1,scheme),PACKETS)
            E=x["unchanged_full_g_conditioned_one_sided_GF5_seven_envelopes"]
            old=x["prior_two_sided_original_g_conditioned"]
            self.assertEqual(x["s"],2)
            self.assertGreater(x["actual_original_Q_with_k_ge4"],30000)
            self.assertLessEqual(E["right_2factor_minus_center"],
                                 E["parity_minus_center"])
            self.assertLessEqual(E["right_2factor_plus_center"],
                                 E["parity_plus_center"])
            self.assertLessEqual(E["right_2factor_minus_center"],
                                 old["right_2factor_original_center"])
            self.assertLessEqual(E["parity_minus_center"],
                                 old["parity_original_center"])
            self.assertLessEqual(E["right_2factor_minus_uniform"],
                                 E["right_2factor_minus_uniform"])
            self.assertTrue(x["right_historical_GF5_classifier_used_for_support"]==False)
            print("AA4CD_W32",scheme,"Q",x["actual_original_Q_with_k_ge4"],
                  "old_abs_center",old["right_2factor_original_center"],
                  "new_neg_center",E["right_2factor_minus_center"],
                  "new_pos_center",E["right_2factor_plus_center"],
                  "parity_neg",E["parity_minus_center"],flush=True)

    def test_04_full_original_64map_historical_seven_GF5_center_direct_oracle(self):
        for scheme in ("lex","S72"):
            z=true_original_W32_signed_seven_center_lower(
                fixture(1,scheme),PACKETS)
            self.assertTrue(z["all_64_complete_right_global_maps_one_sided_verified"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            self.assertLessEqual(z["new_one_sided_negative_error"],
                                 z["prior_absolute_right_2factor_error"])
            self.assertGreaterEqual(z["new_certified_UNCHANGED_seven_GF5_weighted_lower"],0)
            self.assertLessEqual(z["new_certified_UNCHANGED_seven_GF5_weighted_lower"],
                                 z["original_UNCHANGED_seven_GF5_weighted_count"])
            self.assertEqual(z["original_UNCHANGED_seven_GF5_weighted_count"],
                             {"lex":11225795,"S72":3283610}[scheme])
            print("AA4CD_ORIGINAL_CENTER",scheme,
                  "weighted_actual",z["original_UNCHANGED_seven_GF5_weighted_count"],
                  "low",z["historical_zero_through_third_signed_projection"],
                  "negative_only_E",z["new_one_sided_negative_error"],
                  "certified_positive_floor",z[
                      "new_certified_UNCHANGED_seven_GF5_weighted_lower"],
                  flush=True)

    def test_05_adversarial_complete_g_reversal_and_original_f_hold(self):
        m=fixture(1,"lex")
        alternative=dict(m,right_labels=tuple(reversed(m["right_labels"])))
        for model in (m,alternative):
            x=true_original_W32_one_sided_f_g_seven_center(model,PACKETS)
            E=x["unchanged_full_g_conditioned_one_sided_GF5_seven_envelopes"]
            self.assertLessEqual(E["right_2factor_minus_center"],
                                 x["prior_two_sided_original_g_conditioned"][
                                     "right_2factor_original_center"])
        self.assertEqual(set(m["right_labels"]),set(alternative["right_labels"]))

    def test_06_true_original_W34_GF4_nononto_K14_signed_source_screen(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            s,V,a,inc,f,g,_,_=_original_source(m)
            self.assertEqual((s,V,a),(4,85,14))
            Q=tuple(tuple(j for j,(p,l) in enumerate(inc) if l==line)[0]
                    for line in (0,2,4,6,8,10))
            z=genuine_original_Q_parity_sixcube(m,Q,PACKETS,
                                                 verify_historical=False)
            for key in ("parity_zero_affine_coset",
                        "physical_right_2regular_states"):
                S=z[key]
                for center in range(64):
                    bounds=one_sided_signed_support_certificate(S,6,center)
                    self.assertEqual((bounds["minus"],bounds["plus"]),
                         independent_unrestricted_sign_bound(S,6,center))
                self.assertLessEqual(len(S),64)

    def test_07_invalid_support_and_local_centers_fail_closed(self):
        for support,k,center in [
            ((0,0),4,0),((16,),4,0),((-1,),4,0),
            ((1,),7,0),((1,),-1,0),((1,),4,16),
            ((1,),4,-1),((1,),4,True),
        ]:
            with self.assertRaises(ValueError):
                one_sided_signed_support_certificate(support,k,center)
        with self.assertRaises(ValueError):
            true_original_W32_one_sided_f_g_seven_center(
                fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            true_original_W32_one_sided_f_g_seven_center(
                fixture(1,"lex"),PACKETS[:5])

if __name__=="__main__":
    unittest.main()
