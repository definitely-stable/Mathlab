"""Independent AA4-AN actual ORIGINAL D-FIRST physical-twofactor fourflag tests."""
import unittest
from collections import Counter
from itertools import combinations,combinations_with_replacement
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index,
)
from hyp105_issue230_d6aa4an_d_pair_fourflag_transfer import (
    rooted_adjacent_physical_twofactor_completions,
    all_h_rooted_D_fourflag_shape_capacity,
    physical_unilateral_D_source_completion_census,
    exact_original_W32_D_FIRST_selected_seven,
)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


def physical_six_shape(anchor,rest):
    """Independent degree/twofactor traversal with no rooted shape oracle."""
    six=tuple(anchor)+tuple(rest)
    degrees=Counter(v for edge in six for v in edge)
    if len(degrees)!=6 or any(deg!=2 for deg in degrees.values()):
        return None
    C=Counter(six)
    if 2 in C.values():
        if tuple(sorted(C.values()))!=(1,1,1,1,2):
            raise AssertionError("false physical repeated edge shape")
        return "C4+C2"
    adj={v:set() for v in degrees}
    for u,v in six:
        adj[u].add(v);adj[v].add(u)
    seen=set();ncomp=0
    for start in adj:
        if start in seen:continue
        ncomp+=1
        pending=[start]
        while pending:
            at=pending.pop()
            if at in seen:continue
            seen.add(at);pending.extend(adj[at]-seen)
    return "C6" if ncomp==1 else "C3+C3" if ncomp==2 else None


def first_D_from_original_flags(model):
    """Independent original incidence flag-pair major; do NOT form D set."""
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    for i,(p,l) in enumerate(inc):
        for j in range(i+1,len(inc)):
            q,m=inc[j]
            if p!=q and l!=m and set(f[p])&set(f[q]) and set(g[l])&set(g[m]):
                return (i,j)
    raise AssertionError("true original source fixture has no D anchor")


