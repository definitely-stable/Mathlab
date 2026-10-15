"""Independent ALL-h TRUE ORIGINAL GQ physical anchored-source capacity tests."""
import random
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4y3_original_source_star_capacity import (
    original_parameters,
    original_single_factor_pattern_capacity,
    original_two_factors_union_capacity,
    original_swapped_source_harm_capacity,
    genuine_W32_star_oracle,
)


def independent_complete_physical_patterns(a):
    """Enumerate FULL physical K_a A/B/C 2-regular six-column patterns
    independently by actual coordinate vertices, without accessing any
    Y3 analytic anchored-source formula.
    """
    vertices=range(a)
    A=[];B=[];C=[]
    for six in combinations(vertices,6):
        edges=tuple(combinations(six,2))
        for chosen in combinations(edges,6):
            degree=Counter(x for e in chosen for x in e)
            if len(degree)==6 and all(v==2 for v in degree.values()):
                A.append(frozenset(chosen))
        for paired in combinations(edges,3):
            degree=Counter(x for e in paired for x in e)
            if len(degree)==6 and all(v==1 for v in degree.values()):
                C.append(frozenset(paired))
    for root in combinations(vertices,2):
        other=[x for x in vertices if x not in root]
        for four in combinations(other,4):
            edges=set(combinations(four,2))
            for perfect in combinations(tuple(edges),2):
                # the REMOVED physical perfect matching of a C4
                ends=Counter(x for e in perfect for x in e)
                if len(ends)!=4 or any(v!=1 for v in ends.values()):
                    continue
                B.append(frozenset((root,)) | frozenset(edges-set(perfect)))
    if len(A)!=len(set(A)) or len(B)!=len(set(B)) or len(C)!=len(set(C)):
        raise AssertionError("independent complete physical pattern repeated")
    return {"A":A,"B":B,"C":C}


