"""AA4-PAIRSEL independent source-priority, color-CSP and path-pair tests."""
from fractions import Fraction
from itertools import combinations,permutations,product
from math import comb,factorial
import unittest

from hyp105_selector_path_pair_covariance_referee import (
    exact_source_priorities,exact_typed_bichromatic_probability,
    exact_joint_path_selector_law,exact_same_endpoints_path_second_moment,
    independent_genuine_source_path_pair_referee,
)
from hyp105_full_physical_degree_tail import genuine_source


def brute_priorities(graph,target):
    total=0
    for pi in permutations(graph):
        pos={v:i for i,v in enumerate(pi)}
        total+=all(all(pos[t]<pos[w] for w in graph[t]) for t in target)
    return Fraction(total,factorial(len(graph)))


def brute_color(edges):
    vertices=sorted({v for e in edges for v in e})
    passed=0
    for bits in product((0,1),repeat=len(vertices)):
        colors=dict(zip(vertices,bits))
        passed+=all(colors[a]!=colors[b] for a,b in edges)
    return Fraction(passed,2**len(vertices))


def brute_full_joint_source_and_both_colorings(graph,flags,f,g,P,Q):
    """Completely separate END-TO-END direct priority-and-two-color oracle.

    Enumerates all n! ORIGINAL source priority orders and all 2^(L+R)
    typed physical bit assignments. It never calls the new formula.
    Only for <=4 source flags and small used physical alphabets.
    """
    targets=set(P[1])|set(Q[1])
    left_symbols=sorted({x for i in targets for x in f[flags[i][0]]})
    right_symbols=sorted({y for i in targets for y in g[flags[i][1]]})
    assert len(graph)<=4 and len(left_symbols)+len(right_symbols)<=8
    total=accepted=0
    for priority in permutations(tuple(graph)):
        ranks={v:i for i,v in enumerate(priority)}
        source_ok=all(all(ranks[t]<ranks[w] for w in graph[t])
                      for t in targets)
        for bits in product((0,1),repeat=len(left_symbols)+len(right_symbols)):
            total+=1
            if not source_ok:continue
            lc=dict(zip(left_symbols,bits[:len(left_symbols)]))
            rc=dict(zip(right_symbols,bits[len(left_symbols):]))
            if all(lc[f[flags[i][0]][0]]!=lc[f[flags[i][0]][1]] and
                   rc[g[flags[i][1]][0]]!=rc[g[flags[i][1]][1]]
                   for i in targets):
                accepted+=1
    return Fraction(accepted,total)


def finite_labels(h,k=0):
    _,V,_=genuine_source(h)
    a=2
    while comb(a,2)<V:a+=1
    labels=tuple(combinations(range(a),2))[:V]
    right=tuple(labels[(19*i+k)%V] for i in range(V))
    return labels,right


