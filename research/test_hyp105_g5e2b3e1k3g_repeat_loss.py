"""Independent K3-G1 antipodal incidence / pencil-triangle falsifiers."""
from collections import Counter, defaultdict
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3g_repeat_loss import (
    antipodal_repeat_certificate, source_pencil_repeat_three,
    triangles_of_edges,
)


def brute_source_repeat_cycle_counts(model, *, max_cycles=150000):
    """Independent brute simple-six-cycle census from actual graph edges."""
    graph=kikuchi_graph(model)
    a=model["a"]
    column={}
    for k,(p,l) in enumerate(model["incidences"]):
        x,x1=model["left_labels"][p]
        y,y1=model["right_labels"][l]
        for u,v in ((x*a+y,x1*a+y1),(x*a+y1,x1*a+y)):
            column[frozenset((u,v))]=k
    seen=0
    hist=Counter()
    def visit(path,visited):
        nonlocal seen
        if len(path)==6:
            if path[0] in graph[path[-1]] and path[1]<path[-1]:
                seen+=1
                if seen>max_cycles:
                    raise RuntimeError("independent C6 budget exceeded")
                src=[column[frozenset((path[i],path[(i+1)%6]))]
                     for i in range(6)]
                hist[6-len(set(src))]+=1
                for c in set(src):
                    if src.count(c)>2:
                        raise AssertionError("one column uses at most 2 edges")
            return
        for w in graph[path[-1]]:
            if w>path[0] and w not in visited:
                visit(path+[w],visited|{w})
    for start in range(len(graph)):
        visit([start],{start})
    return hist


def independent_triangle_count(edges):
    graph=defaultdict(set)
    for x,y in edges:
        graph[x].add(y)
        graph[y].add(x)
    return sum(1 for x in graph for y in graph[x] if y>x
               for z in graph[x]&graph[y] if z>y)


def canonical_six_walks():
    out=[]
    def grow(seq):
        if len(seq)==6:
            if seq[-1]!=seq[0]:
                out.append(tuple(seq))
            return
        for v in range(max(seq)+2):
            if v!=seq[-1]:
                grow(seq+[v])
    grow([0])
    return out


class K3G1RepeatLossTests(unittest.TestCase):
    def test_exhaustive_two_coordinate_pattern_no_two_repeat_columns(self):
        patterns=canonical_six_walks()
        self.assertEqual(len(patterns),41)
        found=Counter()
        for x in patterns:
            for y in patterns:
                if len(set(zip(x,y)))!=6:
                    continue
                keys=[(frozenset((x[i],x[(i+1)%6])),
                       frozenset((y[i],y[(i+1)%6])))
                      for i in range(6)]
                found[6-len(set(keys))]+=1
        self.assertEqual(found,{0:879,1:48,3:2})
        self.assertEqual(found[2],0)

    def test_independent_full_cycle_census_and_product_incidence(self):
        for h,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            result=antipodal_repeat_certificate(model)
            hist=brute_source_repeat_cycle_counts(model)
            self.assertEqual(hist[2],0)
            self.assertEqual(result["C6_rep1"],hist[1])
            self.assertEqual(result["C6_rep3"],hist[3])
            self.assertEqual(result["C6_repeat_exact"],hist[1]+hist[3])
            self.assertEqual(
                result["J_repeat_column_antipodal_path_incidence"],
                hist[1]+3*hist[3])
            self.assertFalse(result["rep1_uniform_o_s6_proved"])

    def test_independent_pencil_graph_triangle_counts(self):
        for h,scheme,seed in ((1,"lex",None),(2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            left=model["left_labels"]
            right=model["right_labels"]
            seen_p=seen_l=0
            for p in range(len(left)):
                seen_p+=independent_triangle_count(
                    [right[l] for pp,l in model["incidences"] if pp==p])
            for l in range(len(right)):
                seen_l+=independent_triangle_count(
                    [left[p] for p,ll in model["incidences"] if ll==l])
            cert=source_pencil_repeat_three(model)
            self.assertEqual(cert["point_pencil_triangles"],seen_p)
            self.assertEqual(cert["line_pencil_triangles"],seen_l)
            self.assertLessEqual(cert["C6_rep3"],cert["all_h_rep3_upper"])
        self.assertEqual(triangles_of_edges([(0,1),(1,2),(0,2)]),1)
        self.assertEqual(triangles_of_edges([(0,1),(1,2)]),0)

    def test_fail_closed_budgets(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            antipodal_repeat_certificate(model,max_incidence_columns=0)
        with self.assertRaises(RuntimeError):
            antipodal_repeat_certificate(model,max_pencil_edges=2)
        with self.assertRaises(ValueError):
            antipodal_repeat_certificate(model,max_incidence_columns=True)
        with self.assertRaises(ValueError):
            triangles_of_edges([],max_edges=True)


if __name__=="__main__":
    unittest.main()
