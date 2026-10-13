"""HYP-105 issue #230 D6-U: proper-scope minima vanish for ORIGINAL sixsets.

Theorem for every s=2**h, h>=1, and every ORIGINAL six-incidence
subset Q of W(3,s): for ANY locally injective physical edge labels
prescribed on a PROPER subset of its ORIGINAL typed endpoint factors,
a globally extendible completion exists with F_Q=0, both for the seven
accepted GF(5)-positive indicator and its nonnegative selected weight.

The proof uses two separate facts: the GQ incidence graph has girth 8,
so every six-edge subgraph is a forest with >=7 typed vertices; and
one FREE factor on either side can always be labelled to violate the
necessary six-coordinate, degree-two physical projection.

This is a NO-GO for certificates using ONLY proper-scope conditional
MINIMA of INDIVIDUAL sixset factors. It is emphatically NOT a NO-GO
for general Sherali-Adams/SOS, arbitrary joint marginals, or Branch A.
"""
from collections import Counter
from itertools import combinations
import json


def physical_two_regular(original_six_endpoints, labels):
    """Independent necessary physical condition shared by all seven classes."""
    deg = Counter(c for v in original_six_endpoints for c in labels[v])
    return len(deg) == 6 and all(x == 2 for x in deg.values())


def _check_prescribed(ordered, prescribed, a):
    if not isinstance(prescribed, dict) or any(v not in ordered for v in prescribed):
        raise ValueError("pinned map must use only scoped ORIGINAL factor IDs")
    seen = set()
    for edge in prescribed.values():
        if (not isinstance(edge, (tuple, list)) or len(edge) != 2
                or any(type(x) is not int for x in edge)
                or not 0 <= edge[0] < edge[1] < a
                or tuple(edge) in seen):
            raise ValueError("pinned physical pairs must be distinct canonical K_a edges")
        seen.add(tuple(edge))


def _first_unused(a, used):
    for edge in combinations(range(a), 2):
        if edge not in used:
            return edge
    raise AssertionError("not enough physical labels for local completion")


def complete_injection(endpoints, prescribed, a):
    """Extend a locally injective fixed map, without a GF5 assertion."""
    ordered = tuple(dict.fromkeys(endpoints))
    _check_prescribed(ordered, prescribed, a)
    result = {v: tuple(e) for v, e in prescribed.items()}
    used = set(result.values())
    for v in ordered:
        if v not in result:
            edge = _first_unused(a, used)
            result[v] = edge
            used.add(edge)
    if len(result) != len(ordered) or len(used) != len(ordered):
        raise AssertionError("local injectivity not preserved")
    return result


def free_site_bad_projection(endpoints, prescribed, a):
    """Constructively invalidate six physical columns with one FREE site.

    Fix every other unpinned original factor arbitrarily, then choose
    the final free ORIGINAL factor's pair. Its multiplicity is 1, 2,
    or >=3: respectively at most ONE pair can be a valid completion,
    an unused pair incident with an occupied coordinate makes degree
    >=3, or EVERY pair makes degree>=3. a>=6 guarantees a candidate.
    """
    ends = tuple(endpoints)
    if (len(ends) != 6 or type(a) is not int or a < 6
            or any(type(x) is not int or x < 0 for x in ends)):
        raise ValueError("six ORIGINAL factor positions and a>=6 required")
    ordered = tuple(dict.fromkeys(ends))
    _check_prescribed(ordered, prescribed, a)
    free = [v for v in ordered if v not in prescribed]
    if not free:
        raise ValueError("proper subset required: at least one free ORIGINAL factor")
    if len(ordered) > a * (a - 1) // 2:
        raise ValueError("K_a too small for distinct local ORIGINAL factors")
    pivot = free[-1]
    fixed = complete_injection(ordered[:-1] if ordered[-1] == pivot else
         tuple(v for v in ordered if v != pivot), prescribed, a)
    used = set(fixed.values())
    multiplicity = ends.count(pivot)
    if multiplicity == 2:
        deg = Counter(c for v in ends if v != pivot for c in fixed[v])
        if not deg:
            raise AssertionError("two occurrences leave four occupied positions")
        u = next(iter(deg))
        candidates = (tuple(sorted((u, v))) for v in range(a) if v != u)
    else:
        candidates = combinations(range(a), 2)
    attempts = 0
    for edge in candidates:
        if edge in used:
            continue
        attempts += 1
        completed = dict(fixed)
        completed[pivot] = edge
        if not physical_two_regular(ends, completed):
            if len(set(completed.values())) != len(ordered):
                raise AssertionError("constructive injection violated")
            return {
                "labels": completed,
                "pivot_original_factor": pivot,
                "pivot_multiplicity": multiplicity,
                "candidates_tested": attempts,
                "bad_projection": True,
            }
    raise AssertionError("free-factor completion theorem failed")


