"""Independent K3-G2 C6 same-original-source vs cross-source oracle."""
from collections import Counter, defaultdict
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3g2_source_coincidence import (
    source_coincidence_certificate, pencil_triangle_edge_profile,
)
from hyp105_g5e2b3e1k3g_repeat_loss import (
    antipodal_repeat_certificate,
)


def brute_triangles_at_edges(edges):
    """Independent direct triangle enumeration rather than degree-intersection."""
    vertices=set(x for edge in edges for x in edge)
    adjacency={frozenset(e) for e in edges}
    counter=Counter()
    triangles=0
    for x,y,z in combinations(sorted(vertices),3):
        es=(frozenset((x,y)),frozenset((y,z)),frozenset((x,z)))
        if all(e in adjacency for e in es):
            triangles+=1
            for e in es:
                counter[tuple(sorted(e))]+=1
    return triangles,counter


def fully_independent_origin_pair_census(model, *, budget=100000):
    """Brute opposite-path witnesses classified by ORIGINAL source IDs.

    Independently reconstruct which original (point,line) incidence
    contributed each Kikuchi edge. Do not call the G1 source-collision
    ledger, original weighted diagonal operator, or triangle counters.
    """
    graph=kikuchi_graph(model)
    a=model["a"]
    edge_source={}
    for p,l in model["incidences"]:
        x,xx=model["left_labels"][p]
        y,yy=model["right_labels"][l]
        for u,v in ((x*a+y,xx*a+yy),(x*a+yy,xx*a+y)):
            edge_source[frozenset((u,v))]=(p,l)
    same=cross=total=0
    for p,l in model["incidences"]:
        x,xx=model["left_labels"][p]
        y,yy=model["right_labels"][l]
        A=x*a+y
        B=xx*a+yy
        C=x*a+yy
        D=xx*a+y
        for u,v,w,z,srcidx,anchor in (
                (A,C,B,D,0,p),(A,D,B,C,1,l)):
            one=graph[u]&graph[v]
            two=graph[w]&graph[z]
            for inner in one:
                src1=edge_source[frozenset((u,inner))][srcidx]
                if src1!=edge_source[frozenset((v,inner))][srcidx]:
                    raise AssertionError("bad original source uniqueness")
                for other in two:
                    # If both 2-paths shared an internal vertex, the
                    # underlying GQ would have forbidden 4/6 incidence.
                    if inner==other:
                        raise AssertionError("forbidden common middle vertex")
                    src2=edge_source[frozenset((w,other))][srcidx]
                    if src2!=edge_source[frozenset((z,other))][srcidx]:
                        raise AssertionError("bad original dual source uniqueness")
                    total+=1
                    if total>budget:
                        raise RuntimeError("independent J witness budget exceeded")
                    if src1==src2:
                        if src1!=anchor:
                            raise AssertionError("global source injectivity broken")
                        same+=1
                    else:
                        cross+=1
    return {"J":total,"same":same,"cross":cross}


class K3G2OriginPairTests(unittest.TestCase):
    def test_arbitrary_simple_pencil_graph_edge_square_bound(self):
        for edges in (
                [],
                [(0,1),(1,2),(0,2)],
                [(0,1),(0,2),(1,2),(0,3),(1,3)],
                [(0,i) for i in range(1,20)],
                [(i,j) for i in range(7) for j in range(i+1,7)],
        ):
            exact=pencil_triangle_edge_profile(edges)
            T,counts=brute_triangles_at_edges(edges)
            self.assertEqual(exact["triangle_count"],T)
            self.assertEqual(exact["tau"],
                             {tuple(sorted(e)):counts[tuple(sorted(e))]
                              for e in edges})
            self.assertEqual(exact["sum_triangle_edge_squares"],
                             sum(v*v for v in counts.values()))
            self.assertLessEqual(exact["sum_triangle_edge_squares"],
                                 2*len(edges)**2)

    def test_whole_graph_independent_original_source_census(self):
        for h,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"lex",None),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            measured=fully_independent_origin_pair_census(model)
            certified=source_coincidence_certificate(model)
            g1=antipodal_repeat_certificate(model)
            self.assertEqual(measured["J"],certified["J_total"])
            self.assertEqual(measured["same"],certified["J_source_same"])
            self.assertEqual(measured["cross"],certified["J_cross_source"])
            self.assertEqual(certified["J_total"],g1[
                "J_repeat_column_antipodal_path_incidence"])
            self.assertEqual(
                certified["C6_rep1_local_pencil_triangle_pairs"]+
                certified["C6_rep1_cross_source"],g1["C6_rep1"])
            self.assertEqual(certified["C6_repeat_total"],g1["C6_repeat_exact"])
            self.assertLessEqual(certified["J_source_same"],
                                 certified["source_same_upper_all_h"])
            self.assertTrue(certified["source_same_uniform_o_s6"])
            self.assertFalse(certified["cross_source_uniform_o_s6_proved"])

    def test_original_pencils_independent_triangle_edge_ledger(self):
        for h,scheme,seed in ((1,"lex",None),(2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            local=triple=0
            for p in range(len(model["left_labels"])):
                ls=[l for pp,l in model["incidences"] if pp==p]
                _,tau=brute_triangles_at_edges([model["right_labels"][l]
                                                for l in ls])
                for l in ls:
                    t=tau[tuple(sorted(model["right_labels"][l]))]
                    local+=t*(t-1)
                    triple+=t
            for l in range(len(model["right_labels"])):
                ps=[p for p,ll in model["incidences"] if ll==l]
                _,tau=brute_triangles_at_edges([model["left_labels"][p]
                                                for p in ps])
                for p in ps:
                    t=tau[tuple(sorted(model["left_labels"][p]))]
                    local+=t*(t-1)
                    triple+=t
            self.assertEqual(triple%3,0)
            cert=source_coincidence_certificate(model)
            self.assertEqual(local,
                  cert["C6_rep1_local_pencil_triangle_pairs"])
            self.assertEqual(triple//3,cert["C6_rep3_pencil_triangles"])
            self.assertEqual(local+triple,cert["J_source_same"])

    def test_fail_closed(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            source_coincidence_certificate(model,max_incidence_columns=2)
        with self.assertRaises(RuntimeError):
            source_coincidence_certificate(model,max_pencil_edges=1)
        with self.assertRaises(ValueError):
            source_coincidence_certificate(model,max_incidence_columns=True)
        with self.assertRaises(ValueError):
            pencil_triangle_edge_profile([(0,1),(1,0)])
        with self.assertRaises(ValueError):
            pencil_triangle_edge_profile([(0,0)])


if __name__=="__main__":
    unittest.main()
