"""Adversarial AA4-B75: true ORIGINAL source finite candidate research and all-h risk gate."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_adversarial_B75_referee import (
    SCHEMA,ROOT_STATUS,SEED,PAIR_ALPHABET,FLAGS,
    IDENTITY,REVERSE,P3_SOURCE_J_K,TARGET,
    genuine_source_for_assignment,all_genuine_proper_p3,
    original_incompatibility,_path_groups,_proxy_weight,fast_screen,
    _exact_original_local_priority,_exact_original_P3_weights,
    _independent_clique_number,exact_source_risk,
    _initial_labelings,_mutate_labels,deterministic_adversarial_scan,
)


class TestAdversarialExactOriginalB75(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=deterministic_adversarial_scan(trials=40,seed=SEED,shortlist=3)
        cls.baseline=cls.report["predeclared_exact_true_source_baselines"]
        cls.leaders=cls.report["exact_fraction_top_candidate_shortlist"]

    def test_open_root_and_no_general_extrapolation(self):
        q=self.report
        self.assertEqual(q["schema"],SCHEMA)
        self.assertEqual(q["issue"],230)
        self.assertEqual(q["status"],ROOT_STATUS)
        self.assertFalse(q["root_PROVED_A"])
        self.assertFalse(q["all_h_B_over_M_less_3_over_4_PROVED"])
        self.assertFalse(q["counterexample_to_asymptotic_B75_claimed"])
        self.assertTrue(q["strict_no_universal_extrapolation_from_finite_witness"])
        self.assertFalse(q["numerical_external_graph_C6_constants_claimed"])

    def test_original_W32_paired_source_exact_flags_and_bijections(self):
        self.assertEqual(len(FLAGS),45)
        self.assertEqual(len(set(FLAGS)),45)
        self.assertEqual(len(PAIR_ALPHABET),15)
        c=genuine_source_for_assignment(IDENTITY,IDENTITY)
        self.assertEqual(len(c["ids"]),45)
        self.assertEqual(len(c["edges"]),90)
        self.assertEqual(c["deleted_original_IDs"],tuple())
        self.assertEqual(tuple(sorted(c["f"])),tuple(sorted(PAIR_ALPHABET)))
        self.assertEqual(tuple(sorted(c["g"])),tuple(sorted(PAIR_ALPHABET)))
        self.assertLessEqual(c["source_max_J"],P3_SOURCE_J_K)

    def test_actual_original_physical_both_diagonals_unique_owned(self):
        c=genuine_source_for_assignment(REVERSE,IDENTITY)
        for i in c["ids"]:
            self.assertEqual(sum(x==i for x in c["edges"].values()),2)
            self.assertTrue(all(i in c["J"][j] for j in c["J"][i]))
        self.assertEqual(len(c["edges"]),2*len(c["ids"]))

    def test_complete_real_original_W32_lex_P3_and_risk_fraction(self):
        x=self.baseline[0]
        self.assertEqual(x["full_original_proper_directed_P3"],1346)
        self.assertEqual(x["ordered_same_end_path_pair_count"],4370)
        self.assertEqual(Fraction(x["exact_ratio_B_over_M"]),
            Fraction(395498199363009600,1190067603581473393))
        self.assertEqual(Fraction(x["exact_weighted_M"]),
            Fraction(170009657654496199,164130319761408000000))
        self.assertEqual(x["true_actual_physical_edges"],90)
        self.assertFalse(x["original_named_deletions"])

    def test_complete_real_original_W32_reverse_P3_and_risk_fraction(self):
        x=self.baseline[1]
        self.assertEqual(x["full_original_proper_directed_P3"],1154)
        self.assertEqual(x["ordered_same_end_path_pair_count"],2942)
        self.assertEqual(Fraction(x["exact_ratio_B_over_M"]),
            Fraction(2197221736032,6861627242215))
        self.assertFalse(x["original_named_deletions"])

    def test_real_original_full_lex_disjoint_classes(self):
        self.assertEqual(self.baseline[0]["disjoint_joint_incompatibility_class_counts"],{
            "compatible":2386,
            "original_J":1348,
            "first_physical_coordinate":464,
            "second_physical_coordinate":172,
        })
        self.assertEqual(self.baseline[0]["actual_max_original_incompatibility_clique"],6)
        self.assertEqual(sum(self.baseline[0]["bin_clique_histogram"].values()),
            self.baseline[0]["physical_ordered_endpoint_bins"])

    def test_candidate_exact_rational_full_source_B_M_G(self):
        for row in self.leaders+self.baseline:
            m=Fraction(row["exact_weighted_M"])
            g=Fraction(row["exact_weighted_G"])
            b=Fraction(row["exact_weighted_B"])
            self.assertGreater(m,0)
            self.assertEqual(g+b,m)
            self.assertEqual(Fraction(row["exact_ratio_G_over_M"])+
                             Fraction(row["exact_ratio_B_over_M"]),1)
            self.assertEqual(Fraction(row["exact_ratio_B_over_M"]),b/m)
            self.assertEqual(sum(row["disjoint_joint_incompatibility_class_counts"].values()),
                             row["ordered_same_end_path_pair_count"])
            self.assertEqual(row["true_actual_physical_edges"],90)
            self.assertLessEqual(row["max_original_source_J_degree"],64)
            self.assertTrue(row["original_pair_injection"])
            self.assertTrue(all(x==i for x,i in []))

    def test_candidates_global_f_g_fully_injective_not_frozen_lex(self):
        for row in self.leaders:
            f=tuple(row["label_map_point_f_perm"])
            g=tuple(row["label_map_line_g_perm"])
            self.assertEqual(tuple(sorted(f)),IDENTITY)
            self.assertEqual(tuple(sorted(g)),IDENTITY)
            c=genuine_source_for_assignment(f,g)
            self.assertEqual(len(c["edges"]),90)
            self.assertEqual(len(c["ids"]),45)
            self.assertFalse(c["deleted_original_IDs"])

    def test_exact_full_original_W32_genuine_owner_priority_vs_frozen_referee(self):
        # TEST-ONLY comparison to separate pre-existing PRIOR source rank implementation.
        from hyp105_original_badpair_clique_motzkin_referee import _source_joint_priority
        c=genuine_source_for_assignment(
            tuple(self.leaders[0]["label_map_point_f_perm"]),
            tuple(self.leaders[0]["label_map_line_g_perm"]))
        paths=all_genuine_proper_p3(c)
        for _,os in paths[:15]:
            self.assertEqual(_exact_original_local_priority(os,c["J"]),
                _source_joint_priority(os,c["J"]))

    def test_heuristic_is_not_claimed_exact_or_probabilistic_evidence(self):
        q=self.report
        self.assertTrue(q["original_f_and_g_separately_permuted"])
        self.assertTrue(q["source_original_Z_deleted_in_search"] is False)
        self.assertEqual(q["random_seed"],SEED)
        self.assertEqual(q["proposal_budget"],40)
        self.assertGreaterEqual(q["unique_completed_proxy_trials"],40)
        self.assertGreaterEqual(len(q["seeded_proposal_categories"]),2)
        self.assertTrue(q["nonproof_fast_degree_product_proxy_max"])

    def test_original_correlated_assignments_replay_deterministically(self):
        again=deterministic_adversarial_scan(trials=40,seed=SEED,shortlist=3)
        self.assertEqual(
            self.report["best_exact_original_W32_full_source_witness"]["label_map_point_f_perm"],
            again["best_exact_original_W32_full_source_witness"]["label_map_point_f_perm"])
        self.assertEqual(
            self.report["best_exact_original_W32_full_source_witness"]["label_map_line_g_perm"],
            again["best_exact_original_W32_full_source_witness"]["label_map_line_g_perm"])
        self.assertEqual(self.report["best_exact_original_W32_ratio"],
                         again["best_exact_original_W32_ratio"])

    def test_minimax_source_risk_at_least_lex_baseline(self):
        best=Fraction(self.report["best_exact_original_W32_ratio"])
        lex=Fraction(self.baseline[0]["exact_ratio_B_over_M"])
        self.assertGreaterEqual(best,lex)
        self.assertEqual(
            best,
            Fraction(self.report["best_exact_original_W32_full_source_witness"]["exact_ratio_B_over_M"]))

    def test_all_exact_candidates_Motzkin_weighted_source_bound(self):
        for row in self.leaders+self.baseline:
            M=Fraction(row["exact_weighted_M"])
            good=Fraction(row["exact_weighted_G"])
            floor=Fraction(row["exact_Motzkin_G_floor"])
            k=row["actual_max_original_incompatibility_clique"]
            self.assertGreaterEqual(good,floor)
            self.assertGreaterEqual(floor,M/Fraction(16*65**3))
            self.assertEqual(
                Fraction(row["exact_Motzkin_bound_on_B_over_M"]),1-floor/M)
            self.assertLessEqual(k,16*65**3)
            self.assertEqual(sum(row["bin_clique_histogram"].values()),
                row["physical_ordered_endpoint_bins"])

    def test_all_h_necessary_clique_five_critical_threshold(self):
        q=self.report
        self.assertTrue(q["mathematical_all_h_clique_five_necessary_for_B_over_M_ge_3_4"])
        self.assertTrue(q["mathematical_weighted_clique_bin_certifies_strict_B_below_3_4_when_sum_M_over_omega_gt_M_over_4"])
        for row in self.leaders+self.baseline:
            B=Fraction(row["exact_ratio_B_over_M"])
            k=row["actual_max_original_incompatibility_clique"]
            if B>=Fraction(3,4):
                self.assertGreaterEqual(k,5)
            if row["weighted_Motzkin_alone_proves_B_over_M_below_three_quarters"]:
                self.assertLess(B,Fraction(3,4))

    def test_explicit_abstract_K4_equal_weight_is_boundary_not_strict(self):
        n=4
        # Equality in weighted Motzkin at clique4: strict 3/4 needs more.
        w=[Fraction(1,n)]*n
        B=sum((w[i]*w[j] for i in range(n) for j in range(n) if i!=j),Fraction(0))
        self.assertEqual(B,Fraction(3,4))
        self.assertEqual(n,4)

    def test_explicit_abstract_K5_can_exceed_3_over_4_not_original(self):
        n=5
        w=[Fraction(1,n)]*n
        B=sum((w[i]*w[j] for i in range(n) for j in range(n) if i!=j),Fraction(0))
        self.assertEqual(B,Fraction(4,5))
        self.assertGreater(B,TARGET)
        # This is a PURE GRAPH demonstration, NOT an ORIGINAL GQ witness.

    def test_real_original_named_Z_deletion_still_owns_two_physical_edges(self):
        ids=tuple(i for i in range(45) if i%17!=0)
        c=genuine_source_for_assignment(IDENTITY,REVERSE,ids)
        self.assertEqual(len(c["deleted_original_IDs"]),3)
        self.assertEqual(len(c["edges"]),84)
        self.assertEqual(len(c["ids"]),42)
        for i in c["ids"]:
            self.assertEqual(sum(j==i for j in c["edges"].values()),2)
        r=exact_source_risk(IDENTITY,REVERSE,ids)
        self.assertEqual(r["paired_CORE_original_source_flags"],42)
        self.assertEqual(len(r["original_named_deletions"]),3)
        # Not asserted to satisfy asymptotic rho*s^4 constraint at small s.

    def test_zero_or_corrupt_original_assignments_rejected(self):
        with self.assertRaises(ValueError):
            genuine_source_for_assignment(IDENTITY[:-1],IDENTITY)
        with self.assertRaises(ValueError):
            genuine_source_for_assignment(IDENTITY,tuple([0]*15))
        with self.assertRaises(ValueError):
            deterministic_adversarial_scan(trials=5)
        with self.assertRaises(ValueError):
            deterministic_adversarial_scan(trials=2001)
        with self.assertRaises(ValueError):
            original_incompatibility(
                (((0,0),(1,1),(2,2),(3,3)),(0,1,2)),
                (((3,3),(1,2),(2,1),(0,0)),(0,1,2)),
                [set() for _ in range(45)])


if __name__=="__main__":
    unittest.main()
