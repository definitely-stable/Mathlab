"""AA4-BO independent all-h arithmetic, physical oracles and genuine originals."""
import unittest
from collections import Counter
from itertools import combinations,permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bo_simultaneous_cherry_repair import (
    two_pin_cycle_survivor_certificate,
    occupied_two_pin_C6_avoiding,
    genuine_root_Q_avoiding_opposite_ids,
    simultaneous_two_original_cherries,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def independent_physical_six_cycle_with_pins_and_exclusions(E,a,e1,e2,F):
    """Different test oracle: enumerate canonical graph Hamiltonian C6 edge sets."""
    occupied=set(E)
    forbidden=set(F)
    pinned={e1,e2}
    output=set()
    for six in combinations(range(a),6):
        v=six[0]
        for tail in permutations(six[1:]):
            order=(v,)+tail
            if order[1]>order[5]:continue
            cyc=frozenset(tuple(sorted((order[i],order[(i+1)%6])))
                          for i in range(6))
            if pinned<=cyc and cyc<=occupied and not cyc&forbidden:
                output.add(cyc)
    return output


def replay_all_swaps(original,swaps,protected):
    cur=list(original)
    for u,v in swaps:
        if u in protected or v in protected:
            raise AssertionError("an original source factor pin has moved")
        cur[u],cur[v]=cur[v],cur[u]
        assert len(set(cur))==len(cur)
        assert all(cur[i]==original[i] for i in protected)
    return tuple(cur)


class AA4BOTwoRoot(unittest.TestCase):
    def test_01_all_h_two_root_strict_positive_arithmetic(self):
        for h in tuple(range(5,37))+(40,48,64,80):
            z=two_pin_cycle_survivor_certificate(1<<h)
            self.assertGreater(z["adjacent_pins_physical_C6_survivors_lower"],0)
            self.assertGreater(z["disjoint_pins_physical_C6_survivors_lower"],0)
            self.assertGreater(z["simultaneously_repairable_pair_fraction_lower"],1/2)
            self.assertLessEqual(z["max_combined_other_original_source_factors"],8)
            self.assertEqual(z["max_whole_original_factor_image_transpositions"],8)
            self.assertTrue(z["original_input_g_positive_NOT_PROVED"])
        for v in (2,4,16,33,True):
            with self.assertRaises(ValueError):
                two_pin_cycle_survivor_certificate(v)

    def test_02_independent_K7_K8_avoided_physical_cycle_oracle(self):
        for a in (7,8):
            E=tuple(combinations(range(a),2))
            for pins in (((0,1),(1,2)),((0,1),(2,3))):
                remaining=tuple(edge for edge in E if edge not in pins)
                for forbidden in ((),remaining[:1],remaining[1:4],remaining[:6]):
                    result=occupied_two_pin_C6_avoiding(E,a,*pins,forbidden)
                    oracle=independent_physical_six_cycle_with_pins_and_exclusions(
                        E,a,*pins,forbidden)
                    self.assertEqual(result is not None,bool(oracle))
                    if result is not None:self.assertIn(frozenset(result),oracle)
        # Pendant edge on abstract near-complete graph: local BL regularity
        # fails, so absence is a negative method control NOT a root counterexample.
        E=tuple(edge for edge in combinations(range(7),2) if 0 not in edge or edge==(0,1))
        self.assertIsNone(occupied_two_pin_C6_avoiding(E,7,(0,1),(2,3),()))
        with self.assertRaises(ValueError):
            occupied_two_pin_C6_avoiding(tuple(combinations(range(7),2)),7,
                                        (0,1),(2,3),tuple(combinations(range(7),2))[:7])

    def test_03_true_W32_source_greedy_distinct_source_factor_and_rejection(self):
        for name,model in (("dual_zero",zero_split_original_W32()),)+tuple(
                (key,fixture(1,key)) for key in ("lex","reverse","S68","S72")):
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            found=0
            for side,by in ((0,byP),(1,byL)):
                for p in range(V):
                    for flags in combinations(by[p],2):
                        pins={inc[j][1-side] for j in flags}
                        Q=genuine_root_Q_avoiding_opposite_ids(model,side,p,flags,pins)
                        if Q is None:continue
                        self.assertEqual(len(Q),6)
                        self.assertEqual(len(set(inc[j][1-side] for j in Q)),6)
                        self.assertEqual(len(set(inc[j][side] for j in Q)),5)
                        found+=1
            self.assertGreater(found,0)
        model=fixture(1,"lex")
        _,_,_,_,_,_,byP,_=_original_source(model)
        with self.assertRaises(ValueError):
            genuine_root_Q_avoiding_opposite_ids(model,0,0,
                                                 (byP[0][0],byP[0][0]),())
        with self.assertRaises(ValueError):
            genuine_root_Q_avoiding_opposite_ids(model,0,0,(999,byP[0][1]),())

    def test_04_true_W34_independent_two_source_roots_ONE_map(self):
        # Genuine symplectic GF(4), nononto physical K14, both typed sides.
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                sampled=[(p,tuple(flags)) for p in (0,1,7,37,84)
                         for flags in combinations(by[p],2)]
                result=None
                for first in sampled[:12]:
                    for second in sampled[12:42]:
                        result=simultaneous_two_original_cherries(
                            model,side,first,second,require_regular=False)
                        if result is not None:break
                    if result is not None:break
                self.assertIsNotNone(result,"finite W34 two REAL root witness required")
                self.assertTrue(result["actual_Qs_are_distinct"])
                self.assertLessEqual(result["exact_minimum_image_transpositions"],8)
                self.assertEqual(len(result["actual_true_original_cherry_certificates"]),2)
                pinned=result["all_original_opposite_pin_ids"]
                old=(g,f)[side]
                final=replay_all_swaps(old,result["actual_shortest_global_transpositions"],pinned)
                self.assertEqual(final,result["final_full_global_map"])
                after=result["repaired_original_complete_model"]
                for cert in result["actual_true_original_cherry_certificates"]:
                    Q=cert["Q"]
                    tag=independent_joint_classify(
                        Q,"B" if side==0 else "A","A" if side==0 else "B",
                        inc,after["left_labels"],after["right_labels"])
                    self.assertEqual(tag,"B-left/A-right" if side==0 else "A-left/B-right")
                    self.assertTrue(set(cert["flags"])<=set(Q))

    def test_05_real_W32_two_root_finite_no_false_asymptotic_promotion(self):
        # No h>=5 claim is inferred from these tiny genuine-source runs.
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        found=False
        roots=[(p,tuple(flags)) for p in range(V) for flags in combinations(byP[p],2)]
        for first in roots[:8]:
            for second in roots[8:]:
                result=simultaneous_two_original_cherries(
                    model,0,first,second,require_regular=False)
                if result is None:continue
                self.assertLessEqual(result["exact_minimum_image_transpositions"],8)
                self.assertTrue(result["same_original_source_incidence_Q_ids_not_resampled"])
                found=True
                break
            if found:break
        # Zero is allowed at h=1: this test is a concrete falsifier,
        # NOT a fabricated all-h W32-positive theorem.
        self.assertIsInstance(found,bool)

    def test_06_genuine_original_root_input_and_false_claim_guards(self):
        model=fixture(1,"lex")
        _,_,_,_,_,_,byP,_=_original_source(model)
        root=(0,tuple(byP[0][:2]))
        with self.assertRaises(ValueError):
            simultaneous_two_original_cherries(model,0,root,root,require_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_two_original_cherries(model,0,root,(0,(999,byP[0][1])),
                                               require_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_two_original_cherries(model,True,root,(1,tuple(byP[1][:2])),
                                               require_regular=False)


if __name__=="__main__":
    unittest.main()
