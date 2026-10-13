"""All-h Hall uniqueness structural source-GQ proof gates for JPKC-008."""
from collections import Counter
from itertools import combinations,permutations
import unittest

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc008_source_hall_coherence import (
    hall_certificate,hall_coherence_certificate,
    all_W32_factor_triples_hall_theorem,
)


class JPKC008Tests(unittest.TestCase):
    def test_complete_original_W32_all_207025_source_3x3_factors(self):
        m=fixture(1,"S68")
        result=all_W32_factor_triples_hall_theorem(m)
        self.assertEqual(result["entire_original_3x3_source_factor_grid"],207025)
        self.assertEqual(sum(result["true_GQ_hall_deficiency_histogram"].values()),207025)
        self.assertTrue(result["all_h_unique_original_perfect_matching_verified"])

    def test_true_W32_all_four_original_shared_source_demand_moments(self):
        reference={
            # E physical seeds, number of 3x3 pairs, Hall feasible,
            # true ORIGINAL A/A positional mismatch, selected D6
            "lex":(786,3144,288,224,64),
            "reverse":(676,2704,152,128,24),
            "S68":(544,2176,54,54,0),
            "S72":(600,2400,84,84,0),
        }
        for scheme,(E,total,feasible,unaligned,D6) in reference.items():
            with self.subTest(scheme=scheme):
                r=hall_coherence_certificate(fixture(1,scheme))
                self.assertEqual(r["actual_endpoint_bad_P3_examined"],E)
                self.assertTrue(r["complete_endpoint_bad_census"])
                self.assertTrue(r["J25_all_h_girth8_unique_3x3_matching"])
                self.assertTrue(r["J26_all_h_Hall_3subset_exact"])
                self.assertTrue(r["J27_all_h_source_matched_D6_telescope"])
                self.assertTrue(r["J27_global_original_factor_key_shared_across_all_anchors"])
                d=r["source_matching_deficit"]
                self.assertEqual(d["source_triple_pairs"],total)
                self.assertEqual(d["hall_deficient_pairs"],total-feasible)
                self.assertEqual(d["hall_feasible_pairs"],feasible)
                self.assertEqual(d["nonaligned_AA"],unaligned)
                self.assertEqual(d["aligned_D6"],D6)
                self.assertFalse(r["root_A_proved"])
                self.assertEqual(
                    r["unique_Hall_feasible_original_factor_pairs"]<=feasible,
                    True)
                self.assertGreaterEqual(
                    r["source_demands_repeated_over_different_physical_P3"],0)

    def test_true_W34_original_lex_random_global_source_hall_demand(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                r=hall_coherence_certificate(
                    fixture(2,scheme),limit_seeds=8,exact_W32=False)
                self.assertEqual(r["actual_endpoint_bad_P3_examined"],8)
                self.assertFalse(r["complete_endpoint_bad_census"])
                self.assertFalse(r["full_W34_original_seven_GF5_census"])
                self.assertTrue(r["J25_all_h_girth8_unique_3x3_matching"])
                self.assertGreater(r["original_source_demand_pair_budget"],0)
                d=r["source_matching_deficit"]
                self.assertEqual(d["source_triple_pairs"],
                                 d["hall_deficient_pairs"]+d["hall_feasible_pairs"])
                self.assertEqual(d["hall_feasible_pairs"],
                                 d["aligned_D6"]+d["nonaligned_AA"])

    def test_true_D4_original_spread_coherent_hall_demand(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        m,cert=spread_adversary_model(2)
        self.assertEqual(cert["M_f_original_exact"],259)
        r=hall_coherence_certificate(m,limit_seeds=8,exact_W32=False)
        self.assertEqual(r["actual_endpoint_bad_P3_examined"],8)
        self.assertFalse(r["complete_endpoint_bad_census"])
        self.assertGreater(r["original_source_demand_pair_budget"],0)
        self.assertFalse(r["root_B_constructed"])

    def test_true_independent_Hall_three_factor_subsets_versus_brute(self):
        ctx=ProjectionClosure(fixture(1,"lex"))
        # Deliberately use widely dispersed true original source factor
        # triples, including both Hall-feasible and Hall-deficient pairs.
        cases=[]
        for P in combinations(range(ctx.v),3):
            for L in combinations(range(ctx.v),3):
                h=hall_certificate(ctx,P,L)
                if h["hall_feasible"]:
                    cases.append((P,L,h))
                    break
            if len(cases)>3:
                break
        self.assertTrue(cases)
        for P,L,h in cases:
            self.assertEqual(h["matched_incidence_permutations"],1)
            self.assertEqual(h["deficiency"],0)
            ids=h["unique_original_matching_ids"]
            self.assertEqual(len(ids),3)
            self.assertEqual(len(set(ids)),3)
        absent=hall_certificate(ctx,(0,1,2),(0,1,2))
        self.assertGreaterEqual(absent["deficiency"],0)
        with self.assertRaisesRegex(ValueError,"distinct ORIGINAL"):
            hall_certificate(ctx,(0,0,1),(0,1,2))
        with self.assertRaisesRegex(ValueError,"out-of-range"):
            hall_certificate(ctx,(0,1,15),(0,1,2))

    def test_fail_closed_limits_invalid_original_maps_and_out_of_scope(self):
        with self.assertRaisesRegex(ValueError,"W32 only"):
            all_W32_factor_triples_hall_theorem(fixture(2,"lex"))
        with self.assertRaisesRegex(ValueError,"budget"):
            all_W32_factor_triples_hall_theorem(fixture(1,"lex"),max_checks=1)
        with self.assertRaisesRegex(ValueError,"W32 only"):
            hall_coherence_certificate(fixture(2,"lex"),exact_W32=True)
        with self.assertRaisesRegex(ValueError,"budget"):
            hall_coherence_certificate(fixture(1,"S68"),max_source_demand_pairs=1)
        with self.assertRaisesRegex(ValueError,"source seed limit"):
            hall_coherence_certificate(fixture(1,"lex"),limit_seeds=0)
        m=fixture(1,"S68")
        f=list(m["left_labels"]);f[0]=f[1]
        m["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            hall_coherence_certificate(m)


if __name__=="__main__":
    unittest.main()
