"""Independent GENUINE W3 fourth Walsh C/B source/exterior/transversal falsifiers."""
import unittest
from collections import Counter
from itertools import product,combinations
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4bv_fourth_GQ_CB_transversals import (
    fourth_GQ_C_B_source_certificate,
    fourth_original_C_B_true_GQ_geometry,
    exact_W32_fourth_original_GQ_C_B_Walsh,
)

PACKETS=((0,1),(2,3),(4,5),(6,7))


def independently_bruteforce_original_W32_four_packet_CB(model,pairs):
    """Independent one-REAL-incidence anchor per packet + TWO arbitrary flags.

    NO use of line-line intersection or C/B five-LINE-factor
    decomposition: use source point & LINE multiplicity fingerprints
    directly, keep every six ORIGINAL source incidence IDs immutable.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if s!=2:raise ValueError("literal 4packet brute oracle W32 only")
    packets=[tuple(j for j,(p,l) in enumerate(inc) if l in source_pair)
             for source_pair in pairs]
    found=set();checked=0
    for head in product(*packets):
        remaining=tuple(j for j in range(len(inc)) if j not in head)
        for extra in combinations(remaining,2):
            checked+=1
            Q=tuple(sorted((*head,*extra)))
            if (tuple(sorted(Counter(inc[j][0] for j in Q).values()))!=(2,2,2) or
                tuple(sorted(Counter(inc[j][1] for j in Q).values()))!=(1,1,1,1,2)):
                continue
            found.add(Q)
    return frozenset(found),checked


def independently_count_original_GQ_common_transversals(model,A,B):
    """True original source incidence-only; no use of fourth production code."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    neighbors=[set() for _ in range(V)]
    for p,l in inc: neighbors[l].add(p)
    return sum((bool(neighbors[x]&neighbors[A]) and bool(neighbors[x]&neighbors[B]))
               for x in range(V) if x not in (A,B))


