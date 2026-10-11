"""Fast independent physical 2-pin falsifiers for C24-B8-D.

Full original W32 62,370-source verification lives in a dedicated hosted job.
"""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2b3e1c24b8a_physical_tensor import (
    physical_factor_state, source_profile,
)
from hyp105_g5e2b3e1c24b8c_conditional_discrepancy import (
    pinned_source_right_probability, source_right_mean,
)
from hyp105_g5e2b3e1c24b8d_two_line_influence import (
    adjacency_probability, source_influence, compiled_matrix, shape,
)


def fixture():
    f={i:e for i,e in enumerate(((0,1),(1,2),(2,3),(3,4),(4,5),(0,5)))}
    d6=tuple((i,i) for i in range(6))
    c=((0,6),(1,6),(2,7),(3,7),(4,8),(5,8))
    b=((0,5),(1,5),(2,9),(3,10),(4,11),(5,12))
    fa={0:(0,1),1:(2,3),2:(3,4),3:(4,5),4:(2,5)}
    a=((0,3),(0,4),(1,5),(2,6),(3,7),(4,8))
    return [(d6,f),(c,f),(b,f),(a,fa)]


class TwoLineInfluenceTests(unittest.TestCase):
    def test_probability_closed_and_unpinned_depletion(self):
        self.assertEqual(adjacency_probability(6),Fraction(4,7))
        with self.assertRaises(ValueError):
            adjacency_probability(5)
        six,f=fixture()[1]
        tag=source_profile(six)
        lines=tuple(l for _,l in six)
        for i,j in ((6,7),(6,13),(13,14)):
            row=source_influence(6,tag,lines,None,i,j)
            adjacent=pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(0,2)},max_states=100000)
            disjoint=pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(2,3)},max_states=100000)
            self.assertEqual(row["adj"],adjacent)
            self.assertEqual(row["dis"],disjoint)
            self.assertEqual(8*adjacent+6*disjoint,
                             14*source_right_mean(six,f,6))
        # Even when NEITHER pinned line occurs in J the conditioning
        # changes its probability via the depleted host edge universe.
        self.assertNotEqual(
            source_influence(6,tag,lines,None,13,14)["influence"],0)

    def test_B_profile_double_and_singleton(self):
        six,f=fixture()[2]
        tag=source_profile(six)
        lines=tuple(l for _,l in six)
        for i,j in ((5,9),(9,10)):
            row=source_influence(6,tag,lines,None,i,j)
            self.assertEqual(row["adj"],pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(0,2)},max_states=200000))
            self.assertEqual(row["dis"],pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(2,3)},max_states=200000))
        self.assertEqual(source_influence(6,tag,lines,None,5,9)["adj"],0)

    def test_matched_D6_signature_not_boolean(self):
        six,f=fixture()[0]
        ok,sig=physical_factor_state(six,f,left=True)
        self.assertTrue(ok)
        self.assertIsNotNone(sig)
        tag=source_profile(six)
        lines=tuple(l for _,l in six)
        for i,j in ((0,1),(0,3)):
            row=source_influence(6,tag,lines,sig,i,j)
            self.assertEqual(row["adj"],pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(0,2)},max_states=100000))
            self.assertEqual(row["dis"],pinned_source_right_probability(
                six,f,6,{i:(0,1),j:(2,3)},max_states=100000))
        bad=((0,1),(1,2),(0,2),(3,4),(4,5),(3,5))
        with self.assertRaises(ValueError):
            shape("D6",lines,bad)

    def test_A_six_singletons_and_all_tag_zero_rows(self):
        six,f=fixture()[3]
        tag=source_profile(six)
        self.assertEqual(tag,"B-left/A-right")
        lines=tuple(l for _,l in six)
        row=source_influence(6,tag,lines,None,3,4)
        self.assertEqual(row["adj"],pinned_source_right_probability(
            six,f,6,{3:(0,1),4:(0,2)},max_states=100000))
        self.assertEqual(row["dis"],pinned_source_right_probability(
            six,f,6,{3:(0,1),4:(2,3)},max_states=100000))
        records=[]
        for ix,(example,left) in enumerate(fixture()):
            tag=source_profile(example)
            l=tuple(v for _,v in example)
            sig=physical_factor_state(example,left,left=True)[1] if tag=="D6" else None
            records.append((tag,l,sig,ix+1))
        src={"records":records,"static_eligible":sum(x[3] for x in records)}
        full=compiled_matrix(src,6,15)
        self.assertTrue(full["full_bijection_row_theorem"])
        self.assertTrue(all(v==0 for v in full["row_sums"].values()))
        for i,j in combinations(range(15),2):
            direct=sum((mult*source_influence(6,tag,ls,sig,i,j)["influence"]
                        for tag,ls,sig,mult in records),Fraction(0))
            self.assertEqual(full["matrix"][(i,j)],direct)
            self.assertEqual(full["matrix"][(i,j)],
                sum((full["by_tag_matrix"][t][(i,j)]
                     for t in full["by_tag_matrix"]),Fraction(0)))

    def test_guards(self):
        six,_=fixture()[0]
        with self.assertRaises(ValueError):
            source_influence(6,"D6",tuple(l for _,l in six),None,0,1)
        # A source population checksum disagreement is an integrity
        # assertion, not a malformed parameter ValueError.
        with self.assertRaisesRegex(AssertionError,"multiplicities lost"):
            compiled_matrix({"records":[],"static_eligible":1},6,15)
        with self.assertRaises(ValueError):
            compiled_matrix({"records":[],"static_eligible":0},6,16)
        with self.assertRaises(ValueError):
            source_influence(6,"D6",tuple(l for _,l in six),
                             ((0,1),),0,1)


if __name__=="__main__":
    unittest.main()
