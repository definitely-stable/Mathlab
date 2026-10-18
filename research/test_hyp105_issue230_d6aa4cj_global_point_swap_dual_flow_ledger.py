"""AA4-CJ all-h original two-source-factor swap law + independent W32 7class census."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4cj_global_point_swap_dual_flow_ledger import (
    original_two_point_global_swap,literal_original_point_six_vertex_2factor,
    original_point_source_kind, original_true_Q_swap_transition,
    true_original_W32_sevenclass_global_point_swap_ledger,
    original_swap_W34_point_A_fiber_falsifiers,
    GF5_WEIGHTS,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    original_B_C_D6_mixed_fixture,
)
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    original_maximal_D6_fan, SIX_CYCLE,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def independent_original_full_W32_7class_census(model):
    """Separate actual ORIGINAL Q loop; no swap-ledger decomposition."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("independent original all-seven full W32 only")
    classcounts=Counter()
    qcount=0
    for Q,_ in selected_left_six(model):
        tag=classify_seven_prechecked(Q,f,g,inc)
        if tag is not None:
            classcounts[tag]+=1
        qcount+=1
    if qcount!=62370:
        raise AssertionError("not all original left 6vertex eligible sixflag IDs")
    return sum(GF5_WEIGHTS[tag]*count for tag,count in classcounts.items()),classcounts


def point_factor_for_physical_edge(f,edge):
    inv={tuple(e):i for i,e in enumerate(f)}
    return inv[tuple(edge)]


def independent_original_single_source_phys_Q(model,p,q):
    """Search actual 6 POINT source factor C6 containing p but not q.

    Does not use the ledger. Its chosen six true incidence IDs are
    independently obtained from original W34/W38 source POINT stars.
    """
    s,V,a,inc,f,g,by_point,_=_original_source(model)
    f=tuple(f)
    e=f[p]
    adj=[[] for _ in range(a)]
    for src,edge in enumerate(f):
        if src in (p,q):continue
        u,v=edge
        adj[u].append((v,src));adj[v].append((u,src))
    def dfs(u,target,used_vertices,sources):
        if len(sources)==5:
            return sources if u==target else None
        for nxt,src in adj[u]:
            if (len(sources)==4 and nxt!=target) or (
                len(sources)<4 and nxt in used_vertices
            ):
                continue
            if nxt==target and len(sources)<4:continue
            result=dfs(nxt,target,used_vertices|{nxt},sources+(src,))
            if result is not None:return result
        return None
    path=dfs(e[0],e[1],{e[0]},())
    if path is None:raise AssertionError("full original occupied source f support lacked p-only physical C6")
    points=(p,)+path
    if len(set(points))!=6 or q in points:
        raise AssertionError("source C6 original POINT factors malformed")
    Q=tuple(sorted(by_point[point][0] for point in points))
    if not literal_original_point_six_vertex_2factor(Q,inc,f):
        raise AssertionError("independent original physical C6 finder did not find true Q")
    return Q


