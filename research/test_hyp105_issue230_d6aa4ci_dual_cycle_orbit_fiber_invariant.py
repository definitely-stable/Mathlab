"""AA4-CI independent original-GQ complete f-orbit historical 7GF5 referees."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import permutations

from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    PERMS,W_B,W_C,W_D,_six_position_dual_cycle,
    complete_original_f_orbit, original_cycle_orbit,
    original_point_A_fiber, original_D6_fan_orbit,
    original_B_C_D6_mixed_fixture,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    original_maximal_D6_fan, SIX_CYCLE, _full_pair_injection,
)
from hyp105_issue230_projection import fixture


def direct_original_historical_fiber_orbit(model,points,records,perms):
    """Independent literal TRUE original Q historical seven-class census.

    Reconstruct full globally injected f_pi each step and classify every
    physically right eligible ORIGINAL Q with existing seven-GF5 tagger.
    No histogram / RHS formula / dual-cycle orbit calculation used.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    allowed={"A-left/B-right","C/A","D6"}
    scores=[]
    for perm in perms:
        fp=complete_original_f_orbit(f,points,perm)
        score=0
        for Q,right_type,cycle in records:
            tag=classify_seven_all_a_original_Q(Q,fp,g,inc)
            if tag is not None:
                if tag not in allowed:
                    raise AssertionError("source-A ORIGINAL sixflag emitted invalid historical tag")
                score+={"A-left/B-right":W_B,"C/A":W_C,"D6":W_D}[tag]
        scores.append(score)
    return tuple(scores)


