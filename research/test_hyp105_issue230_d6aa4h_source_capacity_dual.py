"""HYP-105 AA4-H independent rational LP/dual and ORIGINAL profile-cover falsifiers."""
import random
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4h_source_capacity_dual import (
    exact_one_cut_lagrangian,toy_capacity_source_coupling,
    greedy_original_profile_cover, certified_minimum_original_profile_cover,
)


class SourceCapacityDualTests(unittest.TestCase):
    def test_D6Y_exact_global_image_cut_dual_recovers_toy_one(self):
        r=toy_capacity_source_coupling(4)
        self.assertEqual(r["true_physical_adjacency_upper"],963)
        self.assertEqual(r["D6Y_false_expected_adjacency"],1020)
        self.assertEqual(r["D6Y_valid_cut_violation"],57)
        self.assertEqual(r["image_cut_dual"]["unconstrained_candidate_cost_floor"],"0")
        self.assertEqual(r["image_cut_dual"]["optimal_one_cut_dual_lower"],"1")
        self.assertEqual(r["image_cut_dual"]["nonnegative_exact_cut_multiplier"],"1/57")
        self.assertTrue(r["all_GF5_objectives_in_toys_are_synthetic"])
        self.assertTrue(r["no_universal_source_GQ_lower"])

    def test_D6X_exact_lifted_global_column_dual_recovers_toy_one(self):
        r=toy_capacity_source_coupling(4)
        self.assertEqual(r["D6X_lifted_capacity_violation"],"5/182")
        z=r["lifted_column_cut_dual"]
        self.assertEqual(z["optimal_one_cut_dual_lower"],"1")
        self.assertEqual(z["nonnegative_exact_cut_multiplier"],"182/5")
        self.assertTrue(r["neither_pseudo_claimed_global_or_standard_SA_feasible"])

    def test_valid_capacity_price_can_leave_strict_gap(self):
        rows=(("true_global",2,-1),("unextendible_pseudo",0,1))
        z=exact_one_cut_lagrangian(rows)
        self.assertEqual(z["unconstrained_candidate_cost_floor"],"0")
        self.assertEqual(z["optimal_one_cut_dual_lower"],"1")
        self.assertEqual(z["nonnegative_exact_cut_multiplier"],"1")
        self.assertLess(Fraction(z["optimal_one_cut_dual_lower"]),2)

    def test_zero_capacity_slack_cannot_fix_original_source_relaxation(self):
        rows=(("true_0",68,0),("true_1",72,0),
              ("abstract_source_lower",63,0))
        z=exact_one_cut_lagrangian(rows)
        self.assertEqual(z["optimal_one_cut_dual_lower"],"63")
        self.assertEqual(z["nonnegative_exact_cut_multiplier"],"0")
        self.assertEqual(z["unconstrained_candidate_cost_floor"],"63")
        self.assertTrue(z["only_valid_for_this_explicit_candidate_universe"])

    def test_fail_closed_malformed_and_unbounded_candidate_sets(self):
        with self.assertRaises(ValueError):
            exact_one_cut_lagrangian([])
        with self.assertRaises(ValueError):
            exact_one_cut_lagrangian([("x",0,1)])
        with self.assertRaises(ValueError):
            exact_one_cut_lagrangian([("x",-1,0)])
        with self.assertRaises(ValueError):
            exact_one_cut_lagrangian([("x",1,0),("x",2,0)])
        with self.assertRaises(ValueError):
            exact_one_cut_lagrangian([("",0,0)])
        with self.assertRaises(ValueError):
            toy_capacity_source_coupling(2)

    def test_random_rational_weak_dual_correct_for_every_true_feasible_row(self):
        rng=random.Random(230)
        for _ in range(140):
            rows=[("true",Fraction(rng.randrange(13),rng.randrange(1,9)),
                   Fraction(-rng.randrange(5),rng.randrange(1,7)))]
            for k in range(rng.randrange(1,11)):
                rows.append(("candidate_%d"%k,
                             Fraction(rng.randrange(13),rng.randrange(1,9)),
                             Fraction(rng.randrange(-7,8),rng.randrange(1,9))))
            cert=exact_one_cut_lagrangian(rows)
            lam=Fraction(cert["nonnegative_exact_cut_multiplier"])
            bound=Fraction(cert["optimal_one_cut_dual_lower"])
            self.assertGreaterEqual(lam,0)
            self.assertEqual(bound,min(c+lam*g for _,c,g in rows))
            self.assertLessEqual(bound,min(c for _,c,g in rows if g<=0))
            self.assertLessEqual(Fraction(cert["unconstrained_candidate_cost_floor"]),bound)

    def test_original_line_profiles_sparse_cover_verified_over_24_states(self):
        full=(1<<24)-1
        rows=[((2,)*6, (1<<10)-1),
              ((4,)*6, ((1<<19)-1)^((1<<10)-1)),
              ((7,)*6, full^((1<<19)-1))]
        c=greedy_original_profile_cover(rows)
        self.assertEqual(c["complete_states_covered"],24)
        self.assertEqual(c["greedy_profiles_used"],3)
        self.assertEqual(c["independently_verified_cover_mask"],full)
        self.assertTrue(c["minimum_size_NOT_claimed"])
        self.assertEqual(len(c["greedy_selected_original_line_multisets"]),3)

    def test_original_profile_cover_can_use_one_globally_positive_profile(self):
        c=greedy_original_profile_cover([((1,2,3,4,5,6),15),
                                         ((0,)*6,7)])
        self.assertEqual(c["greedy_profiles_used"],1)
        self.assertEqual(c["complete_states_covered"],4)
        self.assertEqual(c["greedy_selected_original_line_multisets"],
                         ((1,2,3,4,5,6),))


    def test_minimum_source_profile_cover_exhaustively_certified_up_to_four(self):
        cases=[
            ([((1,),15),((2,),7)],1),
            ([((1,),3),((2,),12)],2),
            ([((1,),1),((2,),2),((3,),4)],3),
            ([((1,),1),((2,),2),((3,),4),((4,),8)],4),
            ([((1,),3),((2,),12),((3,),1)],2),
        ]
        for rows,expected in cases:
            c=certified_minimum_original_profile_cover(rows)
            self.assertEqual(c["exact_minimum_original_line_profiles"],expected)
            self.assertTrue(c["dominance_pruning_is_exact_for_unit_cover"])
            self.assertTrue(c["complete_search_for_all_smaller_cover_sizes"])
            witness=0
            for mask in c["exact_minimum_cover_masks"]:
                witness |= mask
            self.assertEqual(witness,c["full_true_original_state_mask"])
        with self.assertRaises(ValueError):
            certified_minimum_original_profile_cover(
                [((i,),1<<i) for i in range(5)])

    def test_independent_brute_small_random_exact_minimum_profile_cover(self):
        from itertools import combinations
        rng=random.Random(23048)
        for nstates in range(2,7):
            full=(1<<nstates)-1
            for _ in range(24):
                rows=[((j,),rng.randrange(1,1<<nstates))
                      for j in range(6)]
                # Guarantee every state has a positive original profile.
                rows.extend([((100+i,),1<<i) for i in range(nstates)])
                # Only request bounded proof when a greedy cover of <=4 exists.
                greedy=greedy_original_profile_cover(rows)
                if greedy["greedy_profiles_used"]>4:
                    continue
                witness=certified_minimum_original_profile_cover(rows)
                observed=witness["exact_minimum_original_line_profiles"]
                brute=None
                for k in range(1,greedy["greedy_profiles_used"]+1):
                    if any((__import__("functools").reduce(
                        int.__or__, (rows[i][1] for i in ix),0)==full)
                       for ix in combinations(range(len(rows)),k)):
                        brute=k
                        break
                self.assertEqual(observed,brute)

    def test_original_profile_cover_fails_if_any_actual_state_has_no_witness(self):
        with self.assertRaises(ValueError):
            greedy_original_profile_cover([])
        with self.assertRaises(ValueError):
            greedy_original_profile_cover([((0,)*6,0)])
        with self.assertRaises(ValueError):
            greedy_original_profile_cover([((0,)*6,3),((0,)*6,1)])
        # Profile mask controls n as highest observed state; a real
        # scenario needs externally verified exactly n=24 from census.
        cover=greedy_original_profile_cover([((0,)*6,1)])
        self.assertEqual(cover["complete_states_covered"],1)


if __name__=="__main__":
    unittest.main()
