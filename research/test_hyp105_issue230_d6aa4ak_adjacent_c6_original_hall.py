"""Independent original symplectic W32/W34/W38 adjacent C6 Hall and 12-channel tests."""
import unittest
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,full_original_W32_sector_certificate,
    single_original_A_sector_permanent,classify_physical_A_twofactor)
from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
    exact_original_connected_C6_transfer)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    pinned_twofactor_completions)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)
from hyp105_issue230_d6aa4ak_adjacent_c6_original_hall import (
    edge,adjacent_pin_vertices,exact_adjacent_C6_original_transfer,
    independent_complete_physical_adjacent_C6_oracle,
    adjacent_low_hole_occupied_C6_all_h,adjacent_original_rootpair)


class GenuineOriginalAdjacentC6Hall(unittest.TestCase):
    def test_01_all_K6_K7_K8_adjacent_pins_have_unique_oriented_C6_paths(self):
        for a in (6,7,8):
            for e0,e1 in combinations(tuple(combinations(range(a),2)),2):
                if not set(e0)&set(e1):continue
                u,v,w=adjacent_pin_vertices((e0,e1))
                expected=set()
                for alpha,mid,gamma in permutations(
                    tuple(x for x in range(a) if x not in (u,v,w)),3):
                    H=frozenset((e0,e1,edge(w,alpha),edge(alpha,mid),
                                 edge(mid,gamma),edge(gamma,v)))
                    self.assertEqual(
                        classify_physical_A_twofactor(tuple(H),(e0,e1)),
                        "connected_C6")
                    expected.add(H)
                actual={frozenset(H) for H in
                        pinned_twofactor_completions(e0,e1,a)
                        if classify_physical_A_twofactor(H,(e0,e1))=="connected_C6"}
                self.assertEqual(actual,expected)
                self.assertEqual(len(expected),(a-3)*(a-4)*(a-5))

    def test_02_full_true_W32_lex_reverse_S68_S72_and_zero_split_two_types(self):
        ms=[zero_split_original_W32()]+[
            fixture(1,name) for name in ("lex","reverse","S68","S72")]
        for index,m in enumerate(ms):
            for side in (0,1):
                accepted=physical=0
                for root in range(15):
                    for flag in range(3):
                        for four in occupied_root_C4_source_factors(
                                m,side=side,root=root):
                            fast=exact_adjacent_C6_original_transfer(
                                m,side=side,root=root,
                                pair_offset=flag,four=four)
                            slow=independent_complete_physical_adjacent_C6_oracle(
                                m,side=side,root=root,
                                pair_offset=flag,four=four)
                            self.assertEqual(
                                fast["accepted_actual_original_six_Q"],
                                slow["accepted_original_Q"])
                            if fast["adjacent"]:
                                accepted+=fast["accepted_actual_original_six_Q"]
                                physical+=slow["occupied_C6"]
                                self.assertEqual(len(fast["channel_results"]),12)
                                self.assertEqual(
                                    slow["accepted_original_Q"],
                                    slow["Hall_positive_C6"]+
                                    slow["real_original_C8_extra"])
                full=full_original_W32_sector_certificate(m,side=side)
                self.assertLessEqual(
                    accepted,full["original_GF5_A_accepted_by_sector"]["connected_C6"])
                # Eight independent strict true-ORIGINAL W32 checks,
                # including the special two-typed split-triangle ZERO
                # physical map and four historical globally complete maps.
                W32_ADJACENT_COUNTS=(
                    ((23,17),(558,432)),  # zero_split
                    ((56,50),(576,468)),  # lex
                    ((18,19),(378,468)),  # reverse
                    ((7,6),(432,630)),    # S68
                    ((11,11),(450,630)),  # S72
                )
                self.assertEqual(accepted,W32_ADJACENT_COUNTS[index][0][side])
                self.assertEqual(physical,W32_ADJACENT_COUNTS[index][1][side])
                print("AA4AK ORIGINAL W32 ADJACENT",index,side,
                      "accepted",accepted,"physically_occupied",physical)

    def test_03_strict_true_W34_lex_random_complete_partial_K14_maps(self):
        for name in ("lex","random"):
            m=fixture(2,name)
            self.assertEqual((m["a"],comb(m["a"],2)-len(m["right_labels"])),
                             (14,6))
            for side in (0,1):
                root,flag=adjacent_original_rootpair(m,side)
                for four in occupied_root_C4_source_factors(
                        m,side=side,root=root)[:4]:
                    a=exact_adjacent_C6_original_transfer(
                        m,side=side,root=root,pair_offset=flag,four=four)
                    b=independent_complete_physical_adjacent_C6_oracle(
                        m,side=side,root=root,pair_offset=flag,four=four)
                    full=single_original_A_sector_permanent(
                        m,side=side,root=root,pair_offset=flag,four=four)
                    self.assertEqual(a["accepted_actual_original_six_Q"],
                                     b["accepted_original_Q"])
                    self.assertEqual(a["accepted_actual_original_six_Q"],
                                     full["accepted"]["connected_C6"])
                    self.assertEqual(b["occupied_C6"],
                                     full["occupied_physical_H"]["connected_C6"])
                    self.assertTrue(a["adjacent"])
                    self.assertLessEqual(a["accepted_actual_original_six_Q"],24*25)

    def test_04_true_W38_original_global_lex_random_both_orientations(self):
        for name in ("lex","random"):
            m=fixture(3,name)
            self.assertEqual((m["a"],comb(35,2)-585),(35,10))
            for side in (0,1):
                root,flag=adjacent_original_rootpair(m,side)
                four=occupied_root_C4_source_factors(
                    m,side=side,root=root)[0]
                fast=exact_adjacent_C6_original_transfer(
                    m,side=side,root=root,pair_offset=flag,four=four)
                slow=independent_complete_physical_adjacent_C6_oracle(
                    m,side=side,root=root,pair_offset=flag,four=four)
                self.assertEqual(fast["accepted_actual_original_six_Q"],
                                 slow["accepted_original_Q"])
                self.assertLessEqual(slow["accepted_original_Q"],24*81)

    def test_05_conditional_physical_hole_union_all_h_and_original_degree_cap(self):
        for h in range(1,44):
            s=1<<h
            c=adjacent_low_hole_occupied_C6_all_h(s)
            self.assertEqual(c["raw_complete_adjacent_C6"],
                             (c["a"]-3)*(c["a"]-4)*(c["a"]-5))
            self.assertEqual(c["genuine_original_C6_accept_upper_per_root_B_C4"],
                             24*(s+1)**2)
            self.assertTrue(c["unconditional_positive_Hall_mass_NOT_PROVED"])
            if s>=16:
                self.assertTrue(
                    c["all_global_low_holes_Hall_rejected_fraction_ge_1_minus_48d2_a3"])
                self.assertGreaterEqual(
                    Fraction(c["all_global_opposite_maps_physical_occupied_C6_floor"]),
                    Fraction(c["a"]**3,2))
                self.assertLess(
                    Fraction(c["Hall_positive_fraction_upper_under_low_holes"]),1)
                self.assertGreater(
                    1-Fraction(c["Hall_positive_fraction_upper_under_low_holes"]),0)
            else:
                self.assertEqual(c["Hall_positive_fraction_upper_under_low_holes"],
                                 "not asserted")

    def test_06_actual_source_transvection_and_independent_physical_relabelling(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        a=m["a"]
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((i+2)%a for i in range(a)))
        original=tuple(tuple(x) for x in m["incidences"])
        changedinc=tuple(tuple(x) for x in changed["incidences"])
        for side in (0,1):
            root,flag=adjacent_original_rootpair(m,side)
            oldflags=tuple(sorted(original[k][1-side] for k in range(
                len(original)) if original[k][side]==root))
            pin=tuple(combinations(oldflags,2))[flag]
            transport=p if side==0 else l
            opptrans=l if side==0 else p
            newroot=transport[root]
            mapped=tuple(sorted(opptrans[x] for x in pin))
            newflags=tuple(sorted(changedinc[k][1-side] for k in range(
                len(changedinc)) if changedinc[k][side]==newroot))
            newflag=tuple(combinations(newflags,2)).index(mapped)
            four=occupied_root_C4_source_factors(m,side=side,root=root)[0]
            moved_four=tuple(transport[q] for q in four)
            before=exact_adjacent_C6_original_transfer(
                m,side=side,root=root,pair_offset=flag,four=four)
            after=exact_adjacent_C6_original_transfer(
                changed,side=side,root=newroot,pair_offset=newflag,
                four=moved_four)
            self.assertEqual(before["accepted_actual_original_six_Q"],
                             after["accepted_actual_original_six_Q"])

    def test_07_reject_invalid_actual_source_physical_models_and_pins(self):
        m=fixture(1,"lex")
        root,flag=adjacent_original_rootpair(m,0)
        four=occupied_root_C4_source_factors(m,side=0,root=root)[0]
        with self.assertRaises(ValueError):
            adjacent_pin_vertices(((0,1),(2,3)))
        with self.assertRaises(ValueError):
            exact_adjacent_C6_original_transfer(
                m,side=0,root=root,pair_offset=flag,four=None)
        with self.assertRaises(ValueError):
            exact_adjacent_C6_original_transfer(
                m,side=0,root=root,pair_offset=flag,four=(root,)*4)
        with self.assertRaises(ValueError):
            exact_adjacent_C6_original_transfer(
                dict(m,right_labels=((0,1),)*15),side=0,root=root,
                pair_offset=flag,four=four)
        with self.assertRaises(ValueError):
            exact_adjacent_C6_original_transfer(
                dict(m,incidences=tuple(m["incidences"])[:-1]),
                side=0,root=root,pair_offset=flag,four=four)


if __name__=="__main__":unittest.main()
