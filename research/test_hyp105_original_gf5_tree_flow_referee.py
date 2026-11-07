"""AA4-GF5TREE independent true original GF5 quantitative referee gates."""
import unittest
from pathlib import Path
from itertools import combinations

from hyp105_original_gf5_tree_flow_referee import (
    SIGN_MASKS, aligned_d6_edges, alternating_D6_sign_mask,
    bbo_templates, canonical_original_GF5_report, column_palette,
    exhaustive_W32_original_BBo_GF5, flow_count_by_tree_chords,
    flow_count_direct_51_palette_mitm, four_cycles, original_case,
    original_six_GF5_weights, six_source_class, source_dual_edges,
    template_census,
)

from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow


class TestOriginalGF5FlowReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.census=template_census()

    def test_all_h_nine_BBo_dual_templates_and_all_90_signs(self):
        z=self.census
        self.assertEqual(len(z["templates_BBo"]),9)
        self.assertEqual(z["BBo_signed_events"],90)
        self.assertEqual(len(z["balanced_sign_masks"]),10)
        self.assertEqual(z["BBo_minimum_per_sign"],5175)
        self.assertEqual(z["BBo_minimum_ten_sign_total"],53526)
        self.assertEqual(z["BBo_maximum_ten_sign_total"],53838)
        self.assertEqual(z["BBo_total_sign_sum_distribution"],{53526:6,53838:3})
        self.assertTrue(all(len(row["signed_weights"])==10 and
                            min(row["signed_weights"])>=5175 and
                            sum(row["signed_weights"])>=53526
                            for row in z["templates_BBo"]))
        self.assertFalse(z["full_original_branch_A_accepted"])

    def test_d6_source_aligned_alternating_and_full_ten_sign_weight(self):
        z=self.census
        self.assertEqual(z["D6_alternating_mask"],21)
        self.assertEqual(z["D6_alternating_signed_weight"],5643)
        self.assertEqual(z["D6_minimum_per_sign"],5265)
        self.assertEqual(z["D6_ten_sign_total"],54162)
        self.assertEqual(z["D6_signed_weights"],
                         (5265,5454,5454,5265,5454,5643,5454,5454,5454,5265))
        self.assertEqual(alternating_D6_sign_mask(aligned_d6_edges()[:6]),21)

    def test_independent_exact_full_51_palette_MITM_matches_tree_flow(self):
        self.assertEqual(len(column_palette()),51)
        tests=[
            (bbo_templates()[0][2],7,5175),
            (bbo_templates()[0][2],25,5535),
            (bbo_templates()[1][2],7,5184),
            (aligned_d6_edges(),21,5643),
            (aligned_d6_edges(),7,5265),
        ]
        for dual,mask,expected in tests:
            with self.subTest(mask=mask,graph=dual):
                self.assertEqual(flow_count_by_tree_chords(dual,mask),expected)
                self.assertEqual(flow_count_direct_51_palette_mitm(
                    dual,mask),expected)

    def test_full_genuine_W32_all_10935_left_B_8_and_7_original_GF5(self):
        for scheme,wanted in (("lex",8),("reverse-line",7)):
            with self.subTest(scheme=scheme):
                z=exhaustive_W32_original_BBo_GF5(scheme)
                self.assertEqual(z["all_original_LEFT_B_candidate_source_sixsets"],10935)
                self.assertEqual(z["complete_original_BBo_sixsets"],wanted)
                self.assertGreaterEqual(z["least_actual_original_BBo_signed_weight"],5175)
                self.assertGreaterEqual(z["least_actual_original_BBo_all_signs_total"],53526)
                self.assertGreater(len(z["first_three_genuine_source_GF5_witnesses"]),0)

    def test_actual_original_nonimage_W32_BBo_still_GF5_positive(self):
        for scheme,ids in (
            ("lex",(11,13,22,25,27,29)),
            ("reverse-line",(15,16,18,22,32,33)),
        ):
            with self.subTest(scheme=scheme):
                c=original_case(1,scheme)
                self.assertEqual(six_source_class(c,ids),"B/B-overlap")
                z=original_six_GF5_weights(c,ids)
                self.assertEqual(z["class"],"B/B-overlap")
                self.assertEqual(len(z["ten_balanced_sign_exact_GF5_weights"]),10)
                self.assertGreaterEqual(z["minimum_one_sign"],5175)
                self.assertGreaterEqual(z["all_ten_sign_total"],53526)

    def test_genuine_W34_D6_3_original_sixsets_and_BBo_deleted_controls(self):
        from json import loads
        base=Path(__file__).parent
        heavy=loads((base/"hyp105_original_deletion_adaptive_heavy_tail_certificates.json").read_text())
        low=loads((base/"hyp105_original_lowtail_alln_energy_certificates.json").read_text())
        d6=0
        for row in heavy["genuine_source_cases"]:
            if row["s"]!=4 or row.get("empty_tail"):
                continue
            c=original_case(2,row["scheme"])
            for ids in row["true_original_D6_six_flag_IDs_selected"]:
                with self.subTest(kind="D6",scheme=row["scheme"],ids=ids):
                    self.assertEqual(six_source_class(c,ids),"D6")
                    self.assertFalse(set(ids)&set(row["deleted_original_flag_IDs"]))
                    v=original_six_GF5_weights(c,ids)
                    self.assertEqual(v["D6_alternating_GF5_weight"],5643)
                    self.assertEqual(v["all_ten_sign_total"],54162)
                    d6+=1
        self.assertEqual(d6,3)
        for row in low["genuine_true_original_cases"]:
            if row["s"]!=4:continue
            c=original_case(2,row["scheme"])
            original=row["real_positive_original_BBo_six_IDs"]
            self.assertGreater(len(original),100)
            for index in sorted({0,len(original)//2,len(original)-1}):
                ids=original[index]
                with self.subTest(kind="BBo",scheme=row["scheme"],idx=index):
                    self.assertFalse(set(ids)&set(row["deleted_original_flag_IDs"]))
                    v=original_six_GF5_weights(c,ids)
                    self.assertEqual(v["class"],"B/B-overlap")
                    self.assertGreaterEqual(v["minimum_one_sign"],5175)
                    self.assertGreaterEqual(v["all_ten_sign_total"],53526)

    def test_independent_historical_Fourier_GF5_crosscheck_TESTS_ONLY(self):
        # Different existing Fourier oracle is imported only by test, not
        # main tree/chord module. Test both original class types and signs.
        testcases=[
            (1,"lex",(11,13,22,25,27,29)),
            (1,"reverse-line",(15,16,18,22,32,33)),
            (2,"lex",(111,116,203,224,383,412)),
        ]
        for h,scheme,ids in testcases:
            c=original_case(h,scheme)
            dual=source_dual_edges(c,ids)
            self.assertIsNotNone(dual)
            supports=[]
            for i in ids:
                p,ell=c["flags"][i]
                supports.append(tuple(c["f"][p])+
                                tuple(c["a"]+z for z in c["g"][ell]))
            for mask in (7,21):
                signs=tuple(1 if mask&(1<<j) else -1 for j in range(6))
                independent=flow_count_by_tree_chords(dual[0],mask)
                historic=exact_dual_GF5_six_flow(
                    supports,signs,dimension=2*c["a"])
                self.assertEqual(independent,historic)

    def test_all_permutations_of_source_column_ID_order_are_flow_invariant(self):
        c=original_case(2,"lex")
        ids=[111,116,203,224,383,412]
        first=original_six_GF5_weights(c,ids)
        for perm in (
            tuple(reversed(ids)),
            ids[2:]+ids[:2],
            (ids[0],ids[3],ids[2],ids[5],ids[4],ids[1]),
        ):
            result=original_six_GF5_weights(c,perm)
            self.assertEqual(result["class"],"D6")
            self.assertEqual(result["all_ten_sign_total"],first["all_ten_sign_total"])
            self.assertEqual(result["D6_alternating_GF5_weight"],5643)

    def test_reject_non_original_and_invalid_sign_graphs(self):
        with self.assertRaises(ValueError):
            original_case(3,"lex")
        c=original_case(1,"lex")
        for ids in ((1,1,2,3,4,5),(0,1,2,3,4),(-1,2,3,4,5,6),
                    (0,1,2,3,4,45)):
            with self.assertRaises(ValueError):
                source_dual_edges(c,ids)
        for mask in (0,1,127,True):
            with self.assertRaises(ValueError):
                flow_count_by_tree_chords(aligned_d6_edges(),mask)
        with self.assertRaises(ValueError):
            flow_count_by_tree_chords(((0,1),)*12,7)
        with self.assertRaises(ValueError):
            four_cycles((1,1,2,3))
        with self.assertRaises(ValueError):
            alternating_D6_sign_mask(((0,1),)*6)

    def test_full_durable_original_proof_report_scope(self):
        r=canonical_original_GF5_report()
        self.assertEqual(r["schema"],"mathlab.hyp105.original-gf5-tree-flow-referee.v1")
        self.assertEqual(r["status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertFalse(r["full_original_Branch_A_accepted"])
        self.assertTrue(r["allh_structural_GF5_templates_checked"])
        self.assertEqual(r["uniform_BBo_per_sign_lower"],5175)
        self.assertEqual(r["uniform_BBo_all_ten_sign_lower"],53526)
        self.assertEqual(r["uniform_D6_designated_alternating_flow"],5643)
        self.assertEqual(r["uniform_D6_all_ten_sign_total"],54162)
        self.assertEqual([z["complete_original_BBo_sixsets"]
                          for z in r["exhaustive_actual_W32_BBo_GF5"]],[8,7])
        self.assertEqual(len(r["actual_W34_D6_GF5_witnesses"]),3)
        self.assertEqual(len(r["actual_W34_BBo_GF5_witnesses"]),2)


if __name__=="__main__":
    unittest.main()
