"""JPKC-011: exact seven-class ORIGINAL sixset physical-P3 visibility.

A global actual ORIGINAL incidence sixset Q, not a selected physical path,
is the counting unit. For each legally globally injected f,g, stratify
every positive W32 Q into source-endpoint-factor-bad-visible, projection-blocked-only,
other-proper-only, or completely proper-P3-invisible. Full W32 census ONLY.

J38 is the all-h exact partition identity, J39 the all-h C-half structural
invisibility (and endpoint-bad B/B exclusion via J15/J17), J40 the exact
class-sensitive necessary GF5-weight telescoping identity. No ROOT A/B.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import (
    GOOD, BLOCKED, _path_fibers, _physical_status,
)
from hyp105_issue230_jpkc006_source_topology_sharp_charge import (
    _local_three_source_paths, J19_CLASS_CAPS,
)
from hyp105_issue230_jpkc010_mixed_positive_transfer import FIBERS
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)

VISIBLE_BAD = "endpoint_factor_bad_visible"
PROJECTION_ONLY = "projection_blocked_but_not_endpoint_factor_bad"
VISIBLE_OTHER = "other_proper_only"
INVISIBLE = "no_proper_P3"
STATES = (VISIBLE_BAD, PROJECTION_ONLY, VISIBLE_OTHER, INVISIBLE)
ALL_TAGS = tuple(R3_CERTIFIED_FLOORS)
C_HALF_TAGS = frozenset(("C/A", "C/B"))
BB_TAGS = frozenset(("B/B-overlap", "B/B-disjoint"))


def _global_proper_source_path_index(ctx, *, max_paths):
    """Index *all* real coordinate-proper oriented physical P3 by ORIGINAL T.

    Every path carries its unique exact three original incidence IDs and
    true original-projection status; no model-independent physical proxy.
    """
    _, fibers, status_counts = _path_fibers(ctx, max_paths)
    by_T = defaultdict(dict)
    for (u, v), entries in fibers.items():
        for b, c, status, ids in entries:
            if status not in GOOD:
                continue
            T = tuple(sorted(ids))
            if len(T) != 3 or len(set(T)) != 3:
                raise AssertionError("proper physical P3 reused ORIGINAL incidence")
            path = (u, b, c, v)
            if path in by_T[T]:
                raise AssertionError("one oriented physical path duplicated by original source ID")
            if _physical_status(ctx, *path) != status:
                raise AssertionError("independent ORIGINAL GQ endpoint status disagrees")
            by_T[T][path] = status
    if sum(map(len, by_T.values())) != sum(status_counts[t] for t in GOOD):
        raise AssertionError("complete proper physical P3 source index missing path")
    if any(len(v) != 2 for v in by_T.values()):
        raise AssertionError("J18 valid source triple must have exactly two oriented reversals")
    return by_T, {k: status_counts[k] for k in GOOD}


def _is_jpkc010_endpoint_factor_bad(ctx, path, status):
    """EXACT JPKC-005/010 source anchor badness, NOT broad projection status.

    A projection may be blocked because p/l intersects an INTERNAL physical
    path coordinate, yet the original endpoint q/r physical pair label
    is disjoint from p/l. Such paths are NOT JPKC-010 endpoint-bad seeds.
    """
    if status not in BLOCKED:
        return False
    u, _, _, v = path
    a = ctx.a
    q = ctx.fi.get(tuple(sorted((u // a, v // a))))
    r = ctx.gi.get(tuple(sorted((u % a, v % a))))
    if q is None or r is None or (q, r) not in ctx.projection:
        return False
    p, l = ctx.projection[q, r]
    return bool(set(ctx.f[q]) & set(ctx.f[p])) or bool(
        set(ctx.g[r]) & set(ctx.g[l]))


def visibility_certificate(model, *, max_paths=2_000_000, max_sixsets=50_000,
                           direct_local_oracle=True, sample_Q=0):
    """Complete W32 ORIGINAL seven-set partition, exact source Q identity.

    Direct independent validation enumerates, for each accepted Q, ALL
    original 3-subsets and their 2^3 diagonal realization choices through
    JPKC-006's local original-incidence path algorithm (no K2 path fibers).
    W34 is rejected: selected W34 seed computations are NOT full S.
    """
    ctx = ProjectionClosure(model)
    if ctx.s != 2:
        raise ValueError("complete JPKC-011 seven-family visibility census W32 only")
    if type(max_sixsets) is not int or max_sixsets < 1:
        raise ValueError("positive ORIGINAL accepted-sixset budget required")
    if type(sample_Q) is not int or sample_Q < 0 or sample_Q > 25:
        raise ValueError("sample_Q must be integer between 0 and 25")

    census = seven_census(model, independent_checks=False, witness_sets=True)
    accepted = census["sets"]
    if len(accepted) > max_sixsets:
        raise ValueError("complete ORIGINAL accepted-sixset budget exceeded")
    paths_by_T, statuses_all_proper = _global_proper_source_path_index(
        ctx, max_paths=max_paths)

    visibility = Counter()
    counts_by_class = defaultdict(Counter)
    oriented_paths_by_class = Counter()
    source_T_by_class = defaultdict(set)
    max_paths_per_Q = Counter()
    weighted_by_state = Counter()
    examples = {}
    local_cache = {}

    for Q, tag in sorted(accepted.items()):
        if len(Q) != 6 or len(set(Q)) != 6 or tag not in ALL_TAGS:
            raise AssertionError("full ORIGINAL seven-census returned invalid Q/tag")
        actual = {}
        source_subtriples = tuple(combinations(Q, 3))
        if len(source_subtriples) != 20:
            raise AssertionError("original sixset lacks 20 source 3-subsets")
        for T in source_subtriples:
            for path, status in paths_by_T.get(T, {}).items():
                if path in actual and actual[path] != status:
                    raise AssertionError("same physical P3 has contradictory GQ status")
                actual[path] = status
                source_T_by_class[tag].add(T)
            if direct_local_oracle:
                if T not in local_cache:
                    local_cache[T] = {
                        path: _physical_status(ctx, *path)
                        for path in _local_three_source_paths(ctx, T)
                    }
                independently = local_cache[T]
                if independently != paths_by_T.get(T, {}):
                    raise AssertionError(
                        "J38 independent local ORIGINAL 3-ID diagonal P3 "
                        "oracle does not equal global K2 source-path index")
        if len(actual) > J19_CLASS_CAPS[tag]:
            raise AssertionError("J39/J19 sharp classwise ORIGINAL Q-P3 cap exceeded")
        if any(status not in GOOD for status in actual.values()):
            raise AssertionError("improper coordinate path admitted to accepted Q")
        if tag in C_HALF_TAGS and actual:
            raise AssertionError("J39 physical C-half cannot contain proper synchronized P3")
        if tag in BB_TAGS and any(s in BLOCKED for s in actual.values()):
            raise AssertionError("J39 J15/J17 B/B cannot contain endpoint-bad P3")
        # JPKC-010 endpoint-factor badness is STRICTLY narrower than
        # JPKC-002 path-projection blocked status; preserving both avoids
        # falsely equating different positive ORIGINAL Q populations.
        bad_factor = any(
            _is_jpkc010_endpoint_factor_bad(ctx, path, status)
            for path, status in actual.items())
        broad_blocked = any(s in BLOCKED for s in actual.values())
        if bad_factor and not broad_blocked:
            raise AssertionError("factor-endpoint bad physical P3 must be projection blocked")
        state = (VISIBLE_BAD if bad_factor
                 else PROJECTION_ONLY if broad_blocked
                 else VISIBLE_OTHER if actual else INVISIBLE)
        counts_by_class[tag][state] += 1
        visibility[state] += 1
        weighted_by_state[state] += R3_CERTIFIED_FLOORS[tag]
        oriented_paths_by_class[tag] += len(actual)
        max_paths_per_Q[tag] = max(max_paths_per_Q[tag], len(actual))
        if sample_Q and len(examples.get(state, ())) < sample_Q:
            examples.setdefault(state, []).append({
                "original_six_incidence_ids": Q, "class": tag,
                "oriented_proper_physical_P3_count": len(actual),
                "source_original_3ID_subsets": len(source_subtriples),
                "actual_original_GQ_path_statuses": dict(Counter(actual.values())),
                "exact_JPKC010_endpoint_factor_bad_path_count": sum(
                    _is_jpkc010_endpoint_factor_bad(ctx, path, status)
                    for path, status in actual.items()),
            })

    if sum(visibility.values()) != census["S_seven"]:
        raise AssertionError("J38 full accepted ORIGINAL positive Q partition lost a sixset")
    if sum(weighted_by_state.values()) != census["GF5_seven_lower_numerator"]:
        raise AssertionError("J40 GF5 weighted ORIGINAL Q visibility decomposition incorrect")
    for tag in ALL_TAGS:
        if sum(counts_by_class[tag].values()) != census["seven_class_motif_counts"][tag]:
            raise AssertionError("J38 per-GF5-class exact original Q partition mismatch")
        if tag in C_HALF_TAGS and counts_by_class[tag][INVISIBLE] != census[
                "seven_class_motif_counts"][tag]:
            raise AssertionError("J39 all C-half original Q must be invisible")
        if tag in BB_TAGS and counts_by_class[tag][VISIBLE_BAD]:
            raise AssertionError("J39 genuine B/B has endpoint-bad original seed")
    if sum(statuses_all_proper.values()) != sum(map(len, paths_by_T.values())):
        raise AssertionError("global proper physical P3 count inconsistent")

    by_tag = {
        tag: {
            "all_positive_original_Q": census["seven_class_motif_counts"][tag],
            **{state: counts_by_class[tag][state] for state in STATES},
            "oriented_proper_P3_witnesses": oriented_paths_by_class[tag],
            "max_oriented_proper_P3_per_Q": max_paths_per_Q[tag],
            "distinct_original_source_triples_with_proper_paths":
                len(source_T_by_class[tag]),
            "certified_GF5_floor_numerator": (
                census["seven_class_motif_counts"][tag] *
                R3_CERTIFIED_FLOORS[tag]),
        }
        for tag in ALL_TAGS
    }
    return {
        "scope": "complete TRUE ORIGINAL W(3,2) globally injected f,g",
        "s": ctx.s, "a": ctx.a,
        "original_incidence_ids_total": len(ctx.edges),
        "all_original_left_sixcoordinate_candidates":
            census["left_6coordinate_candidates"],
        "complete_original_positive_seven_S": census["S_seven"],
        "accepted_original_sixsets_exactly_once": len(accepted),
        "true_original_f_g_globally_injective": True,
        "all_actual_proper_P3_status_count": statuses_all_proper,
        "all_true_original_proper_3ID_T_with_paths": len(paths_by_T),
        "source_triples_independently_verified": (
            len(local_cache) if direct_local_oracle else None),
        "all_positive_Q_local_diagonal_equals_global_path_oracle":
            bool(direct_local_oracle),
        "J38_complete_original_Q_visibility_partition":
            {state: visibility[state] for state in STATES},
        "J38_exact_seven_class_visibility": by_tag,
        "J39_all_h_C_half_invisible_to_proper_P3": True,
        "J39_all_h_BB_invisible_to_endpoint_bad_P3": True,
        "J40_GF5_floor_by_visibility": {
            state: weighted_by_state[state] for state in STATES},
        "J40_full_original_GF5_floor_numerator":
            census["GF5_seven_lower_numerator"],
        "J40_exact_seven_GF5_necessary_weight_telescope": True,
        "positive_Q_invisible_to_JPKC010_bad_seed_ledger":
            visibility[PROJECTION_ONLY] + visibility[VISIBLE_OTHER] +
            visibility[INVISIBLE],
        "positive_Q_invisible_to_ALL_proper_P3":
            visibility[INVISIBLE],
        "original_positive_Q_with_broad_blocked_projection_P3":
            visibility[VISIBLE_BAD] + visibility[PROJECTION_ONLY],
        "J38_distinguishes_internal_physical_projection_block_from_factor_bad":
            True,
        "original_examples": examples if sample_Q else None,
        "root_A_proved": False, "root_B_constructed": False,
        "not_full_R3": True, "no_W34_full_census": True,
    }


def visibility_right_four_factor_fiber(scheme, *, states=None,
                                       direct_local_oracle=False):
    """Complete legal pinned W32 right-fiber 24 permutations; NEVER Q-local."""
    if scheme not in FIBERS:
        raise ValueError("only pinned true W32 S68/S72 family accepted")
    if states is not None and (
            type(states) is not int or not 1 <= states <= 24):
        raise ValueError("states must be an integer in [1,24]")
    model = fixture(1, scheme)
    block = FIBERS[scheme]
    base_right = tuple(tuple(x) for x in model["right_labels"])
    original_image = tuple(base_right[i] for i in block)
    orders = tuple(permutations(original_image))
    if len(orders) != 24 or len(set(orders)) != 24:
        raise AssertionError("W32 full globally-injective four-original-line fiber size")
    orders = orders[:states] if states is not None else orders
    rows = []
    for order in orders:
        new_right = list(base_right)
        for i, pair in zip(block, order):
            new_right[i] = pair
        if len(set(new_right)) != len(base_right):
            raise AssertionError("original right line map no longer globally injective")
        actual = dict(model)
        actual["right_labels"] = tuple(new_right)
        cert = visibility_certificate(
            actual, direct_local_oracle=direct_local_oracle)
        rows.append({
            "original_global_right_block_images": order,
            "full_original_S": cert["complete_original_positive_seven_S"],
            "partition": cert["J38_complete_original_Q_visibility_partition"],
            "GF5_floor_by_visibility":
                cert["J40_GF5_floor_by_visibility"],
            "class_visibility": {
                name: {
                    state: cert["J38_exact_seven_class_visibility"][name][state]
                    for state in STATES}
                for name in ALL_TAGS},
        })
    if rows[0]["full_original_S"] != {"S68":68,"S72":72}[scheme]:
        raise AssertionError("frozen W32 original S baseline drift")
    if any(sum(row["partition"].values()) != row["full_original_S"]
           for row in rows):
        raise AssertionError("global coherent right fiber partitions do not conserve S")
    return {
        "scheme": scheme, "right_original_block": block,
        "all_24_globally_injective_states_exhausted": len(rows) == 24,
        "legal_complete_global_maps_examined": len(rows),
        "min_full_seven_S": min(row["full_original_S"] for row in rows),
        "min_endpoint_bad_visible_Q": min(
            row["partition"][VISIBLE_BAD] for row in rows),
        "min_projection_blocked_not_factor_bad_Q": min(
            row["partition"][PROJECTION_ONLY] for row in rows),
        "min_other_proper_only_Q": min(
            row["partition"][VISIBLE_OTHER] for row in rows),
        "min_no_proper_P3_Q": min(
            row["partition"][INVISIBLE] for row in rows),
        "min_positive_Q_not_detected_by_endpoint_bad": min(
            row["partition"][PROJECTION_ONLY] +
            row["partition"][VISIBLE_OTHER] + row["partition"][INVISIBLE]
            for row in rows),
        "max_positive_Q_not_detected_by_endpoint_bad": max(
            row["partition"][PROJECTION_ONLY] +
            row["partition"][VISIBLE_OTHER] + row["partition"][INVISIBLE]
            for row in rows),
        "all_states": rows,
        "no_universal_all_h_claim": True,
    }


def report(*, scheme=None, sample_Q=0):
    if scheme is not None:
        return {"slice": "JPKC-011", "fiber":
                visibility_right_four_factor_fiber(scheme)}
    records = [
        {"scheme": name, **visibility_certificate(
            fixture(1, name), sample_Q=sample_Q)}
        for name in ("lex","reverse","S68","S72")
    ]
    return {
        "slice": "JPKC-011",
        "finite_scope": "full W32 original seven-class visibility",
        "status": "RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER",
        "all_h_S_omega_proved": False, "root_B_constructed": False,
        "records": records,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fiber", choices=tuple(FIBERS))
    ap.add_argument("--examples", type=int, default=0)
    args = ap.parse_args()
    print(json.dumps(report(scheme=args.fiber, sample_Q=args.examples),
                     indent=2, sort_keys=True))
