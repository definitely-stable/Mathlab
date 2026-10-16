"""AA4-AR genuine original f, FIXED line physical image, ONE global permutation.

Independent all-h rational, real GQ W32/W34/W38 and physical C6
path-completion and source-line codegree falsifiers. No fake large GQ.
"""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4aq_conditional_original_D6_mean import (
    all_h_one_side_permutation_D6_theorem,
    independent_occupied_C6_cycle_census,
    true_original_six_line_SDR_count)
from hyp105_issue230_d6aa4ar_fixed_support_d6_concentration import (
    original_fixed_edges_C6_completion,
    max_true_original_source_C6_path_completion,
    genuine_original_six_line_codegree_upper,
    fixed_both_support_conditional_D6_variance_certificate)
from hyp105_issue230_d6aa4ap_unique_original_D6_path_kernel import (
    true_original_W32_all_D6_source_path_census)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def _falling_independent(n,k):
    out=1
    for j in range(k):out*=n-j
    return out


def physical_simple_six_cycles(a):
    """Independent physical cycle edge-major canonical incidence sets;
    no r,c completion formula, no variance code."""
    cycles=set()
    for vertices in permutations(range(a),6):
        cycle=tuple(sorted(tuple(sorted((vertices[j],vertices[(j+1)%6])))
                           for j in range(6)))
        cycles.add(cycle)
    return cycles


def prescribed_physical_path_components(edges):
    """Independent DFS in physical graph of r prescribed edges."""
    vertices=set(v for e in edges for v in e)
    neighbors={v:set() for v in vertices}
    for u,v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    if any(len(neighbors[v])>2 for v in vertices):
        return 0
    seen=set();c=0
    for v in vertices:
        if v in seen:continue
        c+=1;stack=[v]
        while stack:
            x=stack.pop()
            if x in seen:continue
            seen.add(x);stack.extend(neighbors[x]-seen)
    return c


def independent_original_fixed_point_cycle_source_sixsets(model,limit=10000):
    """Literal genuine 6 REAL point->6 DIFFERENT original line flag Q.

    Enumerate physically occupied ORIGINAL point C6 first, then choose
    real original GQ incident lines using recursion, never create fake
    source Q. Sample count explicit to cap test runtimes.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    cycles=independent_occupied_C6_cycle_census(f,a)
    actual=[]
    for point_ids in cycles.values():
        ps=tuple(point_ids)
        def rec(j,used,lines):
            if len(actual)>=limit:return
            if j==6:
                actual.append((ps,tuple(lines)))
                return
            for ll in np[ps[j]]:
                if ll not in used:
                    rec(j+1,used|{ll},lines+[ll])
                    if len(actual)>=limit:return
        rec(0,set(),[])
        if len(actual)>=limit:break
    return actual


def independent_physical_given_sixline_codegree(model,sixlines):
    """Genuine ORIGINAL source-line 6-codegree brute: physical C6
    on any six distinct source points, each incident to its
    prescribed six true line factors under some permutation.
    Direct physical point graph; independent of theoretical cap.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    touch=set(p for line in sixlines for p in nl[line])
    source_cycles=independent_occupied_C6_cycle_census(f,a)
    result=0
    for ps in source_cycles.values():
        if any(p not in touch for p in ps):continue
        for lineperm in permutations(sixlines):
            if all(lineperm[j] in np[ps[j]] for j in range(6)):
                result+=1
    return result