class AA4CIOriginalFullS6Fiber(unittest.TestCase):
    def test_01_original_W34_mixed_B_C_D6_all720_maps(self):
        model,pts,selected=original_B_C_D6_mixed_fixture(2)
        r=original_point_A_fiber(model,pts)
        self.assertEqual((r["s"],r["V"],r["a"]),(4,85,14))
        self.assertEqual(r["true_original_incidence_Q_count"],5**6)
        self.assertGreaterEqual(r["source_class_counts"].get("B",0),1)
        self.assertGreaterEqual(r["source_class_counts"].get("C",0),1)
        self.assertGreaterEqual(r["source_class_counts"].get("A_physical_C6",0),1)
        self.assertGreaterEqual(r["original_baseline_B_C_weighted"],W_B+W_C)
        self.assertGreaterEqual(r["active_cyclic_dual_types"],1)
        literal=direct_original_historical_fiber_orbit(
            model,pts,r["eligible_actual_original_Q"],PERMS)
        self.assertEqual(literal,r["orbit_scores"])
        self.assertEqual(Fraction(sum(literal),720),r["original_exact_orbit_mean"])
        self.assertEqual(Fraction(sum(x*x for x in literal),720),
                         r["original_exact_orbit_second_moment"])
        self.assertEqual(len(r["right_cyclic_dual_hist"]),r["active_cyclic_dual_types"])
        s,V,a,inc,f,g,_,_=_original_source(model)
        for name,Q in selected.items():
            tag=classify_seven_all_a_original_Q(Q,f,g,inc)
            self.assertEqual(tag,{"B":"A-left/B-right","C":"C/A","D6":"D6"}[name])
        print("AA4CI_ORIGINAL_W34_MIXED","source_class",r["source_class_counts"],
              "active_cycles",r["active_cyclic_dual_types"],
              "baseline",r["original_baseline_B_C_weighted"],
              "minmax",(min(literal),max(literal)),
              "mean",str(r["original_exact_orbit_mean"]),flush=True)

    def test_02_original_W38_mixed_B_C_D6_full_source_fiber_60representatives(self):
        model,pts,selected=original_B_C_D6_mixed_fixture(3)
        r=original_point_A_fiber(model,pts)
        self.assertEqual((r["s"],r["V"]),(8,585))
        self.assertEqual(r["true_original_incidence_Q_count"],9**6)
        self.assertGreaterEqual(r["source_class_counts"].get("B",0),1)
        self.assertGreaterEqual(r["source_class_counts"].get("C",0),1)
        self.assertGreaterEqual(r["source_class_counts"].get("A_physical_C6",0),1)
        s,V,a,inc,f,g,_,_=_original_source(model)
        orbit,_=original_cycle_orbit(f,pts)
        representatives={}
        for i,key in enumerate(orbit):
            representatives.setdefault(key,i)
        self.assertEqual(len(representatives),60)
        ix=tuple(representatives.values())
        selected_perms=tuple(PERMS[j] for j in ix)
        literal=direct_original_historical_fiber_orbit(
            model,pts,r["eligible_actual_original_Q"],selected_perms)
        self.assertEqual(literal,tuple(r["orbit_scores"][j] for j in ix))
        self.assertEqual(Fraction(sum(literal),60),r["original_exact_orbit_mean"])
        self.assertEqual(Fraction(sum(v*v for v in literal),60),
                         r["original_exact_orbit_second_moment"])
        print("AA4CI_ORIGINAL_W38_MIXED","source_class",r["source_class_counts"],
              "active_cycles",r["active_cyclic_dual_types"],
              "baseline",r["original_baseline_B_C_weighted"],
              "mean",str(r["original_exact_orbit_mean"]),flush=True)

    def test_03_original_W32_K6_lex_S72_six_source_point_fiber(self):
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            inverse={edge:i for i,edge in enumerate(f)}
            pts=tuple(inverse[edge] for edge in SIX_CYCLE)
            r=original_point_A_fiber(model,pts)
            self.assertEqual(r["true_original_incidence_Q_count"],3**6)
            self.assertEqual(len(r["orbit_scores"]),720)
            direct=direct_original_historical_fiber_orbit(
                model,pts,r["eligible_actual_original_Q"],PERMS)
            self.assertEqual(direct,r["orbit_scores"])
            for Q,typ,cycle in r["eligible_actual_original_Q"]:
                self.assertEqual(
                    classify_seven_all_a_original_Q(Q,f,g,inc),
                    classify_seven_prechecked(Q,f,g,inc))
            print("AA4CI_W32_OLDCLASSIFIER",scheme,
                  "right",r["source_class_counts"],
                  "baseline",r["original_baseline_B_C_weighted"],
                  "nonzero_orbit",sum(x>0 for x in direct),flush=True)

    def test_04_original_AA4CH_fan_12positive_708zero_global_POINT_maps(self):
        for h in (2,3):
            r=original_D6_fan_orbit(h)
            z=original_maximal_D6_fan(h)
            self.assertEqual(r["fan_size"],(1<<h)+1)
            self.assertEqual(r["positive_global_f_orbit_maps"],12)
            self.assertEqual(r["zero_global_f_orbit_maps"],708)
            self.assertEqual(r["weighted_fan_original_orbit_mean"],
                             Fraction(W_D*((1<<h)+1),60))
            s,V,a,inc,f,g,_,_=_original_source(z["normal_model"])
            direct=[]
            for perm in PERMS:
                changed=complete_original_f_orbit(f,z["point_ids"],perm)
                flags=sum(classify_seven_all_a_original_Q(Q,changed,g,inc)=="D6"
                          for Q in z["fan"])
                self.assertIn(flags,(0,s+1))
                direct.append(flags)
            self.assertEqual(direct.count(s+1),12)
            self.assertEqual(direct.count(0),708)
            print("AA4CI_ORIGINAL_ALLH_FAN_ORBIT","s",s,
                  "true_original_D6_fan",s+1,
                  "whole_f_maps_with_all_fan_D6",12,
                  "whole_f_maps_with_NO_fan_GF5",708,flush=True)

    def test_05_permutation_cycle_orbit_guard_and_disconnected_left(self):
        model,pts,sel=original_B_C_D6_mixed_fixture(2)
        s,V,a,inc,f,g,_,_=_original_source(model)
        by_perm,mult=original_cycle_orbit(f,pts)
        self.assertEqual(len(by_perm),720)
        self.assertEqual(len(mult),60)
        self.assertEqual(set(mult.values()),{12})
        x=tuple((0,1),(1,2)) if False else ()
        bad_edges=((0,1),(1,2),(0,2),(3,4),(4,5),(3,5))
        self.assertIsNone(_six_position_dual_cycle(bad_edges))
        bad=_full_pair_injection(V,a,dict(zip(pts,bad_edges)))
        modified=dict(model,left_labels=bad)
        with self.assertRaises(ValueError):
            original_point_A_fiber(modified,pts)
        with self.assertRaises(ValueError):
            original_point_A_fiber(model,pts[:5])
        with self.assertRaises(ValueError):
            original_point_A_fiber(model,pts[:5]+pts[:1])
        with self.assertRaises(ValueError):
            complete_original_f_orbit(f,pts,(0,1,2,3,3,5))
        with self.assertRaises(ValueError):
            complete_original_f_orbit(f,pts,(0,1,2,3,4))
        with self.assertRaises(ValueError):
            complete_original_f_orbit(f,pts,(0,1,2,3,4,6))


if __name__=="__main__":
    unittest.main()
