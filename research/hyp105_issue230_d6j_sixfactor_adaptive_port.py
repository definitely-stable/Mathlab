"""HYP-105 #230 D6-J: sharp six-factor FULL vs uniform port equivalence.

TRUE original source triple T / positive accepted recipient sixset Q and
the D6-D one-common-incidence rule are used throughout. Uniform D6-I
reserves K/6 from each Q at each original port; adaptive port budgets
are extracted as exact integral edge flows from the full factored
network. Both E and I source parts share the SAME K slots.

For any finite incidence system and K>=0, write Vfull(K) for the exact
integral full flow, V6(K) for D6-I six-scaled restricted uniform flow:

    V6(K) <= 6*Vfull(K) <= V6(6*K).

Thus with U(K)=(6*C-V6(K))//6 and Dfull(K)=C-Vfull(K):

    U(6*K) <= Dfull(K) <= U(K).

For fully supported nonempty instances:
    Kfull <= Kuniform <= 6*Kfull.
The factor 6 is globally optimal (singleton overlap T intersect Q={e}).

This is an ALL-h comparison of transport models, NOT the all-h
GF(5) positive-sixset growth theorem, a fixed uniform K theorem, or
a replacement of complete true W34 targets by BB-only witnesses.
"""
from collections import Counter
import json

from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6d_incidence_factored_charging import (
    _validated, factored_frontier,
)
from hyp105_issue230_d6e_support_expansion_profile import _normalise_split
from hyp105_issue230_d6i_uniform_port_hall import (
    uniform_port_hall_cut, uniform_port_zero_exception_capacity,
)


