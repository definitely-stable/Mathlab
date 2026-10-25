"""HYP-105 #230 D6-L: exact directed ORIGINAL three-port pressure calibration.

The ORIGINAL weighted blocked-source triple T contributes a directional
boundary cost 2*N*|T intersect F|*w(T) whenever T crosses F (0 or 3
original incidences inside have zero cost). Unlike an undirected
pair-projection, this retains the 1-vs-2 selected-incidence distinction.

For active source incidence I, N=|I|, p(e)=2*L(e)-K*d_A(e),
G=sum_I p(e), and q(e)=N*p(e)-G, sum q=0. The independent directed
incidence->triple->incidence flow has e->T capacity 2*N*w(T)
and T->e infinite capacity. Its exact mincut shortfall is

    E_dir = max_(F subset I) (
        sum_(e in F) q(e) - 2*N*boundary_w(F)
    )_+,

where boundary_w(F) counts a crossing T with its number of ORIGINAL
incidences inside F. The network's primal gives an integer hyperedge
transport witness; its dual gives ORIGINAL F, unlike pair projection.

For all instances, letting Delta6 be D6-I's exact restricted uniform
Hall deficit and U_K=floor(Delta6/6),

    0 <= Delta6 - max(0,G) <= floor(E_dir/N)  (N>0),

and E_dir=0 implies Delta6=max(0,G). E_dir<=E_pair from D6-K.
This is a new constructive conditional all-h theorem, NOT a claim that
the condition holds for arbitrary true correlated GF5-positive W(3,s)
maps. Complete accepted seven-class targets only for genuine W32.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6k_signed_pressure_boundary import (
    _pressure_inputs, original_signed_pressure_boundary,
    signed_pressure_global_certificate,
)


def directed_original_triple_calibration(source_weights, accepted, K,
                                         split_weights=None):
    """Recover primal directed original triple flows or the exact dual cut."""
    triples, sixsets, split, active, loads, degrees, p, pair = (
        _pressure_inputs(source_weights, accepted, K, split_weights)
    )
    N=len(active)
    C=sum(source_weights.values())
    if N==0:
        return {
            "status":"EMPTY-SOURCE-DIRECTED-TRIPLE-CALIBRATION",
            "K":K,"N":0,"C":0,"G":0,"integer_q_supply":0,
            "routed_q":0,"directed_calibration_deficit_E":0,
            "certified_zero_directed_calibration_deficit":True,
            "original_directed_hypergraph_slack_bound":0,
            "pair_calibration_deficit_upper":0,
            "triple_primal_all_integer_ports":[],
            "dual_original_incidence_support_F":[],
            "dual_original_triple_boundary":0,
            "scope":"ALL-FINITE-DIRECTED-ORIGINAL-TRIPLES-NOT-BRANCH-A"
        }
    G=sum(p.values())
    q={e:N*p[e]-G for e in active}
    if sum(q.values())!=0:
        raise AssertionError("scaled centered pressure does not sum to zero")
    total_supply=sum(max(0,v) for v in q.values())
    a={e:1+i for i,e in enumerate(active)}
    t0=1+N
    sink=t0+len(triples)
    net=_Dinic(sink+1)
    INF=total_supply+1

    def put(u,v,cap):
        j=len(net.graph[u])
        net.edge(u,v,cap)
        return u,j,cap

    def sent(edge):
        u,j,cap=edge
        v=cap-net.graph[u][j][1]
        if not 0<=v<=cap:
            raise AssertionError("invalid directed original residual edge")
        return v

    incoming=[]
    outgoing=[]
    for i,t in enumerate(triples):
        # e -> auxiliary T costs precisely 2N w(T) when e is selected
        # but at least one other original incidence of T is unselected.
        for e in t:
            incoming.append((t,e,put(a[e],t0+i,2*N*source_weights[t])))
            outgoing.append((t,e,put(t0+i,a[e],INF)))
    for e in active:
        if q[e]>0:
            put(0,a[e],q[e])
        elif q[e]<0:
            put(a[e],sink,-q[e])
    flow=net.maxflow(0,sink)
    if not 0<=flow<=total_supply:
        raise AssertionError("directed calibration routed invalid q amount")
    E=total_supply-flow
    reach=net.reachable(0)
    F={e for e in active if a[e] in reach}
    witness=original_signed_pressure_boundary(
        source_weights,accepted,K,F,split
    )
    cut_boundary=witness["original_partial_source_boundary"]
    cut_viol=sum(q[e] for e in F)-2*N*cut_boundary
    if cut_viol!=E or E<0:
        raise AssertionError("directed triple mincut is not exact")
    if E and E<=0:
        raise AssertionError("positive shortfall must have positive dual cut")
    if E and not F:
        raise AssertionError("positive calibration deficit has no original support")
    if E==0 and cut_viol!=0:
        raise AssertionError("full centered source calibration must have zero dual")

    in_by=Counter()
    out_by=Counter()
    vertex_div=Counter()
    triple_primal=[]
    if E==0:
        # An explicit integral primal flow, not just a boolean maxflow.
        by_t={}
        for t,e,arc in incoming:
            mass=sent(arc)
            in_by[t]+=mass
            vertex_div[e]+=mass
            if mass:
                by_t.setdefault(t,{"incoming":[],"outgoing":[]})[
                    "incoming"].append([e,mass])
        for t,e,arc in outgoing:
            mass=sent(arc)
            out_by[t]+=mass
            vertex_div[e]-=mass
            if mass:
                by_t.setdefault(t,{"incoming":[],"outgoing":[]})[
                    "outgoing"].append([e,mass])
        if any(in_by[t]!=out_by[t] for t in triples):
            raise AssertionError("original three-port auxiliary flow not conserved")
        if any(vertex_div[e]!=q[e] for e in active):
            raise AssertionError("integer directed triple flux divergence wrong")
        for t, x in sorted(by_t.items()):
            if any(m>2*N*source_weights[t] for e,m in x["incoming"]):
                raise AssertionError("per-port original triple boundary exceeded")
            triple_primal.append({
                "source_original_triple":list(t),
                "incoming_original_ports":x["incoming"],
                "outgoing_original_ports":x["outgoing"],
                "total_flow":in_by[t]
            })

    pair_compatible=Counter()
    for t in triples:
        for e,f in combinations(t,2):
            pair_compatible[(e,f)]+=source_weights[t]
    if pair_compatible!=pair:
        raise AssertionError("directed triple graph lost original co-occurrence")
    return {
        "status":("CERTIFIED-DIRECTED-ORIGINAL-TRIPLE-CALIBRATION"
                  if not E else "EXACT-DIRECTED-CALIBRATION-OBSTRUCTION"),
        "scope":"ALL-FINITE-DIRECTED-ORIGINAL-TRIPLES-NOT-BRANCH-A",
        "K":K,"N":N,"C":C,"G":G,
        "joint_original_E_I_source_masses":{
            name:sum(parts.values()) for name,parts in split.items()},
        "integer_q_supply":total_supply,
        "routed_q":flow,
        "directed_calibration_deficit_E":E,
        "certified_zero_directed_calibration_deficit":E==0,
        "original_directed_hypergraph_slack_bound":E//N,
        "dual_original_incidence_support_F":sorted(F),
        "dual_original_triple_boundary":cut_boundary,
        "dual_positive_port_boundary_D":witness[
            "positive_original_port_boundary_D"],
        "dual_signed_pressure_sum":witness["signed_vertex_pressure_sum"],
        "dual_integer_centred_pressure_sum":sum(q[e] for e in F),
        "dual_exact_deficit":cut_viol,
        "triple_primal_all_integer_ports":triple_primal,
        "triple_primal_nonzero_count":len(triple_primal),
        "all_h_original_GF5_label_uniform_gate":"OPEN",
    }


def compare_original_pair_and_directed(source_weights, accepted, K,
                                       split_weights=None):
    """Fail closed against D6-K PAIR and true D6-I/D6-F source-boundary cuts."""
    from hyp105_issue230_d6k_signed_pressure_boundary import (
        original_signed_pressure_boundary,
    )
    base=signed_pressure_global_certificate(
        source_weights,accepted,K,split_weights)
    directed=directed_original_triple_calibration(
        source_weights,accepted,K,split_weights)
    N=directed["N"]
    pair=base["centred_pair_pressure_calibration"]
    E_dir=directed["directed_calibration_deficit_E"]
    E_pair=pair["scaled_supply"]-pair["routed_supply"]
    if E_dir>E_pair:
        raise AssertionError("stronger directed original boundary lost against PAIR")
    G=base["global_signed_pressure_G"]
    delta=base["uniform_exact_scaled_Hall_deficit_Delta6"]
    local=delta-max(0,G)
    if local<0 or (N and local>E_dir//N):
        raise AssertionError("centered original directed hypergraph local bound failed")
    if E_dir==0 and local!=0:
        raise AssertionError("directed calibration complete but local Hall excess remains")
    pair_obstruction=pair.get("failed_pair_cut_witness")
    if pair_obstruction:
        F=pair_obstruction["original_incidence_support_F"]
        original=original_signed_pressure_boundary(
            source_weights,accepted,K,F,split_weights)
        q_on_F=N*original["signed_vertex_pressure_sum"]-len(F)*G
        directional_cost=2*N*original["original_partial_source_boundary"]
        pair_cost=N*original["original_pair_projection_cut_weight"]
        if (q_on_F-pair_cost !=
                pair_obstruction["exact_positive_pair_cut_shortfall"]):
            raise AssertionError("independent pair cut mismatch")
        if directional_cost<pair_cost:
            raise AssertionError("wrong original directed triple boundary sign")
    return {
        "status":"EXACT-ORIGINAL-TRIPLE-DIRECTED-VS-PAIR-HALL-CERTIFICATE",
        "original_directed":directed,
        "original_pair": {
            "feasible":pair["feasible"],
            "centred_pair_deficit_E":E_pair,
            "first_pair_cut_witness":pair_obstruction
        },
        "true_original_exact_uniform_Delta6":delta,
        "true_original_exact_uniform_local_excess":local,
        "true_original_D6F_integer_exception":base[
            "exact_D6F_full_original_exception_mass"],
        "directed_is_no_weaker_than_pair":E_dir<=E_pair,
        "all_h_original_GF5_sixset_growth":"OPEN",
    }


def finite_genuine_W32_directed_report():
    from hyp105_issue230_d6h_incidence_budget_certificate import (
        _complete_w32_inputs,
    )
    from hyp105_issue230_d6d_incidence_factored_charging import factored_frontier
    rows=[]
    for scheme in ("lex","reverse","S68","S72"):
        targets, sources, split=_complete_w32_inputs(scheme)
        original=factored_frontier(sources,targets)
        K=original["optimal_K"]
        if K is None or K<1:
            raise AssertionError("true complete W32 must have positive K")
        previous=compare_original_pair_and_directed(
            sources,targets,K-1,split)
        at=compare_original_pair_and_directed(sources,targets,K,split)
        if previous["true_original_exact_uniform_local_excess"]!=0:
            raise AssertionError("W32 K-1 expected globally tight true uniform cut")
        if at["true_original_exact_uniform_Delta6"]!=0:
            raise AssertionError("W32 K exact uniform should be zero")
        rows.append({
            "scheme":scheme,
            "C":sum(sources.values()),
            "E":sum(split["endpoint"].values()),
            "I":sum(split["internal"].values()),
            "S_complete_TRUE_GQ_seven_GF5_positive":len(targets),
            "full_original_K":K,
            "K_minus_one":previous,
            "K_at_minimum":at,
        })
    return {
        "slice":"HYP105-ISSUE230-D6L-DIRECTED-ORIGINAL-TRIPLE-CALIBRATION",
        "all_finite_exact_directed_cut_duality":"PROVED",
        "all_h_uniform_K":"OPEN",
        "root_Branch_A_B":"OPEN",
        "W34_W38_complete_seven_S":"UNKNOWN-NO-BB-SUBSTITUTION",
        "genuine_complete_original_W32_cases":rows,
    }


if __name__=="__main__":
    print(json.dumps(finite_genuine_W32_directed_report(),indent=2,sort_keys=True))
