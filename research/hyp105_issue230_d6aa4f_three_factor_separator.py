"""HYP-105 #230 D6-AA4-F: ORIGINAL three-source-factor separator hierarchy.

All-h CONDITIONAL frozen-outside exact min inequalities. Real original W32
seven-family tests preserve one globally injected map per fiber state and
all six original incidence positions. This does NOT prove universal Branch A.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial

PAIRS = ((0, 1), (0, 2), (1, 2))


def permutation_states(types, baseline):
    """All fixed-image coherent permutations, independently within each type."""
    types, baseline = tuple(types), tuple(baseline)
    if len(types) != 3 or len(baseline) != 3 or any(t not in ("P", "L") for t in types):
        raise ValueError("exactly three typed ORIGINAL factors required")
    groups = {t: tuple(i for i in range(3) if types[i] == t) for t in ("P", "L")}
    if any(len({baseline[i] for i in idx}) != len(idx) for idx in groups.values()):
        raise ValueError("baseline labels must be distinct within each type")
    result = []
    for pp, ll in product(
        permutations(tuple(baseline[i] for i in groups["P"])),
        permutations(tuple(baseline[i] for i in groups["L"])),
    ):
        state = list(baseline)
        for ids, labels in ((groups["P"], pp), (groups["L"], ll)):
            for i, x in zip(ids, labels):
                state[i] = x
        result.append(tuple(state))
    expected = factorial(len(groups["P"])) * factorial(len(groups["L"]))
    if len(result) != expected or len(set(result)) != expected:
        raise AssertionError("incomplete real coherent typed injection fiber")
    return tuple(result)


def separator_hierarchy(types, states, motifs):
    """Exact three-factor cost hierarchy, with independent pair scopes.

    motifs: (scope of typed-factor positions, cost at EACH globally complete
    state), in the same deterministic state order. All costs must depend
    ONLY on the declared ORIGINAL factor support. The pair relaxation
    groups each motif exactly once; a true 3-factor motif is minimized
    independently (not falsely projected to an ordinary pair).
    """
    types = tuple(types)
    states = tuple(tuple(state) for state in states)
    motifs = tuple((tuple(scope), tuple(cost)) for scope, cost in motifs)
    if not states or states != permutation_states(types, states[0]):
        raise ValueError("states must be ALL coherent fixed-image typed permutations")
    n = len(states)
    pair_groups = {p: [] for p in PAIRS}
    three_way = []
    independent = 0
    for scope, values in motifs:
        if len(set(scope)) != len(scope) or any(type(i) is not int or i not in range(3)
                                                for i in scope):
            raise ValueError("motif has invalid ORIGINAL factor support")
        if len(values) != n or any(type(c) is not int or c < 0 for c in values):
            raise ValueError("need complete nonnegative integer cost at all global states")
        projection = {}
        for state, cost in zip(states, values):
            key = tuple(state[i] for i in scope)
            if key in projection and projection[key] != cost:
                raise AssertionError("motif cost depends on factor OUTSIDE claimed source support")
            projection[key] = cost
        independent += min(values)
        containing_pairs = tuple(p for p in PAIRS if set(scope) <= set(p))
        if containing_pairs:
            pair_groups[containing_pairs[0]].append((scope, values))
        elif set(scope) == {0, 1, 2}:
            three_way.append(values)
        else:
            raise AssertionError("unclassified source dependency")
    pair_min = sum(min(values) for values in three_way)
    pair_group_cost = {}
    for p, group in pair_groups.items():
        if not group:
            pair_group_cost[str(p)] = 0
            continue
        costs = {}
        for s, state in enumerate(states):
            projected = (state[p[0]], state[p[1]])
            value = sum(vals[s] for _, vals in group)
            if projected in costs and costs[projected] != value:
                raise AssertionError("pair group varies with omitted ORIGINAL factor")
            costs[projected] = value
        pair_group_cost[str(p)] = min(costs.values())
        pair_min += pair_group_cost[str(p)]
    score_by_state = tuple(sum(vals[s] for _, vals in motifs) for s in range(n))
    triple_min = min(score_by_state) if score_by_state else 0
    if not 0 <= independent <= pair_min <= triple_min:
        raise AssertionError("violated exact source consistency hierarchy")
    return {
        "original_typed_factor_count": 3,
        "globally_coherent_states": n,
        "independent_Q_lower": independent,
        "pairwise_source_coherent_lower": pair_min,
        "three_source_joint_exact_minimum": triple_min,
        "pair_to_triple_gap": triple_min - pair_min,
        "pair_groups_minima": pair_group_cost,
        "true_three_factor_scope_motifs": len(three_way),
        "all_global_state_scores": score_by_state,
        "minimum_achieving_state": states[score_by_state.index(triple_min)] if n else None,
    }


def triangle_gap():
    """Analytic AA4-E counterexample: pairwise consistency still permits zero."""
    types = ("P", "P", "P")
    states = permutation_states(types, (0, 1, 2))
    motifs = []
    for i, j in PAIRS:
        motifs.append(((i, j), tuple(int(x[j] != (x[i] + 1) % 3)
                                    for x in states)))
    result = separator_hierarchy(types, states, motifs)
    if (result["independent_Q_lower"], result["pairwise_source_coherent_lower"],
            result["three_source_joint_exact_minimum"]) != (0, 0, 1):
        raise AssertionError("synthetic triangle falsifier no longer separates")
    # Each zero-cost pair relation has THREE cyclic states; each factor's
    # marginal is uniform. Pair scopes overlap with perfectly consistent
    # singletons, yet there is no globally feasible zero-cost triple.
    for (i, j), values in motifs:
        zero = [state for state, v in zip(states, values) if v == 0]
        if len(zero) != 3 or any(sorted(z[k] for z in zero) != [0, 1, 2]
                                 for k in (i, j)):
            raise AssertionError("unary-consistent zero-cost pseudomarginal broken")
    return result


def _three_factor_candidate_blocks(model, scheme):
    """Two actual ORIGINAL pure-type 3-subsets of critical 4-transversals."""
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph, incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    source = genuine_original_positive_hypergraph(model)
    bits, weights, allmask = incidence_cover_bits(source["records"])
    partition = finite_source_support_partition(bits, weights, allmask)
    if partition["number_transversal_blocks"] != {"S68": 53, "S72": 119}[scheme]:
        raise AssertionError("true original W32 source transversal baseline drift")
    blocks = partition["transversal_original_factor_blocks"]
    selected = {}
    for ty, predicate in (("P", lambda x: x < 15), ("L", lambda x: x >= 15)):
        candidates = [b for b in blocks if all(predicate(x) for x in b)]
        if not candidates:
            raise AssertionError("missing genuine original pure-type transversal")
        selected[ty] = candidates[0][:3]
    return selected, bits, weights, allmask


def true_original_w32_three_factor_census(scheme):
    """Actual full 7-class ORIGINAL Q, no image-only/fake independent Q choices.

    For each REAL global map in two disjoint pure-type 3-factor permutation
    fibers, run historical 62,370-original-candidate classifier. Assemble
    per-ORIGINAL-Q cost tables on the true touched source factors, checking
    that varying other labels cannot alter that Q's classification.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        R3_CERTIFIED_FLOORS, seven_census)
    from hyp105_issue230_d6aa4c_edit_transversal import survivor_certificate

    if scheme not in ("S68", "S72"):
        raise ValueError("only genuine pinned ORIGINAL W32 schemes")
    model = fixture(1, scheme)
    candidate_blocks, bits, weights, allmask = _three_factor_candidate_blocks(model, scheme)
    incidences = tuple(model["incidences"])
    if len(incidences) != 45:
        raise AssertionError("original W32 incidence host missing")
    result = {}
    for ty in ("P", "L"):
        typed_ids = candidate_blocks[ty]
        factors = tuple(("P", i) if i < 15 else ("L", i-15) for i in typed_ids)
        types = tuple(f[0] for f in factors)
        left = tuple(tuple(x) for x in model["left_labels"])
        right = tuple(tuple(x) for x in model["right_labels"])
        baseline = tuple((left if t == "P" else right)[i] for t, i in factors)
        states = permutation_states(types, baseline)
        censuses = []
        all_tags = set()
        for state in states:
            lf, rg = list(left), list(right)
            for (t, i), x in zip(factors, state):
                if t == "P":
                    lf[i] = x
                else:
                    rg[i] = x
            actual = seven_census({**model, "left_labels":tuple(lf),
                                   "right_labels":tuple(rg)},
                                  independent_checks=False, witness_sets=True)
            tags = actual["sets"]
            if actual["S_seven"] != len(tags) or actual[
                    "GF5_seven_lower_numerator"] != sum(
                    R3_CERTIFIED_FLOORS[tag] for tag in tags.values()):
                raise AssertionError("GF5 numerator and ORIGINAL Q unit mass diverge")
            censuses.append(actual)
            all_tags.update(tags)
        if len(censuses) != len(states) or len(states) != 6:
            raise AssertionError("expected all six pure-type permutations")
        rows, weighted_rows = [], []
        scopes = Counter()
        for q in sorted(all_tags):
            host_factors = {("P", p) for p, _ in (incidences[i] for i in q)}
            host_factors |= {("L", l) for _, l in (incidences[i] for i in q)}
            scope = tuple(i for i, f in enumerate(factors) if f in host_factors)
            scopes[len(scope)] += 1
            rows.append((scope, tuple(int(q in census["sets"]) for census in censuses)))
            weighted_rows.append((scope, tuple(
                R3_CERTIFIED_FLOORS.get(census["sets"].get(q), 0)
                for census in censuses)))
        count = separator_hierarchy(types, states, rows)
        gf5 = separator_hierarchy(types, states, weighted_rows)
        if tuple(c["S_seven"] for c in censuses) != count["all_global_state_scores"]:
            raise AssertionError("lost full original sixset class count under source lifting")
        if tuple(c["GF5_seven_lower_numerator"] for c in censuses) != gf5[
                "all_global_state_scores"]:
            raise AssertionError("lost certified 51-palette numerator under source lifting")
        retained, retained_GF5, _ = survivor_certificate(
            bits, weights, allmask, typed_ids)
        if retained > count["independent_Q_lower"] or (
                retained_GF5 > gf5["independent_Q_lower"]):
            raise AssertionError("unchanged old Q does not survive all true completions")
        if censuses[0]["S_seven"] != {"S68":68,"S72":72}[scheme]:
            raise AssertionError("baseline should be first globally coherent state")
        result[ty] = {
            "original_typed_block_ids": typed_ids,
            "distinct_original_Q_positive_in_at_least_one_state": len(all_tags),
            "original_Q_by_number_of_touched_three_factors": dict(scopes),
            "AA4C_unchanged_old_original_Q_floor": retained,
            "AA4C_unchanged_old_GF5_numerator_floor": retained_GF5,
            "seven": count,
            "selected_GF5_numerator": gf5,
            "all_genuine_original_Q_six_position_classifiers": True,
            "original_W32_candidates_per_full_state": 62370,
            "not_all_h_universal_certificate": True,
        }
    return {"scheme":scheme, "scope":"pure-type 3-factor source fibers of genuine W32",
            "by_type": result, "Branch_A":"OPEN", "Branch_B":"OPEN"}


def report(scheme=None):
    out = {
        "slice": "HYP105-ISSUE230-D6-AA4-F-THREE-FACTOR-SEPARATOR",
        "all_h_conditional_frozen_outside_hierarchy": True,
        "all_h_start_map_independent_positivity": False,
        "three_factor_triangle_pseudomarginal_NO_GO": True,
        "triangle": triangle_gap(),
        "Branch_A": "OPEN", "Branch_B": "OPEN",
        "full_GF5_R3": False, "ASET_exponent": False,
    }
    if scheme is not None:
        out["true_W32"] = true_original_w32_three_factor_census(scheme)
    return out


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--scheme", choices=("S68","S72"))
    args = parser.parse_args()
    print(json.dumps(report(args.scheme), default=list, indent=2, sort_keys=True))
