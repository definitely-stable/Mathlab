"""AA4-BM: four-transposition pinned-root B/A repair, original W(3,2^h).

Research draft: the repair changes at most four *opposite original factor*
images of ONE complete globally injected map.  Two genuine source root
images remain pinned.  Does NOT assert positivity on the input fixed map.
"""
from itertools import combinations, permutations, product
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    robust_all_h_two_root_pin_BA_floor,
    every_fixed_original_g_good_root_pin_majority,
)


def repair_four_prescribed_images(images, prescription, protected=()):
    """At most k<=4 transpositions, preserving protected original factor IDs.

    Image labels may be arbitrary hashable occupied physical pairs.  Swaps
    change images assigned to ORIGINAL factor IDs, not physical endpoints.
    """
    labels = tuple(tuple(sorted(e)) for e in images)
    if len(set(labels)) != len(labels):
        raise ValueError("a complete globally injective map is required")
    requests = tuple((i, tuple(sorted(edge))) for i, edge in prescription)
    frozen = set(protected)
    ids = [i for i, _ in requests]
    targets = [edge for _, edge in requests]
    if len(requests) > 4 or len(set(ids)) != len(ids) or len(set(targets)) != len(targets):
        raise ValueError("at most four distinct original source IDs and distinct target images")
    if any(type(i) is not int or i < 0 or i >= len(labels) or i in frozen for i in ids):
        raise ValueError("prescribed original factor is invalid or protected")
    if any(type(i) is not int or i < 0 or i >= len(labels) for i in frozen):
        raise ValueError("protected original factor outside complete map")
    if any(edge not in labels for edge in targets):
        raise ValueError("target physical image not in original occupied support")
    if any(labels[i] in set(targets) for i in frozen):
        raise ValueError("cannot move a protected pinned source image")
    result = list(labels)
    reverse = {e: i for i, e in enumerate(result)}
    swaps = []
    for i, desired in requests:
        owner = reverse[desired]
        if owner == i:
            continue
        if owner in frozen:
            raise AssertionError("an occupied target unexpectedly belongs to a protected ID")
        old = result[i]
        result[i], result[owner] = result[owner], result[i]
        reverse[old], reverse[desired] = owner, i
        swaps.append((i, owner))
    if tuple(result[i] for i in frozen) != tuple(labels[i] for i in frozen):
        raise AssertionError("pinned original source images changed")
    if any(result[i] != edge for i, edge in requests) or len(swaps) > 4:
        raise AssertionError("four-swap prescription was not fulfilled")
    return tuple(result), tuple(swaps)


def first_genuine_original_root_C4_sixflag(model, side, root, flags):
    """A TRUE six-distinct incidence-ID B/C4 source-Q, not a synthetic Q."""
    s, V, a, incidence, f, g, byP, byL = _original_source(model)
    if type(side) is not int or side not in (0, 1):
        raise ValueError("typed side must be 0 (POINT) or 1 (LINE)")
    roots = (byP, byL)[side]
    pair = tuple(flags)
    if type(root) is not int or root not in range(V) or len(pair) != 2 or len(set(pair)) != 2:
        raise ValueError("two different genuine original rooted flags required")
    if any(type(j) is not int or j not in roots[root] for j in pair):
        raise ValueError("both flags must meet the actual original root")
    original_opposite = {incidence[j][1-side] for j in pair}
    if len(original_opposite) != 2:
        raise AssertionError("two source cherry flags must have distinct opposite factors")
    first = (f, g)[side]
    complement = [v for v in range(a) if v not in first[root]]
    inv = {edge: p for p, edge in enumerate(first)}
    for vertices in combinations(complement, 4):
        for kind, physical_edges in _full_four_patterns(vertices, set(first))[2]:
            if kind != "C4":
                continue
            factors = tuple(inv[e] for e in physical_edges)
            if len(set(factors)) != 4 or root in factors:
                raise AssertionError("source physical four-cycle not on distinct ORIGINAL factors")
            for chosen in product(*(roots[p] for p in factors)):
                Q = pair + tuple(chosen)
                if len(set(Q)) != 6:
                    continue
                opposite_ids = tuple(incidence[j][1-side] for j in Q)
                if len(set(opposite_ids)) == 6:
                    return tuple(Q), opposite_ids
    return None


