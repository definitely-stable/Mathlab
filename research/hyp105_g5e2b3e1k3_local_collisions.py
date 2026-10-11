"""HYP-105 E1-K3-A/B: exact endpoint-local 3-path collision certificates.

These are exact identities for arbitrary finite simple graphs, NOT a
uniform all-h bound on legal W(3,s) pair-labelings. In particular filtering
on the endpoint codegree alone does not control the internal collision mass.
No Branch A/B, complete R3 bound, or ASET exponent is claimed.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import ceil
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph


def _validate_graph(neighbors):
    n = len(neighbors)
    for u, row in enumerate(neighbors):
        for v in row:
            if type(v) is not int or v < 0 or v >= n or v == u:
                raise ValueError("simple graph without loops required")
            if u not in neighbors[v]:
                raise ValueError("symmetric simple graph required")


def endpoint_collision_rows(neighbors, *, max_pairs=50_000,
                            max_paths=2_000_000):
    """Yield ordered-endpoint collision profiles, including zero-path pairs.

    Let k_z(u,v) count 3-paths with z as ONE of their two internal
    vertices, and b(u,v) count unordered central edges {b,c} for
    which both u-b-c-v and u-c-b-v exist. Then, exactly:

        Theta(u,v) = sum_z k_z(k_z-1) - 2*b(u,v)
        Theta_two_internal(u,v) = 2*b(u,v)
        Theta_one_internal(u,v) = sum_z k_z(k_z-1) - 4*b(u,v)
        D(u,v) = P3(u,v)*(P3(u,v)-1) - Theta(u,v).

    D counts ordered pairs of internally disjoint paths. Summing over
    all ordered u!=v gives exactly 12*C6. No pairwise path comparisons
    are used in this production implementation.

    This function deliberately fails closed before exceeding budgets.
    It stores path interiors for one start vertex at a time.
    """
    if type(max_pairs) is not int or max_pairs < 0:
        raise ValueError("max_pairs must be a nonnegative integer")
    if type(max_paths) is not int or max_paths < 0:
        raise ValueError("max_paths must be a nonnegative integer")
    _validate_graph(neighbors)
    n = len(neighbors)
    if n * (n - 1) > max_pairs:
        raise RuntimeError("endpoint-pair budget exceeded (fail closed)")
    walked = 0
    for u in range(n):
        # v -> [path count, internal vertex loads, central edge masks].
        by_endpoint = {}
        for b in neighbors[u]:
            for c in neighbors[b]:
                if c == u:
                    continue
                for v in neighbors[c]:
                    if v == b or v == u:
                        continue
                    walked += 1
                    if walked > max_paths:
                        raise RuntimeError("3-path budget exceeded (fail closed)")
                    if v not in by_endpoint:
                        by_endpoint[v] = [0, Counter(), {}]
                    record = by_endpoint[v]
                    record[0] += 1
                    record[1][b] += 1
                    record[1][c] += 1
                    pair = (min(b, c), max(b, c))
                    masks = record[2]
                    masks[pair] = masks.get(pair, 0) | (1 if b < c else 2)

        for v in range(n):
            if v == u:
                continue
            paths, loads, masks = by_endpoint.get(v, (0, {}, {}))
            repeated = sum(t * (t - 1) for t in loads.values())
            reversed_edges = sum(bits == 3 for bits in masks.values())
            shared_one = repeated - 4 * reversed_edges
            shared_two = 2 * reversed_edges
            theta = shared_one + shared_two
            disjoint = paths * (paths - 1) - theta
            if shared_one < 0 or disjoint < 0:
                raise AssertionError("invalid path-collision partition")
            yield {
                "u": u, "v": v, "p3": paths,
                "max_internal_load": max(loads.values(), default=0),
                "one_internal": shared_one,
                "two_internal": shared_two,
                "theta": theta,
                "disjoint": disjoint,
            }


def localized_certificate(neighbors, mode="all", threshold=None, *,
                          max_pairs=50_000, max_paths=2_000_000):
    """C6 >= (M_U^2/|U| - M_U - Theta_U)/12 for any endpoint set U.

    Modes:
      all: all u!=v, including zero-path pairs
      active: only pairs with positive P3
      endpoint-codegree: active pairs with |N(u) intersect N(v)| <= threshold
      internal-load: active pairs with max_z k_z(u,v) <= threshold

    Subsets may be selected after seeing the whole graph: the certificate
    remains pointwise valid. Empty U yields only the trivial C6>=0.
    """
    modes = ("all", "active", "endpoint-codegree", "internal-load")
    if mode not in modes:
        raise ValueError("unknown endpoint selection")
    if mode in ("endpoint-codegree", "internal-load"):
        if type(threshold) is not int or threshold < 0:
            raise ValueError("threshold must be a nonnegative integer")
    elif threshold is not None:
        raise ValueError("threshold is only valid for bounded selectors")
    selected = 0
    p3_selected = theta_selected = disjoint_selected = 0
    one_selected = two_selected = 0
    p3_all = theta_all = disjoint_all = 0
    for row in endpoint_collision_rows(neighbors, max_pairs=max_pairs,
                                       max_paths=max_paths):
        p, theta = row["p3"], row["theta"]
        p3_all += p
        theta_all += theta
        disjoint_all += row["disjoint"]
        if mode == "all":
            keep = True
        elif mode == "active":
            keep = p > 0
        elif mode == "endpoint-codegree":
            keep = p > 0 and len(neighbors[row["u"]] &
                                  neighbors[row["v"]]) <= threshold
        else:
            keep = p > 0 and row["max_internal_load"] <= threshold
        if keep:
            selected += 1
            p3_selected += p
            theta_selected += theta
            disjoint_selected += row["disjoint"]
            one_selected += row["one_internal"]
            two_selected += row["two_internal"]

    lower = (Fraction(p3_selected * p3_selected, selected)
             - p3_selected - theta_selected) if selected else Fraction(0)
    if disjoint_selected < lower:
        raise AssertionError("localized Cauchy-Schwarz inequality violated")
    return {
        "mode": mode, "threshold": threshold,
        "graph_order": len(neighbors),
        "ordered_pairs": len(neighbors) * (len(neighbors) - 1),
        "selected_pairs": selected,
        "all_P3": p3_all, "all_Theta": theta_all,
        "all_disjoint": disjoint_all,
        "selected_P3": p3_selected, "selected_Theta": theta_selected,
        "selected_one_internal": one_selected,
        "selected_two_internal": two_selected,
        "selected_disjoint": disjoint_selected,
        "retained_path_fraction": str(Fraction(p3_selected, p3_all)) if p3_all else "0",
        "CS_disjoint_floor": str(lower),
        "C6_rational_floor": str(lower / 12),
        "C6_integer_floor": max(0, ceil(lower / 12)),
    }


def book_graph(t):
    """K_{2,t}, a counterexample to endpoint-codegree-only filtering."""
    if type(t) is not int or t < 2:
        raise ValueError("book parameter t>=2 required")
    rows = [set() for _ in range(t + 2)]
    for w in range(2, t + 2):
        for u in (0, 1):
            rows[u].add(w)
            rows[w].add(u)
    return tuple(frozenset(row) for row in rows)


def star_degree_tensor(model):
    """Independent GQ incidence-star formula for ALL Kikuchi degrees.

    d(x,y) = sum_{z!=x,t!=y} I(F_{xz}, G_{yt}).
    Each incidence gives exactly four physical star memberships.
    """
    a = model["a"]
    deg = [0] * (a * a)
    for p, l in model["incidences"]:
        for x in model["left_labels"][p]:
            for y in model["right_labels"][l]:
                deg[x * a + y] += 1
    return tuple(deg)


def star_codegree_tensor(model, u, v):
    """Independent original-incidence contraction for c_Ghat(u,v).

    Missing physical pair labels have zero incidence. The formula works
    with equal or unequal first/second endpoint coordinates.
    """
    a = model["a"]
    if not (type(u) is int and type(v) is int
            and 0 <= u < a * a and 0 <= v < a * a and u != v):
        raise ValueError("distinct valid Kikuchi vertices required")
    points = {tuple(edge): i for i, edge in
              enumerate(model["left_labels"])}
    lines = {tuple(edge): j for j, edge in
             enumerate(model["right_labels"])}
    incidences = set(model["incidences"])
    x, y = divmod(u, a)
    xx, yy = divmod(v, a)
    common = 0
    for z in range(a):
        if z == x or z == xx:
            continue
        p1 = points.get(tuple(sorted((x, z))))
        p2 = points.get(tuple(sorted((xx, z))))
        if p1 is None or p2 is None:
            continue
        for t in range(a):
            if t == y or t == yy:
                continue
            l1 = lines.get(tuple(sorted((y, t))))
            l2 = lines.get(tuple(sorted((yy, t))))
            if l1 is not None and l2 is not None:
                common += ((p1, l1) in incidences and
                           (p2, l2) in incidences)
    return common


def report():
    out = {"slice": "HYP-105-B3.2-E1-K3-AB",
           "branch_A_or_B_decided": False,
           "uniform_book_control_proved": False,
           "models": {}}
    for power, scheme, seed in ((1, "lex", None),
                                (1, "reverse-line", None),
                                (2, "random", 20261011)):
        model = gq_pair_model(power, scheme, seed)
        graph = kikuchi_graph(model)
        key = "s%s-%s" % (model["s"], scheme)
        out["models"][key] = [
            localized_certificate(graph, "all"),
            localized_certificate(graph, "active"),
            localized_certificate(graph, "endpoint-codegree", 0),
            localized_certificate(graph, "internal-load", 2),
        ]
    for t in (3, 7):
        graph = book_graph(t)
        result = localized_certificate(graph, "endpoint-codegree", 0)
        if result["all_Theta"] != 4 * t * (t - 1) * (t - 2):
            raise AssertionError("book counterexample checksum")
        if result["selected_P3"] != result["all_P3"]:
            raise AssertionError("book filter unexpectedly dropped paths")
        out["models"]["K2,%s" % t] = result
    return out


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
