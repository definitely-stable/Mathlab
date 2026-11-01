"""AA4-CELLREF: independent abstract-graph / actual ORIGINAL GQ falsifiers."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_mixed_cellwise_effective_degree_referee import (
    arbitrary_graph_cellwise_certificate,independent_original_cell_referee,
)
from hyp105_four_internal_blocker_weighted_referee import four_blocker_referee


def maps(power,k=0):
    _,V,_=genuine_source(power)
    a=2
    while a*(a-1)//2<V:a+=1
    labels=tuple(combinations(range(a),2))[:V]
    return labels,tuple(labels[(19*i+k)%V] for i in range(V))


class ExactEffectiveDegreeMixedBlocker(unittest.TestCase):
    def test_all_64_bipartite_two_by_three_graphs_all_residues(self):
        for mask in range(64):
            graph={i:set() for i in range(5)}
            for x in range(2):
                for y in range(3):
                    if mask & (1<<(3*x+y)):
                        graph[x].add(2+y)
                        graph[2+y].add(x)
            triples_all=[(v0,u,w) for v0 in graph for u in graph[v0] for w in graph]
            for residue in range(6):
                triples=tuple(t for j,t in enumerate(triples_all)
                              if (j+residue*17+mask)%6 in (0,1,2))
                z=arbitrary_graph_cellwise_certificate(graph,triples)
                self.assertTrue(z["new_never_worse"])
                self.assertLessEqual(z["new_cauchy_bound"],z["old_cauchy_bound"])
                self.assertLessEqual(z["weighted_completions"]**2,
                                     z["new_cauchy_bound"])
                self.assertLessEqual(z["supported_degree_weighted_moment"],
                                     z["full_degree_weighted_moment"])
                self.assertLessEqual(z["Xi_effective_first_edge"],z["triples"])

    def test_all_256_bipartite_two_by_four_graphs_stress_irregular(self):
        for mask in range(256):
            graph={i:set() for i in range(6)}
            for x in range(2):
                for y in range(4):
                    if mask & (1<<(4*x+y)):
                        graph[x].add(2+y)
                        graph[2+y].add(x)
            triples_all=[(v0,u,w) for v0 in graph for u in graph[v0] for w in graph]
            for residue in (0,1,2,3):
                triples=tuple(t for j,t in enumerate(triples_all)
                              if (j+residue+mask)%5==0)
                z=arbitrary_graph_cellwise_certificate(graph,triples)
                self.assertLessEqual(z["new_cauchy_bound"],z["old_cauchy_bound"])

    def test_strict_improvement_on_irregular_physical_support(self):
        graph={0:{2,3,4},1:{2,3,4},2:{0,1},3:{0,1},4:{0,1}}
        # Only ONE first edge 2->0 and one supported second endpoint 1.
        z=arbitrary_graph_cellwise_certificate(graph,((2,0,1),))
        self.assertEqual(z["weighted_completions"],3)
        self.assertEqual(z["Xi_effective_first_edge"],Fraction(1,3))
        self.assertEqual(z["supported_degree_weighted_moment"],27)
        self.assertEqual(z["new_cauchy_bound"],9)
        self.assertEqual(z["weighted_completions"]**2,9)
        self.assertTrue(z["strict_improvement"])
        self.assertGreater(z["old_cauchy_bound"],z["new_cauchy_bound"])

    def test_generic_full_candidate_support_has_no_universal_strict_gain(self):
        # For EVERY first physical edge and EVERY possible final vertex:
        # m(u,w)=deg(u), Xi=B, Theta_T=Theta identically.
        # Thus generic cellwise Cauchy alone CANNOT certify a uniform
        # strict gain in exponent; genuine original source restrictions
        # would be needed for any such claim.
        for graph in (
            {0:{1},1:{0}},
            {0:{2,3,4},1:{2,3,4},2:{0,1},3:{0,1},4:{0,1}},
            {0:{1,2},1:{0,2},2:{0,1}},
        ):
            full=tuple((v0,u,w) for v0 in graph for u in graph[v0]
                       for w in graph)
            z=arbitrary_graph_cellwise_certificate(graph,full)
            self.assertEqual(z["Xi_effective_first_edge"],z["triples"])
            self.assertEqual(z["supported_degree_weighted_moment"],
                             z["full_degree_weighted_moment"])
            self.assertEqual(z["new_cauchy_bound"],z["old_cauchy_bound"])
            self.assertFalse(z["strict_improvement"])

    def test_true_original_W32_full_and_deletions_compare_earlier_referee(self):
        _,V,flags=genuine_source(1)
        for k in (0,1,3):
            f,g=maps(1,k)
            for core in (None,tuple(range(0,len(flags),2)),
                         tuple(i for i in range(len(flags)) if i%5!=0),
                         tuple(range(0,len(flags),4))):
                with self.subTest(k=k,core=core is None):
                    z=independent_original_cell_referee(1,f,g,core)
                    historical=four_blocker_referee(1,f,g,core)
                    self.assertTrue(z["source_physical_identity_verified"])
                    self.assertEqual(z["original_full_core_phi"],
                                     historical["primal"]["phi"])
                    self.assertEqual(z["original_incident_defect"],
                                     historical["primal"]["incident_defect"])
                    self.assertEqual(z["left"]["weighted_completions"],
                                     historical["primal"]["weighted_completions"])
                    self.assertEqual(z["right"]["weighted_completions"],
                                     historical["dual"]["weighted_completions"])
                    self.assertEqual(z["four_position_union"],
                                     historical["proper_union"])
                    self.assertEqual(z["four_physical_blocked_positions"],
                                     historical["proper_blocked_by_position"])
                    self.assertLessEqual(z["left"]["new_cauchy_bound"],
                                         z["left"]["old_cauchy_bound"])
                    self.assertLessEqual(z["right"]["new_cauchy_bound"],
                                         z["right"]["old_cauchy_bound"])

    def test_true_original_W34_sparse_and_full_correlations(self):
        _,V,flags=genuine_source(2)
        for k,core in ((0,None),
                       (3,tuple(range(0,len(flags),3)))):
            with self.subTest(k=k):
                f,g=maps(2,k)
                z=independent_original_cell_referee(2,f,g,core)
                self.assertTrue(z["source_physical_identity_verified"])
                self.assertEqual(z["original_core_physical_edges"],
                                 2*z["original_core_ids"])
                for side in ("left","right"):
                    v=z[side]
                    self.assertLessEqual(v["new_cauchy_bound"],
                                         v["old_cauchy_bound"])
                    self.assertGreaterEqual(v["full_degree_weighted_moment"],
                                            v["supported_degree_weighted_moment"])
                self.assertEqual(
                    z["four_physical_blocked_positions"][0],
                    z["four_physical_blocked_positions"][1])
                self.assertEqual(
                    z["four_physical_blocked_positions"][2],
                    z["four_physical_blocked_positions"][3])

    def test_true_original_W34_protected_K44_sparse_source_core(self):
        f,g,ids=planted_original_k44()
        z=independent_original_cell_referee(2,f,g,ids)
        self.assertEqual(z["original_core_ids"],16)
        self.assertEqual(z["original_core_physical_edges"],32)
        self.assertTrue(z["source_physical_identity_verified"])

    def test_point_line_dual_symmetry_and_empty_original_core(self):
        f,g=maps(1,0)
        z=independent_original_cell_referee(1,f,g,())
        for side in ("left","right"):
            self.assertEqual(z[side]["triples"],0)
            self.assertEqual(z[side]["Xi_effective_first_edge"],0)
            self.assertEqual(z[side]["new_cauchy_bound"],0)
        self.assertEqual(z["four_position_union"],0)
        self.assertEqual(z["left"]["traceA4"],z["right"]["traceA4"])

    def test_reject_incorrect_triples_non_simple_graph_and_original_maps(self):
        graph={0:{1},1:{0}}
        for ts in (((0,1,0),(0,1,0)),((1,1,0),),((9,1,0),)):
            with self.assertRaises(ValueError):
                arbitrary_graph_cellwise_certificate(graph,ts)
        with self.assertRaises(ValueError):
            arbitrary_graph_cellwise_certificate({0:{1},1:set()},())
        with self.assertRaises(ValueError):
            arbitrary_graph_cellwise_certificate({0:{0}},())
        f,g=maps(1,0)
        with self.assertRaises(ValueError):
            independent_original_cell_referee(3,f,g)
        with self.assertRaises(ValueError):
            independent_original_cell_referee(1,f[:-1],g)
        with self.assertRaises(ValueError):
            independent_original_cell_referee(1,(f[0],)*len(f),g)
        with self.assertRaises(ValueError):
            independent_original_cell_referee(1,f,g,(0,0))
        with self.assertRaises(ValueError):
            independent_original_cell_referee(1,f,g,(True,))


if __name__=="__main__":
    unittest.main()
