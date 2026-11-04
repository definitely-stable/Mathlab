"""Independent all-ten-sign mutual exclusion proof on TRUE ORIGINAL W32/W34.

The previous AA4-SIGN10 signed counts are EXPECTATIONS OF THE SUM of
ten dependent signed events, not union probabilities in general.
New exact original dual-coordinate closure theorem proves that
for D6 and B/B-overlap specifically, the ten signs CANNOT coincide,
because any overlap implies forbidden singleton or genuine 2v2.
This test independently exhausts all 45 pairs of canonical balanced
partitions, all 15 size-four original source subsets of each physical
twelve-coordinate graph, and each of the actual full 51-palette signs.
"""
from fractions import Fraction
from itertools import combinations
import copy
import unittest

from hyp105_gf5_original_sixid_flow_referee import (
    bb_overlap_templates,coincident_c6_template,
    planted_original_d6,planted_original_bb_overlap,
    SIGNS,gf5_flow_inclusion_exclusion,gf5_flow_spanning_tree)
from hyp105_original_ten_sign_exclusive import (
    Q_TEN,MIN_UNION_SIX_SIGNED,closed_four_flag_subsets,
    canonical_ten_original_signs_are_mutually_exclusive,
    original_ten_sign_union_counts,stronger_genuine_W32_original_tensign_packing,
    conditional_allh_exclusive_signed_palettes)


class OriginalExclusiveTenGF5SignTests(unittest.TestCase):
    def test_combinatorial_two_sign_overlap_always_R2_or_R1(self):
        self.assertEqual(len(SIGNS),10)
        for a,b in combinations(SIGNS,2):
            # Every canonical 3-vs-3 plus triple contains local ID 0,
            # global sign complement was identified exactly once.
            self.assertIn(0,a)
            self.assertIn(0,b)
            intersection=len(a&b)
            self.assertIn(intersection,(1,2))
            # Subtraction of two balanced GF5 equations implies an
            # equal-sum on 3-intersection original source columns each
            # side; R2 if common=1, R1 if common=2.
            self.assertEqual(len(a-b),3-intersection)
            self.assertEqual(len(b-a),3-intersection)

    def test_all_true_geometric_sixset_templates_have_NO_internal_R2_support(self):
        template=coincident_c6_template()
        self.assertEqual(closed_four_flag_subsets(template),())
        self.assertTrue(canonical_ten_original_signs_are_mutually_exclusive(
            template)["all_10_balanced_signed_GF5_events_pairwise_exclusive"])
        bb=list(bb_overlap_templates())
        self.assertEqual(len(bb),9)
        for i,edges in enumerate(bb):
            with self.subTest(BB_template=i):
                self.assertEqual(closed_four_flag_subsets(edges),())
                x=original_ten_sign_union_counts(edges,"B/B-overlap")
                self.assertIn(x[
                    "source_ten_sign_union_favorable_palette_assignments_exact"],
                    (53526,53838))
                self.assertEqual(
                    len(x["all_ten_original_signed_flow_counts"]),10)
                self.assertTrue(x[
                    "probability_may_be_summed_without_any_R2_or_singleton_overlap"])

    def test_true_original_W32_and_W34_planted_physical_maps_sixset_signs(self):
        for power in (1,2):
            for typ,maker,total in (
                ("D6",planted_original_d6,{54162}),
                ("B/B-overlap",planted_original_bb_overlap,{53526,53838})):
                with self.subTest(power=power,type=typ):
                    src=maker(power)
                    self.assertEqual(len(src["ids"]),6)
                    self.assertEqual(len(set(src["ids"])),6)
                    r=original_ten_sign_union_counts(src["edges"],typ)
                    self.assertIn(
                        r["source_ten_sign_union_favorable_palette_assignments_exact"],
                        total)
                    self.assertEqual(
                        r["source_four_flag_dual_closed_subsets"],[])

    def test_both_frozen_genuine_W32_source_sixset_packing_products_are_exact(self):
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                r=stronger_genuine_W32_original_tensign_packing(scheme)
                self.assertEqual(r["original_source_W32_flags"],45)
                self.assertEqual(r["source_disjoint_sixset_packing_size"],3)
                six=r["source_original_sixset_witnesses"]
                self.assertEqual(len({
                    i for x in six for i in x["original_source_IDs"]}),18)
                p=Fraction(1)
                for x in six:
                    v=x["ten_sign_GF5_full_51_palette_audit"]
                    self.assertEqual(
                        v["source_four_flag_dual_closed_subsets"],[])
                    count=v[
                        "source_ten_sign_union_favorable_palette_assignments_exact"]
                    self.assertGreaterEqual(count,53526)
                    p*=1-Fraction(count,51**6)
                exact=r["exact_independent_NO_motif_with_ANY_of_ten_signs_probability"]
                self.assertEqual(p,Fraction(exact["numerator"],exact["denominator"]))
                self.assertLessEqual(p,(1-Q_TEN)**3)
                self.assertFalse(r["root_allh_accepted_here"])

    def test_bad_synthetic_two_copy_components_are_REJECTED_not_source_evidence(self):
        # Adversarial algebraic test only, NOT a GQ source realization:
        # both colored projections equal three doubled disjoint pairs.
        side=((0,1),(0,1),(2,3),(2,3),(4,5),(4,5))
        fake=side+side
        self.assertTrue(closed_four_flag_subsets(fake))
        with self.assertRaises(AssertionError):
            canonical_ten_original_signs_are_mutually_exclusive(fake)
        with self.assertRaises(AssertionError):
            original_ten_sign_union_counts(fake,"D6")

    def test_allh_strictly_conditional_and_53526_uniform_signed_union_floor(self):
        self.assertEqual(Q_TEN,Fraction(53526,51**6))
        self.assertGreater(Q_TEN,10*Fraction(5175,51**6))
        with self.assertRaises(ValueError):
            conditional_allh_exclusive_signed_palettes(16,Fraction(1,1024))
        r=conditional_allh_exclusive_signed_palettes(
            16,Fraction(1,1024),assume_external_674=True)
        self.assertTrue(r["parent_674_geometric_allh_is_NOT_acceptance"])
        self.assertFalse(r["root_allh_accepted"])
        self.assertEqual(Fraction(r["allh_clean_exponential_rate"]),
                         Q_TEN*Fraction(1,1024)/6)


if __name__=="__main__":
    unittest.main()
