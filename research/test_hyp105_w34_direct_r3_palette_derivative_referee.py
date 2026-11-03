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
    exact_gf5_original_vectors,exact_full_original_external_r3,
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

    def test_committed_true_W34_425_original_direct_R3_source_certificates(self):
        # Exact hosted run arrays are COMMITTED as immutable scientific
        # witnesses, not merely reconstructed from the 2-round selector.
        # Independently rerun the full 12,704,100 original triple external
        # 28D GF5 audit on BOTH saved complete source assignments.
        c=json.loads(Path(__file__).with_name(
            "hyp105_w34_direct_r3_repaired_source_certificates.json"
        ).read_text(encoding="utf-8"))
        self.assertTrue(c["source_geometry_unchanged"])
        self.assertTrue(c["all_425_original_flag_IDs_maintained"])
        self.assertFalse(c["new_asymptotic_ASET_exponent_proved"])
        self.assertEqual(c["hosted_full_source_GitHub_run_id"],41608653224)
        self.assertEqual(set(c["schemes"]),{"lex","reverse-line"})
        wanted={
            "lex":{"initial":(1,507,86),"final":(1,497,76),
                   "edits":((28,21,3),(38,30,7))},
            "reverse-line":{"initial":(0,96,96),"final":(0,83,83),
                            "edits":((135,21,13),(175,33,4))},
        }
        for scheme,z in c["schemes"].items():
            with self.subTest(scheme=scheme):
                w=wanted[scheme]
                model=self.w34[scheme]
                indices=tuple(z["repaired_all_original_425_palettes"])
                previous=tuple(self.prior["schemes"][scheme][
                    "all_425_ORIGINAL_flag_palette_indices"])
                self.assertEqual(z["all_original_425_flag_count"],425)
                self.assertEqual(len(indices),425)
                self.assertEqual(tuple(z[
                    "exact_source_baseline_D2_D3_TRUE_R3"]),w["initial"])
                self.assertEqual(tuple(z[
                    "final_exact_original_R2_D3_R3"]),w["final"])
                self.assertEqual(z["changed_original_source_flag_count"],2)
                changes=tuple(
                    (step["source_ID"],step["old_original_palette"],
                     step["new_original_palette"])
                    for step in z["accepted_changes"])
                self.assertEqual(changes,w["edits"])
                self.assertEqual(
                    {i for i,(a,b) in enumerate(zip(previous,indices)) if a!=b},
                    {step[0] for step in w["edits"]})
                self.assertTrue(z["source_original_pair_maps_unchanged"])
                self.assertTrue(z[
                    "all_accepted_steps_independently_12704100_rechecked"])
                self.assertEqual(len(z["candidate_source_audit"]),8)
                for step in z["accepted_changes"]:
                    initial=step["before_D2_D3_true_R3"]
                    after=step["after_exact_D2_D3_true_R3"]
                    self.assertGreater(initial[2],after[2])
                    self.assertLessEqual(after[0],initial[0])
                    self.assertEqual(
                        step["true_R3_drop"],initial[2]-after[2])
                    self.assertTrue(step[
                        "fresh_full_true_ORIGINAL_12_704_100_triples_verified"])
                    self.assertEqual(len(step[
                        "all_51_exact_candidate_delta_D2_D3_TRUE_R3"]),51)
                source_ids,vectors=exact_gf5_original_vectors(model,indices)
                self.assertEqual(len(set(source_ids)),425)
                self.assertEqual(len(set(vectors)),425)
                self.assertTrue(all(sum(v)%5==4 and
                    sum(bool(a) for a in v)==4 for v in vectors))
                self.assertEqual(len(_two_sum_collision_source_pairs(
                    model,indices)),w["final"][0])
                # New clean source-to-physical external census, independent
                # of the 51-way projected source-derivative selector.
                fresh=exact_full_original_external_r3(
                    model,indices,max_triples=12704100,max_witnesses=8)
                self.assertEqual((
                    fresh["R2_signed_2v2_events_exact"],
                    fresh["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                    fresh["FULL_six_distinct_original_ID_3v3_signed_event_count"]),
                    w["final"])
                self.assertEqual(
                    fresh["all_triples_exact_external_disk_records_processed"],
                    12704100)
                self.assertTrue(fresh[
                    "independent_original_R2_to_R3_overlap_identity_verified"])
                self.assertFalse(fresh["complete_source_GF5_zero_to_three_ASET"])

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
