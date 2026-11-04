"""Independent ORIGINAL deletion-commuting full/core mixed physical G7 tests.

These tests deliberately combine the deep parent #672 mixed full/core
book identity with adversarial ORIGINAL-ID deletion Z as in #674, and
physically reconstruct all six ORIGINAL incidence flags of surviving
GF5-positive B/B-overlap paths. The independent source-first vs
physical-endpoint-first vs literal 3-walk codepaths must agree.
This is NOT a finite test of asymptotic all-h quantifiers.
"""
from collections import Counter
from itertools import combinations
import json
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source
from hyp105_bbo_resilience import avoidance_certificate
from hyp105_original_masked_mixed_blocker import (
    _true_flags_and_labels,_independent_physical_source_graph,
    _masked_half_audit,_original_positive_BBo_path_census,
    full_original_masked_mixed_referee)


class TrueOriginalPhysicalDeletionMixedBlocker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maps={(power,scheme):pair_labeled_symplectic(power,scheme)
                  for power in (1,2)
                  for scheme in ("lex","reverse-line")}

    def test_complete_genuine_W32_full_core_masked_original_source_contractions(self):
        for scheme in ("lex","reverse-line"):
            m=self.maps[1,scheme]
            for Z in ((),(0,),(1,13,33),(0,25,26,33,34),
                      tuple(range(0,45,9))):
                with self.subTest(scheme=scheme,Z=Z):
                    core=tuple(i for i in range(45) if i not in Z)
                    z=full_original_masked_mixed_referee(
                        1,m["left_labels"],m["right_labels"],core,Z)
                    self.assertTrue(z["source_masked_mixed_identity_exact"])
                    self.assertTrue(z["all_source_first_physical_masked_triples_match"])
                    self.assertEqual(z["source_B_masked_exact"],
                                     z["physical_original_source_records_exact"])
                    self.assertEqual(
                        z["exact_theta_full"]-z["exact_theta_allowed"],
                        z["exact_theta_removed_by_original_owner"])
                    self.assertLessEqual(z[
                        "original_admissible_first_internal_blocker_triples_exact"],
                        z["source_B_masked_exact"])
                    self.assertLessEqual(z[
                        "masked_K_max"],z[
                        "masked_core_R_max_scaled_by_2d"])
                    self.assertTrue(z["physical_weighted_blocker_W2_le_BDeltaTr4"])
                    self.assertFalse(z["universal_allh_mixed_blocker_exponent_claimed_newly"])
                    self.assertEqual(z["root_230_status"],
                                     "OPEN_WITH_FORMAL_BLOCKER")

    def test_true_original_masked_source_is_monotone_for_FIXED_original_core(self):
        for power,scheme in ((1,"lex"),(1,"reverse-line"),(2,"lex")):
            with self.subTest(power=power,scheme=scheme):
                m=self.maps[power,scheme]
                n=len(m["incidences"])
                Z2=(0,3,7,11)
                core=tuple(i for i in range(n)
                           if i not in Z2 and i%3 in (0,1))
                first=_masked_half_audit(
                    power,m["left_labels"],m["right_labels"],core,())
                second=_masked_half_audit(
                    power,m["left_labels"],m["right_labels"],core,(0,))
                third=_masked_half_audit(
                    power,m["left_labels"],m["right_labels"],core,Z2)
                self.assertGreaterEqual(first["exact_theta_allowed"],
                                        second["exact_theta_allowed"])
                self.assertGreaterEqual(second["exact_theta_allowed"],
                                        third["exact_theta_allowed"])
                self.assertEqual(
                    first["exact_theta_allowed"]-
                    third["exact_theta_allowed"],
                    third["exact_theta_removed_by_original_owner"])
                self.assertEqual(
                    first["exact_theta_allowed"]-
                    second["exact_theta_allowed"],
                    second["exact_theta_removed_by_original_owner"])
                self.assertEqual(first["physical_core_trace_A4"],
                                 third["physical_core_trace_A4"])
                self.assertEqual(first["physical_core_Delta"],
                                 third["physical_core_Delta"])

    def test_deleted_original_flag_has_FOUR_physical_cells_NOT_four_edges(self):
        m=self.maps[1,"lex"]
        flags=m["incidences"]
        f,g=m["left_labels"],m["right_labels"]
        core=tuple(i for i in range(45) if i not in (0,1,2,3))
        phys=_independent_physical_source_graph(flags,f,g,core)
        degree=phys[2]
        base=_masked_half_audit(1,f,g,core,())
        masked=_masked_half_audit(1,f,g,core,(0,1,2,3))
        direct=0
        for i in (0,1,2,3):
            p,l=flags[i]
            x,k=f[p];y,w=g[l]
            vertices=((x,y),(x,w),(k,y),(k,w))
            self.assertEqual(len(set(vertices)),4)
            direct+=sum(degree[v] for v in vertices)
        self.assertEqual(direct,base["exact_theta_allowed"]-
                         masked["exact_theta_allowed"])
        self.assertEqual(direct,masked[
            "exact_theta_removed_by_original_owner"])
        self.assertEqual(masked["exact_theta_full"],base["exact_theta_full"])

    def test_complete_true_original_W34_sparse_core_with_FULL_anchors_outside_core(self):
        for scheme in ("lex","reverse-line"):
            m=self.maps[2,scheme]
            Z=tuple(range(0,425,29))
            core=tuple(i for i in range(425)
                       if i%5 in (0,2,4) and i not in Z)
            z=full_original_masked_mixed_referee(
                2,m["left_labels"],m["right_labels"],core,Z)
            self.assertEqual(z["s"],4)
            self.assertEqual(z["original_source_flags"],425)
            self.assertEqual(z["original_paired_core_source_count"],len(core))
            self.assertEqual(z["deleted_original_IDs"],list(Z))
            self.assertTrue(z["source_masked_mixed_identity_exact"])
            self.assertTrue(z["all_source_first_physical_masked_triples_match"])
            self.assertTrue(z["fullcore_deletion_sensitivity_identity_all_N"])
            source=z["source_original_G7_full_nonZ_certificate"]
            self.assertTrue(source["each_original_6set_all_six_flags_avoid_Z"])
            self.assertTrue(source["two_directed_paths_per_original_BBo_source_sixset"])
            self.assertEqual(
                source["unblocked_source_disjoint_original_six_ID_directed_paths"],
                2*source["accepted_true_original_BBo_sixsets"])
            # Anchors outside CORE are ALLOWED, provided all three anchor
            # flags avoid Z. This is the critical mixed/full distinction.
            self.assertGreater(source[
                "unblocked_BBo_source_path_anchor_outside_core"],0)

    def test_independent_original_G7_full_core_paths_match_existing_separate_source_oracle(self):
        for power,scheme in ((1,"lex"),(1,"reverse-line"),(2,"lex")):
            with self.subTest(power=power,scheme=scheme):
                m=self.maps[power,scheme]
                n=len(m["incidences"])
                Z=tuple(range(0,n,13))
                core=tuple(i for i in range(n)
                           if i not in Z and i%3 in (1,2))
                z=_original_positive_BBo_path_census(
                    power,m["left_labels"],m["right_labels"],core,Z)
                independent=avoidance_certificate(
                    power,m["left_labels"],m["right_labels"],Z,core_ids=core)
                self.assertEqual(
                    set(tuple(i) for i in z["original_BBo_sixset_IDs"]),
                    set(tuple(i) for i in independent["produced_sixsets"]))
                self.assertEqual(
                    z["unblocked_source_disjoint_original_six_ID_directed_paths"],
                    independent["unblocked_paths_avoiding_all_six_forbidden_ids"])
                self.assertEqual(
                    z["accepted_true_original_BBo_sixsets"],
                    independent["accepted_original_BBo_subcount_avoiding_Z"])
                self.assertTrue(z[
                    "historical_full_GF5_BBo_positive_class_verified"])

    def test_falsified_original_global_source_and_deletion_overlap_fail_closed(self):
        m=self.maps[1,"lex"]
        f,g=m["left_labels"],m["right_labels"]
        with self.assertRaises(ValueError):
            _masked_half_audit(1,f,g,(0,1,2),(2,))
        with self.assertRaises(ValueError):
            _masked_half_audit(1,f,g,(0,0,1),())
        with self.assertRaises(ValueError):
            _masked_half_audit(1,f,g,(0,1),(45,))
        with self.assertRaises(ValueError):
            _masked_half_audit(1,f,g,(0,1),(-1,))
        with self.assertRaises(ValueError):
            _masked_half_audit(1,f,g,(0,1),(True,))
        corrupt=list(f)
        corrupt[0]=corrupt[1]
        with self.assertRaises(ValueError):
            _masked_half_audit(1,corrupt,g,(0,1),())
        with self.assertRaises(ValueError):
            _masked_half_audit(3,f,g,(0,1),())


if __name__=="__main__":
    unittest.main()
