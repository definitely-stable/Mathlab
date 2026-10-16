"""HYP-105 #230 AA4-AT: EXACT shortest full-GLOBAL line-image transpositions.

A mathematical shortest-path subproblem underlying #545 and #548:
Fix true original six incidence IDs Q, all point / line source factors
different, point physical projection is connected C6, globally injected
f,g and a prescribed PHYSICALLY OCCUPIED oriented line C6 edge target
at the six ordered ORIGINAL source flag positions.

Let I be the six original line factor IDs. Define T(i) to be the
original source line factor currently owning desired g-image at flag i.
T:I→L is an injection, directed partial functional graph consisting of
disjoint directed paths escaping I, nontrivial cycles contained in I,
and fixed loops. The EXACT minimum number of transpositions on the
ENTIRE global map needed to realize the six targets is
  (# i∈I with T(i)!=i) - (# directed cycles of length>=2 within I).
This follows by extending the partial permutation to all line factors,
maximizing its number of cycles. The minimal global transposition
sequence is constructed independently and checked.

For physical K6, enumerate ALL 6! oriented physical six-cycles on the
SAME fixed globally occupied line image, so one exact MINIMUM over
all source-D6-compatible g' is provably attained. Results on actual
original W(3,2) global f,g are exact, not merely a repair upper bound.
For a>6, only candidate-conditioned distance is claimed (enumerating
all oriented six-coordinate cycles would be too large); parent #548
supplies a legal <=5 upper witness for any genuine original Q.

New result can prove that the <=5 construction is SHARP (if a real
original Q has exact min5), or falsify such sharpness if enumeration
shows all W32 min<=4; never extrapolate W32 to all h without proof.
"""
from collections import Counter
from itertools import permutations
from math import factorial

from hyp105_issue230_d6aa4as_every_original_Q_five_swap_repair import (
    _strict_finite_actual_original_model,
    original_left_C6_order_on_six_flag_IDs,
    _canonical_edge,
)


def _line_target_graph(left_line_ids, desired_owner_ids, total_lines):
    """True original factor IDs only. The target list is injective."""
    R=tuple(left_line_ids)
    T=tuple(desired_owner_ids)
    if (len(R)!=len(T) or len(R)!=6 or len(set(R))!=6
            or len(set(T))!=6 or any(type(v) is not int
            or v<0 or v>=total_lines for v in R+T)):
        raise ValueError("six distinct valid actual original source line IDs")
    return dict(zip(R,T))


def minimum_global_source_transpositions_for_target(
        original_line_ids,target_owners,total_lines):
    """Exact TRANSPOSITION distance of a partial source-label permutation.

    Count moved constrained original sources, subtract cycles internal
    to those original sources. No assumptions about original geometry
    beyond six actual distinct source line factor IDs and global label
    injection.
    """
    T=_line_target_graph(original_line_ids,target_owners,total_lines)
    marked=set()
    nontrivial_cycles=[]
    for start in T:
        if start in marked:continue
        at=start
        order=[];positions={}
        while at in T and at not in marked and at not in positions:
            positions[at]=len(order)
            order.append(at)
            at=T[at]
        if at in positions:
            cycle=tuple(order[positions[at]:])
            if len(cycle)>1:nontrivial_cycles.append(cycle)
        marked.update(order)
    moved=sum(i!=j for i,j in T.items())
    minimum=moved-len(nontrivial_cycles)
    if not (0<=minimum<=6):
        raise AssertionError("invalid shortest global source transposition")
    return {"minimum_GLOBAL_original_line_source_transpositions":minimum,
            "moved_constrained_original_LINE_source_factor_count":moved,
            "number_of_internal_nontrivial_cycles":len(nontrivial_cycles),
            "internal_nontrivial_cycles":tuple(nontrivial_cycles),
            "six_source_factor_owner_graph":tuple(sorted(T.items())),
            "exact_minimum_proven_by_partial_permutation_cycle_extension":True}


