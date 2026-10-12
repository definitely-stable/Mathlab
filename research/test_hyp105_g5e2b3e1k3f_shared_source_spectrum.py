"""Independent W(3,s) source spectral and shared physical-star transport tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3e_weighted_codegrees import mixed_weighted_profile
from hyp105_g5e2b3e1k3f_shared_source_spectrum import (
    _source_stars, shared_star_tail_certificate, source_star_transport,
)


def independent_source_matrix_multiply(model):
    """Slow explicit P @ ORIGINAL GQ incidence @ L^T, not K1's tensor."""
    a=model["a"]
    D=[[0]*a for _ in range(a)]
    for p,l in model["incidences"]:
        point=model["left_labels"][p]
        line=model["right_labels"][l]
        for x in point:
            for y in line:
                D[x][y]+=1
    return D


def original_point_graph_parameters(model):
    """Verify W(3,s) point-collinearity SRG parameters directly, not eigensolver."""
    s=model["s"]
    V=len(model["left_labels"])
    points_to_lines=[set() for _ in range(V)]
    for p,l in model["incidences"]:
        points_to_lines[p].add(l)
    if any(len(r)!=s+1 for r in points_to_lines):
        raise AssertionError("original source incidence degrees invalid")
    adj=[set() for _ in range(V)]
    for p,q in combinations(range(V),2):
        if points_to_lines[p]&points_to_lines[q]:
            adj[p].add(q)
            adj[q].add(p)
    expected_degree=s*(s+1)
    assert all(len(row)==expected_degree for row in adj)
    adjacent_count=nonadjacent_count=0
    for p,q in combinations(range(V),2):
        if q in adj[p]:
            adjacent_count+=1
            assert len(adj[p]&adj[q])==s-1
        else:
            nonadjacent_count+=1
            assert len(adj[p]&adj[q])==s+1
    assert adjacent_count and nonadjacent_count
    return adjacent_count,nonadjacent_count


class SharedSourceSpectralTests(unittest.TestCase):
    def test_original_gq_srg_spectrum_certificates(self):
        for h in (1,2):
            model=gq_pair_model(h,"lex")
            adjacent,nonadjacent=original_point_graph_parameters(model)
            self.assertGreater(adjacent,0)
            self.assertGreater(nonadjacent,0)

    def test_exact_source_marginals_independent_matrix_multiply(self):
        for h,scheme,seed in (
            (1,"lex",None),(1,"reverse-line",None),
            (1,"random",230),(2,"lex",None),
            (2,"random",20261011),(2,"random",230)
        ):
            model=gq_pair_model(h,scheme,seed)
            a=model["a"]
            D=independent_source_matrix_multiply(model)
            cert=source_star_transport(model)
            alpha,beta=_source_stars(model)
            self.assertEqual(cert["left_star_degrees"],alpha)
            self.assertEqual(cert["right_star_degrees"],beta)
            self.assertEqual(cert["row_marginals"],list(map(sum,D)))
            self.assertEqual(cert["column_marginals"],
                             [sum(D[x][y] for x in range(a)) for y in range(a)])
            graph=kikuchi_graph(model)
            for x in range(a):
                for y in range(a):
                    self.assertEqual(D[x][y],len(graph[x*a+y]))
            V=len(model["left_labels"])
            s=model["s"]
            error=sum((V*D[x][y]-(s+1)*alpha[x]*beta[y])**2
                      for x in range(a) for y in range(a))
            self.assertEqual(error,cert["residual_squared_numerator"])
            self.assertLessEqual(error,cert["spectral_upper_squared_numerator"])

    def test_shared_star_joint_C4_weighted_tails(self):
        for h,scheme,seed in (
            (1,"lex",None),(1,"reverse-line",None),
            (2,"lex",None),(2,"random",20261011),(2,"random",230)
        ):
            model=gq_pair_model(h,scheme,seed)
            result=shared_star_tail_certificate(model)
            weighted=mixed_weighted_profile(model)
            self.assertEqual(result["B_mixed"],weighted["B_mixed"])
            self.assertGreaterEqual(result["B_upper_K3F_joint_marginals_spectrum"],
                                    result["B_mixed"])
            self.assertFalse(result["all_h_seven_family_floor_proved"])
            graph=kikuchi_graph(model)
            a=model["a"]
            for layer in result["C4_weighted_layers"]:
                k=layer["k"]
                direct=sum(int(len(row)>=k) for row in graph)
                self.assertEqual(direct,layer["actual_high_stars"])
                self.assertLessEqual(direct,layer["combined_high_star_upper"])
                self.assertLessEqual(
                    layer["source_star_C4_weighted_tail"],
                    layer["all_h_joint_tail_upper"])
                # INDEPENDENT physical common-neighborhood C4 weight.
                brute=sum(len(graph[u]&graph[v])*(len(graph[u]&graph[v])-1)//2
                          for u in range(a*a) for v in range(u+1,a*a)
                          if u//a!=v//a and u%a!=v%a
                          and len(graph[u])>=k and len(graph[v])>=k)
                self.assertEqual(brute,layer["source_star_C4_weighted_tail"])

    def test_low_frequency_and_fail_closed_guards(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            shared_star_tail_certificate(model,max_pairs=2)
        with self.assertRaises(RuntimeError):
            shared_star_tail_certificate(model,max_c4=0)
        with self.assertRaises(ValueError):
            source_star_transport(dict(model,left_labels=((0,1),)*15))
        with self.assertRaises(ValueError):
            source_star_transport(dict(model,s=3))


if __name__=="__main__":
    unittest.main()