class GenuineOriginalDfirstPhysical2factorTests(unittest.TestCase):
    def test_01_all_h_complete_Ka_three_shapes_and_unilateral_real_source_count(self):
        for h in range(1,51):
            s=1<<h
            z=all_h_rooted_D_fourflag_shape_capacity(s)
            a=z["a"];d=s+1
            self.assertEqual(z["V"],(s+1)*(s*s+1))
            self.assertEqual(z["complete_Ka_C6_shape_count"],
                             (a-3)*(a-4)*(a-5))
            self.assertEqual(z["complete_Ka_two_C3_shape_count"],comb(a-3,3))
            self.assertEqual(z["complete_Ka_C4_plus_doubled_C2_shape_count"],
                             (a-3)*comb(a-4,2))
            expected=((a-3)*(a-4)*(a-5)+comb(a-3,3))*d**4 + (
                (a-3)*comb(a-4,2))*d*d*comb(d,2)
            self.assertEqual(z["full_Ka_exact_unilateral_four_REAL_original_flags"],expected)
            self.assertTrue(z["every_genuine_original_D_pair_positive_true_GF5_extension_NOT_PROVED"])

    def test_02_independent_exhaustive_physical_K6_K7_K8_four_residual_multisets(self):
        for a in (6,7,8):
            anchor=((0,1),(0,2))
            from_new={}
            for kind,rem in rooted_adjacent_physical_twofactor_completions(
                    *anchor,a):
                key=tuple(sorted(rem))
                self.assertNotIn(key,from_new)
                from_new[key]=kind
            allpairs=tuple(combinations(range(a),2))
            independent={}
            for other in combinations_with_replacement(allpairs,4):
                kind=physical_six_shape(anchor,other)
                if kind is not None:independent[tuple(sorted(other))]=kind
            self.assertEqual(from_new,independent)
            self.assertEqual(
                dict(Counter(from_new.values())),
                {"C6":(a-3)*(a-4)*(a-5),
                 "C3+C3":comb(a-3,3),
                 "C4+C2":(a-3)*comb(a-4,2)})
            self.assertEqual(len(from_new),
                             (a-3)*(a-4)*(a-5)+comb(a-3,3)+
                             (a-3)*comb(a-4,2))

    def test_03_true_original_W32_all_five_complete_maps_D_FIRST_vs_Q_FIRST(self):
        cases=(("dual-zero",zero_split_original_W32(),277,164,115,162),
               ("lex",fixture(1,"lex"),307,517,212,95),
               ("reverse",fixture(1,"reverse"),300,246,166,134),
               ("S68",fixture(1,"S68"),257,79,64,193),
               ("S72",fixture(1,"S72"),261,75,59,202))
        for name,model,D,E,C,Z in cases:
            z=exact_original_W32_D_FIRST_selected_seven(
                model,full_independent=True)
            self.assertEqual(
                (z["genuine_original_D_anchors"],
                 z["D_FIRST_seven_accepted_extension_E"],
                 z["D_FIRST_D_pairs_covered_by_any_selected_seven"],
                 z["D_FIRST_D_pairs_ZERO_seven_extensions"]),
                (D,E,C,Z))
            self.assertEqual(
                z["physical_point_only_all_D_unilateral_candidate_fourflag_total"],
                D*648)
            self.assertGreaterEqual(
                z["both_typed_physical_2regular_D_incidence_total"],E)
            self.assertTrue(z["INDEPENDENT_historical_Q_FIRST_seven_charge_agreed"])
            print("AA4AN ORIGINAL",name,
                  "D",D,"point_source_candidates",D*648,
                  "bilateral_twofactor",z[
                      "both_typed_physical_2regular_D_incidence_total"],
                  "selected_GF5_extension_E",E,
                  "uncovered_D",Z,
                  "E_tags",z["D_FIRST_selected_seven_E_by_tag"])

    def test_04_true_W32_direct_all_four_flags_brute_matches_unilateral_648(self):
        # Independent source-first 4-subset oracle, NOT physical
        # K_a pattern construction. Each physical accepted Q is counted
        # exactly once for a fixed actual D anchor.
        for scheme,m in (("lex",fixture(1,"lex")),
                         ("S68",fixture(1,"S68"))):
            s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
            anchor=first_D_from_original_flags(m)
            others=tuple(j for j in range(len(inc)) if j not in anchor)
            count=Counter()
            for quad in combinations(others,4):
                six=tuple(anchor)+quad
                physical=tuple(f[inc[j][0]] for j in six)
                kind=physical_six_shape(physical[:2],physical[2:])
                if kind is not None:count[kind]+=1
            fast=physical_unilateral_D_source_completion_census(
                m,anchor,side=0,enumerate_flags=True)
            self.assertEqual(dict(count),fast[
                "exact_one_side_REAL_original_four_flag_completions_by_shape"])
            self.assertEqual(sum(count.values()),648)
            self.assertEqual(dict(count),{
                "C6":486,"C3+C3":81,"C4+C2":81})

    def test_05_real_W34_nononto_K14_two_sides_and_true_source_flag_quartets(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
            self.assertEqual((a,comb(a,2)-V),(14,6))
            anchor=first_D_from_original_flags(m)
            for side in (0,1):
                fast=physical_unilateral_D_source_completion_census(
                    m,anchor,side=side,enumerate_flags=True)
                self.assertLessEqual(
                    fast["exact_one_side_original_four_FLAG_completions_total"],
                    all_h_rooted_D_fourflag_shape_capacity(s)[
                        "full_Ka_exact_unilateral_four_REAL_original_flags"])
                self.assertTrue(fast["full_source_original_flag_enumerator_checked"])
                self.assertEqual(
                    sum(fast["exact_one_side_REAL_original_four_flag_completions_by_shape"].values()),
                    fast["exact_one_side_original_four_FLAG_completions_total"])
                self.assertGreater(fast["exact_one_side_original_four_FLAG_completions_total"],0)

    def test_06_real_W38_partial_K35_source_Q_count_without_materializing_4flag_cartesian(self):
        for scheme in ("lex","random"):
            m=fixture(3,scheme)
            anchor=first_D_from_original_flags(m)
            for side in (0,1):
                z=physical_unilateral_D_source_completion_census(
                    m,anchor,side=side,enumerate_flags=False)
                self.assertEqual(z["a"],35)
                self.assertLessEqual(
                    z["exact_one_side_original_four_FLAG_completions_total"],
                    all_h_rooted_D_fourflag_shape_capacity(8)[
                        "full_Ka_exact_unilateral_four_REAL_original_flags"])
                self.assertGreater(z["actually_occupied_global_physical_2factor_by_shape"]["C6"],0)

    def test_07_maximal_palette_hole_star_kills_all_D_anchored_physical_2factors(self):
        # This is a SHARP physical injection non-lift counterexample
        # for palette size V=C(a-1,2)+1. It does NOT assert existence
        # of any dyadic W3s order attaining this exact maximal m.
        for a in (6,7,8,12):
            x,u,v=0,1,2
            missing={(min(u,z),max(u,z)) for z in range(a) if z!=x and z!=u}
            self.assertEqual(len(missing),a-2)
            occupied=set(combinations(range(a),2))-missing
            self.assertIn((x,u),occupied)
            self.assertIn((x,v),occupied)
            self.assertEqual(len(occupied),comb(a-1,2)+1)
            kinds=Counter(kind for kind,edges in
                          rooted_adjacent_physical_twofactor_completions(
                              (x,u),(x,v),a)
                          if all(e in occupied for e in edges))
            self.assertEqual(kinds,Counter())

    def test_08_true_source_common_symplectic_automorphism_physical_relabel(self):
        m=zero_split_original_W32()
        x=exact_original_W32_D_FIRST_selected_seven(m)
        pt,ln=symplectic_transvection_source(m,2)
        a=m["a"]
        altered=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((j+3)%a for j in range(a)))
        y=exact_original_W32_D_FIRST_selected_seven(altered)
        for key in (
            "genuine_original_D_anchors",
            "physical_point_only_all_D_unilateral_candidate_fourflag_total",
            "both_typed_physical_2regular_D_incidence_total",
            "D_FIRST_seven_accepted_extension_E",
            "D_FIRST_accepted_seven_sixsets_WITH_D_anchor",
            "D_FIRST_D_pairs_ZERO_seven_extensions",
            "D_FIRST_selected_seven_E_by_tag",
        ):
            self.assertEqual(x[key],y[key])

    def test_09_strict_reject_fake_source_injection_and_invalid_original_anchor(self):
        m=fixture(1,"lex")
        anchor=first_D_from_original_flags(m)
        with self.assertRaises(ValueError):
            rooted_adjacent_physical_twofactor_completions((0,1),(2,3),6).__next__()
        with self.assertRaises(ValueError):
            all_h_rooted_D_fourflag_shape_capacity(12)
        for bad in (dict(m,left_labels=((0,1),)*15),
                    dict(m,right_labels=((0,1),)*15),
                    dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises(ValueError):
                physical_unilateral_D_source_completion_census(
                    bad,anchor,side=0)
        with self.assertRaises(ValueError):
            physical_unilateral_D_source_completion_census(
                m,(anchor[0],anchor[0]),side=0)
        with self.assertRaises(ValueError):
            physical_unilateral_D_source_completion_census(
                m,anchor,side=2)


if __name__=="__main__":
    unittest.main()
