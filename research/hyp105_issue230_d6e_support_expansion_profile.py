"""HYP-105 #230 D6-E: source-closed support expansion profile.

D6-D reduced one-incidence repair to the exact weighted Hall condition

    M(F) <= K * B(F)

for source-closed ORIGINAL incidence supports F. This slice does NOT prove a
uniform all-h K. It makes the analytic obstruction explicit and testable:
for a chosen support F it reports the exact endpoint/internal source mass,
the positive sixset boundary B(F), the local required K, and the source-closed
profile induced by a factorized Hall mincut.

Complete seven-positive targets are used only for true W32 finite instances.
No W34 BB-only subset is substituted for the unknown full seven-family S.
"""
from collections import Counter
from math import ceil
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6b_coherent_pruning import (
    _edge,
    _bits_from_original_endpoints,
    original_diagonals,
    full_retention,
    retained_path_census,
)
from hyp105_issue230_d6c_local_charge_hall import _Dinic
from hyp105_issue230_d6d_incidence_factored_charging import (
    _validated,
    factored_frontier,
)


def _normalise_split(source_weights, split_weights):
    triples, _ = _validated(source_weights, {})
    source = Counter({t: source_weights[t] for t in triples})
    if split_weights is None:
        return {"total": Counter(source)}
    if not isinstance(split_weights, dict) or not split_weights:
        raise ValueError("split_weights must be a nonempty mapping of name -> Counter")
    result = {}
    for name, weights in split_weights.items():
        if not isinstance(name, str) or not name:
            raise ValueError("split category names must be nonempty strings")
        c = Counter(weights)
        for t, value in c.items():
            if t not in source:
                raise ValueError("split contains a source triple absent from source_weights")
            if type(value) is not int or value < 0:
                raise ValueError("split weights must be nonnegative integers")
        result[name] = c
    for t, value in source.items():
        if sum(result[name][t] for name in result) != value:
            raise ValueError("split weights must add exactly to every source demand")
    return result


def _split_totals(split_weights, active_triples):
    return {name: sum(weights[t] for t in active_triples)
            for name, weights in split_weights.items()}


def source_closed_support_profile(source_weights, accepted, incidence_set,
                                  split_weights=None, *, candidate_K=None):
    """Evaluate exact source-closed Hall data for one ORIGINAL support F.

    The analytic reduction checks the source-closed family U_F={T:T subset F}.
    Its true denominator is computed from the *active* source incidence union,
    not from irrelevant incidences in raw F. Adding incidences that support no
    source triple must not artificially improve the bound.
    """
    if candidate_K is not None and (type(candidate_K) is not int or candidate_K < 0):
        raise ValueError("candidate_K must be a nonnegative integer or None")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    F = set(incidence_set)
    if any(type(e) is not int or e < 0 for e in F):
        raise ValueError("incidence_set must contain nonnegative ORIGINAL incidence ids")

    active = [t for t in triples if set(t) <= F]
    active_union = {e for t in active for e in t}
    demand = sum(source_weights[t] for t in active)
    boundary = [q for q in sixsets if active_union.intersection(q)]
    B = len(boundary)
    if demand == 0:
        local_K = 0
    elif B == 0:
        local_K = None
    else:
        local_K = ceil(demand / B)
    excess = None
    if candidate_K is not None:
        excess = max(0, demand - candidate_K * B)
    return {
        "raw_original_incidence_set_size": len(F),
        "active_source_closed_triples": len(active),
        "active_original_incidence_union_size": len(active_union),
        "source_closed_oriented_demand": demand,
        "split_source_demand": _split_totals(split, active),
        "eligible_positive_original_sixsets_B": B,
        "minimal_K_required_by_this_F": local_K,
        "denominator_zero_with_positive_demand": demand > 0 and B == 0,
        "candidate_K": candidate_K,
        "excess_over_candidate_K": excess,
        "active_original_incidence_union_example": sorted(active_union)[:20],
        "source_closed_uses_active_union_denominator": True,
    }


