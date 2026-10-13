"""HYP-105 D6-Y: independent sharp image bound and fractional occupancy gap."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6y_capacity_adjacency_cut import (
    sharp_adjacency_image_bound,constructive_sharp_original_injection,
    pairwise_capacity_saturated_distribution,graph_adjacency_count,
    edge_adjacent,independent_full_pair_oracle,
    independent_missing_edge_brute,report,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_proof_audit import parameters


def independent_quadratic_count(physical):
    """Brute unordered PAIRS, deliberately not degree-Counter code path."""
    count=0
    for a,b in combinations(physical,2):
        if len(set(a).intersection(b))==1:
            count+=1
    return count


class D6YGlobalImageCapacityTests(unittest.TestCase):
    def test_all_h_sharp_closed_form_and_minimal_palette(self):
        for h in range(1,10):
            s=2**h
            row=sharp_adjacency_image_bound(s)
            a,V,K,m=(row[k] for k in
                      ("a","V","K","missing_physical_edges"))
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertGreaterEqual(K,V)
            self.assertLess(comb(a-1,2),V)
            self.assertLessEqual(m,a-2)
            self.assertEqual(row["sharp_max_occupied_adjacent_unordered_pairs"],
                             a*comb(a-1,2)-2*m*(a-2)+comb(m,2))
            cap=Fraction(row["pairwise_lifted_capacity_upper"])
            sharp=Fraction(row["true_global_random_original_pair_adjacent_upper"])
            expected_gap=Fraction(m*(2*(a-2)-m+1),V*(V-1))
            self.assertEqual(cap-sharp,expected_gap)
            self.assertEqual(bool(cap>sharp),m>0)
        self.assertEqual(sharp_adjacency_image_bound(4)["missing_physical_edges"],6)

    def test_original_geometry_real_W32_W34_W38_sharp_constructed(self):
        for power in (1,2,3):
            s=2**power
            model=fixture(power,"lex")
            true=tuple(model["incidences"])
            geo=parameters(s)
            self.assertEqual(len(true),geo["V"]*(s+1))
            witness=constructive_sharp_original_injection(s)
            L=witness["left_original_labels"]
            R=witness["right_original_labels"]
            self.assertEqual(len(L),geo["V"])
            self.assertEqual(len(R),geo["V"])
            self.assertEqual(len(set(L)),len(L))
            self.assertEqual(len(set(R)),len(R))
            bound=sharp_adjacency_image_bound(s)[
                "sharp_max_occupied_adjacent_unordered_pairs"]
            self.assertEqual(witness["exact_adjacent_left_unordered_original_point_pairs"],
                             bound)
            self.assertEqual(independent_quadratic_count(L),bound)
            self.assertEqual(independent_quadratic_count(R),bound)
            self.assertEqual(graph_adjacency_count(L,geo["a"]),bound)

    def test_complete_two_original_site_exact_marginals_and_selected_lifts(self):
        for s in (2,4):
            x=independent_full_pair_oracle(s)
            K=parameters(s)["K"]
            self.assertEqual(x["ordered_distinct_physical_pair_cases"],K*(K-1))
            self.assertEqual(x[
                "all_physical_column_lifts_for_any_first_original_point_label"],"PASS")
            self.assertEqual(x[
                "every_original_pair_marginal_normalizes_to_uniform"],"PASS")
        for h in range(1,10):
            s=2**h
            d=pairwise_capacity_saturated_distribution(s)
            self.assertTrue(d["selected_rank_two_physical_column_lifts_feasible"])
            self.assertTrue(d["joint_marginals_exactly_normalized_and_exchangeable"])
            self.assertTrue(d["physical_row_injectivity_two_sites"])
            self.assertEqual(
                Fraction(d["uniform_original_site_edge_marginal"]),
                Fraction(1,d["K"]))
            self.assertEqual(d["global_image_quadratic_cut_violated"],
                             d["K"]>d["V"])
            self.assertLessEqual(
                Fraction(d["distinct_original_point_joint_disjoint"]),
                Fraction(1,d["K"]*(d["V"]-1)))
            self.assertEqual(
                Fraction(d["expected_total_adjacent_original_point_pairs"])-
                Fraction(d["maximum_for_any_global_point_injection"]),
                Fraction(sharp_adjacency_image_bound(s)[
                    "sharp_integrality_gap_adjacent_pair_count"]))

    def test_full_exhaustive_missing_images_exact_smal_alphabets(self):
        for a,m in ((5,3),(6,4),(7,5)):
            x=independent_missing_edge_brute(a,m)
            self.assertEqual(x["all_missing_image_subsets_checked"],
                             comb(comb(a,2),m))
            self.assertTrue(x["sharp_missing_star_extremum_attained"])
            self.assertGreater(x["number_tied_extremizers"],0)

    def test_true_first_nonzero_gap_s4_exact_arithmetic(self):
        x=sharp_adjacency_image_bound(4)
        self.assertEqual((x["a"],x["V"],x["K"],x["missing_physical_edges"]),
                         (14,85,91,6))
        self.assertEqual(x["complete_Ka_adjacent_unordered_edge_pairs"],1092)
        self.assertEqual(x["sharp_max_occupied_adjacent_unordered_pairs"],963)
        self.assertEqual(
            Fraction(x["pairwise_lifted_capacity_upper"]),Fraction(2,7))
        self.assertEqual(
            Fraction(x["true_global_random_original_pair_adjacent_upper"]),
            Fraction(321,1190))
        self.assertEqual(
            Fraction(x["sharp_integrality_gap_random_pair_probability"]),
            Fraction(19,1190))
        d=pairwise_capacity_saturated_distribution(4)
        self.assertEqual(
            Fraction(d["expected_total_adjacent_original_point_pairs"]),1020)
        self.assertEqual(
            Fraction(d["global_image_quadratic_capacity_cut_slack"]),-57)
        self.assertTrue(d["global_image_quadratic_cut_violated"])

    def test_pair_orbit_is_not_claimed_actual_global_or_standard_SA(self):
        for h in range(1,6):
            z=pairwise_capacity_saturated_distribution(2**h)
            self.assertTrue(z["pairwise_marginals_not_claimed_extendible"])
            self.assertTrue(z["standard_SA_feasibility_not_claimed"])
        z=sharp_adjacency_image_bound(2)
        self.assertEqual(z["missing_physical_edges"],0)
        self.assertEqual(z["sharp_integrality_gap_adjacent_pair_count"],"0")

    def test_fail_closed_budget_duplicate_and_noncanonical(self):
        with self.assertRaises(ValueError):
            graph_adjacency_count(((0,1),(0,1)),6)
        with self.assertRaises(ValueError):
            graph_adjacency_count(((2,0),),6)
        with self.assertRaises(ValueError):
            graph_adjacency_count(((0,6),),6)
        with self.assertRaises(ValueError):
            graph_adjacency_count(((0,1),),3)
        with self.assertRaises(ValueError):
            constructive_sharp_original_injection(4,max_labels=20)
        with self.assertRaises(ValueError):
            independent_full_pair_oracle(4,max_k=10)
        with self.assertRaises(ValueError):
            independent_missing_edge_brute(7,5,max_subsets=100)
        with self.assertRaises(ValueError):
            independent_missing_edge_brute(5,4)

    def test_report_honest_no_root_theorem(self):
        x=report()
        self.assertEqual(x["theorem"],
                         "ALL-H-SHARP-GLOBAL-TYPED-PHYSICAL-IMAGE-ADJACENCY")
        self.assertEqual(x["stronger_quadratic_global_image_cut"],
                         "NECESSARY-AND-SHARP")
        self.assertEqual(x["global_injection_both_typed_sides"],"EXACT-ALL-H")
        self.assertTrue(x["not_full_GF5_seven_lower"])
        self.assertFalse(x["general_Sherali_Adams_gap_PROVED"])
        self.assertFalse(x["original_global_S_PROVED_A"])
        self.assertFalse(x["infinite_correlated_counterexample_PROVED_B"])
        self.assertEqual((x["Branch_A"],x["Branch_B"]),("OPEN","OPEN"))
        self.assertEqual(len(x["all_h_parameters"]),8)
        self.assertEqual(len(x["independent_full_missing_edge_oracle"]),3)


if __name__=="__main__":
    unittest.main()
