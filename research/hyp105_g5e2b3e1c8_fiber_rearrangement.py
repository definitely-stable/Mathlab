"""HYP-105 C8: exact frozen-fiber rearrangement under ONE common bijection.

Finite oracle for all-V valid lower inequalities; only the B/A source-target
sixset intersection of C0/C5. No GQ all-h positive crossing is inferred.
"""
from collections import defaultdict, Counter
from itertools import permutations
from math import comb, perm

from hyp105_g5e2b3e1c5_common_bijection import (
    validate_weighted_sixsets, physical_occupied_target, fixed_map_overlap,
)
from hyp105_g5e2b3e1c7_adversarial_minimum import rearrangement_lower_bound


def _checked_inputs(source, target, V, D, images):
    if type(V) is not int or V < 6:
        raise ValueError("V must be an integer >=6")
    s = validate_weighted_sixsets(source, V)
    if not isinstance(target, (set, frozenset, tuple, list)):
        raise ValueError("target must be an explicit sixset collection")
    t = validate_weighted_sixsets({R: 1 for R in target}, V)
    if len(t) != len(target):
        raise ValueError("target duplicates are forbidden")
    d = tuple(D)
    p = tuple(images)
    if (len(d) != len(p) or len(d) > V
            or any(type(x) is not int or not 0 <= x < V for x in d+p)
            or len(set(d)) != len(d) or len(set(p)) != len(p)):
        raise ValueError("pins must be two equally sized injective maps")
    return s, tuple(t), d, p


def frozen_fiber_rearrangement(source, target, V, original_pins=(),
                               physical_pins=()):
    """Exact relaxation after freezing ONE partial bijection p:D->physical.

    For each A subset D, source class X_A={R:R intersect D=A} has
    cardinality N_A=C(V-|D|,6-|A|). All full extensions map X_A
    bijectively onto Y_{p(A)}. Relax this induced bijection within
    EACH class to an arbitrary S_{N_A} permutation, independently.
    Hence the class cost is the sum of the q_A SMALLEST weights in
    that class, including all zero weights not explicitly stored.
    """
    source, target, D, p = _checked_inputs(
        source, target, V, original_pins, physical_pins)
    k = len(D)
    src = defaultdict(list)
    for R, w in source.items():
        key = tuple(j for j, i in enumerate(D) if i in R)
        src[key].append(w)
    tgt = Counter()
    for Q in target:
        key = tuple(j for j, i in enumerate(p) if i in Q)
        tgt[key] += 1
    total = 0
    for pattern, count in tgt.items():
        capacity = comb(V-k, 6-len(pattern)) if 0 <= 6-len(pattern) <= V-k else 0
        weights = src[pattern]
        if count > capacity or len(weights) > capacity:
            raise AssertionError("non-bijective conditional sixset fiber")
        missing_zeros = capacity - len(weights)
        if count > missing_zeros:
            total += sum(sorted(weights)[:count-missing_zeros])
    return total


def universal_k_pin_lower(source, target, V, original_pins=(),
                          *, max_prefixes=50000):
    """Global lower bound min_{injective p:D->F} relaxed class costs.

    Exact exhaustive enumeration of the *k-pins*, not V! full maps.
    Enumeration budget is a hard validation gate: no partial minimum
    is returned as a valid universal certificate.
    """
    D = tuple(original_pins)
    if (type(max_prefixes) is not int or max_prefixes < 1
            or any(type(x) is not int or not 0 <= x < V for x in D)
            or len(D) != len(set(D)) or len(D) > V or V < 6):
        raise ValueError("invalid frozen original labels or enumeration cap")
    n = perm(V, len(D))
    if n > max_prefixes:
        raise ValueError("prefix space exceeds cap; no universal claim")
    best = None
    argmin = None
    count = 0
    for images in permutations(range(V), len(D)):
        value = frozen_fiber_rearrangement(source, target, V, D, images)
        count += 1
        if best is None or value < best:
            best, argmin = value, tuple(images)
    if count != n:
        raise AssertionError("incomplete pin enumeration")
    global_base = rearrangement_lower_bound(source, target, V)
    if best < global_base:
        raise AssertionError("conditioning weakened rearrangement relaxation")
    return {
        "V": V, "original_pins": D, "minimum_fiber_lower": best,
        "argmin_physical_pins": argmin,
        "unconditioned_rearrangement_lower": global_base,
        "enumerated_injective_prefixes": count,
        "all_prefixes_exhausted": True,
        "all_h_positive_GQ_crossing_proved": False,
        "scope": "ONE_FIXED_LEFT_f_AND_OCCUPIED_F_BA_ONLY",
    }


def W32_fiber_report():
    """Genuine W32 source/target, only low-k universal relaxations."""
    from itertools import combinations
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph

    F = tuple(combinations(range(6), 2))
    target = physical_occupied_target(6, F)
    lookup = {label: i for i, label in enumerate(F)}
    result = {}
    for kind in ("lex", "reverse-line"):
        model = pair_labeled_symplectic(1, kind)
        source = source_weighted_BA_hypergraph(model)
        pi = tuple(lookup[e] for e in model["right_labels"])
        k0 = universal_k_pin_lower(source, target, 15)
        k1 = universal_k_pin_lower(source, target, 15, (0,))
        k2 = universal_k_pin_lower(source, target, 15, (0, 1))
        actual = fixed_map_overlap(source, target, pi)
        if not 0 <= k0["minimum_fiber_lower"] <= k1["minimum_fiber_lower"] <= k2["minimum_fiber_lower"] <= actual:
            raise AssertionError("invalid W32 universal fiber certificate chain")
        result[kind] = {
            "V": 15, "actual_original_right_g_overlap": actual,
            "unconditional_lower": k0["minimum_fiber_lower"],
            "one_pin_universal_lower": k1["minimum_fiber_lower"],
            "two_pin_universal_lower": k2["minimum_fiber_lower"],
            "one_pin_prefixes": k1["enumerated_injective_prefixes"],
            "two_pin_prefixes": k2["enumerated_injective_prefixes"],
            "f_and_F_minimum_proved": False,
            "seven_family_lower_proved": False,
        }
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(W32_fiber_report(), sort_keys=True, indent=2))