def construct_shortest_global_original_line_image_swaps(
        actual_global_line_images, original_line_ids, desired_physical_edges):
    """Independent constructive oracle: freeze required original factors.

    For each path from indegree-zero constrained source factor, swap
    source images following its T edges until it exits the six Q
    factors; for each remaining cycle swap along it to close.
    Returns a FULL globally injected original line pair map and
    one shortest list of swaps, never changing original incidence Q.
    """
    g=tuple(tuple(edge) for edge in actual_global_line_images)
    V=len(g)
    if len(set(g))!=V:raise ValueError("not a complete globally injective original line map")
    target_edges=tuple(tuple(edge) for edge in desired_physical_edges)
    if len(target_edges)!=6 or len(set(target_edges))!=6:
        raise ValueError("six distinct desired physically occupied edges")
    owner={e:i for i,e in enumerate(g)}
    if any(e not in owner for e in target_edges):
        raise ValueError("desired original line images must be occupied in same fixed global support")
    target_owner=tuple(owner[e] for e in target_edges)
    T=_line_target_graph(original_line_ids,target_owner,V)
    certificate=minimum_global_source_transpositions_for_target(
        original_line_ids,target_owner,V)
    touched=set()
    target_predecessors=set(T.values())&set(T)
    starts=tuple(i for i in T if i not in target_predecessors)
    working=list(g)
    swaps=[]
    def exchange(i,j):
        if i==j:raise AssertionError("no loop transposition allowed")
        working[i],working[j]=working[j],working[i]
        swaps.append((i,j))
    for start in starts:
        at=start
        while at in T and at not in touched:
            touched.add(at)
            nxt=T[at]
            if at!=nxt:exchange(at,nxt)
            at=nxt
    for start in T:
        if start in touched:continue
        cycle=[start]
        nxt=T[start]
        while nxt!=start:
            if nxt not in T or nxt in cycle:
                raise AssertionError("remaining partial source owner graph must be a cycle")
            cycle.append(nxt)
            nxt=T[nxt]
        touched.update(cycle)
        for i,j in zip(cycle,cycle[1:]):
            exchange(i,j)
    if any(working[i]!=e for i,e in zip(original_line_ids,target_edges)):
        raise AssertionError("minimum original global source swap construction did not reach target")
    if len(swaps)!=certificate["minimum_GLOBAL_original_line_source_transpositions"]:
        raise AssertionError("constructed original source swaps not shortest")
    if len(set(working))!=V or set(working)!=set(g):
        raise AssertionError("not same full occupied original line physical support")
    return {"minimum":len(swaps),"swaps":tuple(swaps),
            "after_GLOBAL_original_line_images":tuple(working),
            "source_owner_graph_certificate":certificate,
            "ORIGINAL_line_image_support_preserved":True}


def _true_original_flag_C6_order(model,Q):
    s,V,d,a,f,g,inc=_strict_finite_actual_original_model(model)
    neighbor=original_left_C6_order_on_six_flag_IDs(inc,f,Q)
    start=min(Q)
    following=min(neighbor[start])
    ordered=[start,following]
    while len(ordered)<6:
        nxt=next(i for i in neighbor[ordered[-1]] if i!=ordered[-2])
        if nxt in ordered:
            raise AssertionError("true source point C6 prematurely closed")
        ordered.append(nxt)
    if start not in neighbor[ordered[-1]]:
        raise AssertionError("true original point-side six flag cycle not closed")
    return s,V,a,f,g,inc,tuple(ordered),tuple(inc[i][1] for i in ordered)


def occupied_global_original_line_D6_cycle_owner_targets(global_right,a):
    """Exhaustive ONLY for genuine W32 K6, all six-position target
    assignments, with original factor labels owned by ONE fixed global g.

    All 6! physical coordinate vertex orders correspond to EXACT
    oriented C6 edge sequences, not six arbitrary physical pairs.
    """
    if a!=6:
        raise ValueError("exact complete physical D6 target cycle enumeration is restricted to K6")
    g=tuple(tuple(e) for e in global_right)
    owned={e:i for i,e in enumerate(g)}
    if len(g)!=15 or len(owned)!=15:
        raise ValueError("genuine W32 globally complete K6 original LINE images")
    targets=set()
    for vs in permutations(range(a),6):
        cycle=tuple(_canonical_edge(vs[i],vs[(i+1)%6]) for i in range(6))
        if all(e in owned for e in cycle):
            targets.add(tuple(owned[e] for e in cycle))
    if len(targets)!=factorial(6):
        raise AssertionError("complete original physical K6 must have exactly 720 oriented D6 targets")
    return tuple(sorted(targets))


