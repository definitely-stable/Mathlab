"""AA4-BV-C/A: real GQ fourth source anchors vs independent entire six-ID Q."""
import unittest
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4bv_fourth_original_GQ_CA_anchors import (
    fourth_order_true_original_POINT_C_certificate,
    actual_original_four_packet_C_anchor_identity,
    true_original_W32_fourth_CA_GF5_Walsh,
)
PACKETS=((0,1),(2,3),(4,5),(6,7))

def independent_original_W32_four_packet_C_brute(model,pairs):
    """1,062,720 original genuine six-source-ID anchor+two-other combinations."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    assert s==2
    packet_rows=[tuple(i for i,(p,l) in enumerate(inc) if l in pair)
                 for pair in pairs]
    entire=set(range(len(inc)))
    unique=set();physical=set()
    traversed=0
    for anchor in product(*packet_rows):
        remaining=sorted(entire-set(anchor))
        for extra in combinations(remaining,2):
            traversed+=1
            Q=tuple(sorted(anchor+extra))
            counts=Counter(inc[i][0] for i in Q)
            if tuple(sorted(counts.values()))!=(2,2,2):continue
            unique.add(Q)
            if len({z for p in counts for z in f[p]})==6:
                physical.add(Q)
    return traversed,frozenset(unique),frozenset(physical)

class OriginalGQFourthCA(unittest.TestCase):
    def test_01_genuine_all_dyadic_h1_to80_degree_five_source_C_bound(self):
        for h in tuple(range(1,38))+(40,48,64,80):
            s=1<<h;d=s+1
            x=fourth_order_true_original_POINT_C_certificate(s)
            self.assertEqual(x["POINT_C_true_original_sixflag_upper_by_211"],
                96*d*d*(d-1)**2)
            self.assertEqual(x["POINT_C_true_original_sixflag_upper_by_22"],
                48*((s+1)*(s*s+1)-2)*comb(d,2))
            self.assertEqual(x["historical_GF5_C_A_fourth_Walsh_abs_upper"]*2,
                x["POINT_C_true_original_sixflag_upper_total"])
            self.assertTrue(x["right_SOURCE_LINE_C_impossible_at_fourth_order"])
        for s in (1,3,True,8.0):
            with self.assertRaises(ValueError):
                fourth_order_true_original_POINT_C_certificate(s)

    def test_02_real_W32_independent_BRUTE_all_Q_and_anchored_inverse_weight(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            geo=actual_original_four_packet_C_anchor_identity(model,PACKETS)
            traversed,allQ,physical=independent_original_W32_four_packet_C_brute(model,PACKETS)
            self.assertEqual(traversed,6**4*comb(41,2))
            self.assertEqual(geo["genuine_original_POINT_C_source_Q"],allQ)
            self.assertEqual(geo["fixed_LEFT_physically_eligible_original_POINT_C_Q"],physical)
            self.assertEqual(geo["multiplicity_corrected_original_Q_count"],len(allQ))
            self.assertEqual(len(allQ),1059)
            self.assertEqual(len(physical),{"lex":31,"S72":47}[scheme])
            self.assertEqual(
              geo["source_right_class_counts"],
              {"C/A":781,"C/B":269,"NOT_GF5":9})
            self.assertLessEqual(geo["original_anchor_profile_211_count"],96*3*3)
            self.assertLessEqual(geo["original_anchor_profile_22_count"],48)
            self.assertLessEqual(len(allQ),
              fourth_order_true_original_POINT_C_certificate(2)[
                "POINT_C_true_original_sixflag_upper_total"])
            print("AA4BV_TRUE_W32_SOURCE_C",scheme,len(allQ),len(physical),
                  geo["source_right_class_counts"],flush=True)

    def test_03_REAL_original_W34_GF4_source_C_and_anchored_loads(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            geo=actual_original_four_packet_C_anchor_identity(model,PACKETS)
            self.assertEqual(geo["s"],4)
            self.assertEqual(geo["multiplicity_corrected_original_Q_count"],
                             len(geo["genuine_original_POINT_C_source_Q"]))
            self.assertLessEqual(geo["original_anchor_profile_22_count"],48)
            self.assertLessEqual(len(geo["genuine_original_POINT_C_source_Q"]),
              fourth_order_true_original_POINT_C_certificate(4)[
                "POINT_C_true_original_sixflag_upper_total"])

    def test_04_true_original_W32_six_id_C_A_C_B_hist_GF5_16global_maps(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            x=true_original_W32_fourth_CA_GF5_Walsh(model,PACKETS)
            self.assertEqual(x["16_COMPLETE_globally_injected_original_right_maps"],16)
            self.assertEqual(
              (x["historical_original_C_A_fourth_Walsh"],
               x["historical_original_C_B_fourth_Walsh"]),
              {"lex":(Fraction(-1,8),Fraction(0)),
               "S72":(Fraction(0),Fraction(1,16))}[scheme])
            self.assertLessEqual(abs(x["historical_original_C_A_fourth_Walsh"]),
                x["source_genuine_original_C_Q_geometry"][
                "historical_C_A_fourth_Walsh_source_cap_from_actual_f"])
            print("AA4BV_TRUE_W32_GF5_C_A",scheme,
                  x["historical_original_C_A_fourth_Walsh"],
                  "C_B",x["historical_original_C_B_fourth_Walsh"],flush=True)

    def test_05_independent_FULL_original_W32_historical_seven_census_x16(self):
        model=fixture(1,"lex")
        original=tuple(model["right_labels"])
        num=Counter()
        for mask in range(16):
            right=apply_disjoint_factor_swaps(original,PACKETS,
                  tuple(i for i in range(4) if mask>>i&1))
            state=seven_census(dict(model,right_labels=right),
                               independent_checks=False)["seven_class_motif_counts"]
            sign=(-1 if mask.bit_count()%2 else 1)
            for c in ("C/A","C/B"):
                num[c]+=sign*state[c]
        actual=true_original_W32_fourth_CA_GF5_Walsh(model,PACKETS)
        self.assertEqual(num["C/A"],actual["historical_original_C_A_fourth_Walsh_numerator"])
        self.assertEqual(num["C/B"],actual["historical_original_C_B_fourth_Walsh_numerator"])

    def test_06_original_source_packet_malformed_guards(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            actual_original_four_packet_C_anchor_identity(model,PACKETS[:3])
        with self.assertRaises(ValueError):
            actual_original_four_packet_C_anchor_identity(model,
                  ((0,1),(1,2),(3,4),(5,6)))
        with self.assertRaises(ValueError):
            true_original_W32_fourth_CA_GF5_Walsh(fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            true_original_W32_fourth_CA_GF5_Walsh(model,PACKETS[:3])

if __name__=="__main__":unittest.main()
