"""C14: true W32 seven-family partial pair lower + bounded joint oracle."""
import unittest
from itertools import permutations
from math import factorial

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c14_domain_certificates import (
    seven_local_completion_lower,
    independent_exact_completion_audit,
    bounded_exact_joint_branch_search,
    genuine_W32_C14_report,
    _filled_model,
)


class C14W32JointProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=pair_labeled_symplectic(1,"reverse-line")
        cls.f={i:PAIRS.index(cls.model["left_labels"][i]) for i in range(13)}
        cls.g={i:PAIRS.index(cls.model["right_labels"][i]) for i in range(13)}

    def test_true_full_map_exact_zero_missing_dims(self):
        f={i:PAIRS.index(e) for i,e in enumerate(self.model["left_labels"])}
        g={i:PAIRS.index(e) for i,e in enumerate(self.model["right_labels"])}
        b=seven_local_completion_lower(self.model,f,g)
        actual=seven_census(self.model,independent_checks=False)
        self.assertEqual(b["certified_every_completion_S_seven_lower"],
                         actual["S_seven"])
        self.assertEqual(b["certified_every_completion_GF5_necessary_numerator_lower"],
                         actual["GF5_seven_lower_numerator"])
        self.assertEqual(sum(b["per_class_guaranteed_count_lower"].values()),
                         actual["S_seven"])
        self.assertEqual(b["left_pinned_fully_decidable_candidates"],62370)
        self.assertEqual(b["exact_local_classifications"],62370)
        self.assertEqual(actual["S_seven"],169)

    def test_partial_bound_for_every_genuine_two_by_two_completion(self):
        bound=seven_local_completion_lower(self.model,self.f,self.g)
        brute=independent_exact_completion_audit(
            self.model,self.f,self.g,max_full_maps=4)
        self.assertLessEqual(bound["certified_every_completion_S_seven_lower"],
                             brute["true_minimum_S_seven_in_box"])
        self.assertLessEqual(
            bound["certified_every_completion_GF5_necessary_numerator_lower"],
            brute["true_minimum_GF5_floor_numerator_in_box"])
        self.assertGreaterEqual(
            bound["locally_inevitable_seven_motifs"],
            bound["frozen_both_halves_positive_motifs"])
        self.assertEqual(brute["complete_joint_maps_checked"],4)

    def test_monotone_on_both_true_partial_extensions(self):
        b=seven_local_completion_lower(self.model,self.f,self.g)
        left_new=dict(self.f)
        left_new[13]=next(j for j in range(15) if j not in self.f.values())
        right_new=dict(self.g)
        right_new[13]=next(j for j in range(15) if j not in self.g.values())
        for f,g in ((left_new,self.g),(self.f,right_new),(left_new,right_new)):
            c=seven_local_completion_lower(self.model,f,g)
            self.assertGreaterEqual(c["certified_every_completion_S_seven_lower"],
                                    b["certified_every_completion_S_seven_lower"])
            self.assertGreaterEqual(
                c["certified_every_completion_GF5_necessary_numerator_lower"],
                b["certified_every_completion_GF5_necessary_numerator_lower"])

    def test_joint_branch_exact_against_completely_separate_oracle(self):
        audit=independent_exact_completion_audit(
            self.model,self.f,self.g,max_full_maps=4)
        tree=bounded_exact_joint_branch_search(
            self.model,self.f,self.g,max_full_maps=4,max_nodes=20)
        self.assertEqual(tree["exact_minimum_within_fixed_joint_completion_box"],
                         audit["true_minimum_S_seven_in_box"])
        self.assertLessEqual(tree["leaves_explicitly_evaluated"],4)
        self.assertLessEqual(tree["nodes_visited"],20)

    def test_true_all_36_joint_W32_box_not_promoted_to_global(self):
        result=genuine_W32_C14_report()
        self.assertEqual(result["all_true_full_joint_mapping_pairs_in_box"],36)
        self.assertEqual(result["independent_true_box_S_min"],
                         result["branch_exact_same_S_min"])
        self.assertLessEqual(result["locally_inevitable_7_motifs_lower"],
                             result["independent_true_box_S_min"])
        self.assertTrue(result["not_global_W32_or_all_h_result"])

    def test_bad_partial_right_budget_and_duplicate_label_fail_closed(self):
        with self.assertRaises(ValueError):
            seven_local_completion_lower(self.model,{}, {})
        with self.assertRaises(ValueError):
            seven_local_completion_lower(self.model,{0:0,1:0},self.g)
        with self.assertRaises(ValueError):
            seven_local_completion_lower(self.model,self.f,{0:True})
        with self.assertRaises(ValueError):
            seven_local_completion_lower(
                self.model,self.f,self.g,max_motif_evaluations=1)
        with self.assertRaises(ValueError):
            independent_exact_completion_audit(
                self.model,self.f,self.g,max_full_maps=3)
        with self.assertRaises(ValueError):
            bounded_exact_joint_branch_search(
                self.model,self.f,self.g,max_nodes=1)
        with self.assertRaises(ValueError):
            bounded_exact_joint_branch_search(
                self.model,self.f,self.g,objective="signed_R3_exact")


if __name__=="__main__":
    unittest.main()
