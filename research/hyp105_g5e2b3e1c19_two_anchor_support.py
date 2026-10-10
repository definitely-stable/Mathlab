"""HYP-105 C19: an all-h TWO-coordinate-cover obstruction to local blocks.

This is a restricted all-h NO-GO for independently minimized witness
BLOCKS, even when ALL original left and right factor labels are coupled
within each block. It is NOT a real common all-W(3,s) f,g labeling with
low seven-class count, and NOT issue #230 Branch B.

If every physical edge assigned to the ORIGINAL left support of a
six-incidence J meets fixed coordinates {x,y}, then the six physical
edge occurrences contribute >=6 incidences at {x,y}. A physical
2-factor must give each of x,y degree <=2 and hence <=4 altogether:
impossible, regardless of the right physical map or GF5 palette.

For V=(s+1)(s²+1), a minimal with C(a,2)>=V, write
t=C(a,2)-V < a-1. The complement of EVERY occupied F of size V has
2t<2(a-1) missing-edge endpoint degrees, so at least TWO physical
vertices have missing degree <=1. Their occupied double-star contains
at least (2a-3)-2=2a-5 edges. When s=2, F=K6 and it contains exactly
2a-3=9. Every named ORIGINAL-left block of at most that many points
can therefore be mapped injectively into a common double-star.
"""
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c18_zero_star_barrier import (
    minimal_physical_coordinates,
)


def all_h_double_star_gate(s):
    """An INTEGER all-powers certificate (analytic proof in C19 docs)."""
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("C19 requires s=2^h, h>=1")
    v = (s + 1) * (s*s + 1)
    a = minimal_physical_coordinates(v)
    missing = comb(a, 2) - v
    if not (comb(a-1, 2) < v <= comb(a, 2)
            and 0 <= missing < a-1 and 2*missing < 2*(a-1)):
        raise AssertionError("minimal physical target occupancy invalid")
    if s == 2:
        if (v, a, missing) != (15, 6, 0):
            raise AssertionError("GF2 original/physical palette changed")
        capacity = 9
    else:
        if a < 7:
            raise AssertionError("incorrect all-h minimal a lower")
        capacity = 2*a - 5
    if not (capacity >= 9 and capacity < v):
        raise AssertionError("unexpected two-anchor support capacity")
    return {
        "s": s,
        "original_GQ_factor_vertices_per_side": v,
        "physical_coordinate_count": a,
        "occupied_physical_pair_edges": v,
        "missing_physical_pair_edges": missing,
        "certified_shared_original_left_block_capacity": capacity,
        "certified_two_anchor_degree_sum_bound": 4,
        "six_incidence_occurrence_required_two_anchor_degree_sum": 6,
        "every_occupied_F_has_a_two_anchor_cover_of_at_least_capacity": True,
        "all_blocks_up_to_capacity_have_zero_seven_local_min": True,
        "all_blocks_up_to_capacity_have_zero_GF5_local_min": True,
        "not_a_real_globally_compatible_low_S_map": True,
    }


def occupied_two_anchor_witness(occupied_edges, a, *, need=1):
    """Find an occupied double-star injection, without assuming F=K_a.

    Exact physical edge IDs are validated. The chosen pair maximizes the
    number of occupied edges meeting its two coordinates; ties are
    broken lexicographically. A fake partial coordinate permutation or
    truncated chosen set is never returned as a certified witness.
    """
    if (type(a) is not int or a < 3
            or type(need) is not int or need < 1):
        raise ValueError("invalid physical alphabet or block size")
    try:
        raw = tuple(occupied_edges)
    except TypeError as e:
        raise ValueError("occupied physical pair edges required") from e
    edges = tuple(tuple(e) for e in raw)
    if (len(set(edges)) != len(edges)
            or any(len(e) != 2
                   or any(type(x) is not int or not 0 <= x < a for x in e)
                   or e[0] >= e[1] for e in edges)):
        raise ValueError("occupied pair edges must be distinct canonical K_a edges")
    if not edges or need > len(edges):
        raise ValueError("insufficient occupied physical edges")
    degree = [0] * a
    occupied = set(edges)
    for x, y in edges:
        degree[x] += 1
        degree[y] += 1
    scored = (
        (degree[x]+degree[y]-int((x,y) in occupied), x, y)
        for x, y in combinations(range(a), 2)
    )
    size, x, y = max(scored, key=lambda t: (t[0], -t[1], -t[2]))
    chosen = tuple(e for e in edges if x in e or y in e)
    if len(chosen) != size:
        raise AssertionError("occupied double-star counting mismatch")
    if size < need:
        raise ValueError("no certified two-anchor physical cover of requested size")
    return {
        "two_physical_coordinates": (x, y),
        "occupied_double_star_size": size,
        "physical_pair_edges_for_named_left_support": tuple(sorted(chosen)[:need]),
        "not_a_global_left_factor_embedding": True,
    }


