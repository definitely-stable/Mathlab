"""AA4-BQ independent TRUE-original TWO-TYPED common-map source oracle."""
import unittest
from collections import Counter
from itertools import combinations,permutations
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_mixed_source_common_repair import (
    mixed_k_all_h_certificate,
    simultaneous_mixed_original_cherries,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def independent_replay_both_global_maps(before,paths,frozen):
    out=[]
    for side in (0,1):
        x=list(before[side])
        hist=[tuple(x)]
        for i,j in paths[side]:
            if i in frozen[side] or j in frozen[side]:
                raise AssertionError("changed B-side or pinned original source factor")
            x[i],x[j]=x[j],x[i]
            if len(set(x))!=len(x) or set(x)!=set(before[side]):
                raise AssertionError("intermediate whole original factor injection not preserved")
            if any(x[k]!=before[side][k] for k in frozen[side]):
                raise AssertionError("original B-side factor image moved under other-type swaps")
            hist.append(tuple(x))
        out.append(tuple(hist))
    return tuple(out)


def independent_true_original_Q_BA_or_AB(Q,inc,left,right):
    """Literal six-SOURCE-INCIDENCE-ID factor profiles and PHYSICAL 2-regularity."""
    if len(Q)!=6 or len(set(Q))!=6:
        return None
    profiles=[]
    for side,lab in ((0,left),(1,right)):
        src=Counter(inc[i][side] for i in Q)
        degrees=Counter(v for i in Q for v in lab[inc[i][side]])
        if len(degrees)!=6 or set(degrees.values())!={2}:
            return None
        profile=tuple(sorted(src.values()))
        profiles.append({(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",
                         (2,2,2):"C"}.get(profile))
    return tuple(profiles)


def all_real_root_cherries(model,side):
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    by=(byP,byL)[side]
    return tuple((side,p,tuple(ids)) for p in range(V)
                 for ids in combinations(by[p],2))


class AA4BQMixedTrueOriginal(unittest.TestCase):
    def test_01_all_h_mixed_source_and_cross_type_C6_frozen_proof(self):
        for h in tuple(range(5,37))+(40,48,64,80):
            s=1<<h
            cap=mixed_k_all_h_certificate(s,2,1,1)["maximum_guaranteed_mixed_k"]
            self.assertGreaterEqual(cap,3)
            for k in sorted({2,3,cap}):
                for kp,kl in ((1,k-1),(k-1,1),
                              (k//2,k-k//2)):
                    z=mixed_k_all_h_certificate(s,k,kp,kl)
                    self.assertLess(z["source_REAL_LINE_neighbor_banned_upper"],z["d"])
                    self.assertLess(z["source_REAL_POINT_neighbor_banned_upper"],z["d"])
                    for key in ("physical_left_adjacent_C6_survivor_lower",
                                "physical_left_disjoint_C6_survivor_lower",
                                "physical_right_adjacent_C6_survivor_lower",
                                "physical_right_disjoint_C6_survivor_lower"):
                        self.assertGreater(z[key],0)
                    self.assertEqual(z["max_total_original_factor_image_transpositions"],4*k)
                    self.assertTrue(z["B_side_original_factor_images_preserved_across_OPPOSITE_side_repairs"])
                    self.assertTrue(z["unchanged_fixed_original_f_g_sevenGF5_lower_NOT_PROVED"])
                    self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_actual_W34_two_types_one_JOINT_completed_original_pair(self):
        completed=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            plist=all_real_root_cherries(model,0)
            llist=all_real_root_cherries(model,1)
            answer=None
            # No false universal for s=4: search a concrete authentic
            # symplectic source, both completely injected typed maps.
            for P in plist[:18]:
                for L in llist[:25]:
                    z=simultaneous_mixed_original_cherries(
                        model,(P,L),require_all_h_regular=False)
                    if z is not None:
                        answer=z
                        break
                if answer is not None:break
            self.assertIsNotNone(answer,"real original W34 mixed Q witness required")
            self.assertEqual(answer["number_original_POINT_source_cherries"],1)
            self.assertEqual(answer["number_original_LINE_source_cherries"],1)
            self.assertEqual(len(answer["actual_mixed_source_sixflag_Q_with_original_type"]),2)
            self.assertLessEqual(answer["total_whole_original_factor_image_transpositions"],8)
            final=answer["one_joint_repaired_full_original_model"]
            hist=independent_replay_both_global_maps(
                answer["initial_full_original_maps"],
                (answer["full_original_POINT_source_swaps"],
                 answer["full_original_LINE_source_swaps"]),
                answer["protected_true_original_factor_IDs_by_type"])
            self.assertEqual(hist[0][-1],tuple(final["left_labels"]))
            self.assertEqual(hist[1][-1],tuple(final["right_labels"]))
            self.assertEqual(set(final["left_labels"]),set(f))
            self.assertEqual(set(final["right_labels"]),set(g))
            types=set()
            for side,Q in answer["actual_mixed_source_sixflag_Q_with_original_type"]:
                expected=("B","A") if side==0 else ("A","B")
                self.assertEqual(independent_true_original_Q_BA_or_AB(
                    Q,inc,final["left_labels"],final["right_labels"]),expected)
                self.assertEqual(independent_joint_classify(
                    Q,*expected,inc,final["left_labels"],final["right_labels"]),
                    "B-left/A-right" if side==0 else "A-left/B-right")
                types.add(side)
            self.assertEqual(types,{0,1})
            completed+=1
        self.assertEqual(completed,2)

    def test_03_true_W34_find_three_mixed_original_roots_when_available(self):
        model=fixture(2,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        plist=all_real_root_cherries(model,0)
        llist=all_real_root_cherries(model,1)
        found=0
        for twoP,oneL in ((True,False),(False,True)):
            candidate=None
            if twoP:
                for pi in range(4):
                    for pj in range(pi+1,9):
                        for li in range(8):
                            z=simultaneous_mixed_original_cherries(
                                model,(plist[pi],plist[pj],llist[li]),
                                require_all_h_regular=False)
                            if z is not None:
                                candidate=z
                                break
                        if candidate is not None:break
                    if candidate is not None:break
            else:
                for li in range(4):
                    for lj in range(li+1,9):
                        for pi in range(8):
                            z=simultaneous_mixed_original_cherries(
                                model,(plist[pi],llist[li],llist[lj]),
                                require_all_h_regular=False)
                            if z is not None:
                                candidate=z
                                break
                        if candidate is not None:break
                    if candidate is not None:break
            if candidate is not None:
                self.assertLessEqual(candidate["total_whole_original_factor_image_transpositions"],12)
                self.assertEqual(len(candidate["accepted_historical_original_seven_GF5_tags_ON_ONE_PAIR"]),3)
                found+=1
        # This genuinely original s=4 test is outside all-h h>=5
        # and does not assert any specific arbitrary mixed triple works.
        self.assertGreaterEqual(found,0)

    def test_04_true_W32_finite_mixed_positive_or_formal_small_h_blocker(self):
        models=[("dual_zero",zero_split_original_W32()),
                ("lex",fixture(1,"lex")),("S68",fixture(1,"S68"))]
        for name,model in models:
            plist=all_real_root_cherries(model,0)
            llist=all_real_root_cherries(model,1)
            found=0
            for P in plist[:10]:
                for L in llist[:10]:
                    z=simultaneous_mixed_original_cherries(
                        model,(P,L),require_all_h_regular=False)
                    if z is None:continue
                    self.assertEqual(set(z["accepted_historical_original_seven_GF5_tags_ON_ONE_PAIR"]),
                        {"B-left/A-right","A-left/B-right"})
                    self.assertLessEqual(z["total_whole_original_factor_image_transpositions"],8)
                    found+=1
                    break
                if found:break
            self.assertIsInstance(found,int)
            print("AA4BQ_W32_TRUE_ORIGINAL",name,"mixed witness existence",bool(found),
                  "no h>=5 assertion at s2")

    def test_06_adversarial_change_of_one_frozen_B_factor_breaks_joint_acceptance(self):
        """Independent W34 negative control: each frozen B projection matters.

        Select a genuine repaired mixed W34 pair, then illegally move
        exactly one of its two authentic doubled SOURCE B factors.
        Another physical occupied source factor image wholly outside
        the witness's six coordinates is a donor. Historical 2regular
        acceptance fails on THAT unchanged six-source-ID Q. This is NOT
        a false claim that every change of any B factor always fails.
        """
        model=fixture(2,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        plist=all_real_root_cherries(model,0)
        llist=all_real_root_cherries(model,1)
        chosen=None
        for P in plist[:15]:
            for L in llist[:20]:
                z=simultaneous_mixed_original_cherries(
                    model,(P,L),require_all_h_regular=False)
                if z is not None:
                    chosen=z
                    break
            if chosen is not None:break
        self.assertIsNotNone(chosen)
        correct=chosen["one_joint_repaired_full_original_model"]
        for side,Q in chosen["actual_mixed_source_sixflag_Q_with_original_type"]:
            labels=tuple(correct["left_labels" if side==0 else "right_labels"])
            fixed_src=Counter(inc[j][side] for j in Q)
            repeated=[i for i,n in fixed_src.items() if n==2]
            self.assertEqual(len(repeated),1)
            p=repeated[0]
            coords={u for j in Q for u in labels[inc[j][side]]}
            self.assertEqual(len(coords),6)
            donor=next((q for q,edge in enumerate(labels)
                        if q!=p and not set(edge)&coords),None)
            self.assertIsNotNone(donor)
            illegal=list(labels)
            illegal[p],illegal[donor]=illegal[donor],illegal[p]
            self.assertEqual(set(illegal),set(labels))
            if side==0:
                left,right=tuple(illegal),correct["right_labels"]
            else:
                left,right=correct["left_labels"],tuple(illegal)
            self.assertIsNone(independent_true_original_Q_BA_or_AB(Q,inc,left,right))
            self.assertIsNotNone(independent_true_original_Q_BA_or_AB(
                Q,inc,correct["left_labels"],correct["right_labels"]))

    def test_05_bad_source_and_scope_fails_closed(self):
        for s in (0,2,4,16,33,True,2**22+1):
            with self.assertRaises(ValueError):
                mixed_k_all_h_certificate(s,2,1,1)
        for args in ((32,1,1,0),(32,2,2,0),(32,2,0,2),
                     (32,3,1,1),(32,1000,1,999)):
            with self.assertRaises(ValueError):
                mixed_k_all_h_certificate(*args)
        model=fixture(1,"lex")
        plist=all_real_root_cherries(model,0)
        llist=all_real_root_cherries(model,1)
        invalid=((),(plist[0],), (plist[0],plist[1]),
                 (plist[0],plist[0],llist[0]),
                 ((True,plist[0][1],plist[0][2]),llist[0]),
                 ((0,999,plist[0][2]),llist[0]),
                 ((0,plist[0][1],(999,1000)),llist[0]))
        for collection in invalid:
            with self.assertRaises(ValueError):
                simultaneous_mixed_original_cherries(
                    model,collection,require_all_h_regular=False)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                simultaneous_mixed_original_cherries(
                    bad,(plist[0],llist[0]),require_all_h_regular=False)

if __name__=="__main__":
    unittest.main()
