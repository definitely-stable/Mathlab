"""Independent tests for AA4-BA2 exact all-h ORIGINAL B/A pair probabilities."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import json
import unittest

from hyp105_allh_BA_overlap_second_moment import (
    K6_overlap_vertex_templates,
    conditional_right_A_pair_probabilities,
    exact_BA_second_moment_from_masks,
    factor_components,
    genuine_W32_left_B_source_masks,
    independent_small_frozen_pair_kernel,
    source_support_overlap_pairs,
    twofactors_on_six,
    unrestricted_twofactor_pair_intersection_counts,
    certified_true_W32_BA_pair_moment,
)
from hyp105_allh_annealed_BA_floor import exact_twofactor_count, falling


def independent_2factors(a, forbidden=()):
    """Standalone degree-2 incidence-count brute physical graph oracle."""
    result=set()
    forbidden=set(forbidden)
    for six in combinations(range(a),6):
        edges=list(combinations(six,2))
        for subset in combinations(edges,6):
            deg={z:0 for z in six}
            for u,v in subset:
                deg[u]+=1;deg[v]+=1
            if any(z!=2 for z in deg.values()):
                continue
            if any(e in forbidden for e in subset):
                continue
            result.add(frozenset(subset))
    return result


def independent_pair_counts(factors):
    """Independent unordered-pair plus diagonal identity, no template use."""
    V=list(factors)
    result=[0]*7
    for i,x in enumerate(V):
        result[6]+=1
        for y in V[i+1:]:
            result[len(x&y)]+=2
    return tuple(result)


class TestAllHOriginalBAOverlapSecondMoment(unittest.TestCase):
    def test_60_connected_and_ten_two_triangles(self):
        factors=twofactors_on_six(tuple(range(6)))
        kinds=Counter(factor_components(x) for x in factors)
        self.assertEqual(kinds,{(6,):60,(3,3):10})
        t=K6_overlap_vertex_templates()
        self.assertEqual(set(t),{(6,),(3,3)})
        for kind,rows in t.items():
            for k in range(7):
                self.assertEqual(sum(rows[k]),70*comb(6,k))
        self.assertTrue(all(len(row)==7 for rows in t.values() for row in rows))

    def test_all_a_overlap_polynomial_against_independent_direct_K6_K7_K8(self):
        for a in (6,7,8):
            with self.subTest(a=a):
                original=independent_2factors(a)
                self.assertEqual(len(original),70*comb(a,6))
                N=independent_pair_counts(original)
                exact=unrestricted_twofactor_pair_intersection_counts(a)
                self.assertEqual(N,exact)
                self.assertEqual(sum(exact),len(original)**2)
                self.assertEqual(exact[6],len(original))
                self.assertEqual(exact[5],0)
                probs=conditional_right_A_pair_probabilities(a)
                self.assertEqual(probs[6],Fraction(
                    70*comb(a,6)*720,falling(comb(a,2),6)))
                for r,x in enumerate(probs):
                    self.assertEqual(x,Fraction(
                        exact[r]*factorial(r)*factorial(6-r)**2,
                        falling(comb(a,2),12-r)))
                    self.assertGreaterEqual(x,0)
                    self.assertLessEqual(x,1)

    def test_frozen_right_images_arbitrary_K6_K7_independent_direct(self):
        for a,F in ((6,()),(6,((0,1),)),(6,((0,1),(2,3))),
                    (7,((0,1),)),(7,((0,1),(2,3)))):
            with self.subTest(a=a, F=F):
                L=independent_2factors(a,F)
                self.assertEqual(
                    len(L),
                    exact_twofactor_count(a,F)["allowed_2factor_edge_sets"])
                exact=independent_small_frozen_pair_kernel(a,F)
                self.assertEqual(exact,independent_pair_counts(L))
                M=comb(a,2)-len(F)
                p=conditional_right_A_pair_probabilities(a,F)
                for r,n in enumerate(exact):
                    self.assertEqual(p[r],Fraction(
                        n*factorial(r)*factorial(6-r)**2,
                        falling(M,12-r)))
                self.assertEqual(p[6],Fraction(720*len(L),falling(M,6)))
        with self.assertRaises(ValueError):
            conditional_right_A_pair_probabilities(8,((0,1),))
        with self.assertRaises(ValueError):
            conditional_right_A_pair_probabilities(6,((0,1),(0,1)))
        with self.assertRaises(ValueError):
            conditional_right_A_pair_probabilities(6,((0,7),))

    def test_original_W32_distinct_source_line_support_and_pair_moments(self):
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                m,masks=genuine_W32_left_B_source_masks(scheme)
                self.assertTrue(len(masks)>0)
                self.assertTrue(all(x.bit_count()==6 for x in masks))
                self.assertEqual(m["v"],15)
                overlaps=source_support_overlap_pairs(masks,15)
                self.assertEqual(sum(overlaps),len(masks)**2)
                self.assertGreater(overlaps[6],len(masks))
                # Original history's independent left-B generator is
                # source-ID unique, but distinct ORIGINAL sixsets
                # can have the SAME six right source line IDs.
                q=certified_true_W32_BA_pair_moment(scheme)
                self.assertEqual(
                    q["source_left_B_original_sixsets_with_six_distinct_lines"],
                    len(masks))
                self.assertEqual(
                    q["original_ordered_sixset_pairs_by_common_source_lines"],
                    overlaps)
                self.assertGreater(q["E_original_BA"],0)
                self.assertGreater(q["E_original_BA_squared"],
                                   q["E_original_BA"]**2)
                self.assertGreater(
                    q["Paley_Zygmund_probability_original_BA_positive_lower"],0)
                self.assertLessEqual(
                    q["Paley_Zygmund_probability_original_BA_positive_lower"],1)
                self.assertFalse(q["adversarial_all_g_lower_proved"])

    def test_true_W32_one_frozen_original_line_conditioned_second_moment(self):
        m,masks=genuine_W32_left_B_source_masks("lex",(0,))
        q=certified_true_W32_BA_pair_moment("lex",(0,))
        self.assertEqual(q["frozen_original_source_line_ids"],(0,))
        self.assertEqual(q["frozen_physical_right_pairs"],
                         (m["right_labels"][0],))
        self.assertEqual(len(masks),
                         q["source_left_B_original_sixsets_with_six_distinct_lines"])
        self.assertGreater(q["E_original_BA"],0)
        self.assertGreaterEqual(q["variance_original_BA"],0)
        self.assertNotEqual(
            q["right_A_pair_joint_probabilities_by_source_line_overlap"],
            conditional_right_A_pair_probabilities(6))
        self.assertLess(
            len(masks), len(genuine_W32_left_B_source_masks("lex")[1]))

    def test_invalid_source_support_fail_closed(self):
        with self.assertRaises(ValueError):
            source_support_overlap_pairs([0b11111],15)
        with self.assertRaises(ValueError):
            source_support_overlap_pairs([0b111111<<15],15)
        with self.assertRaises(ValueError):
            source_support_overlap_pairs([True],15)
        with self.assertRaises(ValueError):
            twofactors_on_six([0,1,2,3,4,4])
        with self.assertRaises(ValueError):
            unrestricted_twofactor_pair_intersection_counts(5)

    def test_machine_readable_original_W32_second_moment_certificate(self):
        cases={}
        for label,J in (("lex",()),("reverse-line",()),
                        ("lex-one-frozen",(0,))):
            scheme="lex" if label=="lex-one-frozen" else label
            x=certified_true_W32_BA_pair_moment(scheme,J)
            cases[label]={
                "original_B_sixsets":x[
                    "source_left_B_original_sixsets_with_six_distinct_lines"],
                "source_ordered_pair_counts_r0_to_r6":x[
                    "original_ordered_sixset_pairs_by_common_source_lines"],
                "right_factor_pair_counts_r0_to_r6":x[
                    "right_physical_twofactor_pair_counts_by_common_edges"],
                "expected_accepted_original_BA":str(x["E_original_BA"]),
                "expected_original_BA_squared":str(x["E_original_BA_squared"]),
                "variance":str(x["variance_original_BA"]),
                "paley_zygmund_P_BA_positive_floor":str(
                    x["Paley_Zygmund_probability_original_BA_positive_lower"]),
            }
        print("HYP105_AA4_BA2_CERTIFICATE="+json.dumps({
            "scope":"true W32 f fixed, globally injected one g, source-ID exact",
            "all_h_unrestricted_P_r_polynomial_valid":True,
            "not_all_completed_g":True,
            "root_A_B_C_proved":False,
            "cases":cases,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
