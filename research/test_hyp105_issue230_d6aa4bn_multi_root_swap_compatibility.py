"""AA4-BN: independent exact optimum via exhaustive small permutations and real GQ."""
import unittest
from collections import Counter
from itertools import combinations,permutations
from random import Random

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    original_fixed_pair_repair_cherry_four_swaps,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4bn_multi_root_swap_compatibility import (
    optimal_prescribed_global_swaps,
    original_multi_cherry_candidate_minimum,
    candidate_from_target,
)


def brute_cayley_distance(x):
    # Independent permutation cycle count, not the partial matching formula.
    n=len(x)
    seen=set()
    cycles=0
    for start in range(n):
        if start in seen: continue
        cycles+=1
        cur=start
        while cur not in seen:
            seen.add(cur)
            cur=x[cur]
    return n-cycles


def independently_exhaust_minimum(n, constraints, pins):
    valid=[]
    for permutation in permutations(range(n)):
        if any(permutation[i]!=i for i in pins):
            continue
        if all(permutation[i]==v for i,v in constraints.items()):
            valid.append(brute_cayley_distance(permutation))
    return min(valid) if valid else None


class AA4BNMultiRootOptimalMatching(unittest.TestCase):
    def test_01_exhaustive_small_Sn_independent_minima(self):
        rng=Random(170230)
        for n in (4,5,6):
            original=tuple((i,i+n) for i in range(n))
            for trial in range(150):
                protected=tuple(sorted(rng.sample(range(n),rng.randrange(0,min(2,n)+1))))
                free=[i for i in range(n) if i not in protected]
                k=rng.randrange(0,len(free)+1)
                sources=rng.sample(free,k)
                # A genuinely arbitrary partial injective prescription,
                # including paths, closed cycles and fixed points.
                targets=rng.sample(free,k)
                root1=tuple((i,original[v]) for i,v in zip(sources[::2],targets[::2]))
                root2=tuple((i,original[v]) for i,v in zip(sources[1::2],targets[1::2]))
                z=optimal_prescribed_global_swaps(original,(root1,root2),protected)
                expected=independently_exhaust_minimum(
                    n,dict(zip(sources,targets)),protected)
                self.assertEqual(z["exact_minimum_image_transpositions"],expected)
                self.assertEqual(len(z["actual_shortest_global_transpositions"]),expected)
                current=list(original)
                for i,j in z["actual_shortest_global_transpositions"]:
                    self.assertNotIn(i,protected)
                    self.assertNotIn(j,protected)
                    current[i],current[j]=current[j],current[i]
                    self.assertEqual(tuple(current[p] for p in protected),
                                     tuple(original[p] for p in protected))
                    self.assertEqual(len(set(current)),n)
                self.assertEqual(tuple(current),z["final_full_global_map"])

    def test_02_two_root_shared_matching_cycle_savings(self):
        original=tuple((i,i+10) for i in range(10))
        groups=(
            ((2,original[3]),(4,original[5])),
            ((3,original[2]),(6,original[7]),(7,original[6]))
        )
        z=optimal_prescribed_global_swaps(original,groups,(0,1))
        self.assertEqual(z["number_nontrivial_arcs"],5)
        self.assertEqual(z["number_nontrivial_closed_cycles"],2)
        self.assertEqual(z["exact_minimum_image_transpositions"],3)
        self.assertEqual(len(z["closed_source_owner_cycles"]),2)
        self.assertEqual(z["final_full_global_map"][2],original[3])
        self.assertEqual(z["final_full_global_map"][3],original[2])
        # Open paths and fixed source requests handled without false cycles.
        path=optimal_prescribed_global_swaps(original,
            (((2,original[3]),),((3,original[4]),)),(0,1))
        self.assertEqual(path["exact_minimum_image_transpositions"],2)
        self.assertEqual(len(path["open_source_owner_paths"]),1)

    def test_03_candidate_specific_cross_root_conflicts(self):
        original=tuple((i,i+12) for i in range(6))
        cases=[
            (((2,original[3]),),((2,original[4]),)), # same source conflict
            (((2,original[3]),),((4,original[3]),)), # distinct sources one target
            (((2,original[0]),),),                   # fixed image stolen
            (((0,original[3]),),),                   # protected source changed
        ]
        for groups in cases:
            with self.assertRaises(ValueError):
                optimal_prescribed_global_swaps(original,groups,(0,1))
        with self.assertRaises(ValueError):
            optimal_prescribed_global_swaps(original,(((2,(99,100)),),))
        with self.assertRaises(ValueError):
            optimal_prescribed_global_swaps((original[0],)*6,())
        with self.assertRaises(ValueError):
            optimal_prescribed_global_swaps(original,(((True,original[2]),),))
        self.assertEqual(optimal_prescribed_global_swaps(original,(),(0,1))[
            "exact_minimum_image_transpositions"],0)

    def test_04_genuine_original_W32_each_root_optimal_vs_BM(self):
        for name,model in (("dual_zero",zero_split_original_W32()),)+tuple(
            (key,fixture(1,key)) for key in ("lex","reverse","S68","S72")):
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            for side,by in ((0,byP),(1,byL)):
                checked=0
                for source in range(V):
                    for flags in combinations(by[source],2):
                        w=original_fixed_pair_repair_cherry_four_swaps(
                            model,side,source,flags,require_regular=False)
                        if w is None:continue
                        Q=w["same_six_REAL_original_incidence_IDs"]
                        repaired=w["original_global_opposite_map_after"]
                        target=tuple(sorted({repaired[inc[j][1-side]] for j in Q}))
                        candidate=candidate_from_target(model,side,source,flags,Q,target)
                        # Re-use exactly the source-ID assignments of the
                        # PARENT feasible global repaired map, not fabricate Q.
                        free={inc[j][1-side] for j in Q}-{inc[j][1-side] for j in flags}
                        candidate["free_assignments"]=tuple(
                            (i,repaired[i]) for i in sorted(free))
                        z=original_multi_cherry_candidate_minimum(model,side,(candidate,))
                        self.assertLessEqual(z["exact_minimum_image_transpositions"],
                                             w["number_global_source_FACTOR_swaps"])
                        self.assertEqual(z["accepted_original_seven_GF5_tags"],
                                         ("B-left/A-right" if side==0 else "A-left/B-right",))
                        self.assertEqual(set(z["final_full_global_map"]),set((g,f)[side]))
                        checked+=1
                        if checked==4: break
                    if checked==4: break
                self.assertEqual(checked,4)

    def test_05_actual_W32_two_distinct_original_cherries_one_map(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        roots=[]
        for p in range(V):
            for flags in combinations(byP[p],2):
                w=original_fixed_pair_repair_cherry_four_swaps(
                    model,0,p,flags,require_regular=False)
                if w is not None:
                    roots.append((p,flags,w))
            if roots:break
        self.assertTrue(roots)
        p,flags,w=roots[0]
        repaired=w["repaired_full_true_original_model"]
        old_opp=tuple(g)
        new_opp=tuple(repaired["right_labels"])
        q1=w["same_six_REAL_original_incidence_IDs"]
        census=seven_census(repaired,independent_checks=False,witness_sets=True)
        pair=None
        for q2,tag in census["sets"].items():
            if tag!="B-left/A-right" or tuple(q2)==tuple(q1):
                continue
            counts=Counter(inc[j][0] for j in q2)
            repeated=[p2 for p2,n in counts.items() if n==2]
            if len(repeated)!=1:continue
            p2=repeated[0]
            if p2==p:continue
            flags2=tuple(j for j in q2 if inc[j][0]==p2)
            if len(flags2)!=2:continue
            if any(old_opp[inc[j][1]]!=new_opp[inc[j][1]] for j in flags2):
                continue
            pair=(p2,flags2,tuple(q2))
            break
        self.assertIsNotNone(pair,"requires independent second original rooted B/A witness")
        p2,flags2,q2=pair
        candidates=[]
        for root,fl,Q in ((p,flags,q1),(p2,flags2,q2)):
            target=tuple(sorted({new_opp[inc[j][1]] for j in Q}))
            z=candidate_from_target(model,0,root,fl,Q,target)
            free={inc[j][1] for j in Q}-{inc[j][1] for j in fl}
            z["free_assignments"]=tuple((i,new_opp[i]) for i in sorted(free))
            candidates.append(z)
        z=original_multi_cherry_candidate_minimum(model,0,candidates)
        self.assertLessEqual(z["exact_minimum_image_transpositions"],4)
        self.assertEqual(len(z["accepted_original_seven_GF5_tags"]),2)
        self.assertTrue(z["same_new_original_full_global_map_satisfies_EVERY_given_certificate"])

    def test_06_real_original_W34_and_invalid_genuine_sixID_targets(self):
        model=fixture(2,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        for side,by in ((0,byP),(1,byL)):
            found=False
            for p in (0,7,37,84):
                for flags in combinations(by[p],2):
                    w=original_fixed_pair_repair_cherry_four_swaps(
                        model,side,p,flags,require_regular=False)
                    if w is None:continue
                    Q=w["same_six_REAL_original_incidence_IDs"]
                    opp=w["original_global_opposite_map_after"]
                    target=tuple(sorted({opp[inc[j][1-side]] for j in Q}))
                    candidate=candidate_from_target(model,side,p,flags,Q,target)
                    free={inc[j][1-side] for j in Q}-{inc[j][1-side] for j in flags}
                    candidate["free_assignments"]=tuple((i,opp[i]) for i in sorted(free))
                    z=original_multi_cherry_candidate_minimum(model,side,(candidate,))
                    self.assertLessEqual(z["exact_minimum_image_transpositions"],4)
                    corrupt=dict(candidate,Q=tuple([Q[0]]*6))
                    with self.assertRaises(ValueError):
                        original_multi_cherry_candidate_minimum(model,side,(corrupt,))
                    found=True
                    break
                if found:break
            self.assertTrue(found)


if __name__=="__main__":
    unittest.main()
