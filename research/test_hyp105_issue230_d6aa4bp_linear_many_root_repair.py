"""AA4-BP independent large-dyadic bounds and actual original multi-root W3."""
import unittest
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify
from hyp105_issue230_d6aa4bo_simultaneous_cherry_repair import simultaneous_two_original_cherries
from hyp105_issue230_d6aa4bp_linear_many_root_repair import (
    linear_many_root_all_h_certificate,
    occupied_two_pin_C6_avoiding_many,
    simultaneous_many_original_cherries,
)


def independently_count_all_connected_C6(E,a,pins,forbidden):
    """Full C6 subsets, NOT the production canonical pinned path templates."""
    E=set(E)
    F=set(forbidden)
    seen=set()
    for six in combinations(range(a),6):
        first=six[0]
        for tail in permutations(six[1:]):
            cycle=(first,)+tail
            if cycle[1]>cycle[5]:
                continue
            physical=frozenset(tuple(sorted((cycle[j],cycle[(j+1)%6])))
                                for j in range(6))
            if set(pins)<=physical and physical<=E and not physical&F:
                seen.add(physical)
    return seen


def independent_replay(original,swaps,protected):
    z=list(original)
    for i,j in swaps:
        assert i not in protected and j not in protected
        z[i],z[j]=z[j],z[i]
        assert len(set(z))==len(z)
        assert all(z[p]==original[p] for p in protected)
    return tuple(z)


