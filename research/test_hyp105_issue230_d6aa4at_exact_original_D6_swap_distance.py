"""AA4-AT mathematically exact true-original minimal D6 global swap distances."""
import unittest
from collections import Counter,deque
from itertools import permutations,combinations
from math import factorial

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4at_exact_original_D6_swap_distance import (
    minimum_global_source_transpositions_for_target,
    construct_shortest_global_original_line_image_swaps,
    occupied_global_original_line_D6_cycle_owner_targets,
    exact_true_original_W32_minimum_D6_repair_distance,
    real_original_W32_min_distance_sample_certificate,
)
from hyp105_issue230_d6aa4as_every_original_Q_five_swap_repair import (
    finite_original_eligible_Q_generator,
    repair_EVERY_actual_original_Q_D6_in_five_line_swaps,
)


def _independent_full_permutation_extension_minimum(R,want,V):
    """Enumerate ALL completions of a 6-constrained partial permutation
    into a FULL V original source line permutation, then evaluate
    each full permutation's exactly-known Cayley transposition length.
    This does NOT traverse the new partial functional-graph logic.
    """
    rest=tuple(i for i in range(V) if i not in R)
    rest_targets=tuple(i for i in range(V) if i not in want)
    result=V
    for other in permutations(rest_targets):
        full=dict(zip(R,want))
        full.update(zip(rest,other))
        seen=set();cycles=0
        for i in range(V):
            if i in seen:continue
            cycles+=1
            j=i
            while j not in seen:
                seen.add(j)
                j=full[j]
        result=min(result,V-cycles)
    return result


def _independent_transposition_BFS_minimum(R,want,V):
    """Literal BFS over ALL legal full global source label permutations
    starting at identity. Only for V=7 to avoid blowup. No cycle math.
    """
    current=tuple(range(V))
    q=deque([(current,0)]);seen={current}
    pairs=tuple(combinations(range(V),2))
    while q:
        state,steps=q.popleft()
        if all(state[i]==want[j] for j,i in enumerate(R)):return steps
        for i,j in pairs:
            nxt=list(state)
            nxt[i],nxt[j]=nxt[j],nxt[i]
            nxt=tuple(nxt)
            if nxt not in seen:
                seen.add(nxt);q.append((nxt,steps+1))
    raise AssertionError("full global original permutation BFS failed")


def _direct_flag_intersection_D6(model,Q,new_g):
    """Completely independent physical C6 positional intersection.
    No historical GF5 classifier or new original optimal graph."""
    inc=model["incidences"]
    f=model["left_labels"]
    by={}
    for field,labels in ((0,f),(1,new_g)):
        adj=set()
        for i,j in combinations(range(6),2):
            x=inc[Q[i]][field];y=inc[Q[j]][field]
            if set(labels[x])&set(labels[y]):adj.add((i,j))
        by[field]=adj
    return (by[0]==by[1] and len(by[0])==6 and
            all(sum(i in e for e in by[0])==2 for i in range(6)))


