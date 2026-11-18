"""AA4-LOW-MOMENT-EXACT: independent exact priority and Jensen falsifiers."""
from fractions import Fraction
from itertools import permutations
from math import comb
import unittest

from hyp105_original_low_moment_exact_priority import (
    SCHEMA,ROOT_STATUS,K_ROOT,
    priority_probability,exact_subset_priority,exact_direct_permutations,
    genuine_original_model,_proper_paths,sample_exact_weighted_jensen,
    abstract_mask_case,certificate
)


def graph_from_masks(r, masks):
    n=r+sum(masks.values())
    nbr=[set() for _ in range(n)]
    j=r
    for mask,k in masks.items():
        for _ in range(k):
            for o in range(r):
                if mask&(1<<o):
                    nbr[o].add(j)
                    nbr[j].add(o)
            j+=1
    return nbr


class TestOriginalLowMomentExactPriority(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_independent_neighbor_source_owners_not_treated_independent_paths(self):
        nbr=graph_from_masks(2,{1:1,2:1})
        d=priority_probability(nbr,(0,1))
        self.assertEqual(d["exact"],Fraction(1,4))
        self.assertEqual(d["first_r_sufficient"],Fraction(1,6))
        self.assertEqual(d["exact"],exact_direct_permutations(nbr,(0,1)))
        self.assertEqual(d["exact"],exact_subset_priority(nbr,(0,1)))

    def test_02_shared_neighbors_show_source_event_dependency(self):
        nbr=graph_from_masks(2,{3:1})
        d=priority_probability(nbr,(0,1))
        self.assertEqual(d["exact"],Fraction(1,3))
        self.assertNotEqual(d["exact"],Fraction(1,4))
        self.assertEqual(d["exact"],d["first_r_sufficient"])
        self.assertEqual(d["exact"],exact_direct_permutations(nbr,(0,1)))

    def test_03_single_owner_full_priority_minimum(self):
        nbr=graph_from_masks(1,{1:4})
        d=priority_probability(nbr,(0,))
        self.assertEqual(d["exact"],Fraction(1,5))
        self.assertEqual(d["exact"],exact_direct_permutations(nbr,(0,)))
        self.assertEqual(d["exact"],exact_subset_priority(nbr,(0,)))

    def test_04_all_small_mask_types_r2_bruteforce_matches_fraction_integral(self):
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    nbr=graph_from_masks(2,{1:a,2:b,3:c})
                    d=priority_probability(nbr,(0,1))
                    self.assertEqual(d["exact"],exact_direct_permutations(nbr,(0,1)))
                    self.assertEqual(d["exact"],exact_subset_priority(nbr,(0,1)))

    def test_05_all_small_mask_types_r3_subset_DP_and_mixed_multiplicity(self):
        masks=(1,2,3,4,5,6,7)
        for k in masks:
            for j in masks:
                if k>j:
                    continue
                nbr=graph_from_masks(3,{k:1,j:1})
                d=priority_probability(nbr,(0,1,2))
                self.assertEqual(d["exact"],exact_direct_permutations(nbr,(0,1,2)))
                self.assertEqual(d["exact"],exact_subset_priority(nbr,(0,1,2)))
                self.assertGreaterEqual(d["exact"],d["first_r_sufficient"])

    def test_06_full_195_owner_source_neighborhood_no_exponential_DP(self):
        nbr=graph_from_masks(3,{7:192})
        v=priority_probability(nbr,(0,1,2))
        self.assertEqual(v["b"],195)
        self.assertEqual(v["exact"],Fraction(1,comb(195,3)))
        self.assertEqual(v["first_r_sufficient"],v["exact"])
        with self.assertRaises(ValueError):
            exact_subset_priority(nbr,(0,1,2))

    def test_07_195_union_three_nonoverlap_color_and_source(self):
        nbr=graph_from_masks(3,{1:64,2:64,4:64})
        d=priority_probability(nbr,(0,1,2))
        self.assertEqual(d["b"],195)
        self.assertEqual(d["exact"],Fraction(1,65**3))
        self.assertGreater(d["exact"],d["first_r_sufficient"])
        self.assertEqual(d["exact_path_survival"],Fraction(1,64*65**3))

    def test_08_original_genuine_source_unique_two_diagonals_and_symmetric_J(self):
        for s in (2,4):
            m=genuine_original_model(s,"reverse")
            V=(s+1)*(s*s+1)
            self.assertEqual(m["V"],V)
            self.assertEqual(len(m["flags"]),(s+1)*V)
            self.assertEqual(len(m["physical_edgeowner"]),2*len(m["flags"]))
            self.assertEqual(m["full_source_J_edges"],
                             sum(len(x) for x in m["nbr"])//2)
            self.assertTrue(all(i not in m["nbr"][i]
                                for i in range(len(m["flags"]))))
            self.assertTrue(all(i in m["nbr"][j]
                                for j in range(len(m["flags"]))
                                for i in m["nbr"][j]))

    def test_09_true_original_proper_physical_paths_source_owner_conflict_free(self):
        for s in (2,4):
            m=genuine_original_model(s,"lex")
            for r in (2,3):
                sample=list(_proper_paths(m,r,45))
                self.assertGreater(len(sample),0)
                for vertices,owners in sample:
                    self.assertEqual(len(vertices),r+1)
                    self.assertEqual(len(set(owners)),r)
                    for i in range(r):
                        self.assertNotIn(owners[i],m["nbr"][owners[(i+1)%r]])
                    p=priority_probability(m["nbr"],owners)
                    self.assertGreaterEqual(p["exact_path_survival"],
                                            p["global_K64_survival_floor"])

    def test_10_exact_weighted_Jensen_endpoint_norm_beats_global_uniform(self):
        for row in self.cert["genuine_original_W32_W34_weighted_marginal_cases"]:
            exact=Fraction(row["exact_marginal_weighted_endpoint_energy"])
            uniform=Fraction(row["uniform_true_K_endpoint_energy"])
            root=Fraction(row["uniform_K64_endpoint_energy"])
            self.assertGreaterEqual(exact,uniform)
            self.assertGreaterEqual(uniform,root)
            self.assertGreater(row["sampled_source_proper_paths"],0)
            self.assertGreater(row["distinct_true_owner_sets"],0)
            self.assertLessEqual(row["largest_actual_local_neighborhood_b"],
                                 row["r"]*(row["max_original_J_degree"]+1))
            self.assertTrue(row["actual_exact_priority_marginal_is_shared_global_permutation"])
            self.assertTrue(row["no_joint_path_independence_assumed"])

    def test_11_actual_true_source_exact_priority_matches_independent_DP(self):
        m=genuine_original_model(2,"reverse")
        for r in (2,3):
            verified=0
            for vertices,owners in _proper_paths(m,r,140):
                p=priority_probability(m["nbr"],owners)
                if p["b"]<=15:
                    self.assertEqual(p["exact"],exact_subset_priority(m["nbr"],owners))
                    verified+=1
                if verified>=10:
                    break
            self.assertGreater(verified,0)

    def test_12_negative_conflicting_owners_invalid_or_asymmetric_J_rejected(self):
        nbr=graph_from_masks(2,{1:1,2:1})
        nbr[0].add(1)
        nbr[1].add(0)
        with self.assertRaises(ValueError):
            priority_probability(nbr,(0,1))
        nbr2=graph_from_masks(2,{1:1})
        nbr2[2].remove(0)
        with self.assertRaises(ValueError):
            priority_probability(nbr2,(0,1))
        with self.assertRaises(ValueError):
            priority_probability(nbr2,(0,0))
        with self.assertRaises(ValueError):
            priority_probability(nbr2,(0,1,10))

    def test_13_invalid_mask_and_wrong_probability_universe_fail_closed(self):
        with self.assertRaises(ValueError):
            abstract_mask_case(3,{8:1})
        with self.assertRaises(ValueError):
            abstract_mask_case(3,{0:1})
        with self.assertRaises(ValueError):
            abstract_mask_case(3,{7:-1})
        with self.assertRaises(ValueError):
            abstract_mask_case(4,{1:1})

    def test_14_no_root_theorem_promotion_only_local_marginal_transfer(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],770)
        self.assertEqual(len(c["abstract_real_source_conflict_mask_cases"]),6)
        self.assertEqual(len(c["genuine_original_W32_W34_weighted_marginal_cases"]),5)
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["ASET_exponent_claimed"])
        self.assertTrue(c["all_h_no_b20_or_exponential_subset_DP_restriction"])
        self.assertTrue(c["all_h_NO_path_independence_assumed"])
        self.assertTrue(c["all_h_original_C6_to_D6_and_GLOBAL_moment_dependencies_remain_open"])


if __name__=="__main__":
    unittest.main()
