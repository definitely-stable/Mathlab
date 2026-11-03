"""AA4-ALL2: verify the rebased 425-source input is the new #717 output.

Inherit the independently validated 102 real W32 51-palette source
tests, then INDEPENDENTLY reconstruct BOTH true source W34 fixed f,g
and ALL 12,704,100 ORIGINAL 3-sums from the AFTER #717 coefficient
arrays. Their 58/65 true-R3 witness degrees are recomputed, not reused.

This specifically rejects the risk of silently doing a second audit on
the OLDER #716 62/69 source assignments, a subtle selection error which
would invalidate a repeat-descent claim.
"""
import json
import unittest

import test_hyp105_w34_oneexchange_exhaustive_referee as prior_tests
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,exact_full_original_external_r3,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    _all_current_actual_signed_witnesses,
)
from hyp105_w34_oneexchange_exhaustive_referee import (
    frozen_complete_W34_sources as original_716,
)
from hyp105_w34_rebased_oneexchange_referee import (
    frozen_complete_W34_sources,
    _derive_all_true_signed_original_degrees,
    construct_exact_source_text,
    PARENT_SHA,SHARDS,SCHEMA,
)


class RebasedAfter717ScientificTests(
        prior_tests.AcceleratedExhaustiveOriginalSourceOneExchange):
    """Also runs the old distinct W32 51x2 physical GF5 falsifiers."""

    def test_rebased_717_full_original_source_geometry_and_risks(self):
        child=frozen_complete_W34_sources()
        ancestor=original_716()
        self.assertEqual(PARENT_SHA,
                         "81c0ee7149859ec7ac4dbe0e997e4541fb19de7f")
        self.assertEqual(SHARDS,8)
        self.assertIn("rebased",SCHEMA)
        expected={
            "lex":((1,483,62),(1,479,58),136,8,10),
            "reverse-line":((0,69,69),(0,65,65),270,22,0),
        }
        self.assertEqual(set(child["schemes"]),set(expected))
        for scheme,z in child["schemes"].items():
            with self.subTest(scheme=scheme):
                before,after,source_id,old,new=expected[scheme]
                model=pair_labeled_symplectic(2,scheme)
                self.assertEqual((model["s"],model["N"],model["m"]),
                                 (4,425,28))
                pre=tuple(z[
                    "frozen_original_GF5_before_source_palette_indices"])
                curr=tuple(z[
                    "full_original_425_GF5_after_source_palette_indices"])
                orig=tuple(ancestor["schemes"][scheme][
                    "all_425_ORIGINAL_ID_ordered_GF5_palette_indices"])
                self.assertEqual(pre,orig)
                self.assertEqual(
                    tuple(z["before_FULL_D2_D3_TRUE_R3"]),before)
                self.assertEqual(
                    tuple(z["after_independently_rehashed_FULL_D2_D3_TRUE_R3"]),
                    after)
                self.assertEqual({i for i in range(425) if pre[i]!=curr[i]},
                                 {source_id})
                self.assertEqual((pre[source_id],curr[source_id]),(old,new))
                self.assertEqual(len(curr),425)
                ids,vec=exact_gf5_original_vectors(model,curr)
                self.assertEqual(ids,tuple(range(425)))
                self.assertEqual(len(set(vec)),425)
                self.assertTrue(all(len(w)==28 and sum(w)%5==4
                    and sum(bool(a) for a in w)==4 for w in vec))
                self.assertEqual(
                    len(_two_sum_collision_source_pairs(model,curr)),after[0])
                full,witnesses=_all_current_actual_signed_witnesses(
                    model,curr,after)
                self.assertEqual(len(witnesses),after[2])
                self.assertEqual(full[
                    "all_triples_exact_external_disk_records_processed"],
                    12704100)
                active=_derive_all_true_signed_original_degrees(
                    witnesses,after[2],425)
                self.assertEqual(sum(deg for _,deg in active),6*after[2])
                self.assertTrue(0<len(active)<=425)
                self.assertTrue(all(deg>0 for _,deg in active))
                source_text=construct_exact_source_text(
                    model,curr,full,active)
                self.assertTrue(source_text.startswith(
                    f"HYP105_W34_ALL1_V1 {scheme} 425 28 51 "))
                self.assertEqual(int(source_text.split()[8]),len(active))
                # No source edit other than exact #717 136/270 is smuggled in.
                self.assertEqual(sum(a!=b for a,b in zip(pre,curr)),1)

    def test_rebased_not_old_716_source_manifest(self):
        c=frozen_complete_W34_sources()
        for scheme,source_id in (("lex",136),("reverse-line",270)):
            parent=original_716()["schemes"][scheme][
                "all_425_ORIGINAL_ID_ordered_GF5_palette_indices"]
            new=c["schemes"][scheme][
                "full_original_425_GF5_after_source_palette_indices"]
            self.assertNotEqual(parent[source_id],new[source_id])
            self.assertEqual(sum(x!=y for x,y in zip(parent,new)),1)


    def test_committed_second_exhaustive_source_certificate_full_real_W34(self):
        # One more FRESH FULL W34 physical 12,704,100-original-triple
        # external signed R3 rehash for EACH source, on the actual
        # PERMANENT saved 425-index after coefficients. The exact
        # source-local C++ H_i(t) cost evaluator is NEVER consulted
        # to decide if these final signed counts are correct.
        p=__import__("pathlib").Path(__file__).with_name(
            "hyp105_w34_rebased_oneexchange_certificates.json")
        cert=json.loads(p.read_text(encoding="utf-8"))
        self.assertEqual(cert["scientific_parent_exact_SHA"],
                         "81c0ee7149859ec7ac4dbe0e997e4541fb19de7f")
        self.assertEqual(cert["hosted_complete_initial_run_id"],41719425649)
        self.assertEqual(cert["hosted_complete_artifact_id"],13271373616)
        self.assertEqual(cert["hosted_complete_artifact_uncompressed_bytes"],1100226)
        self.assertEqual(cert["hosted_complete_artifact_sha256"],
                         "d90523f53744fb223d336cade3adaa76b5fccc0b6a380839b32f1d546beaea39")
        self.assertEqual(cert["total_fresh_active_original_source_IDs"],502)
        self.assertEqual(cert["total_exact_51_palette_candidates"],25602)
        self.assertTrue(cert["original_source_maps_f_g_unchanged"])
        self.assertTrue(cert["scientific_no_asymptotic_exponent_proved"])
        self.assertTrue(cert["no_full_425_source_zero_ASET_found"])
        expected={
            "lex":((1,479,58),(1,475,54),239,348,(276,6,0),
                   {"1":160,"2":54,"3":20,"4":5},147),
            "reverse-line":((0,65,65),(0,61,61),263,390,(285,50,3),
                            {"1":167,"2":70,"3":21,"4":5},174),
        }
        frozen=frozen_complete_W34_sources()
        self.assertEqual(set(cert["schemes"]),set(expected))
        for scheme,z in cert["schemes"].items():
            with self.subTest(scheme=scheme):
                before,after,active,degree,edit,distribution,rejected=expected[scheme]
                model=pair_labeled_symplectic(2,scheme)
                prior=tuple(z["frozen_original_425_GF5_source_palettes_before"])
                current=tuple(z["full_original_425_GF5_source_palettes_after"])
                self.assertEqual(len(current),425)
                self.assertEqual(len(prior),425)
                self.assertEqual(prior,tuple(frozen["schemes"][scheme][
                    "full_original_425_GF5_after_source_palette_indices"]))
                self.assertEqual(
                    tuple(z["before_FULL_D2_D3_TRUE_R3"]),before)
                self.assertEqual(
                    tuple(z["after_independently_rehashed_FULL_D2_D3_TRUE_R3"]),after)
                self.assertEqual(z["all_current_active_ORIGINAL_source_IDs_examined"],
                                 active)
                self.assertEqual(z[
                    "sum_actual_true_sixflag_source_incidence_degrees"],degree)
                self.assertEqual(z["strict_improving_current_active_source_count"],
                                 active)
                self.assertEqual(z["strict_best_R3_drop_per_source_histogram"],
                                 distribution)
                self.assertEqual(sum(distribution.values()),active)
                self.assertEqual(z[
                    "R2_guarded_rejected_one_source_palette_options"],rejected)
                self.assertFalse(z[
                    "guarded_one_exchange_local_optimum_of_prior_assignment"])
                self.assertTrue(z["full_original_R3_remains_nonzero"])
                self.assertTrue(z[
                    "independent_full_12704100_original_source_triples_rehashed"])
                source=z["optimal_one_source_change"]
                self.assertEqual((
                    source["original_source_flag_ID"],
                    source["prior_legal_checksum4_palette_index"],
                    source["new_legal_checksum4_palette_index"]),edit)
                self.assertEqual(source["true_full_R3_strict_decrease"],4)
                self.assertEqual(
                    {i for i in range(425) if prior[i]!=current[i]},
                    {edit[0]})
                self.assertEqual((prior[edit[0]],current[edit[0]]),
                                 (edit[1],edit[2]))
                ids,vec=exact_gf5_original_vectors(model,current)
                self.assertEqual(ids,tuple(range(425)))
                self.assertEqual(len(set(vec)),425)
                self.assertTrue(all(len(c)==28 and sum(c)%5==4 and
                    sum(bool(x) for x in c)==4 for c in vec))
                self.assertEqual(len(
                    _two_sum_collision_source_pairs(model,current)),after[0])
                full=exact_full_original_external_r3(
                    model,current,max_triples=12704100,max_witnesses=16)
                self.assertEqual((
                    full["R2_signed_2v2_events_exact"],
                    full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                    full["FULL_six_distinct_original_ID_3v3_signed_event_count"]),
                    after)
                self.assertTrue(full[
                    "independent_original_R2_to_R3_overlap_identity_verified"])
                self.assertEqual(full[
                    "all_triples_exact_external_disk_records_processed"],
                    12704100)
                for witness in full[
                    "verified_independent_true_source_witnesses"]:
                    plus=tuple(witness["positive_ORIGINAL_three"])
                    minus=tuple(witness["negative_ORIGINAL_three"])
                    self.assertEqual(len(set(plus+minus)),6)
                    self.assertTrue(all(
                        sum(vec[i][j] for i in plus)%5==
                        sum(vec[i][j] for i in minus)%5
                        for j in range(28)))


if __name__=="__main__":
    unittest.main()
