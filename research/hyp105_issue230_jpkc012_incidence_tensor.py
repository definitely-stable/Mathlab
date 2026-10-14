"""JPKC-012: direct ORIGINAL six-incidence tensor, no physical P3 gate.

J41: sparse right-original-factor profile contraction for six non-D6 classes.
J42: normalized six-source-line positional dual contraction for D6.
J43: coherent finite source-profile minimax certificate; not an all-h
      positive lower bound. One globally injective f,g for every Q.
W32 full ORIGINAL sixset census; no false full W34 or ASET theorem.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc010_mixed_positive_transfer import FIBERS
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)

ALL_TAGS = tuple(R3_CERTIFIED_FLOORS)
LEFT_TYPES = ("A", "B", "C")
NON_D6_TAGS = tuple(x for x in ALL_TAGS if x != "D6")


def physical_twofactor_multigraphs(six_coords):
    """Enumerate 2-regular *multigraphs* on six symbols, edges up to double.

    Construct from degree deficits at the smallest unfinished coordinate,
    choosing its 1 or 2 higher-index neighbors as an UNORDERED multiset.
    This is an independent exact-cover enumerator, not the historical
    C6/C4/matching generator or a physical proper P3 enumerator.
    """
    coords=tuple(sorted(six_coords))
    if len(coords)!=6 or len(set(coords))!=6 or any(type(x)!=int or x<0 for x in coords):
        raise ValueError("six distinct nonnegative physical coordinates required")
    patterns=[]
    def walk(remaining, pairs):
        active=[i for i,d in enumerate(remaining) if d]
        if not active:
            if len(pairs)!=6:
                raise AssertionError("physical degree-two six-edge budget drift")
            patterns.append(tuple(sorted(pairs)))
            return
        i=active[0]
        d=remaining[i]
        if d not in (1,2):
            raise AssertionError("invalid physical degree deficit")
        viable=[j for j in range(i+1,6) if remaining[j]>0]
        options=((j,) for j in viable) if d==1 else combinations_with_replacement(viable,2)
        for js in options:
            if any(js.count(j)>remaining[j] for j in js):
                continue
            next_remaining=list(remaining)
            next_remaining[i]=0
            for j in js:
                next_remaining[j]-=1
            if min(next_remaining)<0:
                raise AssertionError("negative exact-cover degree deficit")
            walk(tuple(next_remaining), pairs+tuple(
                (coords[i],coords[j]) for j in js))
    walk((2,)*6, ())
    if len(patterns)!=130 or len(set(patterns))!=130:
        raise AssertionError("complete K6 70 simple +45 doubled+square+15 doubled-matching")
    return tuple(patterns)


def source_multiplicity_type(factors):
    multiplicities=tuple(sorted(Counter(factors).values(),reverse=True))
    return {
        (1,1,1,1,1,1):"A",
        (2,1,1,1,1):"B",
        (2,2,2):"C",
    }.get(multiplicities)


def _same_global_labels(ctx, right_labels):
    labels=tuple(tuple(x) for x in right_labels)
    if (len(labels)!=ctx.v or len(set(labels))!=ctx.v
            or any(len(e)!=2 or any(type(k)!=int for k in e)
                   or not 0<=e[0]<e[1]<ctx.a for e in labels)):
        raise ValueError("globally injective full original right-factor pair labels required")
    return labels


def _physical_half_type(ctx, source_factor_profile, right_labels):
    factors=tuple(source_factor_profile)
    profile=source_multiplicity_type(factors)
    if profile is None:
        return None
    degree=[0]*ctx.a
    for factor in factors:
        for coordinate in right_labels[factor]:
            degree[coordinate]+=1
    if degree.count(2)!=6 or any(d not in (0,2) for d in degree):
        return None
    return profile


def _source_line_normalized_dual(ctx, original_Q):
    """Build LEFT physical 2-factor as pairs of named ORIGINAL RIGHT lines.

    Only defined for Q having six DISTINCT ORIGINAL line factors.
    This removes arbitrary 0..5 incidence position indexing entirely.
    """
    original_lines=tuple(ctx.edges[eid][1] for eid in original_Q)
    if len(set(original_lines))!=6:
        raise ValueError("J42 requires six distinct ORIGINAL right lines")
    physical=defaultdict(list)
    for eid in original_Q:
        p,r=ctx.edges[eid]
        for coord in ctx.f[p]:
            physical[coord].append(r)
    if len(physical)!=6 or any(len(ls)!=2 for ls in physical.values()):
        raise AssertionError("J42 left physical 2-factor six original positions broken")
    return tuple(sorted(tuple(sorted(rs)) for rs in physical.values()))


def _right_line_dual(ctx, source_lines, right_labels):
    physical=defaultdict(list)
    for line in source_lines:
        for coord in right_labels[line]:
            physical[coord].append(line)
    if len(physical)!=6 or any(len(ls)!=2 for ls in physical.values()):
        return None
    return tuple(sorted(tuple(sorted(rs)) for rs in physical.values()))


def _connected_dual(dual):
    if dual is None or len(dual)!=6 or any(len(edge)!=2 for edge in dual):
        return False
    vertices={x for edge in dual for x in edge}
    if len(vertices)!=6 or any(sum(v in pair for pair in dual)!=2 for v in vertices):
        return False
    adj=defaultdict(set)
    for u,v in dual:
        if u==v:
            return False
        adj[u].add(v)
        adj[v].add(u)
    if any(len(x)!=2 for x in adj.values()):
        return False
    reached={next(iter(vertices))}
    front=list(reached)
    while front:
        for v in adj[front.pop()]:
            if v not in reached:
                reached.add(v)
                front.append(v)
    return len(reached)==6


def compile_incidence_tensor(model, *, max_original_candidates=80_000,
                             verify_original_subset_uniqueness=True):
    """Compile once from one genuine ORIGINAL left injection f.

    Independent ORIGINAL LEFT 2-regular multigraph exact-cover expansion:
    130 physical K6 multigraphs and ORIGINAL incident ID choices per factor.
    Sparse tensor row (left A/B/C, multiset ORIGINAL right lines, overlap)
    drives six accepted classes; D6 has extra normalized source line dual.
    NO P3 index, no historical selected_left_six or seven_census call.
    """
    ctx=ProjectionClosure(model)
    if ctx.s!=2 or ctx.a!=6:
        raise ValueError("full JPKC-012 ORIGINAL tensor limited to W32")
    if type(max_original_candidates)!=int or max_original_candidates<1:
        raise ValueError("positive exact original candidate budget required")
    patterns=physical_twofactor_multigraphs(range(ctx.a))
    by_point=[tuple(ctx.edge_id[(p,l)] for l in sorted(ctx.point_lines[p]))
              for p in range(ctx.v)]
    reverse_pair=ctx.fi
    source_profile=Counter()
    right_cylinders=Counter()
    right_dual_cylinders=Counter()
    right_original_profile_keys=set()
    histogram=Counter()
    seen=set() if verify_original_subset_uniqueness else None
    observed=0
    example={}
    for edges in patterns:
        pair_counts=Counter(edges)
        profile=tuple(sorted(pair_counts.values(),reverse=True))
        left_type={(1,1,1,1,1,1):"A",
                   (2,1,1,1,1):"B",
                   (2,2,2):"C"}.get(profile)
        if left_type is None:
            raise AssertionError("left six-pair exact cover has forbidden A/B/C profile")
        factors=[]
        choices=[]
        for pair,m in sorted(pair_counts.items()):
            p=reverse_pair.get(pair)
            if p is None:
                # W32 pair-label bijection should occupy ALL 15 physical edges.
                raise AssertionError("W32 physical edge missing true ORIGINAL point factor")
            factors.append(p)
            choices.append(tuple(combinations(by_point[p],m)))
        source_profile["left_pattern_"+left_type]+=1
        for picks in product(*choices):
            Q=tuple(sorted(eid for ids in picks for eid in ids))
            if len(Q)!=6 or len(set(Q))!=6:
                raise AssertionError("J41 six distinct ORIGINAL incidence IDs required")
            if seen is not None:
                if Q in seen:
                    raise AssertionError("one ORIGINAL six-incidence Q repeated in two tensor rows")
                seen.add(Q)
            observed+=1
            if observed>max_original_candidates:
                raise ValueError("exact original left six-incidence candidate budget exceeded")
            r_lines=tuple(ctx.edges[eid][1] for eid in Q)
            r_multiset=tuple(sorted(r_lines))
            r_type=source_multiplicity_type(r_lines)
            overlap=-1
            if left_type=="B" and r_type=="B":
                multiplicity=Counter(ctx.edges[eid][0] for eid in Q)
                repeated_p=next(p for p,n in multiplicity.items() if n==2)
                repeated_r=next(r for r,n in Counter(r_lines).items() if n==2)
                overlap=sum(ctx.edges[eid]==(repeated_p,repeated_r) for eid in Q)
                if overlap not in (0,1):
                    raise AssertionError("ORIGINAL GQ cannot repeat a point-line incidence")
            key=(left_type,r_multiset,overlap)
            right_cylinders[key]+=1
            right_original_profile_keys.add(r_multiset)
            histogram[left_type]+=1
            if r_type=="A" and left_type=="A":
                right_dual_cylinders[(r_multiset,
                    _source_line_normalized_dual(ctx,Q))]+=1
            if left_type not in example:
                example[left_type]=Q
    if observed!=62370 or histogram!=Counter({"A":51030,"B":10935,"C":405}):
        raise AssertionError("independent exact-cover 62,370 A/B/C original candidate mass mismatch")
    if sum(right_cylinders.values())!=observed:
        raise AssertionError("J41 original right-profile tensor lost incidence sixsets")
    if len(right_dual_cylinders)>sum(v for (lt,ls,_),v in right_cylinders.items()
                                    if lt=="A" and source_multiplicity_type(ls)=="A"):
        raise AssertionError("J42 source-line dual fiber exceeds A/A sixset count")
    return {
        "ctx":ctx,
        "candidate_original_Q":observed,
        "original_point_profile_histogram":dict(histogram),
        "physical_twofactor_pattern_histogram":{
            k:source_profile[k] for k in sorted(source_profile)},
        "source_line_profile_count":len(right_original_profile_keys),
        "sparse_right_profile_cylinders":right_cylinders,
        "positional_AA_D6_dual_cylinders":right_dual_cylinders,
        "distinct_sparse_right_profile_cylinder_rows":len(right_cylinders),
        "distinct_source_line_AA_dual_rows":len(right_dual_cylinders),
        "original_Q_examples_by_left_type":example,
        "independent_no_P3_left_generator":True,
    }


def _type_tag(left_type, right_type, overlap):
    if right_type is None:
        return None
    if (left_type,right_type) == ("A","B"):
        return "A-left/B-right"
    if (left_type,right_type) == ("B","A"):
        return "B-left/A-right"
    if (left_type=="C" and right_type in ("A","B")
            or right_type=="C" and left_type in ("A","B")):
        return "C/A" if "A" in (left_type,right_type) else "C/B"
    if left_type=="B" and right_type=="B":
        if overlap not in (0,1):
            raise AssertionError("J41 right B/B needs exact ORIGINAL overlap flag")
        return "B/B-overlap" if overlap else "B/B-disjoint"
    return None


def contract_incidence_tensor(compiled, right_labels, *, record_profile_values=False):
    """Direct all-seven ORIGINAL tensor contraction with ONE shared right g.

    Six sectors depend ONLY on the original right-factor multiset.
    D6: precise source-line-named dual equality and 6-cycle connectedness.
    """
    ctx=compiled["ctx"]
    g=_same_global_labels(ctx,right_labels)
    status={}
    counted=Counter()
    weighted=Counter()
    profile_scores=Counter()
    accepted_rows=0
    right_patterns=compiled["sparse_right_profile_cylinders"]
    for (l_type,r_source,overlap),n in right_patterns.items():
        if r_source not in status:
            status[r_source]=_physical_half_type(ctx,r_source,g)
        tag=_type_tag(l_type,status[r_source],overlap)
        if tag is not None:
            counted[tag]+=n
            weighted[tag]+=n*R3_CERTIFIED_FLOORS[tag]
            profile_scores[r_source]+=n
            accepted_rows+=1
    for (lines,left_dual),n in compiled["positional_AA_D6_dual_cylinders"].items():
        if status[lines]!="A":
            continue
        right_dual=_right_line_dual(ctx,lines,g)
        if right_dual==left_dual and _connected_dual(left_dual):
            counted["D6"]+=n
            weighted["D6"]+=n*R3_CERTIFIED_FLOORS["D6"]
            profile_scores[lines]+=n
    if sum(counted.values())>compiled["candidate_original_Q"]:
        raise AssertionError("J41/J42 selected original Q exceed six-incidence population")
    if sum(weighted.values())!=sum(counted[t]*R3_CERTIFIED_FLOORS[t]
                                   for t in ALL_TAGS):
        raise AssertionError("GF5 necessary class-weight tensor loss")
    if sum(profile_scores.values())!=sum(counted.values()):
        raise AssertionError("right ORIGINAL factor-profile contraction lost accepted Q")
    return {
        "complete_W32_true_original_S":sum(counted.values()),
        "original_seven_classes":{tag:counted[tag] for tag in ALL_TAGS},
        "GF5_51_column_certified_floor_numerator":sum(weighted.values()),
        "original_right_factor_profiles_examined":len(status),
        "active_positive_right_source_profiles":len(profile_scores),
        "active_positive_right_source_profile_rows":accepted_rows,
        "one_global_right_factor_assignment_shared_by_all_original_Q":True,
        "J41_non_D6_source_multiset_contraction_exact":True,
        "J42_D6_original_line_named_dual_contraction_exact":True,
        "profile_score_by_original_right_multiset":
            profile_scores if record_profile_values else None,
        "Root_A_proved":False,"Root_B_constructed":False,
    }


def independent_comparison(model, compiled=None):
    if compiled is None:
        compiled=compile_incidence_tensor(model)
    cert=contract_incidence_tensor(compiled,model["right_labels"])
    independent=seven_census(model,independent_checks=False,witness_sets=False)
    if cert["complete_W32_true_original_S"]!=independent["S_seven"]:
        raise AssertionError("direct J41/J42 ORIGINAL tensor S differs from historical seven-census")
    if cert["original_seven_classes"]!=independent["seven_class_motif_counts"]:
        raise AssertionError("direct seven-sector SOURCE tensor differs from independent GF5 classifier")
    if cert["GF5_51_column_certified_floor_numerator"]!=independent["GF5_seven_lower_numerator"]:
        raise AssertionError("direct SOURCE tensor seven-class GF5 floor numerator mismatch")
    cert["independent_original_seven_census_confirmed"]=True
    return cert


def coherent_right_fiber_tensor(scheme, *, states=None,
                                compare_independent=True):
    """J43 exact shared original source-profile cylinders on 24 maps.

    Fiber rows are one entire ORIGINAL right source profile, not one Q.
    Profile coherence gap min sum - sum min is >=0 for any finite shared
    assignment fiber. This is a CONDITIONAL all-h identity, not Root A.
    """
    if scheme not in FIBERS:
        raise ValueError("only pinned W32 S68/S72 true original fibers supported")
    if states is not None and (type(states)!=int or not 1<=states<=24):
        raise ValueError("positive integer states in [1,24] required")
    model=fixture(1,scheme)
    compiled=compile_incidence_tensor(model)
    old=tuple(tuple(e) for e in model["right_labels"])
    block=FIBERS[scheme]
    old_image=tuple(old[i] for i in block)
    orders=tuple(permutations(old_image))
    if len(orders)!=24 or len(set(orders))!=24:
        raise AssertionError("W32 global right-factor fiber 4!=24 violated")
    if states is not None:
        orders=orders[:states]
    rows=[]
    by_profile=defaultdict(list)
    for order in orders:
        next_g=list(old)
        for i,pair in zip(block,order):
            next_g[i]=pair
        actual=dict(model)
        actual["right_labels"]=tuple(next_g)
        result=contract_incidence_tensor(
            compiled,next_g,record_profile_values=True)
        if compare_independent:
            independent=seven_census(actual,independent_checks=False)
            if result["original_seven_classes"]!=independent["seven_class_motif_counts"]:
                raise AssertionError("J43 global fiber tensor vs independent exact 7 GF5 census")
        for profile,count in result["profile_score_by_original_right_multiset"].items():
            by_profile[profile].append((len(rows),count))
        rows.append({
            "original_global_four_line_images":order,
            "S":result["complete_W32_true_original_S"],
            "by_GF5_class":result["original_seven_classes"],
            "GF5_floor_numerator":result["GF5_51_column_certified_floor_numerator"],
            "positive_source_profile_count":result["active_positive_right_source_profiles"],
        })
    N=len(rows)
    independent_profile_min=0
    profile_masks={}
    universally_positive_profiles=0
    for profile,hits in by_profile.items():
        vec=[0]*N
        for k,n in hits:
            if vec[k]:
                raise AssertionError("one original source profile repeated in a fiber state")
            vec[k]=n
        independent_profile_min+=min(vec)
        mask=sum(1<<i for i,n in enumerate(vec) if n)
        if not mask:
            raise AssertionError("inactive right source profile inserted into positive tensor")
        profile_masks[profile]=mask
        universally_positive_profiles+=int(mask==(1<<N)-1)
    # Small reproducible finite source-profile cover. This is explicitly
    # greedy, NOT an unsupported optimal minimum-cardinality cover.
    remaining=(1<<N)-1
    greedy_cover=[]
    while remaining:
        if not profile_masks:
            raise AssertionError("some globally legal fiber state has no positive profile")
        chosen=max(profile_masks,key=lambda p:(
            (profile_masks[p]&remaining).bit_count(),tuple(-v for v in p)))
        fresh=remaining&profile_masks[chosen]
        if not fresh:
            raise AssertionError("no original positive source-profile covers remaining states")
        greedy_cover.append({
            "original_right_line_factor_multiset":chosen,
            "positive_state_bitmask":profile_masks[chosen],
            "new_globally_legal_fiber_states_covered":fresh.bit_count(),
        })
        remaining &= ~fresh
        if len(greedy_cover)>N:
            raise AssertionError("greedy finite-state positive-profile cover too large")
    if sum(x["new_globally_legal_fiber_states_covered"] for x in greedy_cover)!=N:
        raise AssertionError("original profile greedy-cover states are not disjointly charged")
    coherent_min=min(x["S"] for x in rows)
    gap=coherent_min-independent_profile_min
    if gap<0:
        raise AssertionError("J43 shared globally-injected assignment beats independent source-profile minima")
    if rows[0]["S"]!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("original W32 pinned seven GF5 baseline drift")
    return {
        "scheme":scheme, "original_right_factor_block":block,
        "complete_24_state_global_fiber":N==24,
        "actual_globally_injective_right_maps":N,
        "exact_min_full_seven_S":coherent_min,
        "sum_of_independent_right_source_profile_minima":independent_profile_min,
        "exact_global_source_profile_coherence_gap":gap,
        "globally_unavoidable_single_right_source_profiles":
            universally_positive_profiles,
        "greedy_all_global_states_positive_source_profile_cover":
            greedy_cover,
        "greedy_profile_cover_exactly_covers_examined_global_states":True,
        "greedy_profile_cover_optimality_claimed":False,
        "all_results_one_global_g_per_state":True,
        "all_states":rows,
        "J43_conditional_coherent_profile_minimax_all_h":True,
        "all_h_global_positive_omega":False,
    }


def report(*, fiber=None):
    if fiber:
        return {"slice":"JPKC-012", "fiber":coherent_right_fiber_tensor(fiber)}
    rows=[]
    for scheme in ("lex","reverse","S68","S72"):
        model=fixture(1,scheme)
        compiled=compile_incidence_tensor(model)
        row=independent_comparison(model,compiled)
        rows.append({"scheme":scheme,
                     "left_candidate_original_Q":compiled["candidate_original_Q"],
                     "left_pattern_histogram":compiled["physical_twofactor_pattern_histogram"],
                     "sparse_right_profile_rows":compiled["distinct_sparse_right_profile_cylinder_rows"],
                     "source_line_profiles":compiled["source_line_profile_count"],
                     "positional_D6_dual_rows":compiled["distinct_source_line_AA_dual_rows"],
                     **row})
    return {"slice":"JPKC-012", "root_A_proved":False,
            "direct_tensor_no_physical_P3_needed":True, "records":rows}


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--fiber",choices=tuple(FIBERS))
    args=ap.parse_args()
    print(json.dumps(report(fiber=args.fiber),sort_keys=True,indent=2))
