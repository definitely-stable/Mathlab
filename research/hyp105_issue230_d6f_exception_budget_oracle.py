"""HYP-105 #230 D6-F: exact exception-budget oracle for Hall transport.

D6-D made one-incidence repair equivalent to weighted Hall flow. D6-E
exposed the source-closed supports F where M_E(F)+M_I(F) must expand into
positive sixset support B(F). D6-F formalizes the compensation alternative:
for a fixed candidate capacity K, how much blocked-path demand must remain
unrepaired as an exception?

The answer is exact for each finite instance: it is the maxflow shortfall in
the same ORIGINAL incidence-factored network. This is a finite certificate
layer only. It does NOT prove an all-h exception bound, a uniform K, Branch A,
Branch B, or any ASET exponent.
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
    _normalise_split,
    factored_cut_profile,
    source_closed_support_profile,
    split_blocked_sources_by_endpoint_internal,
)


def exception_budget_for_capacity(source_weights, accepted, capacity,
                                  split_weights=None):
    """Exact minimum uncharged source mass for a fixed target capacity K.

    If the D6-D flow at capacity K routes value V out of total demand C, then
    every legal one-incidence assignment with this K leaves at least C-V units
    unassigned, and maxflow realizes C-V as sufficient. Unsupported sources
    therefore become irreducible exception mass even when K is huge.
    """
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    triples, sixsets = _validated(source_weights, accepted)
    split = _normalise_split(source_weights, split_weights)
    total = sum(source_weights.values())
    audit = factored_cut_profile(source_weights, accepted, capacity, split)
    value = audit["value"]
    exception = total - value
    if exception < 0:
        raise AssertionError("maxflow routed more than total demand")

    if exception == 0:
        return {
            "status": "ZERO-EXCEPTION-FEASIBLE",
            "capacity_K": capacity,
            "source_total": total,
            "max_chargeable_mass": value,
            "minimal_exception_mass": 0,
            "recipient_original_sixsets": len(sixsets),
            "global_capacity": capacity * len(sixsets),
            "certificate": audit,
            "all_h_exception_mass_bound_proved": False,
        }

    hint = {}
    if audit["status"] == "EXACT-HALL-OBSTRUCTION":
        residual = audit["residual_cut_split_demand"]
        # This is a lower-hint from one exact mincut, not a canonical split of
        # the removable exception set. It is still useful: each component can
        # be inspected in the same source-closed obstruction profile.
        hint = dict(residual)
        profile = audit["source_closed_profile"]
        if profile["excess_over_candidate_K"] < exception:
            raise AssertionError("source-closed excess must dominate maxflow exception")
    else:
        profile = None

    return {
        "status": "EXACT-EXCEPTION-BUDGET",
        "capacity_K": capacity,
        "source_total": total,
        "max_chargeable_mass": value,
        "minimal_exception_mass": exception,
        "recipient_original_sixsets": len(sixsets),
        "global_capacity": capacity * len(sixsets),
        "exception_split_lower_hint": hint,
        "source_closed_obstruction_profile": profile,
        "certificate": audit,
        "all_h_exception_mass_bound_proved": False,
    }


def exception_frontier(source_weights, accepted, capacities, split_weights=None):
    """Evaluate exact exception budgets over a finite set of candidate K."""
    if not capacities:
        raise ValueError("at least one capacity must be supplied")
    normalised = sorted(set(capacities))
    if any(type(k) is not int or k < 0 for k in normalised):
        raise ValueError("capacities must be nonnegative integers")
    rows = [exception_budget_for_capacity(source_weights, accepted, k, split_weights)
            for k in normalised]
    exceptions = [row["minimal_exception_mass"] for row in rows]
    routed = [row["max_chargeable_mass"] for row in rows]
    return {
        "capacities": normalised,
        "frontier": rows,
        "exception_mass_nonincreasing_in_K": all(
            exceptions[i] >= exceptions[i + 1] for i in range(len(exceptions) - 1)
        ),
        "max_chargeable_mass_nondecreasing_in_K": all(
            routed[i] <= routed[i + 1] for i in range(len(routed) - 1)
        ),
    }


def minimal_capacity_for_exception_budget(source_weights, accepted, budget,
                                          split_weights=None):
    """Smallest K whose exact exception mass is <= budget, if finite."""
    if type(budget) is not int or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    _validated(source_weights, accepted)
    total = sum(source_weights.values())
    if total == 0:
        return {
            "status": "EMPTY-SOURCE-NO-INFERENCE",
            "budget": budget,
            "minimum_capacity_K": 0,
            "certificate": exception_budget_for_capacity(source_weights, accepted, 0, split_weights),
        }

    upper = exception_budget_for_capacity(source_weights, accepted, total, split_weights)
    if upper["minimal_exception_mass"] > budget:
        return {
            "status": "NO-FINITE-K-MEETS-BUDGET",
            "budget": budget,
            "minimum_capacity_K": None,
            "irreducible_exception_mass": upper["minimal_exception_mass"],
            "certificate_at_K_equal_total_demand": upper,
        }

    lo = 0
    hi = total
    while lo < hi:
        mid = (lo + hi) // 2
        row = exception_budget_for_capacity(source_weights, accepted, mid, split_weights)
        if row["minimal_exception_mass"] <= budget:
            hi = mid
        else:
            lo = mid + 1
    certificate = exception_budget_for_capacity(source_weights, accepted, lo, split_weights)
    if certificate["minimal_exception_mass"] > budget:
        raise AssertionError("binary search returned infeasible capacity")
    return {
        "status": "EXACT-FINITE-MINIMUM-CAPACITY-FOR-BUDGET",
        "budget": budget,
        "minimum_capacity_K": lo,
        "certificate": certificate,
    }


def _complete_w32_inputs(scheme):
    model = fixture(1, scheme)
    core = ProjectionClosure(model)
    accepted = seven_census(model, independent_checks=True, witness_sets=True)["sets"]
    split = split_blocked_sources_by_endpoint_internal(core, full_retention(core))
    return core, accepted, split["sources"], split["split"], split["independent"]


def _w32_exception_row(scheme):
    core, accepted, sources, split, independent = _complete_w32_inputs(scheme)
    exact = factored_frontier(sources, accepted)
    if exact["status"] != "EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM":
        raise AssertionError("complete W32 all-seven inputs must be exactly repairable")
    K = exact["optimal_K"]
    if K <= 0:
        raise AssertionError("nonempty complete W32 source needs positive K")

    capacities = list(range(max(0, K - 3), K + 2))
    frontier = exception_frontier(sources, accepted, capacities, split)
    zero_exception = minimal_capacity_for_exception_budget(sources, accepted, 0, split)
    if zero_exception["minimum_capacity_K"] != K:
        raise AssertionError("zero-exception capacity must reproduce D6-D min K")

    km1 = exception_budget_for_capacity(sources, accepted, K - 1, split)
    global_F = {e for t in sources for e in t}
    global_profile = source_closed_support_profile(
        sources, accepted, global_F, split, candidate_K=K - 1
    )
    if km1["minimal_exception_mass"] != global_profile["excess_over_candidate_K"]:
        raise AssertionError("W32 K-1 exception should equal the global support deficit")

    return {
        "scheme": scheme,
        "s": core.s,
        "scope": "COMPLETE-ALL-SEVEN-ORIGINAL-W32",
        "C_blocked_oriented": sum(sources.values()),
        "E_endpoint_bad": independent["E_endpoint_bad_proper_P3"],
        "I_internal_only": independent["I_safe_endpoint_internal_only_proper_P3"],
        "full_seven_positive_S": len(accepted),
        "D6D_exact_zero_exception_K": K,
        "zero_exception_capacity": zero_exception,
        "K_minus_one_budget": km1,
        "K_minus_one_global_source_closed_excess": global_profile["excess_over_candidate_K"],
        "frontier": frontier,
        "all_h_exception_mass_bound_proved": False,
    }


def finite_w32_exception_budget_report():
    rows = [_w32_exception_row(scheme)
            for scheme in ("lex", "reverse", "S68", "S72")]
    return {
        "slice": "HYP105-ISSUE230-D6F-EXCEPTION-BUDGET-ORACLE",
        "restricted_theorem_C_status": "FINITE-EXCEPTION-BUDGET-CERTIFICATE-ONLY",
        "compensation_target": "C <= K*S + exception_mass",
        "exact_finite_exception_budget": "PROVED-BY-MAXFLOW-MINCUT",
        "all_h_uniform_K": "OPEN",
        "all_h_exception_mass_bound": "OPEN",
        "controlled_exception_mass_bound": "OPEN",
        "root_branch_A_or_B": "OPEN",
        "W34_W38_complete_seven_family_S": "UNKNOWN-NOT-REPLACED-BY-BB",
        "W32_COMPLETE_positive_all_seven_exception_frontiers": rows,
    }


def report():
    return finite_w32_exception_budget_report()


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