def adaptive_original_port_certificate(source_weights, accepted, K,
                                       split_weights=None):
    """Recover an OPTIMAL integer recipient-to-ORIGINAL-port allocation.

    Each a(Q,e) is the *actual edge flow* from original incidence e to
    original positive Q in the full D6-D network. The source->T->e
    network whose incidence sink capacity is c(e)=sum_Q a(Q,e)
    reproduces exactly the same optimal value; conversely every legal
    incidence allocation embeds in the original D6-D network.

    The port-source flow and recipient allocation are therefore a
    primal feasibility witness; original maxflow/mincut supplies
    optimality. For compact JSON reports we retain only nonzero
    allocations with typed original IDs.
    """
    if type(K) is not int or K < 0:
        raise ValueError("nonnegative integer recipient capacity required")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    C = sum(source_weights.values())
    incidences = sorted({e for t in triples for e in t} |
                        {e for q in sixsets for e in q})
    e_index = {e: i for i, e in enumerate(incidences)}
    first_t = 1
    first_e = first_t + len(triples)
    first_q = first_e + len(incidences)
    sink = first_q + len(sixsets)
    flow = _Dinic(sink + 1)
    INF = C + 1

    def recorded_edge(u, v, cap):
        i = len(flow.graph[u])
        flow.edge(u, v, cap)
        return (u, i, cap)

    def sent(record):
        u, i, original = record
        current = flow.graph[u][i][1]
        amount = original - current
        if amount < 0 or amount > original:
            raise AssertionError("invalid residual ORIGINAL primal arc")
        return amount

    te_edges = []
    eq_edges = []
    qout_edges = []
    for i, t in enumerate(triples):
        recorded_edge(0, first_t + i, source_weights[t])
        for e in t:
            te_edges.append((i, e, recorded_edge(
                first_t + i, first_e + e_index[e], INF)))
    for j, q in enumerate(sixsets):
        for e in q:
            eq_edges.append((e, j, recorded_edge(
                first_e + e_index[e], first_q + j, INF)))
        qout_edges.append(recorded_edge(first_q + j, sink, K))

    full_value = flow.maxflow(0, sink)
    source_to_e = Counter()
    incoming_e = Counter()
    for i, e, edge in te_edges:
        mass = sent(edge)
        if mass:
            source_to_e[(triples[i], e)] = mass
            incoming_e[e] += mass
    recipient_a = {}
    outbound_e = Counter()
    recipient_loads = Counter()
    for e, j, edge in eq_edges:
        mass = sent(edge)
        if mass:
            recipient_a[(sixsets[j], e)] = mass
            outbound_e[e] += mass
            recipient_loads[sixsets[j]] += mass
    for j, edge in enumerate(qout_edges):
        if sent(edge) != recipient_loads[sixsets[j]]:
            raise AssertionError("ORIGINAL recipient flow conservation broken")
    if incoming_e != outbound_e:
        raise AssertionError("ORIGINAL incidence-port conservation broken")
    if sum(incoming_e.values()) != full_value:
        raise AssertionError("original exact source flow differs from port ledger")
    if any(recipient_loads[q] > K for q in sixsets):
        raise AssertionError("original recipient K budget double-spent")
    if any(sum(m for (q2, e), m in recipient_a.items() if q2 == q) >
           K for q in sixsets):
        raise AssertionError("adaptive allocation violates recipient simplex")

    # Check that the extracted exact optimal adaptive capacities suffice
    # WITHOUT consulting any recipient geometry in this surrogate.
    sources_base = 1
    port_base = sources_base + len(triples)
    small_sink = port_base + len(incidences)
    reduced = _Dinic(small_sink + 1)
    for i, t in enumerate(triples):
        reduced.edge(0, sources_base + i, source_weights[t])
        for e in t:
            reduced.edge(sources_base + i, port_base + e_index[e], INF)
    for e in incidences:
        reduced.edge(port_base + e_index[e], small_sink, outbound_e[e])
    adaptive_value = reduced.maxflow(0, small_sink)
    if adaptive_value != full_value:
        raise AssertionError("optimal adaptive port restriction lost exact full flow")

    uniform_same = uniform_port_hall_cut(source_weights, accepted, K, split)
    uniform_times_six = uniform_port_hall_cut(
        source_weights, accepted, 6 * K, split)
    V6_K = uniform_same["six_scaled_uniform_port_flow_V6"]
    V6_6K = uniform_times_six["six_scaled_uniform_port_flow_V6"]
    if V6_K > 6 * full_value or V6_6K < 6 * full_value:
        raise AssertionError("sharp all-h six-factor flow sandwich falsified")
    exact_D = C - full_value
    U_at_K = uniform_same[
        "original_D6F_integer_exception_upper_floor_Delta6_div6"]
    U_at_6K = uniform_times_six[
        "original_D6F_integer_exception_upper_floor_Delta6_div6"]
    if not U_at_6K <= exact_D <= U_at_K:
        raise AssertionError("integer six-factor exception sandwich falsified")

    deg = Counter(e for q in sixsets for e in q)
    # An original full-flow witness scaled by six is feasible at uniform
    # parameter 6K: incidence cap is (6K)*deg(e), while its delivered
    # witness load is 6*incoming_e[e] <= 6K*deg(e).
    if any(incoming_e[e] > K * deg[e] for e in incidences):
        raise AssertionError("full witness cannot embed at uniform parameter 6K")
    return {
        "scope": "ALL-FINITE-ALL-H-SHARP-SIX-FACTOR-TRANSPORT-SANDWICH",
        "K": K,
        "C": C,
        "original_recipient_count_S": len(sixsets),
        "split_source_mass": {name: sum(w.values())
                              for name, w in split.items()},
        "full_original_exact_integral_flow": full_value,
        "full_original_exact_integer_exception": exact_D,
        "uniform_scaled_flow_at_K": V6_K,
        "uniform_scaled_flow_at_6K": V6_6K,
        "uniform_exception_upper_at_K": U_at_K,
        "uniform_exception_lower_at_6K": U_at_6K,
        "six_factor_flow_sandwich": True,
        "six_factor_exception_sandwich": True,
        "adaptive_primal": {
            "optimal_port_restricted_flow": adaptive_value,
            "nonzero_recipient_incidence_allocations": len(recipient_a),
            "nonzero_source_incidence_assignments": len(source_to_e),
            "recipient_budget_used": sum(recipient_loads.values()),
            "port_load_sum": sum(incoming_e.values()),
            "active_original_source_incidences": sorted(
                e for e in incidences if incoming_e[e]),
            "per_port_capacities": [[e, outbound_e[e]]
                                    for e in incidences if outbound_e[e]],
            "per_recipient_port_allocation": [
                {"original_sixset": list(q), "original_incidence": e,
                 "allocated_integer_K_slots": n}
                for (q, e), n in sorted(recipient_a.items())
            ],
            "per_source_port_assignment": [
                {"original_source_triple": list(t), "original_incidence": e,
                 "routed_oriented_mass": n}
                for (t, e), n in sorted(source_to_e.items())
            ],
        },
        "all_h_fixed_K_or_Branch_A_proved": False,
        "root_Branch_A_or_B": "OPEN",
    }


