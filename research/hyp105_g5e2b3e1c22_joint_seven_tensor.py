"""HYP-105 C22: exact one-COMMON-global-right seven-family joint tensor.

All-h theorem (for any pair-coordinate size a and any finite ORIGINAL
bipartite incidence host): six physical pairs span exactly six coordinates,
each degree two, IFF bitwise OR of their six two-bit masks has popcount=6
and XOR of those six masks is 0. Proof: six edges have total degree 12.
OR popcount six and XOR zero force each occupied coordinate to have even
positive degree at least 2; all six must therefore have degree exactly 2.

For any two ORIGINAL right-factor lines i,j, changing their globally
shared physical labels changes the seven indicator ONLY on original
six-incidence sets touching i or j. Hence the FULL seven-family and GF5
necessary-weight differences equal sums restricted to that EXACT common
original source fiber; no independent per-motif assignments or swaps.

The executable all-seven compiler is exact only on genuine W(3,2), 15
original point/line factors and 45 original incidences, with one frozen
global original left map f(p)=K6_PAIRS[p]. It builds one weighted source
of ORIGINAL distinct six-incidence sets with original incidence-ID
multiplicity; the source is shared by all 105 complete swapped right g.
Group multiplicity compresses only identical source signatures, NOT
different original sixsets into unsupported synthetic witnesses.

Outputs are FINITE correlated genuine-GQ S/D6/class and GF5 necessary
floor envelopes. Not a full S15 search, not an all-h universal lower,
not a full R3/GF5 flow computation or ASET exponent.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from math import comb
from functools import lru_cache

from hyp105_g5e2b3e1a_fixed_leading import (
    PAIRS, GF5_DENOM, selected_left_six, validated_small_model)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c21d_adversarial_right import (
    W32_LEX_RIGHT_ZERO_D6, W32_SEVEN_EXPECTED, genuine_global_W32_model)

TAGS = tuple(R3_CERTIFIED_FLOORS)
EDGE_BITS = tuple((1 << u) | (1 << v) for u,v in PAIRS)
COLUMN_PAIRS = tuple(combinations(range(6), 2))


def six_edges_degree_two_by_parity(pair_masks):
    """All-a exact six-pair 2-regular physical projection condition."""
    if len(pair_masks) != 6 or any(
            type(m) is not int or m <= 0 or m.bit_count() != 2
            for m in pair_masks):
        raise ValueError("exactly six valid two-coordinate bit masks required")
    union = 0
    parity = 0
    for mask in pair_masks:
        union |= mask
        parity ^= mask
    return union.bit_count() == 6 and parity == 0


def all_h_D6_one_global_right_transposition_influence(s):
    """Uniform ALL-h absolute Lipschitz bound for D6 under ONE line swap.

    Fixed complete original point f. Every original right line l is
    incident with Delta=s+1 distinct original points. For each
    original incidence (p,l), at most 24*C(a-2,4) physical simple
    C6s contain physical f(p), and the five OTHER ORIGINAL points
    in such a cycle each admit Delta original incidence selections.
    Therefore number of left-C6 original sixsets containing an
    incidence on l is <=24*C(a-2,4)*Delta^6. Union bound over the
    TWO swapped ORIGINAL right lines yields
        |D6(f,g swap(l1,l2))-D6(f,g)| <=48*C(a-2,4)*Delta^6.
    Counts original sixsets ONCE and is independent of the occupied
    pair-alphabet missing-edge pattern and global right g.

    This is O(s^12), too weak to imply ANY positive adversarial
    Omega(s^6) D6 or seven-class lower. Explicit nontransfer.
    """
    from hyp105_g5e2b3e1c20_global_left_c6 import all_h_global_left_c6_lower
    c20=all_h_global_left_c6_lower(s)
    a=c20["minimal_physical_coordinates"]
    delta=s+1
    per_original_line=24*comb(a-2,4)*delta**6
    two_line=2*per_original_line
    full_C6_source_upper=c20["all_Ka_simple_six_cycles"]*delta**6
    return {
        "s":s,"Delta":delta,"physical_coordinates":a,
        "per_fixed_physical_pair_C6_max":24*comb(a-2,4),
        "original_left_C6_with_one_fixed_right_line_upper":per_original_line,
        "original_left_C6_with_two_swapped_right_lines_upper":two_line,
        "all_original_left_C6_upper":full_C6_source_upper,
        "D6_absolute_transposition_change_upper":
            min(two_line,full_C6_source_upper),
        "asymptotic_influence_upper":"O(s^12)",
        "not_positive_all_g_D6_or_seven_lower":True,
    }


def _column_dual_signature(pair_masks):
    """Exactly six named column edges; bit for each intersecting pair."""
    signature = 0
    for i,(u,v) in enumerate(COLUMN_PAIRS):
        if pair_masks[u] & pair_masks[v]:
            signature |= (1 << i)
    return signature


def _cycle6_connected(signature):
    """Independent 6-vertex simple connected 2-regular dual check."""
    degree = [0]*6
    neighbors = [[] for _ in range(6)]
    for k,(i,j) in enumerate(COLUMN_PAIRS):
        if signature & (1 << k):
            degree[i] += 1
            degree[j] += 1
            neighbors[i].append(j)
            neighbors[j].append(i)
    if degree != [2]*6:
        return False
    seen={0}
    todo=[0]
    while todo:
        for n in neighbors[todo.pop()]:
            if n not in seen:
                seen.add(n)
                todo.append(n)
    return len(seen) == 6


def _endpoint_profile(endpoint_ids):
    counts = tuple(sorted(Counter(endpoint_ids).values(),reverse=True))
    if counts == (1,1,1,1,1,1):
        return "A"
    if counts == (2,1,1,1,1):
        return "B"
    if counts == (2,2,2):
        return "C"
    return None


def _eligible_schema(kind,points,lines,left_labels):
    """Original multiplicity profile + fixed left physical structure."""
    original_right = _endpoint_profile(lines)
    if original_right is None:
        return None
    if kind == "A" and original_right == "A":
        left_masks = tuple(
            (1<<left_labels[p][0])|(1<<left_labels[p][1]) for p in points)
        dual = _column_dual_signature(left_masks)
        return ("D6",dual) if _cycle6_connected(dual) else None
    if kind == "B" and original_right == "A":
        return ("B-left/A-right",-1)
    if kind == "A" and original_right == "B":
        return ("A-left/B-right",-1)
    if set((kind,original_right)) == {"C","A"}:
        return ("C/A",-1)
    if set((kind,original_right)) == {"C","B"}:
        return ("C/B",-1)
    if kind == original_right == "B":
        twice_point = next(p for p,n in Counter(points).items() if n==2)
        twice_line = next(l for l,n in Counter(lines).items() if n==2)
        point_positions = {i for i,p in enumerate(points) if p==twice_point}
        line_positions = {i for i,l in enumerate(lines) if l==twice_line}
        common = len(point_positions & line_positions)
        if common not in (0,1):
            raise AssertionError("original W32 incidence double cherry invalid")
        return ("B/B-overlap" if common else "B/B-disjoint",-1)
    return None


def compile_original_W32_joint_source(*,max_original_candidates=62370):
    """One genuine full original 45-incidence source; weighted signatures."""
    if type(max_original_candidates) is not int or max_original_candidates < 62370:
        raise ValueError("strict complete 62370 original left source budget required")
    model=genuine_global_W32_model()
    left,right,incidences,_=validated_small_model(model)
    grouped=Counter()
    total=0
    expected_kind=Counter()
    eligible=Counter()
    # Seven-class schema is static in f and ORIGINAL endpoint IDs. Only
    # physical right pair projection / exact D6 dual depends on g.
    for ids,kind in selected_left_six(model):
        total+=1
        if total > max_original_candidates:
            raise ValueError("original source exceeds complete budget")
        pts=tuple(incidences[i][0] for i in ids)
        lns=tuple(incidences[i][1] for i in ids)
        schema=_eligible_schema(kind,pts,lns,left)
        expected_kind[kind]+=1
        if schema is None:
            continue
        tag,dual=schema
        eligible[tag]+=1
        grouped[(tag,lns,dual)]+=1
    if total != 62370 or expected_kind != Counter(
            {"A":51030,"B":10935,"C":405}):
        raise AssertionError("original W32 A/B/C 62370 sixsets source changed")
    if sum(grouped.values()) != sum(eligible.values()):
        raise AssertionError("weighted signature compression lost actual sixsets")
    data=tuple((tag,ls,dual,mult) for (tag,ls,dual),mult in
               sorted(grouped.items()))
    by_line=[set() for _ in range(15)]
    for i,(_tag,lines,_dual,_mult) in enumerate(data):
        for line in set(lines):
            by_line[line].add(i)
    return {
        "model":model,
        "full_actual_original_sixsets":total,
        "left_source_original_profiles":dict(expected_kind),
        "original_candidate_class_profiles":dict(eligible),
        "eligible_original_sixsets":sum(eligible.values()),
        "compressed_source_records":len(data),
        "records":data,
        "source_record_ids_touching_original_right_line":
            tuple(frozenset(ids) for ids in by_line),
        "source_original_endpoint_occurrence_is_shared":True,
    }


def _valid_complete_g(right_perm):
    perm=tuple(right_perm)
    if len(perm)!=15 or any(type(x) is not int for x in perm) or (
            set(perm)!=set(range(15))):
        raise ValueError("ONE complete true W32 original-right-to-K6 bijection required")
    return perm


def _class_from_precompiled_record(record,right_masks):
    """One ORIGINAL sixset group and ONE shared physically valid right g."""
    kind,lines,dual,_mult=record
    edges=tuple(right_masks[l] for l in lines)
    if not six_edges_degree_two_by_parity(edges):
        return None
    if kind=="D6" and _column_dual_signature(edges)!=dual:
        return None
    return kind


def counts_for_global_right_mapping(compiled,right_perm):
    """Exact seven-vector for one common original right mapping."""
    right_perm=_valid_complete_g(right_perm)
    physical=tuple(EDGE_BITS[i] for i in right_perm)
    counts=Counter({tag:0 for tag in TAGS})
    for rec in compiled["records"]:
        cls=_class_from_precompiled_record(rec,physical)
        if cls:
            counts[cls]+=rec[3]
    return {tag:counts[tag] for tag in TAGS}


def _certified_lower_GF5_numerator(counts):
    return sum(R3_CERTIFIED_FLOORS[k]*counts[k] for k in TAGS)


def _swap_g(perm,i,j):
    value=list(perm)
    value[i],value[j]=value[j],value[i]
    return tuple(value)


def exact_joint_one_swap_neighborhood(*,max_original_candidates=62370):
    """Exact 105 complete right transposition class tradeoff envelope.

    Baseline full seven vector recomputed once from compiled signatures.
    For swap (i,j), evaluate ONLY source groups touching original i or j.
    Sources disjoint from these two ORIGINAL line IDs cannot change under
    swapping their GLOBAL physical assignments: proven all-h locality.
    """
    compiled=compile_original_W32_joint_source(
        max_original_candidates=max_original_candidates)
    baseline=W32_LEX_RIGHT_ZERO_D6
    initial=counts_for_global_right_mapping(compiled,baseline)
    if initial != W32_SEVEN_EXPECTED:
        raise AssertionError("frozen exact historical W32 seven-vector mismatch")
    old_mask=tuple(EDGE_BITS[i] for i in baseline)
    refs=compiled["source_record_ids_touching_original_right_line"]
    records=compiled["records"]
    trials=[]
    hist_S=Counter()
    hist_D6=Counter()
    min_conditioned=defaultdict(lambda:{"min_S":None,"min_GF5":None})
    for i,j in combinations(range(15),2):
        p=_swap_g(baseline,i,j)
        new_mask=tuple(EDGE_BITS[k] for k in p)
        counts=Counter(initial)
        affected=refs[i] | refs[j]
        changed_records=0
        changed_original_sixsets=0
        for rid in affected:
            rec=records[rid]
            before=_class_from_precompiled_record(rec,old_mask)
            after=_class_from_precompiled_record(rec,new_mask)
            if before == after:
                continue
            changed_records+=1
            changed_original_sixsets+=rec[3]
            if before is not None:
                counts[before]-=rec[3]
            if after is not None:
                counts[after]+=rec[3]
        if any(counts[k]<0 for k in TAGS):
            raise AssertionError("nonnegative joint tensor invalid")
        count={k:counts[k] for k in TAGS}
        score=sum(count.values())
        risk=_certified_lower_GF5_numerator(count)
        hist_S[score]+=1
        hist_D6[count["D6"]]+=1
        condition=min_conditioned[count["D6"]]
        if condition["min_S"] is None or score<condition["min_S"]:
            condition["min_S"]=score
            condition["min_S_witness_original_right_swap"]=(i,j)
        if condition["min_GF5"] is None or risk<condition["min_GF5"]:
            condition["min_GF5"]=risk
            condition["min_GF5_witness_original_right_swap"]=(i,j)
        trials.append({
            "swap_original_right_lines":(i,j),
            "seven_counts":count,
            "S_seven":score,
            "GF5_seven_necessary_numerator":risk,
            "source_records_touched":len(affected),
            "source_records_with_changed_acceptance":changed_records,
            "original_sixsets_with_changed_class":changed_original_sixsets,
        })
    if len(trials)!=comb(15,2) or sum(hist_D6.values())!=105:
        raise AssertionError("105 complete global right swaps not exhausted")
    if dict(hist_D6)!={0:40,1:29,2:24,3:6,4:4,5:1,9:1}:
        raise AssertionError("C21-D independent physical C6 one-swap histogram broken")
    min_S=min(v["S_seven"] for v in trials)
    min_GF5=min(v["GF5_seven_necessary_numerator"] for v in trials)
    # A seven-risk counterexample MUST provide SAME full global g;
    # this audit tracks one full permutation for each envelope optimum.
    min_S_witness=next(t for t in trials if t["S_seven"]==min_S)
    min_GF5_witness=next(t for t in trials if
                         t["GF5_seven_necessary_numerator"]==min_GF5)
    # Sample covariance is exact integer numerator, intentionally NOT
    # a claim that low D6 structurally forces high other classes.
    xd=[v["seven_counts"]["D6"] for v in trials]
    other=[v["S_seven"]-v["seven_counts"]["D6"] for v in trials]
    covariance_numerator=105*sum(x*y for x,y in zip(xd,other))-sum(xd)*sum(other)
    return {
        "scope":"TRUE_ORIGINAL_W32_105_COMPLETE_ONE_RIGHT_TRANSPOSITION_NEIGHBORS",
        "original_incidence_universe":45,
        "source_actual_left_sixsets":compiled["full_actual_original_sixsets"],
        "source_eligible_seven_pattern_sixsets":
            compiled["eligible_original_sixsets"],
        "source_compiled_weighted_records":compiled["compressed_source_records"],
        "original_source_profiles":compiled["left_source_original_profiles"],
        "original_right_permutation":baseline,
        "baseline_seven_counts":initial,
        "baseline_S_seven":sum(initial.values()),
        "baseline_GF5_seven_necessary_numerator":
            _certified_lower_GF5_numerator(initial),
        "one_swap_full_right_maps":len(trials),
        "D6_histogram":dict(sorted(hist_D6.items())),
        "S_seven_histogram":dict(sorted(hist_S.items())),
        "minimum_S_seven_over_only_105_swaps":min_S,
        "min_S_attaining_global_right_swap":min_S_witness,
        "minimum_GF5_necessary_numerator_over_only_105_swaps":min_GF5,
        "min_GF5_attaining_global_right_swap":min_GF5_witness,
        "per_D6_level_exact_minima_over_only_105_swaps":
            {d:min_conditioned[d] for d in sorted(min_conditioned)},
        "D6_vs_other_six_classes_exact_covariance_numerator":
            covariance_numerator,
        "all_105_exact_global_right_joint_profiles":trials,
        "all_h_swap_affected_original_right_lines_only":True,
        "all_h_pair_mask_or_xor_twofactor_identity":True,
        "not_full_15_factorial_right_search":True,
        "not_global_all_h_seven_Omega_s6_or_ASET_bound":True,
    }


def independently_check_historical_full_W32_global_maps(
        results, *, maximum_full_census_checks=4):
    """No fast tensor self-validation: historical full 62370 classifier.

    Verify SAME actual ORIGINAL GQ right bijections, a complete full
    historical seven_census recalculation. Existing independent source
    source from weighted B-left/right hypergraph checked separately.
    """
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_g5e2b3e1c0_weighted_overlap import (
        source_weighted_BA_hypergraph,exact_BA_overlap,
        simple_six_2factor_targets)
    if type(maximum_full_census_checks) is not int or (
            maximum_full_census_checks < 1):
        raise ValueError("independent full census positive budget required")
    trials=results["all_105_exact_global_right_joint_profiles"]
    # Include lowest S, highest S, D6=0 and D6>0 to avoid cherry-pick.
    selected=[
        min(trials,key=lambda p:(p["S_seven"],p["swap_original_right_lines"])),
        max(trials,key=lambda p:(p["S_seven"],p["swap_original_right_lines"])),
        next(t for t in trials if t["seven_counts"]["D6"]==0),
        next(t for t in trials if t["seven_counts"]["D6"]>0),
    ]
    distinct={}
    for item in selected:
        distinct[item["swap_original_right_lines"]]=item
    if len(distinct)>maximum_full_census_checks:
        raise ValueError("independent full-census budget too small")
    reports=[]
    baseline=tuple(W32_LEX_RIGHT_ZERO_D6)
    for swap, fast in sorted(distinct.items()):
        p=_swap_g(baseline,*swap)
        m=genuine_global_W32_model(p)
        historical=seven_census(m,independent_checks=False)
        if (historical["seven_class_motif_counts"] != fast["seven_counts"]
                or historical["S_seven"] != fast["S_seven"]
                or historical["GF5_seven_lower_numerator"] !=
                   fast["GF5_seven_necessary_numerator"]):
            raise AssertionError("full W32 historical classifier falsifies joint tensor")
        weights=source_weighted_BA_hypergraph(m)
        direct_B=exact_BA_overlap(
            weights,m["right_labels"],target=simple_six_2factor_targets(6))
        if direct_B != fast["seven_counts"]["B-left/A-right"]:
            raise AssertionError("independent original B-left weighted source mismatch")
        reports.append({
            "one_global_right_swap":swap,
            "historical_exact_all_62370_source_census_match":True,
            "independent_B_left_A_right_weighted_source_match":True,
            "S_seven":fast["S_seven"],
            "D6":fast["seven_counts"]["D6"],
            "GF5_seven_necessary_numerator":
                fast["GF5_seven_necessary_numerator"],
        })
    if not reports:
        raise AssertionError("no real W32 historical classifier cross-check")
    return reports


def _thin_report(results):
    return {k:v for k,v in results.items()
            if k!="all_105_exact_global_right_joint_profiles"}


if __name__=="__main__":
    import json
    report=exact_joint_one_swap_neighborhood()
    print(json.dumps({
        "joint_global_right_105":_thin_report(report),
        "independent_true_original_W32_full_62370_falsifiers":
            independently_check_historical_full_W32_global_maps(report),
    },indent=2,sort_keys=True))
