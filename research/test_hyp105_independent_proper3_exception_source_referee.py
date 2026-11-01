"""AA4-P3EXC independent 64-condition exact P3 and original BBo pathway review."""
from itertools import combinations
from fractions import Fraction
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_independent_proper3_exception_source_referee import (
    _three_walk_source_free,_three_walk_endpoint_tensor,_two_walk_books,
    _inclusion_exclusion_64,_validate_pair_labels,
    exact_original_proper3_exceptional_referee,
)


def source_labels(power,offset=0):
    _,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    labels=tuple(combinations(range(a),2))[:V]
    g=tuple(labels[(i+offset)%V] for i in range(V))
    return labels,g


def graph_from_physical_mask(a,mask):
    g={(x,y):set() for x in range(a) for y in range(a)}
    pairs=[]
    for x in range(a):
        for z in range(x+1,a):
            for y in range(a):
                for w in range(y+1,a):
                    pairs.extend(( ((x,y),(z,w)), ((x,w),(z,y)) ))
    for j,(u,v) in enumerate(pairs):
        if mask>>j&1:
            g[u].add(v);g[v].add(u)
    return g,len(pairs)


class IndependentProper3Exceptions(unittest.TestCase):
    def test_exact_six_bad_events_on_all_sixty_four_two_by_three_grid_graphs(self):
        # rectangular grid x=2, y=3, 6 actual opposite-corner edges
        vertices=tuple((x,y) for x in range(2) for y in range(3))
        edges=[]
        for y in range(3):
            for z in range(y+1,3):
                edges.extend((((0,y),(1,z)),((0,z),(1,y))))
        self.assertEqual(len(edges),6)
        for mask in range(64):
            g={v:set() for v in vertices}
            for i,(u,v) in enumerate(edges):
                if mask>>i&1:g[u].add(v);g[v].add(u)
            w,b,h,p=_three_walk_source_free(g)
            tensor=_three_walk_endpoint_tensor(g)
            self.assertEqual(p,tensor)
            ie=_inclusion_exclusion_64(h)
            self.assertEqual(ie["proper_inclusion_exclusion"],sum(p.values()))
            self.assertEqual(ie["improper_inclusion_exclusion"],b)
            self.assertEqual(sum(h.values()),w)
            two=_two_walk_books(g)
            self.assertLessEqual(b,2*two["max_degree"]*two["B2"]
                                 +two["max_degree"]*(two["Qx"]+two["Qy"]))
            self.assertGreaterEqual(Fraction(w),Fraction((2*two["edges"])**3,6**2))

    def test_4096_all_two_by_four_physical_opposite_corner_edge_graphs(self):
        vertices=tuple((x,y) for x in range(2) for y in range(4))
        edges=[]
        for y in range(4):
            for z in range(y+1,4):
                edges.extend((((0,y),(1,z)),((0,z),(1,y))))
        self.assertEqual(len(edges),12)
        for mask in range(4096):
            g={v:set() for v in vertices}
            for i,(u,v) in enumerate(edges):
                if mask>>i&1:g[u].add(v);g[v].add(u)
            w,b,h,p=_three_walk_source_free(g)
            self.assertEqual(p,_three_walk_endpoint_tensor(g))
            ie=_inclusion_exclusion_64(h)
            self.assertEqual(ie["proper_inclusion_exclusion"],sum(p.values()))
            self.assertEqual(ie["improper_inclusion_exclusion"],b)
            self.assertEqual(w-b,sum(p.values()))

    def test_direct_proper_diagonal_chain_and_empty_physical_graph(self):
        vertices=tuple((i,i) for i in range(4))
        g={v:set() for v in vertices}
        for u,v in zip(vertices,vertices[1:]):
            g[u].add(v);g[v].add(u)
        w,b,h,p=_three_walk_source_free(g)
        self.assertEqual(p,_three_walk_endpoint_tensor(g))
        self.assertGreaterEqual(p[vertices[0],vertices[-1]],1)
        self.assertGreater(b,0)
        self.assertEqual(_inclusion_exclusion_64(h)["proper_inclusion_exclusion"],sum(p.values()))
        empty={v:set() for v in vertices}
        self.assertEqual(_three_walk_source_free(empty)[0],0)
        self.assertFalse(_three_walk_endpoint_tensor(empty))

    def test_true_W32_all_full_map_original_endpoint_classes_and_BBo_two_to_one(self):
        _,V,flags=genuine_source(1)
        for k in (0,1,3,7,11):
            f,g=source_labels(1,k)
            z=exact_original_proper3_exceptional_referee(1,f,g)
            self.assertEqual(z["physical_core_edges"],2*len(flags))
            self.assertTrue(z["independent_endpoint_tensor_equal_forward_walk"])
            self.assertTrue(z["original_sixID_path_bookkeeping_exact"])
            self.assertEqual(z["exceptional_endpoint_count"],
                             sum(z["full_original_four_class_endpoint_counts"][x]
                                 for x in ("missing","incident","bad")))
            self.assertEqual(z["original_BBo_image"]["unblocked_original_paths"],
                             2*z["original_BBo_image"]["produced_original_BBo_sixsets"])
            self.assertEqual(z["original_BBo_image"]["directed_paths_per_original_sixset"],
                             (2,) if z["original_BBo_image"]["unblocked_original_paths"] else ())

    def test_true_W32_original_sparse_core_and_anchor_outside_core(self):
        _,_,flags=genuine_source(1)
        f,g=source_labels(1,1)
        for core in ((),tuple(range(0,len(flags),2)),
                     tuple(i for i in range(len(flags)) if i%4==0),
                     tuple(i for i in range(len(flags)) if i%5)):
            z=exact_original_proper3_exceptional_referee(1,f,g,core)
            self.assertEqual(z["original_core_flag_count"],len(core))
            self.assertEqual(z["physical_core_edges"],2*len(core))
            self.assertEqual(z["two_walk_full_books"]["B2"],
                4*len(core)+4*(z["original_core_Mf"]+z["original_core_Mg"]))
            self.assertLessEqual(z["exceptional_endpoint_proper_mass"]**2,
                                 z["exceptional_adaptive_cauchy_upper_squared"])

    def test_true_W34_original_full_and_sparse_correlated_g(self):
        s,V,flags=genuine_source(2)
        for k,core in ((0,None),(17,tuple(i for i in range(len(flags)) if i%3==0))):
            f,g=source_labels(2,k)
            z=exact_original_proper3_exceptional_referee(2,f,g,core)
            self.assertTrue(z["original_sixID_path_bookkeeping_exact"])
            self.assertEqual(z["all_directed_three_walks"],
                             z["proper_directed_three_walks"]+
                             z["improper_directed_three_walks"])
            self.assertEqual(z["physical_core_edges"],2*z["original_core_flag_count"])
            self.assertLessEqual(z["exceptional_endpoint_proper_mass"]**2,
                                 z["exceptional_adaptive_cauchy_upper_squared"])
            self.assertEqual(z["original_BBo_image"]["unblocked_original_paths"],
                             2*z["original_BBo_image"]["produced_original_BBo_sixsets"])

    def test_true_W34_protected_K44_original_sparse_source(self):
        f,g,ids=planted_original_k44()
        z=exact_original_proper3_exceptional_referee(2,f,g,ids)
        self.assertEqual(z["original_core_flag_count"],16)
        self.assertEqual(z["physical_core_edges"],32)
        self.assertTrue(z["original_sixID_path_bookkeeping_exact"])

    def test_fail_closed_duplicate_illegal_noncomplete_source_maps(self):
        f,g=source_labels(1)
        _,_,flags=genuine_source(1)
        for bad in (0,3,-1,1.0,True):
            with self.assertRaises(ValueError):
                exact_original_proper3_exceptional_referee(bad,f,g)
        with self.assertRaises(ValueError):
            exact_original_proper3_exceptional_referee(1,f[:-1],g)
        with self.assertRaises(ValueError):
            exact_original_proper3_exceptional_referee(1,(f[0],)*len(f),g)
        with self.assertRaises(ValueError):
            exact_original_proper3_exceptional_referee(1,f,g,(0,0))
        with self.assertRaises(ValueError):
            exact_original_proper3_exceptional_referee(1,f,g,(True,))
        with self.assertRaises(ValueError):
            exact_original_proper3_exceptional_referee(1,f,g,(len(flags),))


if __name__=="__main__":
    unittest.main()