def sharp_six_factor_capacity_frontier(source_weights, accepted,
                                       split_weights=None):
    """Compute true and restricted minimum K and verify the sharp bound."""
    triples, _ = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    full = factored_frontier(source_weights, accepted)
    uniform = uniform_port_zero_exception_capacity(
        source_weights, accepted, split)
    full_K = full["optimal_K"]
    uniform_K = uniform["uniform_minimum_K"]
    if not triples:
        if full_K is not None or uniform_K != 0:
            raise AssertionError("empty original source semantics changed")
        return {
            "status": "EMPTY-SOURCE-NO-INFERENCE",
            "full_original_K": None,
            "uniform_original_K": 0,
        }
    if full_K is None:
        if uniform_K is not None:
            raise AssertionError("uniform supported source but full unsupported")
        return {
            "status": "NO-FINITE-K-UNSUPPORTED-SOURCE",
            "full_original_K": None,
            "uniform_original_K": None,
        }
    if uniform_K is None or not full_K <= uniform_K <= 6 * full_K:
        raise AssertionError("sharp uniform/full K sandwich violated")
    return {
        "status": "SHARP-SIX-FACTOR-UNIFORM-FULL-CAPACITY-EQUIVALENCE",
        "full_original_K": full_K,
        "uniform_original_K": uniform_K,
        "uniform_to_full_congestion_ratio_exact": [
            uniform_K, full_K],
        "at_full_K": adaptive_original_port_certificate(
            source_weights, accepted, full_K, split),
        "universal_six_factor_sharp": True,
        "all_h_uniform_bounded_K_automatically_proved": False,
    }


def genuine_W32_six_factor_report():
    """True original W32 complete GF5 seven-positive same-map comparator."""
    from hyp105_issue230_d6h_incidence_budget_certificate import (
        _complete_w32_inputs,
    )
    rows = []
    for scheme in ("lex", "reverse", "S68", "S72"):
        positive, weights, split = _complete_w32_inputs(scheme)
        frontier = sharp_six_factor_capacity_frontier(weights, positive, split)
        if frontier["status"] != "SHARP-SIX-FACTOR-UNIFORM-FULL-CAPACITY-EQUIVALENCE":
            raise AssertionError("true original W32 should be fully supported")
        cert = frontier["at_full_K"]
        rows.append({
            "scheme": scheme,
            "C": sum(weights.values()),
            "S": len(positive),
            "E": sum(split["endpoint"].values()),
            "I": sum(split["internal"].values()),
            "K_full": frontier["full_original_K"],
            "K_uniform": frontier["uniform_original_K"],
            "full_exact_exception_at_K_full": cert[
                "full_original_exact_integer_exception"],
            "six_factor_lower_upper_at_K_full": [
                cert["uniform_exception_lower_at_6K"],
                cert["uniform_exception_upper_at_K"],
            ],
            "nonzero_optimal_adaptive_recipient_port_allocations": cert[
                "adaptive_primal"]["nonzero_recipient_incidence_allocations"],
            "port_budget_used": cert["adaptive_primal"]["port_load_sum"],
        })
    return {
        "slice": "HYP105-ISSUE230-D6J-SHARP-SIX-FACTOR-ADAPTIVE-PORT",
        "universal_six_factor_sandwich": "PROVED-ALL-FINITE-SYSTEMS",
        "optimal_adaptive_recipient_port_allocation": "EXACT-INTEGRAL-WITNESS",
        "W34_W38_full_seven_original_positive_S": "UNKNOWN-NO-BB-SUBSTITUTION",
        "all_h_fixed_K": "OPEN",
        "root_Branch_A_or_B": "OPEN",
        "genuine_complete_seven_W32_cases": rows,
    }


if __name__ == "__main__":
    print(json.dumps(genuine_W32_six_factor_report(), indent=2, sort_keys=True))