class AA4BPLinearManyOriginalRoots(unittest.TestCase):
    def test_01_all_dyadic_h5_80_source_dominates_physical_with_exact_fractions(self):
        for h in tuple(range(5,37))+(40,48,64,80):
            s=1<<h
            z=linear_many_root_all_h_certificate(s)
            k=z["max_guaranteed_roots"]
            self.assertEqual(k,(s+1)//6)
            self.assertGreaterEqual(k,5)
            self.assertLess(k*4,z["V"])
            self.assertLess(z["source_banned_original_opposite_ids_worst"],s+1)
            self.assertGreater(z["physical_adjacent_pin_C6_survivor_lower"],0)
            self.assertGreater(z["physical_disjoint_pin_C6_survivor_lower"],0)
            self.assertLess(2*z["physical_forbidden_edges_worst"],z["a"]-4)
            self.assertGreater(z["guaranteed_pin_regular_original_cherries"],
                               Fraction(3,4)*z["number_true_original_cherries"])
            for t in sorted(set((2,3,5,k))):
                if t>k:continue
                q=linear_many_root_all_h_certificate(s,t)
                self.assertEqual(q["max_original_whole_factor_image_swaps"],4*t)
                self.assertEqual(q["max_protected_true_original_opposite_factor_ids"],2*t)
        for bad in (1,2,4,8,16,33,True):
            with self.assertRaises(ValueError):
                linear_many_root_all_h_certificate(bad)
        with self.assertRaises(ValueError):
            linear_many_root_all_h_certificate(32,6)
        with self.assertRaises(ValueError):
            linear_many_root_all_h_certificate(32,True)

    def test_02_independent_complete_K8_K9_physical_cycle_with_SEVEN_exclusions(self):
        for a in (8,9):
            E=tuple(combinations(range(a),2))
            for pins in (((0,1),(1,2)),((0,1),(2,3))):
                remaining=tuple(e for e in E if e not in pins)
                for forbidden in ((),remaining[1:4],remaining[:7],remaining[-8:]):
                    witness=occupied_two_pin_C6_avoiding_many(E,a,*pins,forbidden)
                    oracle=independently_count_all_connected_C6(E,a,pins,forbidden)
                    if witness is not None:
                        self.assertIn(frozenset(witness),oracle)
                    # Canonical one-orientation search need not contain
                    # every C6: do NOT claim the reverse implication.
        E=tuple(e for e in combinations(range(8),2) if 0 not in e or e==(0,1))
        self.assertIsNone(occupied_two_pin_C6_avoiding_many(E,8,(0,1),(2,3),()))
        with self.assertRaises(ValueError):
            occupied_two_pin_C6_avoiding_many(E,8,(0,1),(2,3),((0,1),))

    def test_03_exact_original_k2_backwards_compatible_with_AA4BO(self):
        model=fixture(2,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        roots=[(p,tuple(flags)) for p in (0,1,7,37,84)
               for flags in combinations(byP[p],2)]
        found=False
        for r1 in roots[:12]:
            for r2 in roots[12:42]:
                old=simultaneous_two_original_cherries(
                    model,0,r1,r2,require_regular=False)
                if old is None:continue
                new=simultaneous_many_original_cherries(
                    model,0,(r1,r2),require_regular=False)
                self.assertIsNotNone(new)
                self.assertEqual(new["number_concurrently_accepted_distinct_original_GF5_sixsets"],2)
                self.assertLessEqual(new["exact_minimum_image_transpositions"],8)
                found=True
                break
            if found:break
        self.assertTrue(found,"must refind actual original symplectic W34 two-root witness")

    def test_04_actual_symplectic_W34_three_distinct_root_Q_one_map_and_dual(self):
        # h=2 is a FINITE falsifier, not the s>=32 all-h theorem.
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                roots=[(p,tuple(x)) for p in (0,1,7,37,84)
                       for x in combinations(by[p],2)]
                witness=None
                # Try diverse actual-original root factor pins / target
                # conflicts; finite k=3 has no general guarantee.
                for ids in ((0,11,22),(0,12,24),(1,13,25),(2,14,26),
                            (0,16,34),(3,19,37),(7,22,40),(10,27,43)):
                    if max(ids)>=len(roots):continue
                    witness=simultaneous_many_original_cherries(
                        model,side,tuple(roots[j] for j in ids),
                        require_regular=False)
                    if witness is not None:break
                self.assertIsNotNone(witness,
                                     "genuine W34 3-root search did not find finite witness")
                self.assertEqual(witness["number_concurrently_accepted_distinct_original_GF5_sixsets"],3)
                self.assertLessEqual(witness["exact_minimum_image_transpositions"],12)
                original=(g,f)[side]
                protected=set(witness["all_protected_TRUE_original_opposite_factor_IDs"])
                final=independent_replay(original,
                    witness["actual_shortest_global_transpositions"],protected)
                self.assertEqual(final,witness["final_full_global_map"])
                fixedmodel=witness["repaired_original_complete_model"]
                for candidate in witness["actual_true_original_cherry_certificates"]:
                    Q=candidate["Q"]
                    tag=independent_joint_classify(Q,
                        "B" if side==0 else "A",
                        "A" if side==0 else "B",
                        inc,fixedmodel["left_labels"],fixedmodel["right_labels"])
                    self.assertEqual(tag,"B-left/A-right" if side==0 else "A-left/B-right")
                    self.assertTrue(set(candidate["flags"])<=set(Q))

    def test_05_higher_k_mathematical_no_exponential_subset_enumeration(self):
        for s,k in ((32,5),(64,10),(128,21),(256,42),(1<<20,(1<<20)//6),
                    (1<<80,(1<<80)//6)):
            z=linear_many_root_all_h_certificate(s,k)
            self.assertEqual(z["simultaneous_roots_k"],k)
            self.assertGreater(z["guaranteed_pin_regular_original_cherries"],k)
            self.assertEqual(z["number_of_original_good_k_subsets_lower_symbolic"],
                             "binomial(G,k)")
            self.assertTrue(z["a_single_new_map_for_ALL_good_roots_NOT_PROVED"])
            self.assertTrue(z["unchanged_input_pair_GF5_positive_NOT_PROVED"])

    def test_06_invalid_original_roots_and_scope_guards(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        root=(0,tuple(byP[0][:2]))
        another=(1,tuple(byP[1][:2]))
        with self.assertRaises(ValueError):
            simultaneous_many_original_cherries(model,0,(root,root),require_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_many_original_cherries(model,0,(root,),require_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_many_original_cherries(model,True,(root,another),
                                               require_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_many_original_cherries(model,0,(root,(0,(999,byP[0][1]))),
                                               require_regular=False)


if __name__=="__main__":
    unittest.main()
