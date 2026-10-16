"""Independent exact physical C6 and true-original W32 stress tests for W2-CYC."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, perm

from hyp105_issue230_d6aa4w2cyc_relative_variance import (
    relative_variance_certificate, physical_C6_containing_r_edges,
    max_fixed_edges_C6_capacity, physical_C6_in_E_edges_upper,
    original_six_line_codegree_bound,
)
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    exact_two_D6_gluing_kernel,
)
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q,
)


def independent_physical_six_cycles(a):
    """Enumerate undirected real coordinate cycles WITHOUT analytic formula."""
    answer = set()
    for order in permutations(range(a), 6):
        ed = frozenset(tuple(sorted((order[i],order[(i+1) % 6])))
                       for i in range(6))
        answer.add(ed)
    return answer


def independent_path_component_count(edges):
    vertices = {v for e in edges for v in e}
    neighbors = {v: set() for v in vertices}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    reached = set()
    c = 0
    for first in vertices:
        if first in reached:
            continue
        c += 1
        reached.add(first)
        stack = [first]
        while stack:
            for v in neighbors[stack.pop()]:
                if v not in reached:
                    reached.add(v)
                    stack.append(v)
    return c


class GenuineOriginalRelativeVarianceTests(unittest.TestCase):
    def test_01_full_physical_C6_complete_graph_independent_enumeration(self):
        for a in (6, 7, 8):
            cycles = independent_physical_six_cycles(a)
            self.assertEqual(len(cycles), perm(a,6)//12)
            reference = frozenset(tuple(sorted((i,(i+1) % 6)))
                                  for i in range(6))
            self.assertIn(reference,cycles)
            for r in range(1,6):
                for fixed in combinations(sorted(reference),r):
                    fixed = frozenset(fixed)
                    components = independent_path_component_count(fixed)
                    actual = sum(fixed <= c for c in cycles)
                    self.assertEqual(actual,
                        physical_C6_containing_r_edges(a,r,components),
                        (a,r,components,fixed))
            self.assertEqual(sum(reference<=c for c in cycles),1)

    def test_02_complete_graph_extension_extremal_path_bound_large_a(self):
        for a in (35, 36, 94, 261, 5805):
            for r in range(1,6):
                max_c = max(physical_C6_containing_r_edges(a,r,c)
                            for c in range(1,min(r,6-r)+1))
                self.assertEqual(max_fixed_edges_C6_capacity(a,r),max_c)
                self.assertEqual(max_c,perm(a-r-1,5-r))
            self.assertEqual(max_fixed_edges_C6_capacity(a,6),1)

    def test_03_independent_alternating_triple_upper_over_arbitrary_graph(self):
        for a in (6,7):
            all_cycles = independent_physical_six_cycles(a)
            all_edges = sorted(combinations(range(a),2))
            # All named C6 edge sets and several independent dense sparse samples
            samples = [set(),set(all_edges),set(next(iter(all_cycles)))]
            for i in range(1,16):
                samples.append({e for j,e in enumerate(all_edges)
                                if ((j*17+i*7) % 11)<(i%11)})
            for graph in samples:
                count = sum(c <= graph for c in all_cycles)
                self.assertLessEqual(Fraction(count),physical_C6_in_E_edges_upper(len(graph)))
        for d in (3,5,9,64,257):
            self.assertEqual(original_six_line_codegree_bound(d),103680*d**3)
            self.assertLessEqual(original_six_line_codegree_bound(d),
                                 720*physical_C6_in_E_edges_upper(6*d))

    def test_04_all_h_exact_fraction_certificate_and_analytic_s_cube(self):
        for h in range(3,23):
            s=1<<h
            z=relative_variance_certificate(s)
            eps=Fraction(z["relative_variance_over_mean_squared_exact_upper"])
            ad=Fraction(z["universal_rational_upper_a_d"])
            universal=Fraction(z["universal_rational_upper_s"])
            self.assertLessEqual(eps,ad)
            self.assertLessEqual(ad,universal)
            self.assertEqual(universal,Fraction(2333592,s**3))
            self.assertGreaterEqual(Fraction(z["mean_D6_lower"]),Fraction(s**6,8))
            self.assertEqual(len(z["r1_to_r6_codegree_upper"]),6)
            self.assertLessEqual(Fraction(z["one_global_g_positive_probability_at_least"]),1)
            self.assertFalse(z["all_f_g_minimax_seven_proved"])
            self.assertTrue(z["same_one_complete_global_g"])

    def test_05_genuine_high_probability_improves_with_s_exact(self):
        eps = {}
        for s in (8,16,32,64,128,256,512,1024):
            z = relative_variance_certificate(s)
            eps[s] = Fraction(z["relative_variance_over_mean_squared_exact_upper"])
            self.assertEqual(
                Fraction(z["one_global_g_positive_probability_at_least"]),
                1/(1+eps[s]))
            self.assertEqual(
                Fraction(z["one_global_g_at_least_s6_over16_probability_at_least"]),
                max(Fraction(),1-4*eps[s]))
        self.assertTrue(all(eps[a]>eps[b]
                            for a,b in zip(tuple(eps)[:-1],tuple(eps)[1:])))
        self.assertLess(eps[64],Fraction(1,10))
        self.assertLess(eps[128],Fraction(1,80))
        self.assertLess(eps[256],Fraction(1,700))

    def test_06_true_original_full_W32_candidate_set_source_line_codegrees(self):
        # An independent incidence-ID census on the *real* symplectic GQ.
        # h=1 is outside the asymptotic gate: only exact combinatorial
        # source-capacity controls and source-original semantics are tested.
        for scheme in ("S68","S72"):
            model,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
            self.assertEqual(len(rows),21186)
            inc=model["incidences"]
            line_sets = []
            marginal = Counter()
            for Q in rows:
                self.assertEqual(len(Q),6)
                self.assertEqual(len(set(Q)),6)
                p=[inc[i][0] for i in Q]
                l=[inc[i][1] for i in Q]
                self.assertEqual(len(set(p)),6)
                self.assertEqual(len(set(l)),6)
                f=frozenset(l)
                line_sets.append(f)
                marginal.update(f)
            self.assertEqual(sum(marginal.values()),6*21186)
            self.assertLessEqual(max(marginal.values()),
                                 3**6*max_fixed_edges_C6_capacity(6,1))
            for Q in tuple(sorted(rows))[:3]:
                L=frozenset(inc[i][1] for i in Q)
                for r in range(1,7):
                    for T in tuple(combinations(sorted(L),r))[:2]:
                        actual=sum(set(T) <= other for other in line_sets)
                        bound=(3**6*max_fixed_edges_C6_capacity(6,r) if r<6
                               else min(3**6,original_six_line_codegree_bound(3)))
                        self.assertLessEqual(actual,bound)

    def test_07_parent_all_overlap_joint_kernel_with_single_global_line_map(self):
        for s in (2,4,8,16):
            z=relative_variance_certificate(s) if s>=8 else None
            examples=(
                (0,1,2,3,4,5), (6,7,8,9,10,11),
                (0,6,7,8,9,10),(0,6,3,7,8,9),
                (0,1,2,6,7,8),(0,2,6,7,8,9),
                (0,1,2,3,5,4),
            )
            first=(0,1,2,3,4,5)
            for second in examples:
                pair=exact_two_D6_gluing_kernel(s,first,second)
                r=pair["source_line_shared_count"]
                p=Fraction(pair["one_event_true_original_D6_probability"])
                joint=Fraction(pair["joint_probability_one_complete_GLOBAL_g"])
                if r==0:
                    K=comb((z["a"] if z else (6 if s==2 else 14)),2)
                    a=z["a"] if z else (6 if s==2 else 14)
                    q=Fraction(perm(a,6),perm(K-6,6))
                elif r==6:
                    q=Fraction(1)
                else:
                    a=z["a"] if z else (6 if s==2 else 14)
                    K=comb(a,2)
                    q=min(Fraction(1),Fraction(
                        12*max_fixed_edges_C6_capacity(a,r),
                        perm(K-6,6-r)))
                self.assertLessEqual(joint,p*q,(s,r,second))


if __name__=="__main__":
    unittest.main()
