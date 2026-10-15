"""AA4-AH exact rank-six true-original GF5 Hall transfer, independent tests."""
import unittest
from itertools import combinations
from hyp105_issue230_d6aa4ah_signature_hall_kernel import (
    PAIRS4,bit_signature_permanent,channel_kernel,rank_six_identity_witness,
    six_channel_original_cohort)
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import original_triangle_hall_cohort
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import transform_model

class SixChannelAllOriginalHall(unittest.TestCase):
    def test_01_full_65536_abstract_signature_kernel_factorization(self):
        hist={}
        for a in range(256):
            for b in range(256):
                direct=bit_signature_permanent(a,b)
                fact=sum(channel_kernel(a,b))
                self.assertEqual(direct,fact)
                hist[direct]=hist.get(direct,0)+1
        self.assertEqual(sum(hist.values()),65536)
        self.assertEqual(bit_signature_permanent(255,255),24)

    def test_02_exact_rational_rank_six_identity_minor(self):
        z=rank_six_identity_witness()
        self.assertTrue(z["all_256x256_abstract_permanent_kernel_rank_exactly_six"])
        self.assertEqual(z["minor"],tuple(tuple(int(i==j) for j in range(6)) for i in range(6)))

    def test_03_real_original_W32_three_maps_both_types_and_actual_rootpairs(self):
        for scheme in ("S68","S72","lex"):
            m=fixture(1,scheme)
            for side in (0,1):
                for root in (0,3,9):
                    for off in (0,1,2):
                        z=six_channel_original_cohort(m,side=side,root=root,
                                                      pair_offset=off,max_C4=3)
                        old=original_triangle_hall_cohort(m,side=side,root=root,
                                                           pair_offset=off,max_C4=3)
                        self.assertEqual(z["accepted_original_GF5_Q_sample"],
                                         old["accepted_original_GF5_restricted"])
                        self.assertEqual(z["source_physical_C4_total"],3)
                        self.assertEqual(z["source_physical_C4_sampled"],3)
                        self.assertEqual(len(z["six_channel_rows"]),3)
                        for row in z["six_channel_rows"]:
                            self.assertEqual(sum(c["true_original_GF5_distinct_Q"]
                                                 for c in row["channels"]),
                                             row["accepted_original_GF5_Q"])
                            self.assertEqual(len(row["channels"]),6)
                            self.assertTrue(all(c["same_site_exclusion"]<=min(
                                c["left_auxiliary_sites"],c["right_auxiliary_sites"])
                                for c in row["channels"]))

    def test_04_real_original_W34_holes_and_zero_Hall_without_fake_candidates(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            for side in (0,1):
                z=six_channel_original_cohort(m,side=side,root=0,
                                              pair_offset=0,max_C4=6)
                old=original_triangle_hall_cohort(m,side=side,root=0,
                                                   pair_offset=0,max_C4=6)
                self.assertGreaterEqual(z["source_physical_C4_total"],945)
                self.assertEqual(z["accepted_original_GF5_Q_sample"],
                                 old["accepted_original_GF5_restricted"])
                self.assertEqual(z["left_occupied_auxiliary_sites"]*
                                 z["right_occupied_auxiliary_sites"]
                                 -z["prohibited_same_auxiliary_sites"],
                                 old["independent_triangle_count"])
                if scheme=="random" and side==1:
                    self.assertEqual(old["indexed_occupied_triangle_candidates"],438)
                    self.assertEqual(old["accepted_original_GF5_restricted"],0)
                    self.assertEqual(z["accepted_original_GF5_Q_sample"],0)

    def test_05_entire_true_W32_triangle_subclass_vs_seven_class_baseline(self):
        expected={"S68":(44,21),"S72":(36,31),"lex":(98,110),
                  "reverse":(77,74)}
        for scheme in expected:
            m=fixture(1,scheme)
            observed=[]
            for side in (0,1):
                count=0
                for root in range(15):
                    for offset in range(3):
                        z=six_channel_original_cohort(m,side=side,root=root,
                                pair_offset=offset,max_C4=3,independent_direct=False)
                        count+=z["accepted_original_GF5_Q_sample"]
                observed.append(count)
            for x,upper in zip(observed,expected[scheme]):
                self.assertGreaterEqual(x,0)
                self.assertLessEqual(x,upper)
            print("true W32 triangle-only BF5",scheme,observed,
                  "full BA/AB prior",expected[scheme])

    def test_06_genuine_source_and_physical_relabel_invariance(self):
        m=fixture(2,"lex")
        four=occupied_root_C4_source_factors(m,side=0,root=0)[0]
        original=six_channel_original_cohort(m,side=0,root=0,
                   pair_offset=0,four_sources=four)
        a=m["a"]
        changed=transform_model(
            m,point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((x+3)%a for x in range(a)))
        updated=six_channel_original_cohort(changed,side=0,root=0,
                   pair_offset=0,four_sources=four)
        self.assertEqual(original["accepted_original_GF5_Q_sample"],
                         updated["accepted_original_GF5_Q_sample"])
        self.assertEqual(
            tuple(z["true_original_GF5_distinct_Q"] for z in original["six_channel_rows"][0]["channels"]),
            tuple(z["true_original_GF5_distinct_Q"] for z in updated["six_channel_rows"][0]["channels"]))

    def test_07_six_channel_direct_Q_validation_for_real_W34(self):
        m=fixture(2,"random")
        for side in (0,1):
            for offset in (0,2,4):
                z=six_channel_original_cohort(m,side=side,root=1,
                                              pair_offset=offset,max_C4=4,
                                              independent_direct=True)
                self.assertEqual(z["source_physical_C4_sampled"],4)
                self.assertTrue(z["physical_Hall_positivity_lower_all_f_g_NOT_PROVED"])

    def test_08_invalid_original_source_and_signature_domains(self):
        for x,y in ((-1,0),(256,0),(0,256),(True,0),(1,False)):
            with self.assertRaises(ValueError):bit_signature_permanent(x,y)
            with self.assertRaises(ValueError):channel_kernel(x,y)
        m=fixture(1,"lex")
        with self.assertRaises(ValueError):six_channel_original_cohort(m,side=2)
        with self.assertRaises(ValueError):six_channel_original_cohort(m,root=15)
        with self.assertRaises(ValueError):six_channel_original_cohort(m,pair_offset=3)
        with self.assertRaises(ValueError):six_channel_original_cohort(m,max_C4=0)
        with self.assertRaises(ValueError):
            six_channel_original_cohort(m,four_sources=(0,1,2,3))
        with self.assertRaises(ValueError):
            six_channel_original_cohort(dict(m,right_labels=((0,1),)*15))

if __name__=="__main__":
    unittest.main()
