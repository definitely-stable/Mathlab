"""HYP-105 #230 D6-D: exact all-h incidence-factored Hall transport.

A source is an ORIGINAL incidence triple T carrying w_T proper blocked oriented
physical three-paths; a recipient is an actual accepted ORIGINAL six-incidence
set Q. Keeping >=1 source incidence is equivalent to integral flow through
source -> T -> original incidence e -> Q -> sink. Thus O(3|T|+6|Q|)
transport arcs replace O(|T|*|Q|) candidate overlap checks, without losing
min-K optimality. The proof and necessary/sufficient ALL-h Hall criterion
are independent of the availability of any all-h lower bound on |Q|.

FULL all-seven targets only for true original W32. W34 *strictly* targets
the synchronized original BB-overlap accepted subclass; it is NEVER the
full seven-family S on W34. An unsupported source in that restricted test
does NOT disprove any rule using the full unknown seven-family collection.
"""
from collections import Counter, defaultdict
from math import ceil
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6b_coherent_pruning import (
    full_retention, prune_original_incidences,
)
from hyp105_issue230_d6c_local_charge_hall import (
    _Dinic, blocked_sources, capacity_frontier,
)


def _validated(source_weights,accepted):
    """Freeze immutable ORIGINAL support keys with strict positive multiplicity."""
    triples=sorted(source_weights)
    sixsets=sorted(accepted)
    if (any(type(source_weights[t]) is not int or source_weights[t]<=0 or
            len(t)!=3 or tuple(sorted(set(t)))!=tuple(t) or
            any(type(x) is not int or x<0 for x in t) for t in triples)):
        raise ValueError("source demands must be positive integer ORIGINAL 3-incidence sets")
    if (any(len(q)!=6 or tuple(sorted(set(q)))!=tuple(q) or
            any(type(x) is not int or x<0 for x in q) for q in sixsets)):
        raise ValueError("targets must be DISTINCT ORIGINAL 6-incidence sets")
    return triples,sixsets


def _factored(source_weights,accepted,capacity,*,certificate=True):
    """Solve TRUE one-incidence common-support flow, NOT weighted GF5 event flow.

    Edges with capacity D+1 are logically infinite because a feasible
    assignment sends at most D total units. Original incidence hubs are
    unconstrained: recipient Q capacity K applies only once across ALL
    incidence hubs and prevents double spending.
    """
    if type(capacity) is not int or capacity<0:
        raise ValueError("nonnegative integer per-original-sixset capacity required")
    triples,sixsets=_validated(source_weights,accepted)
    total=sum(source_weights.values())
    incs=sorted({e for t in triples for e in t} |
                {e for q in sixsets for e in q})
    index={e:i for i,e in enumerate(incs)}
    m=len(triples);n=len(incs);k=len(sixsets)
    S=0;T=1;I=T+m;Q=I+n;sink=Q+k
    flow=_Dinic(sink+1)
    INF=total+1
    for i,t in enumerate(triples):
        flow.edge(S,T+i,source_weights[t])
        for e in t:
            flow.edge(T+i,I+index[e],INF)
    for j,q in enumerate(sixsets):
        for e in q:
            flow.edge(I+index[e],Q+j,INF)
        flow.edge(Q+j,sink,capacity)
    value=flow.maxflow(S,sink)
    if value==total or not certificate:
        return {
            "value":value,
            "complete":value==total,
            "source_total":total,
            "original_incidence_hubs":n,
            "explicit_transport_arc_bound":3*m+6*k,
            "explicit_transport_arcs":3*m+6*k,
            "exact_hall_cut":None
        }
    reachable=flow.reachable(S)
    A=[i for i in range(m) if T+i in reachable]
    source_inc={e for i in A for e in triples[i]}
    N=[j for j,q in enumerate(sixsets) if source_inc.intersection(q)]
    A_mass=sum(source_weights[triples[i]] for i in A)
    deficiency=A_mass-capacity*len(N)
    if (deficiency!=total-value or deficiency<=0 or
            any(I+index[e] not in reachable for e in source_inc) or
            any(Q+j not in reachable for j in N)):
        raise AssertionError("factored original incidence residual Hall cut is not exact")
    return {
        "value":value,"complete":False,"source_total":total,
        "original_incidence_hubs":n,
        "explicit_transport_arc_bound":3*m+6*k,
        "explicit_transport_arcs":3*m+6*k,
        "exact_hall_cut":{
            "source_triples":len(A),
            "source_demand":A_mass,
            "incidence_union_count":len(source_inc),
            "original_incidence_union_example":sorted(source_inc)[:12],
            "recipient_sixsets_touching_incidence_union":len(N),
            "max_load_per_original_sixset":capacity,
            "strict_hall_deficit":deficiency,
            "flow_shortfall":total-value,
            "representative_ORIGINAL_source_triples":[list(triples[i]) for i in A[:5]],
        }
    }


