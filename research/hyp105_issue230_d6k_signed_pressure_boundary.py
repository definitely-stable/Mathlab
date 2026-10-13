"""HYP-105 #230 D6-K: exact signed-pressure / source-boundary Hall dual.

Every T is a three-set of ORIGINAL GQ incidence IDs carrying combined
oriented proper P3 masses E+I. Every accepted Q is an ORIGINAL positive
sixset from the SAME globally coherent f,g. Neither pair-labeled physical
coordinates nor BB-only W34 targets are substituted.

For active original-incidence support I=union_T T, K>=0, let
  L(e)=sum_{T contains e}w(T), d(e)=#{Q contains e},
  p_K(e)=2L(e)-K*d(e),
  boundary_w(F)=sum_{T:0<|T intersect F|<3}|T intersect F|w(T).
Then for EVERY F subset I:
  6*M(F)-K*D(F) = sum_{e in F}p_K(e)-2*boundary_w(F).
The uniform D6-I deficiency is the exact positive maximum over F.

We give a NEW conditional, exact-arithmetic expansion/variance criterion
under which ALL local positive Hall excess vanishes. It is sufficient,
NOT asserted for all W(3,s) global correlated labelings. A pair-cooccurrence
graph has pair cut <=2*boundary_w(F); a certified spanning-tree
algebraic-connectivity lower bound yields one checkable stronger gate.

A lower bound D(I)=Omega(s^6) would IMPLY S=Omega(s^6) immediately
(D(I)<=6*S): it cannot silently count as an independently proved input.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6d_incidence_factored_charging import _validated
from hyp105_issue230_d6e_support_expansion_profile import _normalise_split
from hyp105_issue230_d6i_uniform_port_hall import uniform_port_hall_cut
from hyp105_issue230_d6f_exception_budget_oracle import exception_budget_for_capacity


def _pressure_inputs(source_weights, accepted, K, split_weights=None):
    if type(K) is not int or K < 0:
        raise ValueError("K must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    incidence_set = set(e for t in triples for e in t)
    loads = Counter()
    pair = Counter()
    for t in triples:
        w = source_weights[t]
        for e in t:
            loads[e] += w
        for edge in combinations(t, 2):
            pair[edge] += w
    d = Counter(e for q in sixsets for e in q)
    p = {e: 2*loads[e]-K*d[e] for e in sorted(incidence_set)}
    if sum(loads.values()) != 3*sum(source_weights.values()):
        raise AssertionError("invalid original triple oriented-load identity")
    if sum(d.values()) != 6*len(sixsets):
        raise AssertionError("invalid original sixset incidence membership count")
    return triples, sixsets, split, sorted(incidence_set), loads, d, p, pair


def original_signed_pressure_boundary(source_weights, accepted, K, F,
                                      split_weights=None):
    """An INDEPENDENT direct triple scan certifying the signed-cut identity."""
    (triples, sixsets, splits, active, loads, d, p, pair) = _pressure_inputs(
        source_weights, accepted, K, split_weights
    )
    selected = set(F)
    if any(type(e) is not int or e < 0 or e not in set(active) for e in selected):
        raise ValueError("F must use distinct nonnegative active ORIGINAL incidence IDs")
    mass = 0
    inside_EI = Counter()
    partial_boundary = 0
    crossing_units = 0
    crossing_one = 0
    crossing_two = 0
    for t in triples:
        n = sum(e in selected for e in t)
        w = source_weights[t]
        if n == 3:
            mass += w
            for name, split in splits.items():
                inside_EI[name] += split[t]
        elif n in (1, 2):
            partial_boundary += n*w
            crossing_units += w
            if n == 1:
                crossing_one += w
            else:
                crossing_two += w
    D = sum(d[e] for e in selected)
    signed = 6*mass-K*D
    signed_pressure = sum(p[e] for e in selected)
    pair_cut = sum(w for (e, f), w in pair.items()
                   if (e in selected) != (f in selected))
    if signed != signed_pressure-2*partial_boundary:
        raise AssertionError("exact original pressure/escape identity violated")
    if pair_cut != 2*crossing_units or pair_cut > 2*partial_boundary:
        raise AssertionError("original pair-projection boundary identity violated")
    if sum(inside_EI.values()) != mass:
        raise AssertionError("original endpoint/internal paths double counted")
    N = len(active)
    G = sum(p.values())
    k = len(selected)
    centred_numerator = N*signed_pressure-k*G
    variance_numerator = N*sum(v*v for v in p.values())-G*G
    if centred_numerator**2 > variance_numerator*k*(N-k):
        raise AssertionError("exact finite pressure-variance Cauchy bound falsified")
    return {
        "K": K,
        "F_original_incidence_support": sorted(selected),
        "active_original_incidence_support_N": N,
        "k": k,
        "source_closed_oriented_M": mass,
        "split_source_closed_E_I": dict(inside_EI),
        "positive_original_port_boundary_D": D,
        "positive_original_sixsets_S": len(sixsets),
        "six_M_minus_K_D": signed,
        "signed_vertex_pressure_sum": signed_pressure,
        "original_partial_source_boundary": partial_boundary,
        "original_crossing_triple_weight": crossing_units,
        "crossing_at_one_original_port_weight": crossing_one,
        "crossing_at_two_original_ports_weight": crossing_two,
        "original_pair_projection_cut_weight": pair_cut,
        "pressure_centred_subset_numerator": centred_numerator,
        "pressure_variance_numerator": variance_numerator,
        "exact_signed_cut_identity": True,
        "exact_cauchy_variance_bound": True,
    }


def _max_spanning_tree_bottleneck(active, weighted_edges):
    """Integer-only maximum bottleneck spanning tree; disconnected -> 0.

    With edge weight at least b along some spanning tree, Rayleigh gives
    lambda_2(L_pair) >= 4b/[N(N-1)] using the range/variance inequality.
    """
    N = len(active)
    if N <= 1:
        return 0, N <= 1
    parent = {e: e for e in active}
    size = {e: 1 for e in active}
    def root(e):
        while parent[e] != e:
            parent[e] = parent[parent[e]]
            e = parent[e]
        return e
    chosen = 0
    bottleneck = 0
    for (u, v), w in sorted(weighted_edges.items(),
                           key=lambda x: (-x[1], x[0])):
        a, b = root(u), root(v)
        if a == b:
            continue
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        chosen += 1
        bottleneck = w
        if chosen == N-1:
            break
    connected = chosen == N-1
    return bottleneck if connected else 0, connected


def centred_pair_pressure_flow(active, p, pair):
    """EXACT integral capacitated calibration of the centered vertex pressure.

    Put q(e)=N*p(e)-G, where sum q=0, and capacity N*w(e,f)
    in BOTH directions of each source-cooccurrence pair. The calibrated
    pair edge flux is an exact divergence-q witness iff every original
    incidence F satisfies |sum_F q| <= N*B_pair(F). This is the exact
    oriented cut condition by ordinary integer maxflow/mincut; it is
    SUFFICIENT, not NECESSARY, for no extra ORIGINAL hypergraph Hall cut.
    """
    N=len(active)
    if N<=1:
        return {
            "status":"TRIVIAL-CENTRED-PRESSURE",
            "feasible":True,
            "scaled_supply":0,
            "routed_supply":0,
            "nonzero_signed_original_pair_flux_count":0,
            "centred_signed_edge_flux":[]
        }
    G=sum(p.values())
    q={e:N*p[e]-G for e in active}
    if sum(q.values())!=0:
        raise AssertionError("centred integer pressure must have zero sum")
    positive=sum(max(0,x) for x in q.values())
    index={e:i+1 for i,e in enumerate(active)}
    sink=N+1
    flow=_Dinic(sink+1)

    def recorded(u,v,cap):
        i=len(flow.graph[u])
        flow.edge(u,v,cap)
        return (u,i,cap)

    def used(record):
        u,j,original=record
        sent=original-flow.graph[u][j][1]
        if not 0<=sent<=original:
            raise AssertionError("invalid calibrated directed residual flow")
        return sent

    edges=[]
    for (u,v),w in sorted(pair.items()):
        a=recorded(index[u],index[v],N*w)
        rev=recorded(index[v],index[u],N*w)
        edges.append((u,v,w,a,rev))
    source_arcs=[]
    sink_arcs=[]
    for e in active:
        if q[e]>0:
            source_arcs.append(recorded(0,index[e],q[e]))
        elif q[e]<0:
            sink_arcs.append(recorded(index[e],sink,-q[e]))
    achieved=flow.maxflow(0,sink)
    if not 0<=achieved<=positive:
        raise AssertionError("centred pair pressure routing exceeds supply")
    flux=[]
    divergence=Counter()
    for u,v,w,a,rev in edges:
        g=used(a)-used(rev)
        if abs(g)>N*w:
            raise AssertionError("pair capacity exceeded in calibration")
        divergence[u]+=g
        divergence[v]-=g
        if g:
            flux.append([u,v,g,N*w])
    if sum(used(x) for x in source_arcs)!=achieved or sum(
        used(x) for x in sink_arcs)!=achieved:
        raise AssertionError("pair calibration source or sink flow conservation")
    fully_routed=achieved==positive
    witness=None
    if fully_routed:
        if any(divergence[e]!=q[e] for e in active):
            raise AssertionError("centred calibration divergence incorrect")
    else:
        reach=flow.reachable(0)
        F={e for e in active if index[e] in reach}
        pair_cut=sum(w for (u,v),w in pair.items() if (u in F)!=(v in F))
        excess=sum(q[e] for e in F)-N*pair_cut
        if excess!=positive-achieved or excess<=0:
            raise AssertionError("calibration cut dual did not expose obstruction")
        witness={
            "original_incidence_support_F":sorted(F),
            "sum_centred_integer_pressure":sum(q[e] for e in F),
            "original_pair_cut_weight":pair_cut,
            "exact_positive_pair_cut_shortfall":excess,
        }
    return {
        "status":("CERTIFIED-CENTRED-PAIR-CALIBRATION" if fully_routed
                  else "PAIR-CALIBRATION-FAILED-NOT-GQ-COUNTEREXAMPLE"),
        "feasible":fully_routed,
        "scaled_supply":positive,
        "routed_supply":achieved,
        "nonzero_signed_original_pair_flux_count":len(flux),
        "centred_signed_edge_flux":flux if fully_routed else [],
        "failed_pair_cut_witness":witness,
        "all_original_incidence_divergences_verified":fully_routed,
    }


def signed_pressure_global_certificate(source_weights, accepted, K,
                                       split_weights=None):
    """Exact all-F max Hall cut, plus independently sufficient spectral gate.

    The tree gate is deliberately CONSERVATIVE and uses no unverified float
    eigenvalue. It can prove global-only obstruction even when p_K(e)>0.
    If its inequality fails, this is not an obstruction: the exact D6-I
    maxflow still decides the full cut. S lower bound remains OPEN.
    """
    (triples, sixsets, splits, active, loads, d, p, pair) = _pressure_inputs(
        source_weights, accepted, K, split_weights
    )
    C = sum(source_weights.values())
    N = len(active)
    G = sum(p.values())  # = 6*C - K*D(I), not necessarily 6*(C-K*S)
    D_I = sum(d[e] for e in active)
    if G != 6*C-K*D_I:
        raise AssertionError("global active source-only pressure invalid")
    v = N*sum(x*x for x in p.values())-G*G
    if v < 0:
        raise AssertionError("integer pressure variance cannot be negative")
    bottleneck, connected = _max_spanning_tree_bottleneck(active, pair)
    calibration=centred_pair_pressure_flow(active,p,pair)
    # lambda2 >= 4*b/[N(N-1)]. For any nontrivial k-cut, Cauchy
    # gives sqrt(v*k*(N-k))/N pressure discrepancy. Rayleigh gives
    # lambda2*k*(N-k)/N on the pair cut, so global-only follows if
    # lambda2^2*(N-1)>=v. Integer-only tree sufficient condition:
    # 16*b^2 >= v*N^2*(N-1).
    spectral_tree_sufficient = (
        N <= 1 or v == 0 or (
            connected and 16*bottleneck*bottleneck >= v*N*N*(N-1)
        )
    )
    mincut = uniform_port_hall_cut(source_weights, accepted, K, splits)
    F = mincut["mincut"]["source_closed_original_incidence_support_F"]
    witness = original_signed_pressure_boundary(
        source_weights, accepted, K, F, splits)
    delta = mincut["exact_uniform_scaled_Hall_deficit_Delta6"]
    if witness["six_M_minus_K_D"] != delta:
        raise AssertionError("direct pressure identity differs from exact mincut")
    global_pressure_deficit = max(0, G)
    if delta < global_pressure_deficit:
        raise AssertionError("global full source support must be candidate cut")
    if calibration["feasible"] and delta != global_pressure_deficit:
        raise AssertionError("centred pair-flux Hall calibration falsified")
    if spectral_tree_sufficient and delta != global_pressure_deficit:
        raise AssertionError("spectral/tree global-only guarantee falsified")
    exact_full = exception_budget_for_capacity(
        source_weights, accepted, K, splits)
    full_exception = exact_full["minimal_exception_mass"]
    upper = delta//6
    if upper < full_exception:
        raise AssertionError("restricted uniform upper failed full original flow")
    return {
        "slice": "HYP105-ISSUE230-D6K-SIGNED-PRESSURE-BOUNDARY",
        "scope": "ALL-FINITE-ALL-H-EXACT-CUT-IDENTITY-CONDITIONAL-EXPANSION",
        "K": K,
        "C_original_joint_E_I": C,
        "S_complete_positive_original_sixsets": len(sixsets),
        "active_original_incidence_N": N,
        "source_mass_split": {
            name: sum(w.values()) for name, w in splits.items()
        },
        "positive_target_port_degree_sum_all_original": 6*len(sixsets),
        "positive_port_degree_sum_on_active_source_I": D_I,
        "positive_port_memberships_outside_active_source_I": (
            6*len(sixsets)-D_I
        ),
        "positive_source_incidence_pressure_count": sum(x>0 for x in p.values()),
        "negative_source_incidence_pressure_count": sum(x<0 for x in p.values()),
        "zero_source_incidence_pressure_count": sum(x==0 for x in p.values()),
        "maximum_signed_source_incidence_pressure": max(p.values(),default=0),
        "minimum_signed_source_incidence_pressure": min(p.values(),default=0),
        "global_signed_pressure_G": G,
        "nonnegative_global_restricted_scaled_deficit": global_pressure_deficit,
        "signed_pressure_variance_numerator_v": v,
        "source_pair_graph_weighted_edges": len(pair),
        "centred_pair_pressure_calibration":calibration,
        "calibrated_pair_flow_global_only_Hall_deficit_CERTIFIED":(
            calibration["feasible"]
        ),
        "source_pair_graph_connected": connected,
        "certified_maximum_spanning_tree_bottleneck_b": bottleneck,
        "certified_fiedler_lower_bound_fraction_4b_over_N_Nminus1": (
            [4*bottleneck,N*(N-1)] if N>=2 else None
        ),
        "spectral_tree_expansion_sufficient_integer_check": (
            16*bottleneck*bottleneck >= v*N*N*(N-1)
            if N>=2 else True
        ),
        "spectral_tree_global_only_Hall_deficit_CERTIFIED": (
            spectral_tree_sufficient
        ),
        "uniform_exact_scaled_Hall_deficit_Delta6": delta,
        "exact_local_Hall_excess_over_global_source_pressure": (
            delta-global_pressure_deficit
        ),
        "exact_D6F_full_original_exception_mass": full_exception,
        "uniform_exception_upper_floor_Delta6_div6": upper,
        "minimum_cut_direct_pressure_boundary_witness": witness,
        "global_port_bound_circularity_gate": (
            "D(I)<=6S: any independent D(I)=Omega(s^6) already implies "
            "S=Omega(s^6); NO such bound established"
        ),
        "all_h_label_uniform_positive_port_expansion": "OPEN",
        "root_Branch_A_or_B": "OPEN",
        "original_W34_W38_full_seven_positive_S": "UNKNOWN",
    }


def genuine_complete_W32_pressure_report():
    """Actual globally injective same-map full-seven W(3,2) ONLY."""
    from hyp105_issue230_d6h_incidence_budget_certificate import (
        _complete_w32_inputs,
    )
    from hyp105_issue230_d6d_incidence_factored_charging import factored_frontier
    cases=[]
    for scheme in ("lex","reverse","S68","S72"):
        recipients,sources,parts=_complete_w32_inputs(scheme)
        K=factored_frontier(sources,recipients)["optimal_K"]
        if K is None or K <= 0:
            raise AssertionError("W32 full-seven proper source not supported")
        prev=signed_pressure_global_certificate(sources,recipients,K-1,parts)
        at=signed_pressure_global_certificate(sources,recipients,K,parts)
        if prev["exact_local_Hall_excess_over_global_source_pressure"] != 0:
            raise AssertionError("W32 K-1 cut unexpectedly gained local excess")
        if at["uniform_exact_scaled_Hall_deficit_Delta6"] != 0:
            raise AssertionError("W32 uniform K min not feasible")
        cases.append({
            "scheme":scheme,
            "C":sum(sources.values()),
            "E":sum(parts["endpoint"].values()),
            "I":sum(parts["internal"].values()),
            "S_complete_seven":len(recipients),
            "K_full":K,
            "at_K_minus_one":prev,
            "at_K":at,
        })
    return {
        "slice":"HYP105-ISSUE230-D6K-SIGNED-PRESSURE-BOUNDARY",
        "all_h_pressure_cut_identity":"PROVED-ALL-FINITE-SYSTEMS",
        "spectral_tree_gate":"PROVED-SUFFICIENT-NOT-GEOMETRY-UNIFORM",
        "S_s_Omega_s6":"OPEN",
        "Branch_A_or_B":"OPEN",
        "W34_W38_complete_seven_positive_S":"UNKNOWN-NO-BB-SUBSTITUTION",
        "genuine_complete_seven_W32_cases":cases,
    }


if __name__=="__main__":
    print(json.dumps(genuine_complete_W32_pressure_report(),sort_keys=True,indent=2))
