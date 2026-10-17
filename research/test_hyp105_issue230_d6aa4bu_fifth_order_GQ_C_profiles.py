"""Independent exact real-original 5packet C/B matching and Walsh falsifiers."""
import unittest
from collections import Counter
from itertools import product,combinations
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4bu_fifth_order_GQ_C_profiles import (
    fifth_order_original_GQ_C_certificate,
    original_five_packet_C_B_geometry,
    independent_fifth_original_W32_GF5,
)
PAIRS=((0,1),(2,3),(4,5),(6,7),(8,9))


def independent_cartesian_five_packet_C_Q(model,pairs):
    """Completely separate W32 brute 5 anchor flags + ONE sixth free flag.

    Unlike production original GQ line-intersection enumeration, this
    oracle does not use any GQ line intersection geometrical routine.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if s!=2:raise ValueError("brute packet product limited to TRUE W32")
    packet=[tuple(j for j,(p,l) in enumerate(inc) if l in pair) for pair in pairs]
    cA=set();cB=set()
    for anchored in product(*packet):
        for extra in range(len(inc)):
            if extra in anchored:continue
            Q=tuple(sorted((*anchored,extra)))
            if len(set(Q))!=6:continue
            p=tuple(sorted(Counter(inc[j][0] for j in Q).values()))
            if p!=(2,2,2):continue
            l=tuple(sorted(Counter(inc[j][1] for j in Q).values()))
            if l==(1,1,1,1,1,1):cA.add(Q)
            elif l==(1,1,1,1,2):cB.add(Q)
    return {"C/A":frozenset(cA),"C/B":frozenset(cB)}


class BUTrueOriginalFifthGQ(unittest.TestCase):
    def test_01_all_h_exact_fifth_source_C_A_quadratic_and_C_B_constant(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h;d=s+1
            z=fifth_order_original_GQ_C_certificate(s)
            self.assertEqual(z["max_actual_original_C_A_Q_touching_ALL_five_packets"],
                             480*d*(d-1))
            self.assertEqual(z["max_actual_original_C_B_Q_touching_ALL_five_packets"],960)
            self.assertEqual(z["max_abs_fifth_Walsh_original_C_A"],240*d*(d-1))
            self.assertEqual(z["max_abs_fifth_Walsh_original_C_B"],480)
            self.assertTrue(z["source_class_CAP_is_not_a_FIXED_MAP_acceptance_lower"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        for val in (1,3,0,-1,True,4+1):
            if val==4+1:continue
            with self.assertRaises(ValueError):
                fifth_order_original_GQ_C_certificate(val)

    def test_02_true_original_W32_independent_five_source_packet_flag_product(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            geo=original_five_packet_C_B_geometry(model,PAIRS)
            oracle=independent_cartesian_five_packet_C_Q(model,PAIRS)
            self.assertEqual(geo["original_C_B_Q_source_flag_sets"],oracle["C/B"])
            self.assertLessEqual(len(oracle["C/A"]),480*3*2)
            self.assertLessEqual(len(oracle["C/B"]),960)
            self.assertEqual(geo["number_source_C_B"],len(oracle["C/B"]))
            s,V,a,inc,f,g,_,_=_original_source(model)
            physical={Q for Q in oracle["C/B"] if len({
                u for p in {inc[j][0] for j in Q} for u in f[p]})==6}
            self.assertEqual(geo["original_C_B_fixed_POINT_physical_eligible_sets"],
                             physical)
            print("AA4BU_W32_fifth_C",scheme,
                  "C/A",len(oracle["C/A"]),"C/B",len(oracle["C/B"]),
                  "left_physical_C_B",len(physical),flush=True)

    def test_03_original_W34_GF4_NONONTO_real_packet_intersections(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            geo=original_five_packet_C_B_geometry(model,PAIRS)
            self.assertEqual((geo["s"],geo["V"]),(4,85))
            self.assertLessEqual(geo["number_source_C_B"],960)
            self.assertLessEqual(geo["number_FIXED_LEFT_physical_eligible_C_B"],960)
            s,V,a,inc,f,g,_,_=_original_source(model)
            for Q in geo["original_C_B_Q_source_flag_sets"]:
                self.assertEqual(tuple(sorted(Counter(inc[j][0] for j in Q).values())),
                                 (2,2,2))
                self.assertEqual(tuple(sorted(Counter(inc[j][1] for j in Q).values())),
                                 (1,1,1,1,2))
                self.assertEqual(len({inc[j][1] for j in Q}),5)
                self.assertEqual(len(Q),6)

    def test_04_true_original_W32_32_GLOBAL_maps_historical_fifth_class(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            z=independent_fifth_original_W32_GF5(model,PAIRS)
            self.assertEqual(z["true_W32_original_32_complete_LINE_maps"],32)
            geom=z["exact_true_original_GQ_C_B_line_matching"]
            self.assertLessEqual(abs(z["original_fifth_class_Walsh_coefficients"]["C/B"]),
                                 geom["refined_fifth_C_B_Walsh_upper"])
            c=fifth_order_original_GQ_C_certificate(2)
            self.assertLessEqual(abs(z["original_fifth_class_Walsh_coefficients"]["C/A"]),
                                 c["max_abs_fifth_Walsh_original_C_A"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            print("AA4BU_W32_GF5_fifth",scheme,
                  z["original_fifth_class_Walsh_coefficients"],flush=True)

    def test_05_fifth_independent_complete_GF5_census_not_packet_only(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        nums=Counter()
        rows=tuple(Q for Q,_ in selected_left_six(model))
        self.assertEqual(len(rows),62370)
        for mask in range(32):
            state=apply_disjoint_factor_swaps(
                g,PAIRS,tuple(i for i in range(5) if mask>>i&1))
            sign=(-1 if mask.bit_count()%2 else 1)
            for Q in rows:
                tag=classify_seven_prechecked(Q,f,state,inc)
                if tag is not None:nums[tag]+=sign
        z=independent_fifth_original_W32_GF5(model,PAIRS)
        self.assertEqual({c:nums[c] for c in R3_CERTIFIED_FLOORS},
                         z["original_fifth_class_Walsh_numerators"])

    def test_06_invalid_packet_and_true_source_fails_closed(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            original_five_packet_C_B_geometry(model,PAIRS[:4])
        with self.assertRaises(ValueError):
            original_five_packet_C_B_geometry(model,
                ((0,1),(1,2),(3,4),(5,6),(7,8)))
        with self.assertRaises(ValueError):
            independent_fifth_original_W32_GF5(fixture(2,"lex"),PAIRS)
        with self.assertRaises(ValueError):
            independent_fifth_original_W32_GF5(model,PAIRS[:4])
        with self.assertRaises(ValueError):
            original_five_packet_C_B_geometry(
                dict(model,right_labels=((0,1),)*15),PAIRS)

if __name__=="__main__":
    unittest.main()
