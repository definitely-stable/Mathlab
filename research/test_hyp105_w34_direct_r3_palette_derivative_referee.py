"""Independent AA4-W34-DIRECT-R3 actual ORIGINAL 51-palette derivative referee.

Prove every one of 51 predicted ΔD2, ΔD3, ΔTRUE R3 for two real
W32 source IDs by FRESH separate exact full 45-original-flag
1/2/3-subset sum counts. W34 both fixed complete real 425 source
maps are reconstructed and checked against frozen complete #714
source-palette and R2/R3 certificates, never artificial 6-flag clones.
"""
from collections import Counter
from pathlib import Path
import json
import math
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,_sums_by_cardinality,
)
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    _read_frozen_r2first_original_certificates,
    all_51_exact_original_source_D2_cross_cost,
    all_51_direct_R3_derivative,
    exact_W34_direct_R3_local_descent,
)


class DirectFullR3GF5Original51PaletteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w32=pair_labeled_symplectic(1,"lex")
        cls.w32idx=committed_sevenclass_indices()["lex"]
        cls.w34={s:pair_labeled_symplectic(2,s) for s in
                 ("lex","reverse-line")}
        cls.prior=_read_frozen_r2first_original_certificates()

    def test_real_W32_all_51_R2_and_true_R3_deltas_against_fresh_full_sum_oracle(self):
        model=self.w32
        original=self.w32idx
        vec=exact_gf5_original_vectors(model,original)[1]
        initial_D2=_sums_by_cardinality(vec,2)[1]
        initial_D3=_sums_by_cardinality(vec,3)[1]
        self.assertEqual(initial_D3,7)
        for source_id in (0,29):
            with self.subTest(source=source_id):
                score=all_51_direct_R3_derivative(
                    model,original,source_id,
                    baseline_D2=initial_D2,baseline_D3=initial_D3,
                    max_other_triples=13244)
                self.assertEqual(len(score[
                    "exact_all_51_source_palette_candidates"]),51)
                self.assertEqual(
                    score["other_original_triples_counted_once"],13244)
                self.assertEqual(score["other_original_pair_sums_for_D2"],946)
                self.assertEqual(score["other_original_pair_sums_for_D3"],946)
                self.assertTrue(score["full_source_exact_no_sampling_or_proxy"])
                for candidate in score[
                        "exact_all_51_source_palette_candidates"]:
                    t=candidate["palette"]
                    modified=list(original);modified[source_id]=t
                    real_vectors=exact_gf5_original_vectors(
                        model,modified)[1]
                    fresh_D2=_sums_by_cardinality(real_vectors,2)[1]
                    fresh_D3=_sums_by_cardinality(real_vectors,3)[1]
                    fresh_R3=fresh_D3-41*fresh_D2
                    self.assertEqual((fresh_D2,fresh_D3,fresh_R3),(
                        candidate["predicted_exact_D2"],
                        candidate["predicted_exact_D3"],
                        candidate["predicted_exact_true_R3"]),
                        f"source {source_id}, palette {t}: false full GF5 delta")
                    self.assertEqual(
                        candidate["delta_true_six_distinct_original_R3"],
                        fresh_R3-(initial_D3-41*initial_D2))
                selected=score["best_R2_nonincrease_candidate"]
                self.assertTrue(selected["R2_guardrail_no_increase"])
                self.assertEqual(selected["predicted_exact_true_R3"],
                                 min(x["predicted_exact_true_R3"] for x in
                                     score["exact_all_51_source_palette_candidates"]
                                     if x["R2_guardrail_no_increase"]))

    def test_actual_original_W34_saved_baselines_and_51_R2_cross(self):
        data=self.prior
        self.assertEqual(data["true_ORIGINAL_flags"],425)
        self.assertEqual(data["full_source_triples_checked_per_scheme"],
                         12704100)
        self.assertFalse(data["full_0to3_ASET_found"])
        for scheme,model in self.w34.items():
            with self.subTest(scheme=scheme):
                s=data["schemes"][scheme]
                idx=tuple(s["all_425_ORIGINAL_flag_palette_indices"])
                self.assertEqual(len(idx),425)
                old2=s["new_exact_full_source_R2"]
                old3=s["new_exact_full_source_D3"]
                oldR=s["new_exact_full_source_signed_R3"]
                self.assertEqual(old3-421*old2,oldR)
                self.assertEqual(len(_two_sum_collision_source_pairs(
                    model,idx)),old2)
                self.assertEqual(
                    (old2,old3,oldR),
                    (1,507,86) if scheme=="lex" else (0,96,96))
                source_id=s["full_original_exact_signed_witnesses"][0][
                    "six_distinct_ORIGINAL_flag_IDs"][0]
                pair_score=all_51_exact_original_source_D2_cross_cost(
                    model,idx,source_id)
                self.assertEqual(len(pair_score[
                    "all_51_legal_source_D2_cross_counts"]),51)
                self.assertEqual(pair_score[
                    "other_original_pair_source_processed"],89676)
                self.assertEqual(pair_score[
                    "other_original_single_source_processed"],424)
                self.assertTrue(pair_score["exact_no_sampling"])
                for t in (0,idx[source_id],7,36,50):
                    candidate=list(idx);candidate[source_id]=t
                    direct=len(_two_sum_collision_source_pairs(
                        model,candidate))
                    predicted=old2+pair_score[
                        "all_51_legal_source_D2_cross_counts"][t]-pair_score[
                            "current_exact_D2_cross_count"]
                    self.assertEqual(direct,predicted)

    def test_genuine_source_input_budget_rejection_and_no_false_optimism(self):
        model=self.w34["lex"]
        idx=tuple(self.prior["schemes"]["lex"][
            "all_425_ORIGINAL_flag_palette_indices"])
        with self.assertRaises(ValueError):
            all_51_exact_original_source_D2_cross_cost(
                model,idx,425)
        with self.assertRaises(ValueError):
            all_51_direct_R3_derivative(
                model,idx,0,baseline_D2=1,baseline_D3=507,
                max_other_triples=14190)
        with self.assertRaises(ValueError):
            all_51_direct_R3_derivative(
                model,idx,0,baseline_D2=-1,baseline_D3=507)
        with self.assertRaises(ValueError):
            all_51_direct_R3_derivative(
                model,idx,0,baseline_D2=1000,baseline_D3=1)
        with self.assertRaises(ValueError):
            exact_W34_direct_R3_local_descent(
                "lex",max_source_candidates_per_round=0,max_updates=1)
        with self.assertRaises(ValueError):
            exact_W34_direct_R3_local_descent(
                "wrong",max_source_candidates_per_round=4,max_updates=1)


if __name__=="__main__":
    unittest.main()
