"""HYP-105 E1-K3-G2-H: complete W32 one-swap Hall falsifier.

Every tested labeling gets the COMPLETE B0 62370-candidate seven-family
positive GF5 census. In contrast to budgeted W34 discovery, a failing
Hall cut here is a sound finite counterexample to the specified rule.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, labeled_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census, R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1k3g2d_charging_hall import _maxflow_with_cut
from hyp105_g5e2b3e1k3g2e_seven_family_hall import explicit_injective_assignment
from hyp105_g5e2b3e1k3g2g_global_adaptive import (
    _source_supports, _positive_target_graph, _assert_valid_certificate,
)


def swapped_labeling(base, side, i, j):
    """Exchange TWO complete original-vertex physical pair labels."""
    if side not in ("left", "right"):
        raise ValueError("side must be left or right")
    if base["s"] != 2 or base["a"] != 6 or (
            len(base["left_labels"]) != 15 or
            len(base["right_labels"]) != 15):
        raise ValueError("exact B0 enumeration requires W(3,2)/K6")
    if type(i) is not int or type(j) is not int or not 0 <= i < j < 15:
        raise ValueError("distinct original vertex IDs required")
    labels = {"left": list(base["left_labels"]),
              "right": list(base["right_labels"])}
    labels[side][i], labels[side][j] = labels[side][j], labels[side][i]
    result = labeled_model(
        2, 6, base["incidences"], labels["left"], labels["right"],
        scheme="one-swap-%s-%d-%d" % (side, i, j))
    for color in ("left", "right"):
        changed = {k for k, (a, b) in enumerate(zip(
            base[color + "_labels"], result[color + "_labels"])) if a != b}
        if changed != ({i, j} if color == side else set()):
            raise AssertionError("unexpected physical label mutation")
    return result


def full_target_hall(model):
    """Complete actual seven-S vs all Jcross, exact Hall and positive R3 floor."""
    if model["s"] != 2 or model["a"] != 6:
        raise ValueError("complete seven-S target oracle is W32 only")
    exact = seven_census(model, witness_sets=True, independent_checks=False)
    if (exact["left_6coordinate_candidates"] != 62370 or
            exact["S_seven"] != len(exact["sets"])):
        raise AssertionError("W32 full seven-S enumeration incomplete")
    if any(R3_CERTIFIED_FLOORS.get(tag, 0) <= 0
           for tag in exact["sets"].values()):
        raise AssertionError("nonpositive GF5 class")
    full_count, sources = _source_supports(model)
    if len(sources) != full_count:
        raise AssertionError("source witnesses unexpectedly sampled")
    targets, adj = _positive_target_graph(sources, exact["sets"])
    if len(targets) != exact["S_seven"]:
        raise AssertionError("full target universe not included")
    flow = _maxflow_with_cut(adj, len(targets), 1)
    constructed = explicit_injective_assignment(adj, len(targets))
    if flow["matched"] != constructed["assigned"]:
        raise AssertionError("independent matching algorithms disagree")
    _assert_valid_certificate(
        model, sources, exact["sets"], targets, adj,
        constructed["assignment"])
    gap = flow["witness_subset_size"] - flow["witness_neighbor_count"]
    if flow["unmatched"]:
        if gap != flow["unmatched"] or gap <= 0:
            raise AssertionError("invalid Hall deficiency mincut")
    elif gap > 0:
        raise AssertionError("false Hall deficiency")
    weights = sum(n * R3_CERTIFIED_FLOORS[tag]
                  for tag, n in exact["seven_class_motif_counts"].items())
    if weights != exact["GF5_seven_lower_numerator"]:
        raise AssertionError("GF5 original-sixset floor inconsistency")
    return {
        "Jcross": full_count,
        "S_seven_exact": exact["S_seven"],
        "GF5_seven_numerator_exact_class_floor": weights,
        "matched": flow["matched"],
        "hall_unit_capacity": flow["all_witnesses_charged"],
        "hall_deficiency": flow["unmatched"],
        "hall_cut_witness_subset": flow["witness_subset_size"],
        "hall_cut_neighbor_size": flow["witness_neighbor_count"],
        "hall_cut_capacity": flow["min_cut_capacity"],
        "isolated_witnesses_full_S": flow["isolated"],
        "min_target_degree": min(map(len, adj), default=0),
        "max_target_degree": max(map(len, adj), default=0),
        "assignment_sha256": constructed["sha256_of_witness_to_target_indices"],
        "S_minus_J": exact["S_seven"] - full_count,
        "S_over_J": str(Fraction(exact["S_seven"], full_count))
                    if full_count else None,
        "distinct_sixsets_checked": len(targets),
        "proof_status": "FINITE_HALL_NO_GO" if flow["unmatched"]
                        else "FINITE_HALL_INJECTION",
    }


def transposition_shell(base, *, sides=("left", "right"),
                        max_pairs_per_side=None):
    """210 complete transpositions only if both sides, all 105 per side."""
    if type(sides) not in (tuple, list) or not sides or (
            len(set(sides)) != len(sides) or
            any(s not in ("left", "right") for s in sides)):
        raise ValueError("distinct nonempty valid sides required")
    if max_pairs_per_side is not None and (
            type(max_pairs_per_side) is not int or
            not 1 <= max_pairs_per_side <= 105):
        raise ValueError("limit must be in 1..105 or absent")
    pairs = list(combinations(range(15), 2))
    chosen = pairs if max_pairs_per_side is None else pairs[:max_pairs_per_side]
    baseline = full_target_hall(base)
    cases = []
    digest = sha256()
    for side in sides:
        for i, j in chosen:
            result = full_target_hall(swapped_labeling(base, side, i, j))
            row = {"side": side, "i": i, "j": j, **result}
            cases.append(row)
            digest.update((side + ":" + str(i) + ":" + str(j) + ":" +
                           str(result["Jcross"]) + ":" +
                           str(result["S_seven_exact"]) + ":" +
                           str(result["matched"]) + ":" +
                           result["assignment_sha256"] + "\n").encode("ascii"))
    worst = lambda key: min(cases, key=lambda r: (r[key], r["side"],
                                                  r["i"], r["j"]))
    most = lambda key: max(cases, key=lambda r: r[key])
    failures = [r for r in cases if not r["hall_unit_capacity"]]
    full_shell = (len(sides) == 2 and set(sides) == {"left", "right"}
                  and len(chosen) == 105 and len(cases) == 210)
    return {
        "slice": "HYP-105-E1-K3-G2-H",
        "base_scheme": base["scheme"],
        "baseline": baseline,
        "tested_sides": list(sides),
        "tested_per_side": len(chosen),
        "tested_coherent_labelings": len(cases),
        "exact_complete_lex_W32_single_swap_shell":
            full_shell and base["scheme"] == "lex",
        "no_global_labeling_exhaustion_claimed": True,
        "no_all_h_charge_claimed": True,
        "no_all_h_S_omega_claimed": True,
        "unit_hall_successes": len(cases) - len(failures),
        "unit_hall_failures": len(failures),
        "finite_Hall_counterexamples": [
            {k:r[k] for k in (
                "side", "i", "j", "Jcross", "S_seven_exact",
                "hall_deficiency", "hall_cut_witness_subset",
                "hall_cut_neighbor_size", "isolated_witnesses_full_S")}
            for r in failures[:10]
        ],
        "universal_unit_two_overlap_charge_refuted_by_this_shell": bool(failures),
        "minimum_exact_S": {k:worst("S_seven_exact")[k]
                            for k in ("side", "i", "j", "S_seven_exact")},
        "maximum_exact_Jcross": {k:most("Jcross")[k]
                                for k in ("side", "i", "j", "Jcross")},
        "minimum_S_minus_J": {k:worst("S_minus_J")[k]
                              for k in ("side", "i", "j", "S_minus_J")},
        "minimum_local_degree": {k:worst("min_target_degree")[k]
                                 for k in ("side", "i", "j", "min_target_degree")},
        "swap_shell_results_sha256": digest.hexdigest(),
        "hall_deficiency_histogram": dict(sorted(Counter(
            r["hall_deficiency"] for r in cases).items())),
        "all_h_Branch_A_B": "OPEN",
    }


def report():
    return transposition_shell(gq_pair_model(1, "lex"))


if __name__ == "__main__":
    print(json.dumps(report(), sort_keys=True, indent=2))