class ExactPathPairSelector(unittest.TestCase):
    def test_all_64_four_vertex_priority_conflicts_and_target_unions(self):
        vertices=range(4)
        edges=tuple(combinations(vertices,2))
        count=0
        for mask in range(64):
            graph={x:set() for x in vertices}
            for i,(u,v) in enumerate(edges):
                if mask>>i&1:
                    graph[u].add(v);graph[v].add(u)
            for r in (1,2,3,4):
                for T in combinations(vertices,r):
                    exact=exact_source_priorities(graph,T)
                    self.assertEqual(exact,brute_priorities(graph,T))
                    self.assertGreaterEqual(exact,0)
                    count+=1
        self.assertEqual(count,64*15)

    def test_all_1024_five_coordinate_color_graphs_vs_full_assignments(self):
        vertices=range(5)
        pairs=tuple(combinations(vertices,2))
        for mask in range(1<<10):
            selected=[p for j,p in enumerate(pairs) if mask>>j&1]
            self.assertEqual(
                exact_typed_bichromatic_probability(selected),
                brute_color(selected))
        self.assertEqual(exact_typed_bichromatic_probability(()),1)
        self.assertEqual(exact_typed_bichromatic_probability(((0,1),(1,2),(0,2))),0)
        self.assertEqual(exact_typed_bichromatic_probability(((0,1),(1,2),(2,3),(0,3))),Fraction(1,8))
        self.assertEqual(exact_typed_bichromatic_probability(((0,1),(0,1))),Fraction(1,2))

    def test_actual_physical_two_paths_odd_left_triangle_negative_covariance(self):
        # Generic legal distinct source flags and globally pair-injective
        # typed maps; NO claim these three matching flags form a full GQ.
        flags=((0,0),(1,1),(2,2))
        f=((0,1),(1,2),(0,2))
        g=((0,1),(1,2),(2,3))
        graph={0:set(),1:set(),2:set()}
        P=(((0,0),(1,1),(2,2)),(0,1))
        Q=(((1,1),(2,2),(0,3)),(1,2))
        law=exact_joint_path_selector_law(graph,flags,f,g,P,Q)
        self.assertEqual(law["source_joint_priority"],1)
        self.assertEqual(law["typed_left_color_probability"],0)
        self.assertEqual(law["joint_full_path_probability"],0)
        self.assertEqual(law["individual_P_probability"],Fraction(1,16))
        self.assertEqual(law["individual_Q_probability"],Fraction(1,16))
        self.assertEqual(law["covariance"],Fraction(-1,256))
        self.assertTrue(law["negative_covariance"])

    def test_actual_physical_two_paths_source_conflict_zero_even_when_cuts_work(self):
        # TWO individually proper paths each survive with >0 probability,
        # but their union contains original-source conflicts.
        flags=((0,0),(1,1),(0,2),(1,3))
        f=((0,1),(1,2))
        g=((0,1),(1,3),(0,2),(2,3))
        conflict={0:{2},1:{3},2:{0},3:{1}}
        P=(((0,0),(1,1),(2,3)),(0,1))
        Q=(((0,0),(1,2),(2,3)),(2,3))
        law=exact_joint_path_selector_law(conflict,flags,f,g,P,Q)
        self.assertEqual(law["source_joint_priority"],0)
        self.assertGreater(law["typed_left_color_probability"],0)
        self.assertGreater(law["typed_right_color_probability"],0)
        self.assertEqual(law["joint_full_path_probability"],0)
        self.assertGreater(law["individual_P_probability"],0)
        self.assertGreater(law["individual_Q_probability"],0)
        self.assertLess(law["covariance"],0)

    def test_two_paths_same_endpoints_exact_second_moment_with_positive_coupling(self):
        flags=((0,0),(1,1),(2,2),(3,3))
        f=((0,1),(1,3),(0,2),(2,3))
        g=f
        source={i:set() for i in range(4)}
        P=(((0,0),(1,1),(3,3)),(0,1))
        Q=(((0,0),(2,2),(3,3)),(2,3))
        law=exact_joint_path_selector_law(source,flags,f,g,P,Q)
        self.assertEqual(law["individual_P_probability"],Fraction(1,16))
        self.assertEqual(law["individual_Q_probability"],Fraction(1,16))
        self.assertEqual(law["typed_left_color_probability"],Fraction(1,8))
        self.assertEqual(law["typed_right_color_probability"],Fraction(1,8))
        self.assertEqual(law["joint_full_path_probability"],Fraction(1,64))
        self.assertGreater(law["covariance"],0)
        moment=exact_same_endpoints_path_second_moment(
            source,flags,f,g,(P,Q))
        self.assertEqual(moment["exact_expected_surviving_paths"],Fraction(1,8))
        self.assertEqual(moment["exact_expected_surviving_paths_squared"],Fraction(5,32))
        self.assertEqual(moment["exact_variance"],Fraction(9,64))
        self.assertEqual(moment["ordered_positive_covariance_pairs"],4)
        self.assertTrue(moment["jensen_second_moment_valid"])

    def test_independent_end_to_end_all_source_permutations_and_both_typed_cuts(self):
        odd_flags=((0,0),(1,1),(2,2))
        odd_f=((0,1),(1,2),(0,2))
        odd_g=((0,1),(1,2),(2,3))
        odd_conflict={i:set() for i in range(3)}
        odd_p=(((0,0),(1,1),(2,2)),(0,1))
        odd_q=(((1,1),(2,2),(0,3)),(1,2))
        src_flags=((0,0),(1,1),(0,2),(1,3))
        src_f=((0,1),(1,2))
        src_g=((0,1),(1,3),(0,2),(2,3))
        src_conflict={0:{2},1:{3},2:{0},3:{1}}
        src_p=(((0,0),(1,1),(2,3)),(0,1))
        src_q=(((0,0),(1,2),(2,3)),(2,3))
        pos_flags=((0,0),(1,1),(2,2),(3,3))
        pos_f=((0,1),(1,3),(0,2),(2,3))
        pos_conflict={i:set() for i in range(4)}
        pos_p=(((0,0),(1,1),(3,3)),(0,1))
        pos_q=(((0,0),(2,2),(3,3)),(2,3))
        for graph,flags,f,g,P,Q in (
            (odd_conflict,odd_flags,odd_f,odd_g,odd_p,odd_q),
            (src_conflict,src_flags,src_f,src_g,src_p,src_q),
            (pos_conflict,pos_flags,pos_f,pos_f,pos_p,pos_q),
        ):
            with self.subTest(flags=flags):
                observed=brute_full_joint_source_and_both_colorings(
                    graph,flags,f,g,P,Q)
                calculated=exact_joint_path_selector_law(
                    graph,flags,f,g,P,Q)["joint_full_path_probability"]
                self.assertEqual(observed,calculated)
        self.assertEqual(brute_full_joint_source_and_both_colorings(
            pos_conflict,pos_flags,pos_f,pos_f,pos_p,pos_q),Fraction(1,64))

    def test_strict_shared_source_neighborhood_positive_but_no_path_assumption(self):
        graph={0:{2},1:{2},2:{0,1}}
        joint=exact_source_priorities(graph,(0,1))
        self.assertEqual(joint,Fraction(1,3))
        self.assertGreater(joint,Fraction(1,4))
        self.assertEqual(exact_source_priorities(graph,(0,2)),0)
        self.assertEqual(exact_source_priorities({0:set()},(0,)),1)

    def test_genuine_original_W32_correlated_complete_maps_r2_r3(self):
        total=0
        for k in (0,1,3):
            f,g=finite_labels(1,k)
            for r in (2,3):
                with self.subTest(k=k,r=r):
                    z=independent_genuine_source_path_pair_referee(
                        1,f,g,r=r,max_paths=25,max_pairs=15)
                    self.assertGreater(z["actual_proper_paths_sampled"],0)
                    self.assertGreaterEqual(
                        z["min_original_single_path_survival"],
                        z["single_path_sigma"])
                    self.assertEqual(z["original_paired_physical_edges"],
                                     2*z["original_core_flags"])
                    if z["same_endpoints_exact_second_moment"] is not None:
                        self.assertTrue(z["same_endpoints_exact_second_moment"]
                                        ["jensen_second_moment_valid"])
                    total+=z["actual_distinct_path_pairs_checked"]
        self.assertGreater(total,30)

    def test_genuine_original_W34_full_sparse_correlated_with_true_original_ids(self):
        _,V,flags=genuine_source(2)
        for k,core in ((0,None),
                       (7,tuple(i for i in range(len(flags)) if i%3))):
            f,g=finite_labels(2,k)
            for r in (2,3):
                with self.subTest(k=k,r=r):
                    z=independent_genuine_source_path_pair_referee(
                        2,f,g,core_ids=core,r=r,max_paths=18,max_pairs=8)
                    self.assertGreater(z["actual_proper_paths_sampled"],0)
                    self.assertGreaterEqual(z["min_original_single_path_survival"],
                                            z["single_path_sigma"])
                    self.assertTrue(
                        z["all_h_analytic_lemma_requires_the_proof_not_finite_tests"])

    def test_reject_invalid_conflicts_cut_symbols_and_path_witnesses(self):
        for g,T in (({0:{1},1:set()},(0,)),
                    ({0:{0}},(0,)),
                    ({0:set()},(1,)),
                    ({0:set()},(0,0))):
            with self.assertRaises(ValueError):
                exact_source_priorities(g,T)
        for labels in (((1,1),),((True,2),),((-1,2),),
                       ((1,),),((0,1,2),)):
            with self.assertRaises(ValueError):
                exact_typed_bichromatic_probability(labels)
        flags=((0,0),(1,1),(2,2))
        f=((0,1),(1,2),(0,2))
        g=((0,1),(1,2),(2,3))
        conflict={0:set(),1:set(),2:set()}
        P=(((0,0),(1,1),(2,2)),(0,1))
        with self.assertRaises(ValueError):
            exact_joint_path_selector_law(
                conflict,flags,f,g,(((0,0),(1,1),(2,2)),(0,0)),P)
        with self.assertRaises(ValueError):
            exact_same_endpoints_path_second_moment(
                conflict,flags,f,g,(P,P))
        with self.assertRaises(ValueError):
            exact_same_endpoints_path_second_moment(
                conflict,flags,f,g,())
        f0,g0=finite_labels(1)
        with self.assertRaises(ValueError):
            independent_genuine_source_path_pair_referee(1,f0,g0,core_ids=(0,0))
        with self.assertRaises(ValueError):
            independent_genuine_source_path_pair_referee(3,f0,g0)


if __name__=="__main__":
    unittest.main()
