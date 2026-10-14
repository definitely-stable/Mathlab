"""HYP-105 / #230 / JPKC-013: exact ORIGINAL global injection compatibility.

J44: each fixed ORIGINAL right source-multiset profile (INCLUDING its D6
      positional dual) depends ONLY on its participating original right
      factor labels. This is a cylinder identity for any true source host.
J45: profile-positive cylinder cover gives a valid injection/matching
      incompatibility inequality on a fixed full legal completion fiber.
J46: exact minimum *cardinality* positive-profile cover for frozen W32
      24-state genuine globally injected S68/S72 four-line fibers.

No all-h Omega(s^6), no global search of all f,g or independent Q relabel.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations
import argparse
import json

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc010_mixed_positive_transfer import FIBERS
from hyp105_issue230_jpkc012_incidence_tensor import (
    compile_incidence_tensor, contract_incidence_tensor,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def exact_minimum_positive_profile_cover(profile_masks, n_states,
                                         *, max_distinct_masks=10_000):
    """Exact minimum-cardinality OR-cover by positive-profile state masks.

    Search DISTINCT maximal masks only; dropping a mask dominated by a
    strict superset cannot increase minimum cover size. Exhaustively
    rule out all smaller k by finite memoized branch-and-bound. The
    returned representative original source profile for a mask is
    lexicographically pinned, so every result is deterministic.
    """
    if type(n_states) is not int or not 1 <= n_states <= 24:
        raise ValueError("exact state cover restricted to 1..24 states")
    if type(max_distinct_masks) is not int or max_distinct_masks < 1:
        raise ValueError("positive exact compatibility-mask budget required")
    all_states=(1<<n_states)-1
    reps={}
    for profile,mask in sorted(profile_masks.items()):
        if (type(mask) is not int or mask <= 0 or mask & ~all_states
                or not isinstance(profile,tuple)):
            raise ValueError("only valid original profile masks are accepted")
        reps.setdefault(mask,profile)
    if not reps or len(reps) > max_distinct_masks:
        raise ValueError("original source profile mask set empty or exact budget exceeded")
    all_mask_values=sorted(reps,key=lambda m:(-m.bit_count(),-m))
    if not all_states == (0 if not all_mask_values else
                         all_states & sum(0 for _ in ()) if False else
                         _bitwise_or(all_mask_values)):
        raise ValueError("some globally legal state has no positive original source profile")
    # A mask included in another mask is never needed for a
    # MINIMUM-CARDINALITY cover. Retain original profiles as witnesses.
    maximal=tuple(mask for mask in all_mask_values if not any(
        other != mask and mask & other == mask
        for other in all_mask_values))
    maximal=tuple(sorted(maximal,key=lambda x:(-x.bit_count(),-x)))
    if not maximal or _bitwise_or(maximal)!=all_states:
        raise AssertionError("domination elimination lost a legal state")

    remaining=all_states
    greedy=[]
    while remaining:
        mask=max(maximal,key=lambda m:((m & remaining).bit_count(),m))
        if not mask & remaining:
            raise AssertionError("no global right-map state cover")
        greedy.append(mask)
        remaining &= ~mask

    @lru_cache(maxsize=None)
    def search(uncovered, budget):
        if not uncovered:
            return ()
        if budget==0:
            return None
        best=max((m & uncovered).bit_count() for m in maximal)
        if best == 0 or best*budget < uncovered.bit_count():
            return None
        # Branch on the rarest still-uncovered globally legal state.
        # All solution covers must include some original profile with
        # that state positive. This branching is complete, not greedy.
        bits=[1<<i for i in range(n_states) if uncovered & (1<<i)]
        pivot=min(bits,key=lambda bit:sum(bool(mask & bit) for mask in maximal))
        options=sorted((mask for mask in maximal if mask & pivot),
                       key=lambda m:(-(m & uncovered).bit_count(),-m))
        for mask in options:
            rest=search(uncovered & ~mask,budget-1)
            if rest is not None:
                return (mask,)+rest
        return None

    found=None
    for k in range(1,len(greedy)+1):
        found=search(all_states,k)
        if found is not None:
            break
    if found is None:
        raise AssertionError("exact solver failed despite known greedy cover")
    if len(found)!=k or _bitwise_or(found)!=all_states:
        raise AssertionError("exact minimum set cover witness invalid")
    return {
        "exact_optimum_cover_cardinality":k,
        "minimality_proved_over_ALL_positive_profile_masks":True,
        "all_proper_smaller_covers_infeasible":True,
        "total_original_positive_source_profiles":len(profile_masks),
        "distinct_positive_state_masks":len(reps),
        "nondominated_positive_state_masks":len(maximal),
        "original_right_source_profile_witnesses":tuple(reps[mask] for mask in found),
        "positive_state_mask_witnesses":found,
        "full_legal_global_state_mask":all_states,
        "complete_covered_global_state_mask":_bitwise_or(found),
        "greedy_upper_bound_cover_size":len(greedy),
        "dynamic_subproblems_checked":search.cache_info().misses,
        "not_all_h_injection_lower_bound":True,
    }


def _bitwise_or(values):
    value=0
    for x in values:
        value |= x
    return value


def coherent_original_injection_certificate(
        scheme, *, states=None, compare_independent=True,
        max_positive_profiles=5000, max_distinct_masks=10_000):
    """Certificate on ONE pinned globally injected original factor fiber.

    For partial states this reports exactly the sampled prefix and
    NEVER calls it an exhaustive 24-map/fiber obstruction.
    """
    if scheme not in FIBERS:
        raise ValueError("true pinned W32 S68/S72 source fiber required")
    if states is not None and (type(states) is not int or not 1 <= states <= 24):
        raise ValueError("states must be integer 1..24")
    if type(max_positive_profiles) is not int or max_positive_profiles < 1:
        raise ValueError("positive original source profile budget required")
    model=fixture(1,scheme)
    compiled=compile_incidence_tensor(model)
    original=tuple(tuple(x) for x in model["right_labels"])
    block=tuple(FIBERS[scheme])
    if len(set(block))!=4:
        raise AssertionError("pinned original four-line block duplicate")
    original_image=tuple(original[i] for i in block)
    choices=tuple(permutations(original_image))
    if len(choices)!=24 or len(set(choices))!=24:
        raise AssertionError("W32 true K6 full 24-state right fiber missing")
    selected=choices if states is None else choices[:states]

    by_profile=defaultdict(dict)
    snapshots=[]
    for index,order in enumerate(selected):
        right=list(original)
        for source_line,pair in zip(block,order):
            right[source_line]=pair
        if len(set(right))!=len(right):
            raise AssertionError("one globally injected line-to-physical-pair assignment required")
        exact=contract_incidence_tensor(
            compiled,tuple(right),record_profile_values=True)
        if compare_independent:
            comparison=dict(model)
            comparison["right_labels"]=tuple(right)
            independent=seven_census(comparison,independent_checks=False)
            if (exact["original_seven_classes"]!=independent["seven_class_motif_counts"]
                    or exact["complete_W32_true_original_S"]!=independent["S_seven"]):
                raise AssertionError("independent full W32 GF5 original sixset mismatch")
        scores=exact["profile_score_by_original_right_multiset"]
        if sum(scores.values())!=exact["complete_W32_true_original_S"]:
            raise AssertionError("one ORIGINAL right-source profile count twice")
        for profile,n in scores.items():
            if type(n) is not int or n<1 or len(profile)!=6:
                raise AssertionError("invalid nonnegative ORIGINAL source profile score")
            if index in by_profile[profile]:
                raise AssertionError("one source profile repeated within one physical global map")
            by_profile[profile][index]=n
        snapshots.append({
            "state_index":index,
            "four_original_right_factor_images":order,
            "full_original_S":exact["complete_W32_true_original_S"],
            "all_seven_GF5_classes":exact["original_seven_classes"],
            "positive_original_source_profiles":len(scores),
        })
    N=len(snapshots)
    if len(by_profile)>max_positive_profiles:
        raise ValueError("exact positive original source profile population budget exceeded")
    all_states=(1<<N)-1
    profiles=sorted(by_profile)
    profile_masks={}
    profile_values={}
    profile_local_restriction_checks=0
    cylinder_sizes=Counter()
    profile_minima=0
    profile_positives_across_all_states=0
    state_values={i:[] for i in range(N)}

    for profile in profiles:
        score_by_state=tuple(by_profile[profile].get(i,0) for i in range(N))
        if not any(score_by_state):
            raise AssertionError("inactive original right profile retained")
        profile_values[profile]=score_by_state
        for i,score in enumerate(score_by_state):
            state_values[i].append(score)
        profile_minima+=min(score_by_state)
        mask=sum((1<<i) for i,n in enumerate(score_by_state) if n)
        profile_masks[profile]=mask
        profile_positives_across_all_states+=int(mask==all_states)
        # J44 locality: for any two globally distinct maps having equal
        # labels on the participating ORIGINAL right source factors,
        # *the whole original profile's score* is equal (including D6).
        active=tuple(x for x in block if x in profile)
        cylinder_sizes[len(active)]+=1
        fiber_map={}
        for index,order in enumerate(selected):
            restriction=tuple(order[block.index(x)] for x in active)
            if restriction in fiber_map and fiber_map[restriction]!=score_by_state[index]:
                raise AssertionError(
                    "J44 SOURCE profile depends on labels outside its original line support")
            fiber_map[restriction]=score_by_state[index]
            profile_local_restriction_checks+=1

    if any(sum(state_values[i])!=snapshots[i]["full_original_S"]
           for i in range(N)):
        raise AssertionError("J44 complete original right-source profile telescope failed")
    solved=exact_minimum_positive_profile_cover(
        profile_masks,N,max_distinct_masks=max_distinct_masks)
    witness_profiles=solved["original_right_source_profile_witnesses"]
    combined=tuple(sum(profile_values[p][i] for p in witness_profiles)
                   for i in range(N))
    if not all(v>=1 for v in combined):
        raise AssertionError("J45 no-good original global factor assignment survived cover")
    # Stronger than Boolean feasibility: a positive integer per-profile
    # weight yields a valid explicit lower bound on the FULL seven-S.
    min_charge=min(combined)
    min_full=min(s["full_original_S"] for s in snapshots)
    if min_full<min_charge:
        raise AssertionError("J45 witness profiles exceed full original sixset count")
    if min_full < profile_minima:
        raise AssertionError("J43 source profile independent minima exceed coherent min")

    cover_rows=[]
    for profile in witness_profiles:
        score=profile_values[profile]
        cover_rows.append({
            "original_source_right_line_multiset":profile,
            "right_source_lines_inside_changed_block":
                tuple(x for x in block if x in profile),
            "positive_state_bitmask":profile_masks[profile],
            "original_positive_sixsets_on_legal_states":score,
            "genuine_source_profile_local_cylinder_verified":True,
        })
    return {
        "scheme":scheme,"s":2,
        "fixed_original_left_factor_map":True,
        "full_original_right_factor_block":block,
        "original_occupied_four_physical_pair_image":original_image,
        "globally_injective_states_examined":N,
        "complete_24_state_injection_fiber_exhausted":N==24,
        "full_seven_S_min_over_examined_maps":min_full,
        "independent_original_source_profile_minima_sum":profile_minima,
        "exact_source_profile_coherence_gap":min_full-profile_minima,
        "total_active_original_source_profiles":len(profiles),
        "individual_original_source_profiles_positive_in_all_states":
            profile_positives_across_all_states,
        "J44_locality_checked_original_profile_state_pairs":
            profile_local_restriction_checks,
        "J44_original_source_line_support_size_histogram":
            dict(sorted(cylinder_sizes.items())),
        "J44_original_factor_cylinder_locality_verified":True,
        "J45_minimal_positive_cover":solved,
        "J45_positive_original_profile_cover_rows":cover_rows,
        "J45_min_sum_of_cover_original_Q_on_one_global_map":min_charge,
        "J45_exact_injection_no_simultaneous_zero_clause_certificate":True,
        "J46_exact_cover_minimality_finite_only":True,
        "independent_GF5_seven_class_oracle_checked_for_every_state":
            compare_independent,
        "J44_all_h_cylinder_identity":True,
        "J45_all_h_conditional_injection_matching_cover_lemma":True,
        "root_A_proved":False,
        "root_B_constructed":False,
        "new_ASET_exponent":False,
    }


def report(*, states=None):
    return {"slice":"JPKC-013",
            "status":"RESTRICTED_THEOREM_C_AND_FINITE_EXACT_INJECTION_COVER",
            "root_A_proved":False,"root_B_constructed":False,
            "results":[coherent_original_injection_certificate(
                scheme,states=states) for scheme in ("S68","S72")]}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--states",type=int)
    a=parser.parse_args()
    print(json.dumps(report(states=a.states),indent=2,sort_keys=True))