class OriginalSourceStarCapacityTests(unittest.TestCase):
    def test_001_complete_Ka_independent_physical_pattern_oracle(self):
        for a in (6,7):
            physical=independent_complete_physical_patterns(a)
            for e1,e2 in (((0,1),(0,2)),((0,1),(2,3))):
                relation="adjacent" if len(set(e1)&set(e2)) else "disjoint"
                # Formulas in the all-h proof count patterns, independent
                # of s and number of original incidences.
                s=2
                single=original_single_factor_pattern_capacity(s)
                tagged=original_two_factors_union_capacity(s,relation)
                b=tagged["physical_complete_Ka_patterns_with_both_marked_edges"]
                for tag in ("A","B","C"):
                    got=sum(e1 in P and e2 in P for P in physical[tag])
                    # With a=6, all-h minimal s=2 matches literal numbers;
                    # with a=7 compare derived full-Ka expressions directly.
                    if a==6:
                        self.assertEqual(got,b[tag])
                if a==7:
                    from math import comb
                    expected={
                        "adjacent":{"A":7*comb(a-3,3),
                                    "B":(a-3)*comb(a-4,2),
                                    "C":0},
                        "disjoint":{"A":14*comb(a-4,2),
                                    "B":6*comb(a-4,2),
                                    "C":comb(a-4,2)},
                    }[relation]
                    for tag in expected:
                        actual=sum(e1 in P and e2 in P for P in physical[tag])
                        self.assertEqual(actual,expected[tag])
            self.assertEqual(
                sum((0,1) in p for p in physical["A"]),
                28*__import__("math").comb(a-2,4))

    def test_002_exact_real_W32_single_original_source_star_and_flag(self):
        result=original_single_factor_pattern_capacity(2)
        self.assertEqual((result["s"],result["d"],result["V"],result["a"],result["K"]),
                         (2,3,15,6,15))
        self.assertEqual(
            result["six_ORIGINAL_IDs_containing_fixed_source_factor_upper"],
            {"A":20412,"B_repeated_root":729,
             "B_single_on_C4":2916,"C":81})
        self.assertEqual(
            result["six_ORIGINAL_IDs_containing_fixed_actual_incidence_upper"],
            {"A":6804,"B_repeated_root":486,
             "B_single_on_C4":972,"C":54})
        self.assertEqual(result["per_source_star_upper"],24138)
        self.assertEqual(result["per_actual_original_incidence_upper"],8316)

    def test_003_exact_W32_two_affected_original_source_factor_pairs(self):
        adjacent=original_two_factors_union_capacity(2,"adjacent")
        disjoint=original_two_factors_union_capacity(2,"disjoint")
        self.assertEqual(
            adjacent["two_source_factor_original_sixsets_both_contained_full_Ka"],
            {"A":5103,"B":729,"C":0})
        self.assertEqual(
            disjoint["two_source_factor_original_sixsets_both_contained_full_Ka"],
            {"A":10206,"B":1458,"C":27})
        self.assertEqual(adjacent["two_source_factor_original_union_upper"],42444)
        self.assertEqual(disjoint["two_source_factor_original_union_upper"],36585)
        self.assertLess(disjoint["two_source_factor_original_union_upper"],
                        adjacent["two_source_factor_original_union_upper"])
        self.assertLess(adjacent["two_source_factor_original_union_upper"],2*24138)
        for a in ("adjacent","disjoint"):
            for b in ("adjacent","disjoint"):
                cap=original_swapped_source_harm_capacity(2,a,b)
                self.assertLessEqual(cap[
                    "harmful_opposite_sign_original_shared_mode_count_upper"],
                    2*42444)
                self.assertFalse(cap["root_all_map_seven_S_Omega_s6_PROVED"])

    def test_004_all_original_powers_two_finiteness_physical_modes(self):
        prev=0
        for h in range(1,15):
            s=1<<h
            x=original_single_factor_pattern_capacity(s)
            self.assertEqual(x["V"],(s+1)*(s*s+1))
            self.assertGreaterEqual(x["K"],x["V"])
            self.assertGreater(x["per_source_star_upper"],prev)
            prev=x["per_source_star_upper"]
            self.assertGreater(x["per_actual_original_incidence_upper"],0)
            for relation in ("adjacent","disjoint"):
                y=original_two_factors_union_capacity(s,relation)
                self.assertGreater(y["two_source_factor_original_union_upper"],0)
                self.assertTrue(y["strict_vs_two_independent_star_upper"])
                self.assertTrue(y["all_h_partial_injection_physical_PATTERN_UPPER"])
                self.assertFalse(y["all_h_two_sided_conflicting_mode_S_lower_PROVED"])

    def test_005_real_full_original_62370_six_ID_and_all_105_pairs(self):
        for scheme in ("S68","S72"):
            z=genuine_W32_star_oracle(scheme)
            self.assertEqual(z["s"],2)
            for tag in ("point","line"):
                q=z["per_typed_side"][tag]
                self.assertEqual(q["source_factors_checked"],15)
                self.assertEqual(q["actual_source_incidences_checked"],45)
                self.assertEqual(q["actual_source_factor_pairs_checked"],105)
                self.assertEqual(q["per_actual_source_factor_ORIGINAL_Q"],24138)
                self.assertEqual(q["per_actual_original_incidence_Q"],8316)
                self.assertEqual(q["adjacent_source_pair_ORIGINAL_Q_union"],42444)
                self.assertEqual(q["disjoint_source_pair_ORIGINAL_Q_union"],36585)
                self.assertEqual(q["pair_classes"],{"adjacent":60,"disjoint":45})

    def test_006_reject_invalid_original_orders_and_fake_geometry_types(self):
        for s in (-1,0,1,3,5,True,"8"):
            with self.assertRaises(ValueError):
                original_parameters(s)
        with self.assertRaises(ValueError):
            original_two_factors_union_capacity(2,"overlapping")
        with self.assertRaises(ValueError):
            original_swapped_source_harm_capacity(4,"same","disjoint")


if __name__=="__main__":
    unittest.main()