def _coverage(source_weights,accepted):
    """Exact unsupported triple census; no fabricated S or BB substitution."""
    triples,sixsets=_validated(source_weights,accepted)
    covered={e for q in sixsets for e in q}
    unsupported=[t for t in triples if not set(t).intersection(covered)]
    return {
        "source_oriented_blocked_paths":sum(source_weights.values()),
        "source_original_incidence_triples":len(triples),
        "recipient_original_sixsets":len(sixsets),
        "accepted_original_incidence_support":len(covered),
        "uncovered_oriented_blocked_paths":sum(source_weights[t] for t in unsupported),
        "unsupported_original_triples":len(unsupported),
        "first_unsupported_true_source_triple":list(unsupported[0]) if unsupported else None,
    }


def factored_frontier(source_weights,accepted,*,solve=True):
    triples,sixsets=_validated(source_weights,accepted)
    coverage=_coverage(source_weights,accepted)
    total=coverage["source_oriented_blocked_paths"]
    if not total:
        return {**coverage,"status":"EMPTY-SOURCE-NO-INFERENCE",
                "optimal_K":None}
    if not sixsets or coverage["uncovered_oriented_blocked_paths"]:
        return {**coverage,"status":"UNSUPPORTED-ONE-INCIDENCE-NO-GO-FOR-GIVEN-TARGETS",
                "optimal_K":None}
    if not solve:
        return {**coverage,"status":"COVERED-NO-CAPACITY-CERTIFICATE",
                "optimal_K":None}
    lo=ceil(total/len(sixsets))
    hi=total
    while lo<hi:
        mid=(lo+hi)//2
        r=_factored(source_weights,accepted,mid,certificate=False)
        if r["complete"]:
            hi=mid
        else:
            lo=mid+1
    optimum=_factored(source_weights,accepted,lo)
    if not optimum["complete"]:
        raise AssertionError("all supported one-incidence sources must be assignable at K=C")
    predecessor=_factored(source_weights,accepted,lo-1)
    if predecessor["complete"]:
        raise AssertionError("K-1 is infeasible by definition of optimum")
    cut=predecessor["exact_hall_cut"]
    if cut["strict_hall_deficit"]<=0:
        raise AssertionError("mincut must yield strict subset Hall obstruction")
    return {
        **coverage,
        "status":"EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM",
        "optimal_K":lo,
        "global_pigeonhole_K_floor":ceil(total/len(sixsets)),
        "extra_local_K_over_pigeonhole":lo-ceil(total/len(sixsets)),
        "factorized_flow_certificate":optimum,
        "K_minus_one_strict_Hall_witness":cut,
        "all_h_uniform_congestion_proved":False,
    }


def exact_incidence_union_hall_formula(source_weights,accepted,subsets):
    """On chosen finite sets F verify exact Hall left for ALL sources T subset F.

    Completeness across arbitrary F is NOT claimed; exact all-h
    equivalence is proved on paper using source-closed unions.
    """
    triples,sixsets=_validated(source_weights,accepted)
    result=[]
    for raw in subsets:
        F=set(raw)
        if any(type(e) is not int or e<0 for e in F):
            raise ValueError("original source-support union must contain valid IDs")
        demand=sum(source_weights[t] for t in triples if set(t)<=F)
        active={e for t in triples if set(t)<=F for e in t}
        recipients=sum(bool(active.intersection(q)) for q in sixsets)
        result.append({
            "input_original_incidence_set_size":len(F),
            "active_original_incidence_union_size":len(active),
            "oriented_source_demand_T_subset_F":demand,
            "eligible_positive_original_sixsets_meeting_active_union":recipients,
            "minimal_K_from_this_particular_closed_source_family":(
                ceil(demand/recipients) if recipients else None
            ),
            "denominator_zero_with_positive_demand":demand>0 and not recipients,
        })
    return result


def _source_for(core,retention,accepted,*,max_walks=5000000):
    led=blocked_sources(core,retention,accepted,max_walks=max_walks)
    return led["sources"],led


