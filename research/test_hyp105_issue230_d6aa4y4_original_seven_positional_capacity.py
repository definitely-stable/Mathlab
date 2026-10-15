"""HYP-105 #230 Y4 independent true-original C6 same-Q positional tests."""
import unittest
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model,exact_ONE_side_original_projection_index)
from hyp105_g5e2b3e1b0_seven_signature import (
    physical_column_dual,is_connected_column_cycle)
from hyp105_issue230_d6aa4y4_original_seven_positional_capacity import (
    original_AA_connected_root_physical_capacity,
    original_AA_affected_two_source_capacity,
    original_AA_crossed_point_line_capacity,
    original_AA_harmful_two_swap_upper,
    original_tag_affected_half_upper,
    parse_original_seven_quadrants,HEADERS,TAGS,QUADRANTS)


def brute_connected_physical_six_cycles(a):
    """Independent enumeration: DO NOT use the 24/6/12 symbolic formulas."""
    out=set()
    for vertices in combinations(range(a),6):
        edges=tuple(combinations(vertices,2))
        for picked in combinations(edges,6):
            degree=Counter(v for e in picked for v in e)
            if len(degree)!=6 or any(q!=2 for q in degree.values()):
                continue
            found={picked[0][0]}
            stack=list(found)
            while stack:
                v=stack.pop()
                for x,y in picked:
                    other=y if v==x else (x if v==y else None)
                    if other is not None and other not in found:
                        found.add(other);stack.append(other)
            if len(found)==6:
                out.add(frozenset(picked))
    return out


class OriginalSevenPositionalY4Tests(unittest.TestCase):
    def test_001_independent_K6_K7_connected_C6_physical_24_6_12(self):
        for a in (6,7):
            cycles=brute_connected_physical_six_cycles(a)
            self.assertEqual(len(cycles),60*comb(a,6))
            e0=(0,1)
            self.assertEqual(sum(e0 in z for z in cycles),24*comb(a-2,4))
            for other,count in (((0,2),6*comb(a-3,3)),
                                ((2,3),12*comb(a-4,2))):
                self.assertEqual(
                    sum(e0 in z and other in z for z in cycles),count)

    def test_002_original_W32_connected_true_source_factor_17496(self):
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            inc,p,g=strict_true_W32_model(model)
            for side,labels in ((0,p),(1,g)):
                half=exact_ONE_side_original_projection_index(model,side)
                count=Counter()
                selected=0
                for Q,source_kind in half["candidate_sixset_map"].items():
                    if source_kind!="A":continue
                    source_cols=tuple(inc[j][side] for j in Q)
                    dual=physical_column_dual(inc,labels,source_cols)
                    if not is_connected_column_cycle(dual):continue
                    selected+=1
                    for src in set(source_cols):count[src]+=1
                self.assertEqual(selected,60*3**6)
                self.assertEqual(len(count),15)
                self.assertTrue(all(v==24*3**6 for v in count.values()))

    def test_003_all_h_original_AA_class_two_source_stronger(self):
        for h in range(1,13):
            s=1<<h
            for r in ("adjacent","disjoint"):
                x=original_AA_affected_two_source_capacity(s,r)
                self.assertGreater(x["connected_mode_two_source_union_upper"],0)
                self.assertLess(x["connected_mode_two_source_union_upper"],
                                x["complete_physical_A_two_source_union_upper"])
                for m in range(4):
                    z=original_AA_harmful_two_swap_upper(s,r,r,m)
                    self.assertTrue(z["all_h_connected_positional_AA_GF5_harm_bound_PROVED"])
                    self.assertLessEqual(
                        z["D6_harmful_same_original_Q_connected_C6_mode_upper"],
                        z["prior_all_seven_untagged_mode_bound"])
                    self.assertFalse(z["all_h_seven_S_omega_s6_PROVED"])

    def test_004_source_typed_all_seven_class_projection_caps(self):
        for s in (2,4,8,16):
            for r in ("adjacent","disjoint"):
                for t in TAGS:
                    from hyp105_issue230_d6aa4y4_original_seven_positional_capacity import (
                        TAG_POINT_SHAPES,TAG_LINE_SHAPES)
                    p=original_tag_affected_half_upper(s,r,TAG_POINT_SHAPES[t])
                    l=original_tag_affected_half_upper(s,r,TAG_LINE_SHAPES[t])
                    self.assertGreater(p,0);self.assertGreater(l,0)
                self.assertEqual(
                    original_tag_affected_half_upper(s,r,("CONNECTED_A",)),
                    original_AA_affected_two_source_capacity(s,r)[
                        "connected_mode_two_source_union_upper"])
        with self.assertRaises(ValueError):
            original_tag_affected_half_upper(2,"unknown",("A",))
        with self.assertRaises(ValueError):
            original_tag_affected_half_upper(2,"adjacent",("A","A"))
        with self.assertRaises(ValueError):
            original_AA_affected_two_source_capacity(2,"same")

    def test_005_all_h_original_AA_2x2_cross_source_girth(self):
        for s in (2,4,8,16,32):
            for m in range(4):
                c=original_AA_crossed_point_line_capacity(s,m)
                self.assertEqual(c["m"],m)
                self.assertGreater(c["original_2point_2line_AA_source_cross_upper"],0)
                self.assertTrue(c["all_h_actual_source_girth_eight_and_positional_connected_C6"])
        with self.assertRaises(ValueError):
            original_AA_crossed_point_line_capacity(2,4)
        with self.assertRaises(ValueError):
            original_AA_crossed_point_line_capacity(2,True)

    def test_006_fail_closed_full_true_original_11236_7_tag_schema(self):
        header="\t".join(HEADERS)
        data=["\t".join(map(str,(i,j,*([0]*28))))
              for i in range(106) for j in range(106)]
        x=parse_original_seven_quadrants(header+"\n"+"\n".join(data))
        self.assertEqual(len(x),11236)
        self.assertEqual(len(x[105,105]),7)
        self.assertEqual(set(x[105,105]["D6"]),set(QUADRANTS))
        with self.assertRaises(AssertionError):
            parse_original_seven_quadrants(header+"\n"+"\n".join(data[:-1]))
        altered=data.copy()
        altered[0]="\t".join(map(str,(0,0,1,*([0]*27))))
        with self.assertRaises(AssertionError):
            parse_original_seven_quadrants(header+"\n"+"\n".join(altered))


if __name__=="__main__":
    unittest.main()