def certified_all_h_occupied_double_star(s, occupied_edges):
    """For arbitrary *actual* occupied F, check the proved universal B."""
    info = all_h_double_star_gate(s)
    edges = tuple(occupied_edges)
    if len(edges) != info["occupied_physical_pair_edges"]:
        raise ValueError("occupied F does not have exactly V original images")
    w = occupied_two_anchor_witness(
        edges, info["physical_coordinate_count"],
        need=info["certified_shared_original_left_block_capacity"])
    if w["occupied_double_star_size"] < info[
            "certified_shared_original_left_block_capacity"]:
        raise AssertionError("all-h double-star theorem contradicted")
    return {**info, **w}


def two_anchor_kills_original_sixset(six_original_incidences, named_left_image,
                                     two_coordinates):
    """Independent per-occurrence necessary left physical degree falsifier."""
    six = tuple(tuple(x) for x in six_original_incidences)
    if len(six) != 6 or len(set(six)) != 6:
        raise ValueError("six DIFFERENT ORIGINAL incidence IDs required")
    x, y = two_coordinates
    if type(x) is not int or type(y) is not int or x == y:
        raise ValueError("distinct physical cover coordinates required")
    dx = dy = 0
    for p, _ in six:
        if p not in named_left_image:
            raise ValueError("an original point touched by J was not assigned")
        e = named_left_image[p]
        if len(e) != 2 or x not in e and y not in e:
            raise ValueError("left image is not a certified double-star assignment")
        dx += int(x in e)
        dy += int(y in e)
    if dx + dy < 6:
        raise AssertionError("two-anchor lower not maintained")
    return {
        "six_original_incidence_occurrences": 6,
        "physical_first_anchor_degree": dx,
        "physical_second_anchor_degree": dy,
        "total_two_anchor_degree": dx+dy,
        "cannot_be_a_six_coordinate_left_two_factor": dx > 2 or dy > 2,
    }


def genuine_W32_C19_report():
    """Actual ORIGINAL W(3,2) and independent full K6 62370-source audit."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS, selected_left_six
    from hyp105_g5e2b3e1c14_domain_certificates import _filled_model

    m = pair_labeled_symplectic(1, "reverse-line")
    physical_to_original = {e: i for i, e in enumerate(m["left_labels"])}
    cycle = ((0,1), (1,2), (2,3), (3,4), (4,5), (0,5))
    support = {physical_to_original[p] for p in cycle}
    if len(support) != 6:
        raise AssertionError("historical physical W32 left labeling lost a 6-cycle")
    support.update(i for i in range(15) if i not in support
                   and len(support) < 9)
    support = tuple(sorted(support))
    if len(support) != 9:
        raise AssertionError("missing nine distinct ORIGINAL points")
    candidate_before = sum(
        all(m["incidences"][e][0] in support for e in six)
        for six, _ in selected_left_six(m))
    if candidate_before == 0:
        raise AssertionError("W32 original nine-point control is vacuous")
    covered = certified_all_h_occupied_double_star(2, PAIRS)
    x, y = covered["two_physical_coordinates"]
    image = dict(zip(support,
                     covered["physical_pair_edges_for_named_left_support"]))
    if len(set(image.values())) != 9:
        raise AssertionError("left shared assignment is not injective")
    full = _filled_model(
        m, {i: PAIRS.index(edge) for i, edge in image.items()}, {})
    candidate_after = sum(
        all(full["incidences"][e][0] in support for e in six)
        for six, _ in selected_left_six(full))
    if candidate_after:
        raise AssertionError("real original W32 generated a killed 2factor")
    # Every sixset with support subset of the nine named ORIGINAL points,
    # whether or not selected by full's source enumeration, is killed.
    six = tuple(
        e for e in m["incidences"] if e[0] in support)[:6]
    witness = two_anchor_kills_original_sixset(six, image, (x,y))
    if not witness["cannot_be_a_six_coordinate_left_two_factor"]:
        raise AssertionError("independent degree failure did not hold")
    return {
        "scope": "REAL_ORIGINAL_W32_PHYSICAL_K6_ALL_LEFT_SOURCE",
        "true_original_left_source_size": 62370,
        "nine_named_original_left_points": support,
        "pre_relabel_true_left_2factor_witnesses_inside_support": candidate_before,
        "post_relabel_true_left_2factor_witnesses_inside_support": candidate_after,
        "physical_two_anchor_pair": (x,y),
        "occupied_double_star_edges": covered["occupied_double_star_size"],
        "real_original_incidence_degree_falsifier": witness,
        "all_h_gate_s2": all_h_double_star_gate(2),
        "no_global_W32_15_point_zero_witness": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C19_report(), indent=2, sort_keys=True))
