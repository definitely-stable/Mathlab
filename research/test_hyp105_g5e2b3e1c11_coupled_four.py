"""Independent C11 one-global-prefix moment and true W32 four-line falsifiers."""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import unittest

from hyp105_g5e2b3e1c5_common_bijection import (
    fixed_map_overlap, common_bijection_moments,
)
from hyp105_g5e2b3e1c11_coupled_four import (
    common_prefix_joint_moments,genuine_W32_coupled_four_report,
)


def brute_shared_prefix(source,target,V,p):
    left=tuple(x for x in range(V) if x not in p)
    right=tuple(x for x in range(V) if x not in p.values())
    vals=[]
    for tail in permutations(right):
        g=[0]*V
        for a,b in p.items():g[a]=b
        for a,b in zip(left,tail):g[a]=b
        vals.append(fixed_map_overlap(source,target,tuple(g)))
    return vals


class CoupledFourC11Tests(unittest.TestCase):
    def test_full_unpinned_matches_independent_C5_seven_intersections(self):
        V=8
        cells=tuple(frozenset(R) for R in combinations(range(V),6))
        source={R:(i%4+1) for i,R in enumerate(cells) if i%3!=0}
        target=set(cells[::3])
        x=common_prefix_joint_moments(source,target,V,{})
        y=common_bijection_moments(source,target,V)
        self.assertEqual(x["mean_one_shared_completion"],
                         y["one_common_right_bijection_mean"])
        self.assertEqual(x["second_moment_one_shared_completion"],
                         y["one_common_right_bijection_second_moment"])
        self.assertEqual(x["variance_one_shared_completion"],
                         y["one_common_right_bijection_variance"])

    def test_small_all_24_shared_four_line_completions(self):
        V=8
        cells=tuple(frozenset(R) for R in combinations(range(V),6))
        source={R:(i%4+1) for i,R in enumerate(cells) if i%3!=0}
        target=set(cells[1::3])
        for p in ({0:0,1:1,2:2,3:3},{0:4,1:1,3:2,6:7},
                  {0:0,1:1,2:2,3:3,4:4,5:5}):
            x=common_prefix_joint_moments(source,target,V,p)
            vals=brute_shared_prefix(source,target,V,p)
            self.assertEqual(len(vals),factorial(V-len(p)))
            self.assertEqual(x["mean_one_shared_completion"],
                             Fraction(sum(vals),len(vals)))
            self.assertEqual(x["second_moment_one_shared_completion"],
                             Fraction(sum(v*v for v in vals),len(vals)))
            self.assertLessEqual(x["worst_completion_lower_from_second_moment"],min(vals))
            self.assertLessEqual(min(vals),x["existential_completion_upper_from_mean"])

    def test_constant_star_prefix_exact_positive_certificates(self):
        V=8
        star={frozenset(set(range(V))-{0,j}) for j in range(1,V)}
        source={R:1 for R in star}
        for image,expected in ((0,7),(1,1)):
            p={0:image,2:2 if image!=2 else 3,3:3 if image!=3 else 4,4:4 if image!=4 else 5}
            if len(set(p.values()))!=len(p):
                continue
            x=common_prefix_joint_moments(source,star,V,p)
            values=brute_shared_prefix(source,star,V,p)
            self.assertTrue(all(v==expected for v in values))
            self.assertEqual(x["variance_one_shared_completion"],0)
            self.assertEqual(x["worst_completion_lower_from_second_moment"],expected)
            self.assertEqual(x["min_exact_if_bounds_meet"],expected)

    def test_true_original_W32_shared_four_recount(self):
        d=genuine_W32_coupled_four_report()
        self.assertEqual(d["historical_BA"],77)
        self.assertEqual(d["all_common_tail_maps_checked"],24)
        self.assertTrue(d["independent_original_C4_tensor_all_24_agree"])
        # Frozen independently verified real W32 24-map baseline.
        self.assertEqual(d["restricted_four_line_exact_minimum"],56)
        self.assertEqual(d["restricted_four_line_exact_maximum"],77)
        self.assertEqual(d["conditional_mean"],"133/2")
        self.assertEqual(d["conditional_variance"],"28")
        self.assertEqual(d["moment_based_lower"],42)
        self.assertEqual(d["conditional_mean_existential_upper"],66)
        self.assertEqual(d["minimizing_full_right_permutation"],
                         (14,13,12,11,10,9,8,7,6,5,4,0,1,3,2))
        self.assertLessEqual(d["moment_based_lower"],
                             d["restricted_four_line_exact_minimum"])
        self.assertGreaterEqual(d["conditional_mean_existential_upper"],
                                d["restricted_four_line_exact_minimum"])
        self.assertFalse(d["f_and_F_unrestricted_15_factorial_minimum_proved"])

    def test_invalid_pin_and_duplicate_target_fail_closed(self):
        V=8
        e=frozenset(range(6))
        bad=({-1:0},{0:8},{0:0,1:0},{True:1})
        for p in bad:
            with self.assertRaises(ValueError):
                common_prefix_joint_moments({e:1},{e},V,p)
        with self.assertRaises(ValueError):
            common_prefix_joint_moments({e:1},[e,e],V,{})
        with self.assertRaises(ValueError):
            common_prefix_joint_moments({e:-1},{e},V,{})
        with self.assertRaises(ValueError):
            common_prefix_joint_moments({e:1},{e},V,{},max_relevant_source_cells=0)


if __name__=="__main__":
    unittest.main()