def original_sixset_forest_scope(six_incidences):
    """Fail-closed six-edge typed forest oracle (real GQ edges supplied)."""
    edges = tuple(six_incidences)
    if (len(edges) != 6 or len(set(edges)) != 6
            or any(not isinstance(e, (tuple, list)) or len(e) != 2
                   or any(type(z) is not int or z < 0 for z in e)
                   for e in edges)):
        raise ValueError("six DISTINCT ORIGINAL point-line incidences required")
    parent = {}
    def root(u):
        parent.setdefault(u, u)
        while parent[u] != u:
            u = parent[u]
        return u
    for p, l in edges:
        u, v = ("P", p), ("L", l)
        ru, rv = root(u), root(v)
        if ru == rv:
            raise ValueError("six ORIGINAL incidences contain a cycle: not a GQ sixset")
        parent[ru] = rv
    L = tuple(dict.fromkeys(p for p, _ in edges))
    R = tuple(dict.fromkeys(l for _, l in edges))
    if len(L) + len(R) < 7:
        raise AssertionError("six distinct forest edges have at least seven sites")
    return L, R


def proper_scope_zero_witness(six_incidences, a, pinned_left, pinned_right):
    """Complete both typed local injections and force the seven-class cost 0.

    Uses ONLY the necessary two-regularity condition, so works for any
    accepted seven-GF5 classifier and any nonnegative class coefficient.
    Local completion extends globally whenever K_a >= V_s.
    """
    if type(a) is not int or a < 6:
        raise ValueError("a>=6 required")
    edges = tuple(tuple(e) for e in six_incidences)
    L, R = original_sixset_forest_scope(edges)
    left_ends = tuple(p for p, _ in edges)
    right_ends = tuple(l for _, l in edges)
    _check_prescribed(L, pinned_left, a)
    _check_prescribed(R, pinned_right, a)
    if len(pinned_left) == len(L) and len(pinned_right) == len(R):
        raise ValueError("only proper scopes have unconditional zero minima")
    if len(pinned_left) < len(L):
        side = "left"
        wl = free_site_bad_projection(left_ends, pinned_left, a)
        f = wl["labels"]
        g = complete_injection(R, pinned_right, a)
        chosen = wl
    else:
        side = "right"
        f = complete_injection(L, pinned_left, a)
        wr = free_site_bad_projection(right_ends, pinned_right, a)
        g = wr["labels"]
        chosen = wr
    return {
        "scope_size": len(L) + len(R),
        "prescribed_size": len(pinned_left) + len(pinned_right),
        "invalidated_side": side,
        "pivot_original_factor": chosen["pivot_original_factor"],
        "pivot_multiplicity": chosen["pivot_multiplicity"],
        "candidate_edges_tested": chosen["candidates_tested"],
        "left_labels": f,
        "right_labels": g,
        "left_two_regular": physical_two_regular(left_ends, f),
        "right_two_regular": physical_two_regular(right_ends, g),
        "seven_GF5_positive_indicator": 0,
        "selected_nonnegative_GF5_weight": 0,
        "local_injections_globally_extendible_when_K_ge_V": True,
    }


def report():
    # Six-edge path, seven typed ORIGINAL sites, a=6, six pinned sites.
    edges = ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2))
    L, R = original_sixset_forest_scope(edges)
    pin_L = {v: e for v, e in zip(L, ((0, 1), (0, 2), (0, 3), (0, 4)))}
    pin_R = {R[0]: (1, 2), R[1]: (1, 3)}
    witness = proper_scope_zero_witness(edges, 6, pin_L, pin_R)
    if witness["left_two_regular"] and witness["right_two_regular"]:
        raise AssertionError("proper-scope witness does not invalidate GF5")
    return {
        "slice": "HYP105-ISSUE230-D6U-PROPER-SCOPE-ZERO-NOGO",
        "theorem": "ALL-H-EVERY-PROPER-LOCAL-SCOPE-GF5-MINIMUM-ZERO",
        "original_sixset_min_typed_scope": 7,
        "all_conditional_minima_for_k_le_6": "ZERO",
        "stronger_every_proper_scope_minimum": "ZERO",
        "no_go_scope": "INDIVIDUAL_FACTOR_PROPER-SCOPE-CONDITIONAL-MINIMA-ONLY",
        "general_Sherali_Adams_no_go": False,
        "Branch_A": "OPEN", "Branch_B": "OPEN",
        "finite_constructive_check": {
            k: witness[k] for k in (
                "scope_size", "prescribed_size", "invalidated_side",
                "left_two_regular", "right_two_regular",
                "candidate_edges_tested", "seven_GF5_positive_indicator")
        },
    }


if __name__ == "__main__":
    print(json.dumps(report(), sort_keys=True))
