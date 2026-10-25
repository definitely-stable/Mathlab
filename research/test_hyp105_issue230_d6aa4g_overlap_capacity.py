"""D6-AA4-G independent local cluster and D6-X/Y capacity falsifiers."""
import random
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4g_overlap_capacity import (
    complete_fixed_image_states,overlapping_triad_certificate,
    analytical_X_Y_capacity_checks)


class OverlapCapacityTests(unittest.TestCase):
    def test_real_four_original_source_factor_injections_exact(self):
        for types,base,n in [
            (("P","P","P","P"),(0,1,2,3),24),
            (("P","P","P","L"),(0,1,2,0),6),
            (("P","P","L","L"),(0,1,0,1),4),
            (("P","L","L","L"),(0,0,1,2),6),
            (("L","L","L","L"),(0,1,2,3),24)]:
            states=complete_fixed_image_states(types,base)
            self.assertEqual(len(states),n)
            self.assertEqual(len(set(states)),n)
            self.assertEqual(states[0],base)
            for st in states:
                for ty in ("P","L"):
                    slots=[st[i] for i,t in enumerate(types) if t==ty]
                    self.assertEqual(len(slots),len(set(slots)))
        with self.assertRaises(ValueError):
            complete_fixed_image_states(("P",)*4,(0,0,2,3))
        with self.assertRaises(ValueError):
            complete_fixed_image_states(("P",)*4,(0,1,2))

    def test_random_motif_true_support_sound_all_twelve_covers(self):
        rng=random.Random(230)
        for types,base in [
            (("P",)*4,(0,1,2,3)),
            (("P","P","L","L"),(0,1,0,1))]:
            states=complete_fixed_image_states(types,base)
            for _ in range(35):
                terms=[]
                for _ in range(20):
                    scope=tuple(i for i in range(4) if rng.randrange(2))
                    sampled={tuple(st[i] for i in scope) for st in states}
                    values={v:rng.randrange(8) for v in sampled}
                    costs=tuple(values[tuple(st[i] for i in scope)] for st in states)
                    terms.append((scope,costs))
                r=overlapping_triad_certificate(types,states,terms)
                self.assertEqual(len(r["all_twelve_covers"]),12)
                self.assertLessEqual(r["independent_Q_lower"],r["best_separate_triad_lower"])
                self.assertLessEqual(r["best_separate_triad_lower"],r["best_shared_pair_separator_lower"])
                self.assertLessEqual(r["best_shared_pair_separator_lower"],r["true_joint_four_factor_minimum"])
                self.assertEqual(r["true_joint_four_factor_minimum"],
                                 min(sum(term[1][i] for term in terms)
                                     for i in range(len(states))))

    def test_separator_overlap_strictly_better_than_unlinked_triads(self):
        states=complete_fixed_image_states(("P",)*4,(0,1,2,3))
        # Two costs demand contradictory labels for shared source factor 1.
        terms=[((1,),tuple(int(s[1]!=0) for s in states)),
               ((1,),tuple(int(s[1]!=1) for s in states))]
        # Shared pair min must see common value if both costs are included
        # in one group. It is exact here regardless of admissible cover.
        r=overlapping_triad_certificate(("P",)*4,states,terms)
        self.assertEqual(r["independent_Q_lower"],0)
        self.assertEqual(r["true_joint_four_factor_minimum"],1)
        self.assertEqual(r["best_shared_pair_separator_lower"],1)

    def test_fail_closed_illegal_Q_support_and_incomplete_states(self):
        types=("P",)*4
        states=complete_fixed_image_states(types,(0,1,2,3))
        with self.assertRaises(ValueError):
            overlapping_triad_certificate(types,states[:-1],())
        with self.assertRaises(ValueError):
            overlapping_triad_certificate(types,states,[((0,0),(0,)*24)])
        with self.assertRaises(ValueError):
            overlapping_triad_certificate(types,states,[((4,),(0,)*24)])
        with self.assertRaises(ValueError):
            overlapping_triad_certificate(types,states,[((0,),(-1,)*24)])
        # Cost changes with source factor 3, though claimed only factor 0.
        with self.assertRaises(AssertionError):
            overlapping_triad_certificate(types,states,[
                ((0,),tuple(int(st[3]==0) for st in states))])

    def test_D6X_projective_star_lift_negative_exact(self):
        r=analytical_X_Y_capacity_checks(4)
        self.assertEqual((r["V"],r["a"],r["K"],r["m"]),(85,14,91,6))
        self.assertTrue(r["D6X_star_pseudo_fails_column_lift"])
        self.assertEqual(Fraction(r["D6X_star_pseudo_column_lift_slack"]),
                         Fraction(-5,182))
        self.assertTrue(r["not_a_GF5_seven_family_lower_bound"])

    def test_D6Y_global_image_cut_rejects_selected_pair_marginals(self):
        r=analytical_X_Y_capacity_checks(4)
        self.assertEqual(r["all_real_images_max_adjacent_pairs"],963)
        self.assertEqual(r["D6Y_selected_two_site_pseudo_adjacent_pairs"],1020)
        self.assertEqual(r["D6Y_selected_two_site_gap"],57)
        for h in range(1,9):
            r=analytical_X_Y_capacity_checks(2**h)
            self.assertGreaterEqual(r["D6Y_selected_two_site_gap"],0)
            self.assertEqual(r["missing_star_constructive_achiever"],
                             r["all_real_images_max_adjacent_pairs"])
            self.assertEqual(r["D6Y_selected_two_site_gap"],
                             r["m"]*(r["a"]-2)-r["m"]*(r["m"]-1)//2)
            self.assertEqual(r["D6Y_pseudo_passes_selected_column_lifts_but_not_global_quad_cut"],
                             bool(r["m"]))


if __name__=="__main__":
    unittest.main()
