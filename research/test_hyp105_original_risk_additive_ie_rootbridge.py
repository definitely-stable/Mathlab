"""AA4-RISKIE: independent 2^12 GF5 flow/51-palette and ORIGINAL R3 tests."""
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
import unittest

from hyp105_original_risk_additive_ie_rootbridge import (
    PAL, K, R, ROOT_STATUS, SIGN_MASKS,
    _cycles4, _bbo_typed_dual_templates, _d6_typed_dual_template,
    _validate_graph, _components_from_mask, all_ten_signs_by_IE,
    all_abstract_sixset_GF5_certificate, _single_owner_path_center, _real_original,
    _typed_dual_factor, _one_source_sixset, genuine_original_risk_fixtures,
    root_symbolic_bridge, canonical_report,
)


class TestOriginalAdditiveRiskIE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x=canonical_report()

    def test_51_nonzero_GF5_checksum_four_palette_rederived_from_scratch(self):
        p=tuple(row for row in product((1,2,3,4),repeat=4)
                if sum(row)%5==4)
        self.assertEqual(len(p),PAL)
        self.assertEqual(len(set(p)),PAL)
        self.assertTrue(all(sum(row)%5==4 and all(1<=v<=4 for v in row)
                            for row in p))

    def test_exact_ten_global_unordered_3v3_sign_partition_indices(self):
        self.assertEqual(len(SIGN_MASKS),10)
        self.assertEqual(len(set(SIGN_MASKS)),10)
        for z in SIGN_MASKS:
            self.assertEqual(z.bit_count(),3)
            self.assertEqual(z&1,1)
            self.assertNotIn(63^z,SIGN_MASKS)
        self.assertEqual(SIGN_MASKS,tuple(
            1+sum(1<<j for j in p) for p in combinations(range(1,6),2)))

    def test_full_9x10_BBo_templates_plus_10_D6_every_signed_flow_nonzero(self):
        e=self.x["full_sixset_GF5_independent_inclusion_exclusion"]
        self.assertEqual(len(e["nine_complete_original_BBo_templates"]),9)
        self.assertEqual(e["BBo_exact_minimum_ten_sum"],53526)
        self.assertGreaterEqual(e["BBo_exact_minimum_single_sign"],5175)
        self.assertEqual(e["D6_ten_sum"],54162)
        self.assertTrue(e["D6_connected"])
        self.assertTrue(e["all_100_balanced_original_sixset_signed_events_strictly_positive"])
        for z in e["nine_complete_original_BBo_templates"]:
            self.assertEqual(len(z["ten_weights"]),10)
            self.assertEqual(sum(z["ten_weights"]),z["sum_ten"])
            self.assertTrue(z["connected"])
            self.assertGreaterEqual(z["sum_ten"],53526)

    def test_independent_2power12_inclusion_exclusion_matches_historical_tree_only_TEST(self):
        # Main implementation has NO tree / Fourier import whatsoever.
        from hyp105_original_gf5_tree_flow_referee import (
            flow_count_by_tree_chords, aligned_d6_edges, bbo_templates,
            SIGN_MASKS as old_signs,
        )
        self.assertEqual(SIGN_MASKS,old_signs)
        bbo=_bbo_typed_dual_templates()
        d6L,d6R=_d6_typed_dual_template()
        trials=[(d6L+d6R,0),(d6L+d6R,5)]
        trials.extend((bbo[i][2]+bbo[i][3],j)
                      for i,j in ((0,0),(1,4),(4,5),(8,9)))
        for edges,ix in trials:
            with self.subTest(ix=ix,edges=edges[:3]):
                actual=all_ten_signs_by_IE(edges[:6],edges[6:])
                historical=flow_count_by_tree_chords(edges,SIGN_MASKS[ix])
                self.assertEqual(actual["ten_exact_signed_51palette_weights"][ix],
                                 historical)

    def test_100_signed_template_digest_independent_matches_prior_TEST_ONLY(self):
        # Independent math method; same normalized 9x10 + one D6 ordering.
        from hyp105_original_gf5_tree_flow_referee import template_census
        e=self.x["full_sixset_GF5_independent_inclusion_exclusion"]
        other=template_census()
        self.assertEqual(e["BBo_exact_minimum_ten_sum"],
                         other["BBo_minimum_ten_sign_total"])
        self.assertEqual(e["D6_ten_sum"],other["D6_ten_sign_total"])
        self.assertEqual(
            e["independent_full_100_signed_flow_table_SHA256"],
            other["exact_all_template_weights_SHA256"]
        )

    def test_NEW_all_order_physical_produced_BBo_synchronized_C4_center_and_53838_weight(self):
        # Among nine all-order ORIGINAL BBo dual C4xC4 templates,
        # the three physical path-owner singleton IDs must form the SAME
        # ordered three-edge path on both typed physical coordinate
        # cycles. The physical middle owner therefore has the same
        # column index in both 4-cycles. Exactly THREE of nine templates
        # satisfy this necessary condition, with exact ten-sign 53838;
        # the other six have 53526 and cannot be produced by a proper
        # single coherent physical 3path source lift.
        e=self.x["full_sixset_GF5_independent_inclusion_exclusion"]
        cls=e["nine_BBo_TEMPLATE_C4_center_compatibility"]
        self.assertEqual(len(cls),9)
        good=[x for x in cls if x["same_three_original_path_owner_CENTER"]]
        bad=[x for x in cls if not x["same_three_original_path_owner_CENTER"]]
        self.assertEqual(len(good),3)
        self.assertEqual(len(bad),6)
        self.assertEqual(
            {(z["left_C4"],z["right_C4"]) for z in good},
            {(0,0),(1,1),(2,2)})
        self.assertTrue(all(z["ten_sign_sum"]==53838 and
                            z["left_center"]==z["right_center"]
                            for z in good))
        self.assertTrue(all(z["ten_sign_sum"]==53526 and
                            z["left_center"]!=z["right_center"]
                            for z in bad))
        self.assertEqual(e["three_physical_path_COMPATIBLE_BBo_minimum_ten_sign_weight"],53838)
        self.assertEqual(e["six_NONIMAGE_C4_center_mismatched_templates_weight"],53526)
        sixsets=self.x["genuine_actual_original_sixID_risk_examples"]["genuine_source_cases"]
        produced=[z for z in sixsets if z["type"]=="BBo"]
        self.assertEqual(len(produced),6)
        self.assertTrue(all(z["physical_path_compatible_BBo_C4_center"] is True
                            and z["ten_sign_sum"]==53838
                            for z in produced))
        self.assertTrue(all(z["physical_path_compatible_BBo_C4_center"] is None
                            for z in sixsets if z["type"]=="D6"))

    def test_genuine_W32_W34_SOURCE_sixID_positive_GF5_and_template_injection(self):
        c=self.x["genuine_actual_original_sixID_risk_examples"]
        items=c["genuine_source_cases"]
        self.assertEqual(len(items),9)
        self.assertEqual(sum(z["type"]=="D6" for z in items),3)
        self.assertEqual(sum(z["type"]=="BBo" for z in items),6)
        for z in items:
            with self.subTest(s=z["s"],scheme=z["scheme"],
                              kind=z["type"],six=z["original_source_six_incidence_IDs"]):
                self.assertEqual(len(z["original_source_six_incidence_IDs"]),6)
                self.assertEqual(len(set(z["original_source_six_incidence_IDs"])),6)
                self.assertEqual(sum(z["ten_sign_weights"]),z["ten_sign_sum"])
                self.assertTrue(z["dual_connected"])
                self.assertGreaterEqual(z["ten_sign_sum"],
                                        54162 if z["type"]=="D6" else 53526)

    def test_exact_proper_event_keys_not_overcounting_sign_reverse_or_source(self):
        scenarios=self.x["genuine_actual_original_sixID_risk_examples"]["genuine_source_cases"]
        signs=[]
        for z in scenarios:
            key=(z["s"],z["scheme"],z["shift_f"],z["shift_g"],
                 tuple(z["original_source_six_incidence_IDs"]))
            for mask in SIGN_MASKS:
                signs.append((key,mask))
        self.assertEqual(len(signs),90)
        self.assertEqual(len(signs),len(set(signs)))
        self.assertEqual(len(set(a[0] for a in signs)),9)
        for _,mask in signs:
            self.assertNotIn(63^mask,SIGN_MASKS)

    def test_same_sixset_connected_dual_means_distinct_sign_events_mutually_exclusive(self):
        # If two signs satisfy the same weighted equality on a connected
        # 2-incidence-per-coordinate dual graph, every edge uv forces
        # epsilon_u epsilon_v = eta_u eta_v. Connectivity gives
        # eta=epsilon or eta=-epsilon on ALL SIX source columns, so
        # the unordered 3+3 keys are IDENTICAL. This is an ALL-ORDER
        # argument; these tests verify connectivity of every true source.
        e=self.x["full_sixset_GF5_independent_inclusion_exclusion"]
        self.assertTrue(e["D6_connected"])
        self.assertTrue(all(v["connected"] for v in e["nine_complete_original_BBo_templates"]))
        for z in self.x["genuine_actual_original_sixID_risk_examples"]["genuine_source_cases"]:
            self.assertTrue(z["dual_connected"])

    def test_two_disjoint_real_W32_sixsets_events_overlap_in_GLOBAL_coefficient_space(self):
        # Exact proof by source column independence: Q0 and Q1 disjoint;
        # each has strictly positive signed-event probability; both
        # events can occur simultaneously (product probability >0).
        # Therefore risk SUM is strictly larger than their UNION
        # probability. This is NOT a flaw, because R3 is defined as SUM.
        q=self.x["genuine_actual_original_sixID_risk_examples"][
            "two_disjoint_actual_original_W32_BBo_source_sets"]
        self.assertEqual(len(q["first_sixset"]),6)
        self.assertEqual(len(q["second_sixset"]),6)
        self.assertFalse(set(q["first_sixset"])&set(q["second_sixset"]))
        total=Fraction(q["sum_of_two_local_signed_event_probabilities"])
        both=Fraction(q["probability_of_both_local_events"])
        union=Fraction(q["probability_of_union_of_two_local_events"])
        self.assertGreater(both,0)
        self.assertEqual(total-union,both)
        self.assertTrue(q["R3_sum_STRICTLY_greater_than_union_probability"])

    def test_exact_Branch_A_source_sixset_to_additive_R3_conditional_composition(self):
        z=self.x["all_order_formal_graph_constant_gate_cases"]
        self.assertEqual(
            [(x["C0_FORMAL"],x["c0_FORMAL"],x["h0"]) for x in z],
            [("1","1",810),("2","1/5",840),("7/3","1/17",847)])
        for x in z:
            self.assertTrue(all(x["checks"].values()))
            self.assertEqual(Fraction(x["rho"])*12*x["q3"]**2*x["L6"],16)
            self.assertEqual(Fraction(x["LOW_BBo_sixset_sextic_floor"]),Fraction(23,48))
            self.assertEqual(Fraction(x["universal_original_source_conditional_R3_rational_floor"]),
                             54162*Fraction(x["delta"])/PAL**6)
            self.assertGreater(
                53526*Fraction(x["LOW_BBo_sixset_sextic_floor"]),
                54162*Fraction(x["delta"]))

    def test_exact_formal_root_ledger_agrees_with_frozen_parent_ONLY_IN_TEST(self):
        from hyp105_original_low_spectral_rho16 import exact_low_source_ledger
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            old=exact_low_source_ledger(C,c)
            new=root_symbolic_bridge(C,c)
            for attr in ("T","q2","q3","L6","L4","B0","E","D","s0","h0"):
                self.assertEqual(new[attr],old[attr])
            self.assertEqual(new["rho"],old["rho"])
            self.assertEqual(new["delta"],old["delta"])

    def test_invalid_sixset_source_IDs_and_fabricated_graph_constant_values_fail_closed(self):
        c=_real_original(1,"lex")
        for ids in ((1,1,2,3,4,5),(0,1,2,3,4),
                    (-1,1,2,3,4,5),(0,1,2,3,4,45)):
            with self.assertRaises(ValueError):_one_source_sixset(c,ids)
        with self.assertRaises(ValueError):
            _validate_graph(((0,1),)*12)
        with self.assertRaises(ValueError):
            all_ten_signs_by_IE(((0,1),)*5,((0,1),)*6)
        with self.assertRaises(ValueError):
            _cycles4((0,0,1,2))
        for a,b in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2))):
            with self.assertRaises(ValueError):root_symbolic_bridge(a,b)
        with self.assertRaises(ValueError):_real_original(3,"lex")

    def test_scientific_draft_and_real_R3_exact_SUM_not_UNION_status(self):
        r=self.x
        self.assertEqual(r["schema"],"mathlab.hyp105.original-risk-additive-IE-rootbridge.v1")
        self.assertEqual(r["root_230_status"],ROOT_STATUS)
        self.assertFalse(r["root_230_PROVED_A_accepted"])
        self.assertTrue(r["full_R3_is_SUM_of_distinct_unordered_3v3_signed_event_probabilities"])
        self.assertFalse(r["R3_is_probability_of_UNION_of_signed_events"])
        self.assertTrue(r["all_order_sixset_to_full_R3_additive_embedding_proved"])
        self.assertTrue(r["all_order_physical_produced_BBo_SAME_owner_C4_center_for_both_typed_factors"])
        self.assertFalse(r["genuine_EXTERNAL_ordinary_C6_graph_theorem_constants_numerically_known"])
        self.assertFalse(r["root_final_independent_all_dependencies_mathematically_accepted"])
        self.assertFalse(r["root_ASET_exponent_proved"])


if __name__=="__main__":
    unittest.main()
