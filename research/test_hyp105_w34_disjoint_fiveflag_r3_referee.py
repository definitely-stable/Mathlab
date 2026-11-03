"""AA4-W34-DISJOINT5 independent true ORIGINAL 3v3 source-local tests.

Main falsifier: on complete REAL W32 map and fixed global palette array,
the full true six-DISTINCT-ID 3v3 census on 51 FRESH physical GF5
assignments must equal R3_current+H_i(t)-H_i(current), for two actual
original source IDs. This is independent of both the new disjoint
pair/triple projected source histogram and the earlier R2/D3 formula.

Second independent falsifier: all 51 of the new disjoint source delta
values must agree with the previous exact #715 ΔD3-(N-4)ΔD2 oracle
on actual W32 source flags. W34 original source map and exact
physical support are separately checked.
"""
import json
from pathlib import Path
from collections import Counter
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,
    full_original_r3_triple_hash_census,
)
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    all_51_direct_R3_derivative,
    _read_frozen_r2first_original_certificates,
)
from hyp105_w34_disjoint_fiveflag_r3_referee import (
    all_51_direct_disjoint_original_R3_costs,
    all_51_independent_direct_R3_candidate_deltas,
    _frozen_W34_true_R3_certificates,
    exact_W34_direct_disjoint_source_descent,
)


class ExactDisjointOriginalFiveFlagGF5Referee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w32=pair_labeled_symplectic(1,"lex")
        cls.old=committed_sevenclass_indices()["lex"]
        cls.w34={
            s:pair_labeled_symplectic(2,s) for s in
            ("lex","reverse-line")}
        cls.parent=_frozen_W34_true_R3_certificates()

    def test_two_real_W32_original_flags_all_51_against_independent_full_R3(self):
        model=self.w32
        old=self.old
        before=full_original_r3_triple_hash_census(model,old)
        true_r3=before["FULL_original_distinct_sixflag_3v3_signed_events"]
        true_r2=before["duplicate_equal_2_sum_pairs"]
        true_d3=before["duplicate_equal_3_sum_pairs"]
        self.assertEqual(true_r3,7)
        for source_id in (0,29):
            with self.subTest(source_id=source_id):
                direct=all_51_direct_disjoint_original_R3_costs(
                    model,old,source_id,max_other_triples=13244)
                d=all_51_independent_direct_R3_candidate_deltas(
                    model,old,source_id,
                    baseline_D2=true_r2,baseline_R3=true_r3,
                    max_other_triples=13244)
                indirect=all_51_direct_R3_derivative(
                    model,old,source_id,baseline_D2=true_r2,
                    baseline_D3=true_d3,max_other_triples=13244)
                self.assertEqual(direct["original_3subsets_processed"],13244)
                self.assertEqual(direct["original_2subsets_indexed"],946)
                self.assertEqual(len(direct[
                    "all_51_exact_TRUE_R3_incidence_counts"]),51)
                self.assertEqual(d["baseline_original_R3_incidence"],
                                 direct["current_source_TRUE_R3_incidence"])
                self.assertTrue(direct["no_D3_or_R2_shadow_used_for_R3"])
                self.assertGreaterEqual(direct[
                    "overlapping_original_pair_triple_matches_correctly_excluded"],0)
                for t in range(51):
                    with self.subTest(source_id=source_id,palette=t):
                        new=list(old);new[source_id]=t
                        fresh=full_original_r3_triple_hash_census(
                            model,tuple(new),max_witnesses=0)
                        predicted=d[
                            "all_51_direct_true_R3_and_R2_candidates"][t]
                        indirect_pred=indirect[
                            "exact_all_51_source_palette_candidates"][t]
                        self.assertEqual(
                            predicted["predicted_FULL_TRUE_R3"],
                            fresh["FULL_original_distinct_sixflag_3v3_signed_events"])
                        self.assertEqual(predicted["predicted_FULL_D2"],
                                         fresh["duplicate_equal_2_sum_pairs"])
                        self.assertEqual(
                            predicted["predicted_FULL_D3_via_independent_identity"],
                            fresh["duplicate_equal_3_sum_pairs"])
                        self.assertEqual(predicted["delta_FULL_TRUE_R3"],
                            indirect_pred["delta_true_six_distinct_original_R3"])
                        self.assertEqual(predicted["delta_full_D2"],
                            indirect_pred["delta_full_D2"])
                self.assertEqual(d["full_original_source_triples_visited_once"],
                                 13244)

    def test_real_W32_zero_signed_incidence_source_cannot_improve_by_single_edit(self):
        model=self.w32
        base=self.old
        full=full_original_r3_triple_hash_census(
            model,base,max_witnesses=20)
        true=full["sample_true_original_signed_event_witnesses"]
        involved=set(i for w in true for i in w["six_original_source_IDs"])
        zero=next(i for i in range(45) if i not in involved)
        h=all_51_direct_disjoint_original_R3_costs(
            model,base,zero,max_other_triples=13244)
        self.assertEqual(h["current_source_TRUE_R3_incidence"],0)
        self.assertTrue(all(x>=0 for x in h[
            "all_51_exact_TRUE_R3_incidence_counts"]))
        # Theorem: an original ID outside every CURRENT real R3
        # collision cannot strictly reduce R3 by editing ONLY its c_i.
        self.assertGreaterEqual(min(h[
            "all_51_exact_TRUE_R3_incidence_counts"]),0)

    def test_real_W34_parent_source_risks_and_legal_G5_pinned_support(self):
        self.assertEqual(set(self.parent["schemes"]),set(self.w34))
        for scheme,model in self.w34.items():
            with self.subTest(scheme=scheme):
                z=self.parent["schemes"][scheme]
                self.assertEqual(tuple(z["final_exact_original_R2_D3_R3"]),
                                 (1,497,76) if scheme=="lex" else
                                 (0,83,83))
                original=tuple(z["repaired_all_original_425_palettes"])
                self.assertEqual(len(original),425)
                indices,vec=exact_gf5_original_vectors(model,original)
                self.assertEqual(len(set(indices)),425)
                self.assertEqual(len(set(vec)),425)
                self.assertTrue(all(sum(w)%5==4 and
                                    sum(bool(i) for i in w)==4 for w in vec))
                self.assertEqual(model["m"],28)

    def test_nonexact_source_budgets_and_inputs_fail_closed(self):
        model=self.w34["lex"]
        original=tuple(self.parent["schemes"]["lex"][
            "repaired_all_original_425_palettes"])
        for source_id in (-1,425):
            with self.assertRaises(ValueError):
                all_51_direct_disjoint_original_R3_costs(
                    model,original,source_id)
        with self.assertRaises(ValueError):
            all_51_direct_disjoint_original_R3_costs(
                model,original,28,max_other_triples=14190)
        with self.assertRaises(ValueError):
            all_51_independent_direct_R3_candidate_deltas(
                model,original,28,baseline_D2=-1,baseline_R3=76)
        with self.assertRaises(ValueError):
            exact_W34_direct_disjoint_source_descent(
                "lex",max_candidates_per_round=0,max_updates=2)
        with self.assertRaises(ValueError):
            exact_W34_direct_disjoint_source_descent(
                "fake",max_candidates_per_round=4,max_updates=2)


if __name__=="__main__":
    unittest.main()