def factored_cut_profile(source_weights, accepted, capacity, split_weights=None):
    """Return the exact factorized mincut and its source-closed F profile."""
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    total = sum(source_weights.values())
    if not total:
        return {"status": "EMPTY-SOURCE-NO-INFERENCE", "value": 0,
                "source_total": 0, "capacity": capacity}
    incs = sorted({e for t in triples for e in t} |
                  {e for q in sixsets for e in q})
    index = {e: i for i, e in enumerate(incs)}
    m = len(triples)
    n = len(incs)
    k = len(sixsets)
    source = 0
    t0 = 1
    i0 = t0 + m
    q0 = i0 + n
    sink = q0 + k
    flow = _Dinic(sink + 1)
    INF = total + 1
    for i, t in enumerate(triples):
        flow.edge(source, t0 + i, source_weights[t])
        for e in t:
            flow.edge(t0 + i, i0 + index[e], INF)
    for j, q in enumerate(sixsets):
        for e in q:
            flow.edge(i0 + index[e], q0 + j, INF)
        flow.edge(q0 + j, sink, capacity)
    value = flow.maxflow(source, sink)
    if value == total:
        return {
            "status": "COMPLETE-HALL-FEASIBLE",
            "capacity": capacity,
            "value": value,
            "source_total": total,
            "original_incidence_hubs": n,
            "explicit_transport_arcs": 3 * m + 6 * k,
        }

    reachable = flow.reachable(source)
    A = [i for i in range(m) if t0 + i in reachable]
    residual_union = {e for i in A for e in triples[i]}
    N = [j for j, q in enumerate(sixsets) if residual_union.intersection(q)]
    residual_demand = sum(source_weights[triples[i]] for i in A)
    residual_split = _split_totals(split, [triples[i] for i in A])
    deficit = residual_demand - capacity * len(N)
    if deficit <= 0 or deficit != total - value:
        raise AssertionError("factorized mincut did not certify the Hall shortfall exactly")
    profile = source_closed_support_profile(
        source_weights, accepted, residual_union, split, candidate_K=capacity
    )
    if profile["excess_over_candidate_K"] < deficit:
        raise AssertionError("source-closed support must be at least as obstructive as residual cut")
    return {
        "status": "EXACT-HALL-OBSTRUCTION",
        "capacity": capacity,
        "value": value,
        "source_total": total,
        "flow_shortfall": total - value,
        "residual_cut_source_triples": len(A),
        "residual_cut_oriented_demand": residual_demand,
        "residual_cut_split_demand": residual_split,
        "residual_cut_original_incidence_union_size": len(residual_union),
        "residual_cut_neighbor_positive_sixsets": len(N),
        "residual_cut_strict_deficit": deficit,
        "residual_cut_original_incidence_union_example": sorted(residual_union)[:20],
        "representative_residual_source_triples": [list(triples[i]) for i in A[:6]],
        "source_closed_profile": profile,
        "original_incidence_hubs": n,
        "explicit_transport_arcs": 3 * m + 6 * k,
    }


def split_blocked_sources_by_endpoint_internal(core, retention, *, max_walks=5_000_000):
    """Recover source triples and split their demand into endpoint/internal masks.

    Endpoint mass is exactly the D6B E atom (`mask & 5`). Internal-only mass
    is exactly the D6B I atom (`mask & 5 == 0 and mask & 10`). The routine is
    independent of D6-C's blocked_sources accumulator and is checked against
    retained_path_census before returning.
    """
    H = retention["adj"]
    a = core.a
    _, owners = original_diagonals(core)
    walk_budget = sum((len(H[u]) - 1) * (len(H[v]) - 1)
                      for u, row in enumerate(H) for v in row)
    if type(max_walks) is not int or max_walks < 0 or walk_budget > max_walks:
        raise ValueError("complete original physical P3 budget exceeded")
    endpoint = Counter()
    internal = Counter()
    by_mask = Counter()
    for v0, row in enumerate(H):
        x0, y0 = divmod(v0, a)
        for v1 in row:
            x1, y1 = divmod(v1, a)
            for v2 in H[v1]:
                x2, y2 = divmod(v2, a)
                if x2 in (x0, x1) or y2 in (y0, y1):
                    continue
                for v3 in H[v2]:
                    x3, y3 = divmod(v3, a)
                    if x3 in (x0, x1, x2) or y3 in (y0, y1, y2):
                        continue
                    q = core.fi.get(_edge(x0, x3))
                    r = core.gi.get(_edge(y0, y3))
                    if q is None or r is None or (q, r) in core.edge_id:
                        continue
                    mask = _bits_from_original_endpoints(
                        core, q, r, ((x0, x1, x2, x3), (y0, y1, y2, y3))
                    )
                    if not mask:
                        continue
                    triple = tuple(sorted((
                        owners[_edge(v0, v1)],
                        owners[_edge(v1, v2)],
                        owners[_edge(v2, v3)],
                    )))
                    if len(set(triple)) != 3:
                        raise AssertionError("proper original physical P3 repeats source incidence")
                    by_mask[mask] += 1
                    if mask & 5:
                        endpoint[triple] += 1
                    elif mask & 10:
                        internal[triple] += 1
                    else:
                        raise AssertionError("nonzero blocked mask must be endpoint or internal")
    independent = retained_path_census(core, retention, independent_endpoints=True)
    if sum(endpoint.values()) != independent["E_endpoint_bad_proper_P3"]:
        raise AssertionError("endpoint split does not match independent D6B E count")
    if sum(internal.values()) != independent["I_safe_endpoint_internal_only_proper_P3"]:
        raise AssertionError("internal split does not match independent D6B I count")
    if sum(by_mask.values()) != independent["C_joint_blocked_proper_P3"]:
        raise AssertionError("blocked split does not match independent D6B C count")
    for mask in range(1, 16):
        if by_mask[mask] != independent["exact_sixteen_mask_histogram"][mask]:
            raise AssertionError("split mask histogram disagrees with independent D6B census")
    sources = endpoint + internal
    return {
        "sources": sources,
        "split": {"endpoint": endpoint, "internal": internal},
        "mask_counts": by_mask,
        "independent": independent,
    }