class AA4CJTrueOriginalGlobalPointSwap(unittest.TestCase):
    def test_01_W32_lex_full_original_sevenclass_global_swap_and_signed_ledger(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        p=point_factor_for_physical_edge(f,(0,1))
        q=point_factor_for_physical_edge(f,(2,3))
        z=true_original_W32_sevenclass_global_point_swap_ledger(model,p,q)
        self.assertEqual(z["global_weighted_all7_before"],11225795)
        self.assertEqual(z["global_weighted_all7_after"],9748767)
        self.assertEqual(z["global_weighted_all7_delta"],-1477028)
        self.assertEqual(z["original_union_left_Q_candidates"],88236)
        self.assertEqual(z["original_A_sector_weighted_delta"],{
            "A_neither":0,"A_both":-11286,"A_exactly_one":-745332})
        self._assert_full_ledger_independent(z,model,p,q)
        self.assertGreater(z["independent_W32_vs_generalized_classifier_Q_count"],62000)
        self.assertTrue(any(key[0]=="A" for key in z["source_sector_positive_candidate_counts"]))
        self.assertEqual(z["original_A_sector_weighted_delta"].get("A_neither",0),0)
        self.assertEqual(z["original_A_sector_weighted_delta"].get("A_both",0)%GF5_WEIGHTS["D6"],0)
        self.assertNotEqual(z["global_weighted_all7_delta"],0)
        print("AA4CJ_W32_LEX",z["original_union_left_Q_candidates"],
              "ALLSEVEN",(z["global_weighted_all7_before"],z["global_weighted_all7_after"]),
              "source_weighted_flux",z["all_source_sector_weighted_delta"],
              "A",z["original_A_sector_weighted_delta"],flush=True)

    def test_02_W32_S72_and_disjoint_other_pointpair_signed_ledger(self):
        for scheme in ("S72","lex"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            p=point_factor_for_physical_edge(f,(1,2))
            q=point_factor_for_physical_edge(f,(4,5))
            z=true_original_W32_sevenclass_global_point_swap_ledger(model,p,q)
            if scheme=="S72":
                self.assertEqual(z["global_weighted_all7_before"],3283610)
                self.assertEqual(z["global_weighted_all7_after"],4747273)
                self.assertEqual(z["global_weighted_all7_delta"],1463663)
                self.assertEqual(z["original_A_sector_weighted_delta"].get("A_exactly_one"),1006563)
                self.assertEqual(z["original_A_sector_weighted_delta"].get("A_both",0),0)
            else:
                self.assertEqual(z["global_weighted_all7_before"],11225795)
                self.assertEqual(z["global_weighted_all7_after"],10799141)
                self.assertEqual(z["global_weighted_all7_delta"],-426654)
                self.assertEqual(z["original_A_sector_weighted_delta"].get("A_exactly_one"),-360240)
                self.assertEqual(z["original_A_sector_weighted_delta"].get("A_both"),11286)
            self._assert_full_ledger_independent(z,model,p,q)
            self.assertEqual(z["original_A_sector_weighted_delta"].get("A_neither",0),0)
            self.assertEqual(z["original_A_sector_weighted_delta"].get("A_both",0)%5643,0)
            print("AA4CJ_W32_OTHER_SWAP",scheme,
                  "ALLSEVEN",(z["global_weighted_all7_before"],z["global_weighted_all7_after"]),
                  "A",z["original_A_sector_weighted_delta"],flush=True)

    def _assert_full_ledger_independent(self,z,model,p,q):
        s,V,a,inc,f,g,_,_=_original_source(model)
        transformed=dict(model,left_labels=original_two_point_global_swap(f,p,q))
        old,old_tags=independent_original_full_W32_7class_census(model)
        new,new_tags=independent_original_full_W32_7class_census(transformed)
        self.assertEqual(z["original_full_left_Q_each"],62370)
        self.assertGreaterEqual(z["original_union_left_Q_candidates"],62370)
        self.assertEqual((old,new),(z["global_weighted_all7_before"],
                                    z["global_weighted_all7_after"]))
        self.assertEqual(z["global_weighted_all7_delta"],new-old)
        for tag in GF5_WEIGHTS:
            self.assertEqual(z["all_seven_original_historical_class_before"].get(tag,0),old_tags[tag])
            self.assertEqual(z["all_seven_original_historical_class_after"].get(tag,0),new_tags[tag])
        self.assertEqual(sum(z["all_source_sector_weighted_delta"].values()),new-old)
        self.assertEqual(sum(z["original_A_sector_weighted_delta"].values()),
                         sum(val for (kind,sec),val in
                             z["all_source_sector_weighted_delta"].items() if kind=="A"))
        self.assertFalse(any(a=="A" and sector=="both_equal" and
                             before==after=="D6"
                             for a,sector,before,after in
                             z["historical_GF5_migration_by_source_sector"]))

    def test_03_TRUE_original_W34_W38_one_global_swap_selected_fiber_BC_invariant_D6_exclusion(self):
        for h in (2,3):
            model,points,byclass=original_B_C_D6_mixed_fixture(h)
            s,V,a,inc,f,g,_,_=_original_source(model)
            p,q=points[0],points[2]
            summary=original_swap_W34_point_A_fiber_falsifiers(model,points,p,q)
            self.assertEqual(summary["s"],1<<h)
            # Three independently pinned ORIGINAL Q; source B/C persistent,
            # source A/D6 dual alignment before yes after NO.
            changed=original_two_point_global_swap(f,p,q)
            for name in ("B","C"):
                Q=byclass[name]
                result=original_true_Q_swap_transition(Q,inc,f,g,p,q)
                self.assertEqual(result["historical_before"],
                                 {"B":"A-left/B-right","C":"C/A"}[name])
                self.assertEqual(result["historical_after"],result["historical_before"])
            Q=byclass["D6"]
            result=original_true_Q_swap_transition(Q,inc,f,g,p,q)
            self.assertEqual(result["historical_before"],"D6")
            self.assertIsNone(result["historical_after"])
            self.assertEqual(result["sector"],"both_equal")
            self.assertEqual(result["A_sector"],"A_both")
            self.assertTrue(result["left_physical_before"])
            self.assertTrue(result["left_physical_after"])
            self.assertEqual(set(f),set(changed))
            print("AA4CJ_ORIGINAL_MIXED",s,
                  "point_A_source_class_after_global_swap",
                  summary["genuine_original_full_f_swap_class_transitions"],flush=True)

    def test_04_TRUE_original_W34_W38_exactly_one_SOURCE_only_can_never_keep_physical(self):
        for h in (2,3):
            model,points,byclass=original_B_C_D6_mixed_fixture(h)
            s,V,a,inc,f,g,_,_=_original_source(model)
            p,q=points[0],points[2]
            true_Q=independent_original_single_source_phys_Q(model,p,q)
            res=original_true_Q_swap_transition(true_Q,inc,f,g,p,q)
            self.assertEqual(res["source_point_kind"],"A")
            self.assertEqual(res["A_sector"],"A_exactly_one")
            self.assertTrue(res["left_physical_before"])
            self.assertFalse(res["left_physical_after"])
            new_model=dict(model,left_labels=original_two_point_global_swap(f,p,q))
            after_Q=independent_original_single_source_phys_Q(new_model,p,q)
            after=original_true_Q_swap_transition(
                after_Q,inc,new_model["left_labels"],g,p,q)
            # Here the baseline must actually be the swapped COMPLETE
            # original f map used to construct this real original Q.
            # A second WHOLE original POINT swap returns the first map.
            self.assertTrue(after["left_physical_before"])
            self.assertFalse(after["left_physical_after"])
            self.assertNotEqual(true_Q,after_Q)
            print("AA4CJ_ONE_PRESENT_SOURCE_W3",s,
                  "source_Q_before",true_Q,"source_Q_after",after_Q,flush=True)

    def test_05_TRUE_original_AA4CH_named_fan_and_invalid_inputs(self):
        for h in (2,3):
            z=original_maximal_D6_fan(h)
            s,V,a,inc,f,g,_,_=_original_source(z["normal_model"])
            p,q=z["point_ids"][0],z["point_ids"][2]
            for Q in z["fan"]:
                state=original_true_Q_swap_transition(Q,inc,f,g,p,q)
                self.assertEqual(state["A_sector"],"A_both")
                self.assertEqual((state["historical_before"],state["historical_after"]),
                                 ("D6",None))
                self.assertEqual(state["weighted_delta"],-5643)
                self.assertTrue(state["left_physical_after"])
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        for args in [(f,-1,0),(f,0,0),(f,True,1),(f,0,V)]:
            with self.assertRaises(ValueError):
                original_two_point_global_swap(*args)
        with self.assertRaises(ValueError):
            original_two_point_global_swap(list(f[:-1])+[f[0]],0,1)
        Q=tuple(range(6))
        with self.assertRaises(ValueError):
            original_true_Q_swap_transition((0,0,1,2,3,4),inc,f,g,0,1)
        with self.assertRaises(ValueError):
            original_true_Q_swap_transition((0,1,2,3,4,999),inc,f,g,0,1)


if __name__=="__main__":
    unittest.main()
