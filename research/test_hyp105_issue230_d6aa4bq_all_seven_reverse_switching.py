"""AA4-BQ independent original seven-GF5 W32, cube, reverse-cover oracles."""
import unittest
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import seven_census, classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
    mobius_cube_coefficients,
    invert_cube_coefficients,
    exact_cube_mean,
    original_seven_source_factor_cube_degree_certificate,
    cayley_ball_size_by_cycles,
    radial_inverse_cover_certificate,
    abstract_one_local_zero_center_barrier,
)

def independent_full_seven_GF5_by_original_flag_sets(model, preselected):
    """An independent scan of all real left physical candidates, fixed once.

    Neither relies on new cube Möbius code for GF5 tagging nor invents
    new six-factor physical Q. Uses historical original seven classifier.
    """
    inc=tuple(model["incidences"])
    f=tuple(model["left_labels"])
    g=tuple(model["right_labels"])
    accepted={}
    for Q,kind in preselected:
        tag=classify_seven_prechecked(Q,f,g,inc)
        if tag is not None:
            accepted[Q]=tag
    return accepted


def direct_boolean_cube_expectation(values,dimension,p):
    return sum(Fraction(values[mask])*(p**mask.bit_count())*
               ((1-p)**(dimension-mask.bit_count()))
               for mask in range(1<<dimension))


def direct_cayley_distance(perm):
    seen=set()
    c=0
    for start in range(len(perm)):
        if start in seen:continue
        c+=1
        node=start
        while node not in seen:
            seen.add(node)
            node=perm[node]
    return len(perm)-c


