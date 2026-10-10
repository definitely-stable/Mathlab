"""HYP-105 C7: finite deterministic right-bijection minimum, strict scope.

Only B-left/A-right original-sixset overlap with one fixed f and occupied F.
Neither a general-GQ all-h theorem nor the full seven-class S bound.
"""
from math import comb
from hyp105_g5e2b3e1c5_common_bijection import (
    validate_weighted_sixsets, fixed_map_overlap,
)


def _bitmask(R):
    return sum(1 << i for i in R)


def rearrangement_lower_bound(source, target, V):
    """Relax S_V to arbitrary permutations of all C(V,6) sixset cells.

    The smallest |target| entries among the weighted source cells,
    including zeros outside its support, sum to a rigorous lower bound.
    """
    src = validate_weighted_sixsets(source, V)
    tgt = validate_weighted_sixsets({R: 1 for R in target}, V)
    if len(tgt) != len(target):
        raise ValueError("duplicate target")
    need = max(0, len(tgt) - (comb(V, 6) - len(src)))
    return sum(sorted(src.values())[:need])


def exact_adversarial_minimum(source, target, V, *, max_nodes=500000):
    """Exact finite minimum, zero witness, or honest budget-limited UNKNOWN.

    For a partial original->occupied bijection, the possible images of
    each source sixset are ALL target sixsets compatible with its inside
    and outside assignments. If every compatible image lies in target,
    that source multiplicity is unavoidable in ALL completions.
    This gives a monotone admissible branch-and-bound lower bound.

    A zero witness proves minimum zero by nonnegativity. A positive
    minimum requires completed search or equality with the independent
    sixset-rearrangement relaxation; a budget cut NEVER certifies it.
    """
    if type(V) is not int or not 6 <= V <= 9:
        raise ValueError("exact permutation search restricted to 6<=V<=9")
    if type(max_nodes) is not int or max_nodes < 1:
        raise ValueError("max_nodes must be a positive integer")
    src = validate_weighted_sixsets(source, V)
    tgt = validate_weighted_sixsets({R: 1 for R in target}, V)
    if len(tgt) != len(target):
        raise ValueError("duplicate target")
    identity = tuple(range(V))
    if not src or not tgt:
        return {"status": "ZERO_WITNESS", "exact_minimum": 0,
                "certified_lower": 0, "witness_upper": 0,
                "witness_permutation": identity, "nodes": 0,
                "exhaustive": False, "model": "ONE_FIXED_f_F_BA_ONLY"}

    items = tuple((_bitmask(R), w) for R, w in src.items())
    masks = tuple(_bitmask(R) for R in tgt)
    masses = [sum(w for R, w in items if R & (1 << i)) for i in range(V)]
    order = tuple(sorted(range(V), key=lambda i: (-masses[i], i)))
    base = rearrangement_lower_bound(src, tgt, V)
    reverse = tuple(reversed(identity))
    best_value, best_perm = min(
        (fixed_map_overlap(src, tgt, pi), pi) for pi in (identity, reverse))
    if best_value == base:
        return {"status": "ZERO_WITNESS" if best_value == 0 else "CERTIFIED_MINIMUM",
                "exact_minimum": best_value, "certified_lower": base,
                "witness_upper": best_value, "witness_permutation": best_perm,
                "nodes": 0, "exhaustive": False, "model": "ONE_FIXED_f_F_BA_ONLY"}

    cache = {}
    nodes = 0
    truncated = False
    prefix = []

    def forced_lower():
        assigned = len(prefix)
        pairs = [(1 << order[j], 1 << prefix[j]) for j in range(assigned)]
        forced = 0
        for edge, weight in items:
            inside = 0
            outside = 0
            for original, physical in pairs:
                if edge & original:
                    inside |= physical
                else:
                    outside |= physical
            key = (inside, outside)
            certain = cache.get(key)
            if certain is None:
                capacity = comb(V - assigned, 6 - inside.bit_count())
                count = sum((T & inside) == inside and not (T & outside)
                            for T in masks)
                if count > capacity:
                    raise AssertionError("source-target completion count contradiction")
                certain = count == capacity
                cache[key] = certain
            if certain:
                forced += weight
        return forced

    def visit(occupied):
        nonlocal nodes, truncated, best_value, best_perm
        if nodes >= max_nodes:
            truncated = True
            return
        nodes += 1
        bound = forced_lower()
        if bound >= best_value:
            return
        if len(prefix) == V:
            if bound < best_value:
                mapping = [0] * V
                for i, physical in enumerate(prefix):
                    mapping[order[i]] = physical
                best_perm = tuple(mapping)
                best_value = bound
            return
        for physical in range(V):
            if not occupied & (1 << physical):
                prefix.append(physical)
                visit(occupied | (1 << physical))
                prefix.pop()
                if best_value == base or truncated:
                    return

    visit(0)
    exact = (not truncated) or best_value == base
    return {"status": ("ZERO_WITNESS" if best_value == 0 else "CERTIFIED_MINIMUM")
            if exact else "UNKNOWN_BUDGET",
            "exact_minimum": best_value if exact else None,
            "certified_lower": best_value if exact else base,
            "witness_upper": best_value, "witness_permutation": best_perm,
            "nodes": nodes, "exhaustive": not truncated,
            "model": "ONE_FIXED_f_F_BA_ONLY"}


def W32_rearrangement_report():
    """True W(3,2): support-only relaxation, NOT factorial optimization."""
    from itertools import combinations
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    from hyp105_g5e2b3e1c5_common_bijection import physical_occupied_target
    F = tuple(combinations(range(6), 2))
    target = physical_occupied_target(6, F)
    index = {edge: i for i, edge in enumerate(F)}
    result = {}
    for scheme in ("lex", "reverse-line"):
        model = pair_labeled_symplectic(1, scheme)
        src = source_weighted_BA_hypergraph(model)
        pi = tuple(index[edge] for edge in model["right_labels"])
        result[scheme] = {
            "V": 15, "source_support": len(src),
            "target_support": len(target), "ambient_sixsets": comb(15, 6),
            "support_only_rearrangement_lower":
                rearrangement_lower_bound(src, target, 15),
            "one_actual_fixed_map_overlap": fixed_map_overlap(src, target, pi),
            "full_minimum_certified": False,
        }
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(W32_rearrangement_report(), indent=2, sort_keys=True))
