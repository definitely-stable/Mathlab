"""JPKC-010: mixed three-class ORIGINAL positive transfer on ONE coherent f,g.

J35: D6 Hall matching and B/A or A/B source-wedge witnesses have a
    common exact (actual physical seed, ORIGINAL six-incidence Q) ledger.
J36: class-sensitive 12/8/8 seed-witness charge (uses J19).
J37: exact fixed globally injected finite-label fiber minimax identity.
Neither a positive all-h witness lower bound nor Root A/B is asserted.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import ceil, comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import (
    _bad_seed_paths, general_seven_original,
)
from hyp105_issue230_jpkc006_source_topology_sharp_charge import (
    _other_source_completion, _signature, J19_CLASS_CAPS,
)
from hyp105_issue230_jpkc007_completion_deficit_ledger import _stratified_indices
from hyp105_issue230_jpkc008_source_hall_coherence import (
    _demand, hall_certificate, source_key_original_anchor,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census

REACHABLE = ("D6", "B-left/A-right", "A-left/B-right")
TOPOLOGY = {
    "D6": "matching_3K2",
    "B-left/A-right": "point_wedge_plus_edge",
    "A-left/B-right": "line_wedge_plus_edge",
}
FIBERS = {"S68": (0, 1, 2, 3), "S72": (1, 7, 9, 12)}


def mixed_positive_certificate(model, *, limit_seeds=None, max_paths=2_000_000,
                               max_pairs=200_000, max_cross_pairs=1_000_000,
                               independent_W32=True):
    """Exact genuine-original seed->Q witnesses for one complete global map.

    `limit_seeds` selects distributed real seeds; NEVER interpret that output
    as a full W34/GF5 census. W32 independent oracle is a full ORIGINAL
    62,370-sixset census, not a separate independent-label proxy.
    """
    ctx = ProjectionClosure(model)
    if ctx.s != 2 and independent_W32:
        raise ValueError("independent complete seven oracle restricted to W32")
    if type(max_pairs) is not int or max_pairs < 1:
        raise ValueError("positive source witness pair budget required")
    if type(max_cross_pairs) is not int or max_cross_pairs < 1:
        raise ValueError("positive cross-source pair budget required")
    # An independent ORIGINAL 62,370-sixset W32 oracle must compare the
    # WHOLE extension set for every true seed, not just membership of hits.
    # Build once per coherent f,g, reused by all selected seed triples.
    full_census = None
    census_source_index = None
    if independent_W32:
        full_census = seven_census(
            model, independent_checks=False, witness_sets=True)
        census_source_index = defaultdict(dict)
        for source_Q, tag in full_census["sets"].items():
            for T3 in combinations(source_Q, 3):
                census_source_index[T3][source_Q] = tag
    _, fibers, _ = _path_fibers(ctx, max_paths)
    seeds = list(_bad_seed_paths(ctx, fibers))
    if not seeds:
        raise ValueError("no true ORIGINAL endpoint-bad physical seeds")
    indices = _stratified_indices(
        len(seeds), len(seeds) if limit_seeds is None else limit_seeds)
    selected = [seeds[i] for i in indices]
    unique_seed_Q = set()
    class_of_Q = {}
    anchors_by_Q = defaultdict(set)
    hits = Counter()
    seed_types = Counter()
    hall_stage = Counter()
    seen_original_keys = {}
    selected_D6_original_keys = set()
    positive_D6_matches = 0

    for path, T, anchor in selected:
        T = tuple(sorted(T))
        found = _other_source_completion(ctx, path, T, anchor)
        if census_source_index is not None and found != census_source_index.get(T, {}):
            raise AssertionError(
                "J35 independent W32 ORIGINAL full seven-census source-extension "
                "set EQUALITY failed (a missed or spurious positive Q)")
        selected_D6 = {Q for Q, tag in found.items() if tag == "D6"}
        hall_D6 = set()
        for P, L, _ in _demand(ctx, path):
            key = (P, L)
            if source_key_original_anchor(ctx, P, L) != anchor:
                raise AssertionError("J35 original source key has wrong GQ anchor")
            if key not in seen_original_keys:
                seen_original_keys[key] = hall_certificate(ctx, P, L)
            h = seen_original_keys[key]
            hall_stage["AA_source_demand_occurrences"] += 1
            if not h["hall_feasible"]:
                hall_stage["AA_Hall_deficient_occurrences"] += 1
                continue
            hall_stage["AA_Hall_feasible_occurrences"] += 1
            ids = h["unique_original_matching_ids"]
            if not ids or set(ids) & set(T):
                raise AssertionError("J35 Hall matched ORIGINAL IDs intersect source seed")
            Q = tuple(sorted((*T, *ids)))
            if general_seven_original(ctx, Q) == "D6":
                hall_D6.add(Q)
                selected_D6_original_keys.add(key)
                hall_stage["AA_selected_D6_occurrences"] += 1
            else:
                hall_stage["AA_nonaligned_occurrences"] += 1
        if hall_D6 != selected_D6:
            raise AssertionError(
                "J35 independent ORIGINAL Hall/D6 and topology D6 sixsets disagree")
        positive_D6_matches += len(hall_D6)
        observed = set()
        for Q, tag in found.items():
            if tag not in REACHABLE:
                raise AssertionError("J35 endpoint-bad seed reached forbidden GF5 class")
            Q = tuple(sorted(Q))
            if len(Q) != 6 or len(set(Q)) != 6 or not set(T).issubset(Q):
                raise AssertionError("J35 invalid ORIGINAL six-incidence witness")
            if general_seven_original(ctx, Q) != tag:
                raise AssertionError("J35 independently reconstructed GF5 class drift")
            U = tuple(sorted(set(Q) - set(T)))
            if _signature(ctx, U) != TOPOLOGY[tag]:
                raise AssertionError("J35 positive ORIGINAL complement topology drift")
            if Q in class_of_Q and class_of_Q[Q] != tag:
                raise AssertionError("one ORIGINAL sixset acquired two incompatible GF5 classes")
            class_of_Q[Q] = tag
            anchors_by_Q[Q].add(anchor)
            witness = (path, Q)
            if witness in unique_seed_Q:
                raise AssertionError("J35 repeated oriented physical seed / ORIGINAL Q")
            unique_seed_Q.add(witness)
            hits[tag] += 1
            observed.add(tag)
            if len(unique_seed_Q) > max_pairs:
                raise ValueError("mixed ORIGINAL seed-to-Q witness pair budget exceeded")
        if not observed:
            seed_types["none"] += 1
        elif "D6" in observed and len(observed) > 1:
            seed_types["D6_and_wedge"] += 1
        elif "D6" in observed:
            seed_types["D6_only"] += 1
        elif len(observed) > 1:
            seed_types["both_wedges_no_D6"] += 1
        else:
            seed_types["single_wedge_no_D6"] += 1

    if hall_stage["AA_Hall_feasible_occurrences"] != (
            hall_stage["AA_selected_D6_occurrences"] +
            hall_stage["AA_nonaligned_occurrences"]):
        raise AssertionError("J35 exact Hall->GF5 telescope violated")
    if hall_stage["AA_source_demand_occurrences"] != (
            hall_stage["AA_Hall_feasible_occurrences"] +
            hall_stage["AA_Hall_deficient_occurrences"]):
        raise AssertionError("J35 complete source demand telescope violated")
    if positive_D6_matches != hits["D6"]:
        raise AssertionError("J35 Hall positive and true D6 seed charges differ")
    if sum(seed_types.values()) != len(selected):
        raise AssertionError("J35 full five-way seed decomposition incomplete")

    by_class = Counter(class_of_Q.values())
    per_Q_hits = Counter(Q for _, Q in unique_seed_Q)
    for Q, multiplicity in per_Q_hits.items():
        if multiplicity > J19_CLASS_CAPS[class_of_Q[Q]]:
            raise AssertionError("J36 sharp J19 class-wise physical P3 cap violated")
        if not anchors_by_Q[Q]:
            raise AssertionError("missing original anchor for source Q")
    if sum(per_Q_hits.values()) != sum(hits.values()):
        raise AssertionError("J36 charge does not conserve ORIGINAL seed-Q pairs")
    # J19 gives an ALL-h NECESSARY bound on the full seven-family S.
    charged = sum(ceil(hits[tag] / J19_CLASS_CAPS[tag]) for tag in REACHABLE)
    if charged > sum(by_class.values()):
        raise AssertionError("J36 J19 per-class charge exceeded distinct witnessed Q")

    # Two independent ORIGINAL sixsets can share true ORIGINAL incidence IDs
    # even when realized through different original GQ anchors. Generate
    # candidate Q pairs by incidence-inverted index, then deduplicate pairs:
    # an overlap of two or three IDs is ONE Q-pair, not 2/3 Q-pairs.
    by_original_id = defaultdict(list)
    for Q in class_of_Q:
        for incidence_id in Q:
            by_original_id[incidence_id].append(Q)
    candidate_pairs = set()
    for bucket in by_original_id.values():
        for Q1, Q2 in combinations(bucket, 2):
            a, b = sorted((Q1, Q2))
            candidate_pairs.add((a, b))
            if len(candidate_pairs) > max_cross_pairs:
                raise ValueError("exact original incidence cross-Q pair budget exceeded")
    cross_by_class = Counter()
    cross_intersection = Counter()
    all_shared_pairs = 0
    for Q1, Q2 in candidate_pairs:
        common = len(set(Q1) & set(Q2))
        if common == 0:
            raise AssertionError("inverted ORIGINAL incidence pair lacks common ID")
        all_shared_pairs += 1
        if all(a == b for a in anchors_by_Q[Q1] for b in anchors_by_Q[Q2]):
            continue
        tags = tuple(sorted((class_of_Q[Q1], class_of_Q[Q2])))
        cross_by_class[" | ".join(tags)] += 1
        cross_intersection[common] += 1
    if sum(cross_by_class.values()) != sum(cross_intersection.values()):
        raise AssertionError("J35 cross-anchor source incidence overlap conservation failed")
    if sum(by_class.values()) != len(class_of_Q):
        raise AssertionError("distinct original sixset counted in multiple classes")

    # JPKC-009 D/H/A cross-anchor ORIGINAL source-demand edges,
    # recomputed from this EXACT SAME f,g and selected physical seeds.
    # The new positive-Q cross-anchor graph is a DIFFERENT graph and
    # must never be substituted for Hall cross-key edges.
    demanded_keys = set(seen_original_keys)
    hall_keys = {k for k, h in seen_original_keys.items() if h["hall_feasible"]}
    if not selected_D6_original_keys <= hall_keys <= demanded_keys:
        raise AssertionError("JPKC-009 source D6/Hall/demand graph nesting failed")
    anchor_cache = {k: source_key_original_anchor(ctx, *k) for k in demanded_keys}
    def source_cross(support, side):
        vertices = defaultdict(list)
        for P, L in support:
            q, r = anchor_cache[P, L]
            if side == "left":
                vertices[P].append(r)
            else:
                vertices[L].append(q)
        return sum(
            comb(len(others), 2)
            - sum(comb(n, 2) for n in Counter(others).values())
            for others in vertices.values())
    cross_stages = {}
    for side in ("left", "right"):
        raw = source_cross(demanded_keys, side)
        hall = source_cross(hall_keys, side)
        d6 = source_cross(selected_D6_original_keys, side)
        if not 0 <= d6 <= hall <= raw:
            raise AssertionError("JPKC-009 cross-anchor source Hall nesting failed")
        cross_stages[side] = {
            "JPKC009_raw_original_source_demand_cross": raw,
            "JPKC009_Hall_original_source_demand_cross": hall,
            "JPKC009_selected_D6_original_source_demand_cross": d6,
        }

    oracle_S = None
    if independent_W32:
        census = full_census
        accepted = census["sets"]
        for Q, tag in class_of_Q.items():
            if accepted.get(Q) != tag:
                raise AssertionError("J35 independent full W32 ORIGINAL sixset oracle disagrees")
        oracle_S = census["S_seven"]
        if len(accepted) != oracle_S or sum(by_class.values()) > oracle_S:
            raise AssertionError("J36 witnessed Q exceeds full exact W32 seven census")

    return {
        "s": ctx.s, "a": ctx.a,
        "one_complete_globally_injective_original_f_g": True,
        "full_real_endpoint_bad_physical_seed_population": len(seeds),
        "examined_real_endpoint_bad_physical_seeds": len(selected),
        "complete_endpoint_bad_seed_census": len(selected) == len(seeds),
        "J35_exact_Hall_D6_equals_source_topology_D6": True,
        "J35_true_original_incidence_ids_and_GF5_positions": True,
        "J35_W32_full_source_three_extension_set_equality":
            bool(independent_W32),
        "AA_original_source_stage": dict(sorted(hall_stage.items())),
        "original_JPKC009_cross_key_stages_on_same_f_g": cross_stages,
        "seed_positive_type_partition": dict(sorted(seed_types.items())),
        "positive_original_seed_Q_witness_pairs": len(unique_seed_Q),
        "class_witness_pairs": {tag: hits[tag] for tag in REACHABLE},
        "class_distinct_positive_original_sixsets_reached":
            {tag: by_class[tag] for tag in REACHABLE},
        "distinct_positive_original_sixsets_reached": len(class_of_Q),
        "J36_class_sensitive_ceil_charge_lower_for_full_S": charged,
        "positive_original_Q_pairs_sharing_incidence": all_shared_pairs,
        "positive_original_Q_cross_anchor_pairs_by_GF5_class":
            dict(sorted(cross_by_class.items())),
        "positive_original_Q_cross_anchor_shared_ID_multiplicity":
            dict(sorted(cross_intersection.items())),
        "independent_full_original_W32_seven_S": oracle_S,
        "full_W34_seven_census": False,
        "does_not_force_positive_all_h_charge": True,
        "root_A_proved": False, "root_B_constructed": False,
    }


def complete_right_four_factor_fiber(scheme, *, states=None):
    """J37 SAME globally injected right map per sixset, pinned AA4-B fiber.

    states=None is exactly all 4!=24 legal W32 completions; a positive
    smaller states argument is EXPLICITLY INCOMPLETE, never a full-fiber
    positivity certificate.
    """
    if scheme not in FIBERS:
        raise ValueError("pinned true W32 S68/S72 fiber required")
    if states is not None and (type(states) is not int or not 1 <= states <= 24):
        raise ValueError("fiber states must be between 1 and 24")
    original = fixture(1, scheme)
    block = FIBERS[scheme]
    right = tuple(tuple(p) for p in original["right_labels"])
    if len(right) != 15 or len(set(right)) != 15:
        raise AssertionError("J37 original W32 right physical image not a K6 bijection")
    options = tuple(permutations(tuple(right[k] for k in block)))
    assert len(options) == 24
    chosen = options[:states] if states is not None else options
    rows = []
    for order in chosen:
        updated = list(right)
        for source_factor, label in zip(block, order):
            updated[source_factor] = label
        if len(set(updated)) != 15 or set(updated) != set(right):
            raise AssertionError("J37 global right factor map injection violated")
        model = dict(original)
        model["right_labels"] = tuple(updated)
        cert = mixed_positive_certificate(model, independent_W32=True)
        rows.append({
            "globally_shared_right_images_on_original_block": order,
            "full_original_seven_S": cert["independent_full_original_W32_seven_S"],
            "seed_witness_pairs": cert["positive_original_seed_Q_witness_pairs"],
            "mixed_class_charge": cert["J36_class_sensitive_ceil_charge_lower_for_full_S"],
            "mixed_reached_distinct_Q": cert["distinct_positive_original_sixsets_reached"],
            "selected_D6_Hall": cert["AA_original_source_stage"].get(
                "AA_selected_D6_occurrences", 0),
            "witness_by_class": cert["class_witness_pairs"],
            "source_cross_anchor_class_pairs":
                cert["positive_original_Q_cross_anchor_pairs_by_GF5_class"],
        })
    if rows[0]["full_original_seven_S"] != {"S68": 68, "S72": 72}[scheme]:
        raise AssertionError("J37 pinned globally coherent baseline S drift")
    if any(r["mixed_class_charge"] > r["mixed_reached_distinct_Q"] or
           r["mixed_reached_distinct_Q"] > r["full_original_seven_S"]
           for r in rows):
        raise AssertionError("J37 invalid per-global-map necessary lower bounds")
    return {
        "scheme": scheme, "original_line_block": block,
        "legally_globally_injected_states_examined": len(rows),
        "entire_24_state_right_factor_fiber_exhausted": len(rows) == 24,
        "min_full_original_seven_S_on_examined_states":
            min(x["full_original_seven_S"] for x in rows),
        "min_reached_positive_original_Q_on_examined_states":
            min(x["mixed_reached_distinct_Q"] for x in rows),
        "min_class_charge_on_examined_states":
            min(x["mixed_class_charge"] for x in rows),
        "all_completions_keep_one_physical_label_per_original_factor": True,
        "states": rows,
        "J37_all_h_finite_fiber_minimax_is_conditional_only": True,
        "root_A_proved": False, "root_B_constructed": False,
    }


def report(*, w34_seeds=4, fiber_scheme=None):
    if fiber_scheme:
        return {"slice": "JPKC-010", "fiber": complete_right_four_factor_fiber(fiber_scheme)}
    rows = [
        {"scheme": name, **mixed_positive_certificate(fixture(1, name))}
        for name in ("lex", "reverse", "S68", "S72")
    ]
    for name in ("lex", "random"):
        rows.append({"scheme": name, **mixed_positive_certificate(
            fixture(2, name), limit_seeds=w34_seeds, independent_W32=False)})
    from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
    model, proof = spread_adversary_model(2)
    rows.append({"scheme": "D4-true-original-symplectic-spread",
                 "M_f_original_exact": proof["M_f_original_exact"],
                 **mixed_positive_certificate(
                     model, limit_seeds=w34_seeds, independent_W32=False)})
    return {"slice": "JPKC-010",
            "status": "RESTRICTED_THEOREM_C_OR_OPEN_WITH_FORMAL_BLOCKER",
            "all_h_global_positive_lower_proved": False,
            "records": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--w34-seeds", type=int, default=4)
    parser.add_argument("--fiber", choices=tuple(FIBERS))
    args = parser.parse_args()
    print(json.dumps(report(w34_seeds=args.w34_seeds, fiber_scheme=args.fiber),
                     sort_keys=True, indent=2))
