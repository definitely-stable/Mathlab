"""AA4-BT exact true-original W3 source LINE-packet intersection falsifiers."""
import unittest
from collections import Counter
from itertools import product,combinations
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_issue230_d6aa4bt_gq_sixth_order_intersections import (
    SIXTH_ALLOWED,SIXTH_FORBIDDEN,
    exact_original_sixflag_packet_hit_count,
    sixth_order_original_GQ_class_certificate,
    genuine_original_six_packet_geometry,
    exact_W32_sixth_historical_class_Walsh,
)

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))

def independent_full_true_original_six_packet_product(model,pairs):
    """Different oracle: direct product of SIX authentic original line-pair flag packets."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    byline=[[] for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        byline[l].append(j)
    packets=[tuple(j for l in pair for j in byline[l]) for pair in pairs]
    C=set()
    eligible=set()
    B=set()
    types=Counter()
    for six in product(*packets):
        points=tuple(inc[j][0] for j in six)
        pcounts=tuple(sorted(Counter(points).values()))
        lines=tuple(inc[j][1] for j in six)
        assert len(set(lines))==6
        types[pcounts]+=1
        Q=tuple(sorted(six))
        if pcounts==(2,2,2):
            C.add(Q)
            distinct={inc[j][0] for j in Q}
            if len(set(z for p in distinct for z in f[p]))==6:
                eligible.add(Q)
        if pcounts==(1,1,1,1,2):
            B.add(Q)
    return dict(C=frozenset(C),eligible=frozenset(eligible),
                B=frozenset(B),types=types,total=sum(types.values()))

class BTGQSixthOrder(unittest.TestCase):
    def test_01_all_dyadic_orders_exact_PACKET_inclusion_exclusion_vs_old_cap(self):
        for h in tuple(range(1,37))+(40,48,64,80):
            s=1<<h;d=s+1;M=(s+1)**2*(s*s+1)
            z=sixth_order_original_GQ_class_certificate(s)
            self.assertEqual(z["sixth_order_original_sixflag_packet_capacity"],(2*d)**6)
            self.assertLessEqual(z["maximum_original_POINT_profile_C_source_Q"],960)
            self.assertEqual(z["per_historical_seven_class_sixth_Walsh_absolute_upper"]["C/A"],480)
            for tag in SIXTH_FORBIDDEN:
                self.assertEqual(z["per_historical_seven_class_sixth_Walsh_absolute_upper"][tag],0)
            self.assertEqual(z["per_historical_seven_class_sixth_Walsh_absolute_upper"]["B-left/A-right"],
                             Fraction(min((2*d)**6,60*(2*d)**4),2))
            for t in range(0,8):
                x=exact_original_sixflag_packet_hit_count(s,t)
                if t==0:self.assertEqual(x,comb(M,6))
                if t==6:self.assertEqual(x,(2*d)**6)
                if t==7:self.assertEqual(x,0)
                if 1<=t<=6:
                    prior=min(comb(M,6),(2*d)**t*comb(M-t,6-t))
                    self.assertLessEqual(x,prior)
        for s,t in ((1,1),(3,2),(4,-1),(2,8),(True,3),(2,True)):
            with self.assertRaises(ValueError):
                exact_original_sixflag_packet_hit_count(s,t)

    def test_02_true_symplectic_W32_independent_all_6pow6_original_incidence_Q(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            geo=genuine_original_six_packet_geometry(model,PACKETS)
            oracle=independent_full_true_original_six_packet_product(model,PACKETS)
            self.assertEqual(oracle["total"],6**6)
            self.assertEqual(geo["source_C_sixflag_sets"],oracle["C"])
            self.assertEqual(geo["fixed_LEFT_physical_C_eligible_original_sixflag_sets"],
                             oracle["eligible"])
            self.assertLessEqual(len(oracle["C"]),960)
            self.assertLessEqual(geo["historical_C_A_sixth_Walsh_bound_refined"],
                                 Fraction(960,2))
            self.assertEqual(geo["number_perfect_packet_matchings"],15)
            for choices in geo["pair_packet_common_point_matchings"].values():
                self.assertLessEqual(len(choices),4)
            self.assertLessEqual(len(oracle["B"]),60*6**4)

    def test_03_genuine_W34_GF4_nononto_original_geometry_NO_fake_large_W3(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            geo=genuine_original_six_packet_geometry(model,PACKETS)
            self.assertEqual(geo["s"],4)
            self.assertEqual(geo["original_incidence_flag_packet_sizes"],(10,)*6)
            self.assertLessEqual(geo["source_C_count"],960)
            self.assertLessEqual(geo["fixed_LEFT_physical_C_eligible_count"],960)
            for choices in geo["pair_packet_common_point_matchings"].values():
                self.assertLessEqual(len(choices),4)

    def test_04_true_W32_historical_all_SEVEN_GF5_exact_sixth_hadamard(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            x=exact_W32_sixth_historical_class_Walsh(model,PACKETS)
            self.assertEqual(x["full_globally_injected_original_LINE_maps"],64)
            self.assertEqual(x["real_W32_sixth_sensitive_left_sixflag_count"],
                             sum(x["original_sixth_sensitive_Q_by_source_class"].values()))
            for tag in SIXTH_FORBIDDEN:
                self.assertEqual(x["sixth_historical_seven_GF5_Walsh_coefficients"][tag],0)
            self.assertLessEqual(abs(x["sixth_historical_seven_GF5_Walsh_coefficients"]["C/A"]),
                                 x["exact_original_GQ_C_intersection_certificate"][
                                     "historical_C_A_sixth_Walsh_bound_refined"])
            print("AA4BT_W32_SIXTH_CLASS_COEFFICIENTS",scheme,
                  x["sixth_historical_seven_GF5_Walsh_coefficients"],
                  "SENSITIVE_SOURCE_TYPES",x["original_sixth_sensitive_Q_by_source_class"],
                  flush=True)

    def test_05_original_TRUE_W32_sixth_class_AGREES_full64_GLOBAL_maps_independent_census(self):
        # Classify ALL real left physical original six-ID Q separately
        # across ALL 64 complete original opposite global maps, not only
        # those already known to be sixth-sensitive.
        # This is an independent full-count falsifier (more expensive).
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
        rows=tuple(Q for Q,_ in selected_left_six(model))
        count={c:0 for c in R3_CERTIFIED_FLOORS}
        for mask in range(64):
            state=apply_disjoint_factor_swaps(g,PACKETS,
                tuple(i for i in range(6) if mask>>i&1))
            signs=(-1 if mask.bit_count()%2 else 1)
            for Q in rows:
                tag=classify_seven_prechecked(Q,f,state,inc)
                if tag is not None:
                    count[tag]+=signs
        sliced=exact_W32_sixth_historical_class_Walsh(model,PACKETS)
        self.assertEqual(count,sliced["sixth_historical_seven_GF5_Walsh_numerators"])

    def test_06_invalid_source_six_packet_scope_and_repeated_factor_guards(self):
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            genuine_original_six_packet_geometry(model,PACKETS[:5])
        with self.assertRaises(ValueError):
            genuine_original_six_packet_geometry(model,
                ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10)))
        with self.assertRaises(ValueError):
            exact_W32_sixth_historical_class_Walsh(fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            exact_W32_sixth_historical_class_Walsh(model,PACKETS[:5])
        with self.assertRaises(ValueError):
            sixth_order_original_GQ_class_certificate(3)
        self.assertEqual(exact_original_sixflag_packet_hit_count(2,7),0)
if __name__=="__main__":
    unittest.main()
