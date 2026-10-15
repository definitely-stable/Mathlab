"""HYP-105 #230 / AA4-R — TRUE original GQ, globally coherent seven-GF5 mixed-swap certificate.

All-h exact identities: one-sided transpositions are supported only on
original six-incidence sets touching the changed source factor; mixed
point/line finite differences only on sets touching BOTH changed types.
These identities give no all-h positive minimum by themselves.
"""
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index, independent_joint_classify,
    strict_true_W32_model,
)

PROFILES = {(1, 1, 1, 1, 1, 1): "A",
            (2, 1, 1, 1, 1): "B", (2, 2, 2): "C"}


def strict_true_W32_gq_model(model):
    """Fail closed on the full GQ point-line axiom, not just no original C4.

    W32 is order (2,2): each of 15 points is on 3 of 15 lines;
    for each nonincident point p and line ell exactly one point on ell
    is collinear with p. This rejects source C6 configurations.
    """
    inc, left, right = strict_true_W32_model(model)
    point_lines = [set() for _ in range(15)]
    line_points = [set() for _ in range(15)]
    for p, ell in inc:
        point_lines[p].add(ell)
        line_points[ell].add(p)
    for p in range(15):
        for ell in range(15):
            if ell in point_lines[p]:
                continue
            anchors = sum(bool(point_lines[p] & point_lines[q])
                          for q in line_points[ell])
            if anchors != 1:
                raise ValueError("not a true ORIGINAL W(3,2): GQ unique anchor axiom fails")
    return inc, left, right


def _kind_on_source_half(Q, inc, labels, side):
    source = [inc[i][side] for i in Q]
    degree = Counter(c for a in source for c in labels[a])
    if len(degree) != 6 or any(n != 2 for n in degree.values()):
        return None
    profile = tuple(sorted(Counter(source).values(), reverse=True))
    kind = PROFILES.get(profile)
    if kind is None:
        raise AssertionError("2-regular half has impossible original-source profile")
    return kind


def accepted_on_fixed_right(model, right_index=None):
    """Independent one-sided right enumerator; classify left directly.

    Does NOT generate left candidates or invoke historical seven_census.
    Every selected ORIGINAL sixset must occur in the fixed genuine
    source-L/right physical projection index.
    """
    inc, f, g = strict_true_W32_gq_model(model)
    if right_index is None:
        right_index = exact_ONE_side_original_projection_index(
            model, 1)["candidate_sixset_map"]
    tags = {}
    for Q, rk in right_index.items():
        pk = _kind_on_source_half(Q, inc, f, 0)
        if pk is None:
            continue
        tag = independent_joint_classify(Q, pk, rk, inc, f, g)
        if tag is not None:
            tags[Q] = tag
    return tags


def _swap(labels, uv):
    if len(uv) != 2 or len(set(uv)) != 2:
        raise ValueError("two different source factor IDs required")
    u, v = uv
    if any(type(x) is not int or not 0 <= x < len(labels) for x in uv):
        raise ValueError("source factor ID out of range")
    result = list(labels)
    result[u], result[v] = result[v], result[u]
    return tuple(result)


def _counts(tags):
    t = Counter(tags.values())
    return {key: t[key] for key in R3_CERTIFIED_FLOORS}


def _numerator(tags):
    return sum(R3_CERTIFIED_FLOORS[tag] for tag in tags.values())


def all_h_two_type_support_ceiling(incidences, point_swap, line_swap):
    """Rigorous combinatorial ceiling for the mixed finite-difference support.

    If N genuine original incidence IDs exist, U is the set incident to
    either changed point and V to either changed line. Every sixset Q
    touching both contains a pair (e in U, j in V); e=j is possible.
    Union bound: r*C(N-1,5)+(len(U)*len(V)-r)*C(N-2,4).
    In a genuine GQ r<=3: two points cannot share two original lines.
    """
    inc = tuple(incidences)
    if len(inc) != len(set(inc)) or len(inc) < 6:
        raise ValueError("six or more distinct ORIGINAL incidence IDs required")
    if len(set(point_swap)) != 2 or len(set(line_swap)) != 2:
        raise ValueError("distinct source swaps required")
    U = {i for i, (p, _) in enumerate(inc) if p in point_swap}
    V = {i for i, (_, l) in enumerate(inc) if l in line_swap}
    r = len(U & V)
    ceiling = min(comb(len(inc), 6),
                  r*comb(len(inc)-1, 5) +
                  (len(U)*len(V)-r)*comb(len(inc)-2, 4))
    return {"N": len(inc), "point_incidence_support": len(U),
            "line_incidence_support": len(V),
            "shared_original_incidence_ids": r,
            "mixed_original_sixset_ceiling": ceiling,
            "GQ_no_C4_r_at_most_three": r <= 3}