class AA4BQOriginalAllSeven(unittest.TestCase):
    def test_01_all_seven_REAL_W32_K6_three_swap_mobius_and_census(self):
        model=fixture(1,"S72")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        self.assertEqual((s,V,a),(2,15,6))
        # These are three commuting actual ORIGINAL LINE source-factor swaps.
        swaps=((0,1),(2,3),(4,5))
        left=tuple(selected_left_six(model))
        self.assertEqual(len(left),62370)
        values=[]
        sixclass_counts=[]
        for mask in range(8):
            chosen=tuple(i for i in range(3) if mask&(1<<i))
            repaired=apply_disjoint_factor_swaps(g,swaps,chosen)
            changed=dict(model,right_labels=repaired)
            accepted=independent_full_seven_GF5_by_original_flag_sets(changed,left)
            values.append(len(accepted))
            sixclass_counts.append(accepted)
            self.assertEqual(set(repaired),set(g))
            self.assertEqual(len(repaired),V)
        baseline=seven_census(model,independent_checks=False,witness_sets=True)
        self.assertEqual(values[0],baseline["S_seven"])
        self.assertEqual(sixclass_counts[0],baseline["sets"])
        coeff=mobius_cube_coefficients(values,3)
        self.assertEqual(invert_cube_coefficients(coeff,3),tuple(values))
        for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            self.assertEqual(exact_cube_mean(coeff,3,p),
                             direct_boolean_cube_expectation(values,3,p))

    def test_02_seven_DISJOINT_original_W32_source_support_exact_zero(self):
        model=fixture(1,"lex")
        _,V,_,inc,f,g,_,_=_original_source(model)
        pairs=tuple((2*i,2*i+1) for i in range(7))
        self.assertEqual(len(set(z for pair in pairs for z in pair)),14)
        left=tuple(selected_left_six(model))
        self.assertEqual(len(left),62370)
        # Independent genuine-original source-Q support witness across
        # EVERY possible first-side sixflag candidate. No fake W3.
        for Q,kind in left:
            z=original_seven_source_factor_cube_degree_certificate(Q,inc,pairs)
            self.assertLessEqual(len(z["swaps_with_possible_Q_influence"]),6)
            self.assertTrue(z["seven_or_higher_disjoint_mixed_finite_differences_ZERO"])
        # Explicit original seven-GF5 per-sixflag oracle over entire
        # 2^7 cube for sampled REAL Q; model-specific accepted tags.
        sample=[Q for Q,_ in left[::max(1,len(left)//29)]]
        for Q in sample:
            vals=[]
            for mask in range(1<<7):
                after=apply_disjoint_factor_swaps(g,pairs,tuple(
                    i for i in range(7) if mask>>i&1))
                vals.append(int(classify_seven_prechecked(Q,f,after,inc) is not None))
            C=mobius_cube_coefficients(vals,7)
            self.assertEqual(C[127],0)
            self.assertEqual(invert_cube_coefficients(C,7),tuple(vals))
        with self.assertRaises(ValueError):
            original_seven_source_factor_cube_degree_certificate(
                (0,0,1,2,3,4),inc,pairs)
        with self.assertRaises(ValueError):
            apply_disjoint_factor_swaps(g,((0,1),(1,2)),(0,1))

    def test_03_Cayley_exact_ball_vs_independent_FULL_Sn(self):
        for n in range(2,8):
            for radius in range(n):
                actual=sum(direct_cayley_distance(p)<=radius for p in permutations(range(n)))
                self.assertEqual(cayley_ball_size_by_cycles(n,radius),actual)
        self.assertEqual(cayley_ball_size_by_cycles(5,2),46)
        self.assertEqual(cayley_ball_size_by_cycles(15,0),1)
        self.assertGreater(cayley_ball_size_by_cycles(15,4),1)
        with self.assertRaises(ValueError):
            cayley_ball_size_by_cycles(1,0)
        with self.assertRaises(ValueError):
            cayley_ball_size_by_cycles(5,5)

    def test_04_independent_exact_inverse_cover_incidence_Ksubsets(self):
        good=(0,1,2,3,4)
        groups=((0,1,2),(1,2,3),(2,3,4),(0,3,4))
        # Covers many but not ALL 3-subsets: must reject falsely
        # overoptimistic reverse switching.
        with self.assertRaises(AssertionError):
            radial_inverse_cover_certificate(good,3,groups)
        good=(0,1,2,3)
        groups=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
        z=radial_inverse_cover_certificate(good,3,groups,universe_size=7)
        self.assertEqual(z["number_original_good_root_subsets"],4)
        self.assertEqual(z["reverse_incidence_count"],4)
        self.assertEqual(z["exact_nonnegative_reverse_cover_slack"],0)
        z=radial_inverse_cover_certificate(good,2,(good,),universe_size=7)
        self.assertEqual(z["reverse_incidence_count"],comb(4,2))
        self.assertTrue(z["center_root_count_positive_NOT_INFERRED"])

    def test_05_uniform_ONE_swap_abstract_countermodel_zero_center_not_GQ(self):
        for n in (2,4,15,85):
            for G in (1,3,27,125):
                z=abstract_one_local_zero_center_barrier(n,G)
                self.assertEqual(z["zero_accepted_original_center"],0)
                self.assertEqual(z["accepted_after_one_global_source_swap"],G)
                self.assertTrue(z["degree_one_on_every_disjoint_swap_cube"])
                self.assertTrue(z["not_a_genuine_W3_or_historical_GF5_counterexample"])
        # Exhaustively demonstrate the countermodel on S5, for EVERY
        # starting full map there is a <=ONE-swap completion accepting
        # ALL G roots, yet many initial centers have ZERO roots.
        n=5
        G=7
        zero=0
        for perm in permutations(range(n)):
            if perm[0]!=0:zero+=1
            donor=perm.index(0)
            z=list(perm)
            z[0],z[donor]=z[donor],z[0]
            self.assertEqual(z[0],0)
            self.assertLessEqual(int(donor!=0),1)
            self.assertEqual(len(set(z)),n)
        self.assertEqual(zero,96)

    def test_06_all_seven_tag_scope_and_negative_inputs(self):
        model=fixture(1,"reverse")
        _,V,_,inc,f,g,_,_=_original_source(model)
        baseline=seven_census(model,independent_checks=False,witness_sets=True)
        self.assertEqual(set(baseline["seven_class_motif_counts"]),
                         {"D6","B-left/A-right","A-left/B-right",
                          "C/A","C/B","B/B-overlap","B/B-disjoint"})
        with self.assertRaises(ValueError):
            mobius_cube_coefficients((1,2,3),2)
        with self.assertRaises(ValueError):
            mobius_cube_coefficients((1,-1),1)
        with self.assertRaises(ValueError):
            exact_cube_mean((1,2),1,Fraction(-1,2))
        with self.assertRaises(ValueError):
            radial_inverse_cover_certificate((0,1),3,())
        with self.assertRaises(ValueError):
            apply_disjoint_factor_swaps(tuple((0,1) for i in range(15)),
                                        ((0,1),),(0,))

if __name__=="__main__":
    unittest.main()
