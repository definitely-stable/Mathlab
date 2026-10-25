"""AA4-SFC: two-step-independent full source-ID collision census falsifiers."""
import json
import os
import unittest

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
