"""HYP-105 C17: sixset-local ORIGINAL left/right scope tensor.

Genuine W(3,2) executable only. Mathematically, for each ORIGINAL
six-incidence set J, accepted seven-class membership depends on the
physical labels of only its touched original point/line endpoints.
Thus a group of witnesses with one shared missing-endpoint signature
can be minimized over local injections on THAT signature. Every local
injection extends to a full actual mapping. Full 15!^2 enumeration is
not part of this certificate. The source union remains finite W32 and
is enumerated exactly for <=3 missing left vertices.
"""
from collections import defaultdict
from itertools import permutations
from math import factorial

from hyp105_g5e2b3e1a_fixed_leading import PAIRS, selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1c14_domain_certificates import (
    _filled_model, _original_W32, _pins,
)


def local_scope_sixset_certificate(
        model, left_pins, right_pins, *,
        max_missing_left=3, max_missing_right=3,
        max_left_source_templates=6,
        max_source_candidates=400000,
        max_local_classifications=10000000):
    """Certified C16 exact *signature* lower via local support scopes.

    Let J be any distinct ORIGINAL six-incidence set. chi_J(f,g)
    depends ONLY on original left/right vertices touched by J,
    including whether the left physical projection is a 2factor.
    If J not in the chosen physical-left source for f, chi_J=0.

    For missing supports U_J,V_J and a disjoint cluster W_(U,V),
    define local table T_(U,V)(alpha,beta)=sum_(J in cluster)
    chi_J(f0 U alpha,g0 V beta). Here alpha,beta are LOCAL injective
    assignments of still-free physical edge IDs to the NAMED original
    supports, and arbitrary filler for untouched vertices is harmless.
    Every local assignment extends to some real full f,g.

    For U!=empty, sum min_(alpha,beta) T_(U,V) is a lower bound.
    For U=empty, we use ONE common full right map across ALL frozen-left
    groups, retaining exactly C15's shared-right eligible floor.
    The combined bound equals C16's original two-sided signature floor,
    but does not form the full F x G joint score matrix. It can be
    defined/evaluated by bounded-support local tables for any fixed
    motif size, rather than enumerating V!^2 complete mappings.
    """
    f = _pins(left_pins, "left original pins")
    g = _pins(right_pins, "right original pins")
    _original_W32(model)
    all_limits = (max_missing_left, max_missing_right,
                  max_left_source_templates, max_source_candidates,
                  max_local_classifications)
    if (any(type(x) is not int or x < 0 for x in all_limits[:2])
            or any(type(x) is not int or x < 1 for x in all_limits[2:])):
        raise ValueError("invalid C17 exact scope budgets")
    missing_l = tuple(x for x in range(15) if x not in f)
    missing_r = tuple(x for x in range(15) if x not in g)
    unused_l = tuple(x for x in range(15) if x not in f.values())
    unused_r = tuple(x for x in range(15) if x not in g.values())
    left_tail_count = factorial(len(missing_l))
    if (len(missing_l) > max_missing_left
            or len(missing_r) > max_missing_right
            or left_tail_count > max_left_source_templates
            or 62370 * left_tail_count > max_source_candidates):
        raise ValueError("C17 bounded W32 source envelope exceeds limits")
    inc = model["incidences"]
    selected_original = set()
    source_instances = 0
    for tail in permutations(unused_l):
        full_f = {**f, **dict(zip(missing_l, tail))}
        full = _filled_model(model, full_f, g)
        seen_this_f = set()
        for six, _ in selected_left_six(full):
            if six in seen_this_f:
                raise AssertionError("duplicate exact original left sixset")
            seen_this_f.add(six)
            selected_original.add(six)
            source_instances += 1
        if len(seen_this_f) != 62370:
            raise AssertionError("missing original source sixsets")
    if source_instances != 62370 * left_tail_count:
        raise AssertionError("incomplete left template source expansion")

    clusters = defaultdict(list)
    for six in selected_original:
        u = tuple(sorted({inc[e][0] for e in six if inc[e][0] not in f}))
        v = tuple(sorted({inc[e][1] for e in six if inc[e][1] not in g}))
        clusters[(u, v)].append(six)
    if sum(map(len, clusters.values())) != len(selected_original):
        raise AssertionError("original sixsets are not disjointly clustered")

    # For every original named support, retain a SMALL local tensor only.
    # Neither global f! x g! scores nor an assumed filler witness are used.
    tensors = {}
    evaluations = 0
    for (u, v), motifs in sorted(clusters.items()):
        local_l = tuple(permutations(unused_l, len(u)))
        local_r = tuple(permutations(unused_r, len(v)))
        left_cache = {}
        right_cache = {}
        for physical in local_l:
            lp = {**f, **dict(zip(u, physical))}
            left_cache[physical] = _filled_model(model, lp, g)["left_labels"]
        for physical in local_r:
            rp = {**g, **dict(zip(v, physical))}
            right_cache[physical] = _filled_model(model, f, rp)["right_labels"]
        values = {}
        for a in local_l:
            left = left_cache[a]
            for b in local_r:
                right = right_cache[b]
                if evaluations + len(motifs) > max_local_classifications:
                    raise ValueError("C17 local motif classification budget exceeded")
                s = risk = 0
                for six in motifs:
                    tag = classify_seven_prechecked(six, left, right, inc)
                    if tag is not None:
                        s += 1
                        risk += R3_CERTIFIED_FLOORS[tag]
                evaluations += len(motifs)
                values[(a, b)] = (s, risk)
        if not values:
            raise AssertionError("empty local original assignment domain")
        tensors[(u, v)] = values

    # Original-left-frozen witnesses depend only on one REAL common right
    # tail, NOT separately chosen minimizing right images for each cell.
    eligible_by_right = [[0, 0] for _ in range(factorial(len(missing_r)))]
    for j, rt in enumerate(permutations(unused_r)):
        assigned_g = dict(zip(missing_r, rt))
        for (u, v), tensor in tensors.items():
            if not u:
                key = ((), tuple(assigned_g[x] for x in v))
                a, b = tensor[key]
                eligible_by_right[j][0] += a
                eligible_by_right[j][1] += b
    base_s = min(q[0] for q in eligible_by_right)
    base_risk = min(q[1] for q in eligible_by_right)
    remaining_s = remaining_risk = 0
    all_local_s = all_local_risk = 0
    rows = []
    for (u, v), tensor in sorted(tensors.items()):
        best_s = min(x[0] for x in tensor.values())
        best_risk = min(x[1] for x in tensor.values())
        all_local_s += best_s
        all_local_risk += best_risk
        if u:
            remaining_s += best_s
            remaining_risk += best_risk
        rows.append({
            "missing_original_left_points": u,
            "missing_original_right_lines": v,
            "original_distinct_sixsets": len(clusters[(u, v)]),
            "local_left_injections": len({a for a, _ in tensor}),
            "local_right_injections": len({b for _, b in tensor}),
            "local_seven_minimum": best_s,
            "local_GF5_necessary_numerator_minimum": best_risk,
        })
    if (all_local_s > base_s + remaining_s
            or all_local_risk > base_risk + remaining_risk):
        raise AssertionError("local polynomial relaxation exceeds shared-right bound")
    return {
        "scope": "TRUE_ORIGINAL_W32_COMPLETE_K6_BOTH_HALVES",
        "candidate_source_instances": source_instances,
        "distinct_original_sixsets_in_source_union": len(selected_original),
        "original_named_two_sided_signature_groups": len(tensors),
        "actual_local_motif_classifications": evaluations,
        "full_joint_completion_score_matrix_allocated": False,
        "C17_all_signature_local_S_lower": all_local_s,
        "C17_all_signature_local_GF5_numerator_lower": all_local_risk,
        "C15_shared_eligible_left_S": base_s,
        "C17_local_two_sided_signature_S_lower": base_s + remaining_s,
        "C15_shared_eligible_left_GF5_numerator": base_risk,
        "C17_local_two_sided_signature_GF5_numerator_lower":
            base_risk + remaining_risk,
        "local_signature_census": tuple(rows),
        "no_universal_all_h_positive_lower_proved": True,
    }


