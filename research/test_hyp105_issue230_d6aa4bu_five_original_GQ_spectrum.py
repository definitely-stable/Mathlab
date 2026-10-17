"""AA4-BU genuine original 5-packet GQ and historical GF5 independent tests."""
import unittest
from itertools import product,combinations
from collections import Counter
from math import comb
from fractions import Fraction
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,seven_census
from hyp105_issue230_d6aa4bu_five_original_GQ_spectrum import (
    fifth_order_original_GQ_certificate,
    genuine_original_five_packet_C_geometry,
    true_original_W32_fifth_historical_GF5)
PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9))

def independent_direct_all_original_packet_sixsets(model):
    s,V,a,inc,f,g,_,_=_original_source(model)
    ids=[tuple(i for i,(_,l) in enumerate(inc) if l in pair) for pair in PACKETS]
    total=A=B=0;C=set();leftC=set();pointB=0
    for k in range(5):
        other=[j for j in range(5) if j!=k]
        for pair in combinations(ids[k],2):
            for tail in product(*(ids[j] for j in other)):
                Q=tuple(sorted(pair+tail));total+=1
                pts=Counter(inc[i][0] for i in Q)
                lns=Counter(inc[i][1] for i in Q)
                lp=tuple(sorted(pts.values()))
                rp=tuple(sorted(lns.values()))
                if rp==(1,1,1,1,1,1):A+=1
                elif rp==(1,1,1,1,2):B+=1
                else:raise AssertionError("fifth original right profile malformed")
                if lp==(1,1,1,1,2):pointB+=1
                if lp==(2,2,2):
                    C.add(Q)
                    if len({e for p in pts for e in f[p]})==6:leftC.add(Q)
    return total,A,B,frozenset(C),frozenset(leftC),pointB

class FivePacketOriginal(unittest.TestCase):
    def test_01_all_dyadic_h1_80_integer_exact_right_profiles(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h;d=s+1;z=fifth_order_original_GQ_certificate(s)
            self.assertEqual(z["total_genuine_sixflag_five_packet_sets"],
                             5*comb(2*d,2)*(2*d)**4)
            self.assertEqual(z["exact_original_RIGHT_source_A"],5*d*d*(2*d)**4)
            self.assertEqual(z["exact_original_RIGHT_source_B"],
                             10*comb(d,2)*(2*d)**4)
            self.assertLessEqual(z["original_POINT_source_C_upper"],4800)
            self.assertEqual(set(z["per_seven_historical_GF5_fifth_Walsh_bound"]),
                             set(R3_CERTIFIED_FLOORS))
            for c in ("C/A","C/B"):
                self.assertLessEqual(z["per_seven_historical_GF5_fifth_Walsh_bound"][c],2400)
        for s in (1,3,True):
            with self.assertRaises(ValueError):fifth_order_original_GQ_certificate(s)

    def test_02_all_97200_REAL_W32_source_sets_vs_INDEPENDENT_75_geometry(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            z=fifth_order_original_GQ_certificate(2)
            result=independent_direct_all_original_packet_sixsets(model)
            source=genuine_original_five_packet_C_geometry(model,PACKETS)
            self.assertEqual(result[0],97200)
            self.assertEqual(result[0],z["total_genuine_sixflag_five_packet_sets"])
            self.assertEqual(result[1],z["exact_original_RIGHT_source_A"])
            self.assertEqual(result[2],z["exact_original_RIGHT_source_B"])
            self.assertEqual(result[3],source["source_C"])
            self.assertEqual(result[4],source["physically_left_C"])
            self.assertLessEqual(result[5],z["original_POINT_source_B_upper"])
            self.assertEqual(source["five_times_fifteen_source_C_matchings"],75)
            self.assertLessEqual(source["source_C_count"],4800)
            self.assertTrue(all(len(z)<=4 for z in source["meetings"].values()))

    def test_03_real_original_W34_GF4_nononto_C_intersections(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            g=genuine_original_five_packet_C_geometry(model,PACKETS)
            self.assertLessEqual(g["source_C_count"],4800)
            self.assertLessEqual(g["physically_left_C_count"],4800)
            self.assertEqual(len(g["meetings"]),15)

    def test_04_true_original_W32_fifth_historical_all_seven(self):
        for scheme in ("lex","S72"):
            g=true_original_W32_fifth_historical_GF5(fixture(1,scheme),PACKETS)
            self.assertEqual(g["number_actual_complete_global_right_maps"],32)
            self.assertEqual(set(g["coefficients"]),set(R3_CERTIFIED_FLOORS))
            self.assertLessEqual(abs(g["coefficients"]["C/A"])+abs(g["coefficients"]["C/B"]),
                                 g["geometry"]["exact_physical_C_fifth_Walsh_bound"])
            print("AA4BU_GENUINE_W32_5_SWAP_GF5",scheme,g["coefficients"],flush=True)

    def test_05_FULL_independent_HISTORICAL_seven_census_32_global_maps(self):
        model=fixture(1,"lex")
        original=tuple(model["right_labels"])
        signed=Counter()
        for mask in range(32):
            right=apply_disjoint_factor_swaps(original,PACKETS,
                tuple(i for i in range(5) if mask>>i&1))
            allseven=seven_census(dict(model,right_labels=right),
                                 independent_checks=False)["seven_class_motif_counts"]
            sign=-1 if mask.bit_count()%2 else 1
            for c,n in allseven.items():signed[c]+=sign*n
        local=true_original_W32_fifth_historical_GF5(model,PACKETS)
        self.assertEqual(local["numerators"],{c:signed[c] for c in R3_CERTIFIED_FLOORS})

    def test_06_invalid_true_original_source_packet_guards(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            genuine_original_five_packet_C_geometry(model,PACKETS[:4])
        with self.assertRaises(ValueError):
            genuine_original_five_packet_C_geometry(model,
                ((0,1),(1,2),(3,4),(5,6),(7,8)))
        with self.assertRaises(ValueError):
            true_original_W32_fifth_historical_GF5(fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            true_original_W32_fifth_historical_GF5(model,PACKETS[:4])
if __name__=="__main__":unittest.main()