def exact_true_original_W32_minimum_D6_repair_distance(model,Q,*,targets=None,
                                                       validate_witness=True):
    """TRUE ORIGINAL Q's GLOBAL optimum over ALL occupied physical K6
    connected C6 line targets, not just parent five-swap construction.

    Refuses s>2; no finite-W32 extrapolation or per-Q source map redraw
    is used in calculating this fixed-Q minimum.
    """
    s,V,a,f,g,inc,flag_cycle,source_line_ids=_true_original_flag_C6_order(model,Q)
    if (s,V,a)!=(2,15,6):
        raise ValueError("exact exhaustive physical D6 optimal search genuine W32 only")
    owners=occupied_global_original_line_D6_cycle_owner_targets(g,a) if targets is None else tuple(targets)
    if len(owners)!=720:
        raise ValueError("exact optimum requires ALL 720 oriented occupied line C6 targets")
    best=7;best_owners=None;hist=Counter()
    for wanted in owners:
        z=minimum_global_source_transpositions_for_target(
            source_line_ids,wanted,V)
        dist=z["minimum_GLOBAL_original_line_source_transpositions"]
        hist[dist]+=1
        if dist<best:
            best=dist;best_owners=wanted
    if not 0<=best<=5:raise AssertionError("parent every-Q global five-swap theorem violated")
    result={
        "s":s,"same_TRUE_ORIGINAL_six_incidence_flag_Q":tuple(Q),
        "point_C6_true_original_flag_position_order":flag_cycle,
        "six_TRUE_original_line_source_factor_IDs_in_order":source_line_ids,
        "ALL_720_oriented_physically_occupied_K6_D6_targets_exhausted":True,
        "EXACT_MINIMUM_full_GLOBAL_line_source_transposition_distance_to_D6":best,
        "ALL_global_target_distance_histogram":dict(sorted(hist.items())),
        "one_optimal_target_actual_line_source_owner_factor_IDs":best_owners,
        "original_f_and_original_incidence_Q_unchanged":True,
        "initial_g_physical_IMAGE_preserved_under_all_candidate_swaps":True,
        "original_fixed_g_positive_D6_iff_distance_ZERO":best==0,
    }
    if validate_witness:
        actual_edges=tuple(g[i] for i in best_owners)
        sol=construct_shortest_global_original_line_image_swaps(
            g,source_line_ids,actual_edges)
        if sol["minimum"]!=best:
            raise AssertionError("claimed actual shortest transposition certificate disagreement")
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        if classify_seven_prechecked(Q,f,sol["after_GLOBAL_original_line_images"],inc)!="D6":
            raise AssertionError("independent HISTORICAL ORIGINAL seven-GF5 classifier rejects optimum")
        result["optimal_actual_whole_original_line_source_swaps"]=sol["swaps"]
        result["historical_original_sixflag_GF5_D6_verified_at_global_OPTIMUM"]=True
    return result


def real_original_W32_min_distance_sample_certificate(model,*,sample_count=50,
                                                       include_full_source_census=False):
    """Deliberate finite sample of actual original source Q from #548;
    optional ALL original source Q exhaustive computation only if
    explicitly requested for genuine W32. Report scope honestly.
    """
    from hyp105_issue230_d6aa4as_every_original_Q_five_swap_repair import (
        finite_original_eligible_Q_generator)
    s,V,d,a,f,g,inc=_strict_finite_actual_original_model(model)
    if s!=2:raise ValueError("genuine original W32 only")
    Qs=tuple(finite_original_eligible_Q_generator(
        model,max_yield=None))
    targets=occupied_global_original_line_D6_cycle_owner_targets(g,a)
    if include_full_source_census:
        selected=Qs
    else:
        if type(sample_count) is not int or sample_count<1:
            raise ValueError("positive sample count")
        step=max(1,len(Qs)//sample_count)
        selected=Qs[::step][:sample_count]
    hist=Counter();by_Q={}
    for Q in selected:
        v=exact_true_original_W32_minimum_D6_repair_distance(
            model,Q,targets=targets,validate_witness=False)
        dist=v["EXACT_MINIMUM_full_GLOBAL_line_source_transposition_distance_to_D6"]
        hist[dist]+=1
        by_Q.setdefault(dist,Q)
    return {"s":2,"total_eligible_original_six_ID_Q":len(Qs),
            "EXACT_orig_original_Q_sampled_for_global_OPTIMUM":len(selected),
            "FULL_source_population_exhausted":include_full_source_census,
            "global_optimal_swap_distance_histogram":dict(sorted(hist.items())),
            "one_genuine_original_Q_witness_per_observed_distance":by_Q,
            "all_720_D6_line_target_orientations_per_Q_exhausted":True,
            "maximum_exact_distance_observed":max(hist),
            "all_TRUE_original_Q_have_optimum_at_most_five_proved_by_parent":True,
            "no_assumption_single_global_repaired_g_for_all_original_Q":True}
