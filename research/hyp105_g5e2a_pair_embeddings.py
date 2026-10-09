"""HYP-105 G5-E2-A: explicit injective pair-coordinate GQ(s,s) controls.

All-s mathematical map defined via an ordered finite-field projective
point/line list and combinatorial unranking. Executable enumeration and
motif checks only at s=2,4, not an all-s GF5 risk bound. Schemes that
reorder ranks are heuristic CONTROLS, not new ASET theorems.
"""
from itertools import combinations
from math import comb
import json

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e1_motifs import classify_small_split_risk

SCHEMES = ("lex", "reverse-line", "coordinate-flag")


def pair_alphabet_size(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("expected positive number of GQ vertices")
    a = 2
    while comb(a, 2) < n:
        a += 1
    return a


def unrank_pair(rank, alphabet_size):
    """Exact lexicographic combinatorial unranking; valid for all a>=2."""
    if not isinstance(alphabet_size, int) or alphabet_size < 2:
        raise ValueError("alphabet size >=2 required")
    if not isinstance(rank, int) or not 0 <= rank < comb(alphabet_size, 2):
        raise ValueError("rank outside coordinate-pair alphabet")
    for a in range(alphabet_size - 1):
        count = alphabet_size - a - 1
        if rank < count:
            return (a, a + rank + 1)
        rank -= count
    raise AssertionError("pair unranking unreachable")


def _rank_order(field, points, lines, scheme):
    """Explicit independently injective object orders.

    'coordinate-flag' is basis-dependent, not a symplectic-invariant
    orbit quotient; it is a negative/positive CONTROL to compare finite
    motif multiplicities, with no claim about good all-s density.
    """
    if scheme not in SCHEMES:
        raise ValueError("unknown explicit scheme")
    v = len(points)
    if len(lines) != v:
        raise AssertionError("GQ(s,s) point/line count not balanced")
    if scheme == "lex":
        return tuple(range(v)), tuple(range(v))
    if scheme == "reverse-line":
        return tuple(range(v)), tuple(reversed(range(v)))

    def point_flag(p):
        return (field.mul(p[0], p[2]) ^ field.mul(p[1], p[3]),
                p[2], p[0], p[1], p[3])
    point_order = tuple(sorted(range(v), key=lambda i: point_flag(points[i])))
    # The line order is a DIFFERENT field-coordinate-dependent flag
    # requiring the full set of incident projective points. Tie break
    # by the existing exact sorted three/five-point line tuple.
    def line_flag(line):
        trace = 0
        for i in line:
            trace ^= field.mul(points[i][0], points[i][3])
        return (trace, tuple(point_flag(points[i]) for i in line),
                line)
    line_order = tuple(sorted(range(v), key=lambda i: line_flag(lines[i])))
    if len(set(point_order)) != v or len(set(line_order)) != v:
        raise AssertionError("non-bijective object rank orders")
    return point_order, line_order


def pair_labeled_symplectic(power, scheme="lex"):
    """One finite true GF(2^h) symplectic graph to 2+2 supports.

    Mathematical ranking/unranking formula applies to all h for which
    finite fields GF(2^h) are defined. Executable enumeration is capped
    here at h=1,2 to guard hosted CI cost, NOT a mathematical no-go.
    """
    if power not in (1, 2):
        raise ValueError("hosted pair enumeration restricted to h=1 or 2")
    field, points, lines, incidence = symplectic_gq(power)
    v = len(points)
    a = pair_alphabet_size(v)
    palette = tuple(combinations(range(a), 2))
    if len(palette) != comb(a, 2):
        raise AssertionError("pair alphabet bad")
    po, lo = _rank_order(field, points, lines, scheme)
    left = [None] * v
    right = [None] * v
    for rank, object_id in enumerate(po):
        left[object_id] = unrank_pair(rank, a)
    for rank, object_id in enumerate(lo):
        right[object_id] = unrank_pair(rank, a)
    if len(set(left)) != v or len(set(right)) != v:
        raise AssertionError("pair-label injections unexpectedly collide")
    supports = tuple(
        tuple(sorted(left[pid] + tuple(a+x for x in right[lid])))
        for pid, lid in incidence
    )
    if len(set(supports)) != len(incidence):
        raise AssertionError("distinct true graph edges yielded duplicate columns")
    if any(len(s) != 4 or sum(c < a for c in s) != 2
           or sum(a <= c < 2*a for c in s) != 2 for s in supports):
        raise AssertionError("not globally split exact 2+2")
    return {
        "s": field.q, "h": power, "m": 2*a,
        "a": a, "v": v, "N": len(incidence),
        "scheme": scheme,
        "points": points, "lines": lines,
        "incidences": incidence,
        "left_labels": tuple(left), "right_labels": tuple(right),
        "supports": supports,
        "all_s_risk_power_proved": False,
    }


def small_motif_probe(model, sample_size=8):
    """Avoid O(N^6): only selected 8-column subsample, not all GQ(s,s)."""
    n = model["N"]
    if sample_size > 9 or not 2 <= sample_size <= n:
        raise ValueError("sample limited to 2..9 unique graph edges")
    # Deterministic spaced sample, distinct even if N divisible by 53:
    candidate = []
    for j in range(n):
        idx = (53*j + 7) % n
        if idx not in candidate:
            candidate.append(idx)
        if len(candidate) == sample_size:
            break
    if len(candidate) < sample_size:
        raise AssertionError("bounded sample selector not injective")
    selected = tuple(model["supports"][i] for i in candidate)
    return {
        "sample_indices": tuple(candidate),
        "k2": {
            k: v for k, v in classify_small_split_risk(
                selected, model["a"], 2).items() if k != "motif_counts"
        },
        "k3": {
            k: v for k, v in classify_small_split_risk(
                selected, model["a"], 3).items() if k != "motif_counts"
        },
    }


def report():
    result = []
    for h in (1, 2):
        for scheme in SCHEMES:
            model = pair_labeled_symplectic(h, scheme)
            probe = small_motif_probe(model)
            result.append({
                "field": "GF(2^%d)" % h,
                "s": model["s"], "m": model["m"], "a": model["a"],
                "vertices_each_half": model["v"],
                "original_graph_edges": model["N"],
                "scheme": scheme,
                "motif_sample_size": len(probe["sample_indices"]),
                "sample_k2_potential_flow_events":
                    probe["k2"]["possible_events"],
                "sample_k3_potential_flow_events":
                    probe["k3"]["possible_events"],
                "all_s_nonzero_flow_risk_bound": None,
                "new_aset_power_proven": False,
            })
    return {
        "scope": "GF(2)/GF(4) executable, all-h rank injection formula",
        "published_GQ_girth_exact": 8,
        "input_model": "projective symplectic W(3,2^h)",
        "coefficient_field": "GF(5), not geometry field",
        "cases": result,
    }


if __name__ == "__main__":
    print(json.dumps(report(), sort_keys=True, indent=2))