class BVOriginalFourthGQ(unittest.TestCase):
    def test_01_all_h_exact_fourth_CB_SOURCE_spectral_cap(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h;d=s+1
            v=fourth_GQ_C_B_source_certificate(s)
            self.assertEqual(v["max_fourth_source_C_B_all_five_LINEs_INSIDE_four_packets"],960)
            self.assertEqual(v["max_fourth_source_C_B_OUTSIDE_repeated_LINE"],96*d)
            self.assertEqual(v["max_fourth_source_C_B_OUTSIDE_singleton_LINE"],
                             192*(2*d-1)*(d-1))
            self.assertEqual(v["max_fourth_source_C_B_original_Q"],
                             960+96*d+192*(2*d-1)*(d-1))
            self.assertEqual(v["max_abs_fourth_original_GF5_C_B_Walsh"],
                             Fraction(v["max_fourth_source_C_B_original_Q"],2))
            self.assertEqual(v["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            self.assertTrue(v["NOT_a_fixed_center_seven_GF5_lower"])
        for n in (0,1,3,5,-2,True):
            with self.assertRaises(ValueError):
                fourth_GQ_C_B_source_certificate(n)

    def test_02_TRUE_W32_fourpacket_source_cartesian_six_Q_matches_GQ_intersections(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            expected,paths=independently_bruteforce_original_W32_four_packet_CB(m,PACKETS)
            z=fourth_original_C_B_true_GQ_geometry(m,PACKETS)
            self.assertEqual(paths,(6**4)*sum(1 for _ in combinations(range(41),2)))
            self.assertEqual(z["real_original_C_B_six_ID_sets"],expected)
            s,V,a,inc,f,g,_,_=_original_source(m)
            physical=frozenset(Q for Q in expected
                if len({u for p in {inc[j][0] for j in Q} for u in f[p]})==6)
            self.assertEqual(z["original_POINT_physical_C_eligible_sets"],physical)
            self.assertEqual(sum(z["source_fourth_C_B_case_counts"].values()),len(expected))
            self.assertEqual(len(expected),269)
            self.assertEqual(z["source_fourth_C_B_case_counts"],
                             {"inside":47,"outside_singleton":181,"outside_repeated":41})
            self.assertEqual(len(physical),{"lex":2,"S72":6}[scheme])
            print("AA4BV_W32_CB",scheme,
                  "raw",len(expected),"physical",len(physical),
                  "cases",z["source_fourth_C_B_case_counts"],flush=True)

    def test_03_real_W32_and_W34_GQ_TRANSVERSAL_d_property_by_two_lines(self):
        for model in (fixture(1,"lex"),fixture(2,"lex"),fixture(2,"random")):
            s,V,a,inc,f,g,_,_=_original_source(model)
            byline=[set() for _ in range(V)]
            for p,l in inc:byline[l].add(p)
            checked=0
            for i in range(V):
                for j in range(i+1,V):
                    if V>30 and (i+j)%7!=0:continue
                    n=independently_count_original_GQ_common_transversals(model,i,j)
                    self.assertLessEqual(n,s+1)
                    if byline[i]&byline[j]:
                        self.assertEqual(n,s-1)
                    else:
                        self.assertEqual(n,s+1)
                    checked+=1
            self.assertGreater(checked,100)

    def test_04_true_original_W34_GF4_NONONTO_K14_four_packet_C_B_exterior(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            geo=fourth_original_C_B_true_GQ_geometry(model,PACKETS)
            s,V,a,inc,f,g,_,_=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            self.assertLessEqual(geo["source_fourth_C_B_count"],
                                 fourth_GQ_C_B_source_certificate(s)[
                                 "max_fourth_source_C_B_original_Q"])
            self.assertEqual(geo["source_fourth_C_B_case_counts"],
                             {"outside_singleton":992,"outside_repeated":112})
            for Q in geo["real_original_C_B_six_ID_sets"]:
                self.assertEqual(len(Q),6)
                self.assertEqual(len(set(Q)),6)
                self.assertEqual(tuple(sorted(Counter(inc[j][0] for j in Q).values())),
                                 (2,2,2))
                self.assertEqual(tuple(sorted(Counter(inc[j][1] for j in Q).values())),
                                 (1,1,1,1,2))
            print("AA4BV_W34_CB",scheme,geo["source_fourth_C_B_case_counts"],flush=True)

    def test_05_true_W32_full16_complete_global_hist_GF5_fourth_cube(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            z=exact_W32_fourth_original_GQ_C_B_Walsh(m,PACKETS)
            self.assertEqual(z["real_W32_full_original_global_LINE_maps"],16)
            self.assertLessEqual(
                abs(z["fourth_true_original_GF5_class_Walsh_coefficients"]["C/B"]),
                z["exact_original_source_C_B_intersections"][
                    "refined_abs_original_C_B_fourth_Walsh"])
            pinned={
                "lex":{"D6":Fraction(0),"B-left/A-right":Fraction(1,4),
                       "A-left/B-right":Fraction(3,16),"C/A":Fraction(-1,8),
                       "C/B":Fraction(0),"B/B-overlap":Fraction(-1,8),
                       "B/B-disjoint":Fraction(1,16)},
                "S72":{"D6":Fraction(0),"B-left/A-right":Fraction(3,8),
                       "A-left/B-right":Fraction(-5,16),"C/A":Fraction(0),
                       "C/B":Fraction(1,16),"B/B-overlap":Fraction(1,16),
                       "B/B-disjoint":Fraction(1,8)}
            }
            self.assertEqual(z["fourth_true_original_GF5_class_Walsh_coefficients"],
                             pinned[scheme])
            print("AA4BV_W32_FOURTH_WALSH",scheme,
                  z["fourth_true_original_GF5_class_Walsh_coefficients"],flush=True)

    def test_06_separate_all_SEVEN_original_GF5_full16_map_census(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        Qs=tuple(Q for Q,_ in selected_left_six(model))
        self.assertEqual(len(Qs),62370)
        nums=Counter()
        for mask in range(16):
            images=apply_disjoint_factor_swaps(g,PACKETS,
                tuple(i for i in range(4) if mask>>i&1))
            sign=-1 if mask.bit_count()%2 else 1
            for Q in Qs:
                tag=classify_seven_prechecked(Q,f,images,inc)
                if tag is not None:nums[tag]+=sign
        subset=exact_W32_fourth_original_GQ_C_B_Walsh(model,PACKETS)
        self.assertEqual({c:nums[c] for c in R3_CERTIFIED_FLOORS},
            subset["fourth_true_original_GF5_class_Walsh_numerators"])

    def test_07_invalid_original_LINE_packets_and_injections_fail_closed(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            fourth_original_C_B_true_GQ_geometry(model,PACKETS[:3])
        with self.assertRaises(ValueError):
            fourth_original_C_B_true_GQ_geometry(model,
                ((0,1),(1,2),(3,4),(5,6)))
        with self.assertRaises(ValueError):
            exact_W32_fourth_original_GQ_C_B_Walsh(fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            exact_W32_fourth_original_GQ_C_B_Walsh(model,PACKETS[:3])
        with self.assertRaises(ValueError):
            fourth_original_C_B_true_GQ_geometry(
                dict(model,left_labels=((0,1),)*15),PACKETS)
        with self.assertRaises(ValueError):
            fourth_original_C_B_true_GQ_geometry(
                dict(model,incidences=model["incidences"][:-1]),PACKETS)

if __name__=="__main__":
    unittest.main()