class BothSupportsFixedOriginalD6Concentration(unittest.TestCase):
    def test_01_every_dyadic_h3_to80_exact_Fraction_quenched_variance(self):
        for h in range(3,81):
            s=1<<h
            q=fixed_both_support_conditional_D6_variance_certificate(s)
            eps=q["uniform_fixed_PHYSICAL_SUPPORT_relative_variance_rational_upper"]
            self.assertGreaterEqual(eps,0)
            self.assertLessEqual(
                eps,Fraction(1331600,q["a"]**2)+Fraction(162000,q["d"]**3))
            self.assertLessEqual(eps,Fraction(827800,s**3))
            self.assertGreaterEqual(q["mean_original_D6_lower_from_AA4_AQ"],
                                    Fraction(2,3)*s**6)
            self.assertTrue(q["fixed_adversarial_original_line_physical_EDGE_IMAGE"])
            self.assertTrue(q["fixed_adversarial_point_source_map_f"])
            self.assertTrue(q["one_GLOBAL_uniform_permutation_of_ORIGINAL_line_factor_ids"])
            self.assertTrue(q["all_two_FIXED_global_factor_MAPS_D6_lower_NOT_PROVED"])
            self.assertTrue(q["root_issue230_Branch_A_B_C_OPEN"])
            self.assertGreaterEqual(
                q["Pr_one_global_assignment_D6_positive_at_least"],0)
            self.assertLessEqual(
                q["Pr_one_global_assignment_D6_positive_at_least"],1)
            self.assertLessEqual(q[
                "Pr_one_global_assignment_D6_at_least_s6_over3_at_least"],1)
        for s in (256,512,1024):
            z=fixed_both_support_conditional_D6_variance_certificate(s)
            self.assertGreater(z[
                "Pr_one_global_assignment_D6_at_least_s6_over3_at_least"],0)

    def test_02_independent_physical_K6_K7_K8_source_path_component_completion(self):
        for a in (6,7,8):
            all_cycles=physical_simple_six_cycles(a)
            total=1
            for k in range(6):total*=a-k
            self.assertEqual(len(all_cycles),total//12)
            example=next(iter(all_cycles))
            for r in range(1,6):
                M=max_true_original_source_C6_path_completion(a,r)
                sampled=list(combinations(example,r))[:7]
                for edges in sampled:
                    c=prescribed_physical_path_components(edges)
                    exact=sum(all(e in cycle for e in edges)
                              for cycle in all_cycles)
                    self.assertEqual(exact,original_fixed_edges_C6_completion(
                        a,r,c))
                    self.assertLessEqual(exact,M)

    def test_03_true_original_W32_source_sixline_codegree_samples_not_fake(self):
        for scheme in ("lex","S68","S72"):
            m=fixture(1,scheme)
            Q=independent_original_fixed_point_cycle_source_sixsets(
                m,limit=75)
            self.assertEqual(len(Q),75)
            source_sets=set(tuple(sorted(lines)) for _,lines in Q)
            for line_set in tuple(source_sets)[:5]:
                got=independent_physical_given_sixline_codegree(m,line_set)
                self.assertLessEqual(
                    got,genuine_original_six_line_codegree_upper(3))
                self.assertGreaterEqual(got,1)

    def test_04_W32_all_global_schemes_have_positive_mean_but_adverse_ZERO_D6(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            true_D6=true_original_W32_all_D6_source_path_census(
                m,historical_Q_first=True)
            self.assertEqual(true_D6["exact_D6_unique_true_original_six_Q"],0)
            mu=all_h_one_side_permutation_D6_theorem(2)
            self.assertGreater(mu[
                "any_fixed_point_global_f_and_any_fixed_line_occupied_image_expectation_lower"],0)
            # AA4-AR all-h variance theorem is explicitly h>=3.
            with self.assertRaises(ValueError):
                fixed_both_support_conditional_D6_variance_certificate(2)

    def test_05_true_original_W34_W38_fixed_physical_line_holes_source_SDR(self):
        for h,missing in ((2,6),(3,10)):
            for scheme in ("lex","random"):
                m=fixture(h,scheme)
                s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
                self.assertEqual((a*(a-1)//2-V),missing)
                self.assertEqual(len({tuple(e) for e in g}),V)
                # Actual GQ source flag injective line matching from six
                # different physical point source images, never redraw g.
                ps=tuple(range(6))
                got=true_original_six_line_SDR_count(ps,np)
                if s>=4:
                    self.assertGreaterEqual(got,d**4*(d*d-15))
                if s>=8:
                    z=fixed_both_support_conditional_D6_variance_certificate(s)
                    self.assertGreaterEqual(z["V"],V)
                    self.assertEqual(z["missing_line_physical_pair_edges"],missing)

    def test_06_source_automorphism_and_two_typed_physical_permutations_preserve_fixed_support_scope(self):
        m=zero_split_original_W32()
        z=independent_original_fixed_point_cycle_source_sixsets(m,limit=22)
        self.assertEqual(len(z),22)
        pt,ln=symplectic_transvection_source(m,1)
        a=m["a"]
        altered=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((j+2)%a for j in range(a)))
        q=independent_original_fixed_point_cycle_source_sixsets(
            altered,limit=22)
        self.assertEqual(len(q),22)
        self.assertEqual(len(set(tuple(e) for e in altered["left_labels"])),15)
        self.assertEqual(len(set(tuple(e) for e in altered["right_labels"])),15)

    def test_08_independently_partial_physical_support_exact_conditional_zero_line_overlap(self):
        # Deliberately a PHYSICAL-only independent conditional gluing
        # experiment, NOT a counterfeit finite W(3,s) source model.
        # Hold arbitrary nononto K7/K8 line physical EDGE SUPPORT
        # fixed across BOTH source-sixset events. Condition on one
        # occupied C6; remaining six original source line labels are
        # sampled uniformly from the V'-6 unused OCCUPIED edges.
        for a,holes in (
            (7,((0,1),(0,3),(1,4),(2,5))),
            (8,((0,1),(0,3),(1,4),(2,5),(3,6),(4,7)))):
            support=set(combinations(range(a),2))-set(holes)
            V=len(support)
            self.assertLess(V,a*(a-1)//2)
            self.assertGreaterEqual(V,12)
            cycles=tuple(c for c in physical_simple_six_cycles(a)
                         if all(e in support for e in c))
            C=len(cycles)
            self.assertGreater(C,0)
            # Direct independent count of ordered physical C6 pairs
            # with NO shared physical edge; this is exactly the
            # conditional r=0 gluing numerator. Do NOT invoke any
            # analytic completion formula.
            disjoint=sum(1 for first in cycles for second in cycles
                         if not(set(first)&set(second)))
            q0=Fraction(12*disjoint,C*_falling_independent(V-6,6))
            marginal=Fraction(12*C,_falling_independent(V,6))
            self.assertLessEqual(q0,
                                 Fraction(12*C,_falling_independent(V-6,6)))
            self.assertLessEqual(q0/marginal,
                                 Fraction(_falling_independent(V,6),
                                          _falling_independent(V-6,6)))
            print("AA4AR NONONTO fixed physical support",a,"occupied",V,
                  "C6",C,"two_cycle_edge_disjoint_ordered",disjoint,
                  "exact_q0_over_p",q0/marginal)

    def test_07_reject_fake_orders_and_invalid_source_global_labels(self):
        for s in (2,4,12,9):
            with self.assertRaises(ValueError):
                fixed_both_support_conditional_D6_variance_certificate(s)
        with self.assertRaises(ValueError):
            original_fixed_edges_C6_completion(6,6,1)
        with self.assertRaises(ValueError):
            max_true_original_source_C6_path_completion(7,0)
        with self.assertRaises(ValueError):
            genuine_original_six_line_codegree_upper(2)
        m=fixture(1,"lex")
        bad=dict(m,left_labels=((0,1),)*15)
        with self.assertRaises(ValueError):
            independent_original_fixed_point_cycle_source_sixsets(bad)


if __name__=="__main__":
    unittest.main()