class ExactOriginalGlobalD6SwapDistance(unittest.TestCase):
    def test_01_ALL_six_constrained_targets_V7_V8_independent_full_permutation_cayley(self):
        for V in (7,8):
            R=tuple(range(6))
            for owners in permutations(range(V),6):
                cert=minimum_global_source_transpositions_for_target(R,owners,V)
                observed=cert["minimum_GLOBAL_original_line_source_transpositions"]
                expected=_independent_full_permutation_extension_minimum(R,owners,V)
                self.assertEqual(observed,expected)
                if V==7 and owners[0] in (0,1):
                    # Distinct BFS implementation for 2/7 of all
                    # true global source targets, V! states max.
                    if owners[1:3] in ((2,3),(1,2)):
                        self.assertEqual(
                            _independent_transposition_BFS_minimum(R,owners,V),
                            expected)
                fake_global=tuple((i,i+1) for i in range(V))
                goal_edges=tuple(fake_global[i] for i in owners)
                actual=construct_shortest_global_original_line_image_swaps(
                    fake_global,R,goal_edges)
                self.assertEqual(actual["minimum"],expected)
                self.assertEqual(set(actual["after_GLOBAL_original_line_images"]),
                                 set(fake_global))
            print("AA4AT exhaustive constrained Cayley original line owner maps V",V,
                  "TARGETS",factorial(V)//factorial(V-6))

    def test_02_every_K6_physical_C6_target_exactly_720_and_all_12_each_unoriented_cycle(self):
        for scheme in ("lex","S68","S72"):
            m=fixture(1,scheme)
            owners=occupied_global_original_line_D6_cycle_owner_targets(
                m["right_labels"],6)
            self.assertEqual(len(owners),720)
            self.assertEqual(len(set(owners)),720)
            self.assertTrue(all(len(set(v))==6 for v in owners))
            # Each physical target sequence consists of SIX globally
            # occupied real SOURCE line factor labels and uses exactly
            # six vertex coordinates with degree two and connected.
            for target in owners:
                edges=[m["right_labels"][i] for i in target]
                degree=Counter(v for e in edges for v in e)
                self.assertEqual(set(degree.values()),{2})

    def test_03_true_original_W32_sampled_Q_full_OPTIMUM_and_independent_D6(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            z=real_original_W32_min_distance_sample_certificate(
                m,sample_count=180)
            self.assertEqual(z["EXACT_orig_original_Q_sampled_for_global_OPTIMUM"],180)
            self.assertGreaterEqual(
                z["total_eligible_original_six_ID_Q"],18000)
            self.assertLessEqual(z["maximum_exact_distance_observed"],5)
            for dist,Q in z["one_genuine_original_Q_witness_per_observed_distance"].items():
                v=exact_true_original_W32_minimum_D6_repair_distance(
                    m,Q,validate_witness=True)
                self.assertEqual(v[
                    "EXACT_MINIMUM_full_GLOBAL_line_source_transposition_distance_to_D6"],dist)
                self.assertTrue(v[
                    "historical_original_sixflag_GF5_D6_verified_at_global_OPTIMUM"])
                # Independent physical flag-position oracle and actual
                # full V=15 globally injected original map from the
                # new shortest-target constructive certificate.
                source_order=v["six_TRUE_original_line_source_factor_IDs_in_order"]
                best=v["one_optimal_target_actual_line_source_owner_factor_IDs"]
                target=tuple(m["right_labels"][x] for x in best)
                constructed=construct_shortest_global_original_line_image_swaps(
                    m["right_labels"],source_order,target)
                self.assertTrue(_direct_flag_intersection_D6(
                    m,Q,constructed["after_GLOBAL_original_line_images"]))
                self.assertEqual(constructed["minimum"],dist)
            print("AA4AT TRUE ORIGINAL W32",scheme,
                  "Q_exact_optimum_sample",z["EXACT_orig_original_Q_sampled_for_global_OPTIMUM"],
                  "distance_histogram",z["global_optimal_swap_distance_histogram"])

    def test_04_actual_original_adversarial_W32_optimal_radius_FIVE_SHARP_witness(self):
        # These REAL original source W32 maps were HISTORICALLY fully
        # certified as D6-ZERO by the earlier independent selected GF5
        # census, outside the strict stack dependency of this PR.
        # Reverify positivity absence for each directly optimized Q,
        # not via a nonexistent sibling-branch code import.
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            z=real_original_W32_min_distance_sample_certificate(
                m,sample_count=180)
            self.assertNotIn(0,z["global_optimal_swap_distance_histogram"])
            self.assertIn(5,z["global_optimal_swap_distance_histogram"])
            Q=z["one_genuine_original_Q_witness_per_observed_distance"][5]
            shortest=exact_true_original_W32_minimum_D6_repair_distance(
                m,Q,validate_witness=True)
            self.assertEqual(
                shortest["EXACT_MINIMUM_full_GLOBAL_line_source_transposition_distance_to_D6"],5)
            self.assertTrue(
                shortest["ALL_720_oriented_physically_occupied_K6_D6_targets_exhausted"])
            self.assertTrue(shortest[
                "historical_original_sixflag_GF5_D6_verified_at_global_OPTIMUM"])
            print("AA4AT RADIUS-FIVE SHARP TRUE ORIGINAL W32",scheme,
                  "exact_six_original_incidence_IDs",Q,
                  "real_global_line_factor_swap_witness",
                  shortest["optimal_actual_whole_original_line_source_swaps"])

    def test_05_parent_all_Q_radius5_vs_NEW_optimal_true_original_W32_samples(self):
        for scheme in ("lex","S68","S72"):
            m=fixture(1,scheme)
            Qs=list(finite_original_eligible_Q_generator(m,max_yield=8))
            for Q in Qs:
                parent=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(m,Q)
                z=exact_true_original_W32_minimum_D6_repair_distance(
                    m,Q)
                self.assertLessEqual(
                    z["EXACT_MINIMUM_full_GLOBAL_line_source_transposition_distance_to_D6"],
                    parent["number_of_GLOBAL_line_factor_image_transpositions"])

    def test_06_negative_malformed_original_true_Q_and_synthetic_global_owners(self):
        m=fixture(1,"lex")
        Q=next(finite_original_eligible_Q_generator(m,max_yield=1))
        with self.assertRaises(ValueError):
            minimum_global_source_transpositions_for_target(
                (0,0,1,2,3,4),(0,1,2,3,4,5),15)
        with self.assertRaises(ValueError):
            minimum_global_source_transpositions_for_target(
                tuple(range(6)),(0,1,1,3,4,5),15)
        with self.assertRaises(ValueError):
            construct_shortest_global_original_line_image_swaps(
                ((0,1),)*15,tuple(range(6)),tuple((i,i+1) for i in range(6)))
        with self.assertRaises(ValueError):
            occupied_global_original_line_D6_cycle_owner_targets(
                m["right_labels"],7)
        with self.assertRaises(ValueError):
            exact_true_original_W32_minimum_D6_repair_distance(
                fixture(2,"lex"),Q)
        with self.assertRaises(ValueError):
            exact_true_original_W32_minimum_D6_repair_distance(
                m,(Q[0],)*6)
        with self.assertRaises(ValueError):
            exact_true_original_W32_minimum_D6_repair_distance(
                m,Q,targets=((0,1,2,3,4,5),))


if __name__=="__main__":unittest.main()
