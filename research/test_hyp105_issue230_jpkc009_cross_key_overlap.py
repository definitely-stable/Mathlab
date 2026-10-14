"""Independent genuine ORIGINAL GQ triple Hall stars and cross-key overlaps."""
from collections import Counter
from itertools import combinations
from math import comb
import unittest

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc009_cross_key_overlap import (
    point_triple_matching_capacity,line_triple_matching_capacity,
    global_triple_capacity_identity,cross_key_certificate,
)
from hyp105_issue230_jpkc008_source_hall_coherence import (
    all_h_original_3matching_capacity,
)


class JPKC009Tests(unittest.TestCase):
    def test_all_455_original_W32_point_triple_Hall_star_capacities(self):
        ctx=ProjectionClosure(fixture(1,"S68"))
        histogram=Counter()
        sumcap=0
        for P in combinations(range(ctx.v),3):
            x=point_triple_matching_capacity(ctx,P,check_direct=True)
            histogram[(x["collinear_point_pairs"],
                       x["single_common_original_line"])]+=1
            sumcap+=x["unique_original_line_triples_satisfying_Hall"]
        self.assertEqual(sum(histogram.values()),comb(15,3))
        self.assertEqual(sumcap,10560)
        self.assertEqual(
            sum(n*(3**3-3*c+2*t) for (c,t),n in histogram.items()),10560)
        self.assertFalse((3,0) in histogram)

    def test_all_455_original_W32_line_triple_Hall_star_capacities(self):
        ctx=ProjectionClosure(fixture(1,"S72"))
        histogram=Counter()
        sumcap=0
        for L in combinations(range(ctx.v),3):
            x=line_triple_matching_capacity(ctx,L,check_direct=True)
            histogram[(x["concurrent_line_pairs"],
                       x["single_common_original_point"])]+=1
            sumcap+=x["unique_original_point_triples_satisfying_Hall"]
        self.assertEqual(sum(histogram.values()),comb(15,3))
        self.assertEqual(sumcap,10560)
        self.assertFalse((3,0) in histogram)

    def test_global_original_W32_W34_Hall_capacities_from_two_independent_formulas(self):
        for power,scheme in ((1,"S68"),(2,"lex"),(2,"random")):
            with self.subTest(power=power,scheme=scheme):
                ctx=ProjectionClosure(fixture(power,scheme))
                x=global_triple_capacity_identity(ctx,full_brute=power==1)
                y=all_h_original_3matching_capacity(ctx)
                self.assertEqual(
                    x["source_matching_capacity_from_point_triples"],
                    y["original_three_edge_matchings_exact_formula"])
                self.assertTrue(x["J32_exact_global_source_capacity_identity"])
                self.assertEqual(x["original_collinear_point_pair_count"],
                                 ctx.v*comb(ctx.delta,2))
                if power==1:
                    self.assertTrue(x["complete_original_triple_sum_checked"])
                    self.assertEqual(x["source_matching_capacity_from_point_triples"],10560)
                else:
                    self.assertFalse(x["complete_original_triple_sum_checked"])

    def test_genuine_original_W32_all_endpoint_bad_P3_demand_graph(self):
        references={
            # E, total demanded original A/A triple key occurrences,
            # distinct source factor keys, unique feasible keys
            "lex":(786,3144,1380,126),
            "reverse":(676,2704,1228,71),
            "S68":(544,2176,1016,27),
            "S72":(600,2400,1092,35),
        }
        for scheme,(E,demand,unique,feasible) in references.items():
            with self.subTest(scheme=scheme):
                row=cross_key_certificate(
                    fixture(1,scheme),full_global_source_triples=True)
                self.assertTrue(row["complete_original_endpoint_bad_seed_census"])
                self.assertEqual(row["exact_endpoint_bad_physical_P3_examined"],E)
                self.assertEqual(row["original_demand_stage"][
                    "original_source_pair_demand_occurrences"],demand)
                self.assertEqual(row["distinct_original_bipartite_source_demand_edges"],unique)
                self.assertEqual(row["repeated_source_edge_demand_occurrences"],demand-unique)
                self.assertEqual(row["original_Hall_feasible_distinct_source_edges"],feasible)
                self.assertTrue(row["all_h_J30_unique_one_sided_source_triple_anchor"])
                self.assertTrue(row["all_h_J31_exact_left_and_dual_Hall_star_capacity"])
                self.assertTrue(row["all_h_J32_global_capacity_equals_J29"])
                self.assertTrue(row["all_h_J33_cross_key_demand_graph_double_count_exact"])
                self.assertTrue(row["J34_exact_nested_Hall_vs_positive_overlap_certified"])
                for side in ("left","right"):
                    raw=row[side+"_point_triple_source_overlap"] if side=="left" else row["right_line_triple_source_overlap"]
                    hall=row[side+"_Hall_feasible_source_overlap"]
                    positive=row[side+"_actual_GF5_D6_source_overlap"]
                    for key in (
                        "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors",
                        "distinct_key_pairs_same_source_triple_same_original_anchor"):
                        self.assertLessEqual(positive[key],hall[key])
                        self.assertLessEqual(hall[key],raw[key])
                if scheme in ("S68","S72"):
                    self.assertGreater(
                        row["left_point_triple_source_overlap"][
                            "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors"],0)
                    self.assertGreater(
                        row["right_line_triple_source_overlap"][
                            "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors"],0)
                    self.assertEqual(
                        row["original_demand_stage"].get("original_selected_D6_occurrences",0),0)
                    self.assertEqual(
                        row["left_actual_GF5_D6_source_overlap"][
                            "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors"],0)
                    self.assertEqual(
                        row["right_actual_GF5_D6_source_overlap"][
                            "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors"],0)
                self.assertTrue(row["complete_source_triple_star_capacity_checked"])
                self.assertEqual(
                    row["global_original_source_Hall_capacity"][
                        "source_matching_capacity_from_point_triples"],10560)
                self.assertEqual(
                    row["original_demand_stage"]["original_Hall_feasible_occurrences"],
                    sum(row["original_demand_stage"].get(field,0) for field in (
                        "original_selected_D6_occurrences",
                        "original_AA_nonaligned_occurrences")))
                self.assertFalse(row["root_A_proved"])

    def test_true_W34_three_original_global_maps_and_partial_source_scope(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        original=[("lex",fixture(2,"lex")),
                  ("random",fixture(2,"random"))]
        spread,cert=spread_adversary_model(2)
        self.assertEqual(cert["M_f_original_exact"],259)
        original.append(("D4-true-spread",spread))
        for name,model in original:
            with self.subTest(name=name):
                row=cross_key_certificate(model,limit_seeds=8)
                self.assertEqual(row["s"],4)
                self.assertEqual(row["exact_endpoint_bad_physical_P3_examined"],8)
                self.assertFalse(row["complete_original_endpoint_bad_seed_census"])
                self.assertGreater(row["distinct_original_bipartite_source_demand_edges"],0)
                self.assertTrue(row["all_h_J32_global_capacity_equals_J29"])
                self.assertTrue(row["does_not_prove_cross_anchor_positive_extension"])

    def test_fail_closed_original_maps_source_triples_and_budgets(self):
        ctx=ProjectionClosure(fixture(1,"lex"))
        with self.assertRaisesRegex(ValueError,"three distinct"):
            point_triple_matching_capacity(ctx,(0,0,1))
        with self.assertRaisesRegex(ValueError,"three distinct"):
            line_triple_matching_capacity(ctx,(0,1,15))
        with self.assertRaisesRegex(ValueError,"budget"):
            cross_key_certificate(fixture(1,"lex"),max_keys=1)
        with self.assertRaisesRegex(ValueError,"source seed limit"):
            cross_key_certificate(fixture(1,"lex"),limit_seeds=0)
        with self.assertRaisesRegex(ValueError,"path budget"):
            cross_key_certificate(fixture(1,"S68"),max_paths=1)
        wrong=fixture(1,"S72")
        left=list(wrong["left_labels"])
        left[0]=left[1]
        wrong["left_labels"]=tuple(left)
        with self.assertRaises(ValueError):
            cross_key_certificate(wrong)


if __name__=="__main__":
    unittest.main()
