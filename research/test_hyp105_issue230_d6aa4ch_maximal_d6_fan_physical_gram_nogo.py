"""AA4-CH independent complete original W34/W38 maximal D6 fan referees."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    original_maximal_D6_fan, original_fan_common_physical_gram_referee,
    _full_pair_injection, _match_unique, SIX_CYCLE,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)


def independent_original_D6_sixflags(Q, f, g, incidences):
    """DIRECT physical and dual cycle oracle, not the stored GF5 tagger."""
    original=tuple(incidences[j] for j in Q)
    if len(set(Q))!=6 or len(set(p for p,l in original))!=6 or len(set(l for p,l in original))!=6:
        return False
    graph=[]
    for side,mapping in ((0,f),(1,g)):
        deg=Counter()
        dual=Counter()
        for i,flag in enumerate(original):
            for v in mapping[flag[side]]:
                deg[v]+=1
        if len(deg)!=6 or any(n!=2 for n in deg.values()):return False
        adjacency=[]
        for v in deg:
            cols=tuple(i for i,flag in enumerate(original) if v in mapping[flag[side]])
            if len(cols)!=2:return False
            adjacency.append(frozenset(cols))
        graph.append(frozenset(adjacency))
    if graph[0]!=graph[1] or len(graph[0])!=6:return False
    adj={j:set() for j in range(6)}
    for e in graph[0]:
        a,b=tuple(e)
        adj[a].add(b);adj[b].add(a)
    reached={0};stack=[0]
    while stack:
        for neighbor in adj[stack.pop()]:
            if neighbor not in reached:
                reached.add(neighbor);stack.append(neighbor)
    return len(reached)==6 and all(len(adj[j])==2 for j in range(6))


class AA4CHTrueOriginalFan(unittest.TestCase):
    def test_01_W34_maximal_original_D6_fan_and_single_point_swap_erases(self):
        z=original_maximal_D6_fan(2)
        self.assertEqual((z["s"],z["V"],z["a"]),(4,85,14))
        self.assertEqual(z["fan_size"],5)
        self.assertEqual(z["fan_weighted_original_GF5_baseline"],5*5643)
        self.assertEqual(z["fan_weighted_original_GF5_scrambled"],0)
        self.assertEqual(len(set(z["line_ids"])),14)
        self.assertEqual(len(set(z["four_shared_original_flags"])),4)
        self._independent_verify(z)
        print("AA4CH_W34_FAN",z["fan_size"],
              "original_weighted_D6",z["fan_weighted_original_GF5_baseline"],
              "scrambled_selected_fan_GF5",0,flush=True)

    def test_02_W38_maximal_original_D6_fan_and_single_point_swap_erases(self):
        z=original_maximal_D6_fan(3)
        self.assertEqual((z["s"],z["V"]),(8,585))
        self.assertEqual(z["fan_size"],9)
        self.assertEqual(z["fan_weighted_original_GF5_baseline"],9*5643)
        self.assertEqual(len(set(z["line_ids"])),22)
        self._independent_verify(z)
        print("AA4CH_W38_FAN",z["fan_size"],
              "original_weighted_D6",z["fan_weighted_original_GF5_baseline"],
              "scrambled_selected_fan_GF5",0,flush=True)

    def _independent_verify(self,z):
        model=z["normal_model"];bad=z["scrambled_model"]
        s,V,a,inc,f,g,_,_=_original_source(model)
        sb,Vb,ab,ib,fb,gb,_,_=_original_source(bad)
        self.assertEqual((s,V,a,inc,g),(sb,Vb,ab,ib,gb))
        self.assertEqual(set(f),set(fb))
        self.assertEqual(len(z["fan"]),s+1)
        all_flags=set()
        for i,Q in enumerate(z["fan"]):
            self.assertEqual(len(Q),6)
            self.assertEqual(len(set(Q)),6)
            self.assertEqual(len(set(Q)&set(z["four_shared_original_flags"])),4)
            self.assertTrue(independent_original_D6_sixflags(Q,f,g,inc))
            self.assertFalse(independent_original_D6_sixflags(Q,fb,g,inc))
            self.assertEqual(classify_seven_all_a_original_Q(Q,f,g,inc),"D6")
            self.assertIsNone(classify_seven_all_a_original_Q(Q,fb,g,inc))
            for other in z["fan"][:i]:
                self.assertEqual(len(set(Q)&set(other)),4)
            all_flags.update(Q)
        self.assertEqual(len(all_flags),4+2*(s+1))
        self.assertEqual(len(set(z["line_ids"])),len(z["line_ids"]))
        p=z["point_ids"]
        self.assertFalse(set(l for idx,(q,l) in enumerate(inc) if q==p[4])
                         & set(l for idx,(q,l) in enumerate(inc) if q==p[5]))
        self.assertTrue(all(max(coord for coord in edge)<a for edge in g))

    def test_03_same_actual_original_g_all256_physical_Gram_but_D6_changed(self):
        for h,expected in ((2,5),(3,9)):
            z=original_fan_common_physical_gram_referee(h)
            self.assertEqual(z["fan_size"],expected)
            self.assertGreater(z["shared_physical_Gram_J00"],0)
            self.assertEqual(z["independent_literal_original_joint_256_maps"],
                             z["shared_physical_Gram_J00"])
            self.assertEqual(z["before_original_center_selected_Q_tags"],("D6","D6"))
            self.assertEqual(z["scrambled_original_center_selected_Q_tags"],(None,None))
            self.assertTrue(z["identical_global_g_and_256_right_physical_Gram"])
            self.assertTrue(z["left_physical_2factor_eligibility_same"])
            self.assertTrue(z["full_original_seven_GQ_S_NOT_COMPUTED"])
            print("AA4CH_MIXED_PHYSICAL_GRAM_SAME_GF5_ERASED",
                  "s",z["s"],"fan",expected,
                  "physical_two_Q_joint",z["shared_physical_Gram_J00"],
                  "before_D6_joint_maps",z["before_original_256_joint_D6"],
                  "after_D6_joint_maps",z["after_original_256_joint_D6"],flush=True)

    def test_04_adversarial_Hall_and_invalid_fan_inputs(self):
        for a in (7,8):
            with self.assertRaises(ValueError):
                _full_pair_injection(5,a,{0:(0,1),1:(1,0)})
        with self.assertRaises(ValueError):
            _full_pair_injection(10,6,{0:(0,0)})
        with self.assertRaises(ValueError):
            _full_pair_injection(10,6,{99:(0,1)})
        # Independent literal Hall SDR positive/negative finite instances.
        matched=_match_unique(((5,6),(6,7),(5,7)))
        self.assertEqual(set(matched),{5,6,7})
        self.assertIn(matched[0],(5,6))
        self.assertIn(matched[1],(6,7))
        self.assertIn(matched[2],(5,7))
        with self.assertRaises(AssertionError):
            _match_unique(((0,), (0,)))
        for h in (1,4,0,-1,True):
            with self.assertRaises(ValueError):
                original_maximal_D6_fan(h)


if __name__=="__main__":unittest.main()
