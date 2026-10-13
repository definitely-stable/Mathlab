"""HYP-105 #230 D6-H: all-h SUFFICIENT incidence-budget transport bound.

For three-incidence ORIGINAL source triples T with integer oriented multiplicity
w(T), and true accepted ORIGINAL six-incidence recipients Q, choose a
nonnegative recipient-to-incidence allocation a(Q,e), supported on e in Q,
with sum_e a(Q,e) <= K. The source -> T -> e -> sink flow with incidence
capacity sum_{Q contains e} a(Q,e) embeds into the original D6-D transport
network, hence its deficit is a rigorous UPPER bound on the minimal
exception budget D_K. This is not a universal assertion that the bound is
small for arbitrary original global maps.

The uniform allocation a(Q,e)=K/6 uses integer scale six. Additional
integral concentrated allocations choose one original incidence per Q.
All source demands contain both E and internal-only I components.
"""
from collections import Counter
from math import floor
import json

from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6d_incidence_factored_charging import _validated
from hyp105_issue230_d6e_support_expansion_profile import _normalise_split


def _incidence_bipartite_flow(weights, e_capacities, scale):
    """Integral T->e capacity flow; all capacities expressed in scale units."""
    triples = sorted(weights)
    incidences = sorted({e for t in triples for e in t})
    idx = {e: j for j, e in enumerate(incidences)}
    first_triple = 1
    first_inc = first_triple + len(triples)
    sink = first_inc + len(incidences)
    graph = _Dinic(sink + 1)
    total_scaled = scale * sum(weights.values())
    infinite = total_scaled + 1
    for j, t in enumerate(triples):
        graph.edge(0, first_triple + j, scale * weights[t])
        for e in t:
            graph.edge(first_triple + j, first_inc + idx[e], infinite)
    for e in incidences:
        graph.edge(first_inc + idx[e], sink, e_capacities.get(e, 0))
    delivered = graph.maxflow(0, sink)
    if not 0 <= delivered <= total_scaled:
        raise AssertionError("source/incidence flow conservation violation")
    return delivered


