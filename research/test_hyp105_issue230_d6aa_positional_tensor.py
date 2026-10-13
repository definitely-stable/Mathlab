"""Independent regressions for HYP-105 #230 D6-AA1–AA3."""
import unittest
from collections import Counter
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_d6aa_positional_tensor import (
    WEIGHTS, POSITION_PAIRS, classify_original_six, classify_position_signatures,
    enumerate_position_graphs, joint_moment_sum, local_signature,
    original_W32_census, source_degree_moments, report)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6z_original_incidence_wedge_moment import (
    validated_original_regular_model)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_independent import (
    F0, G68, G72, geometry, lift_census)


def elementary_moment(six_edges, labels, side, k):
    d = Counter(coord for point, line in six_edges
                for coord in labels[(point, line)[side]])
    return sum(comb(n, k) for n in d.values() if n >= k)


class D6AAPositionalTests(unittest.TestCase):
    def test_all_130_independently_enumerated_multigraphs(self):
        self.assertEqual(enumerate_position_graphs(),
            {"A_C6":60, "A_C3_plus_C3":10, "B":45, "C":15,
             "total":130})
        # Concrete realizations of A6, A(3+3), B(4+2), C(2+2+2).
        cases = (
            (((0,1),(1,2),(2,3),(3,4),(4,5),(0,5)), "A",True),
            (((0,1),(1,2),(0,2),(3,4),(4,5),(3,5)), "A",False),
            (((0,1),(0,1),(2,3),(3,4),(4,5),(2,5)), "B",False),
            (((0,1),(0,1),(2,3),(2,3),(4,5),(4,5)), "C",False),
        )
        for pairs, kind, connected in cases:
            sig=local_signature(pairs)
            self.assertTrue(sig["regular"])
            self.assertEqual(sig["kind"],kind)
            self.assertEqual(sig["connected"],connected)
            self.assertEqual(sig["W2"],6)
            self.assertEqual(sig["W3"],0)
            self.assertEqual(len(sig["position_graph"]),6)

    def test_whitney_K3_vs_K13_pair_intersection_falsifier(self):
        triangles=((0,1),(0,2),(1,2),(3,4),(3,5),(4,5))
        stars=((0,1),(0,2),(0,3),(4,5),(4,6),(4,7))
        a,b=local_signature(triangles),local_signature(stars)
        self.assertEqual(a["pair_intersections"],b["pair_intersections"])
        self.assertEqual((a["W2"],b["W2"]),(6,6))
        self.assertEqual((a["W3"],b["W3"]),(0,2))
        self.assertTrue(a["regular"])
        self.assertFalse(b["regular"])
        self.assertIsNone(classify_position_signatures(a,b))

    def test_uniform_permutation_of_six_original_incidence_positions(self):
        left=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        right=left
        first=classify_position_signatures(local_signature(left),
                                           local_signature(right))
        self.assertEqual(first,"D6")
        # All 720 simultaneous permutations, no source column identity lost.
        for permutation in permutations(range(6)):
            self.assertEqual(classify_position_signatures(
                local_signature(tuple(left[i] for i in permutation)),
                local_signature(tuple(right[i] for i in permutation))),first)
        # Nonaligned A/A 6-cycles are *not* D6.
        shifted=((0,1),(1,2),(2,3),(3,5),(4,5),(0,4))
        self.assertIsNone(classify_position_signatures(
            local_signature(left),local_signature(shifted)))

    def test_six_position_BB_intersection_and_fake_C_C(self):
        b0=((0,1),(0,1),(2,3),(3,4),(4,5),(2,5))
        bdisjoint=((0,2),(2,3),(0,3),(4,5),(4,5),(1,2))
        # Construct B/B directly from positional multigraphs so double
        # positions are controlled by design; physical labels arbitrary.
        def realize(edges):
            return tuple(tuple(i for i,edge in enumerate(edges) if v in edge)
                         for v in range(6))
        # Two B graph patterns with doubled edges on (0,1), (1,2), (2,3).
        original=local_signature(b0)
        self.assertEqual(original["doubled_positions"],((0,1),))
        for double_edge, overlap in (((0,1),2),((1,2),1),((2,3),0)):
            rest=tuple(i for i in range(6) if i not in double_edge)
            four=((10,11),(11,12),(12,13),(10,13))
            pairs=[None]*6
            pairs[double_edge[0]]=pairs[double_edge[1]]=(8,9)
            for idx,pair in zip(rest,four):
                pairs[idx]=pair
            rhs=local_signature(pairs)
            self.assertEqual(rhs["kind"],"B")
            tag=classify_position_signatures(original,rhs)
            if overlap==2:
                self.assertIsNone(tag)  # Duplicate ORIGINAL (p,l) row.
            else:
                self.assertEqual(tag,
                    "B/B-overlap" if overlap==1 else "B/B-disjoint")
        c=((0,1),(0,1),(2,3),(2,3),(4,5),(4,5))
        self.assertIsNone(classify_position_signatures(
            local_signature(c),local_signature(c)))

    def test_all_W32_candidates_against_two_independent_references(self):
        self.assertEqual(WEIGHTS,R3_CERTIFIED_FLOORS)
        for scheme,wanted in (("S68",68),("S72",72)):
            m=fixture(1,scheme)
            p,L,R,E=validated_original_regular_model(m)
            independent_counts=Counter()
            rejected=0
            for ids,_ in selected_left_six(m):
                six=tuple(E[i] for i in ids)
                actual=classify_original_six(six,L,R)
                expected=classify_seven_prechecked(ids,L,R,E)
                self.assertEqual(actual,expected)
                if actual:
                    independent_counts[actual]+=1
                else:
                    rejected+=1
            self.assertEqual(rejected+sum(independent_counts.values()),62370)
            self.assertEqual(sum(independent_counts.values()),wanted)
            baseline=seven_census(m,independent_checks=False)
            self.assertEqual(dict(independent_counts),
                             {k:v for k,v in baseline[
                                 "seven_class_motif_counts"].items() if v})
            self.assertEqual(sum(independent_counts[k]*v
                             for k,v in WEIGHTS.items()),
                             baseline["GF5_seven_lower_numerator"])
            self.assertEqual(original_W32_census(m)["by_class"],
                             dict(independent_counts))

        # Third oracle uses its OWN symplectic W32 construction and
        # physical pair templates, not the selected_left_six enumerator.
        _, _, own_inc=geometry()
        for g,target in ((G68,68),(G72,72)):
            _, counts, _=lift_census(F0,g,own_inc)
            self.assertEqual(sum(counts.values()),target)

    def test_all_orders_one_side_global_moment_identity(self):
        for power in (1,2):
            model=fixture(power,"lex")
            _,L,R,E=validated_original_regular_model(model)
            delta=model["s"]+1
            N=len(E)
            for side,labels in ((0,L),(1,R)):
                expected={}
                count=Counter(coord for p,l in E
                    for coord in labels[(p,l)[side]])
                for k in range(1,7):
                    expected[k]=comb(N-k,6-k)*sum(
                        comb(v,k) for v in count.values() if v>=k)
                self.assertEqual(source_degree_moments(
                    model["s"],labels),expected)

        # Independent brute expansion over ALL 28 sixsets on eight
        # ORIGINAL positions: checks every k=1..6 (not just k<=3).
        E=((0,0),(0,1),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3))
        L=((0,1),(0,2),(1,2),(2,3))
        R=((0,2),(0,3),(1,3),(1,2))
        for side,labels in ((0,L),(1,R)):
            deg=Counter(coord for e in E
                for coord in labels[e[side]])
            for k in range(1,7):
                direct=sum(elementary_moment(six,labels,side,k)
                           for six in combinations(E,6))
                formula=comb(len(E)-k,6-k)*sum(
                    comb(n,k) for n in deg.values() if n>=k)
                self.assertEqual(direct,formula)

    def test_joint_moment_algebra_covers_overlap_and_source_geometry(self):
        E=((0,0),(0,1),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3))
        L=((0,1),(0,2),(1,2),(2,3))
        R=((0,2),(0,3),(1,3),(1,2))
        for r in range(1,7):
            for t in range(1,7):
                direct=sum(elementary_moment(six,L,0,r)
                           *elementary_moment(six,R,1,t)
                           for six in combinations(E,6))
                result=joint_moment_sum(E,L,R,r,t)
                self.assertEqual(result["total"],direct)
                self.assertEqual(sum(result["by_overlap"].values()),direct)
        # In the real GQ, joint counts depend on original geometry.
        m=fixture(1,"S68")
        z=joint_moment_sum(m["incidences"],m["left_labels"],
                           m["right_labels"],2,2)
        self.assertGreater(z["total"],0)
        self.assertEqual(set(z["by_overlap"]),{0,1,2})

    def test_malformed_input_and_scope(self):
        with self.assertRaises(ValueError):
            local_signature(((0,1),)*5)
        with self.assertRaises(ValueError):
            local_signature(((0,0),)*6)
        with self.assertRaises(ValueError):
            classify_original_six(((0,0),)*6,((0,1),),((2,3),))
        with self.assertRaises(ValueError):
            source_degree_moments(2, ((0,1),)*15)
        with self.assertRaises(ValueError):
            joint_moment_sum(((0,0),)*6,((0,1),),((2,3),),2,2)

    def test_machine_readable_claim_scope(self):
        result=report()
        self.assertEqual(result["slice"],"HYP105-ISSUE230-D6-AA1-AA3")
        self.assertEqual(result["position_graph_census"]["total"],130)
        self.assertEqual([r["S_seven"] for r in result["original_W32"]],
                         [68,72])
        self.assertTrue(result["all_h_local_exact_Phi"])
        self.assertFalse(result["full_GF5_R3"])
        self.assertFalse(result["all_h_positive_S_lower"])
        self.assertEqual((result["Branch_A"],result["Branch_B"]),
                         ("OPEN","OPEN"))


if __name__ == "__main__":
    unittest.main()
