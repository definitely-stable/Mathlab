"""Definition-level independent root-52 and genuine original seven-GF5 five-swap audits."""
import random
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb, factorial

from hyp105_issue230_d6aa4at_seven_swap_boundary import (
    rooted_k6_2regular_multigraph_oracle,
    all_h_seven_original_line_fiber_bound,
    genuine_original_W32_five_swap_seven_boundary,
    R3_CERTIFIED_FLOORS,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, classify_seven_prechecked,
)
from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    repair_original_D6_with_at_most_five_line_swaps,
)


class AllOriginalSevenFiveSwapBoundaryTests(unittest.TestCase):
    def test_01_independent_all_K6_multigraphs_and_all_15_edge_root_symmetry(self):
        # No call to theorem's oracle for the main counting: independently
        # choose multisets of six K6 unordered edges and inspect degrees.
        edges=list(combinations(range(6),2))
        counts=Counter()
        for six in combinations_with_replacement(edges,6):
            D=[0]*6
            for u,v in six:
                D[u]+=1;D[v]+=1
            if D != [2]*6:
                continue
            freq=Counter(six)
            profile=tuple(sorted(freq.values(),reverse=True))
            ty={(1,)*6:"A",(2,1,1,1,1):"B",(2,2,2):"C"}[profile]
            counts[ty]+=1
        self.assertEqual(counts,{"A":70,"B":45,"C":15})
        self.assertEqual(sum(counts.values()),130)

        rooted={e:Counter() for e in edges}
        for six in combinations_with_replacement(edges,6):
            D=[0]*6
            for u,v in six:
                D[u]+=1;D[v]+=1
            if D!=[2]*6:
                continue
            multiplicity=Counter(six)
            profile=tuple(sorted(multiplicity.values(),reverse=True))
            ty={(1,)*6:"A",(2,1,1,1,1):"B",(2,2,2):"C"}[profile]
            for edge,n in multiplicity.items():
                rooted[edge][ty]+=n
        self.assertEqual(set(tuple(sorted(c.items())) for c in rooted.values()),
                         {(('A',28),('B',18),('C',6))})
        self.assertEqual(rooted_k6_2regular_multigraph_oracle()[
            "fixed_edge_rooted_occurrence_count_by_profile"],{"A":28,"B":18,"C":6})
        # All fifteen root edges have 52 occurrences, while unrooted total
        # edges across 130 original multigraphs is 130*6=780=15*52.
        self.assertEqual(sum(map(lambda d:sum(d.values()),rooted.values())),780)

    def test_02_exact_all_h_dyadic_five_swap_original_fiber_numerator(self):
        for h in tuple(range(1,35))+(40,64,80):
            s=1<<h
            z=all_h_seven_original_line_fiber_bound(s)
            a=z["a"];d=s+1
            c=comb(a-2,4)
            self.assertEqual(
                z["total_left_2regular_original_Q_cap_per_original_line"],
                6240*d**6*c)
            self.assertEqual(
                z["weighted_51palette_GF5_necessary_floor_numerator_change_abs_bound"],
                10*300312000*d**6*c)
            self.assertEqual(sum(z["exact_rooted_physical_multiset_counts"].values()),52)
            self.assertFalse(z["original_seven_minimax_proved"])
            self.assertTrue(z["theorem_new_bound_is_O_s12_not_lower_s6"])
            if s>=4:
                self.assertLessEqual(z["all_seven_tag_change_abs_bound_for_at_most_t_changed_lines"],
                                     160000*s**12)

    def test_03_rooted_type_separate_cap_and_original_GF5_51_weights(self):
        z=all_h_seven_original_line_fiber_bound(2)
        self.assertEqual(z["exact_rooted_physical_multiset_counts"],{"A":28,"B":18,"C":6})
        self.assertEqual({k:v//(factorial(5)*3**6)
                          for k,v in z["source_line_fiber_cap_by_left_A_B_C"].items()},
                         {"A":28,"B":18,"C":6})
        self.assertEqual(R3_CERTIFIED_FLOORS["D6"],5643)
        self.assertEqual(R3_CERTIFIED_FLOORS["C/B"],49050)
        self.assertEqual(R3_CERTIFIED_FLOORS["B/B-overlap"],51750)
        with self.assertRaises(ValueError):
            all_h_seven_original_line_fiber_bound(3)
        with self.assertRaises(ValueError):
            all_h_seven_original_line_fiber_bound(2,affected_lines=11)
        with self.assertRaises(ValueError):
            all_h_seven_original_line_fiber_bound(2,affected_lines=-1)

    def test_04_source_original_W32_independent_single_line_coverage(self):
        # Counts are definition-level and use the historical 62,370
        # actual distinct original-incidence LEFT 2-factor source six-Q.
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            originals=tuple(tuple(x) for x in model["incidences"])
            actual={l:Counter() for l in range(15)}
            S=0
            for ids,kind in selected_left_six(model):
                S+=1
                self.assertEqual(len(set(ids)),6)
                self.assertIn(kind,("A","B","C"))
                for l in {originals[i][1] for i in ids}:
                    actual[l][kind]+=1
            self.assertEqual(S,62370)
            b=all_h_seven_original_line_fiber_bound(2,affected_lines=1)
            for l,row in actual.items():
                for ty in ("A","B","C"):
                    self.assertLessEqual(row[ty],b["source_line_fiber_cap_by_left_A_B_C"][ty])
                self.assertLessEqual(sum(row.values()),
                                     b["total_left_2regular_original_Q_cap_per_original_line"])
            self.assertGreater(sum(map(lambda r:sum(r.values()),actual.values())),0)

    def test_05_actual_original_S68_S72_five_swap_full_seven_signed_support(self):
        for scheme,original_seven in (("S68",68),("S72",72)):
            z=genuine_original_W32_five_swap_seven_boundary(scheme)
            self.assertEqual(z["original_seven_S_before"],original_seven)
            self.assertEqual(z["total_original_six_ID_left_2regular_candidates"],62370)
            self.assertEqual(z["repaired_Q_true_original_D6_verified"],True)
            self.assertLessEqual(z["five_swap_global_original_line_steps"],5)
            self.assertLessEqual(z["number_of_distinct_actual_source_line_labels_ever_swapped"],10)
            self.assertEqual(z["original_seven_S_signed_change"],
                             z["repaired_seven_S_after"]-z["original_seven_S_before"])
            self.assertEqual(sum(q["signed_seven_delta_total"] for q in
                                 z["each_swap_true_original_source_line_sparse_details"]),
                             z["original_seven_S_signed_change"])
            self.assertEqual(sum(q["signed_selected_GF5_floor_numerator_delta"] for q in
                                 z["each_swap_true_original_source_line_sparse_details"]),
                             z["original_selected_GF5_floor_numerator_signed_change"])
            self.assertGreater(z["actual_source_line_cut_candidate_Q"],0)
            self.assertTrue(z["independent_complete_original_census_compared"])
            expected={
                "S68": (169,101,61699,165,64,4386335),
                "S72": (159,87,62349,158,71,3849249),
            }[scheme]
            actual=(
                z["repaired_seven_S_after"],
                z["original_seven_S_signed_change"],
                z["actual_source_line_cut_candidate_Q"],
                z["accepted_original_six_ID_Q_gained"],
                z["accepted_original_six_ID_Q_lost"],
                z["original_selected_GF5_floor_numerator_signed_change"],
            )
            self.assertEqual(actual,expected)
            self.assertFalse(z["this_bound_PROVES_root_A_B_C"])

    def test_06_actual_original_lex_reverse_second_oracle_no_fake_zero_claim(self):
        for scheme in ("lex","reverse"):
            z=genuine_original_W32_five_swap_seven_boundary(scheme)
            independent=seven_census(fixture(1,scheme),independent_checks=False)
            self.assertEqual(z["original_seven_S_before"],independent["S_seven"])
            self.assertEqual(z["original_7class_before"],
                             {k:v for k,v in independent["seven_class_motif_counts"].items()
                              if v!=0})
            self.assertTrue(z["independent_complete_original_census_compared"])
            expected={
                "lex": (259,180,-79,61439,165,244,-3167553),
                "reverse": (169,189,20,61147,180,160,975177),
            }[scheme]
            actual=(
                z["original_seven_S_before"],
                z["repaired_seven_S_after"],
                z["original_seven_S_signed_change"],
                z["actual_source_line_cut_candidate_Q"],
                z["accepted_original_six_ID_Q_gained"],
                z["accepted_original_six_ID_Q_lost"],
                z["original_selected_GF5_floor_numerator_signed_change"],
            )
            self.assertEqual(actual,expected)
            self.assertEqual(
                z["accepted_original_six_ID_Q_gained"]-z["accepted_original_six_ID_Q_lost"],
                z["original_seven_S_signed_change"])
            if scheme=="lex":
                # ACTUAL original W32: globally legal +D6 repair LOWERED
                # total seven-class positive S, refuting monotone transport.
                self.assertLess(z["original_seven_S_signed_change"],0)


if __name__=="__main__":
    unittest.main()
