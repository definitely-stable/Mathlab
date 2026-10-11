"""B8-I independent K4 global-injection tree coverage, replay and forgery gates."""
from copy import deepcopy
from itertools import combinations,permutations
import unittest

from hyp105_g5e2b3e1c24b8i_global_cover_replay import build_cover,replay_cover
from hyp105_g5e2b3e1c24b8h_joint_source_cylinder import (
    joint_cylinder_certificate,
)

EDGES=tuple(combinations(range(4),2))


def score_a(assignment):
    score=0
    for i,j in combinations(range(len(assignment)),2):
        e,f=EDGES[assignment[i]],EDGES[assignment[j]]
        if set(e)&set(f):
            score+=(i+2*j)%5+1
    return score


def score_b(assignment):
    # Independent bitmask physical-intersection implementation.
    images={i:(1<<EDGES[e][0])|(1<<EDGES[e][1])
            for i,e in assignment.items()}
    return sum((i+2*j)%5+1 for i,j in combinations(range(len(assignment)),2)
               if images[i]&images[j])


def local_source(records,payload,assignment):
    i,j,kind=payload
    adjacent=bool(set(EDGES[assignment[i]])&set(EDGES[assignment[j]]))
    return adjacent if kind=="adj" else not adjacent


def true_weighted_score(records):
    def evaluate(assignment):
        return sum(weight*int(local_source(records,payload,assignment))
                   for support,weight,payload in records)
    return evaluate


class GlobalCoverReplayTests(unittest.TestCase):
    def test_all_6p4_360_global_injections_replayed_without_missing_branches(self):
        n,m=4,6
        c=build_cover(n,m,{},(0,1,2,3),score_a,max_nodes=600,max_leaves=400)
        result=replay_cover(c,score_b,max_nodes=600,max_leaves=400)
        expected=min(score_b(dict(enumerate(image)))
                     for image in permutations(range(m),n))
        self.assertEqual(result["exact_cylinder_minimum"],expected)
        self.assertEqual(result["whole_global_injection_leaf_count"],360)
        self.assertTrue(result["global_branch_coverage_verified"])
        self.assertFalse(result["has_pruned_subtrees"])
        self.assertFalse(result["NO_all_h_unpinned_omega_s6_conclusion"] is False)

    def test_full_k4_bijection_720_globally_coherent_leaf_scores(self):
        c=build_cover(6,6,{},tuple(range(6)),score_a,
                      max_nodes=2000,max_leaves=800)
        r=replay_cover(c,score_b,max_nodes=2000,max_leaves=800)
        self.assertEqual(r["whole_global_injection_leaf_count"],720)
        self.assertEqual(r["exact_cylinder_minimum"],
                         min(score_b(dict(enumerate(images)))
                             for images in permutations(range(6))))

    def test_real_pointwise_source_bound_can_prune_entire_k4_root(self):
        records=(((0,1),2,(0,1,"adj")),
                 ((0,1),3,(0,1,"dis")))
        src=true_weighted_score(records)
        def exact_support_floor(pinned):
            cert=joint_cylinder_certificate(
                records,pinned,4,6,
                lambda payload,mapping:local_source(records,payload,mapping),
                max_union_support=2,include_exact=False,
                max_group_states=100,max_record_evaluations=1000)
            return cert["coupled_pointwise_seven_lower"]
        c=build_cover(4,6,{},(0,1,2,3),src,threshold=2,
                      floor=exact_support_floor,floor_max_depth=0)
        verified=replay_cover(c,src,floor=exact_support_floor)
        self.assertTrue(verified["positive_threshold_proven"])
        self.assertTrue(verified["has_pruned_subtrees"])
        self.assertEqual(verified["pruned_subtree_count"],1)
        self.assertEqual(verified["whole_global_injection_leaf_count"],0)
        self.assertEqual(verified["certified_cylinder_score_lower"],2)
        self.assertIsNone(verified["exact_cylinder_minimum"])
        self.assertEqual(min(src(dict(enumerate(x)))
                             for x in permutations(range(6),4)),2)

    def test_constrained_partial_right_cylinder_is_fully_covered(self):
        pins={0:4,2:1}
        order=(3,1)
        c=build_cover(4,6,pins,order,score_a,max_nodes=40,max_leaves=20)
        result=replay_cover(c,score_b,max_nodes=40,max_leaves=20)
        expected=min(score_b({**pins,3:x,1:y})
                     for x,y in permutations(
                         tuple(e for e in range(6) if e not in pins.values()),2))
        self.assertEqual(result["exact_cylinder_minimum"],expected)
        self.assertEqual(result["whole_global_injection_leaf_count"],12)

    def test_tampered_branch_missing_edge_and_leaf_score_fail_closed(self):
        c=build_cover(4,6,{0:0,1:1},(2,3),score_a,max_nodes=40,max_leaves=20)
        with self.assertRaisesRegex(ValueError,"edge cover"):
            forged=deepcopy(c)
            forged["tree"]["children"].pop()
            replay_cover(forged,score_b)
        with self.assertRaisesRegex(ValueError,"edge cover"):
            forged=deepcopy(c)
            forged["tree"]["children"][1]["edge"]=forged["tree"]["children"][0]["edge"]
            replay_cover(forged,score_b)
        with self.assertRaisesRegex(ValueError,"score does not reproduce"):
            forged=deepcopy(c)
            forged["tree"]["children"][0]["node"]["children"][0]["node"]["score"]+=1
            replay_cover(forged,score_b)
        with self.assertRaisesRegex(ValueError,"count mismatch"):
            forged=deepcopy(c)
            forged["builder_counts"]["leaves"]+=1
            replay_cover(forged,score_b)

    def test_forged_prune_rejected_and_finite_search_budgets(self):
        records=(((0,1),2,(0,1,"adj")),
                 ((0,1),3,(0,1,"dis")))
        src=true_weighted_score(records)
        floor=lambda pins:joint_cylinder_certificate(
            records,pins,4,6,
            lambda payload,assignment:local_source(records,payload,assignment),
            max_union_support=2,include_exact=False,
            max_group_states=100)["coupled_pointwise_seven_lower"]
        c=build_cover(4,6,{},(0,1,2,3),src,threshold=2,floor=floor)
        with self.assertRaisesRegex(ValueError,"insufficient"):
            fake=deepcopy(c)
            fake["tree"]["bound"]=1
            replay_cover(fake,src,floor=floor)
        with self.assertRaisesRegex(ValueError,"unauthorized"):
            replay_cover(c,src)
        with self.assertRaisesRegex(ValueError,"leaf budget"):
            build_cover(4,6,{},(0,1,2,3),score_a,max_nodes=1000,max_leaves=10)
        with self.assertRaisesRegex(ValueError,"order"):
            build_cover(4,6,{},(0,1,1,3),score_a)
        with self.assertRaises(ValueError):
            build_cover(4,6,{0:0,1:0},(2,3),score_a)

if __name__=="__main__":
    unittest.main()
