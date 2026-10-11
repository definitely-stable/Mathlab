"""HYP-105 C24-B2: exact original-W(3,2) joint seven-family finite audit.

Two source orientations and independently coded classifiers. A common globally
coherent ORIGINAL left f and ORIGINAL right g for every actual six-incidence set.
105 one-right-transposition neighbors only, NOT full 15! or an all-h minimum.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product

from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, original_W32, degree_two_on_six_coordinates)
from hyp105_g5e2b3e1c24b_three_collision import (
    W32_LEFT_H45, W32_RIGHT_H45_ZERO,
    right_C_source_with_left_f, exact_collision_decomposition)

TAGS = ("D6", "B-left/A-right", "A-left/B-right", "C/A", "C/B",
        "B/B-overlap", "B/B-disjoint")
GF5_WEIGHTS = (5643, 45600, 45600, 43320, 49050, 51750, 45010)
A, B, C = (1, 1, 1, 1, 1, 1), (2, 1, 1, 1, 1), (2, 2, 2)
COLUMN_PAIRS = tuple(combinations(range(6), 2))
BITS = tuple((1 << x) | (1 << y) for x, y in K6_PAIRS)


def full_permutation(perm):
    if (len(perm) != 15 or any(type(i) is not int for i in perm)
            or set(perm) != set(range(15))):
        raise ValueError("one complete original W32 global K6 pair injection required")
    return tuple(perm)


def dual(edges):
    return tuple((i, j) for i, j in COLUMN_PAIRS
                 if bool(set(edges[i]) & set(edges[j])))


def connected(s):
    graph = [set() for _ in range(6)]
    for i, j in s:
        graph[i].add(j)
        graph[j].add(i)
    if len(s) != 6 or any(len(row) != 2 for row in graph):
        return False
    seen, stack = {0}, [0]
    while stack:
        for j in graph[stack.pop()]:
            if j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == 6


def static_schema(six, f):
    pts, lines = tuple(p for p, _ in six), tuple(l for _, l in six)
    lc, rc = Counter(pts), Counter(lines)
    lp = tuple(sorted(lc.values(), reverse=True))
    rp = tuple(sorted(rc.values(), reverse=True))
    if rp not in (A, B, C):
        return None
    if lp == A and rp == A:
        signature = dual(tuple(K6_PAIRS[f[p - 1]] for p in pts))
        return ("D6", signature) if connected(signature) else None
    if lp == B and rp == A:
        return ("B-left/A-right", None)
    if lp == A and rp == B:
        return ("A-left/B-right", None)
    if (lp, rp) in ((A, C), (C, A)):
        return ("C/A", None)
    if (lp, rp) in ((B, C), (C, B)):
        return ("C/B", None)
    if lp == rp == B:
        p = next(p for p, n in lc.items() if n == 2)
        l = next(l for l, n in rc.items() if n == 2)
        common = sum(x == p and y == l for x, y in six)
        if common > 1:
            raise AssertionError("duplicated genuine GQ incidence")
        return ("B/B-overlap" if common else "B/B-disjoint", None)
    return None


def physical_templates():
    x = tuple(pattern for pattern in combinations_with_replacement(range(15), 6)
              if degree_two_on_six_coordinates(K6_PAIRS[i] for i in pattern))
    if len(x) != 130:
        raise AssertionError("physical K6 two-factor multiset count changed")
    return x


@lru_cache(maxsize=3)
def compile_left(left_f=W32_LEFT_H45):
    f = full_permutation(left_f)
    _, lines, _ = original_W32()
    incident = {p: tuple(i for i, line in enumerate(lines) if p in line)
                for p in range(1, 16)}
    inverse = {edge: i + 1 for i, edge in enumerate(f)}
    grouped, left_types, seen = Counter(), Counter(), set()
    for pattern in physical_templates():
        counts = Counter(pattern)
        groups = tuple(sorted((inverse[e], n) for e, n in counts.items()))
        left_types[tuple(sorted(counts.values(), reverse=True))] += 1
        choices = [tuple(combinations(incident[p], n)) for p, n in groups]
        for pick in product(*choices):
            six = tuple(sorted((p, l) for (p, _), selected in zip(groups, pick)
                               for l in selected))
            if six in seen:
                raise AssertionError("left source contains duplicate original sixset")
            seen.add(six)
            tag = static_schema(six, f)
            if tag is not None:
                name, sig = tag
                grouped[(name, tuple(l for _, l in six), sig)] += 1
    if (len(seen) != 62370 or
            left_types != Counter({A: 70, B: 45, C: 15})):
        raise AssertionError("true GQ full left 62,370 source incomplete")
    records = tuple((tag, ls, sig, count)
                    for (tag, ls, sig), count in grouped.items())
    by_line = tuple(frozenset(k for k, r in enumerate(records) if l in r[1])
                    for l in range(15))
    return {"f": f, "left_source_size": len(seen),
            "static_eligible": sum(grouped.values()),
            "compressed_records": len(records),
            "records": records, "by_line": by_line}


def right_masks(g):
    return tuple(BITS[i] for i in full_permutation(g))


def accepted(record, masks):
    name, lines, sig, _ = record
    es = tuple(masks[l] for l in lines)
    unions, parity = 0, 0
    for e in es:
        unions |= e
        parity ^= e
    if unions.bit_count() != 6 or parity != 0:
        return False
    if name == "D6":
        return tuple((i, j) for i, j in COLUMN_PAIRS if es[i] & es[j]) == sig
    return True


def result(counts, right_c):
    tags = {k: counts[k] for k in TAGS}
    if min(tags.values()) < 0 or right_c < 0:
        raise AssertionError("negative original motif count")
    return {"seven_counts": tags, "S_seven": sum(tags.values()),
            "Q7_necessary_numerator": sum(tags[k] * w
                                          for k, w in zip(TAGS, GF5_WEIGHTS)),
            "right_C_accepted": right_c}


def full_left_score(source, g):
    masks, scores, right_c = right_masks(g), Counter(), 0
    for rec in source["records"]:
        if accepted(rec, masks):
            scores[rec[0]] += rec[3]
            if len(set(rec[1])) == 3:
                right_c += rec[3]
    return result(scores, right_c)


def reference_classifier(six, f, g):
    """Independent physical endpoint/column-dual classifier, no static schema."""
    pts, ls = [p for p, _ in six], [l for _, l in six]
    L = [K6_PAIRS[f[p - 1]] for p in pts]
    R = [K6_PAIRS[g[l]] for l in ls]
    if not degree_two_on_six_coordinates(L) or not degree_two_on_six_coordinates(R):
        return None
    pc, lc = Counter(pts), Counter(ls)
    pt, lt = sorted(pc.values(), reverse=True), sorted(lc.values(), reverse=True)
    if pt == lt == [1] * 6:
        def coordinate_dual(edges):
            x = {}
            for i, e in enumerate(edges):
                for v in e:
                    x.setdefault(v, []).append(i)
            return frozenset(frozenset(v) for v in x.values())
        left, right = coordinate_dual(L), coordinate_dual(R)
        if left != right or len(left) != 6:
            return None
        adjacency = [set() for _ in range(6)]
        for e in left:
            a, b = tuple(e)
            adjacency[a].add(b)
            adjacency[b].add(a)
        seen, stack = {0}, [0]
        while stack:
            for node in adjacency[stack.pop()]:
                if node not in seen:
                    seen.add(node)
                    stack.append(node)
        return "D6" if len(seen) == 6 else None
    if pt == [2, 1, 1, 1, 1] and lt == [1] * 6:
        return "B-left/A-right"
    if pt == [1] * 6 and lt == [2, 1, 1, 1, 1]:
        return "A-left/B-right"
    if (pt == [2, 2, 2] and lt == [1] * 6 or
            lt == [2, 2, 2] and pt == [1] * 6):
        return "C/A"
    if (pt == [2, 2, 2] and lt == [2, 1, 1, 1, 1] or
            lt == [2, 2, 2] and pt == [2, 1, 1, 1, 1]):
        return "C/B"
    if pt == lt == [2, 1, 1, 1, 1]:
        p = next(p for p, n in pc.items() if n == 2)
        l = next(l for l, n in lc.items() if n == 2)
        return "B/B-overlap" if (p, l) in six else "B/B-disjoint"
    return None


def right_first_independent(f, g):
    """Completely separate right-first 62,370 ORIGINAL incidence enumerator."""
    f, g = full_permutation(f), full_permutation(g)
    _, lines, _ = original_W32()
    line_of_edge = {edge: l for l, edge in enumerate(g)}
    scores, seen, right_c = Counter(), set(), 0
    for pattern in physical_templates():
        groups = tuple(sorted((line_of_edge[e], n)
                              for e, n in Counter(pattern).items()))
        choices = [tuple(combinations(lines[l], n)) for l, n in groups]
        for pick in product(*choices):
            six = tuple(sorted((p, l) for (l, _), pts in zip(groups, pick)
                               for p in pts))
            if six in seen:
                raise AssertionError("right-first duplicate original sixset")
            seen.add(six)
            tag = reference_classifier(six, f, g)
            if tag:
                scores[tag] += 1
                if len({l for _, l in six}) == 3:
                    right_c += 1
    if len(seen) != 62370:
        raise AssertionError("incomplete right-first original source")
    return {"right_source_size": len(seen), **result(scores, right_c)}


def right_swap_105(source, baseline=W32_RIGHT_H45_ZERO):
    """One globally consistent g per swap; exact sparse affected-fiber updates."""
    baseline = full_permutation(baseline)
    records, refs = source["records"], source["by_line"]
    old_masks = right_masks(baseline)
    old = full_left_score(source, baseline)
    runs = []
    for i, j in combinations(range(15), 2):
        new = list(baseline)
        new[i], new[j] = new[j], new[i]
        masks = right_masks(new)
        counts = Counter(old["seven_counts"])
        right_c = old["right_C_accepted"]
        touched = refs[i] | refs[j]
        for rid in touched:
            rec = records[rid]
            before, after = accepted(rec, old_masks), accepted(rec, masks)
            if before != after:
                delta = rec[3] * (1 if after else -1)
                counts[rec[0]] += delta
                if len(set(rec[1])) == 3:
                    right_c += delta
        row = result(counts, right_c)
        row["swap"] = (i, j)
        row["touched_records"] = len(touched)
        runs.append(row)
    if len(runs) != 105:
        raise AssertionError("right swaps incomplete")
    choose = lambda cases, key: min(cases, key=lambda x: (x[key], x["swap"]))
    zero = [r for r in runs if r["right_C_accepted"] == 0]
    return {"baseline": old, "swaps": runs,
            "min_S": choose(runs, "S_seven"),
            "min_Q7": choose(runs, "Q7_necessary_numerator"),
            "min_S_given_C_zero": choose(zero, "S_seven"),
            "C_histogram": dict(sorted(Counter(r["right_C_accepted"] for r in runs).items())),
            "D6_histogram": dict(sorted(Counter(r["seven_counts"]["D6"] for r in runs).items())),
            "number_of_swaps": len(runs),
            "C_zero_neighbors": len(zero)}


def report():
    src = compile_left()
    first = full_left_score(src, W32_RIGHT_H45_ZERO)
    second = right_first_independent(W32_LEFT_H45, W32_RIGHT_H45_ZERO)
    if first["seven_counts"] != second["seven_counts"]:
        raise AssertionError("left-first/right-first seven classifiers disagree")
    triple = right_C_source_with_left_f(W32_LEFT_H45)
    c = exact_collision_decomposition(triple, W32_RIGHT_H45_ZERO, K6_PAIRS)
    if first["right_C_accepted"] != c["accepted_right_C"]:
        raise AssertionError("right C-only != full-seven right C projection")
    neighborhood = right_swap_105(src)
    return {"left_source": src["left_source_size"],
            "static_eligible": src["static_eligible"],
            "compressed_records": src["compressed_records"],
            "baseline": first, "independent_right_source": second["right_source_size"],
            "one_global_right_105": {k: v for k, v in neighborhood.items() if k != "swaps"},
            "no_global_15_factorial_or_all_h_minimum_claim": True}


if __name__ == "__main__":
    import json
    print(json.dumps(report(), indent=2, sort_keys=True))
