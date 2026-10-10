"""HYP-105 C18: rigorous all-h ZERO for no-left-pin pure-local C17 relaxation.

This is a method-kill theorem, NOT a zero-cost real common pair-labeling.
Each independently minimized ORIGINAL left-support cluster can choose its
own incompatible star-centered physical injection; such choices must NEVER
be spliced into one global f. The full S_seven(f,g) may be positive.
"""
from collections import Counter
from math import comb


def minimal_physical_coordinates(v):
    if type(v) is not int or v < 1:
        raise ValueError("positive factor-vertex count required")
    a = 2
    while comb(a, 2) < v:
        a += 1
    return a


def all_h_occupied_star_gate(s):
    """Exact symbolic degree-count proof for ALL powers s=2^h, h>=1.

    V=(s+1)(s^2+1), minimal physical a with C(a,2)>=V.
    Any occupied image F subset E(K_a), |F|=V, satisfies
    max physical star degree >= ceil(2V/a)>=5 by handshaking.
    Proof V>2a: s=2 => V=15,a=6. For s>=4 => a>=7 and
    V>C(a-1,2)>2a. No symmetry/independence of f,g assumed.
    """
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("requires s=2^h, h>=1")
    v = (s + 1) * (s*s + 1)
    a = minimal_physical_coordinates(v)
    if s == 2:
        if (v, a) != (15, 6):
            raise AssertionError("wrong GF2 physical palette")
    elif not (a >= 7 and comb(a-1, 2) > 2*a):
        raise AssertionError("missing generic minimal-coordinate density proof")
    if not (comb(a-1, 2) < v <= comb(a, 2) and v > 2*a):
        raise AssertionError("wrong minimal target occupancy inequalities")
    return {
        "s": s, "original_GQ_factor_vertices_per_side": v,
        "minimal_physical_coordinates": a,
        "occupied_pair_edges": v,
        "occupied_target_average_degree_num": 2*v,
        "occupied_target_average_degree_den": a,
        "certified_minimum_max_star_degree": (2*v+a-1)//a,
        "star_degree_at_least_5_in_every_allowed_occupied_F": True,
        "C17_no_left_pin_pure_local_S_lower_exactly": 0,
        "C17_no_left_pin_pure_local_GF5_numerator_lower_exactly": 0,
        "no_real_common_global_f_g_zero_witness_inferred": True,
    }


def star_destroying_left_assignment(occupied_edges, original_left_support):
    """For 1<=k<=6 distinct ORIGINAL left vertices, a LOCAL injection.

    Occupied physical edges are distinct unordered pairs. A common
    coordinate star of >=5 edges kills EVERY six-incidence J with
    EXACT support original_left_support: the common coordinate occurs
    six times when k<=5 and at least five times when k=6, violating
    the necessary degree=2 per-coordinate physical 2-factor condition.
    This local assignment uses no right labels whatsoever.
    """
    if not hasattr(original_left_support, "__iter__"):
        raise ValueError("named original left support required")
    original_left_support = tuple(original_left_support)
    if (not 1 <= len(original_left_support) <= 6
            or len(set(original_left_support)) != len(original_left_support)):
        raise ValueError("support must contain 1..6 different original points")
    edges = tuple(tuple(sorted(e)) for e in occupied_edges)
    if (len(edges) != len(set(edges))
            or any(len(e) != 2 or e[0] == e[1] for e in edges)
            or len(edges) < 6):
        raise ValueError("six or more distinct simple physical pair edges required")
    degrees = Counter(x for edge in edges for x in edge)
    centers = sorted(x for x, degree in degrees.items() if degree >= 5)
    if not centers:
        raise ValueError("no physical star of size five; theorem not applicable")
    center = centers[0]
    star = sorted(e for e in edges if center in e)
    k = len(original_left_support)
    chosen = star[:min(k, 5)]
    if k == 6:
        chosen += [next(e for e in edges if e not in chosen)]
    if len(chosen) != k or len(set(chosen)) != k:
        raise AssertionError("failed to build injective local star assignment")
    return dict(zip(original_left_support, chosen)), center


def exact_sixset_left_projection_invalid(original_six_incidences, local_map):
    """Independent degree diagnostic: six ORIGINAL (point,line) IDs."""
    if (len(original_six_incidences) != 6
            or len(set(original_six_incidences)) != 6
            or any(p not in local_map for p, _ in original_six_incidences)):
        raise ValueError("exactly six distinct mapped original incidences required")
    degrees = Counter()
    for p, _ in original_six_incidences:
        degrees.update(local_map[p])
    return max(degrees.values()) > 2, max(degrees.values())


def genuine_W32_C18_report():
    """Original true W32 incidence examples across A/B/C source shapes."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import (
        PAIRS, selected_left_six, _half_projection_kind,
    )
    m = pair_labeled_symplectic(1, "reverse-line")
    inc = m["incidences"]
    examples = {}
    for six, kind in selected_left_six(m):
        if kind in examples:
            continue
        src = tuple(sorted({inc[e][0] for e in six}))
        mapping, center = star_destroying_left_assignment(PAIRS, src)
        originals = tuple(inc[e] for e in six)
        killed, degree = exact_sixset_left_projection_invalid(
            originals, mapping)
        # Independent accepted left-projection classifier, with filler
        # irrelevant since all touched ORIGINAL source points are mapped.
        f = {i: PAIRS.index(pair) for i, pair in mapping.items()}
        from hyp105_g5e2b3e1c14_domain_certificates import _filled_model
        full = _filled_model(m, f, {})
        observed = _half_projection_kind(
            tuple(p for p, _ in originals), full["left_labels"])
        if not killed or observed is not None or degree < 5:
            raise AssertionError("actual original W32 star does not kill motif")
        examples[kind] = {
            "distinct_original_left_points": len(src),
            "local_killing_star_center": center,
            "left_coordinate_degree": degree,
        }
        if len(examples) == 3:
            break
    if set(examples) != {"A", "B", "C"}:
        raise AssertionError("missing real original GQ A/B/C control")
    return {
        "scope": "W32_NAMED_ORIGINAL_SIX_INCIDENCES_A_B_C",
        "all_h_star_gate_s2": all_h_occupied_star_gate(2),
        "independent_original_W32_motif_controls": examples,
        "zero_bound_is_relaxation_only": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C18_report(), indent=2, sort_keys=True))
