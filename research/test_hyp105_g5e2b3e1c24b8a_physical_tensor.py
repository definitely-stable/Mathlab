"""B8-A independent Boolean/cycle identity falsifiers; NO full W32 orbit in unittest."""
from itertools import combinations
import unittest

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS, original_W32
from hyp105_g5e2b3e1c24b2_joint_seven import reference_classifier
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b8a_physical_tensor import (
    TAGS, source_profile, physical_factor_state, source_rectangle,
    audit_rectangle,
)


def edges_map(positions, permutation, *, left):
    return {(i + 1 if left else i): tuple(K6_PAIRS[k])
            for i, k in enumerate(permutation)}


def tiny_maps(six):
    """Distinct global assignments to K8 pairs, unrelated to any per-J choice."""
    pts = sorted({p for p, _ in six})
    lines = sorted({l for _, l in six})
    edges = tuple(combinations(range(8), 2))
    f0 = dict(zip(pts, edges[:len(pts)]))
    f1 = f0.copy()
    g0 = dict(zip(lines, edges[6:6 + len(lines)]))
    g1 = g0.copy()
    if len(pts) >= 2:
        f1[pts[0]], f1[pts[-1]] = f1[pts[-1]], f1[pts[0]]
    if len(lines) >= 2:
        g1[lines[0]], g1[lines[-1]] = g1[lines[-1]], g1[lines[0]]
    return f0, f1, g0, g1


class PhysicalMotifTensorTests(unittest.TestCase):
    def test_all_seven_static_original_tags(self):
        examples = {
            "D6": ((0,10),(1,11),(2,12),(3,13),(4,14),(5,15)),
            "B-left/A-right": ((0,10),(0,11),(1,12),(2,13),(3,14),(4,15)),
            "A-left/B-right": ((0,10),(1,10),(2,11),(3,12),(4,13),(5,14)),
            "C/A": ((0,10),(0,11),(1,12),(1,13),(2,14),(2,15)),
            "C/B": ((0,10),(0,11),(1,10),(1,12),(2,13),(2,14)),
            "B/B-overlap": ((0,10),(0,11),(1,10),(2,12),(3,13),(4,14)),
            "B/B-disjoint": ((0,10),(0,11),(1,12),(2,12),(3,13),(4,14)),
        }
        self.assertEqual(set(examples), set(TAGS))
        for name, six in examples.items():
            with self.subTest(tag=name):
                self.assertEqual(source_profile(six), name)
                maps = tiny_maps(six)
                row = source_rectangle(six, *maps)
                self.assertEqual(row["tag"], name)
                self.assertEqual(
                    row["mixed"],
                    row["direct"][3]-row["direct"][1]-row["direct"][2]+row["direct"][0])
                self.assertEqual(row["mixed"], row["tensor"])
                self.assertLessEqual(abs(row["mixed"]), row["physical_joint_cap"])
        for bad in (((),), ((0,1),)*6, ((0,1),(0,2)), ((1.5,1),)*6):
            with self.assertRaises(ValueError):
                source_profile(bad)

    def test_connected_d6_signature_and_disconnected_two_triangles(self):
        six = tuple((i, i+20) for i in range(6))
        cycle = ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        left = dict(enumerate(cycle))
        right = {i+20: e for i,e in enumerate(cycle)}
        self.assertTrue(physical_factor_state(six,left,left=True)[0])
        self.assertEqual(source_rectangle(six,left,left,right,right)["direct"], (1,1,1,1))
        different = right.copy()
        different[20], different[22] = different[22], different[20]
        self.assertEqual(source_rectangle(six,left,left,different,different)["direct"], (0,0,0,0))
        triangles = ((0,1),(1,2),(0,2),(3,4),(4,5),(3,5))
        split = dict(enumerate(triangles))
        physical, signature = physical_factor_state(six,split,left=True)
        self.assertTrue(physical)
        self.assertIsNone(signature)
        self.assertEqual(source_rectangle(six,split,split,right,right)["direct"], (0,0,0,0))

    def test_explicit_mixed_d6_changes_are_not_product_of_booleans(self):
        six = tuple((i,i+20) for i in range(6))
        cycle = ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        left0 = dict(enumerate(cycle))
        left1 = left0.copy()
        left1[0],left1[2] = left1[2],left1[0]
        right0 = {i+20:e for i,e in enumerate(cycle)}
        right1 = right0.copy()
        right1[20],right1[22] = right1[22],right1[20]
        row = source_rectangle(six,left0,left1,right0,right1)
        self.assertEqual(row["direct"], (1,0,0,1))
        self.assertEqual(row["mixed"], 2)
        self.assertEqual(row["physical_joint_cap"], 2)
        self.assertTrue(all(physical_factor_state(six,assign,left=is_left)[0]
                            for assign,is_left in ((left0,True),(left1,True),
                                                   (right0,False),(right1,False))))

    def test_original_W32_small_source_independent_full_classifier(self):
        _, lines, _ = original_W32()
        incidences = tuple(sorted((p,l) for l,line in enumerate(lines) for p in line))
        # Each sixset is from the ORIGINAL common universe, not manufactured
        # individually under a different physical assignment.
        seed = incidences[0:10] + incidences[20:24]
        f0, g0 = tuple(W32_LEFT_H45), tuple(W32_RIGHT_S68)
        f1 = legal_transpose(f0,3,8)
        g1 = legal_transpose(g0,0,14)
        maps = (edges_map(seed,f0,left=True),edges_map(seed,f1,left=True),
                edges_map(seed,g0,left=False),edges_map(seed,g1,left=False))
        source = tuple(combinations(seed,6))
        self.assertEqual(len(source),3003)
        report = audit_rectangle(source,*maps)
        self.assertTrue(report["mixed_tensor_identity_exact"])
        for six in source:
            row = source_rectangle(six,*maps)
            observed = tuple(int(reference_classifier(six,f,g) is not None)
                             for f,g in ((f0,g0),(f1,g0),(f0,g1),(f1,g1)))
            self.assertEqual(row["direct"] if row is not None else (0,0,0,0),observed)
        self.assertEqual(report["mixed_curvature"],
                         report["S_11"]-report["S_10"]-report["S_01"]+report["S_00"])


if __name__=="__main__":
    unittest.main()