def _w32_row(scheme):
    model = fixture(1, scheme)
    core = ProjectionClosure(model)
    accepted = seven_census(model, independent_checks=True, witness_sets=True)["sets"]
    split = split_blocked_sources_by_endpoint_internal(core, full_retention(core))
    sources = split["sources"]
    frontier = factored_frontier(sources, accepted)
    if frontier["status"] != "EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM":
        raise AssertionError("D6-E needs a supported complete all-seven W32 frontier")
    K = frontier["optimal_K"]
    global_F = {e for t in sources for e in t}
    global_profile = source_closed_support_profile(
        sources, accepted, global_F, split["split"], candidate_K=K
    )
    k_profile = factored_cut_profile(sources, accepted, K, split["split"])
    km1_profile = factored_cut_profile(sources, accepted, K - 1, split["split"])
    if k_profile["status"] != "COMPLETE-HALL-FEASIBLE":
        raise AssertionError("optimal K must be feasible")
    if km1_profile["status"] != "EXACT-HALL-OBSTRUCTION":
        raise AssertionError("K-1 must expose an exact Hall obstruction")
    if global_profile["minimal_K_required_by_this_F"] != K:
        raise AssertionError("finite W32 D6-D optimum no longer equals global source support floor")
    independent = split["independent"]
    return {
        "scheme": scheme,
        "s": core.s,
        "scope": "COMPLETE-ALL-SEVEN-ORIGINAL-W32",
        "C_blocked_oriented": sum(sources.values()),
        "E_endpoint_bad": independent["E_endpoint_bad_proper_P3"],
        "I_internal_only": independent["I_safe_endpoint_internal_only_proper_P3"],
        "full_seven_positive_S": len(accepted),
        "D6D_exact_optimal_K": K,
        "global_source_closed_profile": global_profile,
        "K_profile": k_profile,
        "K_minus_one_profile": km1_profile,
        "all_h_uniform_support_expansion_bound_proved": False,
    }


def finite_w32_support_expansion_report():
    rows = [_w32_row(scheme) for scheme in ("lex", "reverse", "S68", "S72")]
    return {
        "slice": "HYP105-ISSUE230-D6E-SOURCE-SUPPORT-EXPANSION-PROFILE",
        "restricted_theorem_C_status": "FINITE-CERTIFICATE-LAYER-ONLY",
        "complete_positive_target_scope": "W32 only; W34/W38 complete seven-family S remains unknown",
        "source_closed_Hall_target": "M_E(F)+M_I(F) <= K*B(F)",
        "all_h_uniform_support_expansion_bound": "OPEN",
        "controlled_exception_mass_bound": "OPEN",
        "root_branch_A_or_B": "OPEN",
        "W32_COMPLETE_positive_all_seven_source_closed_profiles": rows,
    }


def report():
    return finite_w32_support_expansion_report()


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
