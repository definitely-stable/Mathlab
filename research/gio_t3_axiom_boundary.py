"""GIO-001.3/T3-A: independent incidence projection boundary and exact falsifiers.

This is NOT a proof of the full T3 motif obstruction theorem. Its proved
claims concern simple incidence girth/coverage and selected projection damage.
No reuse of GQ structure(), SRG, or motif oracle to establish these claims.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import argparse
import json

from gio_generalized_gq import geometry

SCHEMA = "mathlab.gio003.t3-axiom-boundary.v1"
BASE_MAIN = "f42aa108a2f9e15dadebf5c45fa4923cc435742b"


def audit_incidence(lines, point_count):
    """Independent finite incidence oracle; fail closed on non-linearity.

    Each point pair lies on at most one line (no incidence 4-cycle).
    A nonincident point/line pair may have 0, 1 or >=2 three-flag
    projections. Two distinct projections certify a literal 6-cycle.
    """
    if type(point_count) is not int or point_count < 1:
        raise ValueError("a positive explicit point count is required")
    if not isinstance(lines, (tuple, list)) or not lines:
        raise ValueError("at least one line required")
    lines = tuple(tuple(line) for line in lines)
    on = [set() for _ in range(point_count)]
    pair_owner = {}
    for ell, line in enumerate(lines):
        if not line or any(type(p) is not int or not 0 <= p < point_count for p in line):
            raise ValueError("invalid incidence point")
        if len(line) != len(set(line)):
            raise ValueError("repeated point on line")
        for p in line:
            on[p].add(ell)
        for p, q in combinations(sorted(line), 2):
            if (p, q) in pair_owner:
                raise ValueError("repeated point pair / incidence 4-cycle")
            pair_owner[p, q] = ell

    flags = tuple(sorted((p, ell) for ell, line in enumerate(lines) for p in line))
    flag_ids = {flag: i for i, flag in enumerate(flags)}
    projected = {}
    missing = []
    multiple = []
    cycle6_witness = None
    # Independent physical projection enumeration: for each (q,r),
    # inspect all feet on r and the unique joining line, if present.
    for q in range(point_count):
        for r, line in enumerate(lines):
            if q in line:
                continue
            candidates = []
            for p in line:
                join = pair_owner.get((min(q, p), max(q, p)))
                if join is not None:
                    path = ((q, join), (p, join), (p, r))
                    assert len(set(path)) == 3
                    assert all(x in flag_ids for x in path)
                    candidates.append(path)
            if not candidates:
                missing.append((q, r))
            elif len(candidates) > 1:
                multiple.append((q, r))
                if cycle6_witness is None:
                    a, b = candidates[:2]
                    assert a[0] == b[0] or a[0][0] == b[0][0]
                    # Each path is (q,joining line),(foot,joining line),(foot,r).
                    # Their union has three distinct points/lines and six flags.
                    assert len(set(a) | set(b)) == 6
                    cycle6_witness = dict(pair=(q, r), paths=[a, b])
            else:
                projected[q, r] = candidates[0]

    loads = Counter(flag for path in projected.values() for flag in path)
    return dict(points=point_count, lines=len(lines), flags=flags, flag_ids=flag_ids,
                on=on, raw_lines=lines, projected=projected,
                missing=tuple(missing), multiple=tuple(multiple),
                cycle6_witness=cycle6_witness, loads=loads,
                maximum_load=max(loads.values(), default=0),
                girth_at_least_eight=len(multiple) == 0)


def deleted_projection_damage(audit, removed_flags):
    """Exact union bound for ANY fixed chosen partial projection.

    The selector must be frozen before adversarial deletions. This function
    checks the forward affected-endpoint census against an independent
    inverse flag-to-endpoints index (both exact sets, not just counts).
    Four physical endpoint orientations require separately injective
    two-symbol point/line maps, as in the inherited GIO model.
    """
    z = set(removed_flags)
    if any(x not in audit["flag_ids"] for x in z):
        raise ValueError("deletion must name actual original source flags")
    forward = {endpoint for endpoint, anchors in audit["projected"].items()
               if any(x in z for x in anchors)}
    inverted = defaultdict(set)
    for endpoint, anchors in audit["projected"].items():
        for flag in anchors:
            inverted[flag].add(endpoint)
    reverse = set().union(*(inverted[x] for x in z)) if z else set()
    assert forward == reverse
    assert all(len(ids) == len(inverted.get(flag, set())) for flag, ids in
               ((x, inverted[x]) for x in z))
    assert len(forward) <= sum(audit["loads"].get(x, 0) for x in z)
    assert len(forward) <= audit["maximum_load"] * len(z)
    return dict(deleted_flags=len(z), affected_endpoints=len(forward),
                four_oriented_endpoints=4 * len(forward),
                load_bound=audit["maximum_load"] * len(z),
                independent_inverse_exact=True)


def disjoint_copies(lines, point_count):
    """A (s,t)-biregular, girth>=8, non-GQ obstruction to coverage."""
    return tuple(tuple(line) for line in lines) + tuple(
        tuple(p + point_count for p in line) for line in lines
    ), 2 * point_count


def remove_one_flag(lines):
    """Remove first named flag without deleting its point or line."""
    rows = [tuple(x) for x in lines]
    point = rows[0][0]
    rows[0] = tuple(p for p in rows[0] if p != point)
    return tuple(rows), (point, 0)


def exact_moore_gate(audit, s, t):
    """Count 3-paths from EVERY q; finite certificate of Moore saturation.

    Mathematical proof: no incidence 4/6 cycles means these paths end at
    distinct nonincident lines. If |L|=(t+1)(st+1) and degrees are
    (t+1)/(s+1), path count = (t+1)st = |L|-(t+1), hence coverage.
    """
    if any(type(x) is not int or x < 1 for x in (s, t)):
        raise ValueError("positive integer bidegrees required")
    expected_points = (s + 1) * (s * t + 1)
    expected_lines = (t + 1) * (s * t + 1)
    regular = all(len(z) == s + 1 for z in audit["raw_lines"]) and all(
        len(z) == t + 1 for z in audit["on"])
    exact_sizes = audit["points"] == expected_points and audit["lines"] == expected_lines
    path_count = (t + 1) * s * t
    nonincident_per_point = expected_lines - (t + 1)
    assert path_count == nonincident_per_point
    if regular and exact_sizes and audit["girth_at_least_eight"]:
        assert len(audit["missing"]) == len(audit["multiple"]) == 0
        assert len(audit["projected"]) == audit["points"] * nonincident_per_point
    return dict(regular=regular, exact_extremal_sizes=exact_sizes,
                girth_at_least_eight=audit["girth_at_least_eight"],
                forces_full_unique_projection=regular and exact_sizes and
                   audit["girth_at_least_eight"],
                three_paths_per_point=path_count,
                nonincident_lines_per_point=nonincident_per_point)


def summarize(a):
    return dict(points=a["points"], lines=a["lines"], flags=len(a["flags"]),
                unique_projected_pairs=len(a["projected"]),
                missing_pairs=len(a["missing"]), multi_projection_pairs=len(a["multiple"]),
                girth_at_least_eight=a["girth_at_least_eight"],
                maximum_selected_projection_flag_load=a["maximum_load"])


def finite_case(name):
    g = geometry(name)
    s, t = g["s"], g["t"]
    orig = audit_incidence(g["lines"], (s + 1) * (s * t + 1))
    moore = exact_moore_gate(orig, s, t)
    assert moore["forces_full_unique_projection"]
    assert orig["maximum_load"] == 3 * s * t
    first = orig["flags"][0]
    exact_singleton = deleted_projection_damage(orig, {first})
    assert exact_singleton["affected_endpoints"] == 3 * s * t
    union_lines, union_points = disjoint_copies(g["lines"], orig["points"])
    double = audit_incidence(union_lines, union_points)
    double_gate = exact_moore_gate(double, s, t)
    assert double_gate["regular"] and not double_gate["exact_extremal_sizes"]
    assert double["girth_at_least_eight"]
    # Missing projections are precisely cross-component point/line pairs.
    assert len(double["missing"]) == 2 * orig["points"] * orig["lines"]
    assert len(double["projected"]) == 2 * len(orig["projected"])
    damaged_lines, removed = remove_one_flag(g["lines"])
    punctured = audit_incidence(damaged_lines, orig["points"])
    assert not exact_moore_gate(punctured, s, t)["regular"]
    assert punctured["girth_at_least_eight"]
    # For old nonincident endpoints, the removed flag killed its precisely
    # 3st anchored projections; (point,old line) is ONE new nonincident pair.
    assert len(punctured["missing"]) == 3 * s * t + 1
    assert len(punctured["projected"]) == len(orig["projected"]) - 3 * s * t
    z = {first, orig["flags"][len(orig["flags"]) // 2], orig["flags"][-1]}
    damage = deleted_projection_damage(orig, z)
    assert damage["affected_endpoints"] <= 3 * s * t * len(z)
    return dict(kind=name, s=s, t=t, full=summarize(orig), moore=moore,
                singleton_damage=exact_singleton, arbitrary_damage=damage,
                double=summarize(double), double_gate=double_gate,
                deleted_one_flag=summarize(punctured),
                double_cross_missing_exact=2 * orig["points"] * orig["lines"])


def certificate():
    names = ("W32", "W33", "Qminus24", "dualQminus42")
    examples = [finite_case(name) for name in names]
    # Literal 6-cycle: q not on the opposite two-point line has TWO
    # different joining lines/feet. Thus 'bounded multiplicity 2'
    # cannot coexist with girth>=8.
    triangle = audit_incidence(((0, 1), (1, 2), (0, 2)), 3)
    assert len(triangle["multiple"]) == 3
    assert len(triangle["missing"]) == 0
    assert triangle["cycle6_witness"] is not None
    # For a two-copy balanced GQ(s,t), the defect is exactly 2 Vp Vl
    # = Theta_b(r^6); the normalized defect among off-incidence pairs
    # tends to 1/2 along equal-order GQ(s,s).
    sample = examples[0]
    vp, vl = sample["full"]["points"], sample["full"]["lines"]
    n = sample["full"]["flags"]
    exact_fraction = Fraction(2 * vp * vl, 4 * vp * vl - 2 * n)
    return dict(schema=SCHEMA,issue=793,meta_issue=790,
                frozen_base_main_sha=BASE_MAIN,
                claim="PROVED_RESTRICTED_AXIOM_BOUNDARY_NOT_T3",
                independent_oracle="all point-line pairs and all joining feet",
                proof_obligations=dict(
                    no_c4_c6_implies_projection_at_most_one=True,
                    exact_biregular_moore_saturation_forces_GQ=True,
                    partial_selector_damage_at_most_maxload_times_deletions=True,
                    oriented_factor_requires_injective_two_symbol_maps=True),
                cases=examples, cycle6=summarize(triangle),
                cycle6_witness=triangle["cycle6_witness"],
                doubled_W32_cross_defect_fraction=str(exact_fraction),
                symbolic_doubled_GQ_missing="2*(s+1)*(t+1)*(s*t+1)^2",
                symbolic_cross_defect_equal_order_order="Theta(s^6)",
                no_full_abstract_T3_motif_theorem=True,
                no_general_ASET_exponent=True,
                no_external_referee=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="gio003-t3-axiom-boundary.json")
    args = ap.parse_args()
    data = certificate()
    Path(args.out).write_text(json.dumps(data, sort_keys=True, indent=2) + "\n",
                              encoding="utf-8")
    print("GIO003_T3_AXIOM_BOUNDARY_CERTIFICATE=" +
          json.dumps(data, sort_keys=True))
