"""HYP-105 #230 D6-G: local Hall-excess envelope.

D6-F computed the exact finite exception budget for a fixed one-incidence
recipient capacity K. D6-G subtracts the unavoidable global capacity deficit

    max(0, C - K*S)

from that exact exception mass. The remainder is the genuine LOCAL Hall excess:
source-support obstruction beyond the cardinality/pigeonhole floor.

This is a finite diagnostic and certificate layer only. It does NOT prove an
all-h local-excess bound, a uniform K, Branch A, Branch B, or an ASET exponent.
"""
from math import ceil
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6b_coherent_pruning import full_retention
from hyp105_issue230_d6d_incidence_factored_charging import (
    _validated,
    factored_frontier,
)
from hyp105_issue230_d6e_support_expansion_profile import (
    split_blocked_sources_by_endpoint_internal,
)
from hyp105_issue230_d6f_exception_budget_oracle import (
    exception_budget_for_capacity,
)


def global_capacity_deficit(source_weights, accepted, capacity):
    """Unavoidable exception mass from total capacity alone."""
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    _, sixsets = _validated(source_weights, accepted)
    total = sum(source_weights.values())
    return max(0, total - capacity * len(sixsets))


def local_excess_for_capacity(source_weights, accepted, capacity, split_weights=None):
    """Exact local Hall-excess over the global capacity deficit.

    A positive value means some source-closed support F has worse expansion
    than the global pigeonhole floor. Zero means that, at this K, all exception
    mass is explained by total capacity C versus K*S, for this finite instance.
    """
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    total = sum(source_weights.values())
    exact = exception_budget_for_capacity(source_weights, accepted, capacity, split_weights)
    global_deficit = global_capacity_deficit(source_weights, accepted, capacity)
    exception = exact["minimal_exception_mass"]
    if exception < global_deficit:
        raise AssertionError("exact exception cannot be smaller than global capacity deficit")
    local = exception - global_deficit
    status = (
        "ZERO-EXCEPTION-FEASIBLE" if exception == 0 else
        "GLOBAL-CAPACITY-ONLY" if local == 0 else
        "LOCAL-HALL-EXCESS"
    )
    return {
        "status": status,
        "capacity_K": capacity,
        "source_total_C": total,
        "recipient_count_S": len(sixsets),
        "global_capacity_KS": capacity * len(sixsets),
        "global_capacity_deficit": global_deficit,
        "exact_exception_mass": exception,
        "local_Hall_excess_over_global_deficit": local,
        "exception_minus_global_deficit_identity": exception - global_deficit == local,
        "unsupported_sources_can_contribute_to_local_excess": (
            exact.get("certificate", {}).get("status") != "COMPLETE-HALL-FEASIBLE"
            and local > 0
        ),
        "exact_exception_certificate": exact,
        "all_h_local_excess_bound_proved": False,
    }


def local_excess_frontier(source_weights, accepted, capacities, split_weights=None):
    """Evaluate local Hall excess over several candidate K values."""
    if not capacities:
        raise ValueError("at least one capacity must be supplied")
    normalised = sorted(set(capacities))
    if any(type(k) is not int or k < 0 for k in normalised):
        raise ValueError("capacities must be nonnegative integers")
    rows = [local_excess_for_capacity(source_weights, accepted, k, split_weights)
            for k in normalised]
    local_values = [row["local_Hall_excess_over_global_deficit"] for row in rows]
    exceptions = [row["exact_exception_mass"] for row in rows]
    return {
        "capacities": normalised,
        "frontier": rows,
        "local_excess_always_nonnegative": all(value >= 0 for value in local_values),
        "exception_mass_nonincreasing_in_K": all(
            exceptions[i] >= exceptions[i + 1] for i in range(len(exceptions) - 1)
        ),
        "exception_minus_global_deficit_verified": all(
            row["exception_minus_global_deficit_identity"] for row in rows
        ),
        "max_local_Hall_excess_over_frontier": max(local_values) if local_values else 0,
        "capacities_with_positive_local_excess": [
            row["capacity_K"] for row in rows
            if row["local_Hall_excess_over_global_deficit"] > 0
        ],
    }


def _complete_w32_inputs(scheme):
    model = fixture(1, scheme)
    core = ProjectionClosure(model)
    accepted = seven_census(model, independent_checks=True, witness_sets=True)["sets"]
    split = split_blocked_sources_by_endpoint_internal(core, full_retention(core))
    return core, accepted, split["sources"], split["split"], split["independent"]


def _w32_local_excess_row(scheme):
    core, accepted, sources, split, independent = _complete_w32_inputs(scheme)
    exact = factored_frontier(sources, accepted)
    if exact["status"] != "EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM":
        raise AssertionError("complete W32 all-seven inputs must be exactly repairable")
    K = exact["optimal_K"]
    if K <= 0:
        raise AssertionError("nonempty complete W32 source needs positive K")
    capacities = list(range(max(0, K - 3), K + 2))
    frontier = local_excess_frontier(sources, accepted, capacities, split)
    km1 = local_excess_for_capacity(sources, accepted, K - 1, split)
    zero = local_excess_for_capacity(sources, accepted, K, split)
    if km1["local_Hall_excess_over_global_deficit"] != 0:
        raise AssertionError("finite W32 K-1 obstruction should remain global-only")
    if zero["exact_exception_mass"] != 0:
        raise AssertionError("D6-D optimal K should be zero-exception feasible")
    return {
        "scheme": scheme,
        "s": core.s,
        "scope": "COMPLETE-ALL-SEVEN-ORIGINAL-W32",
        "C_blocked_oriented": sum(sources.values()),
        "E_endpoint_bad": independent["E_endpoint_bad_proper_P3"],
        "I_internal_only": independent["I_safe_endpoint_internal_only_proper_P3"],
        "full_seven_positive_S": len(accepted),
        "D6D_exact_zero_exception_K": K,
        "K_minus_one_local_excess": km1,
        "K_zero_exception_row": zero,
        "frontier": frontier,
        "all_h_local_excess_bound_proved": False,
    }


def finite_w32_local_excess_report():
    rows = [_w32_local_excess_row(scheme)
            for scheme in ("lex", "reverse", "S68", "S72")]
    return {
        "slice": "HYP105-ISSUE230-D6G-LOCAL-HALL-EXCESS-ENVELOPE",
        "restricted_theorem_C_status": "FINITE-LOCAL-EXCESS-DIAGNOSTIC-ONLY",
        "local_excess_definition": "exception_K - max(0, C-K*S)",
        "exact_finite_exception_budget": "REUSED-FROM-D6F-MAXFLOW-MINCUT",
        "all_h_uniform_K": "OPEN",
        "all_h_exception_mass_bound": "OPEN",
        "all_h_local_excess_bound": "OPEN",
        "root_branch_A_or_B": "OPEN",
        "W34_W38_complete_seven_family_S": "UNKNOWN-NOT-REPLACED-BY-BB",
        "W32_COMPLETE_positive_all_seven_local_excess_envelopes": rows,
    }


def report():
    return finite_w32_local_excess_report()


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