def genuine_W32_C17_report():
    """Finite root cross-check versus independently implemented C16."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c16_two_sided_source import (
        two_sided_source_certificate,
    )
    m = pair_labeled_symplectic(1, "reverse-line")
    f = {i: PAIRS.index(m["left_labels"][i]) for i in range(12)}
    g = {i: PAIRS.index(m["right_labels"][i]) for i in range(12)}
    local = local_scope_sixset_certificate(m, f, g)
    original = two_sided_source_certificate(m, f, g)
    for a, b in (
        ("C15_shared_eligible_left_S", "C15_eligible_one_right_lower_S"),
        ("C17_local_two_sided_signature_S_lower",
         "C16_two_sided_signature_lower_S"),
        ("C15_shared_eligible_left_GF5_numerator",
         "C15_eligible_one_right_lower_GF5_numerator"),
        ("C17_local_two_sided_signature_GF5_numerator_lower",
         "C16_two_sided_signature_lower_GF5_numerator"),
    ):
        if local[a] != original[b]:
            raise AssertionError("C17 local independent minimization differs from C16")
    if (local["C15_shared_eligible_left_S"] != 12
            or local["C15_shared_eligible_left_GF5_numerator"] != 513393):
        raise AssertionError("accepted prior C15 root baseline changed")
    return local


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C17_report(), indent=2, sort_keys=True))