def exact_W32_joint_mixed_swap_certificate(model, point_swap, line_swap):
    """Four REAL complete-global-injection maps, seven classes and GF5 weights.

    No fictitious independently relabeled Q and no local pseudo-maps.
    """
    inc, f, g = strict_true_W32_gq_model(model)
    fp = _swap(f, point_swap)
    gp = _swap(g, line_swap)
    base = {**model, "left_labels": f, "right_labels": g}
    pchange = {**base, "left_labels": fp}
    lchange = {**base, "right_labels": gp}
    both = {**pchange, "right_labels": gp}
    idx0 = exact_ONE_side_original_projection_index(base, 1)["candidate_sixset_map"]
    idx1 = exact_ONE_side_original_projection_index(lchange, 1)["candidate_sixset_map"]
    t00 = accepted_on_fixed_right(base, idx0)
    t10 = accepted_on_fixed_right(pchange, idx0)
    t01 = accepted_on_fixed_right(lchange, idx1)
    t11 = accepted_on_fixed_right(both, idx1)
    tables = (t00, t10, t01, t11)
    count = tuple(len(t) for t in tables)
    weighted = tuple(_numerator(t) for t in tables)
    mix = count[3]-count[1]-count[2]+count[0]
    wm = weighted[3]-weighted[1]-weighted[2]+weighted[0]
    U = {i for i, (p, _) in enumerate(inc) if p in point_swap}
    V = {i for i, (_, l) in enumerate(inc) if l in line_swap}
    allQ = set().union(*(t.keys() for t in tables))
    touched_point = lambda Q: not U.isdisjoint(Q)
    touched_line = lambda Q: not V.isdisjoint(Q)
    if any(t00.get(Q) != t10.get(Q) for Q in allQ if not touched_point(Q)):
        raise AssertionError("point swap changed a sixset avoiding both point factors")
    if any(t00.get(Q) != t01.get(Q) for Q in allQ if not touched_line(Q)):
        raise AssertionError("line swap changed a sixset avoiding both line factors")
    mixed_support = {
        Q for Q in allQ
        if touched_point(Q) and touched_line(Q)
    }
    def e(t, Q):
        return int(Q in t)
    localized_mix = sum(
        e(t11,Q)-e(t10,Q)-e(t01,Q)+e(t00,Q)
        for Q in mixed_support)
    localized_weight = sum(
        sum((1 if t.get(Q)==tag else 0)*mult*sgn
            for t,sgn in ((t11,1),(t10,-1),(t01,-1),(t00,1))
            for tag,mult in R3_CERTIFIED_FLOORS.items())
        for Q in mixed_support)
    if localized_mix != mix or localized_weight != wm:
        raise AssertionError("mixed swap residual escaped true ORIGINAL joint support")
    bound = all_h_two_type_support_ceiling(inc, point_swap, line_swap)
    if not bound["GQ_no_C4_r_at_most_three"]:
        raise AssertionError("true original GQ no-C4 source bound violated")
    if len(mixed_support) > bound["mixed_original_sixset_ceiling"]:
        raise AssertionError("mixed support violates rigorous all-h ceiling")
    k00,k10,k01,k11 = map(_counts,tables)
    per_tag = {tag: k11[tag]-k10[tag]-k01[tag]+k00[tag]
               for tag in R3_CERTIFIED_FLOORS}
    if sum(per_tag.values()) != mix:
        raise AssertionError("seven-class mixed decomposition failed")
    return {
        "scope": "TRUE W32 same ORIGINAL incidence IDs and FOUR coherent full injected maps",
        "point_swap": list(point_swap), "line_swap": list(line_swap),
        "seven_S_00_10_01_11": list(count),
        "certified_GF5_numerator_00_10_01_11": list(weighted),
        "left_delta":count[1]-count[0], "right_delta":count[2]-count[0],
        "genuine_two_type_mixed_delta":mix,
        "certified_GF5_mixed_numerator":wm,
        "mixed_delta_by_each_of_7_GF5_classes":per_tag,
        "original_sixsets_in_mixed_support":len(mixed_support),
        "original_gq_combinatorial_ceiling":bound,
        "all_h_exact_two_type_swap_support_theorem":True,
        "full_all_h_global_S_lower_PROVED":False,
        "branch_B_infinite_counterfamily_PROVED":False,
    }


if __name__ == "__main__":
    import argparse, json
    from hyp105_issue230_projection import fixture
    p = argparse.ArgumentParser()
    p.add_argument("--scheme", choices=("lex","reverse","S68","S72"), default="S68")
    p.add_argument("--point", type=int, nargs=2, default=[0,1])
    p.add_argument("--line", type=int, nargs=2, default=[0,1])
    opts = p.parse_args()
    print(json.dumps(exact_W32_joint_mixed_swap_certificate(
        fixture(1,opts.scheme), opts.point, opts.line), indent=2, sort_keys=True))
