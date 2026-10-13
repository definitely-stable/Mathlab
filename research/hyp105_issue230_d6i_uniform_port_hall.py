"""HYP-105 #230 D6-I: exact ALL-h Hall dual of the UNIFORM D6-H port budget.

The *restricted* rational transport reserves K/6 slots at each of six
ORIGINAL incidences in every actual accepted ORIGINAL sixset Q. Multiply
all source and port capacities by six. The resulting T->e flow is integral.

Its deficit Delta6=6*C-flow6 has the exact source-closed support dual

    Delta6 = max_F (6*M(F)-K*D(F))_+,
    D(F)=sum_{e in F}d_A(e)=sum_{Q in A}|Q intersect F|.

This is an exact theorem for the RESTRICTED uniform-port relaxation,
NOT an equivalence for the full original T->e->Q network. The true D6-F
integer exception D_K is bounded above by floor(Delta6/6), potentially
strictly. Original E and internal-only I share one source weight w(T).

The full seven-class accepted-positive target pool is available ONLY for
true same-map W(3,2) cases in the accompanying report. No fabricated S
for W(3,4) or W(3,8).
"""
from collections import Counter
from math import ceil
import json

from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6d_incidence_factored_charging import _validated
from hyp105_issue230_d6e_support_expansion_profile import _normalise_split


def positive_port_degrees(accepted):
    """True ORIGINAL target-incidence degrees, preserving target identity."""
    _, sixsets = _validated({}, accepted)
    d = Counter(e for q in sixsets for e in q)
    if sum(d.values()) != 6 * len(sixsets):
        raise AssertionError("original sixset-to-incidence double count invalid")
    return d


def source_closed_port_profile(source_weights, accepted, incidence_support,
                               split_weights=None, *, candidate_K=None):
    """Independent direct arithmetic for any proposed ORIGINAL support F.

    Inert incidence IDs in raw F are deliberately removed. Only active
    original source triples T subset F define the source-closed family;
    its active union is the true Hall neighborhood's incidence support.
    """
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    F = set(incidence_support)
    if any(type(e) is not int or e < 0 for e in F):
        raise ValueError("F contains a non-ORIGINAL nonnegative integer ID")
    if candidate_K is not None and (type(candidate_K) is not int or candidate_K < 0):
        raise ValueError("K must be a nonnegative integer")
    active = [t for t in triples if set(t) <= F]
    active_union = {e for t in active for e in t}
    degrees = Counter(e for q in sixsets for e in q)
    M = sum(source_weights[t] for t in active)
    D = sum(degrees[e] for e in active_union)
    profiles = {
        name: sum(weights[t] for t in active)
        for name, weights in split.items()
    }
    if sum(profiles.values()) != M:
        raise AssertionError("endpoint/internal paths double spent")
    return {
        "input_original_incidence_set_size": len(F),
        "active_original_source_triples": len(active),
        "original_active_incidence_support": sorted(active_union),
        "active_incidence_count": len(active_union),
        "oriented_source_mass_M": M,
        "split_oriented_source_mass": profiles,
        "positive_port_degree_sum_D": D,
        "positive_target_incidence_memberships_on_F": D,
        "recipient_sixsets_touching_F": sum(
            bool(active_union.intersection(q)) for q in sixsets
        ),
        "exact_port_capacity_floor_K": (
            0 if not M else ceil(6 * M / D) if D else None
        ),
        "zero_denominator_positive_mass": M > 0 and D == 0,
        "candidate_K": candidate_K,
        "signed_scaled_Hall_deficit": (
            6 * M - candidate_K * D if candidate_K is not None else None
        ),
        "positive_scaled_Hall_deficit": (
            max(0, 6 * M - candidate_K * D)
            if candidate_K is not None else None
        ),
    }


