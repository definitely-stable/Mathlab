"""HYP-105 B3.2-E1-K1: Kikuchi graph, D6 = proper six-cycles, CS/Moore floor.

Exact all-h identities (proved in the K1 research note) plus finite checks:

* K1. For legal pair injections f,g of W(3,s) the level-(1,1) Kikuchi graph
  G^ on [a]x[a] has, for every incidence (p,l) with f(p)={x,x'} and
  g(l)={y,y'}, the two edges (x,y)-(x',y') and (x,y')-(x',y). It is simple
  with exactly 2N edges, and the accepted D6 family equals the number of
  PROPER six-cycles of G^ (six distinct first and six distinct second
  coordinates). Proper four-cycles are the accepted Q4 family.
* K2. sum_{u,v} P3(u,v)^2 = P3 + 12*C6(G^) + Theta with the explicit
  coincidence mass Theta computed here from codegrees only.
* K3. NB3 >= 2m_c(d_c-1)^2 on the 2-core (Alon-Hoory-Linial) and the
  peeling monotonicity give P3 >= 4N(4N/a^2-1)^2 - 6*C3.

Hence 12*D6 >= L(P3) - Theta - 12*C6_improper with L(x)=x(x/a^4-1). This is
a CONDITIONAL floor: no all-h control of Theta or of improper cycles is
claimed. No Branch A/B decision, no full GF5 R3 and no ASET exponent.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json
import random
import sys

from hyp105_b1_symplectic import exact_gq_certificate, symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_alphabet_size, unrank_pair

SUPPORTED_POWERS = (1, 2, 3)
SCHEMES = ("lex", "reverse-line", "random")


def labeled_model(s, a, incidences, left, right, scheme="custom"):
    """Validated finite factor incidence with two injective pair labelings."""
    if type(s) is not int or s < 2 or type(a) is not int or a < 4:
        raise ValueError("integer s>=2 and physical alphabet a>=4 required")
    left = tuple(tuple(p) for p in left)
    right = tuple(tuple(p) for p in right)
    for labels in (left, right):
        if (len(set(labels)) != len(labels) or
                any(len(p) != 2 or type(p[0]) is not int or
                    type(p[1]) is not int or not 0 <= p[0] < p[1] < a
                    for p in labels)):
            raise ValueError("injective unordered pair labels in K_a required")
    incidences = tuple(tuple(e) for e in incidences)
    if (len(set(incidences)) != len(incidences) or
            any(len(e) != 2 or not 0 <= e[0] < len(left) or
                not 0 <= e[1] < len(right) for e in incidences)):
        raise ValueError("distinct factor incidences in range required")
    return {
        "s": s, "a": a, "v_left": len(left), "v_right": len(right),
        "N": len(incidences), "incidences": incidences,
        "left_labels": left, "right_labels": right, "scheme": scheme,
    }


def gq_pair_model(power, scheme="lex", seed=None):
    """True symplectic W(3,2^power) with explicit pair labels in K_a.

    lex and reverse-line coincide with pair_labeled_symplectic at h=1,2;
    random draws both injections from the WHOLE K_a edge set (unused host
    edges allowed) with a fixed integer seed.
    """
    if power not in SUPPORTED_POWERS:
        raise ValueError("executable Kikuchi model limited to s=2,4,8")
    if scheme not in SCHEMES:
        raise ValueError("unknown labeling scheme")
    field, points, lines, incidences = symplectic_gq(power)
    v = len(points)
    if len(lines) != v:
        raise AssertionError("GQ(s,s) must be balanced")
    a = pair_alphabet_size(v)
    palette = tuple(unrank_pair(r, a) for r in range(comb(a, 2)))
    if scheme == "lex":
        left, right = palette[:v], palette[:v]
    elif scheme == "reverse-line":
        left = palette[:v]
        right = tuple(palette[v - 1 - j] for j in range(v))
    else:
        if type(seed) is not int:
            raise ValueError("random scheme needs an explicit integer seed")
        rng = random.Random(seed)
        left = tuple(rng.sample(palette, v))
        right = tuple(rng.sample(palette, v))
    model = labeled_model(field.q, a, incidences, left, right, scheme)
    model["h"] = power
    model["seed"] = seed
    return model


def kikuchi_graph(model):
    """Level-(1,1) Kikuchi graph; vertex x*a+y encodes (x,y)."""
    a = model["a"]
    neighbors = [set() for _ in range(a * a)]
    for p, l in model["incidences"]:
        x, x2 = model["left_labels"][p]
        y, y2 = model["right_labels"][l]
        for u, w in ((x * a + y, x2 * a + y2), (x * a + y2, x2 * a + y)):
            if w in neighbors[u]:
                raise AssertionError("Kikuchi graph of an injective model is simple")
            neighbors[u].add(w)
            neighbors[w].add(u)
    if sum(map(len, neighbors)) != 4 * model["N"]:
        raise AssertionError("Kikuchi graph must have exactly 2N edges")
    return tuple(frozenset(row) for row in neighbors)


def six_cycle_census(neighbors, a, max_cycles=5_000_000):
    """Every simple six-cycle once (min start, second < last), by type."""
    counts = Counter()
    seen = 0
    for start in range(len(neighbors)):
        path = [start]
        on_path = {start}

        def walk():
            nonlocal seen
            last = path[-1]
            if len(path) == 6:
                if start in neighbors[last] and path[1] < last:
                    seen += 1
                    if seen > max_cycles:
                        raise RuntimeError("six-cycle budget exceeded (fail closed)")
                    xs = len({w // a for w in path}) == 6
                    ys = len({w % a for w in path}) == 6
                    counts[(xs, ys)] += 1
                return
            for w in neighbors[last]:
                if w > start and w not in on_path:
                    path.append(w)
                    on_path.add(w)
                    walk()
                    on_path.remove(w)
                    path.pop()

        walk()
    return {
        "C6": seen,
        "proper_D6": counts[(True, True)],
        "improper_x_repeat_only": counts[(False, True)],
        "improper_y_repeat_only": counts[(True, False)],
        "improper_both_repeat": counts[(False, False)],
        "improper_total": seen - counts[(True, True)],
    }


def proper_six_cycles_pruned(neighbors, a):
    """Fast proper-only count: prune repeated coordinates during the walk."""
    count = 0
    for start in range(len(neighbors)):
        x0, y0 = divmod(start, a)

        def walk(last, depth, xs, ys, second):
            nonlocal count
            for w in neighbors[last]:
                if w <= start:
                    if depth == 5 and w == start and second < last:
                        count += 1
                    continue
                if depth == 5:
                    continue
                xw, yw = divmod(w, a)
                if (xs >> xw) & 1 or (ys >> yw) & 1:
                    continue
                walk(w, depth + 1, xs | (1 << xw), ys | (1 << yw),
                     w if depth == 0 else second)

        walk(start, 0, 1 << x0, 1 << y0, -1)
    return count


def path3_profile(neighbors):
    """Simple 3-paths P3, sum_{u,v}P3(u,v)^2, triangles and NB3=P3+6*C3."""
    n = len(neighbors)
    per_pair = Counter()
    for u in range(n):
        for b in neighbors[u]:
            for c in neighbors[b]:
                if c == u:
                    continue
                for v in neighbors[c]:
                    if v != b and v != u:
                        per_pair[u * n + v] += 1
    p3 = sum(per_pair.values())
    triangles = sum(1 for u in range(n) for v in neighbors[u] if v > u
                    for w in neighbors[u] & neighbors[v] if w > v)
    return {
        "P3": p3,
        "sum_P3_squared": sum(c * c for c in per_pair.values()),
        "C3": triangles,
        "NB3": p3 + 6 * triangles,
    }


def codegree_profile(neighbors, a=None):
    """Codegrees of all pairs at distance <=2 and the K2 coincidence mass."""
    n = len(neighbors)
    codeg = Counter()
    for w in range(n):
        for b, c in combinations(sorted(neighbors[w]), 2):
            codeg[(b, c)] += 1
    deg = [len(row) for row in neighbors]
    c4_twice = 0
    theta_c4 = 0
    theta_diamond = 0
    for (u, v), c in codeg.items():
        pairs = comb(c, 2)
        c4_twice += pairs
        adjacent = v in neighbors[u]
        theta_c4 += 4 * pairs * (deg[u] + deg[v] - 4 - 2 * adjacent)
        if adjacent:
            theta_diamond += 2 * c * (c - 1)
    bowties = 0
    for center in range(n):
        incident = [codeg[(min(center, u), max(center, u))]
                    for u in neighbors[center]]
        t_center = sum(incident) // 2
        bowties += comb(t_center, 2) - sum(comb(t, 2) for t in incident)
    if c4_twice % 2:
        raise AssertionError("each four-cycle has exactly two diagonals")
    result = {
        "C4": c4_twice // 2,
        "Theta_C4_pendant": theta_c4,
        "Theta_diamond": theta_diamond,
        "Theta_bowtie": 16 * bowties,
        "bowties": bowties,
        "Theta": theta_c4 + theta_diamond + 16 * bowties,
        "max_codegree": max(codeg.values(), default=0),
        "M2": sum(d * d for d in deg),
        "M3": sum(d ** 3 for d in deg),
        "max_degree": max(deg),
    }
    if a is not None:
        proper_twice = 0
        for (u, v), c in codeg.items():
            if c < 2:
                continue
            common = sorted(neighbors[u] & neighbors[v])
            for b, d in combinations(common, 2):
                cyc = (u, b, v, d)
                if (len({w // a for w in cyc}) == 4 and
                        len({w % a for w in cyc}) == 4):
                    proper_twice += 1
        if proper_twice % 2:
            raise AssertionError("proper four-cycles also have two diagonals")
        result["proper_C4_Q4"] = proper_twice // 2
    return result


def two_core(neighbors):
    """Peel vertices of degree <=1; return core size, edges, average degree."""
    alive = [bool(row) for row in neighbors]
    deg = [len(row) for row in neighbors]
    stack = [v for v in range(len(neighbors)) if alive[v] and deg[v] <= 1]
    while stack:
        v = stack.pop()
        if not alive[v]:
            continue
        alive[v] = False
        for w in neighbors[v]:
            if alive[w]:
                deg[w] -= 1
                if deg[w] <= 1:
                    stack.append(w)
    n_core = sum(alive)
    m_core = sum(deg[v] for v in range(len(neighbors)) if alive[v]) // 2
    return n_core, m_core


def ahl_nb3_lower(neighbors):
    """Alon-Hoory-Linial lower 2m(d-1)^2 for NB3 on the 2-core (exact)."""
    n_core, m_core = two_core(neighbors)
    if n_core == 0:
        return Fraction(0)
    d = Fraction(2 * m_core, n_core)
    if d < 2:
        return Fraction(0)
    return 2 * m_core * (d - 1) ** 2


def a_priori_p3_floor(N, a):
    """4N(4N/a^2-1)^2 = 2m(dbar-1)^2 with m=2N and dbar over all a^2 vertices."""
    d = Fraction(4 * N, a * a)
    if d < 3:
        raise ValueError("peeling monotonicity proved only for average degree >=3")
    return 4 * N * (d - 1) ** 2


def cs_floor(p3, a):
    """L(x)=x(x/a^4-1), the Cauchy-Schwarz value for sum P3(u,v)^2 - P3."""
    return Fraction(p3) * (Fraction(p3, a ** 4) - 1)


def gq_parameters(s):
    v = (s + 1) * (s * s + 1)
    a = pair_alphabet_size(v)
    return v, (s + 1) * v, a


def a_priori_table(powers=range(1, 7)):
    """Exact mu0 and the a-priori leading term L(P3_0)/(12 s^6) per s=2^h."""
    rows = []
    for h in powers:
        s = 1 << h
        v, N, a = gq_parameters(s)
        p30 = a_priori_p3_floor(N, a)
        rows.append({
            "s": s, "V": v, "N": N, "a": a, "K_minus_V": comb(a, 2) - v,
            "dbar": float(Fraction(4 * N, a * a)),
            "edges_over_n_4_3": float(2 * N / (a * a) ** (4 / 3)),
            "mu0": float(p30 / a ** 4),
            "leading_D6_term_over_s6": float(cs_floor(p30, a) / 12 / s ** 6),
        })
    return rows


def kikuchi_statistics(model, *, cycles=True, max_cycles=5_000_000):
    """All K1/K2/K3 quantities for one labeled model."""
    a = model["a"]
    neighbors = kikuchi_graph(model)
    paths = path3_profile(neighbors)
    cod = codegree_profile(neighbors, a)
    ahl = ahl_nb3_lower(neighbors)
    if paths["NB3"] < ahl:
        raise AssertionError("Alon-Hoory-Linial NB3 lower violated")
    p30 = a_priori_p3_floor(model["N"], a)
    if ahl < p30:
        raise AssertionError("2-core peeling monotonicity violated")
    if paths["P3"] < p30 - 6 * paths["C3"]:
        raise AssertionError("a-priori P3 floor violated")
    out = {
        "s": model["s"], "a": a, "scheme": model["scheme"],
        "seed": model.get("seed"), "N": model["N"],
        "kikuchi_vertices": a * a,
        "kikuchi_edges": 2 * model["N"],
        "P3": paths["P3"], "sum_P3_squared": paths["sum_P3_squared"],
        "C3": paths["C3"], "NB3": paths["NB3"],
        "mu": str(Fraction(paths["P3"], a ** 4)),
        "AHL_NB3_lower": str(ahl),
        "a_priori_P3_floor": str(p30 - 6 * paths["C3"]),
        **cod,
    }
    if cycles:
        census = six_cycle_census(neighbors, a, max_cycles)
        identity = (paths["P3"] + 12 * census["C6"] + cod["Theta"])
        if identity != paths["sum_P3_squared"]:
            raise AssertionError("exact K2 identity failed")
        floor_value = (cs_floor(paths["P3"], a) - cod["Theta"]
                       - 12 * census["improper_total"])
        if 12 * census["proper_D6"] < floor_value:
            raise AssertionError("conditional D6 floor violated")
        a_priori = (cs_floor(max(p30 - 6 * paths["C3"], Fraction(a ** 4, 2)), a)
                    - cod["Theta"] - 12 * census["improper_total"])
        out.update(census)
        out["K2_identity_verified"] = True
        out["conditional_D6_floor"] = str(floor_value / 12)
        out["a_priori_conditional_D6_floor"] = str(a_priori / 12)
        out["D6_over_s6"] = float(Fraction(census["proper_D6"], model["s"] ** 6))
    return out


def greedy_d6_adversary(model, moves, seed):
    """Report-only deterministic greedy descent of the exact proper-C6 count.

    Moves: swap two labels on one side, or move one label to an unused K_a
    edge. A move is kept iff D6 does not increase. Finite evidence only.
    """
    if type(moves) is not int or moves < 0 or type(seed) is not int:
        raise ValueError("integer move budget and seed required")
    a = model["a"]
    palette = tuple(unrank_pair(r, a) for r in range(comb(a, 2)))
    left = list(model["left_labels"])
    right = list(model["right_labels"])
    free = {"L": [p for p in palette if p not in set(left)],
            "R": [p for p in palette if p not in set(right)]}

    def score():
        trial = labeled_model(model["s"], a, model["incidences"], left, right)
        return proper_six_cycles_pruned(kikuchi_graph(trial), a)

    rng = random.Random(seed)
    current = start = score()
    for _ in range(moves):
        side = "L" if rng.random() < 0.5 else "R"
        labels = left if side == "L" else right
        if free[side] and rng.random() < 0.15:
            i = rng.randrange(len(labels))
            j = rng.randrange(len(free[side]))
            labels[i], free[side][j] = free[side][j], labels[i]
            undo = ("free", i, j)
        else:
            i, j = rng.sample(range(len(labels)), 2)
            labels[i], labels[j] = labels[j], labels[i]
            undo = ("swap", i, j)
        new = score()
        if new <= current:
            current = new
        elif undo[0] == "free":
            labels[undo[1]], free[side][undo[2]] = free[side][undo[2]], labels[undo[1]]
        else:
            labels[undo[1]], labels[undo[2]] = labels[undo[2]], labels[undo[1]]
    final = labeled_model(model["s"], a, model["incidences"], left, right,
                          "greedy-from-" + model["scheme"])
    return {"start_D6": start, "final_D6": current, "moves": moves,
            "seed": seed, "final_model": final}


def report(include_s8_cycles=False, adversary_moves=0):
    out = {
        "slice": "HYP-105-B3.2-E1-K1",
        "gq_certificates": [exact_gq_certificate(h) for h in SUPPORTED_POWERS],
        "a_priori_table": a_priori_table(),
        "models": [],
    }
    for power, scheme, seed in ((1, "lex", None), (1, "reverse-line", None),
                                (2, "lex", None), (2, "random", 20261011)):
        out["models"].append(kikuchi_statistics(gq_pair_model(power, scheme, seed)))
    out["models"].append(kikuchi_statistics(gq_pair_model(3, "lex"),
                                            cycles=include_s8_cycles))
    if adversary_moves:
        start = gq_pair_model(2, "random", 11)
        run = greedy_d6_adversary(start, adversary_moves, 11)
        final = kikuchi_statistics(run["final_model"])
        out["s4_greedy_adversary"] = {
            "start_D6": run["start_D6"], "final_D6": run["final_D6"],
            "moves": adversary_moves, "seed": 11, "final_statistics": final,
        }
    out.update({
        "all_h_exact_identities": ["K1 D6=proper C6", "K2 CS identity",
                                   "K3 AHL/peeling floor"],
        "conditional_only": True,
        "coincidence_mass_lemma_proved": False,
        "branch_A_or_B_decided": False,
        "full_R3_or_ASET_exponent": False,
    })
    return out


if __name__ == "__main__":
    moves = int(sys.argv[sys.argv.index("--adversary") + 1]) if "--adversary" in sys.argv else 0
    print(json.dumps(report("--s8-cycles" in sys.argv, moves), indent=2,
                     sort_keys=True, default=str))
