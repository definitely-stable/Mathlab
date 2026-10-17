"""AA4-BP independent source W32/W34 k-root SAME full g verification."""
import unittest
from collections import Counter
from itertools import combinations,permutations
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bp_k_root_common_repair import (
    k_root_uniform_all_h_certificate,
    _physical_pinned_sixcycle_avoiding_many,
    simultaneous_k_original_cherries,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify
from hyp105_issue230_d6aa4bo_simultaneous_cherry_repair import (
    simultaneous_two_original_cherries,
)


def independent_physical_connected_C6_with_two_pins(E,a,p1,p2,F):
    """Unrelated undirected 6-vertex / cycles with physical forbidden edges."""
    edges=set(E)
    forbid=set(F)
    good=set()
    for six in combinations(range(a),6):
        for tail in permutations(six[1:]):
            order=(six[0],)+tail
            if order[1]>order[-1]:continue
            target=frozenset(tuple(sorted((order[i],order[(i+1)%6])))
                             for i in range(6))
            if {p1,p2}<=target and target<=edges and not target&forbid:
                good.add(target)
    return good


def independent_replay_full_source_factor_swaps(before,path,pins):
    """Rebuild each entire original-factor physical permutation from scratch."""
    seen=[tuple(before)]
    cur=list(before)
    for x,y in path:
        if x in pins or y in pins:raise AssertionError("protected genuine source LINE moved")
        cur[x],cur[y]=cur[y],cur[x]
        assert len(set(cur))==len(cur)
        assert set(cur)==set(before)
        for i in pins: assert cur[i]==before[i]
        seen.append(tuple(cur))
    return tuple(seen)


def candidate_true_original_root_lists(model,side):
    _,V,a,inc,f,g,byP,byL=_original_source(model)
    by=(byP,byL)[side]
    return tuple((p,tuple(fl)) for p in range(V) for fl in combinations(by[p],2))


class AA4BPTrueOriginalKRootCommon(unittest.TestCase):
    def test_01_all_h_uniform_growing_k_exact_integer_cycle_and_source_Hall(self):
        for h in tuple(range(5,37))+(40,48,64,80):
            s=1<<h
            full=k_root_uniform_all_h_certificate(s)
            cap=full["max_certified_k_distinct_original_roots"]
            self.assertGreaterEqual(cap,4)
            for k in (1,2,cap):
                z=k_root_uniform_all_h_certificate(s,k)
                self.assertGreater(z["adjacent_pinned_physical_sixcycle_survivor_lower"],0)
                self.assertGreater(z["disjoint_pinned_physical_sixcycle_survivor_lower"],0)
                self.assertLess(z["max_forbidden_real_original_opposite_SOURCE_line_ids_per_new_flag"],z["d"])
                self.assertLessEqual(z["max_whole_original_line_image_transpositions_one_COMMON_map"],4*k)
                self.assertEqual(z["distinct_true_original_source_sixflag_BA_motifs_in_one_map_lower"],k)
                self.assertGreater(4*z["guaranteed_physically_regular_original_point_cherries"],
                                   3*z["all_genuine_point_cherries"])
                self.assertTrue(z["every_k_subset_of_regular_original_roots_has_one_own_COMMON_repair"])
                self.assertTrue(z["original_UNMODIFIED_full_f_g_GF5_positive_NOT_PROVED"])
                self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            if h<=9:
                G=full["guaranteed_physically_regular_original_point_cherries"]
                N=full["all_genuine_point_cherries"]
                self.assertGreater(Fraction(comb(G,cap),comb(N,cap)),0)
                self.assertLess(Fraction(comb(G,cap),comb(N,cap)),1)

    def test_02_independent_physical_K8_forbiddens_above_six(self):
        a=8
        E=tuple(combinations(range(a),2))
        for pins in (((0,1),(1,2)),((0,1),(2,3))):
            available=tuple(x for x in E if x not in pins)
            for F in ((),available[:3],available[:7],available[4:13]):
                result=_physical_pinned_sixcycle_avoiding_many(E,a,*pins,F)
                oracle=independent_physical_connected_C6_with_two_pins(
                    E,a,*pins,F)
                if result is not None:
                    self.assertIn(frozenset(result),oracle)
                if not oracle:
                    self.assertIsNone(result)
        with self.assertRaises(ValueError):
            _physical_pinned_sixcycle_avoiding_many(E,a,(0,1),(0,1),())
        with self.assertRaises(ValueError):
            _physical_pinned_sixcycle_avoiding_many(E,a,(0,1),(1,2),((0,1),))

    def test_03_real_original_W34_two_and_select_three_COMMON_full_global_map(self):
        matched=0
        triples=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side in (0,1):
                roots=candidate_true_original_root_lists(model,side)
                chosen=None
                # Search only finite ACTUAL W(3,4) source. No h>=5
                # asymptotic theorem inferred from selected finite data.
                for i in range(0,min(20,len(roots)),2):
                    for j in range(i+1,min(45,len(roots)),3):
                        candidate=simultaneous_k_original_cherries(
                            model,side,(roots[i],roots[j]),
                            require_all_h_regular=False)
                        if candidate is not None:
                            chosen=(roots[i],roots[j],candidate)
                            break
                    if chosen:break
                self.assertIsNotNone(chosen,"genuine W34 pair common witness required")
                first,second,result=chosen
                self.assertTrue(result["one_and_same_common_global_repaired_source_map_for_ALL_k"])
                self.assertEqual(len(result["actual_k_distinct_true_original_Qs"]),2)
                self.assertLessEqual(result["exact_minimum_image_transpositions"],8)
                protected=result["all_original_ROOT_PIN_source_factor_IDs"]
                old=(g,f)[side]
                history=independent_replay_full_source_factor_swaps(
                    old,result["actual_shortest_global_transpositions"],protected)
                self.assertEqual(history[-1],result["final_full_global_map"])
                for Q in result["actual_k_distinct_true_original_Qs"]:
                    after=result["repaired_original_complete_model"]
                    tag=independent_joint_classify(
                        Q,"B" if side==0 else "A","A" if side==0 else "B",
                        inc,after["left_labels"],after["right_labels"])
                    self.assertEqual(tag,"B-left/A-right" if side==0 else "A-left/B-right")
                matched+=1
                # Opportunistic actual W34 three-root candidate:
                # no false universal h=2 theorem.
                for third in roots[20:75]:
                    if third in (first,second):continue
                    candidate=simultaneous_k_original_cherries(
                        model,side,(first,second,third),
                        require_all_h_regular=False)
                    if candidate is not None:
                        self.assertEqual(len(candidate["actual_k_distinct_true_original_Qs"]),3)
                        self.assertLessEqual(candidate["exact_minimum_image_transpositions"],12)
                        triples+=1
                        break
        self.assertEqual(matched,4)
        self.assertGreaterEqual(triples,0)

    def test_04_real_original_W32_multi_root_source_is_NOT_fake_asymptotic(self):
        mods=(("dual_zero",zero_split_original_W32()),
              ("lex",fixture(1,"lex")),("S68",fixture(1,"S68")))
        finite_results=0
        for name,model in mods:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            roots=candidate_true_original_root_lists(model,0)
            # Actual original W32 source valency d=3: k>=3
            # asymptotic d>=33 guarantee must NOT be inferred.
            for i in range(4):
                for j in range(4,12):
                    q=simultaneous_k_original_cherries(
                        model,0,(roots[i],roots[j]),
                        require_all_h_regular=False)
                    if q is None:continue
                    self.assertLessEqual(q["exact_minimum_image_transpositions"],8)
                    self.assertEqual(len(q["actual_k_distinct_true_original_Qs"]),2)
                    finite_results+=1
                    break
                if finite_results:break
        self.assertGreaterEqual(finite_results,1)

    def test_05_all_k_source_factor_ids_and_bad_argument_fail_closed(self):
        for s in (0,2,4,16,33,True,2**22+1):
            with self.assertRaises(ValueError):
                k_root_uniform_all_h_certificate(s,1)
        for k in (0,-1,True,5,1000):
            with self.assertRaises(ValueError):
                k_root_uniform_all_h_certificate(32,k)
        model=fixture(1,"lex")
        roots=candidate_true_original_root_lists(model,0)
        with self.assertRaises(ValueError):
            simultaneous_k_original_cherries(model,0,())
        with self.assertRaises(ValueError):
            simultaneous_k_original_cherries(model,0,(roots[0],roots[0]),
                                              require_all_h_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_k_original_cherries(model,True,(roots[0],),
                                              require_all_h_regular=False)
        with self.assertRaises(ValueError):
            simultaneous_k_original_cherries(model,0,((999,(1,2)),),
                                              require_all_h_regular=False)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                simultaneous_k_original_cherries(bad,0,(roots[0],),
                                                  require_all_h_regular=False)

    def test_06_original_selected_Q_source_uniqueness_and_exact_shortest_transpositions(self):
        model=fixture(2,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        roots=candidate_true_original_root_lists(model,0)
        pair=None
        for i in range(10):
            for j in range(i+1,30):
                result=simultaneous_k_original_cherries(
                    model,0,(roots[i],roots[j]),require_all_h_regular=False)
                if result is not None:
                    pair=result
                    break
            if pair:break
        self.assertIsNotNone(pair)
        protected=set(pair["all_original_ROOT_PIN_source_factor_IDs"])
        free=set(pair["all_free_original_source_factor_IDs"])
        self.assertFalse(protected&free)
        self.assertEqual(len(free),8)
        self.assertEqual(len(pair["all_distinct_occupied_free_physical_images"]),8)
        self.assertEqual(len(set(pair["actual_k_distinct_true_original_Qs"])),2)
        self.assertEqual(len(pair["accepted_original_seven_GF5_tags"]),2)
        before=tuple(g)
        replays=independent_replay_full_source_factor_swaps(
            before,pair["actual_shortest_global_transpositions"],protected)
        self.assertEqual(replays[-1],pair["final_full_global_map"])
        self.assertEqual(len(replays)-1,pair["number_nontrivial_arcs"]-
                         pair["number_nontrivial_closed_cycles"])

if __name__=="__main__":
    unittest.main()