def w32_case(scheme):
    """All seven accepted true ORIGINAL positive classes; full-G only."""
    model=fixture(1,scheme)
    core=ProjectionClosure(model)
    all_seven=seven_census(model,independent_checks=True,witness_sets=True)
    recipients=all_seven["sets"]
    source,led=_source_for(core,full_retention(core),recipients)
    total=sum(source.values())
    if (all_seven["S_seven"]!=len(recipients)
            or total!=led["independent"]["C_joint_blocked_proper_P3"]):
        raise AssertionError("W32 complete positive targets or blocked source inconsistent")
    main=factored_frontier(source,recipients)
    # Cross-check completely different uncompressed T->Q bipartite flow,
    # forcing agreement for every true W32 globally pair-injective map.
    direct=capacity_frontier(source,recipients,1,solve=True)
    if direct["status"]!="EXACT-FINITE-INTEGRAL-HALL-OPTIMUM":
        if main["status"]!="UNSUPPORTED-ONE-INCIDENCE-NO-GO-FOR-GIVEN-TARGETS":
            raise AssertionError("factored complete status disagrees with D6C")
    elif (main["optimal_K"]!=direct["min_max_congestion"]
          or main["status"]!="EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM"):
        raise AssertionError("independent T-Q and T-e-Q min-K disagreed")
    classes=sorted(set(recipients.values()))
    drop=[]
    for classname in classes:
        remaining={q:label for q,label in recipients.items() if label!=classname}
        coverage=_coverage(source,remaining)
        drop.append({
            "excluded_positive_seven_class":classname,
            "excluded_true_original_sixsets":len(recipients)-len(remaining),
            "remaining_accepted_original_sixsets":len(remaining),
            "one_overlap_source_uncovered_oriented_paths":coverage[
                "uncovered_oriented_blocked_paths"],
            "full_original_seven_class_not_assumed_in_reduced_test":True,
        })
    return {
        "scope":"COMPLETE-ALL-SEVEN-ORIGINAL-W32",
        "scheme":scheme,"s":2,
        "original_full_global_f_g":True,
        "C_blocked_oriented":total,
        "E_endpoint_bad":led["independent"]["E_endpoint_bad_proper_P3"],
        "I_internal_only":led["independent"]["I_safe_endpoint_internal_only_proper_P3"],
        "full_seven_positive_S":len(recipients),
        "real_positive_class_counts":dict(all_seven["seven_class_motif_counts"]),
        "r1_incidence_factorized":main,
        "independent_D6C_direct_min_K":direct.get("min_max_congestion"),
        "one_class_deleted_coverage_diagnostics":drop,
    }


def w34_bb_only(right_mode):
    """Strict TRUE ORIGINAL synchronized-BB target subset, never all S."""
    model,_,_,_=true_spread_global_model(2,right_mode)
    core=ProjectionClosure(model)
    oracle=core.census(collect_witnesses=True)
    accepted={six:"B/B-overlap" for six in oracle["witness_multiplicities"]}
    if len(accepted)!=oracle["synchronized_BBo"]:
        raise AssertionError("original PR394 two-oriented-path BB multiplicity failed")
    policies=(full_retention(core),prune_original_incidences(core,"finite-calibration"))
    rows=[]
    for retention in policies:
        source,led=_source_for(core,retention,accepted,max_walks=10000000)
        measured=_coverage(source,accepted)
        # On incomplete target family, unsupported source is a correct NO-GO
        # ONLY for BB_sync recipients. If fully supported, solve exact K.
        frontier=factored_frontier(source,accepted,solve=True)
        if measured["source_oriented_blocked_paths"]!=led[
                "independent"]["C_joint_blocked_proper_P3"]:
            raise AssertionError("original W34 C does not match complete D6B 16 atoms")
        rows.append({
            "s":4,"mode":right_mode,
            "policy":retention["policy"],
            "target_scope":"ONLY-TRUE-ORIGINAL-ACCEPTED-SYNC-BB-SUBSET",
            "all_seven_positive_S":None,
            "full_synchronised_positive_BB_target_sixsets":len(accepted),
            "target_positive_original_GF5_class":"B/B-overlap",
            "retained_true_physical_edges":retention["retained_physical_edges"],
            "original_blocked_oriented":sum(source.values()),
            "E_endpoint_bad":led["independent"]["E_endpoint_bad_proper_P3"],
            "I_internal_only":led["independent"]["I_safe_endpoint_internal_only_proper_P3"],
            "r1_BB_subset_incidence_factorized":frontier,
            "BB_subset_is_entire_S":False,
            "all_h_universal_charge_proved":False,
        })
    return rows


def report():
    w32=[w32_case(x) for x in ("lex","reverse","S68","S72")]
    w34=[x for mode in ("balanced","reverse") for x in w34_bb_only(mode)]
    return {
        "slice":"HYP105-ISSUE230-D6D-ALL-h-FACTORED-ONE-INCIDENCE-HALL",
        "all_h_transport_factorization_and_exact_Hall_identity":"PROVED",
        "all_h_uniform_bounded_congestion":"OPEN",
        "all_h_original_seven_lower":"OPEN",
        "all_h_infinite_small_S_counterfamily":"OPEN",
        "W32_COMPLETE_positive_all_seven":w32,
        "W34_ONLY_true_positive_sync_BB_subsets":w34,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
