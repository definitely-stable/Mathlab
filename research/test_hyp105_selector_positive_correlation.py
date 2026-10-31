"""Independent exact selector referee: old all-h factors and new 4x/27x."""
from fractions import Fraction
from itertools import combinations,permutations,product
from math import factorial
import json
from pathlib import Path
import unittest

from hyp105_selector_positive_correlation import (
    exact_joint_local_minimum_probability,
    local_minimum_lower_probability,
    improved_path_selector_sigma,
    genuine_original_path_selector_probabilities,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source


def separate_exact_priority_permutation_oracle(graph,targets):
    """Combinatorially independent direct n! priority-order enumeration."""
    target=set(targets)
    vertices=tuple(graph)
    accepted=0
    for order in permutations(vertices):
        index={v:i for i,v in enumerate(order)}
        if all(all(index[t]<index[w] for w in graph[t]) for t in target):
            accepted+=1
    return Fraction(accepted,factorial(len(vertices)))


def exact_independent_coordinate_two_half_cuts(r):
    """Direct all binary colorings of distinct path-coordinate symbols."""
    words=tuple(product((0,1),repeat=r+1))
    passing=sum(
        all(a[j]!=a[j+1] and b[j]!=b[j+1] for j in range(r))
        for a in words for b in words
    )
    return Fraction(passing,len(words)**2)


class TestSelectorPositiveCorrelation(unittest.TestCase):
    def test_exhaustive_all_five_vertex_conflict_graphs_exact_probability(self):
        vertices=tuple(range(5))
        pairs=tuple(combinations(vertices,2))
        checked=0
        for mask in range(1<<len(pairs)):
            graph={v:set() for v in vertices}
            for bit,(u,v) in enumerate(pairs):
                if mask&(1<<bit):
                    graph[u].add(v)
                    graph[v].add(u)
            for r in (2,3):
                for T in combinations(vertices,r):
                    if any(y in graph[x] for x,y in combinations(T,2)):
                        continue
                    expected=separate_exact_priority_permutation_oracle(graph,T)
                    observed=exact_joint_local_minimum_probability(graph,T)
                    independent=local_minimum_lower_probability(graph,T)
                    self.assertEqual(observed,expected)
                    self.assertGreaterEqual(observed,independent)
                    self.assertGreaterEqual(
                        observed,Fraction(1,(1+max(map(len,graph.values())))**r))
                    checked+=1
        self.assertGreater(checked,1000)

    def test_overlap_correlation_is_strict_and_not_independence(self):
        # Conflict path (0--2--1), targets 0,1 are nonadjacent.
        # Shared neighbor 2 must follow both targets:
        # P(U2>max(U0,U1))=1/3 > 1/4=P(0 min)*P(1 min).
        graph={0:{2},1:{2},2:{0,1}}
        observed=exact_joint_local_minimum_probability(graph,(0,1))
        self.assertEqual(observed,Fraction(1,3))
        self.assertEqual(
            local_minimum_lower_probability(graph,(0,1)),
            Fraction(1,4))
        self.assertEqual(observed*exact_independent_coordinate_two_half_cuts(2),
                         Fraction(1,48))
        # A third nonconflicting target with a disjoint leaf exactly
        # factors its own local minimum; shared pair still has gain.
        graph={0:{3},1:{3},2:{4},3:{0,1},4:{2}}
        self.assertEqual(exact_joint_local_minimum_probability(
            graph,(0,1,2)),Fraction(1,6))
        self.assertEqual(local_minimum_lower_probability(
            graph,(0,1,2)),Fraction(1,8))
        with self.assertRaises(ValueError):
            exact_joint_local_minimum_probability({0:{1},1:{0}},(0,1))
        with self.assertRaises(ValueError):
            exact_joint_local_minimum_probability({0:{1},1:set()},(0,))
        with self.assertRaises(ValueError):
            local_minimum_lower_probability({0:{1},1:{0}},(0,1))

    def test_exact_all_h_sigma_replacement_and_independent_cut_oracle(self):
        for K in (0,1,2,3,8,64,1000):
            with self.subTest(K=K):
                q=improved_path_selector_sigma(K)
                self.assertEqual(q["sigma2_new_over_old"],4)
                self.assertEqual(q["sigma3_new_over_old"],27)
                self.assertEqual(q["new_sigma2"],Fraction(1,16*(K+1)**2))
                self.assertEqual(q["new_sigma3"],Fraction(1,64*(K+1)**3))
                self.assertEqual(
                    q["proper_P2_Frobenius_squared_coefficient_old"],
                    16*q["proper_P2_Frobenius_squared_coefficient_new"])
                self.assertEqual(
                    q["proper_P3_Frobenius_squared_coefficient_old"],
                    729*q["proper_P3_Frobenius_squared_coefficient_new"])
        for r in (2,3):
            self.assertEqual(
                exact_independent_coordinate_two_half_cuts(r),
                Fraction(1,4**r))
        for invalid in (-1,True,1.5):
            with self.assertRaises(ValueError):
                improved_path_selector_sigma(invalid)

    def test_true_original_W32_five_correlated_g_and_real_proper_paths(self):
        model=pair_labeled_symplectic(1,"lex")
        f=tuple(model["left_labels"])
        base=tuple(model["right_labels"])
        total=0
        for shift in (0,1,3,7,11):
            g=tuple(base[(i+shift)%len(base)] for i in range(len(base)))
            for r in (2,3):
                with self.subTest(shift=shift,r=r):
                    result=genuine_original_path_selector_probabilities(
                        1,f,g,r=r,max_paths=16)
                    self.assertGreater(result["paths_checked"],0)
                    self.assertEqual(
                        result["new_all_h_uniform_sigma"],
                        improved_path_selector_sigma(
                            result["original_core_max_conflict_degree_K"])[
                                f"new_sigma{r}"])
                    for cert in result["original_proper_path_certificates"]:
                        self.assertEqual(
                            len(cert["original_flag_IDs_ordered"]),r)
                        self.assertEqual(
                            cert["both_typed_coordinate_cut_probability"],
                            Fraction(1,4**r))
                        self.assertGreaterEqual(
                            cert["whole_source_flag_path_exact_survival_probability"],
                            cert["all_h_uniform_sigma_floor"])
                        self.assertGreaterEqual(
                            cert["priority_exact_joint_probability"],
                            cert["priority_degree_product_floor"])
                    total+=result["paths_checked"]
        self.assertGreaterEqual(total,40)

    def test_true_original_W34_full_sparse_and_reassigned_g_paths(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f=tuple(map(tuple,fixture["f"]))
        g=tuple(map(tuple,fixture["g"]))
        _,V,flags=genuine_source(2)
        cores=(
            ("full",None,g),
            ("sparse",tuple(i for i in range(len(flags)) if i%3),g),
            ("reassigned",tuple(i for i in range(len(flags)) if i%4),
                tuple(g[(i+17)%V] for i in range(V))),
        )
        for label,core,right in cores:
            for r in (2,3):
                with self.subTest(label=label,r=r):
                    c=genuine_original_path_selector_probabilities(
                        2,f,right,core,r=r,max_paths=14)
                    self.assertGreater(c["paths_checked"],0)
                    self.assertTrue(c["not_a_computational_proof_for_all_h"])
                    self.assertTrue(all(
                        z["priority_exact_joint_probability"]>=
                            z["priority_degree_product_floor"]
                        for z in c["original_proper_path_certificates"]))

    def test_invalid_real_original_path_inputs_fail_closed(self):
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        for bad in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                genuine_original_path_selector_probabilities(
                    1,f,g,bad)
        with self.assertRaises(ValueError):
            genuine_original_path_selector_probabilities(1,f[:-1],g)
        with self.assertRaises(ValueError):
            genuine_original_path_selector_probabilities(1,f,g,r=4)
        with self.assertRaises(ValueError):
            genuine_original_path_selector_probabilities(
                1,f,g,max_paths=0)

    def test_machine_readable_symbolic_sigma_certificate(self):
        q=improved_path_selector_sigma(64)
        print("HYP105_AA4_SELPLUS_CERTIFICATE="+json.dumps({
            "scope":"all h original fixed maps, nonconflicting source path flags",
            "K":q["K"],
            "sigma2_new":str(q["new_sigma2"]),
            "sigma3_new":str(q["new_sigma3"]),
            "sigma2_gain":int(q["sigma2_new_over_old"]),
            "sigma3_gain":int(q["sigma3_new_over_old"]),
            "P2_square_bound_improvement":q["new_P2_Frobenius_upper_gain"],
            "P3_square_bound_improvement":q["new_P3_Frobenius_upper_gain"],
            "probabilities_exact_rational":True,
            "not_an_independent_full_Branch_A_proof":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
