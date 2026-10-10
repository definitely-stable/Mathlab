"""C15 independent same-map cluster minima, exact 4/36 W32 falsifiers."""
from itertools import combinations
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c14_domain_certificates import (
    seven_local_completion_lower,independent_exact_completion_audit,
    _filled_model,
)
from hyp105_g5e2b3e1c15_coupled_right_clusters import (
    coupled_right_witness_certificate,coupled_right_joint_branch_search,
    genuine_W32_C15_report,
)


class C15CoupledRightProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=pair_labeled_symplectic(1,"reverse-line")
        cls.f={i:PAIRS.index(cls.m["left_labels"][i]) for i in range(12)}
        cls.g={i:PAIRS.index(cls.m["right_labels"][i]) for i in range(12)}

    def test_3_free_true_right_signature_and_global_common_hierarchy(self):
        x=coupled_right_witness_certificate(self.m,self.f,self.g)
        old=seven_local_completion_lower(self.m,self.f,self.g)
        self.assertEqual(x["actual_one_common_right_completions"],6)
        self.assertEqual(x["C14_independent_single_seven_lower"],
                         old["certified_every_completion_S_seven_lower"])
        self.assertEqual(
            x["C14_independent_single_GF5_necessary_numerator_lower"],
            old["certified_every_completion_GF5_necessary_numerator_lower"])
        for suffix in ("seven_lower","GF5_necessary_numerator_lower"):
            if suffix=="seven_lower":
                a,b,c=(x[k] for k in
                   ("C14_independent_single_seven_lower",
                    "C15_support_cluster_seven_lower",
                    "C15_one_shared_right_seven_lower"))
            else:
                a,b,c=(x[k] for k in
                   ("C14_independent_single_GF5_necessary_numerator_lower",
                    "C15_support_cluster_GF5_necessary_numerator_lower",
                    "C15_one_shared_right_GF5_necessary_numerator_lower"))
            self.assertLessEqual(a,b)
            self.assertLessEqual(b,c)
        self.assertEqual(sum(t["original_six_incidence_witnesses"]
                             for t in x["signature_cluster_certificates"]),
                         x["eligible_all_left_pinned_candidates"])

    def test_right_prefix_monotone_and_left_prefix_monotone_for_S_and_GF5(self):
        x=coupled_right_witness_certificate(self.m,self.f,self.g)
        fl=dict(self.f);fl[12]=next(v for v in range(15) if v not in fl.values())
        gr=dict(self.g);gr[12]=next(v for v in range(15) if v not in gr.values())
        for fp,gp in ((fl,self.g),(self.f,gr),(fl,gr)):
            y=coupled_right_witness_certificate(self.m,fp,gp)
            for name in ("C15_support_cluster_seven_lower",
                         "C15_one_shared_right_seven_lower",
                         "C15_support_cluster_GF5_necessary_numerator_lower",
                         "C15_one_shared_right_GF5_necessary_numerator_lower"):
                self.assertGreaterEqual(y[name],x[name])

    def test_fully_pinned_true_seven_and_Gf5_exact(self):
        f={i:PAIRS.index(e) for i,e in enumerate(self.m["left_labels"])}
        g={i:PAIRS.index(e) for i,e in enumerate(self.m["right_labels"])}
        x=coupled_right_witness_certificate(self.m,f,g)
        reference=seven_census(self.m,independent_checks=False)
        for name in ("C14_independent_single_seven_lower",
                     "C15_support_cluster_seven_lower",
                     "C15_one_shared_right_seven_lower"):
            self.assertEqual(x[name],reference["S_seven"])
        for name in ("C14_independent_single_GF5_necessary_numerator_lower",
                     "C15_support_cluster_GF5_necessary_numerator_lower",
                     "C15_one_shared_right_GF5_necessary_numerator_lower"):
            self.assertEqual(x[name],reference["GF5_seven_lower_numerator"])
        self.assertEqual(x["actual_one_common_right_completions"],1)

    def test_all_36_joint_original_maps_independent_soundness(self):
        from hyp105_g5e2b3e1c14_domain_certificates import _completion_pairs
        lower=coupled_right_witness_certificate(self.m,self.f,self.g)
        mins=[]
        for fl,gr in _completion_pairs(self.m,self.f,self.g,max_full_maps=36):
            full=_filled_model(self.m,fl,gr)
            x=seven_census(full,independent_checks=False)
            self.assertGreaterEqual(
                x["S_seven"],lower["C15_one_shared_right_seven_lower"])
            self.assertGreaterEqual(
                x["GF5_seven_lower_numerator"],
                lower["C15_one_shared_right_GF5_necessary_numerator_lower"])
            mins.append(x["S_seven"])
        self.assertEqual(len(mins),36)
        self.assertEqual(min(mins),148)

    def test_small_true_4_joint_map_mode_optima(self):
        f=dict(self.f);g=dict(self.g)
        f[12]=next(v for v in range(15) if v not in f.values())
        g[12]=next(v for v in range(15) if v not in g.values())
        brute=independent_exact_completion_audit(
            self.m,f,g,max_full_maps=4)
        for mode in ("single","cluster","shared"):
            for objective,expected in (
                ("S_seven",brute["true_minimum_S_seven_in_box"]),
                ("GF5_floor_numerator",
                 brute["true_minimum_GF5_floor_numerator_in_box"])):
                z=coupled_right_joint_branch_search(
                    self.m,f,g,mode=mode,objective=objective,
                    max_full_maps=4,max_nodes=30)
                self.assertEqual(z["exact_minimum_in_given_legal_joint_box"],
                                 expected)

    def test_invalid_domains_and_budget_fail_closed(self):
        with self.assertRaises(ValueError):
            coupled_right_witness_certificate(self.m,self.f,{})
        with self.assertRaises(ValueError):
            coupled_right_witness_certificate(self.m,{0:0,1:0},self.g)
        with self.assertRaises(ValueError):
            coupled_right_witness_certificate(
                self.m,self.f,self.g,max_motif_evaluations=1)
        with self.assertRaises(ValueError):
            coupled_right_joint_branch_search(
                self.m,self.f,self.g,max_nodes=1)
        with self.assertRaises(ValueError):
            coupled_right_joint_branch_search(
                self.m,self.f,self.g,mode="random")
        with self.assertRaises(ValueError):
            coupled_right_joint_branch_search(
                self.m,self.f,self.g,objective="full_GF5_exact")


if __name__=="__main__":
    unittest.main()
