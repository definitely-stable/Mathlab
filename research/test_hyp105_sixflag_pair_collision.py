"""AA4-SFC: two-step-independent full source-ID collision census falsifiers."""
import json
import os
import unittest
from collections import Counter, deque

from hyp105_sixflag_pair_collision import source_sixflag_collision_census
from hyp105_weighted_variance_transfer import witness_maps


class TestSixOriginalFlagCollision(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(os.path.dirname(__file__),
                               "hyp105_w34_adversarial_certificate.json"),
                  encoding="utf-8") as stream:
            cls.cert = json.load(stream)

    def test_both_true_w32_covariance_sign_witnesses(self):
        # Exact results from separate finite GF(2) geometric/corner oracle.
        for seed, row in (
            (41, (1322,0,336,986,8612,4608,2032,0,1972,576,254,158,22,18)),
            (91, (1100,0,240,860,6312,3224,1368,0,1720,403,171,157,23,18)),
        ):
            with self.subTest(seed=seed):
                f,g = witness_maps(seed)
                c = source_sixflag_collision_census(1,f,g)
                seen = tuple(c[k] for k in (
                    "physical_proper","missing","incident","P","Q",
                    "Q0_six_distinct_source_flags",
                    "Q1_five_distinct_source_flags",
                    "Q2_forbidden_two_shared_flags",
                    "Q3_reverse_orbit",
                    "C0","C1","occupied_source_endpoint_pairs",
                    "zero_source_endpoint_pairs","max_N3",
                ))
                self.assertEqual(seen,row)
                self.assertEqual(c["U"],180)
                self.assertEqual(c["Q"],2*c["P"]+8*(c["C0"]+c["C1"]))
                self.assertFalse(c["root_GF5_sevenclass_proved"])

    def test_true_symplectic_w34_sixflag_collision_moment(self):
        c = source_sixflag_collision_census(
            2,self.cert["f"],self.cert["g"],verify_with_previous=True
        )
        self.assertEqual(c["U"],6800)
        self.assertEqual((c["physical_proper"],c["missing"],c["incident"]),
                         (70476,8306,3440))
        self.assertEqual((c["P"],c["Q"]),(58730,676700))
        self.assertEqual(
            (c["Q0_six_distinct_source_flags"],
             c["Q1_five_distinct_source_flags"],
             c["Q2_forbidden_two_shared_flags"],
             c["Q3_reverse_orbit"]),
            (486880,72360,0,117460)
        )
        self.assertEqual((c["C0"],c["C1"]),(60860,9045))
        self.assertEqual((c["occupied_source_endpoint_pairs"],
                          c["zero_source_endpoint_pairs"],c["max_N3"]),
                         (6613,187,38))
        self.assertEqual((c["bad_P"],c["good_P"]),(35616,23114))
        self.assertEqual((c["bad_Q"],c["good_Q"]),(415704,260996))
        self.assertEqual(c["Q"],2*c["P"]+8*(c["C0"]+c["C1"]))

    def test_original_typed_injection_is_fail_closed(self):
        f,g = witness_maps(41)
        bad = list(f)
        bad[0] = bad[1]
        with self.assertRaises(ValueError):
            source_sixflag_collision_census(1,bad,g)
        with self.assertRaises(ValueError):
            source_sixflag_collision_census(1,f,g[:-1])
        with self.assertRaises(ValueError):
            source_sixflag_collision_census(3,f,g)

    def test_middle_end_postings_against_independent_source_certificates(self):
        cases = [
            (1, *witness_maps(41), (53,201,3,4)),
            (1, *witness_maps(91), (45,126,3,3)),
            (2, self.cert["f"], self.cert["g"], (240,8805,3,4)),
        ]
        for power, f, g, expected in cases:
            with self.subTest(power=power, expected=expected):
                c = source_sixflag_collision_census(
                    power,f,g,verify_with_previous=False
                )
                self.assertIn("C1_middle",c)
                self.assertEqual(tuple(c[k] for k in (
                    "C1_middle","C1_end",
                    "max_middle_flag_occupancy","max_end_flag_occupancy",
                )),expected)
                self.assertEqual(c["C1_middle"]+c["C1_end"],c["C1"])
                self.assertEqual(2*c["middle_flag_appearances"],c["P"])
                self.assertEqual(c["end_flag_appearances"],c["P"])
                self.assertLessEqual(4*c["C1_middle"],3*c["P"])

    def test_middle_bound_on_all_complement_paired_four_by_four_hosts(self):
        pairs = sorted({tuple(sorted(((p,l),(p^1,l^1))))
                        for p in range(4) for l in range(4)})
        histogram = Counter()
        for mask in range(1 << len(pairs)):
            edges = [edge for i,pair in enumerate(pairs) if mask & (1 << i)
                     for edge in pair]
            adjacency = [set() for _ in range(8)]
            for p,l in edges:
                adjacency[p].add(l+4)
                adjacency[l+4].add(p)
            valid = True
            # Independently detect a short cycle by finding an alternate
            # path for each edge, without using the census or its bound.
            for p,l in edges:
                target = l+4
                distances = {p:0}
                queue = deque([p])
                while queue:
                    u = queue.popleft()
                    for v in adjacency[u]:
                        if {u,v} == {p,target} or v in distances:
                            continue
                        distances[v] = distances[u]+1
                        queue.append(v)
                if target in distances and distances[target] < 7:
                    valid = False
                    break
            if valid:
                histogram[mask.bit_count()] += 1
        self.assertEqual(histogram,{0:1,1:8,2:24,3:32,4:8})

    def test_physical_coordinate_relabelings_leave_all_counts_unchanged(self):
        f,g = witness_maps(91)
        before = source_sixflag_collision_census(1,f,g,verify_with_previous=False)
        f2 = [tuple(sorted(((5*x+1)%6,(5*y+1)%6))) for x,y in f]
        g2 = [tuple(sorted(((5*x+2)%6,(5*y+2)%6))) for x,y in g]
        after = source_sixflag_collision_census(
            1,f2,g2,verify_with_previous=False
        )
        self.assertEqual(before,after)


if __name__ == "__main__":
    unittest.main()
