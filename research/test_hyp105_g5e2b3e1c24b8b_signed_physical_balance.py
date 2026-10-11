"""B8-B independent deterministic signed/source/probability falsifiers (fast CI)."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import comb, factorial, perm
import unittest

from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, original_W32,
)
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import reference_classifier
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b8a_physical_tensor import physical_factor_state
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import (
    PROFILE_A, PROFILE_B, PROFILE_C,
    SIGN_KEYS, source_signed_transitions, exact_signed_fiber_census,
    swap_orientation_sign_identity, profile_probability,
    d6_signature_probability, original_source_annealed_probability,
    exact_annealed_source_expectation,
)


def physical_templates_independent():
    """Brute physical K6 multiset enumeration, no reuse of B2 templates."""
    kinds=Counter()
    connected=[]
    for eids in combinations_with_replacement(range(15),6):
        deg=Counter(x for e in eids for x in K6_PAIRS[e])
        if len(deg)!=6 or set(deg.values())!={2}:
            continue
        multiplicity=tuple(sorted(Counter(eids).values(), reverse=True))
        kinds[multiplicity]+=1
        if multiplicity==PROFILE_A:
            edge_pairs=tuple(K6_PAIRS[e] for e in eids)
            seen={edge_pairs[0][0]}
            stack=list(seen)
            adj={i:set() for i in range(6)}
            for x,y in edge_pairs:
                adj[x].add(y)
                adj[y].add(x)
            while stack:
                for y in adj[stack.pop()]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            if len(seen)==6:
                connected.append(edge_pairs)
    return kinds, connected


def edge_maps(f, *, left):
    return {(i+1 if left else i):K6_PAIRS[k] for i,k in enumerate(f)}


class SignedPhysicalBalanceTests(unittest.TestCase):
    def test_exact_A_B_C_template_counts_and_marginal_laws(self):
        kinds, connected=physical_templates_independent()
        self.assertEqual(kinds,Counter({PROFILE_A:70,PROFILE_B:45,PROFILE_C:15}))
        self.assertEqual(len(connected),60)
        for a in (6,7,10):
            m=comb(a,2)
            c=comb(a,6)
            # Independently weight templates by number of valid distinct
            # ordered original-vertex-to-edge assignments.
            self.assertEqual(profile_probability(a,PROFILE_A),
                             Fraction(c*kinds[PROFILE_A]*factorial(6),perm(m,6)))
            self.assertEqual(profile_probability(a,PROFILE_B),
                             Fraction(c*kinds[PROFILE_B]*factorial(4),perm(m,5)))
            self.assertEqual(profile_probability(a,PROFILE_C),
                             Fraction(c*kinds[PROFILE_C]*factorial(3),perm(m,3)))
            self.assertEqual(d6_signature_probability(a),
                             Fraction(c*factorial(6),perm(m,6)))
        with self.assertRaises(ValueError):
            profile_probability(5,PROFILE_A)
        with self.assertRaises(ValueError):
            profile_probability(True,PROFILE_C)
        with self.assertRaises(ValueError):
            d6_signature_probability(5)

    def test_each_connected_D6_cycle_signature_has_exactly_720_maps_for_a6(self):
        _, connected=physical_templates_independent()
        cycle_counts=Counter()
        six=tuple((i,i+20) for i in range(6))
        for pattern in connected:
            for edges in permutations(pattern):
                mapping=dict(enumerate(edges))
                accepted,sig=physical_factor_state(six,mapping,left=True)
                self.assertTrue(accepted)
                self.assertIsNotNone(sig)
                cycle_counts[sig]+=1
        self.assertEqual(len(cycle_counts),60)
        self.assertEqual(set(cycle_counts.values()),{720})
        self.assertEqual(sum(cycle_counts.values()),60*720)

    def test_true_original_W32_small_source_four_map_signed_referee(self):
        _,lines,_=original_W32()
        universe=tuple(sorted((p,l) for l,group in enumerate(lines) for p in group))
        sample=universe[:10]+universe[20:24]
        src=tuple(combinations(sample,6))
        self.assertEqual(len(src),3003)
        f0,g0=tuple(W32_LEFT_H45),tuple(W32_RIGHT_S68)
        f1,g1=legal_transpose(f0,3,8),legal_transpose(g0,0,14)
        maps=(edge_maps(f0,left=True),edge_maps(f1,left=True),
              edge_maps(g0,left=False),edge_maps(g1,left=False))
        result=exact_signed_fiber_census(src,*maps)
        self.assertEqual(result["kappa"],result["positive_matched"]-result["negative_matched"])
        self.assertLessEqual(result["absolute_matched"],result["physical_change_cap"])
        self.assertEqual(sum(v["signed"] for v in result["by_tag"].values()),result["kappa"])
        self.assertEqual(result["net_cancellation"],
                         result["absolute_matched"]-abs(result["kappa"]))
        for six in src:
            x=source_signed_transitions(six,*maps)
            direct=tuple(int(reference_classifier(six,f,g) is not None)
                         for f,g in ((f0,g0),(f1,g0),(f0,g1),(f1,g1)))
            if x is None:
                self.assertEqual(direct,(0,0,0,0))
            else:
                self.assertEqual(x["four_scores"],direct)
                self.assertEqual(x["mixed"],direct[3]-direct[1]-direct[2]+direct[0])
                self.assertEqual(x["positive"]+x["negative"],
                                 sum(x["quadrants"].values()))
        signs=swap_orientation_sign_identity(f0,f1,g0,g1,result["four_scores"])
        self.assertEqual((signs["left_reversed"],signs["right_reversed"]),
                         (-result["kappa"],-result["kappa"]))
        self.assertEqual(signs["uniform_complete_right_orbit_signed_mean"],Fraction(0))
        with self.assertRaises(ValueError):
            exact_signed_fiber_census(src+src[:1],*maps)

    def test_D6_can_have_two_same_sign_matched_transitions(self):
        six=tuple((i,i+20) for i in range(6))
        edges=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        l0=dict(enumerate(edges))
        l1=l0.copy()
        l1[0],l1[2]=l1[2],l1[0]
        r0={i+20:x for i,x in enumerate(edges)}
        r1=r0.copy()
        r1[20],r1[22]=r1[22],r1[20]
        row=source_signed_transitions(six,l0,l1,r0,r1)
        self.assertEqual(row["tag"],"D6")
        self.assertEqual(row["four_scores"],(1,0,0,1))
        self.assertEqual((row["mixed"],row["positive"],row["negative"]), (2,2,0))
        self.assertEqual((row["quadrants"]["gain_gain"],row["quadrants"]["loss_loss"]),(1,1))
        self.assertEqual(row["physical_cap"],2)
        backward=source_signed_transitions(six,l0,l1,r1,r0)
        self.assertEqual((backward["mixed"],backward["positive"],backward["negative"]),
                         (-2,0,2))

    def test_all_seven_source_annealed_probabilities_are_exact_and_rational(self):
        examples=(
            ((0,10),(1,11),(2,12),(3,13),(4,14),(5,15)),
            ((0,10),(0,11),(1,12),(2,13),(3,14),(4,15)),
            ((0,10),(1,10),(2,11),(3,12),(4,13),(5,14)),
            ((0,10),(0,11),(1,12),(1,13),(2,14),(2,15)),
            ((0,10),(0,11),(1,10),(1,12),(2,13),(2,14)),
            ((0,10),(0,11),(1,10),(2,12),(3,13),(4,14)),
            ((0,10),(0,11),(1,12),(2,12),(3,13),(4,14)),
        )
        for a in (6,9):
            expectation=exact_annealed_source_expectation(examples,a)
            independent=sum((original_source_annealed_probability(x,a) for x in examples),Fraction(0))
            self.assertEqual(expectation["expected_S"],independent)
            self.assertGreater(expectation["expected_S"],0)
            self.assertLess(expectation["expected_S"],len(examples))
            self.assertTrue(expectation["no_minimum_or_concentration_claim"])
            self.assertEqual(original_source_annealed_probability(examples[0],a),
                             60*d6_signature_probability(a)**2)
        self.assertEqual(original_source_annealed_probability(
            ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5)),6),Fraction(0))


if __name__=="__main__":
    unittest.main()