def iter_occupied_two_pin_A_targets(occupied, a, pin1, pin2):
    """Independent exact physical 6-cycle / disjoint-two-triangle generator.

    Targets are UNORDERED six-edge sets, with canonical connected cycle
    direction and unordered triangle partition; two pins must be present.
    """
    E = {tuple(sorted(e)) for e in occupied}
    pins = {tuple(sorted(pin1)), tuple(sorted(pin2))}
    if len(E) != len(tuple(occupied)) or len(pins) != 2 or not pins <= E:
        raise ValueError("two different pins in a globally injected edge support required")
    fixed_vertices = set(pin1 + pin2)
    for six in combinations(range(a), 6):
        if not fixed_vertices <= set(six):
            continue
        for tail in permutations(six[1:]):
            cycle = (six[0],) + tail
            if cycle[1] > cycle[5]:
                continue
            edges = frozenset(tuple(sorted((cycle[i], cycle[(i+1)%6]))) for i in range(6))
            if pins <= edges and edges <= E:
                yield edges
        for tri_tail in combinations(six[1:], 2):
            tr1 = set((six[0],) + tri_tail)
            tr2 = set(six) - tr1
            edges = frozenset(tuple(sorted(e)) for tri in (tr1, tr2)
                              for e in combinations(sorted(tri), 2))
            if pins <= edges and edges <= E:
                yield edges


def repair_genuine_original_cherry(model, side, root, flags):
    """One actual fixed f,g -> one root-accepted original B/A via <=4 swaps.

    This is a finite *witness construction*; the all-h existence of Q and
    target uses the strict-parent AA4-BK/BL estimates for s>=32.
    """
    s, V, a, incidence, f, g, byP, byL = _original_source(model)
    original = (f, g)[1-side]
    pair = tuple(flags)
    if len(pair) != 2 or any(type(j) is not int or j < 0 or j >= len(incidence) for j in pair):
        raise ValueError("genuine original incidence IDs required")
    pins_ids = tuple(incidence[j][1-side] for j in pair)
    if len(set(pins_ids)) != 2:
        raise ValueError("distinct original opposite factor IDs required")
    pins = [original[i] for i in pins_ids]
    six = first_genuine_original_root_C4_sixflag(model, side, root, pair)
    if six is None:
        return None
    Q, source_ids = six
    unpinned = tuple(i for i in source_ids if i not in pins_ids)
    if len(unpinned) != 4 or len(set(unpinned)) != 4:
        raise AssertionError("six original opposite source factors must be distinct")
    target = next(iter_occupied_two_pin_A_targets(original, a, *pins), None)
    if target is None:
        return None
    rest = sorted(target - set(pins))
    if len(rest) != 4:
        raise AssertionError("six physical target edges include exactly two pinned edges")
    repaired, swaps = repair_four_prescribed_images(
        original, tuple(zip(unpinned, rest)), protected=pins_ids)
    degrees = {}
    for j in Q:
        for col in repaired[incidence[j][1-side]]:
            degrees[col] = degrees.get(col, 0) + 1
    if len(degrees) != 6 or set(degrees.values()) != {2}:
        raise AssertionError("same six TRUE original incidence IDs not right A/2-regular")
    return {"s":s, "source_six_original_flag_IDs":Q,
            "pinned_actual_original_opposite_factor_IDs":pins_ids,
            "source_opposite_six_original_factors":source_ids,
            "fixed_original_complete_opposite_images":tuple(original),
            "repaired_complete_opposite_images":repaired,
            "physical_A_target":tuple(sorted(target)),
            "transpositions_of_original_factor_images":swaps,
            "rooted_historical_positive_class":"B/A" if side == 0 else "A/B",
            "original_first_side_unchanged":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def all_h_pin_regular_four_swap_certificate(s):
    """ALL dyadic s>=32 (not a fake instantiated high-order GQ)."""
    z = robust_all_h_two_root_pin_BA_floor(s)
    p = every_fixed_original_g_good_root_pin_majority(s)
    t_floor = z["both_types_physical_A_with_two_pins_lower"]
    if t_floor <= 0:
        raise AssertionError("no pinned physical A templates under BL-LOCAL")
    return {"s":s,"a":z["a"],"V":z["V"],
            "good_actual_original_cherry_root_fraction_lower":
                p["fraction_true_original_cherries_with_regular_two_pinned_images_lower"],
            "distinct_global_4swap_repairs_for_EACH_good_root_lower":
                24*t_floor,
            "given_entire_input_original_g_actual_accepted_count_NOT_BOUNDED":True,
            "same_single_repaired_g_for_all_roots_NOT_PROVED":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
