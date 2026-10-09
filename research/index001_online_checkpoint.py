"""INDEX-001 G2-B3-B: deterministic online checkpoint/adversarial finite oracles.

Frozen one-slot WAL / full-image snapshot accounting ONLY. Decisions occur
before observing current restart count. No original online theorem, hardware
durability, NAND I/O, randomized policies or Rust implementation.
"""
import argparse
from fractions import Fraction
import itertools
import json

from index001_checkpoint_policy import (
    Weights, actual_filesystem_trace, exhaustive_offline,
    optimal_offline, score,
)
from index001_workload_io import workload_traces

ENTRY = 28


def snapshot_size(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive integer universe required")
    return 24 + 4 * n


def safe_threshold(n):
    """Smallest integer T with E*T >= S (ceil(S/E))."""
    s = snapshot_size(n)
    return (s + ENTRY - 1) // ENTRY


def component_bound(n, threshold):
    """Exact elementary worst-case *upper bound*, NOT a sharp ratio."""
    if not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be positive integer")
    s = snapshot_size(n)
    return max(Fraction(1) + Fraction(s, ENTRY * threshold),
               Fraction(1) + Fraction(ENTRY * (threshold - 1), s))


def _checkpoint(strategy, time, pending_age, last_restarts, default_t):
    if strategy == "threshold":
        return pending_age >= default_t
    if strategy == "immediate":
        return True
    if strategy == "never":
        return False
    if strategy == "reactive":
        return last_restarts > 0 and pending_age > 0
    raise ValueError("unknown online strategy")


def online_policy(n, restarts, strategy="threshold", threshold=None):
    """Checkpoint tuple, depending on past r_1..r_(t-1) only."""
    tlimit = safe_threshold(n) if threshold is None else threshold
    component_bound(n, tlimit)
    age = 0
    previous = 0
    checkpoints = []
    for t, r in enumerate(restarts, 1):
        if not isinstance(r, int) or r < 0:
            raise ValueError("restart counts must be nonnegative integers")
        pending = age + 1
        if _checkpoint(strategy, t, pending, previous, tlimit):
            checkpoints.append(t)
            age = 0
        else:
            age = pending
        previous = r   # May influence only the *next* checkpoint.
    return tuple(checkpoints)


def adaptive_greedy_trace(n, horizon, strategy="threshold", threshold=None,
                          max_restart=2):
    """Greedy *witness*, not a computed optimal adaptive adversary."""
    if not isinstance(horizon, int) or horizon < 0:
        raise ValueError("invalid horizon")
    if not isinstance(max_restart, int) or max_restart < 0:
        raise ValueError("invalid restart bound")
    tlimit = safe_threshold(n) if threshold is None else threshold
    component_bound(n, tlimit)
    result = []
    age = 0
    previous = 0
    for t in range(1, horizon + 1):
        pending = age + 1
        chose_checkpoint = _checkpoint(strategy, t, pending, previous, tlimit)
        current = 0 if chose_checkpoint else max_restart
        age = 0 if chose_checkpoint else pending
        result.append(current)
        previous = current
    return tuple(result)


def cost_ratio(a, b):
    if a is None or b is None:
        raise ValueError("both policies must be feasible")
    top, bottom = a["weighted_cost"], b["weighted_cost"]
    if bottom == 0:
        if top != 0:
            raise AssertionError("online positive cost vs zero offline cost")
        return Fraction(1)
    return Fraction(top, bottom)


def compare(n, restarts, weights=Weights(1, 6, 0),
            strategy="threshold", threshold=None, independent=False):
    counts = tuple(restarts)
    checkpoints = online_policy(n, counts, strategy, threshold)
    online = score(n, counts, checkpoints, weights)
    offline = optimal_offline(n, counts, weights)
    if independent:
        if len(counts) > 12:
            raise ValueError("independent offline exhaustive search max U=12")
        brute = exhaustive_offline(n, counts, weights)
        if offline != brute:
            raise AssertionError("offline DP differs from exhaustive subset oracle")
    ratio = cost_ratio(online, offline)
    if strategy == "threshold" and ratio > component_bound(
            n, safe_threshold(n) if threshold is None else threshold):
        raise AssertionError("component-wise theorem violated")
    return {
        "online_checkpoint": list(checkpoints),
        "offline_checkpoint": offline["checkpoints"],
        "online_weighted_cost": online["weighted_cost"],
        "offline_weighted_cost": offline["weighted_cost"],
        "ratio": {"numerator": ratio.numerator, "denominator": ratio.denominator},
        "online_written": online["written_bytes"],
        "offline_written": offline["written_bytes"],
        "online_recovery": online["recovery_read_bytes"],
        "offline_recovery": offline["recovery_read_bytes"],
        "online_byte_steps": online["steady_footprint_byte_steps"],
        "offline_byte_steps": offline["steady_footprint_byte_steps"],
    }


def finite_worst(n, horizon, max_restart=2, weights=Weights(1, 6, 0),
                 strategy="threshold", threshold=None):
    """Full bounded exogenous history enumeration (not infinite game proof)."""
    if not isinstance(horizon, int) or not 0 <= horizon <= 8:
        raise ValueError("finite search supported only for 0<=U<=8")
    if not isinstance(max_restart, int) or not 0 <= max_restart <= 3:
        raise ValueError("finite restart alphabet must be 0..3")
    best = None
    for history in itertools.product(range(max_restart + 1), repeat=horizon):
        row = compare(n, history, weights, strategy, threshold)
        quotient = Fraction(row["ratio"]["numerator"], row["ratio"]["denominator"])
        # First in lexicographic order remains selected on ties.
        if best is None or quotient > best[0]:
            best = (quotient, history, row)
    ratio, history, row = best
    return {
        "universe": n,
        "horizon": horizon,
        "restart_cap_per_step": max_restart,
        "histories_checked": (max_restart + 1) ** horizon,
        "strategy": strategy,
        "witness": list(history),
        "witness_online_checkpoint": row["online_checkpoint"],
        "witness_offline_checkpoint": row["offline_checkpoint"],
        "ratio": row["ratio"],
        "reference_bound": {
            "numerator": component_bound(
                n, safe_threshold(n) if threshold is None else threshold).numerator,
            "denominator": component_bound(
                n, safe_threshold(n) if threshold is None else threshold).denominator,
        } if strategy == "threshold" else None,
    }


def build_report():
    n = 32
    threshold = safe_threshold(n)
    traces = workload_traces()
    rows = {}
    for name, operations in traces.items():
        u = len(operations)
        if name == "nested_ranges":
            r = tuple(2 if t in (3, u - 1) else 0 for t in range(1, u + 1))
        elif name == "alternating_singletons":
            r = tuple(1 if t % 4 == 0 else 0 for t in range(1, u + 1))
        else:
            r = tuple(1 if t == u else 0 for t in range(1, u + 1))
        weights = Weights(1, 6, 0)
        online = compare(n, r, weights, independent=True)
        filesystem = actual_filesystem_trace(
            operations, r, online["online_checkpoint"], n, weights)
        if filesystem["written_bytes"] != online["online_written"]:
            raise AssertionError("POSIX write-byte ledger not aligned with model")
        if filesystem["recovery_read_bytes"] != online["online_recovery"]:
            raise AssertionError("POSIX recovery ledger not aligned with model")
        rows[name] = {
            "updates": u,
            "restart_counts": list(r),
            "competitive_comparison": online,
            "filesystem_actual_write_bytes": filesystem["written_bytes"],
            "filesystem_actual_recovery_bytes": filesystem["recovery_read_bytes"],
        }
    example = finite_worst(4, 7, 2, Weights(1, 6, 0))
    greedy = adaptive_greedy_trace(4, 7, "threshold", max_restart=2)
    return {
        "schema": "mathlab.index001.g2b3b.online-fixed-frame.v1",
        "classification": "ELEMENTARY_2_UPPER_BOUND_NOT_NOVELTY",
        "weights": {"write": 1, "recovery": 6, "footprint": 0},
        "threshold": threshold,
        "guarantee": "J_online <= 2 J_offline WITHOUT hard WAL/peak caps",
        "hard_caps": "EXCLUDED_FROM_THEOREM",
        "randomized_online": "NOT_STUDIED",
        "physical_nand_bytes": "NOT_MEASURED",
        "workloads": rows,
        "finite_worst_witness": example,
        "adaptive_greedy_not_minimax": list(greedy),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    options = parser.parse_args()
    result = build_report()
    if options.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("INDEX-001 online T=", result["threshold"])
        for name, row in result["workloads"].items():
            comp = row["competitive_comparison"]
            print(f"{name}: ONLINE={comp['online_weighted_cost']} "
                  f"OFFLINE={comp['offline_weighted_cost']} "
                  f"ratio={comp['ratio']['numerator']}/{comp['ratio']['denominator']}")
        worst = result["finite_worst_witness"]
        print(f"finite U={worst['horizon']}, enumerated {worst['histories_checked']} "
              f"histories, max ratio={worst['ratio']['numerator']}/{worst['ratio']['denominator']}")
        print("INDEX001_G2B3B_ONLINE_2_UPPER_BOUND_PASS")


if __name__ == "__main__":
    main()
