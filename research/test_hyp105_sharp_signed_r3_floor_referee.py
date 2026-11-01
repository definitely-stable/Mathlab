"""Sharp signed-event risk on TRUE original W(3,s) sixsets.

A separate direct 4^7 chord oracle independently verifies every ten-sign
coefficient, not only the historical single alternating D6 event.
"""
from collections import Counter
from fractions import Fraction
import unittest

from hyp105_sharp_signed_r3_floor_referee import (
    PALETTE_DENOMINATOR,
    SHARP_D6_COEFFICIENT, SHARP_BBO_COEFFICIENT,
    coincident_d6_full_signed_certificate,
    bb_overlap_full_signed_certificate,
    true_original_nine_bbo_lifts,
    true_original_d6_full_signed_lift,
    stronger_root_r3_floor,
)
from hyp105_gf5_original_sixid_flow_referee import (
    SIGNS, gf5_flow_spanning_tree, gf5_flow_inclusion_exclusion,
    bb_overlap_templates, coincident_c6_template,
)


class SharpTenSignOriginalRisk(unittest.TestCase):
    def test_all_ten_d6_signs_both_finite_field_oracles(self):
        z=coincident_d6_full_signed_certificate(independent_tree=True)
        self.assertEqual(z["histogram"],{5265:3,5454:6,5643:1})
        self.assertEqual(z["exact_total"],54162)
        self.assertEqual(z["all_ten_signed_events"],10)
        self.assertEqual(z["improvement"],Fraction(54162,5643))
        self.assertEqual(
            z["ten_signed_counts"],
            (5265,5454,5454,5265,5454,5643,5454,5454,5454,5265))
        self.assertEqual(len(SIGNS),10)
        self.assertEqual(SIGNS[5],frozenset((0,2,4)))

    def test_complete_ninety_signed_BBo_both_oracles(self):
        z=bb_overlap_full_signed_certificate(independent_tree=True)
        self.assertEqual(z["histogram"],{53526:6,53838:3})
        self.assertEqual(sum(z["nine_template_totals"]),482670)
        self.assertEqual(z["min_exact_ten_signs_per_original_sixset"],53526)
        self.assertEqual(z["max_exact_ten_signs_per_original_sixset"],53838)
        self.assertEqual(z["improvement"],Fraction(53526,51750))
        self.assertEqual(len(z["nine_template_totals"]),9)

    def test_all_nine_sharp_original_BBo_lifts_both_true_GQ_orders(self):
        for h in (1,2):
            with self.subTest(power=h):
                rows=true_original_nine_bbo_lifts(h,independent_tree=True)
                self.assertEqual(len(rows),9)
                self.assertEqual(
                    Counter(row["signed_mass"] for row in rows),
                    Counter({53526:6,53838:3}))
                self.assertEqual(len({row["six_source_ids"] for row in rows}),1)
                self.assertTrue(all(row["point_factor_count"]==5 and
                                    row["line_factor_count"]==5 for row in rows))
                self.assertTrue(all(len(row["signed_vector"])==10 for row in rows))

    def test_true_original_D6_all_ten_signs_not_only_one_alternating(self):
        for h in (1,2):
            with self.subTest(power=h):
                report=true_original_d6_full_signed_lift(h,independent_tree=True)
                self.assertEqual(report["signed_mass"],SHARP_D6_COEFFICIENT)
                self.assertEqual(Counter(report["signed_vector"]),
                                 Counter({5265:3,5454:6,5643:1}))
                self.assertEqual(len(set(report["six_source_ids"])),6)

    def test_signed_events_are_counted_separately_without_union_independence(self):
        for D,B in ((0,0),(1,0),(0,1),(1,1),(3,8),(10000,12345)):
            with self.subTest(D=D,B=B):
                z=stronger_root_r3_floor(D,B)
                self.assertEqual(z["numerator"],
                                 SHARP_D6_COEFFICIENT*D+SHARP_BBO_COEFFICIENT*B)
                self.assertGreaterEqual(z["numerator"],53526*(D+B))
                self.assertGreaterEqual(z["numerator"],z["old_numerator"])
                self.assertEqual(z["exact_risk_floor"],
                                 Fraction(z["numerator"],PALETTE_DENOMINATOR))
                self.assertEqual(z["root_asymptotic_coefficient_conditional"],53526)

    def test_permutation_invariance_for_every_ten_signs(self):
        permutations=((3,5,0,2,4,1),(5,4,3,2,1,0))
        samples=(coincident_c6_template(),next(iter(bb_overlap_templates())))
        for edges in samples:
            baseline=tuple(gf5_flow_inclusion_exclusion(edges,plus)
                           for plus in SIGNS)
            for perm in permutations:
                renamed_edges=tuple(tuple(sorted((perm[u],perm[v]))) for u,v in edges)
                for idx,plus in enumerate(SIGNS):
                    newplus={perm[k] for k in plus}
                    if 0 not in newplus:
                        newplus=set(range(6))-newplus
                    self.assertEqual(
                        gf5_flow_inclusion_exclusion(renamed_edges,frozenset(newplus)),
                        baseline[idx])

    def test_symbolic_root_floor_is_sharp_nonnegative_and_fail_closed(self):
        cases=((0,0,0),(1,0,54162),(0,1,53526),(1,1,107688))
        for D,B,expected in cases:
            self.assertEqual(stronger_root_r3_floor(D,B)["numerator"],expected)
        for bad in (-1,1.5,True,None,"1",Fraction(1,1)):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    stronger_root_r3_floor(bad,1)
                with self.assertRaises(ValueError):
                    stronger_root_r3_floor(1,bad)
        with self.assertRaises(ValueError):
            true_original_nine_bbo_lifts(3)
        with self.assertRaises(ValueError):
            true_original_d6_full_signed_lift(3)


if __name__=="__main__":
    unittest.main()
