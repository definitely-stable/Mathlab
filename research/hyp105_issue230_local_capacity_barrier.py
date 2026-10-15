"""Exact falsifier for a LOCAL five-source capacity claim, not issue 230 A/B.

The symbolic construction works for every s=2^h >= 8 with t=s.
Finite geometry execution below checks s=4,t=2 and s=8,t=8.
The theorem concerns a local source selection, not the full-model motif sum.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys

from hyp105_b1_symplectic import symplectic_gq, symplectic
from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_source_plaquettes import OriginalPlaquette


def complete_labels(v, a, prescribed):
    assert len(set(prescribed.values())) == len(prescribed)
    unused = iter(e for e in combinations(range(a), 2)
                  if e not in set(prescribed.values()))
    labels = tuple(prescribed[i] if i in prescribed else next(unused)
                   for i in range(v))
    assert len(set(labels)) == v
    assert all(0 <= x < y < a for x, y in labels)
    return labels


def construct(power, t):
    field, points, lines, incidence = symplectic_gq(power)
    s, v = field.q, len(points)
    a = parameters(s)["a"]
    assert t <= s and 2 + 4*t <= a
    line_sets = tuple(set(row) for row in lines)
    point_lines = [set() for _ in points]
    for p, l in incidence:
        point_lines[p].add(l)

    # Source anchors are pairwise noncollinear. Regularity guarantees
    # a greedy independent set of at least s+1 points (proof in notes).
    anchors, forbidden = [], set()
    for _ in range(t):
        c = next(p for p in range(v) if p not in forbidden)
        anchors.append(c)
        forbidden.add(c)
        for l in point_lines[c]:
            forbidden.update(line_sets[l])

    # For a point off a source line, exactly one incident line meets it.
    # At step i<t<=s, fewer than s lines are forbidden.
    anchor_lines, used_points = [], set()
    for c in anchors:
        l = next(l for l in sorted(point_lines[c])
                 if not line_sets[l].intersection(used_points))
        anchor_lines.append(l)
        used_points.update(line_sets[l])

    q_grid = [sorted(line_sets[l] - {c})[:t]
              for c, l in zip(anchors, anchor_lines)]
    r_grid = [sorted(point_lines[c] - {l})[:t]
              for c, l in zip(anchors, anchor_lines)]
    reserved_p = set(anchors).union(*(set(row) for row in q_grid))
    reserved_l = set(anchor_lines).union(*(set(row) for row in r_grid))
    assert len(reserved_p) == len(reserved_l) == t*t+t
    excluded_p, excluded_l = set(reserved_p), set(reserved_l)
    source_matching = []
    for _ in range(2*t+1):
        p, l = next(e for e in incidence
                    if e[0] not in excluded_p and e[1] not in excluded_l)
        source_matching.append((p, l))
        excluded_p.add(p)
        excluded_l.add(l)

    left, right = {}, {}
    def assign(table, object_id, pair):
        assert object_id not in table
        pair = tuple(sorted(pair))
        assert pair not in table.values()
        table[object_id] = pair
    p0, l0 = source_matching[0]
    assign(left, p0, (0, 1))
    assign(right, l0, (0, 1))
    for i in range(t):
        p, l = source_matching[1+i]
        assign(left, p, (0, 2+i))
        assign(right, l, (0, 2+i))
        p, l = source_matching[1+t+i]
        assign(left, p, (1, 2+t+i))
        assign(right, l, (1, 2+t+i))
        assign(left, anchors[i], (0, 2+2*t+i))
        assign(right, anchor_lines[i], (2+2*t+2*i, 3+2*t+2*i))
        for j in range(t):
            assign(left, q_grid[i][j], (2+i, 2+t+j))
            assign(right, r_grid[i][j], (2+i, 2+t+j))
    f, g = complete_labels(v, a, left), complete_labels(v, a, right)
    model = dict(s=s, a=a, v=v, m=2*a, N=len(incidence),
                 points=points, lines=lines, incidences=incidence,
                 left_labels=f, right_labels=g)
    edge_id = {e: i for i, e in enumerate(incidence)}
    selected = tuple(edge_id[e] for e in source_matching)
    return field, model, dict(t=t, anchors=anchors, anchor_lines=anchor_lines,
                             q_grid=q_grid, r_grid=r_grid,
                             selected=selected, source_matching=source_matching,
                             point_lines=point_lines, line_sets=line_sets)


def validate(field, model, data):
    s, a, t = model["s"], model["a"], data["t"]
    f, g = model["left_labels"], model["right_labels"]
    inc, points = model["incidences"], model["points"]
    point_lines, line_sets = data["point_lines"], data["line_sets"]
    edge_id = {e: i for i, e in enumerate(inc)}
    selected = data["selected"]
    adjacency, provenance = {}, {}
    for eid in selected:
        p, l = inc[eid]
        x, xx = f[p]
        y, yy = g[l]
        for u, v in (((x, y), (xx, yy)), ((x, yy), (xx, y))):
            edge = tuple(sorted((u, v)))
            assert edge not in provenance
            provenance[edge] = eid
            adjacency.setdefault(u, set()).add(v)
            adjacency.setdefault(v, set()).add(u)
    assert len(provenance) == 4*t+2
    assert min(map(len, adjacency.values())) == 1

    # Independent method 1: enumerate genuine original three-edge paths.
    # Independent method 2: symplectic orthogonality on the actual line.
    closed_physical_profiles = Counter()
    for i, j in product(range(t), repeat=2):
        q, r = data["q_grid"][i][j], data["r_grid"][i][j]
        assert (q, r) not in edge_id
        original_paths = [(p, l) for l in point_lines[q]
                          for p in line_sets[l] - {q}
                          if r in point_lines[p] and r != l]
        assert original_paths == [(data["anchors"][i], data["anchor_lines"][i])]
        orthogonal = [p for p in sorted(line_sets[r])
                      if symplectic(points[q], points[p], field) == 0]
        assert orthogonal == [data["anchors"][i]]
        c = orthogonal[0]
        connecting_lines = point_lines[q].intersection(point_lines[c])
        assert connecting_lines == {data["anchor_lines"][i]}
        l = data["anchor_lines"][i]
        assert set(f[c]).isdisjoint(f[q])
        assert set(g[l]).isdisjoint(g[r])
        assert set(f[c]).intersection({0, 1}) == {0}
        assert set(g[l]).isdisjoint({0, 1})

        six = (selected[1+i], selected[0], selected[1+t+j],
               edge_id[q, l], edge_id[c, l], edge_id[c, r])
        assert len(set(six)) == 6
        left_degree = Counter(x for eid in six for x in f[inc[eid][0]])
        right_degree = Counter(y for eid in six for y in g[inc[eid][1]])
        # These sixsets are outside all seven selected classes, structurally.
        assert sorted(left_degree.values()) == [2, 2, 2, 2, 4]
        assert sorted(right_degree.values()) == [2, 2, 2, 2, 2, 2]
        closed_physical_profiles["five_left_six_right"] += 1

    # Direct physical definition-level enumeration of the ENTIRE selected
    # paired graph, not merely the prescribed central rectangle.
    families, oriented_squares, paths = set(), 0, 0
    for u, nu in adjacency.items():
        assert len({x for x, y in nu}) == len(nu)
        assert len({y for x, y in nu}) == len(nu)
        for v in nu:
            first, last = sorted(nu - {v}), sorted(adjacency[v] - {u})
            for w, z in product(first, last):
                paths += 1
                assert len({x for x, y in (w, u, v, z)}) == 4
                assert len({y for x, y in (w, u, v, z)}) == 4
            for wi, wk in combinations(first, 2):
                for zj, zl in combinations(last, 2):
                    assert provenance[tuple(sorted((u, v)))] == selected[0]
                    ids = tuple(sorted(provenance[tuple(sorted(e))] for e in
                                       ((u, v), (u, wi), (u, wk), (v, zj), (v, zl))))
                    assert len(set(ids)) == 5
                    assert len({inc[e][0] for e in ids}) == 5
                    assert len({inc[e][1] for e in ids}) == 5
                    families.add(ids)
                    oriented_squares += 1
    expected = comb(t, 2)**2
    assert len(families) == expected
    assert oriented_squares == 2*expected
    assert paths == 2*t*t

    # Third method: prior source-provenance oracle, on this NEW global map.
    cl, cr = [0]*a, [0]*a
    for colors in (cl, cr):
        colors[1] = 1
        for i in range(t):
            colors[2+i] = 1
    old_oracle = OriginalPlaquette(model, selected, cl, cr).census(
        max_paths=10_000, max_plaquettes=50_000,
        independent_paths=True, independent_plaquettes=True)
    assert old_oracle["all_four_internally_blocked_plaquettes"] == 2*expected
    assert old_oracle["internally_blocked_end_clean_weight"] == "1"
    assert old_oracle["stationary"] is False
    assert old_oracle["raw_nb_weight"] == "2"
    palette = [w for w in product(range(1, 5), repeat=4) if sum(w) % 5 == 4]
    assert len(palette) == 51
    return dict(s=s, a=a, t=t, original_V=model["v"], original_N=model["N"],
                complete_global_injections=True,
                middle_original_incidence_id=selected[0],
                selected_original_source_count=len(selected),
                paired_physical_edges=len(provenance),
                local_min_active_degree=min(map(len, adjacency.values())),
                proper_NB3_paths=paths,
                original_and_algebraic_anchor_checks=t*t,
                all_blocked_distinct_five_source_sets_at_one_middle=len(families),
                all_blocked_oriented_squares=oriented_squares,
                independent_prior_oracle_all_blocked_squares=
                    old_oracle["all_four_internally_blocked_plaquettes"],
                closure_profiles=dict(closed_physical_profiles),
                nonzero_checksum4_GF5_palette_size=len(palette),
                high_degree_EICE002_Gstar=False,
                root_A_proved=False, root_B_proved=False)


def main(output_dir=None):
    outdir = Path(output_dir) if output_dir is not None else Path("/tmp/issue230-local-capacity")
    outdir.mkdir(parents=True, exist_ok=True)
    reports = []
    for power, t in ((2, 2), (3, 8)):
        field, model, data = construct(power, t)
        report = validate(field, model, data)
        certificate = {"model": model,
                       "construction": {k: v for k, v in data.items()
                                        if k not in ("point_lines", "line_sets")},
                       "report": report}
        encoded = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
        filename = outdir / f"capacity_w3_{model['s']}.json"
        filename.write_bytes(encoded)
        report["certificate_sha256"] = hashlib.sha256(encoded).hexdigest()
        reports.append(report)
        print(json.dumps(report, sort_keys=True), flush=True)
    (outdir / "capacity_results.json").write_text(
        json.dumps(reports, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