def uniform_port_hall_cut(source_weights, accepted, K, split_weights=None):
    """Solve the exact restricted uniform port flow and reconstruct mincut.

    Edges T->e have capacity six*C+1, so NO minimum cut with value <=6*C
    can split an original triple from its original incidence endpoints.
    Every source-side residual e has an original reachable source triple
    parent. The residual T set is source-closed under its e union.
    """
    if type(K) is not int or K < 0:
        raise ValueError("K must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    deg = positive_port_degrees(accepted)
    C = sum(source_weights.values())
    inc = sorted({e for t in triples for e in t})
    index = {e: i for i, e in enumerate(inc)}
    first_T = 1
    first_e = first_T + len(triples)
    sink = first_e + len(inc)
    graph = _Dinic(sink + 1)
    INF = 6 * C + 1
    for i, t in enumerate(triples):
        graph.edge(0, first_T + i, 6 * source_weights[t])
        for e in t:
            graph.edge(first_T + i, first_e + index[e], INF)
    for e in inc:
        graph.edge(first_e + index[e], sink, K * deg[e])
    V6 = graph.maxflow(0, sink)
    if V6 < 0 or V6 > 6 * C:
        raise AssertionError("scaled uniform flow exceeds source mass")
    reachable = graph.reachable(0)
    active = [t for i, t in enumerate(triples) if first_T + i in reachable]
    F = {e for t in active for e in t}
    residual_inc = {e for e in inc if first_e + index[e] in reachable}
    if F != residual_inc:
        raise AssertionError("source-side residual port support inconsistent")
    if any((set(t) <= F) != (t in active) for t in triples):
        raise AssertionError("minimum residual source support is not closed")

    independent = source_closed_port_profile(
        source_weights, accepted, F, split, candidate_K=K
    )
    cut_mass = independent["oriented_source_mass_M"]
    cut_ports = independent["positive_port_degree_sum_D"]
    Delta6 = 6 * C - V6
    deficit = 6 * cut_mass - K * cut_ports
    if Delta6 != deficit or Delta6 < 0:
        raise AssertionError("exact scaled Hall mincut arithmetic differs")
    # The original rational recipient slots are feasible in the FULL
    # factored D6-D graph, which has integer maxflow. Thus floor, not ceil.
    bound = Delta6 // 6
    return {
        "scope": "EXACT-UNIFORM-PORT-HALL-DUAL-NOT-FULL-ORIGINAL-HALL",
        "K": K,
        "oriented_source_total_C": C,
        "accepted_original_sixsets_S": len(sixsets),
        "all_positive_target_port_memberships": 6 * len(sixsets),
        "six_scaled_source_total": 6 * C,
        "six_scaled_uniform_port_flow_V6": V6,
        "exact_uniform_scaled_Hall_deficit_Delta6": Delta6,
        "original_D6F_integer_exception_upper_floor_Delta6_div6": bound,
        "uniform_restricted_full_rational_transport": Delta6 == 0,
        "mincut": {
            "source_closed_original_incidence_support_F": sorted(F),
            "source_closed_triples": len(active),
            "source_closed_oriented_mass_M": cut_mass,
            "source_closed_split_E_I": independent["split_oriented_source_mass"],
            "original_positive_port_boundary_D": cut_ports,
            "positive_original_sixsets_touching_F": independent[
                "recipient_sixsets_touching_F"],
            "six_M_minus_K_D": deficit,
            "scaled_flow_shortfall": Delta6,
            "profile": independent,
        },
        "all_h_uniform_K_established": False,
        "actual_original_Branch_A_or_B": "OPEN",
    }


def uniform_port_zero_exception_capacity(source_weights, accepted,
                                         split_weights=None):
    """Exact minimum integer K for the *uniform* rational port restriction.

    If a source triple has NO positive incidence in any Q, it is
    unsupported even at unbounded K. Otherwise K=6*C is sufficient,
    since every such incident port has rational capacity at least C.
    """
    triples, _ = _validated(source_weights, accepted)
    deg = positive_port_degrees(accepted)
    C = sum(source_weights.values())
    unsupported = [t for t in triples if not any(deg[e] for e in t)]
    if unsupported:
        return {
            "status": "NO-FINITE-UNIFORM-K-UNSUPPORTED-TRUE-SOURCE",
            "uniform_minimum_K": None,
            "unsupported_original_triples": len(unsupported),
            "unsupported_oriented_mass": sum(source_weights[t] for t in unsupported),
            "first_unsupported_original_source_triple": list(unsupported[0]),
        }
    if not C:
        return {
            "status": "EMPTY-SOURCE-NO-INFERENCE",
            "uniform_minimum_K": 0,
            "at_K_certificate": uniform_port_hall_cut(
                source_weights, accepted, 0, split_weights
            ),
        }
    lo, hi = 0, 6 * C
    if uniform_port_hall_cut(source_weights, accepted, hi, split_weights)[
        "exact_uniform_scaled_Hall_deficit_Delta6"
    ] != 0:
        raise AssertionError("supported triple failed at K=6*C")
    while lo < hi:
        mid = (lo + hi) // 2
        deficit = uniform_port_hall_cut(
            source_weights, accepted, mid, split_weights
        )["exact_uniform_scaled_Hall_deficit_Delta6"]
        if deficit == 0:
            hi = mid
        else:
            lo = mid + 1
    at_K = uniform_port_hall_cut(source_weights, accepted, lo, split_weights)
    previous = uniform_port_hall_cut(
        source_weights, accepted, lo - 1, split_weights
    )
    if lo < 1 or previous["exact_uniform_scaled_Hall_deficit_Delta6"] <= 0:
        raise AssertionError("unrestricted uniform minimum K falsified")
    return {
        "status": "EXACT-MINIMUM-UNIFORM-PORT-ALL-SOURCE-K",
        "uniform_minimum_K": lo,
        "at_K_certificate": at_K,
        "K_minus_one_strict_source_closed_port_cut": previous,
        "universal_bound_on_K_proved": False,
    }


def finite_w32_port_report():
    """Four true W32 same-map COMPLETE seven positive ORIGINAL recipient pools."""
    from hyp105_issue230_d6h_incidence_budget_certificate import (
        _complete_w32_inputs, incidence_budget_certificate,
    )
    from hyp105_issue230_d6d_incidence_factored_charging import factored_frontier
    from hyp105_issue230_d6f_exception_budget_oracle import exception_budget_for_capacity
    rows = []
    for scheme in ("lex", "reverse", "S68", "S72"):
        targets, source, components = _complete_w32_inputs(scheme)
        original = factored_frontier(source, targets)
        restriction = uniform_port_zero_exception_capacity(
            source, targets, components
        )
        original_K = original["optimal_K"]
        uniform_K = restriction["uniform_minimum_K"]
        if original_K is None or uniform_K < original_K:
            raise AssertionError("uniform restriction beat full original optimal K")
        finite = []
        for K in (original_K - 1, original_K):
            profile = uniform_port_hall_cut(source, targets, K, components)
            old = incidence_budget_certificate(source, targets, K, components)
            exact = exception_budget_for_capacity(source, targets, K, components)
            bound = profile[
                "original_D6F_integer_exception_upper_floor_Delta6_div6"
            ]
            if (bound != old["uniform"]["certified_integer_exception_upper"]
                    or bound < exact["minimal_exception_mass"]):
                raise AssertionError("D6-I mincut disagrees with independent D6-H flow")
            finite.append({
                "K": K,
                "D6F_exact_exception": exact["minimal_exception_mass"],
                "D6H_uniform_exception_upper": bound,
                "port_cut": profile,
            })
        rows.append({
            "scheme": scheme,
            "source_scope": "COMPLETE-TRUE-ORIGINAL-W32-FULL-G",
            "target_scope": "FULL-SEVEN-ORIGINAL-GF5-POSITIVE-ONLY-W32",
            "C": sum(source.values()),
            "E": sum(components["endpoint"].values()),
            "I": sum(components["internal"].values()),
            "S": len(targets),
            "D6D_exact_full_original_minimum_K": original_K,
            "D6I_uniform_restricted_minimum_K": uniform_K,
            "uniform_K_extra_over_full_original_K": uniform_K - original_K,
            "capacity_cases": finite,
        })
    return {
        "slice": "HYP105-ISSUE230-D6I-EXACT-UNIFORM-PORT-WEIGHTED-HALL",
        "all_h_uniform_port_Hall_equivalence": "PROVED-RESTRICTED-FINITE-SYSTEMS",
        "all_h_uniform_K": "OPEN",
        "all_h_original_accepted_seven_S_lower": "OPEN",
        "root_Branch_A_or_B": "OPEN",
        "W34_W38_full_positive_seven_S": "UNKNOWN-NO-BB-SUBSTITUTION",
        "genuine_W32_complete_seven_cases": rows,
    }


if __name__ == "__main__":
    print(json.dumps(finite_w32_port_report(), indent=2, sort_keys=True))
