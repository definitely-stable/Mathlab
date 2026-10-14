"""JPKC-014 rigorous ORIGINAL factor-choice and source incidence capacity checks."""
from collections import Counter
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc014_source_factor_capacity import (
    incidence_capacity_certificate, single_factor_choice_certificate,
)


class SourceFactorCapacityTests(unittest.TestCase):
    def test_true_original_block_disjoint_Q_anchors_exact(self):
        model=fixture(1,"S72")
        edges=model["incidences"]
        a=next(i for i,x in enumerate(edges) if x[1]==0)
        b=next(i for i,x in enumerate(edges) if x[1]==1)
        c=next(i for i,x in enumerate(edges) if x[1]==2)
        others=tuple(i for i,x in enumerate(edges) if x[1] not in (0,1,2))
        self.assertGreaterEqual(len(others),5)
        Q0=tuple(sorted((a,)+others[:5]))
        Q1=tuple(sorted((b,)+others[:5]))
        cert=incidence_capacity_certificate(
            {0:[Q0],1:[Q1]},edges,disjoint_block=(0,1,2))
        self.assertEqual(cert["distinct_original_incidence_sixsets"],2)
        self.assertEqual(cert["exact_original_incidence_capacity_lower_bound"],2)
        self.assertEqual(cert["max_actual_anchor_multiplicity_of_an_original_Q"],1)
        self.assertTrue(cert["single_moving_source_factor_disjoint_charge_verified"])
        Q01=tuple(sorted((a,b)+others[:4]))
        with self.assertRaisesRegex(AssertionError,"single-factor"):
            incidence_capacity_certificate({0:[Q01]},edges,
                                           disjoint_block=(0,1,2))

    def test_overlapping_true_original_Q_capacity_at_most_six(self):
        edges=fixture(1,"lex")["incidences"]
        Q=tuple(range(6))
        anchors=tuple(sorted(set(edges[i][1] for i in Q)))
        c=incidence_capacity_certificate(
            {r:(Q,) for r in anchors},edges)
        self.assertEqual(c["distinct_original_incidence_sixsets"],1)
        self.assertEqual(c["total_anchor_original_Q_charges"],len(anchors))
        self.assertEqual(c["max_actual_anchor_multiplicity_of_an_original_Q"],len(anchors))
        self.assertEqual(c["exact_original_incidence_capacity_lower_bound"],1)
        with self.assertRaisesRegex(AssertionError,"anchor"):
            incidence_capacity_certificate({99:(Q,)},edges)
        with self.assertRaisesRegex(ValueError,"distinct ORIGINAL"):
            incidence_capacity_certificate({anchors[0]:[(0,0,1,2,3,4)]},edges)

    def test_frozen_full_24_original_S72_one_line_image_star(self):
        cert=single_factor_choice_certificate("S72")
        stars=cert["J47_single_factor_original_image_stars"]
        self.assertIn(7,stars)
        r=stars[7]
        self.assertGreaterEqual(r["min_true_original_Q_per_legal_image"],1)
        self.assertEqual(
            len(r["per_original_physical_image_witnesses"]),4)
        self.assertEqual(
            len(set(str(x["image"]) for x in r["per_original_physical_image_witnesses"])),4)
        values=tuple(r["four_image_positive_state_partition_masks"].values())
        self.assertEqual(len(values),4)
        self.assertTrue(all(m.bit_count()==6 for m in values))
        self.assertEqual(sum(values),(1<<24)-1)
        self.assertEqual(cert["full_original_seven_S_min"],68)
        self.assertGreaterEqual(cert["J48_all_h_conditional_block_disjoint_original_Q_lower"],1)
        self.assertEqual(cert["J48_disjoint_Q_charge_summaries"]["max_actual_multiplicity"],1)
        self.assertTrue(cert["J49_true_original_incidence_census_reverified_every_state"])
        self.assertFalse(cert["all_h_universal_star_existence_proved"])

    def test_frozen_full_24_original_S68_no_double_original_Q_charge(self):
        cert=single_factor_choice_certificate("S68")
        self.assertEqual(cert["full_original_seven_S_min"],68)
        self.assertTrue(cert["complete_24_state_true_original_injection_fiber"])
        self.assertLessEqual(cert["J48_all_h_conditional_block_disjoint_original_Q_lower"],68)
        self.assertGreaterEqual(
            cert["J48_finite_exact_min_selected_true_original_Q_by_state"],
            cert["J48_all_h_conditional_block_disjoint_original_Q_lower"])
        self.assertEqual(cert["J48_disjoint_Q_charge_summaries"]["max_actual_multiplicity"],
                         1 if cert["J48_distinct_original_block_line_stars"] else 0)

    def test_fail_closed_incomplete_illegal_model_and_duplicate_Q(self):
        with self.assertRaisesRegex(ValueError,"complete"):
            single_factor_choice_certificate("S72",states=2)
        with self.assertRaises(ValueError):
            single_factor_choice_certificate("lex")
        with self.assertRaisesRegex(ValueError,"budget"):
            single_factor_choice_certificate("S72",max_profiles=1)
        edges=fixture(1,"S68")["incidences"]
        q=tuple(range(6))
        r=edges[0][1]
        with self.assertRaisesRegex(AssertionError,"duplicate"):
            incidence_capacity_certificate({r:[q,q]},edges)
        with self.assertRaisesRegex(ValueError,"six"):
            incidence_capacity_certificate({r:[(0,1,2)]},edges)
        with self.assertRaisesRegex(ValueError,"distinct"):
            incidence_capacity_certificate({r:[q]},edges,disjoint_block=(r,r))


if __name__=="__main__":
    unittest.main()