def incidence_budget_certificate(source_weights, accepted, K, split_weights=None):
    """All-h theorem instance: upper bound on the EXACT D6-F exception D_K.

    - UNIFORM: each sixset reserves K/6 of its capacity for EACH of its six
      original incidences, independent of source path orientation.
    - PRESSURE: each sixset gives its K slots to the incidence with largest
      incident source weight L(e) (fixed lexicographic ties).
    - GREEDY: each sixset gives K slots to the incidence with largest
      still-uncovered load, an explicit finite deterministic construction.
    The latter two use integral capacities. None claims optimality.
    """
    if type(K) is not int or K < 0:
        raise ValueError("K must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    splits = _normalise_split(source_weights, split_weights)
    total = sum(source_weights.values())
    load = Counter()
    component_loads = {}
    for name, masses in splits.items():
        part = Counter()
        for t, weight in masses.items():
            if weight:
                part.update({e: weight for e in t})
        component_loads[name] = part
        load.update(part)
    if sum(load.values()) != 3 * total:
        raise AssertionError("three-incidence mass identity violated")
    d = Counter(e for q in sixsets for e in q)
    if sum(d.values()) != 6 * len(sixsets):
        raise AssertionError("six-incidence recipient degree identity violated")

    uniform_caps = {e: K * d[e] for e in d}
    uniform_delivered_scaled = _incidence_bipartite_flow(
        source_weights, uniform_caps, 6)
    uniform_exception_scaled = 6 * total - uniform_delivered_scaled
    uniform_exception_upper = uniform_exception_scaled // 6

    # Explicit equal 1/3 distribution of every source path to its three
    # incidences is a feasible fractional T->e plan before truncation.
    equal_split_overflow_scaled = sum(
        max(0, 2 * load[e] - K * d[e]) for e in load
    )
    if uniform_exception_scaled > equal_split_overflow_scaled:
        raise AssertionError("optimized incidence flow worse than equal split")

    def integral_orientation(greedy):
        counts = Counter()
        remaining = Counter(load)
        for q in sixsets:
            if greedy:
                chosen = min(q, key=lambda e: (
                    -max(0, remaining[e]), -load[e], e))
            else:
                chosen = min(q, key=lambda e: (-load[e], e))
            counts[chosen] += 1
            remaining[chosen] -= K
        if sum(counts.values()) != len(sixsets):
            raise AssertionError("each original recipient must be used once")
        capacities = {e: K * n for e, n in counts.items()}
        delivered = _incidence_bipartite_flow(source_weights, capacities, 1)
        return {
            "source_mass_routable_with_fixed_orientation": delivered,
            "certified_integer_exception_upper": total - delivered,
            "distinct_chosen_original_incidences": len(counts),
        }

    pressure = integral_orientation(False)
    greedy = integral_orientation(True)
    upper = min(
        uniform_exception_upper,
        pressure["certified_integer_exception_upper"],
        greedy["certified_integer_exception_upper"],
    )
    component_sums = {name: sum(masses.values()) for name, masses in splits.items()}
    if sum(component_sums.values()) != total:
        raise AssertionError("endpoint/internal components failed to add up")
    result = {
        "scope": "SUFFICIENT-UPPER-BOUND-ALL-FINITE-ORIGINAL-INCIDENCE-SYSTEMS",
        "K": K,
        "C": total,
        "S_recipient_sixsets": len(sixsets),
        "component_source_masses": component_sums,
        "source_incidence_load_sum": sum(load.values()),
        "positive_target_incidence_degree_sum": sum(d.values()),
        "source_incidences_without_positive_target": sum(
            1 for e in load if not d[e]
        ),
        "max_endpoint_or_internal_joint_load": max(load.values(), default=0),
        "uniform": {
            "scale": 6,
            "routable_mass_scaled": uniform_delivered_scaled,
            "exception_scaled": uniform_exception_scaled,
            "certified_integer_exception_upper": uniform_exception_upper,
            "equal_source_thirds_overflow_scaled": equal_split_overflow_scaled,
            "equal_source_thirds_exception_upper": equal_split_overflow_scaled // 6,
            "pointwise_incidence_domination_holds": all(
                2 * load[e] <= K * d[e] for e in load
            ),
        },
        "largest_load_orientation": pressure,
        "greedy_remaining_load_orientation": greedy,
        "best_certified_exception_upper": upper,
        "exact_D6F_exception_is_at_most_this_upper": True,
        "universal_h_independent_K_or_small_exception_proved": False,
    }
    if not 0 <= upper <= total:
        raise AssertionError("invalid certified exception upper bound")
    if result["uniform"]["pointwise_incidence_domination_holds"] and upper != 0:
        raise AssertionError("pointwise 2 L(e) <= K d(e) must close all sources")
    return result


def _complete_w32_inputs(scheme):
    from hyp105_issue230_projection import ProjectionClosure, fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_issue230_d6b_coherent_pruning import full_retention
    from hyp105_issue230_d6e_support_expansion_profile import (
        split_blocked_sources_by_endpoint_internal,
    )
    model = fixture(1, scheme)
    core = ProjectionClosure(model)
    targets = seven_census(model, independent_checks=True, witness_sets=True)["sets"]
    src = split_blocked_sources_by_endpoint_internal(core, full_retention(core))
    return targets, src["sources"], src["split"]


def finite_w32_certificate_report():
    """Only W32 has the COMPLETE accepted seven-family enumeration here."""
    from hyp105_issue230_d6f_exception_budget_oracle import (
        exception_budget_for_capacity,
    )
    from hyp105_issue230_d6d_incidence_factored_charging import factored_frontier
    rows = []
    for scheme in ("lex", "reverse", "S68", "S72"):
        targets, source, parts = _complete_w32_inputs(scheme)
        optimum = factored_frontier(source, targets)
        if optimum["optimal_K"] is None:
            raise AssertionError("genuine full-seven W32 zero-exception K missing")
        k0 = optimum["optimal_K"]
        measured = []
        for k in sorted(set((max(0, k0 - 1), k0))):
            certificate = incidence_budget_certificate(source, targets, k, parts)
            exact = exception_budget_for_capacity(source, targets, k, parts)
            if exact["minimal_exception_mass"] > certificate[
                "best_certified_exception_upper"
            ]:
                raise AssertionError("D6-H analytical sufficient upper violated")
            measured.append({
                "K": k,
                "exact_D6F_exception": exact["minimal_exception_mass"],
                "certificates": certificate,
            })
        rows.append({
            "scheme": scheme,
            "true_original_complete_seven_S": len(targets),
            "blocked_C": sum(source.values()),
            "E": sum(parts["endpoint"].values()),
            "I": sum(parts["internal"].values()),
            "D6D_optimal_K": k0,
            "capacity_rows": measured,
        })
    return {
        "slice": "HYP105-ISSUE230-D6H-INCIDENCE-BUDGET-SUFFICIENT-CERTIFICATE",
        "all_h_incidence_budget_upper_theorem": "PROVED",
        "all_h_uniform_K": "OPEN",
        "all_h_exception_small_o_s6": "OPEN",
        "root_branch_A_or_B": "OPEN",
        "W34_W38_full_seven_S": "UNKNOWN",
        "W32_true_original_complete_seven_cases": rows,
    }


if __name__ == "__main__":
    print(json.dumps(finite_w32_certificate_report(), indent=2, sort_keys=True))
